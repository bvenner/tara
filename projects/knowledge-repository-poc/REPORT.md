# Knowledge-Repository POC — Phase A, Step 1

**Co-occurrence hypergraph over the RET × TSSI corpus** — built 2026-08-23, no LLM involved.

## Method

Node rule (**co-occurrence v1**): nodes are
- `section` — every markdown heading in the corpus
- `keyword` — RAKE keyword phrases (deterministic, per document top-15 + per section top-6)
- `citation` — bibliography entries from `program/references.bib` (74 keys), matched in-text by author-year
- `artifact` — theorem tags T1–T4 and Track A–F
- `notation` — curated spine tokens: gravitation, Cattaneo, simultaneism, SK condition, τ_J, subcharacteristic, Fourier, MELT

Hyperedge rule: within each document section, the set of concepts present (arity ≥ 2) is one hyperedge. Provenance is recorded per hyperedge (source doc + section).

## Corpus

32 markdown documents (program doc, critiques, findings, 26 literature notes, research log, to_human notes) across 116 sections; `references.bib` for citation entities.

## Results

| Metric | Value |
|---|---|
| Nodes | 396 (231 keyword · 116 section · 31 citation · 10 artifact · 8 notation) |
| Hyperedges | 114 (arity 2–16) |
| Max / mean degree | 33 / 1.87 (heavy-tailed; leaf-dominated) |
| Degree ≥ 9 nodes | 15 |

Top hubs (hyperedge degree):

| Node | Kind | Degree |
|---|---|---|
| gravitation | notation | 33 |
| Cattaneo | notation | 30 |
| simultaneism | notation | 29 |
| SK condition | notation | 26 |
| T3 | artifact | 23 |
| τ_J | notation | 20 |
| Track B / T4 / Track A / Track C | artifact | 17 |
| subcharacteristic | notation | 13 |
| T1 | artifact | 13 |
| Fourier | notation | 11 |

The hub structure matches the program's intellectual spine (the correspondence: gravitation ⇄ Cattaneo ⇄ simultaneism, with SK condition / τ_J / the theorem set as the technical core) — a sanity signal that section-level co-occurrence already recovers the corpus's central structure.

## Artifacts (`graph/`)

- `hypergraph.json` — `V` (node list), `E` (hyperedge member lists), `hyperedges` (full records with `doc`/`section` provenance). Shape is HNX-loadable (`Hypergraph(V, E)`).
- `provenance.tsv` — per-hyperedge `edge_id / doc / section / arity`.
- `stats.json` — full counts, arity histogram, degree distribution, hub table.

## Rebuild

```
python scripts/build_hypergraph.py            # ≥ Py3.10, stdlib only
```

## Next

- **Step 2 ✅ — plumbing pipelines + MCP wiring** (2026-08-23). Three typed pipelines in `pipelines/`, backed by JSON-Lines workers over the graph artifact via plumbing's `exec` primitive; exposed to opencode via `plumb-mcp`.

### Pipelines (`pipelines/`)

| Pipeline | Input | Output | Purpose |
|---|---|---|---|
| `ingest.plumb` | `null` | `{docs,nodes,edges,mean_degree,max_degree}` | Rebuild the co-occurrence hypergraph from the corpus (`build_hypergraph.py --compact`) |
| `query.plumb` | `{concept}` | typed `QueryResult` record | Concept → matching hyperedges with `doc`/`section` provenance |
| `evidence.plumb` | `{concept, max_edges}` | `string` | Markdown evidence bundle for agent grounding |

Workers: `scripts/graph_query.py` (JSON Lines in/out, resolves the graph relative to its own file) and `build_hypergraph.py --compact`.

### MCP wiring

- `plumb-mcp-wrapper.sh` runs the nix-built `plumb-mcp` with cwd = `pipelines/` (so `exec` relative paths resolve); registered as the `plumb` MCP server in `opencode.jsonc`.
- Verified: `opencode mcp list` → `plumb ✓ connected`; raw JSON-RPC handshake served `check` + `call` and a `call` of `query.plumb` returned the query result.

### Verified behavior

- `ingest`: rebuild → `{"docs":32,"nodes":396,"edges":114,"mean_degree":1.874,"max_degree":33}`.
- `query`: `{concept:"cattaneo"}` → 5 matched nodes (notation + section + 2 keywords + citation), 30 edges with provenance; `{concept:"pineapple"}` → empty result.
- `evidence`: `SK condition` → bundles the corpus's core sections (§4 Track A, §1 Overview, §3 correspondence) as markdown.
- Boundary rejection: a non-object into `query.plumb` fatals the `exec` morphism before the worker runs.
- `plumb-check`: all three pipelines pass (`query`: 3 types, 2 bindings).

### Step 2 gotchas (learned)

- `id` is a reserved token in plumbing (the identity morphism) — record fields must not be named `id` (renamed to `node_id`/`edge_id`).
- `exec` input-type failure fatals the morphism without the detailed `input_type_mismatch` diagnostic that `map` emits — still a hard rejection.
- Pipelines assume cwd = `pipelines/` (the wrapper provides it); relative `../scripts/...` paths resolve from there.

