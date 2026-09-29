# Workspace Architecture Review — 2026-09-27

Prompted by Brad's four questions: (1) does infrastructure belong in the same
directory as research outputs? (2) global `papers/` or per-project? (3) full
review + maintenance recommendations; (4) should research-assistant output live
in the same repo as the assistant code?

## 1. What actually exists today (measured, not remembered)

| Path | Role | Tracked? | Size |
|---|---|---|---|
| `AGENTS.md`, `to_human/` | workspace threads + human notes | yes | tiny |
| `projects/ret-tssi-value-dynamics/` | research thread (output) | yes | small |
| `projects/island-digital-twin/` | research thread (1 lit review) | yes | tiny |
| `projects/knowledge-repository-poc/` | **the research assistant** (scripts, pipelines, bin, skills) + its **data** (corpus/, graph/) + notes | yes | 2.9 MB |
| `papers/` | raw-PDF staging for the assistant (`fetch_fulltext.py` hardcodes `<repo>/papers/incoming/`), plus ad-hoc PDFs | **no** (`incoming/*`, `processed/` ignored) | 16 MB |
| `writing/human/` | personal project transcripts | **23 tracked files** | **236 MB** |
| `archive/` | retired threads | no | 27 MB |
| `devenv.nix`, `pyproject.toml`, `uv.lock`, `.github/` | environment + CI | yes | small |
| `package.json` + `node_modules/` | exists **only** for `@anyproto/anytype-mcp` | package.json yes, node_modules ignored | 43 MB |
| `knowledge-repository-proposal.md` | thread-2 rethink doc | yes | 16 KB |
| `.enc.env` (sops-encrypted) + `.sops.yaml` | secrets, correctly | yes | tiny |
| `~/tools/plumbing` | the other half of the assistant, **outside the repo entirely** | no | — |

56 commits, 154 tracked files, ~230 MB of tracked payload of which **~205 MB is
audio (`.m4a`) and raw transcript JSON in `writing/human/`**.

## 2. Direct answers

**Q1 — agent infrastructure inside `projects/` with the research outputs?**
No — it's a category error that's now Showing wear. `knowledge-repository-poc`
started as a *research question* ("does the hypergraph+repository idea work?"),
but it graduated: it has CI, a smoke suite, validated worker contracts, and it
serves all other threads. Meanwhile true research threads sit beside it (and a
new one — Means of Production — is coming). Today's git policy flip
(default-track `projects/`) increases the odds that any junk dropped under
`projects/` gets committed. The memo's three threads are **outputs**; the machine
that ingests/grounds them is **infrastructure**; they grow at different rhythms
(code churns per session; corpus changes at checkpoints) and different "done"
criteria (tests vs. prose review).

**Q2 — global `papers/` vs per-project?**
The current `papers/` works because it is really a **global raw-PDF cache** (the
assistant stages `<repo>/papers/incoming/<key>.pdf`; keys are OpenAlex work IDs,
which are global identity, not project identity). Duplicating that per project
would fork the key scheme and re-download the same arXiv PDFs. Per-project only
what is *derived and citable* — which already exists and is already per-project
(`projects/knowledge-repository-poc/corpus/fulltext/*.md`, committed; the raw
PDFs are not). **Keep global staging (raw, untracked); keep derived text
per/consumed-by the corpus (tracked).** One caveat: untracked PDFs can die with
the disk, so anything cited in a committed doc should have a tracked note or
keyed OpenAlex record behind it, not just the PDF.

