# Island Digital Twin — Literature Review

Research question: combine **island metabolism** (metabolismofislands.org) with **local digital twins** (ldt4ssc.eu) to develop an "island digital twin" — metabolic flow models built on a realistic 3D model of the island's natural and built topography, facilitating participatory sustainability planning.

Status: draft literature map, 2026-08-23. Sources compiled via web research; DOIs/stably-URLs verified where possible; unverified items flagged. Companion to the knowledge-repository workflow (these sources are candidates for OpenAlex `expand` ingestion into `projects/knowledge-repository-poc/`).

---

## Executive summary

The idea sits at the junction of four established bodies of work, and — importantly — **each side of the bridge already has a precedent**:

1. **Island metabolism** (socio-metabolic research: MFA/MSA of islands) tells us *what flows and accumulates* — materials, energy, water, waste, stocks — and why islands are metabolically vulnerable. This is the "island specific" half of the concept, already institutionalized as a network with a data hub (metabolismofislands.org, sister to metabolismofcities.org).
2. **3D city models / geospatial standards** provide the *geometric substrate* ("realistic 3D model of natural and built topography") and, crucially, standardized data models for attaching flow/stock data to that geometry. The CityGML **Energy ADE** — and its 2025 **Resources module (v3.0)**, which explicitly models *energy, water, food, waste, construction material* — is effectively a standard for "metabolic data on a 3D terrain+building model."
3. **Digital twins** (urban digital twin theory; SIDS practice; the EU Local-Digital-Twin ecosystem incl. LDT4SSC) provide the *twin container*: linked representation + simulation + (lately) participatory/social extensions. Direct island precedents exist: **Inishmore** (P2P energy twin on a 3D building model), **Tuvalu & Grenada** (SIDS climate-adaptation twins), **Culatra**, **Kefalonia/ARGOS** (open-source experiment).
4. **Participatory planning support / geodesign** supplies the *decision process*: planning support systems (PSS), PPGIS, and Steinitz's six-question geodesign framework — a proven methodology for *using models iteratively with stakeholders* to design change.

**Gap this project can occupy:** to our knowledge, no published work yet couples **economy-wide island material/energy/water accounting** with a **standard-based semantic 3D island model** (CityGML-type) inside a **participatory geodesign workflow**. The nearest neighbours connect only two of the four legs at a time.

---

## A. Island & urban metabolism — the flow layer

| # | Source | Verified metadata | Relevance |
|---|---|---|---|
| A1 | Kennedy, C., Cuddihy, J., & Engel-Yan, J. (2007). **The Changing Metabolism of Cities**. *Journal of Industrial Ecology* 11(2), 43–59. | DOI 10.1162/jie.2007.1107 | Foundational urban-metabolism framework (MFA across water/materials/energy/nutrients); the accounting convention most island studies inherit. |
| A2 | Singh, S.J., et al. (eds.*) (2020). **Introduction: The Metabolism of Islands** (editorial, Special Issue *Metabolism of Islands*). *Sustainability* 12(22), 9516. | DOI 10.3390/su12229516 | The programmatic statement of island metabolic research; scopes flows, stocks, stock–flow–service nexus, and the "island industrial ecology" agenda. |
| A3 | Noll, D., Lauk, C., Haas, W., Singh, S.J., Petridis, P., Wiedenhofer, D. (2022). **The sociometabolic transition of a small Greek island** (Samothraki 1929–2019): stock dynamics, resource flows, material circularity. *J. Ind. Ecol.* 26(2), 577–591. | DOI 10.1111/jiec.13206 | Complete island MFA/MSA time series — the model to emulate for quantitative island stocks·flows; published with an open database. |
| A4 | Bahers, J.-B., Singh, S., Durand, M. (2022). **Analyzing Socio-Metabolic Vulnerability: Evidence from the Comoros Archipelago.** *Anthropocene Science* 1, 164–178. | DOI 10.1007/s44177-022-00017-1 | Introduces *socio-metabolic vulnerability* — the link between resource-use patterns, systemic risk, and island vulnerability (climate-relevant framing). |
| A5 | Singh, S.J., et al. (2022). **Socio-metabolic risk and tipping points on islands.** *Environmental Research Letters* 17(6), 065009. | DOI 10.1088/1748-9326/ac6f6c | Defines socio-metabolic risk (SMR) for SIDS; water/waste/infrastructure sectors; argues for spatially-explicit stock/flow + inclusive risk governance. |
| A6 | (2014). **Resource Use in Small Island States** (Iceland; Trinidad & Tobago), *J. Ind. Ecol.* 18(2), 294–305. | DOI 10.1111/jiec.12100 | Economy-wide MFA for two island states — reference for island-scope accounting conventions. |
| A7 | (2020). **The 'Metal-Energy-Construction Mineral' Nexus in the Island Metabolism** (New Caledonia). *Sustainability* 12(6), 2191. | DOI 10.3390/su12062191 | Nexus approach to island metabolism; also demonstrates participatory method (stakeholder interviews) alongside MEFA. |
| A8 | (2020). **The Impact of Hurricane Irma on the Metabolism of St. Martin's Island.** *Sustainability* 12(17), 6731. | DOI 10.3390/su12176731 | Disaster-driven metabolism dynamics — relevant to climate-resilience scenarios an island twin would simulate. |
| A9 | **Metabolism of Islands** network & platform (metabolismofislands.org) | site; open-source platform: github.com/Metabolism-of-Islands/metabolism-of-islands-platform | The project in question: research network + curated island data hub/dashboards (biophysical context, infrastructure, stocks & flows) + community tools; sister to metabolismofcities.org. |