## Next

- **Step 3 ✅ — agentic reasoning pass (hyperedge intersection)** (2026-08-23). Two new pipelines, `trace.plumb` (structured `Trace`) and `trace_report.plumb` (markdown), implement hyperedge-intersection reasoning: given seed concepts, keep only hyperedges where ≥ `min_seeds` co-occur. This is the "node-intersection as a verifiable guardrail" move from the HGR methodology, done with no LLM.

### The demo question

> How does the τ→0 relaxation limit relate to the SK condition for gravitation convergence?

Seeds: `[tau_J, sk condition, subcharacteristic, gravitation, T3]`, `min_seeds = 3`. Result: **14 intersecting hyperedges across 14 sections**, ranked by seed count then arity:

| Rank | Seeds | Sec. | Location |
|---|---|---|---|
| 1 | all 5 | §4 Track A | `research-program.md` — the hyperbolic value-price system |
| 2 | 4 | §5 | `findings.md` — model skeleton (T1–T4, Cattaneo closure) |
| 3 | 3+ | §3 | `research-program.md` — the core correspondence table |
| … | 3–4 | §6/7/8 | `proposal-walkthrough.md` — math / economics / CS explainers |
| … | 3 | §4 | `findings.md` — correspondence table · §A1 critiques · §9 landmarks |

The trace recovers precisely the sections that jointly ground the answer (Track A formulation → model skeleton → correspondence → walkthrough treatments), with full provenance per hyperedge. Artifact saved at `graph/evidence-trace-tau-sk.md`.

### Step 3 gotcha

Worker `graph_query.py` gained `--mode trace` / `--mode trace-text` (JSON-Lines in/out, exact-field record output so the `Trace` boundary type checks). `si`-based per-seed indexing, dedup by edge id, ranked output — all deterministic, no LLM.

## Next

- **Phase B ✅ — multi-project corpora, OpenAlex expansion, richer kinds, incremental fast path** (2026-08-23).

### Corpus manifest (`corpus.json`) — build is now manifest-driven

