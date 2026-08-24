# Context Preservation — 2026-08-23

Full-session state for resumption after compaction/context reset. **Read this first.** Source of truth for procedures/locations: repo-root `AGENTS.md` (auto-loaded); project `AGENTS.md` files; the documents named below.

---

## 1. The four live threads

| Thread | Status | Entry point |
|---|---|---|
| RET × TSSI research program | delivered; program doc finished; Master's sub-problem open | `projects/ret-tssi-value-dynamics/AGENTS.md` |
| Knowledge repository (hypergraph + plumbing) | active infrastructure; Phases A–B done | `knowledge-repository-proposal.md` · `projects/knowledge-repository-poc/REPORT.md` |
| Island Digital Twin | active new research question; literature + corpus + grounding done | `projects/island-digital-twin/literature-review.md` |
| AnyType elimination | superseded by the repository rethink; Phase 0 export kept as safety net | `archive/projects/anytype-based-tara/eliminate-anytype-plan.md` |

Environment facts are in `AGENTS.md` (tooling bullets) and §7 below.

---

## 2. Thread 1 — RET × TSSI research program (stable)

- Six-track program document (`program/research-program.md`), 18 steelmanned critiques (`program/critiques.md`, all amendments applied), 75-entry track-organized `references.bib`, `findings.md`, 26 literature notes, and an **accessible walkthrough** (delivered `to_human/2026-08-16-proposal-walkthrough.md`, incl. a "statistical compass" section using Jaynes' MaxEnt).
- **Open:** Master's sub-problem M1–M6 (`research-program.md §11`); M1 default, M4 low-risk alternative, M5 numerics, M6 formalization. `proposal/masters-proposal.md` (exposé) still to be written once chosen (must not assume value-theory/thermo background; cite Jou (2020) in the intro).
- Git: program + walkthrough were pushed once via feature branch + PR (**PR #2 merged** into `main`).

## 3. Thread 2 — TARA infra & AnyType elimination (mostly superseded)

- Original architecture: `archive/projects/anytype-based-tara/research-assistant-architecture.md` (tracked). The `-bcv.md` draft is **untracked and must never be committed**.
- Migration work that still stands as reference: `scripts/export_anytype.py` (dry-run/--commit/--verify), Phase 0 export (21 AnyType objects → `data/tara_graph.db` tables papers/authors/projects/experiments + markdown/JSON dumps in `data/`). Bugs fixed during that pass: quoted `ANYTYPE_API_BASE_URL` in env breaks the AnyType client; `**Field:**` markdown parser bug; stale `anytype_id` collisions on junk rows 1 & 2 (flagged for cleanup).
- **Superseded by Thread 2 of the rethink:** OpenAlex is the bibliographic ground truth; the SQLite relational direction (Phase 1+ of `eliminate-anytype-plan.md`) is dropped. AnyType is decommission-tracked: MCP entry in `opencode.jsonc` now fails; server may still be running (read-only reference).

## 4. Thread 3 — Knowledge repository (active infrastructure)

- Proposal: `knowledge-repository-proposal.md` — the rethink. **Recorded decisions:** (1) plumbing AGPL-3.0 acceptable now; future interest = strongly-typed host language with native multi-party session types; (2) Phase A corpus = RET×TSSI; (3) **co-occurrence hyperedges first, no LLM** (LLM relation-typing only as measured enrichment).
- **Authoritative status: `projects/knowledge-repository-poc/REPORT.md`.** Architecture:
  - `scripts/build_hypergraph.py` — co-occurrence hypergraph builder (node kinds: section/keyword/citation/artifact/notation/project/author/work), manifest `corpus.json` (roots: ret-tssi, poc, top, island-dt) + external OpenAlex works (`corpus/external/`), **incremental content-hash fast-path** (`graph/build_meta.json`).
  - Artifacts: `graph/hypergraph.json` (HNX-loadable V/E/members), `provenance.tsv`, `stats.json`.
  - Pipelines (`pipelines/`, cwd must be that dir): `ingest` (rebuild), `query`, `evidence`, `trace`, `trace_report` (hyperedge-intersection reasoning), `expand` (OpenAlex). Workers: `scripts/graph_query.py`, `expand_openalex.py`.
  - Integration: `plumb-mcp-wrapper.sh` → `plumb` MCP server in `opencode.jsonc`; bash helper `scripts/pipeline.py <name> '<json>'` (mirrors MCP `call`); **skill** `skills/hypergraph-grounding/SKILL.md` registered via `opencode.jsonc` `skills.paths` (repo `.opencode/` is gitignored, so the committed skill path is required).
  - **OpenCode-side LLM pairing demonstrated:** `graph/grounded-answer-tau-sk.md` (LLM synthesized from trace output only, citing `doc :: section`).
- Phase status: A1–A3 done; B done (multi-project, OpenAlex expansion, authors/works, incremental); opencode-side pairing done. Changed config needs an **opencode restart** (skills + new MCP server don't hot-load).
- **Key measurement (island-DT out-of-sample test):** single-abstract co-occurrence hyperedges are a *precision* tool, not a recall tool — at `min_seeds=2` the composed question grounded only within the 3D/energy pillar; at `min_seeds=1` (union evidence bundle) it assembled 13 sections across all four pillars. **Signal:** if cross-pillar assembly matters, embeddings (semantic neighborhoods) are the principled recall-widening (see §8 decisions).

## 5. Thread 4 — Island Digital Twin (active research question)

- `projects/island-digital-twin/literature-review.md` — 35+ verified sources across four pillars (A island/urban metabolism; B 3D city-model standards; C urban/island digital twins + EU LDT ecosystem; D participatory planning support/geodesign), a synthesis, and the novelty gap: **metabolic MFA/MSA on a CityGML-class 3D island model inside a participatory geodesign workflow** has no published precedent.
- Direct island-twin precedents found: Inishmore P2P energy twin (Buckley et al. 2024, DOI 10.3390/en17225541); Tuvalu/Grenada SIDS adaptation twins (grey lit); Culatra grid twin; Kefalonia ARGOS (open-source). Standards bridge: CityGML **Energy ADE 3.0 "Resources" module** models energy/water/food/waste/construction-material on 3D objects.
- The idea: combine **island metabolism** (metabolismofislands.org — a network + data hub+dashboards, open-source platform, sister to metabolismofcities.org) with **local digital twins** (ldt4ssc.eu; EU LDT Toolbox, CitiVERSE EDIC, Living-in.EU, SIMPL). Status: review committed; **19 DOI-keyed sources ingested into the repository** (`expand`), grounding tested → `graph/evidence-trace-island-dt.md`; one DOI (Chinese coastal-zone journal 10.12082/dqxxkx.2025.250220) not in OpenAlex.
- OpenAlex ingest resolved several review-flagged author lists (e.g., Helsinki B5 = Airaksinen & Rossknecht; New Caledonia = Bahers, Ventura, Antheaume et al.).

## 6. Git state (as of 2026-08-23)

- Repo `bvenner/tara` is **public**; collaborator `cappuccinocosmico` has **admin**. `main` is **9 commits ahead of origin, unpushed** (since the PR #2 merge): ec40103 → 1c3b135 (list in `git log --oneline origin/main..HEAD`).
- Push rule: feature branch + PR only, with confirmation. Working tree clean except the never-commit `.bcv` file.
- `.gitignore` exceptions: `projects/ret-tssi-value-dynamics/`, `projects/knowledge-repository-poc/`, `projects/island-digital-twin/`.
- GitHub infra used: `gh` (authenticated, admin), SSH remote OK; a manual GitHub API outage during collaborator-invite was transient.

## 7. Environment / tooling

- devenv (Nix) shell at repo; Python 3.13 venv (devenv-managed); `nix` 2.34.7; network available.
- plumbing: **wheels broken** (bundled libzmq needs libnorm/libpgm/libsodium.so.23); working = Nix build at `~/tools/plumbing` (OCaml, `nix develop -c dune build`), binaries under `_build/default/bin/{plumb,check,render,mcp,chat}/main.exe`, language version 1.2~rc1. Gotchas: `id` is a reserved token (records can't have an `id` field); `exec` output must be exact-typed; exec boundary mismatches fatal the morphism; pipelines assume cwd=`pipelines/`; `map(expr)` references input record fields.
- OpenAlex client at `projects/knowledge-repository-poc/scripts/lib/openalex_client.py` (4 req/s throttle; DOI/arXiv/topic; abstract reconstruction needed from `abstract_inverted_index`).
- **No LLM provider key** (ANTHROPIC/OPENAI/GOOGLE all absent) — pipeline-internal `agent` is key-gated; opencode-side pairing needs no key.
- opencode config: `opencode.jsonc` (instructions=[ret-tssi AGENTS.md], `skills.paths`=[poc/skills], mcp: `anytype` [failing, decommission] + `plumb` [working]). **Restart opencode to load skills + plumb MCP.**

## 8. Open decisions & likely next steps

1. **Embeddings vs Phase C:** corpus evidence favors embeddings (semantic neighborhoods, recall-widening) if cross-pillar assembly matters; Phase C (persistent service/dashboard) not yet justified.
2. **Pipeline-internal LLM:** add an `agent` binding after `trace` once a provider key exists.
3. **AnyType decommission (Phase 3):** largely moot; remove MCP entry/wrapper/secrets when convenient; rotate tara-bot key (ids are on the public repo).
4. **RET×TSSI Master's sub-problem:** M1–M6 still open; exposé (`proposal/masters-proposal.md`) not started.
5. **Island-DT next:** deepen the question (scope an island case, participatory geodesign workflow design, more ingest), possibly tie to metabolismofislands.org network and EU LDT pilot calls (~€1M per pilot).
6. **Push the 9 unpushed commits** (feature branch + PR) when confirmed.

## 9. Conventions (stand on these)

- Semantic commit prefixes; commit only when asked; never push main (feature branch + PR); ask before destructive commands / `git push`/`checkout` / edits outside this dir.
- Untracked `archive/projects/anytype-based-tara/research-assistant-architecture-bcv.md` must never be committed.
- User: Dr. Bradley "Brad" Vener; Denver/Mountain; GitHub `bvenner`; concise communication.
- "Entropy" in program docs = convex Lyapunov structure, not thermodynamic entropy.