## B. 3D city models & standards — the geometric + data substrate

| # | Source | Verified metadata | Relevance |
|---|---|---|---|
| B1 | Biljecki, F., Stoter, J., Ledoux, H., Zlatanova, S., Çöltekin, A. (2015). **Applications of 3D City Models: State of the Art Review.** *ISPRS Int. J. Geo-Inf.* 4(4), 2842–2889. | DOI 10.3390/ijgi4042842 | Canonical taxonomy of 3D city-model use cases (29 use cases / 100+ applications) — motivation and positioning for the 3D substrate. |
| B2 | Agugiaro, G., Benner, J., Cipriano, P., Nouvel, R. (2018). **The Energy Application Domain Extension for CityGML.** *Open Geospatial Data, Software and Standards* 3, 2. | DOI 10.1186/s40965-018-0042-y (open access) | The standard data model tying energy demand/production to semantic 3D buildings — the technical bridge between "3D island model" and "flow model". |
| B3 | Agugiaro, G., Padsala, R., Coors, V. (2025). **CityGML Energy ADE v3.0** (beta 7). TU Delft / HFT Stuttgart, open development. | 3d.bk.tudelft.nl/projects/energyade/; github.com/tudelft3d/Energy_ADE; citygmlwiki.org | **KEY:** the new **Resources module** explicitly models *energy, water, food, waste, construction material* as demand/production/storage/accumulation on city objects — i.e., a standardized "metabolic data on 3D geometry" model. Directly extensible to island-wide metabolic layers. Also: 3DCityDB (PostgreSQL/PostGIS reference implementation). |
| B4 | Malhotra, A., Bischof, J., Nichersu, A., et al. (2022). **Information modelling for urban building energy simulation — a taxonomic review.** *Building and Environment* 209, 108552. | DOI 10.1016/j.buildenv.2021.108552 | UBEM-state-of-the-art incl. CityGML/EnergyPlus pipelines and (sobering) evidence on reproducibility/interoperability gaps — scope the risk for island UBEM. |
| B5 | (2020). **Heating demand prediction from 3D city models + CityGML Energy ADE — case study Helsinki.** *ISPRS Int. J. Geo-Inf.* 9(10), 602. | DOI 10.3390/ijgi9100602 | End-to-end reference workflow: 3D city model → Energy ADE → district heating/CO₂ scenarios → 3D Tiles web viz. (authors unverified — confirm before citing formally). |
| B6 | OGC **CityGML 3.0** (2021) + 3DCityDB toolchain | ogc.org; 3dcitydb.org | Standards baseline for semantic 3D terrain+built model of an island (incl. TIN/terrain, vegetation, water bodies). |

