---
title: "Research topics v3 — Reflect pass over the meta-plan and transcripts"
date: 2026-10-24
kind: options
project: moaiwi-research-program
---

# Research topics v3 — a clean-sheet agenda

*Output of a **Reflect** process (meta-plan §4.4) run on 2026-10-24 over `meta-plan-v3.md` and the transcripts (`MOAIWI-{1,2,3,4}.md`, `Informatics1Readable.md`). This is a **clean-sheet revision** of the research agenda: it does not track the existing `research-plans/` (B1–B4), whose fate remains undecided — though where partial work exists it is noted as salvageable input, not as a plan. Topics below are **suggestions and a proposed prioritization** for Brad's review; each will become a research plan under meta-plan §7 (question/decision, expected outputs, resources, answer criteria, recording location).*

## How topics were found

1. Every claim in the meta-plan that is currently ungrounded — marked "hypothesis", "to be tested", "risk noted", or left to research plans.
2. Every design space the transcripts work out without settling (finance mechanics, law, measurement, marketing).
3. Every development intention in §4 that requires knowledge before it requires code (meta-process theory, repositories, formalization).
4. The plan's own thesis (§1), which currently has no adversary.

## How they are prioritized

Four criteria, in order: **(1) decision horizon** — does the answer inform a decision that lands in M1/M2/M3, or one that is far off?; **(2) unblocking** — does the answer unblock other topics or the pitch's credibility?; **(3) access cost** — interviews and budget questions have windows (the action circle is forming now); literature never expires but can always wait a week; **(4) the revenue math** — the $50k arithmetic (meta-plan §3.1) is the near-term reality check on everything.

---

## Tier 0 — needed for Phase M1 now (decision-forcing, some with windows)

### T1. What do impact-investor funds actually pay for software and research support?
- **Question.** Per client per year: what is the software/services budget of the action-circle funds and comparable USSEN-adjacent funds? Do they buy software, or services, or nothing?
- **Informs.** The revenue arithmetic ($50k ÷ ~20 = ~$2.5k/client/yr vs. 5–10 at $5k–10k); the choice between the (a) replace-software-spend and (b) grow-the-fund halves of the value logic; pricing in M2. The meta-plan's "risk noted" (§3.1) says explicitly: *M1 must establish this.*
- **Source.** meta-plan §3.1 (arithmetic, risk note); MOAIWI-4 (market sketch: ~200 funds, ~20 warm intros).
- **Access note.** Window: the action circle is newly formed; this question is askable inside the M1 interviews and at circle meetings. It degrades in value if asked late.
- **Priority rationale.** Decision horizon = M1/M2; unblocks pricing and the whole Moaiwi business case; access window open now.

### T2. Back-office needs and incumbent tools of impact-investor clients
- **Question.** What do these funds' back offices actually do all day? What tools do they use (accounting, portfolio tracking, impact reporting, research)? Where do they complain? What would make them switch or add a subscription?
- **Informs.** Feature prioritization for the Fortress B2B addition; the demo's content (Fortress demo + research-stack proposal); whether any incumbent is beatable on reliability *and* price.
- **Source.** meta-plan §3.1 (value logic, "listen to them complain"); MOAIWI-4 (interview method: ask what a thing like this would be for).
- **Priority rationale.** Same window as T1; together they are the "ground truth" half of M1.

### T3. What defeated previous attempts to scale cooperative networks?
- **Question.** The inventory the thesis needs: capital starvation? coordination cost? information loss in aggregation? governance capture? measurement failure? legal form? For each, what did the attempt (Mondragon and others) do, and what happened?
- **Informs.** The §1 thesis's falsifier; framing-memo-v3's central argument; Cooptopia's hypothesis refinement (§3.3); which problems Hyphae's design must actually attack (as opposed to the ones nobody has).
- **Source.** meta-plan §1 (left to research plans, Brad 2026-10-24) and §3.3.
- **Home.** Aligns with **B1** (`B1-architecture-governance-plan-v2.md`, in progress): B1's RQ2/RQ4 already hold adjacent failure modes. Suggested B1 modifications to absorb T3 are in **Appendix A**; T3 may live *inside* B1 rather than as a separate plan.
- **Priority rationale.** Unblocks the most: every later project claims to solve these problems. A literature pass is cheap and can run parallel to T1/T2 fieldwork. Note the Phase B corpus (40 works, B1 screening, P0 readings) is salvageable *input* to this topic.

