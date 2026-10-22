# moaiwi-network-poc — business plan POC for a corporation that is a federation of worker cooperatives

Thread goal: a business plan presented as a workshop/panel pitch (pitch deck + website with live demos) to an invite-only hybrid gathering of Resist & Build DEN-2026 contacts, aiming to attract impact investors while generating social, environmental, and financial impacts without a prior commitment to an aggregation scale. The event is **feedback stage**; investor-facing materials are the next phase. Working name "moaiwi" is internal only — naming is deliberately delegated to the audience (see framing memo §7).

## Resume path (read first after any session/context reset)

1. `writing/machine/2026-10-21-moaiwi-network-poc-meta-plan.md` — the meta-plan (30-day sprint, phases, gates)
2. `framing-memo.md` — Phase A output: thesis, productive tension, audience register, abstraction policy + glossary
3. `research-plans/` — B1–B3 research plans (work packages, keyword/search strategy) — pre-download gate
4. (next) `options/` — B1–B3 options memos and research-proposals lists

## Roles and gates

- **Nic** — main presenter; reviews all outputs before any next phase proceeds (gate protocol in meta-plan §3).
- **Brad** — builds the plan and artifacts; available for questions; not presenting.
- Phase 0 done 2026-10-21 (scaffold). Phase A done 2026-10-21 (framing memo) → **Gate 1 awaiting Nic's review**.
- Gate 0 items (event date, slot length, attendee mix, hybrid platform/AV, site visibility, review turnaround) are **deferred by Brad** — they bind at Phase E, not Phase A. Calendar recalibrates when the date is known.

## Planned layout

- `framing-memo.md` — Phase A output
- `research-plans/` — B1–B3 research plans (work packages, keyword/search strategy; pre-download gate)
- `options/` — B1 architecture-governance, B2 impact-accounting, B3 capital-allocation memos (Phase B)
- `plan/` — business plan content (Phase C)
- `data/` — synthetic federation dataset + schema (Phase D)
- `demos/` — impact calculator, federation simulator, financial dashboard (Phase D)
- `deck/` (Slidev) and `handout/` (Marp) — Phase E

## Reference integration (B1–B3)

Decision reversed 2026-10-21 (Brad): this thread integrates reference materials downloaded for Phases B1–B3 into the hypergraph knowledge repository (`projects/knowledge-repository-poc/`), superseding the standalone posture in the meta-plan's original draft.

- OpenAlex works: `uv run python projects/knowledge-repository-poc/scripts/pipeline.py expand '{"mode":"doi","doi":"<doi>","topic":"","limit":25}'` (or `mode:"topic"` with `"topic":"<concept>"`).
- Manually-downloaded PDFs: stage in `papers/incoming/<key>.pdf`, convert with fulltext `mode:"local"`.
- After corpus edits, rebuild the hypergraph: `uv run python projects/knowledge-repository-poc/scripts/build_hypergraph.py --force`.
- Query via `pipeline.py {query|trace|trace_report|evidence}`; cite `doc :: section`; follow the `hypergraph-grounding` skill — never assert beyond what the trace returns or the cited section states.

## Conventions

- Semantic commit prefixes; commit only when asked; push only to a feature branch with explicit confirmation.
- Structurally abstract: role labels only (glossary in framing memo §6); no entity or cooperative names; options, never decisions, on architecture/governance/instrument/aggregation.
- Standing disclaimer on every artifact with numbers: *"Illustrative — synthetic federation data. Assumptions documented with the dataset."*
- Research lenses (locked): network science + cooperative game theory; resilience + panarchy; Ostrom + solidarity economy; category theory/sheaves; control/operations research. Thermodynamics/stat-mech is **deliberately excluded** from the pitch agenda (planetary models lean industrial-ecology/LCA-style accounting).
- Reference materials for B1–B3 are integrated into the hypergraph knowledge repository (see **Reference integration** above); memo claims are grounded and cited `doc :: section`.