## C. Digital twins — the container (urban theory, island practice, EU policy)

| # | Source | Verified metadata | Relevance |
|---|---|---|---|
| C1 | Batty, M. (2018). **Digital twins.** *Environment and Planning B: Urban Analytics and City Science* 45(5), 817–820. | DOI 10.1177/2399808318796416 | Defining statement: twin must run *decoupled/offline* for scenario exploration (high-vs-low frequency city); the "model ≠ twin" caution is directly relevant to planning uses. |
| C2 | Batty, M. (2023). **Digital Twins in City Planning.** CASA Working Paper 237, UCL. | open access (ucl.ac.uk/bartlett/casa) | Current perspective linking twins to planning practice and public engagement. |
| C3 | Ravid, B.Y., & Aharon-Gutman, M. (2022). **The Social Digital Twin: the Social Turn in Smart Cities.** *EPB* 50(6), 1455–1470. | journal/vol confirmed; DOI to verify | The *social/participatory* extension of digital twins — direct theoretical support for the "facilitate participatory planning" goal. |
| C4 | Buckley, N., Bo, C., Delkhah, F., Byrne, N., Ní Shearcaigh, A., Brennan, S., et al. (2024). **Evaluation of a Peer-to-Peer Smart Grid Using Digital Twins: A Case Study of a Remote European Island** (Inishmore, IE). *Energies* 17(22), 5541. | DOI 10.3390/en17225541 (open access) | **Direct island-digital-twin precedent:** physics-based building/energy twin (IES ICL) of an island community, 3D geometry, surveys + smart-meter data, P2P/decarbonization scenarios. The closest existing realization of this idea. |
| C5 | **SIDS digital twins** (Tuvalu; Grenada) — UN Statistics Division blog (2024) + Esri (PLACE + SPC Digital Earth Pacific; ArcGIS Reality photogrammetry). | unstats.un.org; esri.com | Nation-level island twins for sea-level/climate adaptation, built on aerial reality-capture 3D + GIS — a proven (if not peer-reviewed-) workflow for island-scale 3D basemaps. |
| C6 | Culatra Island (PT) **Renewable Energy Community grid digital twin** (MATLAB/Simulink, five-layer). | IEEE DataPort dataset (2024) | Island energy-grid twin (building/grid level) — architecture example for the flow-simulation layer. |
| C7 | ARGOS — open-source island digital twin experiment (Kefalonia, GR): PostGIS + FastAPI + MapLibre + PMTiles; OSM/COPERNICUS/Sentinel data. | dev.to/ptzivras (2026) | Community-built, €0/mo stack — evidence the 3D+flow stack can be open and cheap; not peer-reviewed. |
| C8 | **EU Local Digital Twins ecosystem:** LDT4SSC (ldt4ssc.eu), EU LDT Toolbox, CitiVERSE EDIC (x-CITE, SENSE, CU, 3DxVERSE), Living-in.EU, SIMPL, EIF4SCC/MIMs+. | EC digital-strategy page; ldt4ssc.eu; knowledgehub.ldt4ssc.eu | Policy/framework layer: standards for interoperable, federated local twins (DCAT/ODRL, MIMs+, SIMPL) and ~€1M pilot calls — the institutional route for a European island twin. |
| C9 | (2022). **The adoption of urban digital twins** (review). *Cities* / Elsevier (ScienceDirect S0264275122003444). | journal/vol to verify | Adoption review — helps scope an island twin's barriers/acceptance in local government. |
| C10 | (2024). **Urban Digital Twins and metaverses towards city multiplicities.** *Urban Analytics and City Science* (PMC11584446). | accession verified (open access) | Critical view: participatory/interactive US city twins incl. risks (privacy, fragmentation) — the cautionary counterweight for the participatory goal. |
| C11 | Fotheringham, A.S. (2023). **Digital twins: The current "Krays" of urban analytics?** *EPB* 50(4), 1020–1022. | DOI 10.1177/23998083231169159 | Provocation/terminology check — important for writing against hype. |
| C12 | (2025). **Construction of a Coastal Zone Digital Twin for Scenario Simulation and Decision Optimization.** *Journal of Geo-information Science* 27(9), 2106–2116. | DOI 10.12082/dqxxkx.2025.250220 | Recent coastal-zone twin for scenario + decision support (adjacent to island coastal metabolism). |

