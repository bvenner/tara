# moaiwi-network-poc — business plan POC for a corporation that is a federation of worker cooperatives

Thread goal: a business plan presented as a **5–10 minute brief overview with a brief live demo** to an invite-only hybrid gathering of Resist & Build DEN-2026 contacts, aiming to attract impact investors while generating social, environmental, and financial impacts without a prior commitment to an aggregation scale. The **pitch deck and website are the primary artifacts** — built to show-ready quality for interested parties; the talk points to them. The event is **feedback stage**; investor-facing materials are the next phase. The sprint is **one combined workstream**: prototype stack + impact-fund interviews + conference pitch. Working name "moaiwi" is internal only — naming is deliberately delegated to the audience (see framing memo §7).

## Resume path (read first after any session/context reset)

1. `writing/human/moaiwi-revision-proposal.md` — **authoritative source for the v3 rewrite (2026-10-24)**; where it conflicts with any other document, it wins
2. `writing/machine/2026-10-22-moaiwi-session-context.md` — session state (comment-phase workflow, git state)
3. `writing/machine/2026-10-21-moaiwi-network-poc-meta-plan.md` — the meta-plan (single combined 30-day sprint, phases, gates; revised 2026-10-22); **superseded by the v3 rewrite**
4. `writing/machine/2026-10-22-moaiwi-transcripts-review.md` — review of MOAIWI-1–3 against the docs; its **2026-10-22 decisions govern** the v2 documents
5. `framing-memo.md` — Phase A output (v1): thesis, productive tension, audience register, abstraction policy + glossary; `framing-memo-v2.md` is the draft with the 2026-10-22 decisions folded in
6. `research-plans/` — B1–B4 research plans (work packages, keyword/search strategy) — pre-download gate; **B4 (higher-order networks) is the operative structural framing**; their fate under v3 is **undecided**
7. `writing/human/MOAIWI-1–3.md`, `MOAIWI-4.md` — the cleaned transcripts; 1–3 are **primary sources for the v3 documents**, so run `grep -rn "Nic"` against them rather than relying on summaries
8. (next) `options/` — B1–B4 options memos and research-proposals lists

## v3 rewrite (2026-10-24) — current phase

`writing/human/moaiwi-revision-proposal.md` is **authoritative** where it conflicts with any existing document. Directive in brief:

- The main artifacts need a major revision. Keep the repository name. Create **v3 documents written from scratch** that do not track the previous documents.
- **Move** `writing/machine/2026-10-21-moaiwi-network-poc-meta-plan.md` into this directory and write a **v3 meta-plan** there. After the meta-plan is revised and reviewed, write **`framing-memo-v3.md`**.
- Primary sources: the transcripts in `writing/human/MOAIWI-{1,2,3,4}.md` **and `writing/human/Informatics1Readable.md`**. *Conflicts with the previous plans are settled by the revision proposal — and must be **noted**, not silently resolved.*
- The fate of `research-plans/` (B1–B4) is **undecided**; do not assume it carries into v3.

**Structure the meta-plan must assume.** Two dimensions:

- **Time = projects**, composed of sub-projects called *phases*: **Moaiwi** (B2B product for USSEN impact investors — organic growth from the R&B Denver 2026 meeting; working name; revenue goal of $50,000/yr to sustain Nic in developing the plan; may expand beyond USSEN), **Hyphae** (technology for a confederation of workplace cooperatives — equity capital from impact investors against measurable environmental, social and financial impacts; models the local economy and the network; replaces conventionally procured goods/services with cooperative provision where that increases value; must produce investor–cooperator synergy neither has alone), and **Cooptopia** (technology to push the cooperative economy past its current ~5%-of-flows ceiling — research-only for now, dependent on Hyphae).
- **Space = meta-processes** running in every phase: **Research, Develop, Deploy, Reflect**. Each is to be realized as interacting agents (human or computational) exchanging resources over channels, and dynamically generated per project stage. Current realizations: Research = TARA in this repository; Develop = Rust + declarative NixOS under LLM supervision, with a planned multi-agent Verus vericoding harness modelled on the Plumbing language; Deploy = reliability that holds as needs change, with digital-twin automation intended; Reflect = not yet systematically developed.

**Roles and naming.** The developer is the workplace cooperative **proletariat.tech (PT)**; **Nic Venner is its lead developer, pronouns they/them**. PT's alpha-stage B2C product is **Fortress** (source: `/home/brad/Projects/fortress`, `codeberg.org/proletariat/fortress`), which is **the basis for Moaiwi**: the goal is to make Fortress sufficiently configurable that one codebase specifies either a home-network server or a business server. Earlier framing had Fortress as an idea source with a common core extracted — the 2026-10-24 revision supersedes it (the span-in-a-category picture may still describe the eventual architecture, but the operative plan is one configurable codebase).


## Roles and gates

- **Nic** — main presenter; reviews all outputs before any next phase proceeds (gate protocol in meta-plan §3). Pronoun: **they/them**. They are the lead developer at **proletariat.tech** (PT), which builds on **Fortress**, PT's alpha-stage B2C product, so the prototype stack grows out of their existing infrastructure.
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

*These govern the **v2** document set (meta-plan, framing memo v2, B1–B4 plans). They remain the 2026-10-22 record; where the **v3 rewrite** directive (`writing/human/moaiwi-revision-proposal.md`) conflicts, v3 wins — notably the project names (Moaiwi / **Hyphae** / **Cooptopia**), the two-dimension structure (projects × Research/Develop/Deploy/Reflect meta-processes), and PT as the developer.*

- **Format:** 5–10 minute brief overview with a brief live demo; deck + site are the primary artifacts.
- **Horizons:** short = prototype stack + impact-fund interviews; medium = beta product for deployment to funds (the wedge, ≈$10K/yr or cooperative membership); long = federation-wide multi-capital modeling + investment vehicle.
- **Register:** horizon-dependent (finance/product short+medium; economic-democracy long term; Siobhan's principle bridges). "Resilience" out of the pitch, parked as long-term investor-segment marketing.
- **Instruments:** initial investors **equity-only**; debt is a long-horizon branch.
- **Data:** demos synthetic; a **validation track** uses real co-op books to validate the schema.
- **Formal framing:** higher-order networks (B4) operative; cost accounting grounded in existing business processes; categorical material long-term only.
- **Tax:** research questions with counsel flags in B1; not deck language.
- **Open long-horizon question:** software & systems development vs direct implementation — requires empirical data before it can be resolved.
- Reference materials for B1–B4 are integrated into the hypergraph knowledge repository (see **Reference integration** above); memo claims are grounded and cited `doc :: section`.
