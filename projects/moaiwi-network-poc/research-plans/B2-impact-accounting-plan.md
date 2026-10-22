# B2 research plan — impact accounting & the aggregation stance

**Status:** research plan (pre-download gate — no references downloaded until reviewed) · 2026-10-21 · Output: options memo (≤3 pp) + research-proposals list due **Gate 2, Mon Nov 2** · Brad drafts, Nic reviews.

## 1. Scope

The aggregation question is the pitch's **core open research output**. The memo must deliver — as options, not decisions:

1. An audit of how existing frameworks commit to a scale of aggregation, and what each commitment costs.
2. 2–3 candidate formalisms for "aggregation without a prior commitment to scale," precise enough that the D1 calculator can instantiate them.
3. Their properties: comparability, verifiability, gaming resistance, measurement cost, investor legibility.
4. Research proposals: the open problems the R&D program should own (including assurance: what keeps all three impact areas honest).

Out of scope: choosing the formalism; any final metric set; thermodynamics/stat-mech (deliberately excluded — planetary modeling stays in the industrial-ecology/LCA register).

## 2. Research questions

- **RQ1.** How do current impact frameworks aggregate, at what scales do they commit, and what do those commitments hide (commensuration, index, greenwashing critiques)?
- **RQ2.** What formalisms permit measurement and composition without a prior scale commitment? Candidates: (a) multi-scale measurement with explicit aggregation maps; (b) vector/set-valued impacts with partial orders; (c) sheaf-theoretic local-to-global composition; (d) biophysical common-denominator accounting for the planetary domain only.
- **RQ3.** Which candidates can the calculator instantiate, and with what UX for "aggregation choices visible and adjustable"?
- **RQ4.** What institutional machinery (assurance, audit, participatory validation) makes multi-scale claims credible to both movement and capital audiences?

## 3. Work packages

| WP | Content | Output |
|---|---|---|
| WP1 | Framework survey + scale-commitment audit: for each framework — what is measured, at what scale aggregated, who verifies, what is lost | audit table |
| WP2 | Critique literature: commensuration, incommensurability, index/impossibility results, impact-washing, performative accounting | critique summary |
| WP3 | Formal toolkit: multi-scale aggregation maps, partial-order/MCDA methods, sheaves/cosheaves/ologs, measurement theory, categorical compositionality | candidate formalisms A–D |
| WP4 | Planetary domain in industrial-ecology register: LCA, environmentally-extended IO, material flow analysis, emergy, planetary boundaries, donut | planetary metric options |
| WP5 | Social domain: well-being, care economy, community wealth, capabilities, participatory indicators | social metric options |
| WP6 | Synthesis → 2–3 formalisms + calculator requirements + research-proposals list | deliverable |

## 4. Literature search plan

Standing note: seeds verified at download time; corpus claims only after ingest (`doc :: section`). Tiers: **P0** must-read, **P1** ingest + skim, **P2** background.

### 4.1 Keyword blocks (queries as they will be run)

**Block A — impact frameworks & practice** (web + OpenAlex)
`impact weighted accounts` · `impact measurement and management` · `IRIS+ metrics GIIN` · `integrated reporting multi-capital` · `full cost accounting` · `triple bottom line critique` · `social return on investment` · `theory of change evaluation` · `impact management project five dimensions` · `B Impact Assessment` · `SDG indicators business` · `sustainability assurance reporting` · `integrated capital impact` (audience term)

**Block B — critique & philosophy of measurement** (OpenAlex)
`commensuration and its discontents` · `incommensurable values ethics` · `social choice aggregation` · `impossibility of aggregation indices` · `greenwashing impact washing` · `performativity accounting` · `audit society` · `indicators sustainable development critique` · `beyond GDP` · `Stiglitz Sen Fitoussi` · `welfare measurement Sen capabilities` · `mismeasurement social progress`

**Block C — formal/mathematical toolkit** (OpenAlex)
`multi-criteria decision analysis` · `partial order ranking indicators` · `outranking methods ELECTRE PROMETHEE` · `measurement theory foundations` · `sheaf theory applications` · `cosheaves data integration` · `category theory compositionality` · `knowledge representation ologs` · `functorial semantics` · `multi-scale modeling hierarchy` · `hierarchy theory ecology` · `Hasse diagram indicators`

**Block D — planetary & biophysical (industrial-ecology register)** (OpenAlex + gray)
`life cycle assessment` · `environmentally extended input output analysis` · `material flow analysis` · `emergy synthesis Odum` · `exergy accounting` · `planetary boundaries accounting` · `doughnut economics` · `ecosystem services valuation critique` · `inclusive wealth` · `genuine progress indicator` · `steady state economics Daly` · `degrowth indicators` · `System of Environmental-Economic Accounting SEEA`

