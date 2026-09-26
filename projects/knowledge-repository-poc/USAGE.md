# Knowledge Repository — How to Use

The repository is a co-occurrence hypergraph over your research corpus
(markdown + OpenAlex bibliographic records + full-text articles), served by
typed pipelines (`plumbing`). It exists so claims can be *grounded* in
`doc :: section` evidence instead of unverified recollection.

This guide assumes you're at the repo root: `~/Documents/Research`.

---

## 1. One-time setup

```bash
devenv shell          # enter the Nix environment (utils + uv + pinned CPython)
uv sync               # provision .venv from uv.lock (or: uv sync --frozen)
```

That's it. `uv.lock` is committed, so any clone/colleague gets the same
dependency graph. `requirements.txt` no longer exists — the lockfile is the
source of truth.

---

## 2. Minimal workflow (60 seconds)

```bash
# Rebuild the hypergraph from the current corpus
uv run python projects/knowledge-repository-poc/scripts/pipeline.py ingest 'null'

# Ground a claim: which sections co-occur with my seed concepts?
uv run python projects/knowledge-repository-poc/scripts/pipeline.py trace_report '{"topic":"How does tau->0 relate to the SK condition?","concepts":["tau_J","SK condition","gravitation"],"min_seeds":3}'
```

The second command prints a markdown evidence trace: every hyperedge (document
section) containing ≥ 3 of your seeds, ranked. Cite those sections.

---

## 3. What the pipelines do

All pipelines take a JSON string on the command line and print a JSON result
(or markdown). The plumbing runtime type-checks the boundaries — malformed
input fails with a clear message. **Records must be complete**: every field in
the pipeline's declared type is required (e.g. `expand`/`fulltext` need all
four/five fields — see the table; `ingest` takes exactly `null`).

| Pipeline | Purpose | Example input |
|---|---|---|
| `ingest` | Rebuild the hypergraph | `null` (unit) |
| `query` | Sections containing a concept | `{"concept":"Cattaneo"}` |
| `evidence` | Markdown evidence bundle for a concept | `{"concept":"Cattaneo","max_edges":10}` |
| `trace` | Structured intersection reasoning | `{"topic":"...","concepts":["a","b"],"min_seeds":2}` |
| `trace_report` | Markdown version of `trace` | same |
| `expand` | Pull works from OpenAlex (bibliographic truth) | `{"mode":"doi","topic":"","limit":5,"doi":"10.3390/..."}` |
| `fulltext` | Download OA full text → markdown (docling); or convert a locally-staged PDF (`mode:"local"`) | `{"mode":"corpus","doi":"","limit":5,"refresh":0,"strict":1}` |

Run any of them with:

```bash
uv run python projects/knowledge-repository-poc/scripts/pipeline.py <name> '<json>'
```

### Modes detail

- **`expand`** modes: `topic` (search, `{"mode":"topic","topic":"...","limit":5,"doi":""}`), `doi`,
  `arxiv`. Writes to `corpus/external/<openalex_id>.json` (idempotent — skips
  existing).
- **`fulltext`** modes: `doi`, `corpus`, and `local`. Full record:
  `{"mode":"...","doi":"...","limit":N,"refresh":0,"strict":1}`.
  `strict:1` (default) only downloads permissively-licensed locations
  (`cc-*`, arXiv, green OA). Writes markdown to `corpus/fulltext/`; PDFs are
  staged in `papers/incoming/`. Note: many publisher hosts bot-gate their PDFs
  (403/Radware), so reliable *downloaded* coverage is archive-hosted OA
  (arXiv) — which is exactly when you fall back to `mode: "local"`.

### Manually downloading a full-text PDF and converting it

Publishers blocking auto-downloads (403/Radware on MDPI, Springer, IOP,
Wiley, ScienceDirect) are the common case. The workflow: get the PDF yourself,
stage it, and let the pipeline convert it with `mode: "local"`.

