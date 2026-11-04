# Plan — the vector-search baseline study ("the Audit")

*Charter settled in the Reflect QA session `../reflect-process/qa-2026-11-03-vector-search-baseline.md` (meta-process review round 2, exchange 1) and written at its jointly declared stopping point. Short names: **the Audit** = this study and its notes; **the Charter** = this file. Decisions B1–B9 in the session record are authoritative; this plan states them as a work plan per meta-plan §7. No gates.*

## Question and decisions informed

**Question (three perspectives on one baseline).** What is vector search — as a retrieval baseline — viewed from **T14** (context engineering), **T18** (knowledge engineering), and **T17** (knowledge mathematics)? The answers feed **two engineering decisions** sharing one evidence base (premises clarified by Brad, 2026-11-03: **Fortress is the Rust system being verified**; KVerus is the candidate machinery on its development path; for TARA, KVerus is inspiration):

1. **The Fortress-verification decision.** **Adopt, fork, or ignore KVerus** for Fortress verification — the outer framing this Audit informs. Inside the adopt/fork branch sits the candidate engineering task: **adding an explicit knowledge representation system to KVerus's existing RAG engine**. Decision space for the knowledge architecture: (i) RAG-only (the skeptical default — fancier machinery must beat it); (ii) RAG + explicit KR bolted on; (iii) integrated hybrid (vector store + hypergraph KB as co-equal stores behind one query layer); (iv) structure-only (framing completeness). (ii)–(iii) are points on a spectrum; a **build-vs-buy axis** runs across (off-the-shelf GraphRAG/KG-RAG products as prior art). Spine note: Fortress is Rust, so the **extraction** end of the acquisition axis carries over from KVerus; the explicit-KR question is governed by the **elicitation** end.
2. **The TARA-side decision (near-term M2/M3 research).** (i) add a separate RAG vector database to TARA; (ii) **build vector search within the hypergraph** (already proposed during TARA work); (iii) the current system as-is. The framing starts from prior evidence on the books: the **embeddings vs. Phase C** finding of 2026-10-11 (explicit pillar/track fan-out solved cross-pillar recall mechanically; embeddings' remaining niche = unanticipated taxonomies).

**Organizing axis** (agent's choice; revisable after the research pass — L41): **extraction ↔ elicitation**. KVerus's knowledge graph is *extracted* from Rust code — a formal domain where acquisition is near-deterministic. A general system must *elicit* knowledge (humans, documents, agents) and formalize it — T17's remit, with T18's elicitation question alongside. Formalization loss (T15's projection loss as the currency) applies to both projections (embedding; elicitation→formalization). **Fixed lenses:** retrieval quality; deployment/cost (T14's bar). **Framing question retained** (B6): the T18 three-arm trial (retrieval/structure/hybrid) — extraction-vs-elicitation is its deepest variable. **Amended 2026-11-03 (B11, closure QA):** validation (how formalizations are checked) is promoted to a **co-organizing axis** alongside extraction↔elicitation.

## Expected outputs

1. **The KVerus deep read** (in scope, ~a day): architecture sufficient to say what "add KR to the engine" touches; findings on retrieval and revision behavior (KVerus's known headline: RAG over Verus documentation mattered most for **proof revision**).
2. **The literature audit** — four layers: (a) KVerus deep read + LeetProof (arXiv:2604.16584; revision-heavy evidence); (b) hybrid-search engineering + buy-side prior art (vector DBs, GraphRAG/KG-RAG products) at **scan depth**; (c) candidate explicit-KR systems (hypergraph KBs, property graphs, RDF/ologs); (d) proof-engineering / human-LLM-agent collaboration evidence (the harness view).
3. **The decision framing** — qualitative **costs and benefits, no explicit metrics**, for both decision spaces, organized on the extraction↔elicitation spine, with a **recommendation for the TARA-side three-way choice**. Candidate wins for TARA are **listed, not implemented** (implementation gated by Brad's huge-win threshold).

Shape: one note with sections in this directory unless it grows (placement by later decision).

## Resources and access

- Literature via web search and OpenAlex (`expand`); KVerus (arXiv:2605.03822) and LeetProof (arXiv:2604.16584) available. In-house prior evidence: the embeddings-vs-Phase-C open decision (workspace AGENTS), the L37 verification note (`../multi-succedent-formalism/claim-polarity-verification-2026-11-02.md` — attitude + revision ops would be *new* structure in any KR added), the multi-succedent desk pass.
- **Constraints (binding): desk audit only** — no empirical runs (deferred until decisions around KVerus are made); no effort on TARA's current realization absent a huge win; no explicit metrics in the framing.
- Evidence goes to the shared corpus per the corpus & hypergraph conventions.

## What counts as an answer / closure

Both decision spaces framed qualitatively along the organizing axis and the two fixed lenses; the KVerus deep read done; the four literature layers covered; the TARA-side recommendation delivered. Closure reviewed by **this Reflect process** (QA). Post-closure: revisit the spine (L41) and the RT touch (L42) when the Audit reports.

## Where results are recorded

Audit notes in this directory; review in `../reflect-process/` (QA session records); evidence in the shared corpus; **the decision lands in this Reflect process** (decision home, B9).
