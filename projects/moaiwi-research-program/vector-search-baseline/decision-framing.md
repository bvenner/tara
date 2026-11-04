# Decision framing — costs and benefits along the extraction ↔ elicitation spine

*The Audit's deliverable (`plan.md` expected output 3). **Qualitative — no explicit metrics** (B1); paper results appear only as source facts, cited to `kverus-deep-read.md` and `literature-audit.md`. Organized on the extraction↔elicitation spine (B5), seen through the two fixed lenses: retrieval quality; deployment/cost (T14's bar). Two decisions share this evidence base (B3, B4, and Brad's clarifications of 2026-11-03: Fortress is the Rust verification target; the outer choice is adopt/fork/ignore KVerus; TARA treats KVerus as inspiration). **Status: accepted at closure** (QA session `qa-2026-11-03-audit-closure.md`, 2026-11-03; decisions B10–B13) — both recommendations stand.*

## The spine, restated as a finding

The pass confirms the organizing axis and sharpens it: **extraction** (from formal sources: code, specs, toolchain docs) is cheap, deterministic, and reliable — KVerus's entire economics rest on it, and Fortress-as-Rust inherits it. **Elicitation** (from prose, humans, intent) is the cost center *and* the error concentration: LeetProof found ~10% of curated reference specs defective (the NL→formal projection); the layer-(b) deployments measured ~1 in 8 extracted relations wrong and non-deterministic re-extraction. What makes elicitation affordable is **validation machinery and revision discipline** — LeetProof's PBT-before-synthesis, the production "supersede, do not just add" recipe, corrections-survive-rebuilds. **Any general KR decision is mostly an elicitation decision; any elicitation decision is mostly a validation decision.**

## Decision 1 — Fortress verification: adopt, fork, or ignore KVerus

### The outer choice

- **Ignore** is the weakest option: KVerus is the only published system built for exactly this use (Rust/Verus, repository scale, toolchain churn, verifier-in-the-loop + human review), it is open source (`asterinas/KVerus`, Zenodo), and ignoring means rebuilding it — its own baseline comparison shows what unaided prompting achieves at repository scale (51.0% vs 4.5%).
- **Adopt-first** is the recommended posture: run KVerus as-is on Fortress-shaped tasks once empirical work is unblocked (Brad's gate: hold empirical runs until the KVerus decisions are made). Its three knowledge layers transfer intact because the extraction end of the spine applies (Fortress is Rust; verus-analyzer-class front ends cover it).
- **Fork** when the KR delta grows (below) or the stack diverges (KVerus is Python/LangChain on a Rust front end — if the Fortress path wants Rust-native hosting, the fork is architectural). Recommend: **adopt, with fork as the scheduled consequence of the KR work, not a precondition.**

### The knowledge architecture inside adopt/fork (B3's space)

| Option | Benefits | Costs | Verdict |
|---|---|---|---|
| (i) RAG-only | Cheapest; commodity | At repository scale it *is* the failed baseline (4.5%); misses the task shape (lemma-heavy, cross-module — "primarily a structural retrieval and lemma-reuse problem") | Not for the target use |
| (ii) **RAG + explicit KR bolted on** | Matches KVerus's proven shape; revision-heavy fitness (toolchain-evolution robustness); explainable context (dependency-scoped, provenance-carrying — T14's requirement met by construction); spec-conflict surfacing (the incorrect-spec boundary cases); the L37 attitude/fixity layer is a small delta | Elicitation for what extraction can't reach (spec intent, project/domain knowledge) — the error-concentration layer; maintenance burden (recipe exists — adopt it: content hashes, per-element provenance, supersession, corrections-survive-rebuilds) | **Recommended starting point** |
| (iii) integrated hybrid (vector + hypergraph co-equal) | Right answer where query mix is relational/multi-hop *and* construction quality is high; n-ary claim structure for the elicited knowledge | Triple-index synchronization; decay without automation; graph-alone wiring traps; higher latency | The **spectrum endpoint** of (ii) — grow into it as the elicited claim layer earns its keep; not the day-one shape |
| (iv) structure-only | Explainability | KVerus's own finding ("RAG over raw code is brittle") is pro-semantics; semantic mismatch retrieval fails | Framing completeness only |

### Build-vs-buy

- **Buy/adopt the maintenance machinery**: 2026 tooling (content-hash fingerprints, per-element provenance, diff reconciliation, supersession semantics, scoped revalidation) is exactly D3's revision discipline; reinventing it would be waste. Hybrid retrieval primitives are commodity.
- **Build the extraction**: formal-source front ends are the moat (prose-extraction quality is the field's ceiling problem; code/spec extraction sidesteps it).
- **Build the claim/attitude layer**: no off-the-shelf system ships it (LPG lacks the claim-vs-assertion primitive; RDF 1.2 has it but is retrieval-hostile; hypergraphs formalize it best but lack production tooling — layer c). This is the differentiating component and the natural interface to T17/the multi-succedent program.

## Decision 2 — TARA retrieval for near-term M2/M3 research (B4's space)

Prior evidence on the books (2026-10-11): explicit pillar/track fan-out solved cross-pillar recall mechanically; embeddings' remaining niche is **unanticipated taxonomies**.

- **(iii) as-is — the near-term default.** Zero cost; current queries are fan-out-shaped and the existing evidence covers them. Keep for M2/M3 research unless a demonstrated need appears.
- **(i) separate RAG vector DB — defer.** Cheapest semantic entry but the wiring risks are documented (split-brain synchronization; the re-ranker trap; budget crowding), and scale heuristics say a small corpus gains little. The unanticipated-taxonomy niche is real but better served by (ii).
- **(ii) vector search within the hypergraph — the right target when a win is needed.** KVerus's shape (structure first, semantic entry over it) reproduced in-house; "attach text to nodes" evidence (layer b); captures the unanticipated-taxonomy niche **without a second store**; aligns with the multi-succedent program's hypergraph direction. It was already proposed during TARA work; this pass strengthens the case and locates it as option (ii) on the spectrum.

**Recommendation: stay (iii) now; take (ii) as the first build when M2/M3 research needs semantic entry.** No implementation now (huge-win gate; no empirical testing — B1/B4).

## Candidate wins for TARA (listed, not implemented)

*Per B4: listing yes, doing gated by the huge-win threshold. **Deferred (B13, 2026-11-03): no TARA changes until M1 is complete**; after M1 they return for decision, W3 first in line.*

- **W1 — vector-within-hypergraph prototype** (option (ii)) behind fixtures/replay: semantic entry + structural closure; measure graph-alone contribution to avoid the re-ranker trap.
- **W2 — attitude/fixity fields** on claim records and on synthesized descriptions (L37): cheap, small, and the differentiating structure no off-the-shelf system has.
- **W3 — ingestion revision discipline** (content hashes, per-element provenance, supersession, corrections-survive-rebuilds): adopt the production recipe wholesale — this is D3 arriving as a concrete pipeline change.
- **W4 — query routing + contribution accounting** (fan-out vs semantic; track what each source contributed): the consensus production pattern, and the discipline that keeps hybrids honest.

## Three-arm trial: pointers for criteria v2 (B6; extraction-vs-elicitation as deepest variable)

Pin the **query mix** (lookup / bridge / aggregate / revision — conclusions flip with it); prefer **retrieval-level measures** (gold-in-budget, bridge recall, graph-alone contribution) over judge scores; **control presentation order** (LLM-judge position effects are documented); include **revision-heavy tasks** (fix-the-failing-thing, KVerus/LeetProof shape); stratify by **knowledge source** (extracted vs elicited).

## T14 / T17 fixed-lens summaries

- **T14 (deployment/cost + harness):** the harness requirements are empirically grounded (layer d) — context assembly must serve *review* (the dominant real cost), human judgment stays the last confirmatory step (AI-last conversations are rejected far more often), risk signals belong at attention granularity, and worked examples are the highest-value retrieval unit (Rango's +47% vs +3%). A KVerus-shaped system with provenance-carrying context is a strong T14 fit; the review-burden evidence is the argument for spending on explainability over recall.
- **T17 (coherence):** the translation targets hold (dependency graph ≈ relational structure; lemma index ≈ projection with a loss profile); the claim/attitude layer is where the multi-succedent program's formalism would attach; the elicitation→formalization projection is the loss-bearing map T15's currency measures (LeetProof = the existence proof for measuring it).

## Provisional character

Qualitative by design; no empirical runs (deferred to the KVerus-decision gate). The spine is confirmed (L41 closed) and **joined by the validation axis as a co-organizing axis** — how formalizations get checked (tests, human review, corrections surviving rebuilds) proved nearly as load-bearing (decision B11, 2026-11-03). The RT touch (L42) was applied at closure (B12).
