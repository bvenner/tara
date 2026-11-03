# QA session record — meta-process review round 2, exchange 1: the three-perspective baseline study (the Audit)

**Date.** 2026-11-03 · **Participants.** Brad + agent · **Process.** Meta-process review round 2, exchange 1 · **Stopping point.** Proposed by agent ("Shall we declare it?"), jointly declared by Brad ("Please declare it.").

**Input.** `reflect-process-instruction.md` (read first, per Brad); the round-2 standing list in `qa-2026-11-01-knowledge-stack.md`; L35 (the baseline study as queued work). Session rules as specified: numbered QA; no document changes and no non-Q&A output until the jointly declared stopping point (this batch); lookups per QA session 1's option (a); chunked deliberation (batches Q1–Q4, Q5–Q8, Q9–Q11, each answered before the next was sent). **Short names: the Audit** = the study and its notes (`../vector-search-baseline/`); **the Charter** = `../vector-search-baseline/plan.md`. KVerus keeps its name.

*Questions below are condensed for the record; Brad's answers are verbatim.*

## Questions and answers

### Batch 1 — the study's charter

**Q1. What is the study's shape?** Candidates: (a) bounded desk pass like the multi-succedent one; (b) desk + hands-on (run vector search over the TARA corpus, replay evidence-trace questions); (c) mathematics note for T17 (embedding as projection, what geometry buys/loses). Agent's lean: (b) with (c) folded in. One note or three?

**Q2. Are these the right per-view questions?** T14 (context engineering): explainability of retrieved chunks (traceability as `doc :: section`), context overload, deployment/cost against T14's bar, the harness test (guide without crippling creativity). T18 (knowledge engineering): where the baseline wins/loses downstream, especially revision-heavy tasks (KVerus's finding: RAG mattered most for proof revision); post-L37 what structure can represent that it can't (explicit retractions) and vice versa. T17 (knowledge mathematics): the embedding map as projection, its projection loss (T15's currency), what corpus structure it destroys (provenance, co-occurrence, multi-relation), and any contact with the shared floor (Rel).

**Q3. What counts as "understood"?** Candidate bar: loss profile of the baseline in the shared currency (projection loss) plus criteria v2 for the three-arm trial (upgrading the provisional criteria v1). Or is a verdict-style note enough?

**Q4. Boundaries and budget.** (a) hybrid arm in or out; (b) the engineering stack (embedding models, ANN indexes, rerankers) in or out; (c) desk-bounded or empirical runs welcome; (d) placement — question-keyed directory `vector-search-baseline/`, record as `qa-2026-11-03-vector-search-baseline.md`?

**A1–A2 (verbatim).** "In general, I don't want to necessarliy pose the options as an either-or choice, since a hybrid vector database-hypergraph knowledge base is also an option. Because the engineering choice must consisder many factors in addition to feasability, I'd like to keep Q1 as a desk audit. I'd also like to avoid any effort on the current realization of TARA unless it's a huge win, since my current plan for the context engineering program would be based on the KVerus system that is written in Rust, and the engineering task would be to add an explicit knowledge representation system to the existing RAG-based engine (since KVerus is on the development path for Fortress). I think these mostly fit in your Q2 specifications."

**A3 (verbatim).** "For Q3, the goal is to frame the costs and benefits of the engineering decision."

**A4 (verbatim).** "For Q4 (a), the hybrid system is definitely in, (b) qualitatively specify the decision space without explicit metrics, (c) this will defnitely require literature review, but I'd hold off on empirical runs until decisions around KVerus are made (d) a question-keyed directory for now."

### Batch 2 — the decision space and perimeter

**Q5.** Agent's draft decision space: (i) RAG-only (KVerus as-is; the skeptical default); (ii) RAG + explicit KR added to the engine (the stated engineering task); (iii) integrated hybrid (vector store + hypergraph KB as co-equal stores behind one query layer); (iv) structure-only (framing completeness). (ii)–(iii) as points on a spectrum; build-vs-buy axis (GraphRAG/KG-RAG products as prior art). Confirm, correct, or add?

**Q6.** Does the three-arm trial survive as the eventual evidence test (audit now = qualitative framing; trial later = Develop-side evals on KVerus), or fold into the engineering-decision process?

**Q7.** Decision home — Develop meta-plan's KVerus/LeetProof input, Nic/PT, or this Reflect process? Needed-by when?

**Q8.** Literature perimeter: (a) KVerus deep-read + LeetProof; (b) hybrid-search engineering and buy-side prior art at scan depth; (c) candidate explicit-KR systems (hypergraph KBs, property graphs, RDF/ologs); (d) proof-engineering / agent-collaboration evidence. All four in?

**A5 (verbatim).** "Q5. Agree."

**A6 (verbatim).** "Q6. Still stands as a framing question. KVerus is already a hybrid system but in a more formal domain (it's knowledge graph is based on reading Rust code) whereas a more general system will need to rely on knowledge elicitation, and thus rely upon the results from T17."