## D. Participatory planning support & geodesign — the decision process

| # | Source | Verified metadata | Relevance |
|---|---|---|---|
| D1 | Sieber, R. (2006). **Public Participation Geographic Information Systems: A Literature Review and Framework.** *Annals of the AAG* 96(3), 491–507. | DOI 10.1111/j.1467-8306.2006.00702.x | Canonical PPGIS framework (place/people, technology/data, process, outcome/evaluation) — the participation theory for the twin's public face. |
| D2 | Brown, G., & Kyttä, M. (2014). **Key issues and research priorities for public participation GIS (PPGIS).** *Applied Geography* 46, 122–136. | DOI 10.1016/j.apgeog.2013.11.004 | PPGIS synthesis (>40 empirical studies) — practical guidance for participatory workflows. |
| D3 | Geertman, S., Ferreira, J., Goodspeed, R., & Stillwell, J. (eds.) (2015). **Planning Support Systems and Smart Cities.** Springer, LNGC. | DOI 10.1007/978-3-319-18368-8 | State of the art on PSS for smart/city planning — the framework into which an island twin as a planning tool slots. |
| D4 | Geertman, S., Allan, A., Pettit, C., & Stillwell, J. (eds.) (2017). **Planning Support Science for Smarter Urban Futures.** Springer, LNGC. | DOI 10.1007/978-3-319-57819-4 | Follow-on: PSS + big data + urban futures; what-if scenario tooling for the community-engagement half. |
| D5 | Steinitz, C. (2012). **A Framework for Geodesign: Changing Geography by Design.** Esri Press. | ISBN 9781589483330 (no DOI; book) | The six-question, three-iteration geodesign framework — a ready-made iterative, stakeholder-driven design methodology exactly suited to "plan on the twin, evaluate scenarios, decide". |

---

## Synthesis: how the pieces compose into an "island digital twin"

Proposed composition (each leg grounded in the above):

- **Accounting:** island socio-metabolic MFA/MSA (A2–A6, A8), structured like A3, following A1 conventions.
- **Geometry + data:** a semantic 3D island model in a CityGML-class standard (B2, B6), carrying metabolic flows via the **Energy ADE 3.0 Resources module** on terrain + buildings + waterways (B3); UBEM pipelines validated per B4/B5.
- **Twin container:** Batty-style decoupled scenario model (C1, C2) with a *social/participatory* enrichment (C3), informed by the EU LDT standards stack for interoperability and pilots (C8) and the SIDS reality-capture basemap precedent (C5). Closest existing analogues to study closely: Inishmore (C4), Culatra (C6), ARGOS (C7).
- **Decision process:** PPGIS/PSS methods (D1–D4) run *through* Stenetiz's geodesign iteration (D5) so the twin is a shared planning instrument, not a deliverable slide.

**Novelty claim to defend:** the coupling of the *metabolic* (A) + *3D-standard* (B) layers is published nowhere as an integrated island twin; the participatory geodesign layer (D) extends the social-digital-twin direction (C3) to island metabolic planning.

## Caveats

- Items flagged "to verify" need author/volume confirmation before formal citation (esp. B5, C3, C9, C10).
- Several island-twin precedents (C5–C7) are grey literature / project sites rather than peer-reviewed; treat as existence-proofs and archives, not methods citations.
- A2 editorial author list unverified; A6/A7/A8 author lists abbreviated — confirm from the DOI landing pages.
- Next concrete step: ingest the DOI-keyed items via the knowledge-repository `expand` pipeline and run a grounding trace over the composed question, so the synthesis above becomes repository-citable.