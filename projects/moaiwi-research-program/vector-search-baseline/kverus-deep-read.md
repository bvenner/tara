# Deep read — KVerus (arXiv:2605.03822v2)

*Part 1 of the Audit (`plan.md`, B7). Full paper read (v2, 2 Aug 2026; ASE 2026). Paper results are reported as source facts; the decision framing itself stays qualitative per B1. Placement decision: one note per Audit output in this directory.*

**Source.** Yuwei Liu, Xinyi Wan, Yanhao Wang, Minghua Wang, Lin Huang, Tao Wei (Ant Group + independent), *KVerus: Scalable and Resilient Formal Verification Proof Generation for Rust Code*, arXiv:2605.03822v2, accepted ASE 2026. Code: github.com/asterinas/KVerus (also Zenodo 10.5281/zenodo.19937769).

## What the system is

A **knowledge-centric proof-generation workflow** for Verus (Rust deductive verifier, SMT/Z3) at repository scale, deployed on CortenMM (the verified memory-management module of the Asterinas Rust OS kernel). Its stated enemy is the **Semantic-Structural Gap**: LLMs generate from semantic code patterns; verification is governed by rigid structural dependencies (dependency graphs, pre/postconditions, lemma availability, toolchain syntax). Headline deployment result: 1,387 proof LoC, 6 new lemmas, **23 previously unverified functions accepted upstream** (21.0% of the module's proof code). Repo-level benchmarks: 51.0% success vs 4.5% for multi-round prompting. Maintenance reality that motivates everything: CortenMM needed **8 Verus synchronizations in 6 months** (~every 3 weeks).

## Knowledge-base anatomy (what "the KB" actually is)

Three knowledge kinds — **not a textbook KR system**, but already more than plain RAG:

1. **Code metadata — a typed directed dependency graph.** Built by **verus-analyzer** (compiler front end: resolved symbols, type info, source ranges, comments) over language objects (functions, spec functions, lemmas, structs, enums, traits, type aliases). Edge u→v = "verifying u may require v" (type/structure deps + call/spec deps incl. requires/ensures/invariant references). **Dependent code** = outgoing traversal at **max depth 3** from the target, deduplicated, serialized as prompt-ready snippets. *Acquisition: deterministic extraction.*
2. **Lemma knowledge — semantic index over synthesized descriptions.** Lemma records (name, params, pre/postconditions, comments, module path); where documentation is sparse, the **LLM synthesizes a natural-language description from the formal interface**; descriptions + existing comments are **vectorized**. Rationale given: "RAG over raw source code is brittle because useful lemmas may not share obvious tokens with the current proof goal." *Acquisition: extraction + lightweight LLM elicitation anchored to formal sources.*
3. **Verus knowledge — topic-indexed, version-aligned documentation.** Official docs + examples parsed by topic (loop invariants, arithmetic overflow, bit-vector reasoning, spec syntax); when docs lag toolchain changes, **PRs are manually registered** as temporary version-specific knowledge. *Acquisition: parsing + manual curation.*

**Workflow.** Preprocessor (graph + lemma extraction) → Comprehender (builds layers 2–3) → Prover (LLM requirement analysis → semantic lemma retrieval → structured prompt = target + dependency-scoped context + retrieved lemmas + Verus knowledge) → Refiner (**error triager** classifies verifier diagnostics → retrieves only the corresponding knowledge → repair prompt with minimal-change discipline: no modifying requires/ensures, no added assumptions; new lemmas from refinement re-enter the KB after passing) → **Verus check (verifier = authority on validity)** → **human review (authority on spec correctness and maintainability)** → upstream patch. Implementation: ~5,837 Python + 1,015 Rust LoC (LangChain + verus-analyzer).

## Evidence (source facts)

- **Ablation (RQ3) is the cost/benefit map.** Single-file: **Verus knowledge dominant** (Human-Eval 54→4 tasks without it); code-metadata/lemma ablations barely hurt. Repository-level: **code metadata and lemma knowledge dominant** (CortenMM 52→10 without code metadata, 52→7 without lemma knowledge; Verus knowledge 52→22). *What pays depends on task shape.*
- **Task shape (Table 2):** CortenMM vs Verus-Bench per task — spec 193 vs 8 LoC; proof 195 vs 10 LoC; **lemmas invoked 13.9 vs 0.07**. Conclusion in-paper: repository-scale proof generation is "primarily a structural retrieval and lemma-reuse problem."
- **Toolchain evolution (RQ4):** across three Verus releases the prompt-only competitor (AutoVerus) dropped 23.9%; KVerus dropped 1.2% — attributed to **version-aligned knowledge**, not model quality (same LLM configured for all tools).
- **Boundary cases (§5.2).** (a) *Incorrect specifications*: repeated proof failure exposed **spec bugs** (missing soundness conditions in `protocol_lock_skip`); fixed by a human expert. Principle stated: "when the specification is wrong, a proof generator should not fabricate proof code to make the verifier pass." (b) *Human cleanup*: 100+ generated lines/7 blocks vs 34 human lines/2 blocks on `initialize_inductive` — generated proofs are **reviewable patches**.
- **Lessons (§6).** Dependency-scoped knowledge is the key scaling unit (treat dependency metadata + proof-intent docs as proof infrastructure); proof generation is also **proof maintenance** (pin verifier versions, archive version-specific logs, proof CI); generated proofs stay in an expert workflow.
- **Limitations (§6).** No validation that specs capture intent; verifier-passing ≠ integrable; evidence strongest for Verus — other SMT verifiers (Dafny-class) plausible, explicit-proof-state provers (Rocq/Isabelle/Lean) need different representations.

## Audit mapping

### What "add explicit KR to the existing RAG engine" would touch

The engine is **already hybrid**: deterministic structural extraction + vector semantic retrieval + classifier-routed doc retrieval. What it lacks — and what an explicit KR layer would add — names cleanly against our own prior findings:

1. **Claim-level knowledge with provenance and attitude.** Everything in KVerus is *artifact*-level (functions, lemmas, doc topics). Claims ("this spec is wrong", "this idiom is superseded in version X") live in prose, human heads, or the manual PR-registration channel. Directly the L37 finding: attitude + revision operations would be **new structure**.
2. **Revision discipline.** KVerus's versioning = manual registration + retrieval-time alignment. A material base with add/retract/supersede (D3) would make the "temporary PR knowledge until docs catch up" channel a first-class, expiring record.
3. **Elicited domain knowledge.** The metadata graph and lemma records are **extracted**; the only elicitation is the synthesized lemma descriptions (cheap, anchored to formal interfaces, **no revision discipline over the descriptions themselves** — a bad synthesis silently degrades retrieval).
4. **Conflict surfaces.** The incorrect-specification boundary case is a **claim conflict** (spec vs required soundness) surfaced only by proof failure. A claim-level KR could record and route it; KVerus routes it to humans.

### The extraction ↔ elicitation spine

KVerus is the **extraction end-point of the axis, made affordable by the formal domain**: Rust/Verus code and specs are already formal, a compiler front end extracts structure deterministically, and LLM elicitation is confined to short descriptions with formal anchors. The general case (documents, human knowledge — TARA, the moaiwi program) pays the full elicitation + formalization cost (T17's remit; T15's projection loss as currency). KVerus quantifies the *shape* of the trade informally: extraction cost ≈ tooling (one front end); elicitation cost ≈ ongoing, human-in-loop, unbounded. **Any general KR decision is mostly an elicitation decision.**

### The three views

- **T14 (context engineering / harness).** KVerus is a worked instance of the harness framing: dependency-scoped closure (depth 3) instead of full-repo prompts = context-overload control; error triage → targeted knowledge = explainable, minimal context; minimal-change repair discipline = guidance without crippling creativity; reviewable patches + spec-bug surfacing = the human driver stays in control. The paper's own vocabulary ("reviewable patch", "human review = authority on spec correctness") is records language: the artifact's authority is split (verifier: validity; human: fitness), exactly the explainability requirement T14 carries.
- **T18 (knowledge engineering).** The Semantic-Structural Gap is our comparison question in microcosm: semantic retrieval (vector) vs structural knowledge (graph) — KVerus's answer is **both, with structure extracted first and semantics synthesized over it**, and the ablation says which pays where. KVerus is itself the hybrid arm of the three-arm trial. Revision-heavy evidence is strong and in the maintenance direction (RQ4, Lesson 2): on revision-heavy work, *version-aligned* and *dependency-scoped* knowledge is what survives.
- **T17 (knowledge mathematics).** The metadata dependency graph is a typed directed graph with a closure operator (depth-bounded reachability) — a consequence relation of the most mechanical kind; the vector layer is a projection of synthesized text (loss: retrieval depends on generated descriptions — no fixity, no attitude). The error triager is a lossy classifier into a fixed topic set. Nothing compositional; the multi-succedent program's translation targets (hypergraph KB / relational structures) have obvious analogues here (dependency graph ≈ relational structure; lemma index ≈ projection).

### TARA-side implications (the three-way decision)

- **Separate RAG vector DB (i):** the KVerus pattern (semantic index alongside structure) — cheap, proven on lemma-shaped retrieval; loses to structure wherever recall depends on non-textual relations (echoes the 2026-10-11 finding: fan-out beat embeddings for cross-pillar recall).
- **Vector search within the hypergraph (ii):** embeddings over vertices/edges with traversal — closest to KVerus's *combination* (retrieval = semantic entry point + structural closure). KVerus's success with "structure first, semantics over it" is the strongest available prior for (ii).
- **As-is (iii):** defensible wherever the taxonomy is explicit and the task is fan-out-shaped (the 2026-10-11 evidence); the KVerus contrast shows where it would stop paying — lemma-heavy/semantic-mismatch retrieval (their "brittle RAG over raw code" finding maps to our keyword/co-occurrence matching).

## Open questions for Brad

1. **RESOLVED (Brad, 2026-11-03).** *Fortress* is the system **written in Rust** — and it is the **verification target**. The paper's KVerus (Python + Rust on verus-analyzer) is the candidate proof-generation machinery for verifying Fortress ("KVerus is on the development path for Fortress" = on the path to being used for Fortress verification).
2. **RESOLVED (Brad, 2026-11-03).** For TARA, KVerus is **inspiration**. This research project (the Audit) helps determine whether to **adopt, fork, or ignore KVerus for Fortress verification** — that is the outer decision framing; the KR-extension question (add explicit KR to the RAG engine) sits inside the adopt/fork branch.
3. The KB's **synthesized lemma descriptions** are unverified generated text silently steering retrieval — a candidate cheap win for attitude/fixity records (L37) in *any* system we build. Note for the framing.

**Premise consequence for the spine.** Fortress being Rust means the **extraction end of the extraction↔elicitation axis applies as-is**: KVerus's economics (deterministic structural extraction via a compiler front end, cheap and reliable) carry over to Fortress verification. The elicitation side governs everything an explicit KR layer would add — domain lemmas, spec intent, project knowledge not in code — and TARA's general case.

## Sources

- arXiv:2605.03822v2 (abs + full HTML read): https://arxiv.org/abs/2605.03822 · https://arxiv.org/html/2605.03822v2
- Code/artifact: https://github.com/asterinas/KVerus · https://doi.org/10.5281/zenodo.19937769