**Q4 — assistant output in the same repo as assistant code?**
For now, **yes** — deliberately. The POC's whole point is **provenance by
construction**: a commit pins prompt/pipeline code, the corpus record produced,
and the grounded-looking artifacts together; the smoke suite asserts
build-*determinism* against byte-identical hypergraph builds; grounding notes
cite `doc :: section`. That consistency argument is load-bearing for this repo
and dissolves if outputs move to a second repo. The cost side (bloat/noisy
diffs) is managed by policy, not by moving: commit derived artifacts at
checkpoints, not per rebuild (the churn-prone files are graph/*.json + corpus/
md never get itself rebuilt); keep bulk media and raw caches out.
**When to reconsider:** if the assistant ever gets reused by others (packaged,
reused as a library), split `infra/` into its own repo *then* — solo research
today pays more friction than it gains.

## 3. Findings — things the questions didn't ask but belong in the review

Ranked by cost-benefit.

1. **Nothing else is as important as this: 205 MB of personal audio is in git.**
   `writing/human/*.m4a` (Informatics1–4, up to 90 MB each) plus raw `.json`
   transcripts are committed to a **public** repo (`bvenner/tara`). They're
   permanent forever — the largest payload is already in history (untracking
   prevents future growth, but the history's already paid at ~230 MB). Also: The
   **Means of Production Working Group** — DSA organizing material — is in the
   same otherwise-public repo, as are class transcripts `remnants-of-a-project-long-gone.md".
   Decide: (a) is this repo *for* publishing research writing, or a
   public-facing portfolio/organizing presence? (b) if not, these files should
   move out or the repo goes private. This is a content/privacy decision, not a
   plumbing one.
2. **AnyType debris** (decommissioned thread): `package.json` +
   `node_modules/` (43 MB) exist only for `@anyproto/anytype-mcp`; AGENTS.md
   itself says the MCP "now failing — decommission". Delete both, drop the MCP
   server from `opencode.jsonc`. None of the AnyType *history* needs deletion —
   that already lives in `archive/` (correct per convention).
3. **Infra/outputs boundary is real even inside the POC**: `scripts/`, `bin/`,
   `pipelines/`, `skills/` are code; `corpus/`, `graph/`, `notes/`, `REPORT.md`
   are artifacts. A clean day-light lines: **`infra/knowledge-repository/`**
   wholesale move — internals use `__file__`-relative paths, so a wholesale
   move keeps internals working; what actually breaks is only the *external*
   references (opencode.jsonc `skills.paths` + MCP wrapper path, CI path
   `python projects/knowledge-repository-poc/scripts/smoke.py`, AGENTS.md
   paths). Recommend doing this as ONE move+grep-audit commit when ready, not
   piecemeal.
4. **Root `knowledge-repository-proposal.md`** is the only tracked root-level
   "thread" doc; harmless, but if the assistant moves to `infra/`, this doc
   should move with it (one line in AGENTS.md updates).
5. **`to_human/` vs per-project `to_human/`** (ret-tssi has its own) is
   slightly inconsistent (one thread has it, others don't). Fine to leave; just
   decide the rule ("workspace-level notes only in root to_human").
6. **`projects/means-of-production-working-group/`** — when this new project
   materializes (see §4 proposal), it slots into the default-track rule
   established 2026-09-26 (no .gitignore edit needed anymore).

## 4. Target layout (Option 1, recommended: monorepo with clean seams)

```
bvenner/tara/
├── AGENTS.md                     # threads + resume paths (updates: paths below)
├── infra/
│   └── knowledge-repository/     # ← today's projects/knowledge-repository-poc/
│      ├── scripts/ bin/ pipelines/ skills/   (code)
│      ├── corpus/ graph/                     (data, committed at checkpoints)
│      └── notes/ REPORT.md USAGE.md
├── projects/                     # research OUTPUT threads only
│   ├── ret-tssi-value-dynamics/
│   ├── island-digital-twin/
│   └── means-of-production-working-group/   (new; AGENTS.md + proposal)
├── papers/                       # global raw-PDF cache — untracked, by design
├── writing/                      # prose; **media files untracked** (git-lfs if ever needed)
├── to_human/                      # cross-thread human notes only
├── devenv.nix / pyproject.toml / uv.lock / .github/   # untouched
```

What does **not** change: the single uv-managed env, the single CI, the single
PR/branch story, `archive/` policy, plumbing remaining at `~/tools/plumbing`
(out-of-repo is actually *good* — it's a separate codebase with its own AGENTS).

If the assistant ever needs to be shared, Option 2 is `infra` as its own repo +
this repo consuming it via a pinned rev — deliberately deferred (per Q4).

## 5. Recommended actions (ordered, with risk)

| # | Action | Risk | Effort |
|---|---|---|---|
| 1 | `git rm --cached` the `writing/human/*.m4a` + raw transcript JSONs; add `writing/human/*.m4a` (and `.json` raws) to `.gitignore` | LOW | 5 min |
| 2 | Decide §3.1 (audio privacy / public-repo content) — **your call**, changes everything downstream | decision | — |
| 3 | Prune AnyType: delete `package.json`, `node_modules/`, drop `anytype` MCP from `opencode.jsonc` | trivial | 10 min |
| 4 | Move POC → `infra/knowledge-repository/` (wholesale) + audit the ~5 external path references (opencode config ×2, CI ×1, AGENTS.md, docs) | medium | 30–60 min |
| 5 | Scaffold `projects/means-of-production-working-group/` (AGENTS.md resume path + move the proposal into the project; register in root AGENTS.md) | trivial | 10 min |
| 6 | (later, when infrastructure graduates from POC–vocab) repo-split re-review of Q4 | decision | — |

Items 1, 3, 5 are safe today. Item 4 is the real restructure — do it when the
next change touches the POC anyway. Item 2 gates nothing technically but colors
everything.

## Appendix — facts this review is based on

- Tracked payload: `git ls-files` (154 files) + sizes; audio files dominate.
- Root .gitignore already ignores `papers/incoming/*.pdf`, `papers/processed/`,
  `node_modules/`, `.devenv/`, `archive/`, `data/`.
- `fetch_fulltext.py`, `smoke.py`, `USAGE.md` hardcode `papers/incoming` (global
  cache works because of this).
- Sops secrets (`​.enc.env`) tracked — encrypted, no cleanup needed.
- `opencode.jsonc` still wires the decommissioned anytype MCP; only `ret-tssi`
  AGENTS.md is listed in `instructions` (other threads have project-level
  AGENTS.md files, discovered contextually — fine but worth documenting).

## Addendum — 2026-09-28 (execution status)

- Action 1 (untrack media) **done** — commit `e42fafc`.
- Action 3 (AnyType prune) **done** — commit `01f6e17`; the Appendix claim that
  `opencode.jsonc` still wires the anytype MCP was stale: no anytype entry
  existed in the root, repo-local, or global opencode config by execution time.
- Action 5 (scaffold `projects/means-of-production-working-group/`) **declined
  for now** — the proposal deliberately stays in `writing/human/` until Brad
  decides to promote it to a project thread.