**Block E — social domain measurement** (OpenAlex + gray)
`well being indicators OECD` · `care economy measurement` · `feminist economics GDP critique` · `community wealth indicators` · `solidarity economy indicators` · `participatory action research indicators` · `worker cooperative impact measurement` · `employee ownership impact evidence` · `quality of employment indicators` · `just transition indicators`

### 4.2 Seed works (verify before ingest)

- Elkington, "Enter the Triple Bottom Line" (2004) + his 2018 HBR retrospective (self-critique) — P0
- Espeland & Stevens, "Commensuration and Its Discontents" (2008) — P0
- Serafeim et al., Impact-Weighted Accounts Initiative reports (HBS) — P0
- Stiglitz, Sen & Fitoussi, *Mismeasuring Our Lives* (2010) — P0
- Sen, *Commodities and Capabilities* (1985) — P1
- Arrow, *Social Choice and Individual Values* (1951) — P1
- Anderson, *Value in Ethics and Economics* (1993) — P1
- Meadows, "Indicators and Information Systems for Sustainable Development" (1998) — P1
- Raworth, *Doughnut Economics* (2017) — P1
- Odum, *Environmental Accounting* (1996) — P2 (emergy route; thermo lens excluded from pitch, kept as accounting option only)
- Krantz, Luce, Suppes & Tversky, *Foundations of Measurement* (1971) — P2 (selected chapters)
- Keeney & Raiffa, *Decisions with Multiple Objectives* (1976) — P1
- Ehrgott, *Multicriteria Optimization* (2005) — P2
- Spivak & Kent, "Ologs: A Categorical Framework for Knowledge Representation" (2012) — P0 (ties to the repository's own representation)
- Fong & Spivak, *An Invitation to Applied Category Theory* (2019) — P2
- Curry, "Sheaves, Cosheaves and Applications" (2014) — P1
- Ghrist, *Elementary Applied Topology* (2014) — P2
- Ostrom 2009 SES framework (Science) — P1 (multi-scale measurement precedent)

### 4.3 Gray-literature targets

GIIN (IRIS+ catalog) · Impact Management Project / Impact Frontiers · GRI · SASB/ISSB (as critique material) · B Lab · Doughnut Economics Action Lab (DEAL) tools · OECD Better Life Index · Wellbeing Economy Governments (WEGo) · Genuine Progress Indicator advocates · NEF (Thriving Places Index, Happy Planet Index) · UNU Inclusive Wealth Report · UN SEEA · Kataly Foundation (Restorative Economics) · Boston Impact Initiative (integrated capital) · USSEN.

### 4.4 Search protocol & volume budget

1. OpenAlex `pipeline.py expand` `mode:"topic"` per Block phrase; screen → tiers. Blocks B/C drive the research agenda; A/D/E drive the practice survey.
2. Gray lit via web + `site:` targets; PDFs to `papers/incoming/` (fulltext `mode:"local"`).
3. Citation chasing from P0 seeds both directions.
4. **Budget: ~35 works** (P0 ≈ 8, P1 ≈ 15, P2 rest). Formal-math P0 hard-capped at 6 to protect the sprint.

## 5. Synthesis method

Options memo skeleton: (1) scale-commitment audit table (framework × measured × aggregation scale × verifier × what's lost); (2) candidate formalisms A–D with properties (comparability, verifiability, gaming resistance, cost, legibility); (3) calculator instantiation requirements for D1 (which views the demo shows, how aggregation choices are exposed); (4) 4–6 research proposals (may include sheaf-formalism development as proposal rather than demo). Claims cited `doc :: section`.

## 6. Grounding & corpus integration

Per project `AGENTS.md` → Reference integration (expand / fulltext local / `build_hypergraph.py --force` / `doc :: section` per `hypergraph-grounding` skill).

## 7. Schedule (Days 5–14 window)

- **Oct 26–27:** searches; P0 downloads; ingest begins.
- **Oct 28–31:** WP1–WP5 notes; audit table populated.
- **Nov 1:** synthesis into candidate formalisms + calculator requirements.
- **Nov 2:** options memo draft → **Gate 2 (B2)**.

## 8. Track risks

- Formal literature can swamp the sprint → P0 formal cap of 6; formalisms may end as research proposals rather than implemented views.
- Framework taxonomy churn (initiatives merge/rename) → record version/date with every source.
- Tension: investor legibility wants a score; the stance resists scalarization → surface the tension explicitly in the memo, with the trade-off axis named.

## 9. Open questions for Nic

1. Should D1 demo one "leading" formalism or a switchable pair (aggregation-maps view vs partial-order view)?
2. How much measurement philosophy appears in the pitch itself vs appendix/research-agenda slides?
3. Environmental scope now: energy/carbon-first, or biodiversity/water included in the metric options from the start?
4. Is there an assurance expectation from this investor audience (third-party audit) we should design toward, or is methodology transparency enough at this stage?
