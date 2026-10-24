# B4 research plan — higher-order networks (cross-cutting topic)

**Status:** research plan (cross-cutting topic; pre-download gate — no references downloaded until reviewed) · 2026-10-22 · Topic memo due **Gate 2, Mon Nov 2** alongside B2 · Brad drafts, Nic reviews. Anchor paper reviewed 2026-10-22 (below).

## 0. Why this topic (Brad's framing, 2026-10-22)

- **Mindshare.** "Higher-order networks" has far more mindshare than our internal formal vocabulary ("hypergraph", "symmetric monoidal category"). It is the natural public term for the deck.
- **A landscape, not a single formalism.** A broad landscape of categorical and combinatorial models is consistent with the concept — which fits our "options, never decisions" posture exactly.
- **Transdisciplinary transport.** Higher-order networks are an active idea across fields; the shared vocabulary can **transport ideas between the planetary, social, and financial universes of discourse** — the three domains of the modeling platform.

The anchor paper's own ambition matches ours almost verbatim: it seeks "a common language for a number of research areas that have predominantly been considered separately" and advocates "cross-fertilization" between communities (Bick et al., §1, §6).

## 1. Anchor source (reviewed)

**Bick, C., Gross, E., Harrington, H.A., Schaub, M.T., "What are higher-order networks?"** — arXiv:2104.11329 (v3, 2022); *SIAM Review* 65(3), 686–731 (2023); DOI 10.1137/21M1414024.

What it gives us (verified in the paper text):

- **Umbrella definition.** Polyadic/non-dyadic relations appear in the literature as "supra-dyadic, nonpairwise, higher-order, or simplicial" — collectively **higher-order networks**: networks with interactions involving three or more entities jointly (buyer–seller–broker is its own socio-economic example, §1).
- **The model landscape it covers:** graphs (dyadic baseline) → **hypergraphs** (edges = arbitrary subsets of vertices; k-uniform; directed/weighted variants) → **simplicial complexes** (hypergraphs closed under inclusion; oriented simplices; directed topology); plus explicit "missing links" families: multiplex/multilayer networks, **higher-order Markov models for flows of "information, energy, mass, money"** (path-dependent flows!), higher-order graphical models/MRFs, (simplicial) signal processing, tensor models. The categorical end of the landscape (hypergraph categories, symmetric monoidal categories, structured/decorated cospans, ologs, sheaves) is adjacent literature the survey does not cover — that is our own contribution to the map (WP2).
- **Three methodological contexts** (§3–5): (i) topology/geometry of data — persistent homology, Čech filtrations, **Hodge-Laplacians**; (ii) statistical models of relational data — probabilistic models over hypergraph/simplicial spaces, null models (co-authorship example); (iii) higher-order network dynamics — synchronization, contagion, ecological coexistence, neural systems.
- **Two arguments we will reuse directly:**
  1. **Projection loses meaning** (§6): interpreting data as graphs "out of necessity… the cost of such methods… is that higher-order relationships and structure is lost, as well as some meaning" — the paper compares collaboration networks analyzed as graphs vs hypergraphs. This is exactly Brad's claim that **cost accounting is the lossy hypergraph→graph projection** (M3 L255, 479) and grounds B2 candidate (e).
  2. **Richer summaries than scalar size measures** (§3): the Euler characteristic is a coarse measure; **homology "is closely related to the Euler characteristic, but provides a more detailed account"** — the formal counterpart of Nic's "something richer than money, like the same way that homology groups extend Euler's number" (M3 L483). Persistent homology additionally "avoids selecting a specific threshold… by analyzing data at multiple scales" (Fig 1B) — a direct fit for the **aggregation stance** (no prior commitment to a scale).
- **The credibility caveat** (§5.2–5.4, Q1–Q3): higher-order expansions are **not unique**, and "effective" higher-order coupling can arise from coordinate changes of an additively coupled (dyadic) system; if a system is coordinate-equivalent to a dyadic one, no higher-order description is necessary. Claims of higher-order structure need equivalence/null checks. We adopt this as a discipline for our own claims (and name it in the pitch as rigor, not weakness).