### T4. Reliability and compliance targets of incumbent cloud services for funds
- **Question.** What must Moaiwi "meet or exceed" concretely — uptime, backups, security posture, data residency, SOC-2-like expectations, support responsiveness? What do funds' existing vendors promise, and what do their contracts say?
- **Informs.** The Develop/Deploy requirement spec for the business server (which drives how much the one-codebase bet has to stretch); the credibility of any reliability claim in the M1 demo.
- **Source.** meta-plan §3.1 ("meet or exceed the reliability targets defined by existing cloud-based services").
- **Priority rationale.** Decision horizon M1/M2; cheap desk research plus interview questions; prevents the demo from promising folklore.

---

## Tier 1 — feeds M2/M3 and Hyphae groundwork

### T5. Impact measurement — making "measurable" mean something
- **Question.** How can environmental, social, and financial impact be measured in a form an equity investor will accept as *measurable*? What exists already (impact-accounting frameworks, multi-capital reporting, verification practice) and what is missing for the three-legged stool?
- **Informs.** The M3 research sub-project (meta-plan §3.1); Hyphae's core promise (§3.2); honesty about what the pitch may claim before then.
- **Source.** meta-plan §3.1/§3.2; MOAIWI-3 (returns measured as contribution to network health — the "circulatory system" idea).
- **Salvage.** **B2** (`B2-impact-accounting-plan-v2.md`) is largely on-target here; the salvage list and the parts to park are in **Appendix B**.
- **Priority rationale.** Long decision horizon (M3) but high unblocking power for Hyphae; an early *scan* (not a full study) is worth doing before any pitch language uses the word "measurable".

### T6. Cooperative finance mechanics — the transcripts' unsettled design space
- **Question.** Non-voting equity at ~15–20%; internal vs. external rates of return and the buy-out of external investors; bonds vs. equity failure modes; portfolio construction (treasuries + zero-interest loans to hit blended returns); annuities for departing members; withdrawal-pause mechanics. Which of these can be formalized well enough to become Hyphae features, and which are speculative?
- **Informs.** Hyphae's modeling spec; Moaiwi's capital-allocation features; what "shared accounting and management tools" (§3.1 seeds) must eventually compute.
- **Source.** MOAIWI-1–3 (the bulk of the financial-architecture conversation); meta-plan §3.2 ("design space Hyphae's modeling has to formalize").
- **Priority rationale.** Medium horizon; overlaps with the salvageable B3 partial work (capital-allocation memo) — usable as input, plan rewritten clean.

### T7. Legal and accounting structures for the network-as-one-entity idea
- **Question.** Cooperative law on outside equity shares and their caps; "double sets of books" practice; treating internal transfers as bookkeeping among subsidiaries rather than taxable flows (with counsel); what the legal form of a *confederation* can be in the US.
- **Informs.** Hyphae's structures; the three-legged stool's legal shape; Moaiwi's accounting tools' schema assumptions.
- **Source.** MOAIWI-1 (20% share threshold, double books, tax framing, portfolio-as-single-thing); meta-plan §3.2.
- **Priority rationale.** Needs counsel eventually, so the research question must be *drafted* early even if answered late; identify what is research vs. what is a lawyer's question.

