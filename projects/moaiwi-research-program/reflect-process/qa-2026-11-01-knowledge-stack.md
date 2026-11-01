# QA session record — the meta-processes (round 1, exchange 2): the knowledge stack (T18, T17)

**Date.** 2026-11-01 · **Participants.** Brad + agent · **Process.** Meta-process review round 1 · **Stopping point.** Proposed by agent (context at 35%), accepted by Brad ("I agree with your suggestion to close and write"), with T13 and T15 to follow before compaction.

**Input.** Continuing from `qa-2026-10-31-tara-records.md`; Brad's three-way division + harness framing; KVerus (arXiv:2605.03822) re-read; Rousseau's systemology (Springer 978-981-10-0892-4) per Brad; the bounded desk pass (work note: `../multi-succedent-formalism/desk-pass-2026-11-01.md`).

## Decisions

- **D1 — Division of labor (supersedes the 2026-10-31 "T14 absorbs T18" plan).** **T14 = context engineering · T18 = knowledge engineering · T17 = knowledge mathematics.** T18 stays a topic; the boundary is *research posture*: T18 is knowledge representation **"for itself"** (tolerant of mathematics that may one day be used for engineering), T14 is **"for development"** (extremely skeptical of any tool not well developed, tested, deployment-ready), T17 formalizes natural language into mathematics. A practical concession to context engineering: the work is divided to fit context windows. TARA = the intermediate area (research on a research assistant).
- **D2 — T14 = context engineering (harness framing).** The harness analogy taken seriously: the harness couples the LLM's energy to the cart of practical work; the human driver guides knowing the purpose of the cargo. A good harness guides an LLM, addressing weaknesses **without crippling creativity**, and helps the human driver with **context overload**. Record metadata matters because context shared between human agents must be **explainable**.
- **D3 — T18.3 dissolved and reformed (default logic → revision discipline).** Both candidate workflows give the LLM the knowledge-structure role (the Karpathy/Obsidian model too — Obsidian holds only the link structure). The design axis is the logic's default. Desk-pass reframe: **what is non-monotonic is the material base, not the logic** (NMMS is conservative over its material base — Hlobil–Brandom per Horty's NDPR review; Cut not admissible). The question becomes the **material-base revision discipline** (add / retract / supersede). "Is a hypergraph-category logic monotonic?" left **open** (Brad: no reference found; bare hypergraphs carry no consequence relation — underdetermined until structure is specified). In-house note: TARA claim records carry accept/reject polarity (bilateral seed) — to verify.
- **D4 — The multi-succedent formalism question (string-diagram work reframed).** One compositional diagrammatic formalism covering (i) hypergraph KBs, (ii) relational structures, (iii) possibly NMMS material bases — *one premise configuration, multiple succedents* as the common feature. Success criterion = the three translations with loss profiles (T15's projection loss as the currency). The program spans all three divisions. Parked Q1–Q3 reorganized: Q1 → translation test; Q2 → the ambient-setting question (= T17's core); Q3 → pyNMMS as a parallel track (candidate-(b) prototype proceeds regardless).
- **D5 — Desk pass headline** (details in the work note): hypergraph ↔ string diagram ↔ DPO rewriting is *established* (SDR I–III; string diagrams = monogamous acyclic hypergraphs); ologs/FDM/FQL give *established* KR↔DB translation with loss-bearing migration functors; Hughes' combinatorial proofs give proofs as graph homomorphisms **over Rel** — multi-succedent proof structure established (additive proof nets; Petri-net link); Brown's NMMS reconstruction leans \*-autonomous/linear (his future work is our question); DOTS (Libkind–Myers) is the T17 bridge (process theories ⊂ categorical systems theory). **The gap: nobody does the three-way translation with NMMS.** Tools: Catlab.jl is mature (Brown is lead maintainer — passes T14's bar); pyNMMS/ROLE.jl pending the skeptical check. Rel keeps surfacing as the shared semantic floor.
- **D6 — T18.1 closed-as-proposed.** Center of gravity = **the comparison question** (Q7 in skeptical form): *does structured knowledge beat retrieval for the downstream tasks, and under what conditions?* Representation and elicitation are hypotheses on trial.
- **D7 — T18.4 closed-as-reframed.** KVerus = affirmative evidence for explicit knowledge bases as context in proof engineering — with the key finding that RAG over Verus documentation mattered most for **proof revision** (the revision loop). But KVerus used off-the-shelf RAG, so **T18's posture is skeptical: default = off-the-shelf RAG; fancier machinery must beat it** (vector search is sophisticated math and engineering — understand the baseline before judging it). **"Why hypergraphs? Why not RAG?" is a core question for TARA itself.** Trial = three arms (retrieval-only / structure-only / hybrid — KVerus is itself hybrid); criteria v1: same corpus/tasks; revision-heavy tasks — **provisional**. Win conditions = boundary wins: T14 effectiveness + T17 mathematical coherence (label correction confirmed).
- **D8 — T17.1–.3 closed.** Three strata: real-world *systems that learn* (implicit; millennia of biological/cultural experience) → natural-language **systems of inquiry** (systemology) → **mathematical formalization** (explicit) — the implicit/explicit question one level higher. T17's remit: formalizing the systemology layer; the systemology literature is **source** and **foil** (against completeness claims for any mathematical representation); RAG is instrumental to the formalization process. **Rousseau's four processes (philosophy, science, engineering, practice)** = the broadest synthesis of the systems literature Brad has found, proposed as a direct replacement for GST (von Bertalanffy/Boulding); RR-DD is a **systems-engineering-focused formulation** of Rousseau's broader categories (mapping to be examined in T13's walk). Breadth ⇒ every formalization is local and need-driven (the incompleteness doctrine, grounded). T17 wins = mathematical coherence **and** adequacy to practical need.

