# moaiwi-network-poc — business plan POC for a corporation that is a federation of worker cooperatives

Thread goal: a business plan presented as a **5–10 minute brief overview with a brief live demo** to an invite-only hybrid gathering of Resist & Build DEN-2026 contacts, aiming to attract impact investors while generating social, environmental, and financial impacts without a prior commitment to an aggregation scale. The **pitch deck and website are the primary artifacts** — built to show-ready quality for interested parties; the talk points to them. The event is **feedback stage**; investor-facing materials are the next phase. The sprint is **one combined workstream**: prototype stack + impact-fund interviews + conference pitch. Working name "moaiwi" is internal only — naming is deliberately delegated to the audience (see framing memo §7).

## Resume path (read first after any session/context reset)

1. `writing/machine/2026-10-22-moaiwi-session-context.md` — session state (comment-phase workflow, git state); resume-first for editing sessions
2. `writing/machine/2026-10-21-moaiwi-network-poc-meta-plan.md` — the meta-plan (single combined 30-day sprint, phases, gates; revised 2026-10-22)
3. `writing/machine/2026-10-22-moaiwi-transcripts-review.md` — review of MOAIWI-1–3 against the docs; its **2026-10-22 decisions govern** (format, horizons, register, instruments, formal framing)
4. `framing-memo.md` — Phase A output (v1, authoritative until Nic's gate): thesis, productive tension, audience register, abstraction policy + glossary; `framing-memo-v2.md` is the draft with the 2026-10-22 decisions folded in
5. `research-plans/` — B1–B4 research plans (work packages, keyword/search strategy) — pre-download gate; **B4 (higher-order networks) is the operative structural framing**
6. (next) `options/` — B1–B4 options memos and research-proposals lists

## Roles and gates

- **Nic** — main presenter; reviews all outputs before any next phase proceeds (gate protocol in meta-plan §3). He is lead developer at **Mycorrhiza Cooperative** (mycor.io), so the prototype stack is built on his existing infrastructure.
- **Brad** — builds the plan and artifacts; available for questions; not presenting.
- **Rachel** — impact-fund discovery interviews, with Nic.
- Phase 0 done 2026-10-21 (scaffold). Phase A done 2026-10-21 (framing memo) → **Gate 1 awaiting Nic's review**, scope revised 2026-10-22 for the three-horizon structure.
- Gates: Gate 2 (B1–B3 options memos + B4 alongside, staggered Oct 29–Nov 4), **Gate 2b (fieldwork checkpoint: interview synthesis + prototype status, Nov 4)**, Gate 3/4 (plan content + demos incl. D0, Nov 11), Gate 5 (rehearsal of the timed overview, Nov 17).
- Gate 0 items (event date, attendee mix, hybrid platform/AV, site visibility, review turnaround) are **deferred by Brad** — they bind at Phase E, not Phase A. **Slot length is settled:** 5–10 minutes including a brief live demo. Calendar recalibrates when the date is known.

## Planned layout

- `framing-memo.md` — Phase A output (v1) · `framing-memo-v2.md` — draft with the 2026-10-22 decisions
- `research-plans/` — B1–B4 research plans (work packages, keyword/search strategy; pre-download gate)
- `options/` — B1 architecture-governance, B2 impact-accounting, B3 capital-allocation memos (Phase B); B4 higher-order-networks framing
- `plan/` — business plan content (Phase C), structured by horizon
- `data/` — synthetic federation dataset + schema (Phase D)
- `demos/` — impact calculator (D1), federation simulator (D2), financial dashboard (D3), **D0 prototype preview** (Phase D)
- `deck/` (Slidev) and `handout/` (Marp) — Phase E

## Reference integration (B1–B4)

Decision reversed 2026-10-21 (Brad): this thread integrates reference materials downloaded for Phases B1–B4 into the hypergraph knowledge repository (`projects/knowledge-repository-poc/`), superseding the standalone posture in the meta-plan's original draft.

- OpenAlex works: `uv run python projects/knowledge-repository-poc/scripts/pipeline.py expand '{"mode":"doi","doi":"<doi>","topic":"","limit":25}'` (or `mode:"topic"` with `"topic":"<concept>"`).
- Manually-downloaded PDFs: stage in `papers/incoming/<key>.pdf`, convert with fulltext `mode:"local"`.
- After corpus edits, rebuild the hypergraph: `uv run python projects/knowledge-repository-poc/scripts/build_hypergraph.py --force`.
- Query via `pipeline.py {query|trace|trace_report|evidence}`; cite `doc :: section`; follow the `hypergraph-grounding` skill — never assert beyond what the trace returns or the cited section states.

## Conventions

- Semantic commit prefixes; commit only when asked; push only to a feature branch with explicit confirmation.
- Structurally abstract: role labels only (glossary in framing memo §6); no entity or cooperative names; options, never decisions, on architecture/governance/instrument/aggregation.
- Standing disclaimer on every artifact with numbers: *"Illustrative — synthetic federation data. Assumptions documented with the dataset."*
- Research lenses (locked): network science + cooperative game theory; **higher-order networks (B4) as the operative structural lens** — projection loss, multi-scale aggregation, community structure; resilience + panarchy (internal/B3 only — the word stays out of the pitch); Ostrom + solidarity economy; control/operations research; cost accounting as a business-process discipline grounded in existing practice. **Category theory / sheaves: long-term only** — categorical semantics is not needed to resolve any short- or medium-term question (Brad, 2026-10-22). Thermodynamics/stat-mech is **deliberately excluded** from the pitch agenda (planetary models lean industrial-ecology/LCA-style accounting).

## Locked decisions (2026-10-22 review batch)

- **Format:** 5–10 minute brief overview with a brief live demo; deck + site are the primary artifacts.
- **Horizons:** short = prototype stack + impact-fund interviews; medium = beta product for deployment to funds (the wedge, ≈$10K/yr or cooperative membership); long = federation-wide multi-capital modeling + investment vehicle.
- **Register:** horizon-dependent (finance/product short+medium; economic-democracy long term; Siobhan's principle bridges). "Resilience" out of the pitch, parked as long-term investor-segment marketing.
- **Instruments:** initial investors **equity-only**; debt is a long-horizon branch.
- **Data:** demos synthetic; a **validation track** uses real co-op books to validate the schema.
- **Formal framing:** higher-order networks (B4) operative; cost accounting grounded in existing business processes; categorical material long-term only.
- **Tax:** research questions with counsel flags in B1; not deck language.
- **Open long-horizon question:** software & systems development vs direct implementation — requires empirical data before it can be resolved.
- Reference materials for B1–B4 are integrated into the hypergraph knowledge repository (see **Reference integration** above); memo claims are grounded and cited `doc :: section`.