## 2. Relationships to existing tracks

- **B2 (impact accounting):** candidate (e) cost-accounting-as-projection gains its formal vocabulary (clique expansion / graph projection vs keeping hyperedges intact); candidate (c) sheaf/local-to-global connects to the categorical landscape; the aggregation stance gains filtrations/persistence as a multi-scale construction. Topic memo feeds B2's research-proposals list.
- **B3 (capital allocation):** WP5/WP6 gain a dynamics vocabulary (higher-order contagion/coexistence; higher-order Markov models for path-dependent internal flows); the flagship "returns out of the circulatory system" question gains a candidate toolkit (Hodge decomposition of flows into gradient/cyclic/harmonic parts).
- **B1 (architecture/governance):** governance bodies and funding bundles are naturally hyperedges (a decision is a group interaction; the barbell construction is a composite instrument — a higher-order object).
- **Demos:** D2's simulator could expose a projection toggle — the same federation shown as higher-order flows vs pairwise projection, with the loss made visible (the paper's graph-vs-hypergraph comparison as a demo mechanic).
- **Deck vocabulary:** "higher-order networks" / "group interactions" / "multi-party exchange" replaces "hypergraph" and "symmetric monoidal category" in pitch artifacts; the formal terms stay in the research appendix.
- **The knowledge repository itself** is a co-occurrence hypergraph — this topic also formalizes our own infrastructure.

## 3. Scope & deliverables

1. **Topic memo** (≤3 pp, lands in `options/` alongside B1–B3 memos) due Gate 2 (Nov 2).
2. **Vocabulary mapping table:** public term ↔ formal object ↔ instance in the Federation (see §6 skeleton).
3. **Model-landscape table:** hypergraph / simplicial / cell complex / multilayer / tensor / SMC-hypergraph-category / olog / sheaf — what each preserves and loses; which our candidates use.
4. **Cross-domain transport table:** which constructions carry between planetary, social, and financial domains (incidence/flow structure; projections as lossy accounting maps; homology/Hodge summaries; filtrations as multi-scale aggregation).
5. **Research-proposal candidates** contributed to B2/B3 lists (§5).
6. **Deck-language guidance** for framing-memo §6 glossary (a future edit, gated).