## Deferred-changes ledger (this session)

| # | Item | Disposition |
|---|---|---|
| L26 | Three-way division supersedes the 2026-10-31 merge/tombstone plan (T18 stays a topic) | **Applied** (RT entries) |
| L27 | T14 harness/context-engineering framing + deployment-skeptical posture | **Applied** (RT) |
| L28 | T18.3 reformed: material-base revision discipline; hypergraph-category monotonicity open | **Applied** (RT) |
| L29 | Multi-succedent formalism question; parked Q1–Q3 reorganized | **Applied** (RT + work note) |
| L30 | Desk-pass work note | **Applied** (`multi-succedent-formalism/desk-pass-2026-11-01.md`) |
| L31 | T18.1 closed (comparison question as center) | **Applied** (RT) |
| L32 | T18.4 closed (skeptical posture; three-arm trial; boundary wins) | **Applied** (RT) |
| L33 | T17 remit + wins (three strata; source+foil; Rousseau anchor) | **Applied** (RT) |
| L34 | Rousseau anchor for T13 (four processes; RR-DD as systems-engineering formulation) | **Applied** (RT) |
| L35 | Three-perspective baseline study (T14/T18/T17 views of vector search) + criteria v1 provisional | Recorded; study = queued work |
| L36 | T17 label correction (mathematical coherence = T17) | **Applied** (record) |
| L37 | TARA claim polarity (accept/reject) as bilateral seed | Open — verify against schemas |

## Applied at this stopping point

This record · the desk-pass work note · RT revisions (T13 anchor; T17/T18/T14 remit revisions + titles) · AGENTS pointer.

## Closing batch (2026-11-01, applied) — round 1 complete

- **T13 closed-as-revised** (13.1: systemology itself is T13's target — Rousseau's question, *Systems* 6(1):7; the four component disciplines map to our four processes; critical method = software/systems engineering; 13.2 mapping agreed-in-principle; philosophy-first ⇒ Reflect leads, converging with the 2026-10-24 decision).
- **T15 closed** (natural-systems discipline; empirical methodology question + deliverable; projection loss = measurement validity and the loss-currency; string-diagram core → T17; "systems science" rename declined).
- **T16 reaffirmed as currently written** (stays with its own process; the Asides input queued there; the terminal-object question stays open there).
- The round-0 **T18 motivation edit (L14) landed** in T18 (origin question; Nic/Brad tension; the Brandom agenda item).

**Cluster convergence: T13 ✓ T14 ✓ T15 ✓ T16 ✓ (reaffirmed) T17 ✓ T18 ✓ — round 1's convergence criterion is met.**

## Open for round 2 / standing

The three-perspective baseline study (vector search understood from the T14/T18/T17 views) · the multi-succedent formalism program (work note: `../multi-succedent-formalism/desk-pass-2026-11-01.md`) · L37 (TARA claim polarity verification) · QA session 2 for democracy-as-regime (its own process) · the C1–C7 batch (L2 harmonization rides it) · the Develop-meta-plan inputs (KVerus/LeetProof; the inferential-role ↔ Hoare-logic thread).
