# QA session record — the meta-processes (round 0)

**Date.** 2026-10-27 · **Participants.** Brad + agent · **Process.** The meta-process review (Reflect applied to the T13–T18 cluster) · **Stopping point.** Jointly declared: "An excellent time to close the round."

**Input.** Brad's `writing/human/comments_on_research_topics_v3.md` (2026-10-27; short name **Comments**) — two sections: the AC/RT overlap (folded into RT and the T1/T2 plans before the session proper) and the meta-process proposal (the coalgebra X → F(X) framing; questions 1–6). Short names: **AC** = `action-circle-workflow-2026-10-25.md`, **RT** = `research-topics-v3.md`, **Instruction** = `reflect-process-instruction.md`.

## Conventions adopted (binding for new text)

- **meta- = self-application** (meta-data = data about data; meta-process = a process applied to processes; meta-plan = a plan for developing plans). The four (Research, Develop, Deploy, Reflect) are **"the four processes"**; historical loose usage is inherited, harmonized with the C1–C7 batch.
- **Chunked deliberation:** numbered batches; Brad answers subsets; the agent responds to each response before the next batch. (Proven this session: the Q5 correction was absorbed before Q6–Q8 progressed.)
- QA discipline per session 1 (no document changes until a joint stopping point; deferred-changes ledger).

## Decisions (design round)

- **D1 — product (Q5).** The review's output is **revisions to RT**, not specifications of the four processes (premature and too hard). The "meta-process meta-plan" proposal is **withdrawn**; next-steps 3.1 (Reflect-meta-plan decision) stays open and separate. Success = every cluster topic explicitly revisited — **reaffirmation counts**; convergence may take several rounds.
- **D2 — home (Q5).** `reflect-process/` — a topic directory for the reflect process itself, holding the Instruction (the realization) and the QA records (the memorial), inspectable by future reflect processes.
- **D3 — agenda (Q6).** A question inventory **harvested from RT.T13–T18/T16 plus the Comments' six**, source-tagged and status-tracked in the session records (QUD-style). Breadth at the inventory level, focus at the exchange level. The separate "meta-process-research-plan" is dropped: framing lives in RT's cluster note + these records.
- **D4 — Q7 reframe.** The question is **engineering, not unification**: *what is the best input to a vericoding process?* — (a) requirements engineering → natural-language specs, (b) knowledge elicitation → material base, (c) something else. The shared-formalism framing is withdrawn. The **LeetProof** phenomenon (specs revised by proof evidence — *correction 2026-10-28: originally misattributed to STARVerus*) makes **revision-friendliness** a first-class criterion; **NMMS non-monotonicity ↔ proof-driven revision** is the hypothesis to test (a material base is built for defeasible revision). Brown's categorical semantics (arXiv:2605.24796) is **demoted off the critical path** — conditional on pyNMMS insufficiency. Comments question 3 (Reflect → NL → material base) is candidate (b)'s pipeline architecture.
- **D5 — Q8.** Closed as "no answer needed" — substance recorded as **L14** below.

## Deferred-changes ledger

