---
title: "A5 — impact-measurement standards prior art + Common Approach due diligence (v1)"
date: 2026-11-06
kind: research-plan
project: [moaiwi-network-poc, moaiwi-research-program]
---

# A5 — Standards prior art + Common Approach due diligence (v1, Nov 8 batch)

*R.1 deliverable of the action-circle workflow (`../action-circle-workflow-2026-10-25.md` §1 A5, added 2026-10-26). Survey of the field's formal artifacts: **CIDS first**, then IRIS+, the impact-management norms / five dimensions, SDG Impact Standards, GRI, crosswalks; plus due diligence on Common Approach's claims ("leading impact data ontology", "the only one used by more than one software") on four axes. Research homes: RT.T5 (standards) and RT.T18 (ontology/lowering). Feeds the A1 glossary and the B1 site's Concepts section. **Every web-sourced claim below is desk-side and unverified beyond the source cited — verify in interviews where marked.***

## 1. The five-dimension division of labor (the field's own statement of roles)

- **IRIS+** (Global Impact investing Network, GIIN): **what to measure** — a taxonomy of standardized metrics; "aligns to more than 50 metrics frameworks, standards and platforms" (their copy). US-based, largest funder network in the space. Pricing/subscription model for full access (verify tier structure).
- **The Impact Management Norms** — the **five dimensions** (*what, who, how much, contribution, risk*, plus a sixth *how* in CIDS usage): developed by the Impact Management Project through consultation with 2000+ impact professionals, now **housed at Impact Frontiers**. These are descriptive *norms*, not a data standard.
- **Common Impact Data Standard (CIDS)**: **how to share it digitally** — Common Approach's own division-of-labor statement: *"IRIS+ defines what to measure; the Common Impact Data Standard defines how to share it."* This framing is what makes CIDS (and not IRIS+) the natural backbone for software.

## 2. CIDS — what the artifact actually is (verified from the published standard)

- **Form.** An OWL ontology in **JSON-LD** serialization, revision **3.2.1** (issued 2025-10-31, documentation modified 2026-10-22 — actively maintained as of this week). Imports upstream ontologies: `iso21972`, `activity`, `icontact`, `organization`, `time`.
- **Content.** A standard representation of an organization's **impact model** (theory of change, logic model, outcome chain — any of these) + the **five dimensions of impact** + a sixth **how**; classes for stakeholders, outcomes, indicators, metrics, activities, outputs, inputs. Explicitly **does not prescribe indicators** — "no standard indicators here"; it standardizes *structure and exchange*, not *measurement choices*.
- **Exchange unit:** the **impact data capsule** — one machine-readable JSON-LD file holding the complete impact model + data, importable/exportable between aligned tools.
- **Alignment tiers:** three tiers; a **Basic Tier** exists precisely to keep the bar low (Excel Add-in, Airtable extension, CSV converter — "data utilities" for organizations that will never become data scientists). Optional **SFF Companion Module** for Canada's Social Finance Fund reporting (its own repo, out of scope for US work).
- **License:** CC BY-SA 4.0 (the v3.0 spec page states CC BY 4.0 — a minor documentation inconsistency to flag; Open Knowledge Graphs lists CC BY-SA 4.0). Free and public.
- **Framework traffic:** introductory guide names what can populate it: SDGs, Canadian Index of Wellbeing, **IRIS+**, SROI, **GRI**, SASB, **Impact-Weighted Accounts**, custom systems. (Crosswalk discipline: crosswalks are claimed; obtain and inspect before relying.)
- **Goal stated by the standard itself:** software vendors should be able to import/export without mapping; "a whole database in a text file".

## 3. Due diligence on Common Approach's claims

**Claim set under audit** (from their published infographic, CC BY-ND — *self-published marketing, treat as assertions to corroborate*): CIDS is (i) the only impact data ontology published publicly and free; (ii) the only one that has been through academic peer review; (iii) the only one created and governed by a nonprofit; (iv) the only one used by more than one software; (v) "world's leading impact data ontology"; (vi) "nine softwares currently aligned or in the process of aligning" (2023 grant text); (vii) aligned platforms "in the USA, Canada and Europe".

**Factual audit (desk pass v1):**