Three roots + external works: `ret-tssi` (recursive `**/*.md`), `poc` (the POC's own docs), `top` (repo-root proposal), plus `corpus/external/*.json` OpenAlex records. Adding a project = adding one manifest entry.

### Pipelines

- New `expand.plumb` — OpenAlex expansion worker (`scripts/expand_openalex.py`, reusing the repo's `scripts/lib/openalex_client.py`), modes `topic` / `doi` / `arxiv`, reconstructs abstracts from `abstract_inverted_index`, idempotent writes.

### Growth (rebuilt graph)

| Metric | Phase A | Phase B |
|---|---|---|
| Docs | 32 | 45 (3 more roots + 10 external works) |
| Sections | 116 | 162 |
| Nodes | 396 | 636 |
| Node kinds | 5 | 8 — adds `project` (4), `author` (74), `work` (10) |
| Hyperedges | 114 | 162 |

Hub structure is preserved (gravitation 36, Cattaneo 34, simultaneism/SK/τ_J follow); `project:ret-tssi` is now the top hub (every ret-tssi section carries it). Trace on the τ→0/SK question grew 14 → 17 hits (now also covering `poc/REPORT.md`), still headed by `program §4 Track A`.

### New capability demonstrated

`query {concept:"foley"}` now returns both the citation node `foley1994 (1994)` **and** the author node `Duncan K. Foley` — the OpenAlex work + author kinds are first-class in the repository.

### Incremental fast path

`build_meta.json` stores the manifest sha + per-doc content hashes; an unchanged corpus reuses the stored summary without rewriting artifacts (`--force` to override). At this corpus size rebuilds are ~instant, but the pattern scales.

### OpenAlex expansion run (this build)

Topic "extended thermodynamics relaxation" (8 works) + DOIs for Foley 1994 (JET), Wright 2005 (Physica A), Jou/EIT 1988 — 11 ingested, 1 deduped (idempotency verified).

## Next

- **OpenCode-side LLM pairing ✅ implemented (2026-08-23)** — no provider key needed.

The LLM stays in opencode (the agent already runs on a model); plumbing remains
mechanical (grounding). Two equivalent ways to pull repository evidence:

1. **MCP:** `plumb:call` with `{source, input}` (server registered in `opencode.jsonc`).
2. **bash helper:** `python projects/knowledge-repository-poc/scripts/pipeline.py <name> '<json>'` (always available; mirrors `call`).

Demonstrated end-to-end: the τ→0/SK question was answered by the opencode agent
synthesizing *only* from the trace output, with per-claim `doc :: section`
citations — saved as `graph/grounded-answer-tau-sk.md`. A repo **skill**
(`skills/hypergraph-grounding/SKILL.md`, registered via `opencode.jsonc`
`skills.paths`) teaches future sessions when/how to ground answers, cite
provenance, and regenerate after corpus edits.

Also fixed in this pass: bibliography author extraction now drops single-letter
tokens (cleaner author hyperedges).

## Next

- **Full-text ingestion (C1, 2026-08-23).** New `pipelines/fulltext.plumb` +
  `scripts/fetch_fulltext.py`: download openly-accessible articles, convert to
  markdown (docling), write to `corpus/fulltext/<openalex_id>.md`, then the
  existing builder ingests them via the new `fulltext` corpus root. Strict
  licensing default (cc-*/arXiv/green). Input `{mode: doi|corpus, doi, limit,
  refresh, strict}`; summary `{found, downloaded, converted, skipped, reasons}`.

**Verified:** types-checked; worker converts PDF→markdown with a provenance
header (source URL, DOI, license, status) preserving section headings that the
hypergraph splits on. Corpus run over all 29 external records downloaded 5
arXiv-hosted works, converted all 5 (physics reviews), skipped the rest with
per-record reasons (bot-gated publisher CDNs: MDPI/Springer/IOP/Wiley/ScienceDirect
all 403/Radware/HCaptcha; strict-license rejections; closed works).

**The operational finding:** archive-hosted OA (arXiv) is reliably fetchable;
publisher `best_oa_location` PDFs are bot-gated (403 at the CDN, headers don't
help), so full-text coverage effectively = arXiv/green copies. The hypergraph
rebuild reflects it: 5 full-text docs → sections 198→448, nodes 865→1874,
edges 198→448 (whole-paper co-occurrence, not just abstracts). The island-DT
grounding trace is unchanged (13/13) — the converted works are physics reviews,
as expected for this batch.

## Next

- **Out-of-sample test: "island digital twin" (2026-08-23).** A fresh research question on a topic the corpus had never touched — island metabolism × local digital twins (see `projects/island-digital-twin/literature-review.md`).

**What was done:** added `island-dt` to the corpus manifest; ingested 19 DOI-keyed sources via the `expand` pipeline (OpenAlex); rebuilt. Graph: 65 docs / 864 nodes / 197 hyperedges / 5 projects / 29 works / 126 authors. OpenAlex metadata also verified several items that the review had flagged (e.g., Helsinki B5 = Airaksinen & Rossknecht; New Caledonia = Bahers, Ventura, Antheaume et al.).

**The measurement that matters:** grounding trace on the composed question at `min_seeds=2` produced **2 hits, both within the 3D/energy pillar** — single-abstract co-occurrence hyperedges do **not** intersect across pillars (metabolic ↔ twin ↔ participatory). At `min_seeds=1` (evidence bundle = union over seeds) the repository assembles **13 sections across all four pillars**, saved as `graph/evidence-trace-island-dt.md`. This is the workflow-value test paying off: for cross-pillar questions, co-occurrence-within-section is a *precision* tool, not a *recall* tool.

**Decision signal:** the union-as-evidence-bundle already works; **embeddings (semantic neighborhoods)** would be the principled recall-widening to make a fresh cross-domain question assemble at higher min-seeds — the "embeddings vs Phase C" question now has corpus-side evidence pointing toward embeddings if cross-pillar assembly matters.

## Next

- **Pydantic worker contracts (2026-08-25).** New `scripts/schemas.py` is the
  canonical Python-side mirror of every `.plumb` exec boundary: `ExpandRequest/
  ExpandSummary`, `FulltextRequest/FulltextSummary`, `QueryRequest/QueryResult`
  (+ NodeRef/Edge), `TraceRequest/TraceResult` (+ Seed/Hit), `IngestSummary`.
  All four workers validate requests on entry (exit with a clear pydantic
  ValidationError — the field, offending value, and rule — instead of failing
  downstream as a silent undefined-behaviour or `morphism_fatal`) and validate
  before emit. All seven exec workers now run via `bin/tara-python` (the
  uv-managed interpreter), since pydantic lives in the uv venv; the previously
  fatal `ingest`/`trace_report` runtime paths are confirmed working.

  Verified: query/evidence/trace/trace_report/expand/fulltext/ingest all run
  through the plumb runtime; rejection paths produce clean ValidationErrors
  (empty concept, negative limit, empty concepts list); build stays
  byte-deterministic; all pipelines type-check; `uv lock --check` clean.

## Next

- **Smoke + CI (Phase 5, 2026-08-25).** `scripts/smoke.py` runs the cheap,
  deterministic Job-1 checks: stack imports (docling/torch/pydantic/requests),
  one worker smoke per contract (query/evidence/trace/trace-report/expand/
  fulltext-skip/ingest), the three pydantic rejection paths, and build
  determinism (two `--force` builds → byte-identical `hypergraph.json`).
  Wired into `.github/workflows/stack.yml` (push + PR): `uv lock --check`,
  `uv sync --frozen`, then the smoke. Nix/plumbing pipeline type-checking
  stays a manual/Job-2 item (runner-side nix eval is the flaky part). Run
  locally: `uv run python projects/knowledge-repository-poc/scripts/smoke.py`.

## Next

- **Pipeline-internal LLM** (still key-gated): an `agent` binding after `trace`, for when a provider key is available — repository stays the guardrail; the LLM renders the argument inside the pipeline.
- **Embeddings** for semantic neighborhood queries (beyond substring matching).
- **Phase C** (persistent query service / review protocols / dashboard) only if file-based serving proves insufficient.