| # | Item | Disposition |
|---|---|---|
| L1 | T16 added to the meta-cluster in RT | **Applied** (RT cluster note) |
| L2 | Harmonize "the four meta-processes" wording | Deferred → C1–C7 batch |
| L3 | Instruction home = `reflect-process/` | **Applied** |
| L4 | Uncommitted changesets on `main` (now 3) | Open — ride with the next batch; commit on Brad's word |
| L5 | Instruction output clause: RT revisions + conventions count as output | **Applied** |
| L6 | "Meta-process meta-plan / settles 3.1" withdrawn; 3.1 stays open | Recorded (D1) |
| L7 | `reflect-process/` created; session records live here | **Applied** |
| L8 | Framing-plan deliverable dropped (framing → RT cluster note + records) | **Applied** |
| L9 | QA session 1 record **moved** here from `democracy-as-regime/`; pointers updated | **Applied** |
| L10 | Agenda = harvested inventory (source-tagged, status-tracked) | Method recorded; harvest is round 1's first act |
| L11 | Multi-round design; convergence = per-topic revisit | Recorded (doctrine) |
| L12 | Q7 reframe (engineering question; Brown demoted; NMMS↔revision hypothesis) | Recorded; agenda item for round 1 |
| L13 | Comments question 3 ↔ candidate (b) pipeline cross-ref | Recorded |
| L14 | Q8 substance: **TARA's origin question** — *is there a role for neurosymbolic approaches in AI now?* (neuro = implicit knowledge, symbolic = explicit); the **Nic/Brad tension** recorded neutrally as live and testable (Nic: LLM+harness advancing too fast; wait for the slowdown. Brad: the question is live now, TARA is the bet); *"understanding what Brandom was saying"* — Brandom anticipated the implicit/explicit interface (inferentialism; logical expressivism = making explicit the inferential relations implicit in practice) — is an **agenda item under T18** | Recorded; T18 motivation edit lands with round 1's RT revisions |

## Amendment — 2026-10-28 (between rounds; Brad)

- **Correction (provenance fix).** The spec-revision phenomenon in D4 is **LeetProof** (Sergey et al., *Certified Program Synthesis with a Multi-modal Verifier*, arXiv:2604.16584, ASE'26 — Lean-based; multi-modal spec validation via property-based testing before code synthesis; uncovered defects even in reference specs), **not STARVerus**. D4's logic is unchanged; only the attribution moved.
- **New agenda item — the substrate question** (source: Brad, 2026-10-28). *Is an SMT-only system like Verus sufficient for refining specifications, or is a dependently typed proof system (e.g. Lean) necessary?* Evidence pair: **LeetProof** (Lean; certified spec validation) vs **KVerus** (Verus/SMT; per Brad, **human review required for all proposed specification modifications**). This couples to D4's input question: where the *trust* for spec revisions sit — type-theoretic certification vs. human review — interacts with which input artifact (a/b/c) is best.
- **New agenda item — KVerus as prior art** (arXiv:2605.03822, ASE 2026). Retrieval-augmented, self-adaptive **Verus** verification: a *dynamic knowledge base* of code metadata + lemma semantics + toolchain specifics; dependency-aware analysis, semantic lemma indexing, **error-driven self-refinement**; bridges the "Semantic-Structural Gap" (LLM semantic patterns vs. structural proof dependencies). Brad: "a good concrete example of the usefulness of an explicit knowledge base." Two program notes: (i) it is **prior art for the planned multi-agent Verus vericoding harness** (Develop track); (ii) its human-review gate for spec modifications is the same containment move as Elenchus's expert authority over the LLM derivability oracle — and its error-driven refinement echoes the NMMS ↔ proof-driven-revision hypothesis.
- **Two corrections to the round-0 dialogue's framing (Brad, 2026-10-28 — recorded so they stand):** (1) The substrate/practice distinction is an **open question, not a working hypothesis** — whether LeetProof vs. KVerus handle spec modifications differently *because of* their substrates (Lean vs. SMT) or because of **social practice** (research-group policy) is unknown; no claim that one substrate forces one trust arrangement. (2) KVerus is "**a** concrete example," not "the closest published instance," of a candidate-(b)-shaped architecture — no completeness claim; a full review of vericoding systems has not been done (and belongs to the Develop-track prior-art work when it is).

## Open for round 1

1. Harvest the agenda (L10): RT.T13–T18/T16 question bullets + Comments 1–6 + D4's engineering question + the Brandom-understanding item.
2. Work the agenda in chunks; produce RT revisions + `qa-2026-10-28-…`-style record; reaffirmation is allowed.
3. Relationship to next-steps 0.5/0.6 (T13/T17 "first passes"): round 1 revisits them — the review subsumes their shape.

## Session mechanics note

The chunked discipline earned its keep twice: the Q5 scope correction (output = RT revisions) and the Q7 reframe (engineering question) each arrived because the agent responded to an answer before proceeding.
