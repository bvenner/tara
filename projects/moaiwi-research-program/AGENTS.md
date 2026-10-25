# moaiwi-research-program — the Research (Explore) meta-process workstream

The research workstream of the moaiwi meta-plan (`../moaiwi-network-poc/meta-plan-v3.md`): everything developed under the **Research meta-process ("Explore")** lives here. This is the moaiwi thread's *research* workstream; the *artifact* workstream (meta-plan, framing memo, deck, site) stays in `../moaiwi-network-poc/`. Promotion to its own project (2026-10-24, option C) keeps `writing/machine` metadata focused: research notes carry `project: moaiwi-research-program`.

## Resume path (read first after any session/context reset)

1. `../moaiwi-network-poc/meta-plan-v3.md` — the governing meta-plan (baseline 2026-10-24); its §7 defines what a research plan must state
2. **`democracy-as-regime/`** — the active **Reflect process (T16, opened 2026-10-25)**: Castoriadis 1997 summary + the terminal-object reframing sketch + **QA session 1 record** (`qa-2026-10-25-terminal-object.md`, with the session conventions and the deferred-changes ledger) + **`next-steps-2026-10-25.md`** (dependency-ordered task list, supersedes Paideia §5); **supersedes the ranking of other topics until settled**. *Naming convention (session 1, persists): **Castor** = `castoriadis-1997-summary.md`; **Paideia** = `reflect-terminal-object-sketch-2026-10-25.md`.*
3. `research-topics-v3.md` — the Reflect-pass agenda: topics T1–T16, prioritization, **Resolved sequencing and policy** (who runs what), and Appendices A–C (B1/B2/B3 salvage maps; B4 → T15)
4. `cooperatives-governance-scaling/B1-architecture-governance-plan-v3.md` — the top-priority *research* plan (carries T3, the thesis's failure-mode inventory) + `T3-preliminary-findings-2026-10-24.md`; v1/v2 of B1 and the other B-plans remain in `../moaiwi-network-poc/research-plans/` as **history**
5. `../moaiwi-network-poc/research-plans/B1-screening-2026-10-22.md` + `B1-p0-readings-2026-10-22.md` — Phase B corpus screening and P0 readings (salvageable input)

## Layout and plan policy (Brad, 2026-10-24)

- **One directory per research question**, named with a short **slug for the question** (e.g. `cooperatives-governance-scaling/` for T3 — question-keyed, not plan-numbered). Each holds the question's plan, options memo, and notes.
- Outside of B1, plans are **clean-sheet developments of new markdown files** — they do not track the old `research-plans/` files, which are read for salvage (per the Appendices) and left in place.
- Plans fall under the Research meta-process and state the meta-plan §7 requirements: question/decisions informed · expected outputs · resources and access · what counts as an answer or closure · where results are recorded. **No gates** — gate/failure-mode machinery belongs to future Develop/Deploy meta-plans (meta-plan §4.1).

## Sequencing (Brad, 2026-10-24)

- Brad proceeds with **T3** (inside B1) without Nic; Nic (maybe Rachel) coordinates **T1**. Desk-only topics may run while T1 is open. T13/T14 (process questions) run in parallel, less urgent for M1. **B1 v3 is the current top priority**; other T-plans are not developed yet.

## Corpus & hypergraph conventions

- Evidence goes to the **shared corpus** regardless of which plan sourced it: `projects/knowledge-repository-poc/corpus/external/` (OpenAlex via `expand`) and `corpus/fulltext/` (PDFs staged to `papers/incoming/<key>.pdf`, converted with `fulltext mode:"local"`); rebuild with `build_hypergraph.py --force`; claims cited `doc :: section` per the `hypergraph-grounding` skill.
- **Plan prose is not in the hypergraph** and the graph does not track which project ingested a work (external records carry no project metadata) — so this project's location does not affect hypergraph maintenance. If plan prose should later become queryable, add **one** `research-program` root to `projects/knowledge-repository-poc/corpus.json` (never one root per question — plan vocabulary would pollute the co-occurrence statistics).
- Tooling quirks (pipeline.py failure, direct-worker invocation, local-mode DOI requirement, noisy OpenAlex queries) are recorded in `../moaiwi-network-poc/research-plans/B1-architecture-governance-plan-v3.md` §4.4 and `writing/machine/2026-10-24-moaiwi-v3-rewrite-context.md` §4.

## Conventions

- Semantic commit prefixes; commit only when asked; push only to a feature branch with explicit confirmation.
- Transcripts (`writing/human/MOAIWI-{1,2,3,4}.md`, `Informatics1Readable.md`) are primary sources and stay verbatim; Nic's pronouns are **they/them**.
- The `research-plans/` directory in `../moaiwi-network-poc/` (B1–B4 v1/v2, Phase B outputs) is **retained as history**; ultimate fate undecided; do not edit or delete without Brad's word.
