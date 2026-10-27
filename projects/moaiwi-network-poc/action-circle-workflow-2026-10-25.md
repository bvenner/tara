---
title: "R.1 action-circle engagement — mutual-education workflow (site + presentation)"
date: 2026-10-25
kind: options
project: moaiwi-network-poc
---

# R.1 workflow — the action-circle engagement as mutual education

*Requested 2026-10-25: a detailed workflow for the ~Nov 20 presentation to the "Finance and Community Capital" action circle, reframed by the autonomy meta-plan's discipline — **a mutual education process, not a pitch** (reciprocal paideia; *logon didonai* — giving and demanding accounts). Brad needs to learn the **language of impact investing** in addition to Nic and Rachel's fieldwork. Structure: the **product website is the durable artifact** with room for detailed language; the 5–10 minute presentation is a **summary of the site** plus a brief live demo. Relationship to the T-topics: this workflow is T1's engagement surface and **answers T9's question by doing** ("the circle itself is the experiment").*

***Revised 2026-10-26** per Brad's notes (preserved verbatim in `writing/human/moaiwi-action-circle-workflow-notes.md`); the decisions taken in response are in the revision record at the end. Where a decision was explicitly deferred, the document says so.*

## 0. Design principles (from the autonomy meta-plan)

1. **Reciprocity first.** The formative aim applies to the formers: we expect to be changed by this exchange. The format must give the circle's reasons the same standing as ours.
2. ***Logon didonai*.** Every claim we make arrives with its reasons; every question we ask invites reasons back. Nothing is asserted that we cannot account for.
3. **Metrics as instruments, not substance.** Impact language is presented as the *sensory apparatus of an affected public* — provisional, revisable. The standing question travels with every metric: *"who chose this, and when does the collectivity get to revise it?"*
4. **Explicit unknowns replace vague promises.** (Inverting MOAIWI-4's "vague promises are fine" — under the regime framing, honesty about unknowns is itself the credibility strategy and the paideic move.)
5. **The three-collective check.** Whose interests are not in the room? One honest treatment of the affected public of the funds' investments — present, not preachy.
6. **Register (Brad, 2026-10-26; provisional "for now").** The **Castoriadis vocabulary stays inside the Reflect process documents**. Everything Nic, Rachel, and the investors see is conventional systems/software-engineering or plain English. Castoriadis is used **for critique of conventional approaches, not as adopted terminology** — expressed as marked gaps where conventional language falls short (see §6 item 5), not as foreign vocabulary. The glossary and this workflow's language are phrased as closely as possible to conventional SE terms (requirements engineering, stakeholder analysis, governance, …).

## 1. Track A — language acquisition (Brad; starts now; independent)

- **A1. The working glossary — a view on an emerging ontology, not a standalone list.** Impact-investing language in **four columns**: *their term* · *definition (credited to prior art wherever a good formal definition exists)* · *what using the term commits you to (the substantive freight: assumptions, measurement choices, obligations)* · *our translation/critique in conventional SE language*. Where prior art defines a term (CIDS, IRIS+, Impact Norms, the Common Approach glossary), the definition is taken and credited; column 3 then carries only what the *standard's usage* drags in beyond the definition. The fourth column is where critique lives — in SE terms per principle 6. **Sources already on hand:** the B2 salvage list (Appendix B) plus the Common Approach resources (see A5), USSEN "What We Believe", Kataly's Restorative Economics, public-banking partner materials. *Output: `impact-investing-glossary.md` (site-destined, see B2).* *Definition shape pending §6 item 5 (translation fidelity).*
- **A2. The circle's own language.** Collect how the R&B DEN-2026 contacts and USSEN-adjacent investors actually speak: their statements, session materials, the transcript record of what the investors said (MOAIWI-4: *they* proposed budgeting a person for cross-fund research — their words, their framing). *Output: a phrasebook of their vocabulary and concerns.*
- **A3. Fieldwork synthesis (depends on 0.4 / T1).** As Nic and Rachel's interview notes arrive, fold in the vocabulary and complaints of actual conversations. The interview protocol itself should carry Brad's language questions (see D1).
- **A4. Survey of impact-investing software** (Brad's note 2; explicit work item). What impact investors are actually *using and paying for*: the impact-investing-specific platforms (impact measurement/reporting, fund and portfolio management) **and** the general back-office stack funds live in (QuickBooks, spreadsheets, Salesforce, Sage Intacct) — the gap between what is offered and what is used is the wedge. Web-side within a ~$20 LLM budget: vendor sites, G2/Capterra, job postings, fund tech-stack traces; the T1 interviews then say what the market scans can't. *Output: a landscape note feeding A1's first/third columns, T1's interview protocol, and B2's product language. Home: a slug directory under `../moaiwi-research-program/` when started (per the file policy); the work item lives here until then. Known coverage limits: vendor bot walls.*
- **A5. Ontology and standards prior art + Common Approach due diligence** (added 2026-10-26). Survey the field's **formal artifacts**: the Common Impact Data Standard (CIDS) first, then the IRIS+ taxonomy, Impact Norms' five dimensions, SDG Impact Standards, GRI, and the published crosswalks. **Due diligence** on Common Approach's claims ("leading impact data ontology", "the only one used by more than one software"): actual adoption and who uses CIDS, formal artifact quality (github.com/CommonApproach), governance/licensing, and US/USSEN fit (the organization is Canadian, Social Finance Fund-adjacent). **Decision (Brad, 2026-10-26): CIDS is the candidate backbone** — the glossary maps to CIDS where it can; the crosswalks handle the rest as Common Approach handles them; due diligence can still overturn the choice. *Output: prior-art memo + alignment recommendation.*

## 2. Track B — the product website (the durable educational artifact)

- **B1. Site skeleton** (can start now, independent): a static build (v2 defaults inherited: Astro/Vite, unlisted hosting, screenshot fallbacks — pending decisions, not commitments). Proposed structure:
  1. **What we're building** — Fortress-based business server, demo materials, what exists today vs. what is proposed.
  2. **The research stack proposal** — the "expandable subset" framing from MOAIWI-4: start small and real, inflatable to the larger abstractions later.
  3. **The questions we bring** — the mutual-education core (§1 of the talk's agenda; see C1): our open questions, stated as *questions*.
  4. **Concepts** — the A1 glossary in public form: credited definitions, the commitments column, and the SE-language translation/critique (principle 6 register).
  5. **What we don't know** — explicit unknowns (measurement, the affected public, pricing, the 5% question). Honest, specific, and unusual enough to be memorable.
  6. **The exchange continues** — how to reach us, what happens after this meeting, the site as the living document that updates after each circle meeting.
- **B2. Detailed product language** (depends on A-track + Nic's demo status): as much depth as the medium allows — each claim carries its evidence or its question-mark; the naming policy applies (working names marked as such; the audience names things). A4's landscape informs the "what we're building" vs. "what exists" distinctions.
- **B3. The standing-question apparatus** (design decision): every metric/impact figure on the site carries the revision question (principle 3) — visibly, as a small recurring affordance rather than a footnote.

## 3. Track C — the presentation (summary of the site; 5–10 min + brief live demo)

- **C1. Talk outline** (draft; depends on B1 skeleton):
  1. *Who we are, what we're building* (~2 min) — brief Fortress demo with the B2B client functionality (Nic's Develop track; live demo + screenshot fallback).
  2. *The research stack proposal* (~2 min) — what we'd study with and for this circle (cross-fund research named in their own framing — A2).
  3. *Three questions we bring* (~3–4 min) — the mutual-education heart: (a) what does your back office actually need, and what do you pay for today? (T1, sharpened by A4); (b) what should "measurable impact" mean *to you* — and who should get to revise the measure? (T5 as public-sensory); (c) what would make software like this worth paying for — and what would make this conversation worth continuing?
  4. *How this continues* (~1 min) — the site is the living document; we'll return with updates; the circle is forming and we intend to learn with it.
- **C2. Rehearsal with Nic** (they/them present; Brad supports) — not a gate (the v2 gate schedule is retired) but practice: the presentation is itself *logon didonai*, rehearsed as such. Target M−3 if the date holds.
- **C3. Demo readiness** (Nic's Develop track — the only hard dependency outside our control): Fortress configured as business server; what exists gets shown as existing.

## 4. Track D — the mutual-education loop (what makes it not-a-pitch)

- **D1. The question list is joint and reciprocal.** Prepared by Brad (language questions from A1/A2) + Nic and Rachel (fieldwork questions from T1) *together*; roughly **half the meeting's substance is our questions to them**. With consent, their answers feed the T1/T9 record and the glossary's commitments column.
- **D2. Feedback is the data.** Pushback, confusion, and complaints are the primary output of the meeting (T1's "listen to them complain"); the note template captures them verbatim where possible.
- **D3. The three-collective question, asked once.** Whose interests are not in this room — the affected public of the funds' investments? Asked honestly to the circle and kept honest on the site (principle 5), in plain English per the register decision (principle 6): the democracy-as-regime work becomes visible in public as the *question*, not the vocabulary.
- **D4. The continuing process.** Ongoing updates at later circle meetings (meta-plan M1: the circle is an unfolding process); after each exchange, the site updates and lessons flow to the next QA session. The site is the public Reflect artifact.
- **D5. Paideic debrief.** After the meeting: what changed in *our* understanding (Brad's language acquisition is an explicit goal — measure it against A1's commitments column), what changed in theirs, and what the exchange suggests for the autonomy meta-plan's open questions.

## 5. Timeline (flexes from the confirmed date — currently ~Nov 20, TBD)

*Revised 2026-10-26 (Brad): the Nov 1 glossary target is pushed to **Nov 8** — the glossary gained scope (A5 prior art + CIDS alignment) — and the binding dates are expressed relative to the meeting date **M** (since M is TBD, absolute dates are the fallback if the meeting holds at ~Nov 20). The glossary is **not on the critical path**: the site skeleton, the question list, and Nic's demo are.*

| Window | Tasks | Depends on |
|---|---|---|
| Now → **M−10 days** (fallback Nov 8) | A1 glossary v1 (prior-art-credited) · A5 prior art + due diligence · A2 phrasebook · B1 site skeleton · D1 question list v1 | — (independent) |
| **M−10 → M−5** (fallback Nov 8–13) | A3 fieldwork synthesis · A4 software survey · B2 product language · C1 talk outline · B3 standing-question affordance | 0.4 fieldwork · Nic's demo status |
| **M−5 → M−3** (fallback Nov 13–17) | C2 rehearsal · site polished to summarizable state · dry run of the mutual-education format | C3 demo readiness |
| **M** (~Nov 20, TBD) | **The meeting** (C1 + demo) | meeting date confirmed |
| After | D4 loop + D5 debrief · site update · lessons into QA session 2 inputs | — |

## 6. Open questions

1. **Meeting date and format** (hybrid/AV/attendee mix — the deferred Gate 0 items) still bind C2/C3 timing; the whole schedule shifts with the date.
2. **Register — resolved 2026-10-26 (Brad, "for now"):** the Castoriadis vocabulary stays internal to the Reflect process documents; all collaborator-facing material is conventional SE/plain language (principle 6). QA session 2 need not ratify unless we revisit.
3. **Site naming and hosting** (naming policy applies; unlisted hosting inherited from v2 defaults).
4. **Who runs the room** — Nic presents; does Brad attend and speak (the language-acquisition goal suggests yes, in the question-asking role)?
5. **Translation fidelity policy (pending Brad's call).** When a term's conventional-SE rendering drops its normative content (e.g., "affected public" → "stakeholders" loses the standing claim; "who chose this?" → "governance" loses the authority question), what does the glossary do? Options on the table: mark the loss explicitly ("nearest-neighbor + loses:" tags), leave plain-English normative phrases untranslated, or omit them. *Recommendation: both of the first two — keep already-plain-English phrases as-is, give the conventional nearest-neighbor with an explicit loss marker, so Castoriadis-for-critique survives as the marked gap rather than as vocabulary.*

## 7. Research links

- **T13 is extended** (2026-10-26) with a work package mapping **Castoriadis' terms ↔ conventional systems/software-engineering language** (e.g., vague needs → requirements engineering); the mapping lives in T13's directory and feeds A1's fourth column. See `../moaiwi-research-program/research-topics-v3.md`.
- **T18 "neurosymbolic knowledge engineering"** (name borrowed from Allen's thesis title) records the *deferred* research project behind Brad's notes 3–4: hypergraph → lower-order structure (glossary/ontology) with defunctionalization as the analogy, CIDS as the target formalism, and Elenchus-style prover-skeptic dialogue as a **recorded possibility, not a decision** (including the two-domain extension and the inferential-role ↔ Hoare-logic ↔ Verus link as an input to the Develop meta-plan). **Deferred**: the 3-week R.1 window does not admit it; A1 proceeds with current tools and prior-art credit.

## Revision record (2026-10-26)

In response to Brad's notes (now in `writing/human/moaiwi-action-circle-workflow-notes.md`):

1. **Glossary made conventional** (note 1): SE-language register decided provisionally (principle 6, closes open question 2); glossary rebuilt as four columns with credited prior-art definitions; T13 extended with the terminology mapping (§7).
2. **Software survey** (note 2): added as explicit work item **A4** (both scopes: impact-specific platforms and the real back-office stack; ~$20 budget; landscape note; home chosen when started).
3. **TARA/hypergraph glossary synthesis and the lower-order-structure question** (note 3): **deferred as research**, recorded as **T18**; the glossary for R.1 proceeds with current tools. Partially settled prior art: the Common Approach impact-ontology series distinguishes vocabularies/taxonomies/ontologies and offers CIDS as an existing target formalism.
4. **Elenchus** (note 4): **recorded as possibility in T18, no decision taken** (Brad, 2026-10-26). Candidates recorded: borrowing the method into TARA vs. running the stock tool; the two-domain dialogue (human + LLM-as-counterparty in the other domain's language, grounded in A1/A2 material); the inferential-role ↔ pre/post/invariants ↔ Verus connection as a Develop-meta-plan input.
5. **CIDS = candidate backbone** with due diligence on Common Approach's claims (A5) — due diligence can overturn.
6. **Timeline** (§5): Nov 1 → Nov 8 / M−10; binding dates relative to the meeting date.