1. **Download the PDF by hand** (e.g. from the publisher or a colleague) and
   save it to `papers/incoming/` with the right key name. The key is the
   `openalex_id` if OpenAlex knows the DOI, else `doi_<sanitized-doi>`:

   ```bash
   # a DOI that IS in OpenAlex -> key is the openalex id (e.g. https_openalex.org_W4404111866)
   # a DOI OpenAlex does not know -> key is: doi_10_9999_my_doi
   # simplest: run the pipeline once; the error message tells you the exact expected filename
   ```

2. **Convert it:**
   ```bash
   uv run python projects/knowledge-repository-poc/scripts/pipeline.py fulltext \
     '{"mode":"local","doi":"10.3390/en17225541","refresh":0,"strict":1}'
   ```
   Expect `{"mode":"local","found":1,"converted":1,...}` and a markdown file at
   `corpus/fulltext/<key>.md`.

   If the stage filename is wrong, the worker reports
   `FileNotFoundError: papers/incoming/<key>.pdf not found` — rename to that
   exact name (rerun `fulltext` in `doi` or `corpus` mode once if you need the
   key for an OpenAlex-known DOI).

3. The conversion uses docling with **OCR and table-structure disabled**
   (born-digital text PDFs don't need either; it also avoids the
   rapidocr+torch native crash and a libxcb dependency that this stack
   otherwise trips). Scanned PDFs and table-heavy layouts are out of scope —
   route those to a full docling pipeline instead.

---

## 4. Growing the corpus

1. Add any markdown repo (e.g. a new research thread) to `corpus.json` under
   `roots`.
2. Optionally expand metadata from OpenAlex: `expand` with a topic or DOI.
3. Optionally fetch OA full text: `fulltext`.
4. `ingest` to rebuild. The fast path only rebuilds when a file changed
   (content-hash in `graph/build_meta.json`).

---

## 5. The grounding skill

If you're using opencode/LLM pairing, the `hypergraph-grounding` skill
(`projects/knowledge-repository-poc/skills/hypergraph-grounding/SKILL.md`)
teaches agents when to query the repository and how to cite provenance. Load it
whenever claims should be traceable to corpus sections.

---

## 6. Local verification (smoke) and CI

```bash
uv run python projects/knowledge-repository-poc/scripts/smoke.py
```

Runs 12 checks: stack imports, one worker smoke per contract, pydantic
rejection paths, and build determinism. This exact script runs in CI on every
push/PR (`.github/workflows/stack.yml`). If it's green locally, the pipeline
contracts hold.

---

## 7. Artifacts and layout

```
projects/knowledge-repository-poc/
  corpus.json        # manifest: roots + external OpenAlex dir
  corpus/external/   # OpenAlex work records
  corpus/fulltext/   # converted OA article markdown
  scripts/           # JSON-Lines workers + schemas.py (pydantic contracts)
    schemas.py       # the Python-side type boundary (mirrors .plumb types)
  pipelines/*.plumb  # typed plumbing pipelines
  bin/tara-python    # interpreter shim (uv-managed venv)
  graph/             # hypergraph.json + index.json + provenance.tsv + stats.json
  skills/            # hypergraph-grounding skill
```

---

## 8. Gotchas

- **Interpreter**: workers run through `bin/tara-python` (the uv-managed
  python). Run everything with `uv run`; don't call `python3` pip-installed
  scripts directly.
- **`tools/plumbing`**: the pipeline runtime lives at `~/tools/plumbing` (Nix
  source build). PyPI wheels of plumbing are broken — don't use them.
- **`id` is reserved**: records can't have an `id` field.
- **Data flow**: pipelines assume cwd `pipelines/` internally — the
  `pipeline.py` runner handles this; don't hand-run the `.plumb` workers from
  arbitrary cwds.
- **LLM**: no provider key is set, so the pipeline-internal `agent` is
  key-gated. The opencode-side pairing (skill + reports) works without one.