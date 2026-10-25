---
title: "B1 research plan v3 — architecture, governance, and the failure-mode inventory (with T3)"
date: 2026-10-24
kind: research-plan
project: moaiwi-research-program
---

# B1 research plan v3 — architecture, governance & the failure-mode inventory

**Status:** v3, clean revision · 2026-10-24 · Falls under the **Research meta-process ("Explore")** per `meta-plan-v3.md` §7 — this plan carries the §7 requirements (question/decisions, outputs, resources, answer criteria, recording). **No gates**: gate and failure-mode machinery belongs to future Develop/Deploy meta-plans (meta-plan §4.1). v1 and v2 remain in the directory as history.

**What changed from v2 (see `research-topics-v3.md` Appendices A and C):** the plan now carries **T3 — the failure-mode inventory of previous attempts to scale cooperative networks** (the meta-plan §1 thesis's adversary, delegated to research plans by Brad 2026-10-24), absorbed from its own scope and from **B3's degeneration-canon work**; WP1 gains two columns (growth ceiling; attributed failure modes); a **failure mode → addressed by?** table becomes a synthesis output; keyword blocks gain a degeneration/persistence block; the v2 Gate 2 schedule, three-horizon mapping, and D2/D3 demo handoffs are **retired**.

**Sequencing (Brad, 2026-10-24):** desk-only; Brad proceeds without Nic. Nic reviews when available — non-blocking. Runs parallel to T1 (Nic, maybe Rachel) and other desk-work topics.

## 1. Scope

### 1.1 Questions answered and decisions informed

As options with trade-offs, never a recommendation:

1. A comparative map of candidate architectures for "a corporation that is also a federation of worker cooperatives" (legal form, ownership, control, capital, tax, liability) — and, per case, **how far it scaled and where it stopped**.
2. **The failure-mode inventory (T3):** what defeated previous attempts to scale cooperative networks — evidenced failure modes, per case, with growth curves — as the meta-plan thesis's adversary list and falsifier.
3. Governance mechanisms that keep economic democracy structural while admitting investor capital in the adversarial US context — without defaulting to one-member-one-vote.
4. Investor-instrument candidates and the governance consequences of each.
5. Research proposals: the open problems the R&D program should own.

**Decisions informed:** framing-memo-v3's argument spine (which problems the program claims to solve); which problems **Hyphae** and **Cooptopia** must actually attack (meta-plan §3.2–3.3); Cooptopia's ~5% ceiling baseline; Moaiwi's demo honesty (what may be claimed about "solving" anything).

### 1.2 Expected outputs

1. Architecture comparison matrix — with the two T3 columns (below).
2. **Failure-mode inventory (T3):** taxonomy × cases, each entry evidenced or explicitly marked unevidenced.
3. Governance mechanism catalog with failure modes and trade-offs.
4. Investor-instrument shortlist with governance consequences.
5. **Failure mode → addressed by? table:** every inventory entry against Moaiwi / Hyphae / Cooptopia claims, marked *claimed / not claimed / speculative*. This table is the meta-plan's falsifier; it must record the failure modes the projects do **not** address.
6. 4–6 research proposals.

### 1.3 Resources and access

Desk research only: OpenAlex/corpus pipeline and gray literature (queries in §4); statutes as web texts; the Phase B corpus (40 works + B1 screening + P0 readings) as salvageable input. **No interview access needed** — which is why this plan proceeds while T1 (fieldwork) is open. Legal texts carry "verify with counsel" flags; no counsel access is assumed.

### 1.4 What counts as an answer or closure

- The inventory covers **≥ 6 cases** with evidenced failure modes and growth-ceiling data (or documented absence of data); the taxonomy names each failure mode's proposed cause and its evidence.
- Matrix cells are filled or marked **unknown**; every legal claim is verification-flagged; every substantive claim cites `doc :: section`.
- The failure mode → addressed by? table has been reviewed by Brad, and the choices it exposes remain **options** — the plan does not close by picking an architecture.
- The research-proposals list exists.

### 1.5 Where results are recorded

Corpus: ingested via the Reference integration path (`expand` / `fulltext mode:"local"` / `build_hypergraph.py --force`), claims cited `doc :: section` per the `hypergraph-grounding` skill. Synthesis outputs land in `options/` when a memo is commissioned; interim notes update this file.

## 2. Research questions

- **RQ1.** What organizational architectures exist for federations of worker cooperatives (holding cooperative, secondary cooperative, corporation-with-co-op-subsidiaries, multi-stakeholder cooperative, union co-op, contractual network), and what does each imply for capital access, control retention, liability, tax, and formation ergonomics?
- **RQ2.** Which governance mechanisms plausibly hold economic democracy against capital pressure in US legal contexts, and what are their failure modes (capture, co-optation, stagnation, deadlock)?
- **RQ3.** Which investor instruments subordinate capital to mission *as structure rather than promise*, and what does practice show?
- **RQ4.** What does federation-level machinery add over co-op autonomy (Mondragon's inter-cooperation mechanisms; degeneration pressures on federations)?
- **RQ5.** How are exit and secession governed — can a thriving unit "go independent," and how are inter-unit transfers (growth funded from profitable parts) kept from breeding resentment?
- **RQ6.** Should the Corporation concentrate on **software & systems development** or on **direct implementation** (operating, incubating, holding)? Not answerable by argument — it requires **empirical data** from the prototype/fieldwork track; the memo maps what each posture implies and leaves the choice open.
- **RQ7 (T3 — the thesis's adversary).** *What defeated previous attempts to scale cooperative networks* — which failure modes (capital starvation, coordination cost, information loss in aggregation, governance capture/co-optation, degeneration, stagnation/deadlock, measurement failure, legal-form limits) are evidenced in which cases, and what do each attempt's growth curves (members, capital, share of local flows) show about where and why growth stopped?

## 3. Work packages

| WP | Content | Output |
|---|---|---|
| WP1 | Comparative architecture scan: Mondragon, Evergreen/Cleveland, union co-op, Emilia-Romagna/Marcora, French SCIC, platform co-ops, steward-ownership firms — with dimensions: tax treatment of inter-co-op flows; "network inside, firm outside"; internal capital accounts; exit/secession governance **+ two T3 columns: (a) scale achieved and growth ceiling — share of local flows where known (the T12/Cooptopia baseline); (b) failure modes attributed, with evidence** | comparison matrix |
| WP2 | **Failure-mode inventory (T3 core):** the taxonomy of RQ7 with case evidence and growth curves; **including the degeneration canon** (Ward/Domar/Vanek/Meade + empirical shared-capitalism and co-op persistence evidence — salvaged from B3 WP2) and the standing-objection answer set it generates | the thesis-adversary inventory |
| WP3 | US legal landscape, Colorado-first: co-op statutes, benefit/PBC, perpetual purpose trust, securities routes (Reg CF/D/A+) for co-op equity and community shares | "what is legally available" inventory, every entry verification-flagged |
| WP4 | Governance innovation: mechanisms from research + movement practice (sociocracy, consent, sortition, quadratic funding, liquid delegation; polycentricity; Ostrom design principles applied to federations) | mechanism catalog with trade-offs |
| WP5 | Investor instruments: non-voting/capped-return preferred, steward-ownership/golden share, reserved-matters classes, layered classes — with the transcript doctrine as option properties (equity-not-bonds selection rule; non-voting ≈10% band, ≤20% outside-ownership ceiling, double-books accounting; buy-out dynamics — external returns minimized, internal > external; withdrawal/gating mechanics). **Research scope covers the full mechanics the transcripts entertain — including debt, 0%-loans, and the barbell (Appendix C nuance): equity-only governs pitch language, not the research scope** | instrument shortlist + governance consequences |
| WP6 | Synthesis → options memo + **failure mode → addressed by? table** (Moaiwi/Hyphae/Cooptopia: claimed / not claimed / speculative) + research-proposals list | deliverable |

## 4. Literature search plan

Standing note: citations are seeds from working knowledge — bibliographic details and DOIs are verified at download time; nothing counts as a corpus claim until ingested and cited `doc :: section`. Tiers: **P0** must-read, **P1** ingest + skim, **P2** background.

### 4.1 Keyword blocks (queries as they will be run)

**Block A — federation & cooperative architectures** (OpenAlex `topic` + Scholar). *Tier 1 — validated by the 2026-10-22 test run (run these first, `limit` 10–25):* `Mondragon secondary cooperative` · `cooperative federation governance` · `inter-cooperation worker cooperative` · `cooperative federation structural change`

*Tier 2 — same block, untested:* `Mondragon Corporation governance` · `solidarity fund Mondragon` · `multi-stakeholder cooperative` · `union co-op model` · `Evergreen cooperatives Cleveland` · `platform cooperativism` · `employee ownership conversion` · `social cooperative Marcora Italy` · `solidarity cooperative SCIC` · `cooperative group legal structure` · `Desjardins cooperative federation` · `non-voting equity stake` · `outside ownership limit cooperative` · `internal capital accounts Ellerman` · `democratic firm` · `secession cooperative exit` · *(v3/T3)* `cooperative degeneration` · `worker cooperative failure` · `cooperative survival rate` · `cooperative growth constraints` · `Mondragon limits growth` · `solidarity economy scale limits` · `cooperative movement stagnation` · `federation failure cooperative`

*Avoid as written:* `worker cooperative federation` (IFSW encyclopedia entries, country-chapter sections) · `cooperative holding company structure` (bank holding companies, grain elevator histories, Chinese rural share-holding enterprises).

**Block B — degeneration, persistence & the labor-managed firm canon** (OpenAlex; salvaged from B3 Block B)
`labor managed firm theory` · `Illyrian firm Ward` · `producer cooperative Domar` · `self managed firm Vanek` · `degeneration thesis cooperative` · `Meade labor managed firm` · `employee ownership productivity evidence` · `shared capitalism at work` · `worker cooperative persistence` · `profit sharing participation performance` · `codetermination firm performance`

**Block C — governance innovation & democracy in firms** (OpenAlex + web)
`economic democracy governance firm` · `democratic workplace institutions` · `governance innovation cooperative` · `sociocracy consent decision making` · `participatory governance organization` · `polycentric governance` · `liquid democracy delegation` · `sortition governance` · `quadratic funding participatory budgeting` · `steward ownership governance` · `purpose trust golden share` · `asset lock mission` · `dual class shares mission protection` · `co-optation risk social enterprise` · `worker voice governance` · `dual class shares founder` · `share buyout investors` · `Treaty of Detroit profit sharing`

**Block D — US/Colorado legal & policy** (web + statute texts; OpenAlex secondary)
`worker cooperative law United States` · `Colorado Cooperative Association Act` · `Colorado employee ownership tax credit` · `benefit corporation cooperative` · `perpetual purpose trust state law` · `cooperative securities regulation` · `Regulation CF cooperative equity` · `community shares securities` · `Capper Volstead antitrust cooperative` · `employee ownership policy United States` · `cooperative legal barriers` · `transfer pricing intercompany` · `consolidated tax return affiliates`

**Block E — movement & political economy register** (web + OpenAlex)
`solidarity economy institutions` · `solidarity economy principles USSEN` · `community wealth building` · `Black cooperative tradition collective courage` · `feminist cooperative economics` · `dual power institutions` · `non-reformist reform` · `commons based peer production` · `economic democracy political economy`

### 4.2 Seed works (verify before ingest)

- Whyte & Whyte, *Making Mondragon* (1991) — P0
- Ostrom, *Governing the Commons* (1990) + Ostrom 2009 SES framework — P0
- Hansmann, *The Ownership of Enterprise* (1996) — P0
- Gordon Nembhard, *Collective Courage* (2014) — P0 (audience register)
- SELC, *Think Outside the Boss* (manual) — P0 (practical US forms)
- *(v3/degeneration)* Ward, "The Illyrian Firm" (1958) — P0 · Domar, "The Soviet Collective Farm as a Producer Cooperative" (1966) — P0 · Freeman, Kruse & Blasi (eds.), *Shared Capitalism at Work* (2010) — P0
- Alchian & Demsetz (1972) — P1 · Kelly, *Owning Our Future* (2012) — P1 · Scholz & Schneider (eds.), *Ours to Hack and to Own* (2016) — P1 · Bowles & Gintis, "Contested Exchange" (1990) — P1 · Chaves / Errasti et al. on Mondragon (locate) — P1 · ILO Recommendation 193 (2002) — P1 · Purpose Foundation steward-ownership materials — P1 · Ellerman, *The Democratic Firm* (1990) — P1 · *(v3/degeneration)* Vanek, *The General Theory of Labor-Managed Market Economies* (1970) — P1 · Meade, "The Theory of Labour-Managed Firms and of Profit Sharing" (1972) — P1
- Drèze (1976) — P2

### 4.3 Gray-literature targets

USFWC · Democracy at Work Institute · NCBA CLUSA · USDA Rural Business-Cooperative Service (Cooperative Information Reports) · Sustainable Economies Law Center · The Democracy Collaborative · USSEN ("What We Believe") · Center for Community Wealth Building (Denver) · Cooperation 5280 (Denver) · International Cooperative Alliance · MONDRAGON corporate governance reports · Purpose Foundation / Purpose Economy · B Lab · Colorado statute texts · Wellspring Cooperative (UMass Amherst) · Center for People's Economics · public-banking partners (below-market pool allocation).

### 4.4 Search protocol & volume budget

1. OpenAlex `mode:"topic"` per block phrase (limit 10–25); screen titles/abstracts → P0/P1/P2. **Screen immediately after each query — never accumulate unscreened records** (2026-10-22 lesson). *Tooling note: `scripts/pipeline.py` fails in this environment (plumb `morphism_fatal`); run the worker directly: `cd pipelines && printf '{"mode":"topic","topic":"<q>","limit":10,"doi":""}' | ../bin/tara-python ../scripts/expand_openalex.py`.*
2. Gray lit: web search with Block D/E strings + `site:` targets; PDFs staged to `papers/incoming/<key>.pdf` (fulltext `mode:"local"`).
3. Citation chasing: backward/forward from the P0 seeds per block.
4. **Budget: ~35 works total** (P0 ≈ 10, P1 ≈ 15, P2 rest). Hard cap.

### 4.5 Retrieval queue (2026-10-24)

**P0 status.** ✅ In corpus full text: **#1** Carman W1539711243 (AgEcon, manual) · **#4** Imaz W4319014659 (Springer, manual) · **#6** Basterretxea W2948895307 (Emerald, manual) · **#7** Pönkä W2914339720 (manual). ⛔ Stranded: **#2** W4407091201 (HAL record is closed source — checked by Brad 2026-10-24), **#3** W7213299274 (ScienceDirect paywall), **#5** W4390292511 (IBFD paywall). *Consequence: WP2/WP4 evidence leans on gray lit and case literature, not the federation-specific journal literature (see §8 transfer risks).*

**P1 status.** ✅ In corpus: **#9** de Peuter & Dyer-Witheford W2111485456 (manual) · **#10** W4389092776 (JEOD, auto) · **#12** W4389195852 (CIRIEC, manual) · **#14** W7210828298 (Ljubljana, manual) · **#16** W4400976761 (Berghahn, manual) · **#19** W4400896471 (Springer, manual) · **#8** W2154482800 (Elgar/SSRN, manual) · plus companion **W4296129757** Corbo et al. 2022 *Technovation* review (manual). 🌐 Still to download: none. ⛔ Paywalled (2026-10-24): #13 W4399878453 (Wiley — confirmed paywalled, Brad), #11 W3196906759, #15 W4205378368, #17 W2476926852, #18 W1548102935. *Stage downloads at `papers/incoming/<key>.pdf` (key = `https_openalex.org_W<id>`); works without a DOI bypass `mode:"local"` and need the direct `convert_local_pdf(rec, key, get_converter)` call (converter **factory**).*

**Read-in-browser.** Guttmann 2020, "Commons and cooperatives: A new governance of collective action" (W3084816230, *Annals of Public and Cooperative Economics*, DOI `10.1111/apce.12291`, 56 citations) — free to read at Wiley, closed to download; record added to `corpus/external/` for citation; cite from reading notes (WP3/WP4 candidate, Ostrom-lineage governance).

**Title collisions — always cite with authors.** "Commons and Cooperatives": Guttmann 2020 ↔ de Peuter & Dyer-Witheford 2010 (P1 #9). "Coopetition and innovation": Corbo et al. 2022 (W4296129757, review) ↔ Basterretxea et al. 2019 (P0 #6, worker co-ops). The pairs are distinct works, not versions.

**Query note.** The four validated Block A queries return only their top 10 each; Guttmann 2020 was never surfaced (rank truncation, and "commons and cooperatives" was not a query phrasing). When Block A re-runs for WP2/WP3, widen phrasing (e.g. `commons and cooperatives governance`, `collective action governance commons`) and raise `limit` to 25.

## 5. Synthesis method

Options memo skeleton: (1) architecture comparison matrix — dimensions: capital access (speed/scale), control retention, liability, tax (incl. inter-co-op flows), formation ergonomics, investor legibility, co-optation resilience, US legal availability, precedent maturity, **+ scale achieved/growth ceiling, + failure modes attributed**; (2) **failure-mode inventory (T3)** with per-case evidence; (3) **failure mode → addressed by? table** (Moaiwi/Hyphae/Cooptopia: claimed / not claimed / speculative) — the meta-plan's falsifier and framing-memo-v3's argument spine; (4) governance mechanism catalog with failure modes; (5) instrument shortlist with governance consequences; (6) 4–6 research proposals. Every substantive claim cites `doc :: section`. *(The v2 three-horizon mapping is retired; horizon/register questions belong to T9.)*

## 6. Grounding & corpus integration

Per project `AGENTS.md` → Reference integration: expand (DOI/topic) for indexed works, fulltext `mode:"local"` for downloaded PDFs, `build_hypergraph.py --force` after corpus edits, claims cited `doc :: section` per the `hypergraph-grounding` skill.

## 7. Sequencing

Desk-only; proceeds now (Brad, without Nic — their review is welcome when available, non-blocking). Parallel to T1 (Nic, maybe Rachel) and the other desk-work topics. **No gate dates** — the v2 Gate 2 schedule is retired; the meta-plan's plan-development method (§7) governs. Natural beats: searches and P0 ingest first; WP2's inventory drafted early (it feeds everything); WP6 synthesis last.

## 8. Track risks

- Statutes drift — every legal claim gets "verify current text" flag.
- Literature skews European/Mondragon — counterweight via Blocks D/E and non-European cases.
- Governance-innovation gray lit explodes — strict P0/P1/P2 tiers and the volume cap.
- Tax-engineering material from the transcripts is recorded as counsel-flagged research questions only; "instrument wrapping" phrasing stays out of all pitch artifacts.
- *(v3)* **Inventory capture risk:** the failure-mode taxonomy must not be tailored to make Hyphae look like the answer. Discipline: record failure modes the projects do *not* address (§1.2 output 5), and mark every entry claimed / not claimed / speculative without advocacy.

## 9. Open questions for Nic (non-blocking)

1. Any architecture they already consider disqualifying?
2. Include non-US designs (UK community shares, Italian Marcora-style funds) as "importable" options?
3. Denver/Colorado anchor institutions may be named in research notes — but pitch artifacts stay structurally abstract. Confirm that split (register questions otherwise belong to T9).
4. Their view on RQ6 (software & systems development vs direct implementation) is welcome as an input to the option map, but not blocking: the memo presents both postures and marks the choice as requiring empirical data.
