---
title: "Review of MOAIWI-1–3 vs framing memo and B1–B3 plans: Nic's unincorporated ideas + proposed changes"
date: 2026-10-22
kind: review
project: moaiwi-network-poc
---

# Review of MOAIWI-1–3 against the current proposal

**Status:** proposed changes only — **nothing applied** to `framing-memo.md` or `research-plans/` yet. Awaiting Nic/Brad approval (gate).

**Sources:** `writing/human/MOAIWI-1.md`, `MOAIWI-2.md`, `MOAIWI-3.md` (Nic = Speaker 0, Brad = Speaker 1). Line refs cite those files as `M1 L159` etc.

**Targets examined:** `projects/moaiwi-network-poc/framing-memo.md`, `research-plans/B1|B2|B3-*.md`. Adjacent proposals (meta-plan, team) in §7 — outside the requested scope but forced by the transcripts.

---

## 1. Executive summary

1. **The pitch's horizon structure is missing.** Nic explicitly structures the pitch as short / medium / long term with deliverables on the short-term side (M3 L11–19, 43, 67). The framing memo's workshop flow has no horizon structure.
2. **The wedge product is missing.** Nic's near-term product is a financial-analysis / back-office stack **for impact investing funds** (self-serve SaaS ≈ $10K/yr, or cooperative membership; built on "Fortress"; shared back office) — not the federation-wide modeling platform in the memo's §2 (M2 L115–147; M3 L43, 51, 67). The memo's "modeling as a product" is currently too vague to be this.
3. **The actual return mechanism is missing.** Flow/market analysis of an area's cooperatives → unmet cooperative demand → formation **with pre-identified customers** → "plugging holes in the cooperative network is exactly the investment thesis" → above-market returns (M1 L127–167, 203, 219). This is the concrete machinery behind "top-down capital direction that raises IRR."
4. **A data flywheel is missing entirely.** Impact funds *want* to share books (the room's reaction: "we should have been doing this for years; we lacked a quant"); funding conditions require use of the tech stack; data from all applicants, not just recipients; gradual privacy deepening; explicitly "not a surveillance state" (M2 L255–339, 343).
5. **Instrument and fund mechanics are missing.** Non-voting equity ≈10% (≤20% co-op ceiling; double books); **equity-not-bonds doctrine**; barbell construction (treasuries + 0% loans); grants-as-revenue vs 0% bonds; fund-as-bank (withdrawal gating, bank-run risk); market-rate capital deferred ≈3 years (M1 L235–275; M2 L355, 387–419; M3 L75, 163, 331–347, 403, 491).
6. **The returns doctrine is sharper than the memo's.** *Minimize external returns, always*; internal IRR must exceed external IRR so external capital can be bought out and replaced by internal capital; Siobhan's principle ("an impact investing fund that prioritizes returns to investors is not an impact investing fund, categorically"); satisficing capital demand + optimizing community betterment (M3 L19, 315, 415–419).
7. **Register conflict — needs Nic's decision.** Nic wants quant-shiny finance language ("quantitative finance but for cooperative and impact investing"; "our medium term pitch does not involve the word solidarity"), while Brad warns that a returns-maximizing pitch reads as parasitic and needs "a much, much better pitch" (M2 L295; M3 L67, 303–315). The memo currently sides with the R&B-movement register only.
8. **Formal inputs for B2/B3 are richer than the plans assume:** cost accounting as the lossy hypergraph→graph map ("the single most important target"); price's ground-truth uniqueness vs estimate-laden impact metrics; overconstrained estimation; R-modules over rigs (no inverses / minimum order quantities); Benanav's multi-criteria economy as an off-the-shelf frame (M2 L27, 107–235; M3 L255, 479).

**Scope flag (see §5.1):** Nic's one-month deliverable (prototype stack + 2–3 impact-fund interviews, to unlock continued funding — M2 L131–147) overlaps but is **not the same** as the meta-plan's 30-day conference sprint. These need reconciliation before Phase B downloads.

---

## 2. Nic's ideas NOT in the current proposal (consolidated)

Grouped; `[Nic]` marks the proposer. "Destination" = where the proposed change would land.

### 2.1 Pitch & product

| # | Idea | Refs | Destination |
|---|---|---|---|
| N1 | Three-horizon pitch structure (short: software prototype + "glimpses" of alternative finance; medium: deployment/integration with existing beta funds; long: the investment vehicle) | M3 L11–19, 43, 59–67 | framing-memo §8 rewrite |
| N2 | Wedge product: self-serve SaaS financial-analysis/back-office stack for impact funds, ≈$10K/yr or cooperative membership ("shared maintenance"); built on existing stack ("Fortress") | M2 L115–147; M3 L51, 67 | framing-memo §2 (revenue line); B-plans fieldwork |
| N3 | MVP = customer discovery: 2–3 interviews with impact-fund owners to enumerate their software needs ("barely viable product"); Nic + Rachel | M2 L131–139 | meta-plan (§7); B-plans fieldwork |
| N4 | Impact funds are the **customer**; co-ops are the **investments**; fund investors are a third party — three distinct roles the current memo blurs | M3 L11–19, 151 | framing-memo §6 glossary + §2 |
| N5 | Medium-term pitch bans the word "solidarity"; tangible benefits first ("shared back office") | M3 L67, 115 | framing-memo §5 (register) |

### 2.2 The return mechanism ("the investment thesis")

| # | Idea | Refs | Destination |
|---|---|---|---|
| N6 | Flow/market analysis of an area's cooperatives = feasibility analysis on businesses that could exist locally; closed market because co-ops buy from each other | M1 L127–159 | framing-memo §2; B3 WP |
| N7 | Identify services all co-ops buy / overloaded demand → "start this exact cooperative with these inflows and outflows" → fund it; **pre-identified customers, not just market demand** | M1 L159–219 | framing-memo §2 |
| N8 | "Plugging holes in the cooperative network is exactly the investment thesis that gets you corporate dollars"; the entire point is to attract capital to cooperative markets | M1 L163–203 | framing-memo §2 (thesis sharpening) |
| N9 | Incubation model: "we will write you less, but give a lot more support"; warm intros to network co-ops; be a coordinating example; YC-style program "if Y Combinator wasn't evil" | M1 L19, 219, 275 | framing-memo §2/§8; B1/B3 |
| N10 | Customers pay a premium for value-aligned supply (Moon Shell pricing); co-ops prefer buying from co-ops; the cooperative marketplace is currently too small | M1 L367 | framing-memo §2 supporting point |

### 2.3 Instruments & fund mechanics

| # | Idea | Refs | Destination |
|---|---|---|---|
| N11 | Non-voting equity ≈10% target (YC's 7+3 → 10% benchmark; 15% floated; "we might have to take more"); **≤20% outside ownership before it stops being a cooperative**; double set of books; some structure as debt, flexible | M1 L235–275 | B1 WP4; B3 WP1 |
| N12 | **Equity-not-bonds doctrine:** bonds = capped upside/unlimited downside, vulture behavior, interest-death spirals, can force bankruptcy; equity = capped downside, tolerant of near-bankruptcy, cannot bankrupt the firm; but equity creates unicorn-growth toxicity; choose equity when your analysis says the firm will do well | M2 L419 (full); M3 L163, 331–347, 403, 491 | B1 WP4; B3 WP2 |
| N13 | Bankruptcy tolerance as design requirement (microlending harm avoided; "no billy clubs"); failed good-faith founders remain network assets | M3 L159, 355–367 | B3 WP2; framing-memo §5 (objection posture) |
| N14 | Barbell/bundle construction: 50% treasuries + 50% 0%-interest loans → blended 3% vs a 3% raise; grants cover return gaps; borrow-at-9% flagged as wipe-out risk; community raises at lower rates; "convert money now into money later" | M2 L387–403 | B3 WP1 |
| N15 | Grants ≠ 0% bonds: grants expect 100% loss ("almost more like revenue"); grants-then-lend; grants + 10% debt variant | M2 L483; M3 L75 | B3 WP1 |
| N16 | Fund-as-bank: every fund can be dissolved by a bank run; withdrawal-suspension fine print (10%/month gating; pause with illiquid assets); leverage lines | M2 L411–419 | B3 WP (new) |
| N17 | Market-rate capital now is a bad idea; revisit when the 10-year is ≈2% (≈3 years) | M2 L355 | B3 WP1; framing-memo §5 |
| N18 | Choose-your-capital doctrine: a strong return thesis buys *choice* of funders (grants, public banks, philanthropic below-market bonds, mission-aligned capitalists); weak rates attract only bad capital | M3 L427 | framing-memo §5/§8; B1 |

### 2.4 Returns doctrine & measurement theory

| # | Idea | Refs | Destination |
|---|---|---|---|
| N19 | **Minimize external returns, always**; internal IRR must exceed external IRR so external investors can be bought out and replaced by internal capital (the precise meaning of "raise internal rates of return") | M3 L327, 415–419 | framing-memo §2 sharpening |
| N20 | Siobhan's principle: "an impact investing fund that prioritizes returns to investors is not an impact investing fund, categorically"; returns recycle to the community (more get to invest) | M3 L315 | framing-memo §5 (tension resolution) |
| N21 | Satisficing capital demand (don't go bankrupt, persist, service bonds) + optimizing material community betterment as the fund's objective structure | M3 L19 | B2/B3 (theory frame) |
| N22 | "Material returns on a community's investment that can keep the fund going" = the thing to maximize; return-maximization tactics empirically produce *worse* community outcomes than generosity (practitioner testimony) | M3 L99, 243 | framing-memo §5; B2 |
| N23 | Goal is not to pay fund investors back; high returns mean more people get to invest (grant→lend→return→expand loop) | M3 L315 | framing-memo §5 |
| N24 | **Returns should come out of the circulatory system, not organ-by-organ extraction** — named explicitly as an unsolved open question ("how exactly does that work?") | M3 L403, 435 | B3 research-proposals list |
| N25 | Internal capital recycling: co-op revenues invested in the main institution; "your ultimate source of capital is other organs in the network" | M3 L443 | B3 WP1 |
| N26 | Single-metric health scores are useless for *improving* health (blood-panel analogy); measurement must be diagnostic, not just scoring; fund what the ecosystem needs (new liver to clear the proteins) | M3 L451 | B2 (property of candidate formalisms) |
| N27 | Non-scalar money thesis: scalar valuation (not merely "money") is the root pathology; any scalar currency produces the same collapses; enriching scalar money into richer forms (rigs/semimodules; **no inverses → minimum order quantities**; HoTT "quality types"; internal accounting "richer than money, like homology groups extend Euler's number") | M1 L23–47, 87; M2 L235; M3 L459–483 | B2 (formal toolkit + stance quote) |
| N28 | Price's mathematical uniqueness: price observable without the production function (eBay test); impact metrics are estimate-laden with no ground truth; accounting has a floor (market prices); cost accounting is the partially-observable black hole between revenues and prices | M2 L107–203 | B2 (theory section) |
| N29 | Overconstrained reconstruction: financial statements + material constraints (patents, real estate, wages) + market prices can jointly pin impact estimates; solved at scale by gradient descent; "the math is limited by the numerical methods that exist in 2026" | M2 L211–227 | B2 (candidate formalism) |
| N30 | Internal-currency dynamics: all-dollar internal accounting forces below-market internal prices ("central router" problem) and makes breakaway easy; non-dollar internal instruments add deliberate inflate/deflate for community health, signal buy-in, and bind the network | M3 L483 | B1/B3 (governance + instrument research) |

### 2.5 Data, standards, partnerships

| # | Idea | Refs | Destination |
|---|---|---|---|
| N31 | Books-sharing flywheel: impact funds want shared books ("such a good idea… for years… we lacked a quant"); portfolio + applicant data; tech-stack use as a **condition of funding**; "gradual privacy unlearning" (Brad); explicitly "not a surveillance state"; observability sold as mutual benefit (incl. tax help) | M2 L255–339, 343–347 | new B-plan WP (B2/B3); framing-memo §2 |
| N32 | Standard-setting ambition: shared calibrated impact model → propose as *the* standard for impact measurement (Brad, endorsed in-context) | M2 L271 | B2 (research proposal) |
| N33 | Public-banking partnership: below-market pools have the same allocation problem; "Mobos" has context; the stack serves them too | M2 L419 | B1/B3 partnerships |
| N34 | PCB-manufacturer component-sourcing / logistics software as the model for network material-flow tooling (connection counts comparable to a whole co-op network) | M3 L251 | B3 (WP6 reference + keywords) |
| N35 | Fieldwork list: Wellspring Cooperative head (economics professor, UMass Amherst) 1:1; Sandy (Center for People's Economics); Moon Shell (Sid) books access; "the wealth fund" books; Center for Community Wealth; students' Thursday group | M1 L367–391 | meta-plan fieldwork; B-plans gray lit |
| N36 | Prototype pragmatism: "pick a bad formalism to begin with and generate a bunch of pretty charts and graphs"; basic accounting model suffices; working model + simulation in a month with LLM assist | M1 L375–399 | demos (D0–D3) scoping |

## 3. Brad's additions in these conversations (also not yet in the proposal)

| # | Idea | Refs | Destination |
|---|---|---|---|
| B1 | Cost accounting = lossy condensation of a hypergraph/SMC production process to a single-channel graph; "the single most important target" (the map where material/energy flows become financial flows) | M3 L255, 479 | B2 (candidate formalism + WP) |
| B2 | Multi-criteria economy (Aaron Benanav) as an off-the-shelf framework to repurpose as multi-criteria impact investing in a month | M2 L27–71 | B2 seeds + keywords (P0) |
| B3 | POMDP/RL as first-order approximation of capitalist pricing (Markov structure), with higher-order corrections; "market socialist" use of the same math | M2 L111, 215 | B2/B3 keywords |
| B4 | Internal vs external returns vocabulary (for LLM and deck clarity); Treaty-of-Detroit framing of internal/external investor tension ("you can't just buy labor peace") | M3 L327, 423 | framing-memo §6 glossary |
| B5 | Network firm / "East India Company more than hedge fund"; relations of production (hierarchical corps) mismatched to forces of production (hyperlocal distributed production) | M3 L351 | framing-memo §2/§3 (theory support) |
| B6 | Dual-power critique: total independence is a purity test; "growing up in the ruins of the old"; regulate the boundary like a living system (porous but viable) | M3 L375 | framing-memo §5 (objection posture) |
| B7 | Microlending harm lesson; bankruptcy exits must not harm the fund | M3 L159 | B3 WP2 |
| B8 | Ellerman internal capital accounts; firm as object in a category of firms *with* internal structure (petit topos / functor of points / test spaces) | M3 L447 | B3 seeds + B2 formal toolkit |
| B9 | Secession/exit conflict: healthy units may "go independent"; growth funded from profitable parts draws down workers' internal equity → conflict management is structural | M3 L455 | B1/B3 (governance research) |
| B10 | Resilience as a "pirate term" for governments/grants; co-ops as low-beta hedge (better in downturns, worse in upturns) — **contested by Nic, see §5** | M3 L71, 199–211 | framing-memo §5 (pending decision) |
| B11 | Economic democracy (rigorous, self-governance) vs solidarity economy (self-organized) split; bridging the gap is important | M3 L175–191 | B1 keywords (already partly present) |
| B12 | Mondragon as prior art: "a cooperative network on the inside and a firm on the outside"; Sid's endorsement as audience evidence | M3 L439 | B1 (comparison dimension) |

## 4. Confirmed — already covered by the current proposal

- Multi-capital modeling (financial + planetary + social) as the corporation's product and edge (M2 L83, M3 L107 aligns with memo §2).
- Non-reduction of impact to a single scalar = exactly B2's aggregation stance (M2 L75–99 confirms it; adds N28's ground-truth argument).
- Material/value flows between cooperatives as the modeling object (M1 L111–115 ≈ B3/B2 scope; typed resources and conversions in a copy-discard SMC — M1 L379–387 — fits B2 toolkit).
- Bottom-up formation vs top-down direction tension (memo §3) and "attract capital to cooperative markets" (memo §2) — confirmed but mechanism missing (N6–N8).
- Non-voting equity as an investor instrument (B1 WP4 option list) — confirmed; N11 adds the parameters.
- Debt-vs-equity instrument candidates (B1 WP4) — confirmed; N12 adds the doctrine.
- Modeling-as-revenue-line (memo §2) — confirmed; N2 makes it concrete.
- Synthetic illustrative data for demos — stands; but see §5.4 on real books.

## 5. Conflicts and open tensions (need Nic's decision)

1. **Scope collision (highest priority).** Nic's one-month goal is a *prototype stack + impact-fund interviews to unlock funding* (M2 L131–147; M3 L43). The meta-plan's 30 days are the *conference pitch*. Options: (a) the conference becomes the venue where the prototype is shown ("glimpses of the future" alongside D1–D3); (b) the prototype becomes the short-term deliverable *in* the deck while D1–D3 remain the workshop demos; (c) separate sprints. Decision needed before B-track downloads.
2. **Pitch register.** Nic: quant-shiny finance language ("quantitative finance but for impact investing"; medium pitch sans "solidarity"). Brad: a returns-forward pitch to this audience reads parasitic ("you need a much, much better pitch") — M3 L303. Proposal: **horizon-dependent register** (finance/product language for short+medium; economic-democracy language for long term), with Siobhan's principle (N20) as the bridge. Decision needed; framing-memo §5 depends on it.
3. **Resilience framing.** Brad: pirate term, low-beta hedge, countercyclical. Nic: "a bet on resilience is a fundamentally bearish bet on the overall economy"; countercyclical = bad when procyclical; labels don't attract investors (M3 L291–299). The word appears nowhere in the pitch docs today; if Brad's side wins it enters §5/§8, if Nic's side wins it stays internal (B3's panarchy use is unaffected).
4. **Real books vs synthetic data.** Nic wants real co-op books now (M1 L391). Demos remain synthetic per the locked decision — proposal: add a **validation track** (real books inform the schema and later credibility) without changing demo data.
5. **Debt posture is inconsistent within Nic's own positions:** "we might have to take more… structure some of it as debt" (M1 L275) vs "debt is a bad investment vehicle" (M3 L331) vs barbell uses 0% loans (M2 L403). B1/B3 need one coherent instrument-posture option set.
6. **Tax-engineering posture** (M1 L315–351, 403–415; M3 L395): subsidiary/consolidated framing, equal-value swaps, instrument wrapping, "obey the spirit + letter," catch-and-chase enforcement analysis. Proposal: record as **research questions with counsel flags** in B1 (tax treatment of inter-co-op flows), and keep the *pitch* at the Graeber-style "reduce dependency on extracting capital" level — the "runes/enchanting financials" phrasing is transcript voice, not deck language.
7. **Team roster.** Rachel (MVP interviews, M2 L131) is not in the meta-plan roles. Add.

## 6. Proposed changes by document

### 6.1 `framing-memo.md`

| § | Type | Proposed change |
|---|---|---|
| §2 | Add | Mechanism paragraph: flow/market analysis → unmet cooperative demand → formation with pre-identified customers → "plugging holes in the network" as the source of above-market returns (N6–N8). Sharpen the thesis phrase "raise internal rates of return" to the precise doctrine: *internal IRR must exceed external IRR so external capital can be bought out and replaced by internal capital; external returns are minimized, always* (N19). |
| §2 | Modify | Revenue line becomes two named layers: **short-term wedge** (financial-analysis/back-office stack for impact funds — SaaS ≈$10K/yr or cooperative membership) and **long-term platform** (the multi-capital modeling capability) (N2, N4). |
| §5 | Modify | Replace the single-register guidance with a **horizon-dependent register** (pending §5.2 decision): quant/finance language for short+medium horizons; economic-democracy language for long term. Insert Siobhan's principle as the resolution device for the returns tension (N20). Add N18 (return thesis buys choice of capital). Hold "resilience" out of pitch language pending §5.3. |
| §6 | Add (glossary) | "internal returns / external returns"; "satisficing capital"; "the technology stack" (abstract name for the fund-facing product); "the cooperative supply chain / alternative production model" as naming-capture targets (M2 L531–547); distinct role labels for **funds served**, **cooperatives funded**, **fund investors** (N4). |
| §8 | Rewrite | Replace the 10-step flow with Nic's three-horizon spine: *Horizon 1 — the problem (fiduciary single-scalar accounting; impact funds underserved) and the stack prototype; Horizon 2 — deployment with beta funds, shared back office, books/observability; Horizon 3 — the investment vehicle: flow analysis, hole-plugging thesis, equity-not-bonds, internal/external returns; then the R&D program and "what we ask of this room."* Demo landing points re-map: D1 under Horizon 3 impact story; D3 under Horizon 1/2; D2 under Horizon 3. |
| §10 | Add | Hand B3 the open-mechanism question N24 ("returns out of the circulatory system"); hand B1 the instrument doctrine (N11, N12) and tax-treatment dimension (§5.6). |
| — | Deletions | **None required.** No current text contradicts the transcripts; the contested items ("resilience," register) are not yet in the docs, only proposed earlier in conversation. |

### 6.2 `research-plans/B1-architecture-governance-plan.md`

- **WP1:** add comparison dimensions — tax treatment of inter-co-op flows (consolidated accounting, transfer pricing, equal-value swaps); "network inside, firm outside" (Mondragon, B12); internal capital accounts (Ellerman, B8); exit/secession governance (B9).
- **WP4:** add instrument doctrine properties — equity-not-bond selection rule (N12); non-voting 10% band + ≤20% outside-ownership ceiling + double books (N11); buy-out/internal-vs-external dynamics (N19); withdrawal mechanics (N16) cross-referenced to B3.
- **Keywords (Block A/B additions):** `non-voting equity stake` · `outside ownership limit cooperative` · `dual class shares founder` · `internal capital accounts Ellerman` · `democratic firm` · `transfer pricing intercompany` · `consolidated tax return affiliates` · `share buyout investors` · `secession cooperative exit` · `Treaty of Detroit profit sharing`.
- **Gray-lit additions:** Wellspring Cooperative (UMass Amherst) · Center for People's Economics · public-banking partners (N33) · Ellerman's *The Democratic Firm* (seed).
- **Open-question update:** add "how visible is the tax-engineering posture in the pitch?" (§5.6).

### 6.3 `research-plans/B2-impact-accounting-plan.md`

- **Formal toolkit (WP3):** add two candidate formalisms — **(e) cost accounting as the lossy hypergraph→graph map** (B1: the target layer where material/energy becomes financial) and **(f) overconstrained reconstruction** of impact metrics from financial + material constraints (N29). Add **diagnostic-not-scoring** as a required property of every candidate (N26), and the price-uniqueness / ground-truth asymmetry argument (N28) as the memo's theory framing.
- **Keywords (Block A/B/C additions):** `multi-criteria economy Benanav` · `satisficing bounded rationality` · `material flow cost accounting MFCA` · `activity based costing` · `cost accounting material flows` · `hybrid unit input output` · `constraint based estimation inference` · `POMDP` · `reinforcement learning resource allocation` · `rig semimodule algebraic economics` · `typed resource flows` · `homotopy type theory quality` · `internal accounting non monetary` · `open book accounting supply chain`.
- **Seeds (add):** Benanav (multi-criteria economy — verify exact work at download) — P0; Simon (satisficing/bounded rationality) — P1; ISO 14051 / MFCA — P2; Ellerman (internal capital accounts) — P2 cross-list.
- **Stance note:** quote N27 ("the goal of the software is to understand your impact, not reduce it to a single scalar" — M2 L83) in the memo's framing, with the rig/semimodule line as a formal direction.
- **Seeds (add, long-term tier) — per Brad 2026-10-22:** **William Lawvere** — quality types vs quantity types (the M1 L87 "quality type" remark; verify exact work at download, e.g. "Taking categories seriously") — P2; **G. A. Kavvos**, "Modalities, Cohesion, and Information Flow" (arXiv:1809.07897; *Proc. ACM Program. Lang.* 3, POPL 2019; DOI 10.1145/3290333) — P2 — information-flow/noninterference results via classified sets as a (weak) model of Lawvere's axiomatic cohesion: prior art for transporting structural machinery between a cohesion framework and a security/observability domain.
- **Scoping decision (Brad, 2026-10-22): categorical semantics is on the long-term path only.** Lawvere/cohesive-topos-level machinery is *not* needed for the short- or medium-term horizons; near-term formal candidates stay combinatorial/statistical (multi-scale aggregation maps, partial orders/MCDA, MFCA, overconstrained reconstruction). The categorical line appears in the R&D agenda as long-horizon research proposals. Keywords parked for when the corpus grows: `quality types quantity types` · `cohesive topos` · `information flow categories`.

### 6.4 `research-plans/B3-capital-allocation-plan.md`

- **New WP: fund construction & liquidity** — barbell/bundle construction (N14); grants-as-revenue vs 0% bonds (N15); fund-as-bank mechanics: withdrawal gating, bank-run risk, illiquid-asset pauses (N16); market-rate timing (N17); choose-your-capital (N18).
- **WP2 additions:** equity-vs-bond behavioral analysis (N12); bankruptcy tolerance + failed-founder retention policy (N13, B7); internal capital recycling (N25).
- **Research-proposals list:** seed it with **N24** ("returns out of the circulatory system — how exactly does that work?") as the flagship open problem; add secession/exit and inter-unit transfer conflict (B9).
- **Terminology:** adopt internal/external returns vocabulary (B4) throughout the memo and D3 dashboard labels.
- **Keywords (Block A/E additions):** `patient capital impact` · `catalytic capital` · `program related investment` · `grant recycling foundation` · `barbell portfolio construction` · `fund liquidity gating withdrawals` · `bank run mutual fund` · `internal capital accounts cooperative` · `cooperative supply chain` · `supply chain contract management software` · `ERP material requirements planning` · `PCB component sourcing software`.
- **Seeds (add):** Ellerman, *The Democratic Firm* — P1; Simon — P2 cross-list.

## 7. Adjacent proposals (beyond the two requested document sets)

- **Meta-plan:** add the three-horizon spine to Phase E; add a **fieldwork/validation workstream** (N3: impact-fund discovery interviews; N35 conversations; N31 books access) — this is also the lean-exploration Nic asked for (M2 L571); add Rachel to the role roster (§5.7); decide the §5.1 scope collision before setting demo scope.
- **Demos:** keep D1–D3 as-is; consider a "D0" artifact — the fund-stack prototype or a screenshot-level preview of it (N2, N36) — subject to §5.1.
- **Workspace process:** the "uniform LLM prompt from contentious conversation" problem (M3 L239) is a workspace-level note candidate (`writing/machine/`, kind: research-plan) and possibly an agent-harness thread item; the transcription-tooling question is resolved (transcripts exist; "pay money to solve" was accepted — M3 L507).

## 8. Transcript ambiguities (verify before citing in formal docs)

Speech-to-text names/terms to confirm with Nic: "Marie"/"acquirers" (M1 L95); "Rich Lee" (M2 L23); "Mobos" — public-banking contact (M2 L419); "quantum economy" (M2 L339 — likely "quant economy"); "My Carriza" — a former startup of Nic's (M3 L363); "Bob" (M2 L547); "Siobhan" spelling (M3 L315); "Fortress" — the existing software stack (M2 L139, M3 L67). Speakers confirm: Sid = Moon Shell Pizza (M1 L391); "mom" and Mel ("pirate communism") as informal audience validation (M2 L551). **Resolved:** "Lebert" (M1 L87) = **William Lawvere** — transcription error per Brad (2026-10-22); the remark is Lawvere's distinction of homotopy types as *quality types, not quantity types*. Lawvere — US mathematician and committed socialist, a very important figure — belongs in the formal-toolkit conversation around Nic's non-scalar "quality type" language.

## 9. Suggested application order (after approval)

1. Resolve §5.1 (scope) and §5.2 (register) — everything else in §6 depends on them.
2. Apply framing-memo §6.1 changes; re-gate as a Gate-1 revision for Nic.
3. Apply B-plan §6.2–6.4 changes before Phase B downloads (they change keywords and seeds).
4. Meta-plan/fieldwork updates (§7) with the next meta-plan touch.
