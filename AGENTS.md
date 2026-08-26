# TARA Research Workspace — AGENTS.md

Multi-thread workspace (public GitHub repo `bvenner/tara`). Four live threads; each has a resume path. **After any context reset, read `to_human/2026-08-23-context-preservation.md` first** (full detail), then each thread's entry point.

## Threads (resume paths)

1. **RET × TSSI research program** (finished delivery; academic program doc) — `projects/ret-tssi-value-dynamics/AGENTS.md` → program docs, critiques, references.bib, walkthrough. Master's sub-problem M1–M6 still open (default M1).
2. **Knowledge repository** (active infrastructure: hypergraph + plumbing) — `knowledge-repository-proposal.md` (3 recorded decisions at top), authoritative status: `projects/knowledge-repository-poc/REPORT.md`. Everything is committed & reproducible.
3. **Island Digital Twin** (active new research question) — `projects/island-digital-twin/literature-review.md`; corpus ingested into the repository; grounding tested (`graph/evidence-trace-island-dt.md`).
4. **AnyType elimination** (superseded by #2; keep as-is) — `archive/projects/anytype-based-tara/eliminate-anytype-plan.md` (Phase 0 export done to `data/tara_graph.db` + dumps).

## Tooling facts (do not re-derive)

- **Python stack: uv-managed** — `pyproject.toml` + committed `uv.lock` are the single source of truth; `devenv.nix` provides the `uv` binary and a pinned CPython 3.13 (nixpkgs-python, needed so binary deps like torch/docling find libstdc++). Provision with `uv sync`; run scripts with `uv run python ...`. `requirements.txt` was deleted — never re-add loose `>=` pins.
- plumbing: **pip wheels are broken** (missing libnorm/libpgm/libsodium soname); use the Nix source build at `~/tools/plumbing` (`nix develop ~/tools/plumbing -c ~/tools/plumbing/_build/default/bin/{plumb,check,render,mcp}/main.exe`). Pipelines assume cwd = `pipelines/`.
- Repository pipeline runner (always available, mirrors MCP `call`): `python projects/knowledge-repository-poc/scripts/pipeline.py <name> '<json>'`. All `exec` workers run through `projects/knowledge-repository-poc/bin/tara-python` (uv-managed interpreter, provides pydantic validated worker contracts in `scripts/schemas.py`).
- OpenAlex client at `projects/knowledge-repository-poc/scripts/lib/openalex_client.py` (4 req/s; abstracts = `abstract_inverted_index`). Expand via `pipelines/expand.plumb`.
- No LLM provider key is set (ANTHROPIC/OPENAI/GOOGLE absent) → pipeline-internal `agent` is key-gated; the **opencode-side pairing works now** (LLM reads the trace, synthesizes, cites `doc :: section`).
- `opencode.jsonc` changed this session: `skills.paths` (hypergraph-grounding skill) + `plumb` MCP server + (pre-existing) `anytype` MCP (now failing — decommission). Requires an opencode **restart** to load.

## Conventions

- Semantic commit prefixes; commit only when asked; never push `main` (feature branch → PR, confirm first); ask before destructive commands / git push|checkout / edits outside this directory.
- Untracked file that must NEVER be committed: `archive/projects/anytype-based-tara/research-assistant-architecture-bcv.md`.
- "Entropy" in program docs = convex Lyapunov structure, not thermodynamic entropy.
- Git: after the collaborator rebase, `main` contains both histories; current work lives on `feat/fulltext-ingestion-v2` (pushed). Push only to feature branches (never `main`).

## Open decisions

- Embeddings (semantic neighborhoods) vs Phase C — corpus evidence (island-DT test) favors embeddings only if cross-pillar recall matters.
- LLM pairing: waiting for a provider key to add a pipeline-internal `agent` binding.
- AnyType decommission (Phase 3) — largely moot after the knowledge-repository rethink; MCP entry still wired.
- RET×TSSI Master's sub-problem: M1 (default) vs M2–M6.
- Push the 9 unpushed commits (feature branch + PR) when confirmed.