### T8. Prior art: Mondragon and cooperative-federation literature
- **Question.** How did Mondragon structure inter-cooperation, capital, and governance? What do secondary studies say about why federation-scale cooperatives plateau? What other federations exist (Emilia-Romagna, Japan's worker-coop unions, SEWA, etc.) and what are their measured outcomes?
- **Informs.** T3's inventory; Hyphae's design choices; Cooptopia's baseline.
- **Source.** meta-plan §3.2/§3.3 (Mondragon as canonical prior art).
- **Priority rationale.** Large literature, never urgent, always valuable; the Phase B corpus already contains 40 works that can seed this. Clean-sheet means the *questions* are re-derived here first.

### T9. Positioning and marketing research for the impact-investor audience
- **Question.** Does the "quantitative finance for cooperative and impact investing" frame actually land? What do ~200 impact investors respond to? Who are the reachable 20, and what messaging moved them at R&B? What does the action circle respond to?
- **Informs.** The M1 presentation content and the ongoing circle updates; later investor-facing materials.
- **Source.** MOAIWI-1 ("oh, shiny"); MOAIWI-4 (marketing strategy discussed); meta-plan §3.1 (positioning paragraph).
- **Priority rationale.** M1 horizon; partially answerable only by doing (the circle itself is the experiment).

### T15. Higher-order networks — the operative structural lens
- **Question.** What is the model landscape consistent with "higher-order networks" (graphs → hypergraphs → simplicial complexes, plus the categorical end), what do projections destroy (clique expansion ↔ cost accounting as the lossy hypergraph→graph map), which constructions **transport** across the planetary / social / financial domains, and what claim discipline applies (genuine vs effective higher-order structure; null/equivalence checks)?
- **Informs.** The public vocabulary of every artifact ("higher-order networks" replaces "hypergraph" / "symmetric monoidal category" in pitch language); T5's aggregation questions (filtrations/persistence as multi-scale measurement; homology as richer-than-scalar summary); T6/T10's toolkit (Hodge decomposition of flows — the "returns out of the circulatory system" question; higher-order Markov models for internal flows); a projection-loss demo mechanic; and the knowledge repository itself (a co-occurrence hypergraph).
- **Source.** The **B4 plan** is the direct model (clean-sheet: the questions are re-derived, but B4's anchor — Bick, Gross, Harrington & Schaub, "What are higher-order networks?", *SIAM Review* 2023 — is already reviewed 2026-10-22 and is salvageable input); meta-plan §6 (the higher-order character); MOAIWI-3 (homology extends Euler's number).
- **Priority rationale.** Cross-cutting: cheap to keep alive, expensive to retrofit; the vocabulary is needed by M1 materials; the claim discipline is a credibility guard. Keep a hard volume cap (B4's ~30-work budget is sane).

---

## Tier 2 — Hyphae, Cooptopia, and meta-process infrastructure (start now only as scouting)

### T10. The local-economy-and-network model
- **Question.** What modeling approach grounds Hyphae — input-output tables, agent-based models, network flow models, category-theoretic structures (long-term only per conventions)? What data exists for a local economy and a cooperative network? How does the value-theoretic picture in `Informatics1Readable.md` (value as a scalar-valued secondary function; price-denominated data limits; internal chart of accounts) constrain the model?
- **Informs.** Hyphae's first phase (the model, §3.2); the replacement-process analysis.
- **Priority rationale.** Hyphae's center of gravity is post-M3, but the *scouting* of data availability should precede it — models have died of data poverty before.

### T11. The replacement process — how to find candidates
- **Question.** Given a local economy and a network, how is a conventionally procured good/service identified as a cooperative-opportunity with increased environmental/social/financial value? What did similar efforts (import substitution, procurement programs) do?
- **Informs.** Hyphae's operative move (§3.2).
- **Priority rationale.** Depends on T10 and T5 (value increase must be measurable); hence later.

### T12. The 5% ceiling (Cooptopia, research-only)
- **Question.** Is the ~5%-of-flows ceiling real, and is the hypothesis (productive/organizational/information technology limits, not inherent) defensible? What does the literature on cooperative-economy scale say?
- **Informs.** Whether Cooptopia is ever more than a research project.
- **Priority rationale.** Explicitly premature by the meta-plan (§3.3); listed so it is not forgotten, not so it is started.

### T13. The four meta-processes, from systems literature
- **Question.** Where does Reflect belong in the cycle (beginning or end)? What are the named variants (Explore, etc.)? What systems literatures articulate four-stage processes (action research, PDCA/OODA, second-order cybernetics…), and what do they say about dynamically generating realizations? *(Extended 2026-10-25, QA session 1:)* a work package mapping **Castoriadis' vocabulary ↔ the meta-systems literature** (instituting/instituted vs. single/double-loop learning; paideia vs. the near-absence of subject-formation in the cycle literature — absence would itself be a finding), plus the **coupling question**: which coupling patterns let a non-party collective (the "affected public" — see T16 and the democracy-as-regime QA session) be heard in the Reflect loop and force a loop-back **without becoming a veto over Develop/Deploy**? Double-loop learning is the candidate mechanism; the public's claim is a double-loop event. *(Extended 2026-10-26, Brad's action-circle notes:)* a work package mapping **Castoriadis' terms ↔ conventional systems/software-engineering language** (e.g., vague needs → formalizable requirements is requirements engineering; paideia → subject-formation/organizational learning; the affected public → stakeholder analysis/participatory design, where the translation is lossy and the loss should be marked). Rationale: the Castoriadis vocabulary is off-putting to collaborators and investors, so it is used **for critique of conventional approaches, not adopted as terminology** (register decision 2026-10-26: Castoriadis stays internal to Reflect documents). The mapping lives in T13's directory and feeds the R.1 glossary's translation column (`../moaiwi-network-poc/action-circle-workflow-2026-10-25.md` Track A1).
- **Informs.** meta-plan §4's doctrine; the meta-plans for Develop/Deploy/Reflect; how Reflect is realized beyond the drafting process; the containment rule of T16 (public in Reflect + interrupt-on-trigger).
- **Source.** Brad, 2026-10-24 (potential research project); QA session 1 (2026-10-25) additions. **Codependent with T17.**
- **Priority rationale.** Low urgency, high leverage on the plan's own coherence; good candidate for an LLM-assisted literature pass. Promoted in importance by T16 (the Reflect process is now load-bearing).

### T17. Categorical systems theory & systemology (formalization of systems theories)
- **Question.** How do **categorical systems theory** (open systems, structured/decorated cospans, operads, coalgebra) and the **language-based systemology** tradition (general systems theory as conceptual vocabulary — Boulding's hierarchy, the viable-system line) relate, and what does formalization buy and cost relative to structured language for the *realizations* of the meta-processes?
- **Informs.** The Develop and Deploy meta-plans (**near-term, Brad 2026-10-25**): specification language for the vericoding harness (Develop), deployment/digital-twin modeling (Deploy), and meta-plan §4's "interacting agents exchanging resources over channels" — already systems vocabulary, deserving formalization or conscious informality. **Codependent with T13** (meaning without formalization stays at slogans; formalization without meaning formalizes the wrong objects).
- **Doctrine.** *Incompleteness stated up front:* every formalization is a procedural realization and therefore necessarily incomplete (converges with Castoriadis §I's fourth factor — the future excludes exhaustive codification). Formalization cannot close the regime; it can make Develop/Deploy realizations more precise where precision is possible.
- **Test cases (not greenfield).** The Plumbing language's formalized multi-agent processes; T15's categorical landscape; the corpus/graph machinery. Brad's codata work (github.com/bvenner/codata-agda) is **one lead among several, not a gate** (QA session 1, #9 amendment).
- **Source.** Brad, 2026-10-25 (QA session 1, Q8). **Tier 1** (promoted 2026-10-25: the Develop/Deploy meta-plans are near).

### T14. Research-process infrastructure (TARA architecture and sibling repositories)
- **Question.** How must TARA's architecture change to realize Research ("Explore") cleanly, and what would repositories for Develop, Deploy, and Reflect look like so the four meta-processes have aligned homes?
- **Informs.** meta-plan §4.1 (development intention); where future meta-plans live.
- **Priority rationale.** Infrastructure rather than knowledge, but it is *research into design*; fold into the knowledge-repository thread rather than starting fresh.

### T18. Neurosymbolic knowledge engineering (recorded 2026-10-26 — deferred, not started)
- **Question.** How can a hypergraph knowledge repository (TARA) develop **lower-order structures** — a glossary, more formally an ontology — out of its higher-order relations? What do the higher-order-networks tools for lowering (incidence/bipartite projections, clique expansion — with projection loss as the information cost) offer, and where does the analogy to **defunctionalization** (higher-order → first-order via reified application) hold or break? Can **Elenchus-style prover-skeptic dialogue** (Allen 2026, inferentialist semantics; bilateral commitments/denials; NMMS material bases) be extended from a single human–LLM pair to a **dialogue between two expert domains** (impact investing ↔ software engineering), and serve as the elicitation method for ontology engineering against an existing target formalism (the **Common Impact Data Standard**, CIDS)?
- **Recorded possibilities (Brad, 2026-10-26 — recorded, *not* decided).** (a) Borrow the Elenchus *method* into TARA (commitments/denials, tension detection, QUD trees as hypergraph structures) rather than adopt its GitHub-issue tooling; (b) the two-domain dialogue as human + LLM-as-counterparty speaking the other domain's language, grounded in corpus material (the A1 glossary/A2 phrasebook evidence base); (c) the **inferential-role ↔ Hoare-logic (pre/post/invariants) ↔ Verus** connection as an input to the Develop meta-plan (material bases as candidate spec artifacts for the vericoding harness); (d) CIDS as the target formalism for hypergraph → ontology lowering, defunctionalization as the analogy.
- **Informs.** The R.1 glossary's long-run method (A1/A5 of the action-circle workflow); T14 (Research-process infrastructure); T15 (higher-order networks — projection loss is the lowering cost) and T17 (systemology, codependent in spirit); the Develop meta-plan via (c).
- **Source.** Brad's notes 2026-10-25 (`writing/human/moaiwi-action-circle-workflow-notes.md`, notes 3–4); Allen, *Elenchus: Generating Knowledge Bases from Prover-Skeptic Dialogues* (arXiv:2603.06974; github.com/bradleypallen/elenchus); Common Approach impact-ontology series (commonapproach.org).
- **Priority rationale.** Brad: "a very interesting research project brewing here but we only have 3 weeks" — **deferred past the R.1 window** (the glossary proceeds with current tools and prior-art credit). Name borrowed from Allen's thesis title, "neurosymbolic knowledge engineering".

---

## Map: topics → phases and meta-plan sections

| Topic | Phase touched | Meta-plan anchor | Tier |
|---|---|---|---|
| T1 budgets/pricing | M1 → M2 | §3.1 arithmetic + risk note | 0 |
| T2 back-office needs | M1 | §3.1 value logic | 0 |
| T3 prior failure modes | all (thesis) | §1 | 0 |
| T4 reliability targets | M1 → M2 | §3.1 "meet or exceed" | 0 |
| T5 impact measurement | M3 → Hyphae | §3.1/§3.2 | 1 |
| T6 finance mechanics | M2 → Hyphae | §3.2 design space | 1 |
| T7 legal/accounting | Hyphae | §3.2 | 1 |
| T8 Mondragon/federations | all | §3.2/§3.3 | 1 |
| T9 positioning | M1 | §3.1 positioning | 1 |
| T10 economy/network model | Hyphae | §3.2 first phase | 2 |
| T11 replacement process | Hyphae | §3.2 | 2 |
| T12 5% ceiling | Cooptopia | §3.3 | 2 |
| T13 meta-process theory | all | §4 | 2 |
| T14 process infrastructure | all | §4.1 | 2 |
| T15 higher-order networks lens | all (cross-cutting) | §6 + all modeling topics | 1 |
| T17 categorical systems theory & systemology | Develop/Deploy meta-plans | §4 + T13 (codependent) | 1 |
| T18 neurosymbolic knowledge engineering | Research meta-process (glossary/ontology method) | §4.1 + T14/T15/T17 | deferred |

## T16 — the terminal-object reframing (Reflect process, opened 2026-10-25)

**Status: active Reflect process — supersedes the ranking of other topics until settled (Brad, 2026-10-25).** The program's terminal object ("grow cooperative networks") is procedural, not substantive; adopting Castoriadis' **"democracy as regime"** (explicit and lucid self-institution; individual + collective autonomy; the common good conceived by the collectivity) as the terminal object is being worked out in `democracy-as-regime/` — `castoriadis-1997-summary.md` (the 1997 essay, converted + summarized) and `reflect-terminal-object-sketch-2026-10-25.md` (the reformulation and its open questions). Consequence for other topics: T3's findings stand as evidence about the *sub-goal*; T5's metrics are instruments, not the substance; T12's 5% ceiling may be political-institutional as much as technological. The inherited framing (solidarity economy; dual power; the politics/economics division of anarchist socialism) is now an explicit object of review.

## Deferred leads (kept, not pursued)

- **Federalism vs. confederalism (political science).** A future research question should review the political-science literature on federal vs. confederal organization (Brad, 2026-10-24) — directly relevant to the Corporation-as-federation question (T3 / B1 WP1) and to Hyphae's "confederation of workplace cooperatives" (meta-plan §3.2). Entry point: Glover 2016, *Structural Cooperative Federalism* (OpenAlex W2942953341) — PDF reviewed and deleted 2026-10-24 as political theory, out of scope for B1; the lead is kept here. *(Note 2026-10-25: this lead gains priority under T16 — federalism vs. confederalism is a political-design question, and the reframing admits politics.)*

## Resolved sequencing and policy (Brad, 2026-10-24)

1. **Who runs what.** Brad proceeds with **T3** without Nic; **Nic (and maybe Rachel) coordinates T1**. Other research questions that require only desk work may be pursued while T1 is still open.
2. **T3 lives inside B1.** B1 is revised per Appendices A and C, producing **`cooperatives-governance-scaling/B1-architecture-governance-plan-v3.md`** (2026-10-24: research work promoted to its own project, `projects/moaiwi-research-program/`, one directory per research question, named with a slug of the question) — the next step and top priority.
3. **File policy.** Outside of B1, plans are **clean-sheet developments of new markdown files keyed to the research question** — *not developed now*, B1 v3 first.
4. **T13/T14 are process, not project, questions.** Pursued **in parallel** (they can impact every project stage), but less urgent for M1, which proceeds with the existing Research and Develop processes and will inform Deploy.

---

## Appendix A — Suggested modifications to `B1-architecture-governance-plan-v2.md` (align with T3)

*For Brad's review (2026-10-24). B1 is in progress; these are suggestions, keyed to B1's sections. The thesis-adversary inventory (T3) can live inside B1 rather than as a separate plan.*

1. **Make the failure-mode inventory an explicit deliverable** (B1 §1 scope, new item): "a failure-mode inventory of previous attempts to scale cooperative networks — what failed, in which case, and why." This is precisely the artifact the meta-plan's §1 delegated to research plans, and it makes B1 the thesis's adversary source.
2. **Add RQ7 (B1 §2):** *What defeated previous attempts to scale cooperative networks — which failure modes (capital starvation, coordination cost, information loss in aggregation, governance capture/co-optation, degeneration, stagnation/deadlock, measurement failure, legal-form limits) are evidenced in which cases, and what do each attempt's growth curves (members, capital, share of local flows) show about where and why growth stopped?*
3. **WP1 comparison matrix gains two columns** (B1 §3): (a) *scale achieved and growth ceiling* — share of local flows is the T12/Cooptopia baseline (the ~5% claim); (b) *failure modes attributed, with evidence*. RQ4's "degeneration pressures" is adjacent but framed as governance risk; these columns turn the inventory into an output rather than a byproduct.
4. **New synthesis output (B1 §5):** a *failure mode → addressed by?* table — each failure mode against Moaiwi / Hyphae / Cooptopia claims (claimed / not claimed / speculative). This is the meta-plan's falsifier and the argument spine of framing-memo-v3.
5. **Keyword additions (B1 §4.1, Block A):** `cooperative degeneration` · `worker cooperative failure` · `cooperative survival rate` · `cooperative growth constraints` · `Mondragon limits growth` · `solidarity economy scale limits` · `cooperative movement stagnation` · `federation failure cooperative`.
6. **v2-era bits to mend while in there:** the Gate 2 schedule and three-horizon mapping are v2 artifacts (under the v3 doctrine, plans state question/outputs/resources/answer criteria; gates belong to future Develop/Deploy meta-plans) — suggest marking them superseded rather than deleting; and §Phase-B note "his dissent" → "their dissent" (Nic, they/them).

## Appendix B — Salvage from `B2-impact-accounting-plan-v2.md` for T5

*What T5 (impact measurement) inherits, and what it should not.*

**Salvage:**
1. **WP1 framework survey + scale-commitment audit table** (framework × measured × aggregation scale × verifier × what's lost) — exactly T5's first output: what exists (IRIS+/GIIN, Impact Management Project, Impact-Weighted Accounts, SROI, integrated/multi-capital reporting…), what each promises, who verifies it.
2. **RQ4, institutional machinery** (assurance, audit, participatory validation) — maps 1:1 onto T5's "in a form an equity investor will accept": third-party audit vs. methodology transparency is T5's practical question.
3. **RQ5 + the diagnostic-not-scoring property** (M3 L451, the blood-panel criterion: measurement must guide *improvement*, not just score) and the price-ground-truth-vs-estimates verification framing (M2 L107–195) — salvage as T5's evaluation criteria, straight from the transcripts.
4. **Block A + Block E query blocks and the P0 seeds** — Espeland & Stevens (commensuration), Serafeim et al. (Impact-Weighted Accounts), Stiglitz–Sen–Fitoussi, Elkington TBL + his 2018 self-critique; gray lit: GIIN/IRIS+, IMP/Impact Frontiers, GRI, Kataly, Boston Impact Initiative, USSEN.
5. **The central tension** (B2 §8): *investor legibility wants a score; the stance resists scalarization* — keep as the tension T5 must surface, not resolve.

**Park or reroute (do not carry into T5):**
- The aggregation-stance core — aggregation-without-scale-commitment, formalisms A–D (incl. sheaf/cosheaf routes), rigs/semimodules, HoTT quality types, overconstrained reconstruction. These are the *anti-scalarization program*, a different question from investor-acceptable measurability; the formal candidates route to **T10** (the economy/network model's formalism) or stay in B2 as history.
- D1 calculator requirements, the three-horizon mapping, the Gate 2 schedule — v2 artifacts, retired.
- Standing exclusions still apply: thermodynamics/stat-mech out; category theory long-term only — so the sheaf/categorical formalisms cannot enter T5's near-term outputs.

## Appendix C — The B3 → T6 relationship (split map)

*For Brad's review (2026-10-24). Unlike B2→T5 (near 1:1), T6 is only the **finance-mechanics core** of `B3-capital-allocation-plan-v2.md`; the rest of B3 fans out into T3, T10, and T15. The map below keeps whoever writes each T-plan from re-running B3's searches — or missing their share of them.*

**Nature of the relationship.** B3 was scoped to produce a capital-allocation options memo *for the pitch* (v2); T6 is scoped to decide which of the transcripts' finance mechanics are formalizable enough to become **Hyphae features** and computations in **Moaiwi's shared accounting/management tools**. Same transcript material, different question: B3 asks what the federation's allocation posture should be; T6 asks what is real enough to build.

**Salvage for T6:**
1. **WP1 (finance-mechanism inventory)** — internal capital accounts, indivisible reserves, solidarity/revolving funds, Caja Laboral → Laboral Kutxa, Desjardins, Evergreen; the **internal vs. external returns terminology** (M3 L327).
2. **WP7 (fund construction & liquidity)** — the barbell/bundle construction (treasuries + 0% loans blended to a target rate), grants-as-revenue vs. 0% bonds, fund-as-bank mechanics (withdrawal gating ≈10%/month, suspension with illiquid assets, bank-run risk), market-rate timing, choose-your-capital doctrine.
3. **WP2's finance half** — equity-vs-bond behavior analysis, bankruptcy tolerance, failed-founder retention as design requirements. *(The degeneration canon half goes to T3 — see below.)*
4. **RQ1's hypothesis and RQ6 (the flagship)** — "internal IRR must exceed external IRR so external capital can be bought out" (M3 L415–419) as a hypothesis to test; "returns out of the circulatory system — and how much can be withdrawn without killing the organism" (M3 L403, 435).
5. **Open question 5 of B3 — the debt-posture inconsistency** (debt proposed M1 L275, condemned M3 L331, used in the barbell M2 L403). This is precisely a transcripts-unsettled item; **T6 owns it as an explicit open question**, resolved into a coherent option set rather than a silent pick.
6. **Search material** — Block A and Block E query strings (incl. the *(v2)* additions: patient/catalytic capital, PRI, grant recycling, barbell, liquidity gating, bank-run), the Ellerman seed, MONDRAGON/Laboral Kutxa/Desjardins gray-lit targets.

**Split map — where the rest of B3 belongs:**
- **WP2 degeneration canon** (Ward/Domar/Vanek/Meade + empirical persistence evidence) → **T3**. Degeneration is a candidate failure mode in T3's inventory; B3's "standing-objection answer set" is inventory material, and Block B's queries (labor-managed firm theory, degeneration thesis, worker cooperative persistence) travel with it.
- **WP3 (allocation as decision process) + WP4 (surplus/fund design via cooperative game theory — core, Shapley/Owen, cost-sharing, claims/bankruptcy; + exit/secession transfers)** → **T10** (the economy/network model's decision machinery) with a secondary feed to Moaiwi's capital-allocation features.
- **WP5 (network dynamics & resilience; panarchy)** → **T15/T10**. Note the v2 decision that "resilience" stays out of the pitch was a register decision for v2 artifacts; under v3 the material is simply research content and the register question is open again (T9 territory).
- **WP6 (BPMN lifecycle process model)** → not a research topic: it is tooling spec for the shared accounting/management tools (and its supply-chain/ERP tooling precedents are Develop-side references).
- **RQ5 (network effects on allocation calculus)** → split: the empirical half to T10, the industrial-symbiosis/replacement half to T11.

**Scope nuance (record so it is not lost):** the 2026-10-22 **equity-only** decision was a *pitch posture* for v2 artifacts. T6's research scope should cover the full mechanics the transcripts entertain — including debt, 0%-loans, and the barbell — because Hyphae must model whatever the design space contains. Equity-only governs what is said to investors; it does not narrow what is studied.

**v2-era items retired with B3:** Gate 2 schedule, three-horizon mapping, and the D2/D3 demo handoffs (the v3 near-term demo is the Fortress demo of M1; D-numbered demos are v2 layout).