| Item | What checking found | Verdict |
|---|---|---|
| Adoption | **Real institutional embedding:** Canada's **Social Finance Fund** (a 10-year government program; wholesaler Realize Capital Partners, intermediaries Boann and Cap Finance) **requires** CIDS-based JSON-LD reporting from its participants, with Common Approach under contract to support adoption. **Pathfinder Pilot (2022–2025):** 33 social purpose organizations across three Canadian networks; **1,027 diverse bottom-up metrics aggregated into seven portfolio-level "Common Frameworks" without prescribing indicators**; 8 public-facing dashboards; data utilities preferred over new software by pilot users. Outside SFF: aligned-tool claims are vendor-stated (threshold.world/b.world, Impact Atlas, ImpactMapper, others) — **not independently verified; number and depth to be confirmed** against the aligned-tools page and interviews. | Plausible for the SFF ecosystem; **US ecosystem adoption unproven — verify** |
| Artifact quality (github.com/CommonApproach) | 6 public repos: **CIDS** spec (9 stars, 3 forks, **36 open issues**, active — updated 2025-11-05); CodeLists; Excel-BasicTier; AirtableBasicTier-Extension (**MIT-0 license**); SFF companion; Excel-to-JSON-LD ETL script. Active but **small-community scale** (single-digit stars/forks; org has no public members listed). | Engaged but thin public developer community |
| Governance / licensing | **Technical Committee** (5–8 members, "technical committees of engaged users"), public-review process ("standards are communities, not documents"), no active public review at check time. Credits: Kate Ruff, Garth Yule (Common Approach); v3.x with University of Toronto (Mark Fox's Centre for Social Services Engineering), Datavid, Impact Frontiers liaison, sector volunteers. **Funding history:** Ontario Ministry + IRP (v1.1), Government of Canada SFF (v3.0–v3.2), Tipping Point Fund grant (2023). Organization is **Canadian** (Springfield MA is USSEN's address, not Common Approach's). | Community-driven process in place; core authorship concentrated; **Canadian-governed with Canadian-government funding** |
| US / USSEN fit | CIDS is free, public, jurisdiction-neutral, and models SPOs generically (cooperatives explicitly among SPO types). The *institutional gravity* (SFF) is Canadian; **no equivalent US public-funder requirement exists to generate adoption on the US side.** GIIN/IRIS+ is the dominant US actor and it is a **metrics** taxonomy, not an exchange standard — they are complementary, not competitors. | Usable in the US; **adoption case must be made, not assumed** |

**Assessment of the "only one used by more than one software" claim:** the peculiar strength of this claim runs on the field having no *competing ontology* — the other named artifacts are metrics taxonomies (IRIS+), norms (the five dimensions), or reporting standards (GRI/SASB/SDG). So the claim is uninformative as a comparison; the informative question is **actual aligned-tool use in production**, which remains vendor-stated. Leadership claim (v) rests on the same absence — assume it is true, mark it un-corroborated.

## 4. Relevance to our threads (why this investment of effort is earned)

- **T5** (impact measurement): the CIDS posture — *standardize the container, not the measures; SPO autonomy in what they measure; funder legibility via structure* — is a concrete, field-tested answer to the central tension T5 inherits from B2: *investor legibility wants a score; the stance resists scalarization* (`../moaiwi-research-program/research-topics-v3.md` Appendix B). It is also the answer shape for the "filling out forms" problem (T5 added question (b)).
- **T18** (knowledge engineering): the Pathfinder pilot's working reduction — *1,027 bottom-up metrics → 7 thematic portfolio frameworks, no indicator prescription* — is exactly the hypergraph → lower-order-structure problem (higher-order relations → glossary/ontology), executed in the field at prototype scale. Record as prior art for the defunctionalization/lowering study; the **method** (iterative thematic folding, done with the metric owners) and the **data shape** (JSON-LD capsules) are both precedented.
- **Numerical-literacy note for the demo:** the SFF gives a **regulatory-ish precedent for the data flow** we would propose to funds (capsules from investees → portfolio aggregation → investor dashboard). That is a story the action circle can recognize, pitched in their language ("shared back office" — their own framing, MOAIWI-4 :: L57).

## 5. Alignment recommendation (v1 — due diligence can overturn)

**Keep CIDS as the candidate backbone for the R.1 glossary and the site's Concepts section**, with two explicit conditions held open:

1. **Verify aligned-tool reality in production** — the aligned-tools page plus interview questions ("which tools export impact data today? to what format? who does the mapping?"). If no aligned tool is in actual US fund use, the backbone question reopens (a fund-side glossary can still be served by IRIS+ vocabulary + capsules as an export target).
2. **Crosswalk check** — obtain the IRIS+ ↔ CIDS alignment materials and the five-dimension mapping in the ontology; the glossary's *definition* column credits CIDS/Impact Frontiers where it maps cleanly and marks residual mapping as open otherwise.

Renewal flag: recheck this memo's "self-published claim" table after each position/standard update; validity date of this pass = 2026-11-06.

## 6. Sources

- https://www.commonapproach.org/standards/common-impact-data-standard/ (+ aligned-tools page)
- https://ontology.commonapproach.org/cids-en.html (spec 3.2.1; acknowledgements; licenses)
- https://ontology.commonapproach.org/3.0/cids-en.html (spec 3.0 abstract: purposes and extensibility)
- https://www.commonapproach.org/wp-content/uploads/2026/02/Linking-Impact-Data_Part-3-The-Common-Impact-Data-Standard.pdf (the audited claims)
- https://www.commonapproach.org/knowledge/resources/celebrating-the-success-of-the-pathfinder-pilot-our-final-report/
- https://www.commonapproach.org/knowledge/resources/common-approach-receives-a-grant-from-the-tipping-point-fund-on-impact-investing/
- https://www.commonapproach.org/community/projects/social-finance-fund/ (+ Reflections and readiness, 2025-06-11)
- https://www.commonapproach.org/wp-content/uploads/2026/02/Common-Impact-Data-Standard_introductory-guide_EN.pdf
- https://www.commonapproach.org/about/governance-groups/technical-committee/
- https://github.com/CommonApproach (org + repo inventory)
- IRIS+ division-of-labor statement: https://www.commonapproach.org/knowledge/resources/how-giins-iris-and-common-approach-are-complementary (via `back-office-needs/landscape-pass1-2026-10-27.md` §5)