**A7 (verbatim).** "Q7. This reflect process. The big question is whether there are wins for TARA now that could be used for near-term M2/M3 research, but I don't want to do empirical testing yet. The KVerus question is a deep dive that may need to be deferred until after the M3 phase is complete or underway."

**A8 (verbatim).** "Q8. Agree with yes."

### Batch 3 — closing questions

**Q9.** Extraction ↔ elicitation (formalization loss on the elicitation side) as the audit's organizing axis, or one of three equal axes alongside retrieval quality and deployment/cost?

**Q10.** What does the near-term M2/M3 research comprise (so a candidate wins list can be targeted)? Confirm the shape: candidates listed, implementation deferred.

**Q11.** KVerus depth: targeted reads now with the deep dive queued and gated on M3, or deep read in scope now?

**A9 (verbatim).** "Q9. Your choice. May revisit after research pass."

**A10 (verbatim).** "Q10. For the M2/M2 work, I see the choice as whether to add a separate RAG vector database to TARA, build a vector search within the hypergraph (already proposed during TARA work) or use the current system as is."

**A11 (verbatim).** "Q11. A deep read is in scope, as I believe that you can get this done in a day or so."

## Decisions

- **B1 — Shape: desk audit.** Literature-level only. **No empirical runs** (deferred until decisions around KVerus are made); **no effort on TARA's current realization absent a huge win**. Deliverable: qualitative **costs/benefits framing of the engineering decision(s)**; the decision space specified **without explicit metrics**. Placement: question-keyed `../vector-search-baseline/`.
- **B2 — Engineering context (load-bearing).** The context-engineering program (T14) will build on **KVerus** (Rust; RAG-based; on the development path for Fortress); the candidate engineering task is **adding an explicit knowledge representation system to the existing RAG engine**. The baseline of the Audit is KVerus's RAG stack, not an abstract "vector search" and not TARA.
- **B3 — General decision space** (not either-or; hybrid is first-class): (i) RAG-only (skeptical default — fancier machinery must beat it); (ii) RAG + explicit KR bolted on; (iii) integrated hybrid (vector store + hypergraph KB as co-equal stores); (iv) structure-only (framing completeness). (ii)–(iii) are a spectrum; a **build-vs-buy axis** runs across (GraphRAG/KG-RAG products as prior art).
- **B4 — TARA-side decision space** (the near-term M2/M3 question): (i) add a separate RAG vector database to TARA; (ii) **build vector search within the hypergraph** (already proposed during TARA work); (iii) the current system as-is. Framed qualitatively with a recommendation expected; **no implementation** (gated by the huge-win threshold) and **no empirical testing**. Prior evidence starts the framing: the embeddings vs. Phase C finding of 2026-10-11 (explicit pillar/track fan-out solved cross-pillar recall mechanically; embeddings' remaining niche = unanticipated taxonomies).
- **B5 — Extraction ↔ elicitation is the Audit's spine.** KVerus is **already hybrid**, but in a formal domain — its knowledge graph is **extracted** from Rust code (near-deterministic acquisition). A general system must **elicit** knowledge (humans, documents, agents) and formalize it — relying on T17's results (with T18's elicitation question). Formalization loss (T15's projection loss as the currency) applies to both projections (embedding; elicitation→formalization). Fixed lenses: retrieval quality; deployment/cost (T14's bar). Spine chosen by agent (Q9); **revisitable after the research pass**.
- **B6 — The three-arm trial stands as a framing question** (not dissolved, not privileged as arm-vs-arm); extraction-vs-elicitation is its deepest variable.
- **B7 — The KVerus deep read is in scope** (~a day, per Brad).
- **B8 — Literature perimeter: all four layers in** — (a) KVerus deep read + LeetProof (revision-heavy evidence); (b) hybrid-search engineering + buy-side prior art at scan depth; (c) candidate explicit-KR systems (hypergraph KBs, property graphs, RDF/ologs); (d) proof-engineering / human-LLM-agent collaboration evidence (the harness view).
- **B9 — Decision home: this Reflect process.** Near-term product: the qualitative framing + the TARA-side recommendation for near-term M2/M3 research.

## Deferred-changes ledger (this session; L-series continues)

| # | Item | Disposition |
|---|---|---|
| L38 | Session record + the Charter (`../vector-search-baseline/plan.md`, B1–B9) | **Applied** (this stopping point) |
| L39 | AGENTS resume-path pointer (this record + `vector-search-baseline/`) | **Applied** |
| L40 | Round-2 standing list (`qa-2026-11-01-knowledge-stack.md`): baseline study → in progress, chartered here | **Applied** |
| L41 | Extraction↔elicitation spine = agent's choice (Q9) | **Open** — revisit after the research pass |
| L42 | RT touch for the Audit's outcomes (both decision spaces; elicitation axis; trial framing) | **Deferred** — no RT changes at this stopping point; revisit when the Audit reports |
| L43 | Three-arm trial remains a framing question; extraction-vs-elicitation its deepest variable | Recorded → T18 (no edit now) |

## Applied at this stopping point

This record · the Charter (`../vector-search-baseline/plan.md`) · AGENTS pointer · round-2 standing-list tick. No changes to `research-topics-v3.md` (L42).