Out of scope: choosing a formalism (that stays B2's options decision); implementing new math; any demo work beyond D2's conceptual design note.

## 4. Research questions

- **RQ1.** What is the model landscape consistent with "higher-order networks" (combinatorial and categorical), and what are the equivalence/loss relations between models (projections, inclusions, expansions)?
- **RQ2.** Which constructions **transport** across the planetary, social, and financial domains — incidence/flow conservation, projection-as-accounting, homological summaries, multi-scale filtrations — and where do the transports break?
- **RQ3.** How do the two anchor arguments (projection loses meaning; homology refines Euler) sharpen B2's candidate formalisms (e) and the aggregation stance?
- **RQ4.** What verification discipline do we adopt from the paper's caveat (non-unique expansions; effective vs genuine higher-order structure; null/equivalence checks)?
- **RQ5.** How should "higher-order networks" appear in the pitch — vocabulary, examples (group exchange, composite instruments, cooperative supply chain), and limits — without overclaiming?
- **RQ6.** Do path-dependent flow models (higher-order Markov models of money/material flows, per the paper's "missing links") give the internal-instrument story a concrete formal home?

## 5. Work packages

| WP | Content | Output |
|---|---|---|
| WP1 | Model landscape & loss relations: graphs/hypergraphs/simplicial/cell/multilayer/tensor + categorical models (hypergraph categories, SMCs, structured cospans, ologs, sheaves); projection/inclusion maps and what they destroy | landscape table + loss catalogue |
| WP2 | Cross-domain transports: planetary (material/energy flow hypergraphs, EEIO/LCA incidence structure, ecological higher-order interactions), social (group/governance interactions, co-authorship-style joint activity), financial (multi-input→multi-output production as hyperedges; composite instruments; claims/obligations sets) | transport table |
| WP3 | Toolkits: persistent homology/filtrations (multi-scale aggregation), Hodge-Laplacians and flow decomposition (gradient/cyclic/harmonic — candidate machinery for "returns out of the circulatory system"), null models and equivalence checks | toolkit notes + B2/B3 proposal candidates |
| WP4 | Vocabulary & pitch integration: mapping table; examples; the projection-loss demo mechanic for D2; deck-language guidance | vocabulary table + guidance |
| WP5 | Synthesis → topic memo + research-proposal contributions | deliverable |

## 6. Literature search plan

Standing note: seeds verified at download time; corpus claims only after ingest (`doc :: section`). Tiers: **P0** must-read, **P1** ingest + skim, **P2** background.

### 6.1 Keyword blocks (queries as they will be run)

**Block A — umbrella & surveys** (OpenAlex + web)
`higher-order networks` · `higher-order interactions` · `nonpairwise interactions` · `polyadic interactions` · `supra-dyadic` · `networks beyond pairwise interactions` · `higher-order networks survey`

**Block B — core models** (OpenAlex)
`hypergraph` · `simplicial complex` · `directed hypergraph` · `uniform hypergraph` · `clique expansion` · `incidence graph bipartite` · `cell complex network` · `hypergraph vs simplicial complex comparison`

**Block C — topology & analysis** (OpenAlex)
`persistent homology` · `topological data analysis` · `Hodge Laplacian` · `Hodge decomposition` · `simplicial homology` · `Euler characteristic` · `Čech complex filtration` · `topological signal processing` · `simplicial signal processing`

**Block D — dynamics & statistics** (OpenAlex)
`higher-order network dynamics` · `effective coupling phase reduction` · `simplicial contagion` · `higher-order social contagion` · `hypergraph stochastic block model` · `random hypergraph null model` · `higher-order Markov model flows` · `motif higher order`

**Block E — categorical/structural landscape** (OpenAlex)
`hypergraph category` · `symmetric monoidal category` · `structured cospans` · `decorated cospans` · `open systems category theory` · `knowledge representation ologs` · `sheaves network data` · `functorial semantics` · `operads networks`

**Block F — domain transports** (OpenAlex + web)
*planetary:* `input output analysis hypergraph` · `material flow network` · `higher-order interactions ecology` · `ecological interaction network higher order` · `trophic interaction network`
*social:* `group interaction network` · `coauthorship hypergraph` · `coalition formation network` · `brokerage triadic` · `collective action network`
*financial:* `production function network` · `supply network hypergraph` · `financial network higher-order` · `buyer seller broker network` · `contract bundling network` · `claims obligations network`

### 6.2 Seed works (verify before ingest)

- Bick, Gross, Harrington & Schaub, "What are higher-order networks?" (arXiv:2104.11329; SIAM Review 65(3), 686–731, 2023) — **P0 (anchor)**
- Battiston et al., "Networks beyond pairwise interactions: structure and dynamics" (Physics Reports, 2020) — P0 (the physics-centered companion survey the anchor cites)
- Battiston et al., "The physics of higher-order networks in nature and society" (Nature Reviews Physics) — P1 (locate; verify year/volume)
- Torres, Blevins, Bassett & Eliassi-Rad, "Simplicial complexes: higher-order dynamics and applications" — P1 (locate)
- Grilli et al., "Higher-order interactions stabilize dynamics in competitive network models" (Science, 2017) — P1 (planetary/ecology transport)
- Iacopini et al., "Simplicial models of social contagion" (Nature Communications, 2019) — P1 (social transport)
- Bairey, Kelsic & Kishony, "High-order species interactions shape ecosystem diversity" (Nature Communications, 2016) — P2
- Lim — Hodge-Laplacian / data analysis on simplicial complexes — P1 (locate exact works)
- Barbarossa & Sardellitti — topological signal processing over simplicial complexes — P2 (locate)
- Baez & Courser, "Structured Cospans" (2020) — P1 (categorical landscape)
- Fong, "Decorated Cospans" — P2
- Spivak & Kent, "Ologs" (2012) — P2 (cross-list B2)
- Fong & Spivak, *An Invitation to Applied Category Theory* (2019) — P2 (cross-list B2)

### 6.3 Tooling (for demos and the repository; not literature)

XGI (Extensible Graph Infrastructure — hypergraphs/simplicial complexes in Python) · HyperNetX (PNNL) · giotto-tda / ripser (persistent homology) · networkx (dyadic baselines). Note: our knowledge repository is itself a hypergraph; the topic formalizes our own infrastructure.

### 6.4 Search protocol & volume budget

1. OpenAlex `pipeline.py expand` `mode:"topic"` per Block phrase (limit 10–25); screen → tiers.
2. Citation chasing from the anchor paper both directions (its bibliography is the field's map).
3. Gray lit minimal: SIAM Review/News, Nature Reviews Physics, NetSci higher-order workshops.
4. **Budget: ~30 works** (P0 ≈ 4, P1 ≈ 12, P2 rest). Hard cap.

## 7. Synthesis method

Topic memo skeleton: (1) umbrella definition + **vocabulary mapping table** (public term ↔ formal object ↔ Federation instance: higher-order network ↔ hypergraph/simplicial ↔ the Federation's flow-and-interaction structure; group interaction ↔ hyperedge ↔ production act / governance decision / composite instrument; shape of the network ↔ homology ↔ multi-scale impact summaries; projection to pairwise ↔ clique expansion ↔ cost accounting; layers ↔ multilayer ↔ planetary/social/financial views); (2) **model-landscape table** with loss relations; (3) **cross-domain transport table**; (4) contributions to B2/B3 research proposals (higher-order impact accounting; projection-loss quantification for cost accounting; Hodge decomposition of network returns; path-dependent internal flow models); (5) claim-discipline box (the §5.4 caveat — effective vs genuine higher-order structure; null/equivalence checks); (6) deck-language guidance. Claims cited `doc :: section`.

## 8. Grounding & corpus integration

Per project `AGENTS.md` → Reference integration. The anchor paper is the first P0 download (arXiv PDF → `papers/incoming/` or `expand` by DOI 10.1137/21M1414024); ingest before drafting the topic memo so its claims are grounded `doc :: section`.

## 9. Schedule (Days 5–14 window)

- **Oct 26–27:** searches; anchor + P0 downloads; ingest begins.
- **Oct 28–31:** WP1–WP4 notes; landscape and transport tables populated.
- **Nov 1:** synthesis into the topic memo.
- **Nov 2:** topic memo draft → **Gate 2 (with B2)**.

## 10. Track risks

- **Term inflation:** "higher-order" also means higher-order Markov orders, derivatives, etc. — the memo defines the umbrella precisely and notes the neighboring usages.
- **Mindshare cuts both ways:** the term is trendy; claims must pass the paper's own discipline (genuine vs effective higher-order structure) or the pitch loses credibility.
- **Scope explosion across three domains** — hard volume cap; transport table limited to constructions that demonstrably carry (WP2 output is a table, not three literature reviews).
- **Category-theory overreach:** the anchor survey is combinatorial/analytic; the categorical models are adjacent literature — the landscape table must mark which claims come from where.

## 11. Open questions for Nic/Brad

1. Confirm "higher-order networks" as the deck's central vocabulary (formal terms demoted to the research appendix).
2. Should D2 implement the projection toggle (higher-order flows vs pairwise projection with visible loss)?
3. Topic memo organizing frame: the paper's three methodological contexts (topology / relational statistics / dynamics) or our three domains (planetary / social / financial), with contexts as toolkit rows?
4. Priority order for the research-proposal candidates (higher-order impact accounting; projection-loss quantification; Hodge decomposition of network returns; path-dependent flow models)?
