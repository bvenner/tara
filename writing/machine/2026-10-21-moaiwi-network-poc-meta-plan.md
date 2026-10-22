---
title: "Meta-plan: moaiwi-network-poc (30-day sprint to workshop pitch)"
date: 2026-10-21
kind: research-plan
project: moaiwi-network-poc
---

# Meta-plan: moaiwi-network-poc

**Date:** 2026-10-21 · **Status:** Phase 0 + Phase A executed 2026-10-21; Gate 1 (framing memo) awaiting Nic review · **Kind:** research-plan (meta-plan: plan to develop a plan)

**Objective:** Within 30 days (assume event by ~Fri 2026-11-20; exact date confirmed at Gate 0), produce and present — Nic presenting — a workshop/panel-format pitch of a structurally abstract business plan for **a corporation that is also a federation of worker cooperatives**, to an invite-only hybrid gathering of contacts from Resist & Build Summit Denver 2026. The goal of the event is **feedback**, not diligence: feedback (including naming/branding input) feeds the subsequent investor-facing-materials phase.

**Pitch thesis (working):** The corporation's reason to exist is its integrated **multi-capital modeling capability** — financial + planetary (material, energy, ecosystem) + social (democracy, well-being, community) — which makes two things compatible: (a) **bottom-up** formation of worker cooperatives with real impact stories and (b) **top-down** capital direction that rapidly raises internal rates of return by funding cooperatives. The model is the product and the edge; modeling is also a revenue line served beyond the federation.

---

## 1. Locked decisions (this conversation)

| Topic | Decision |
|---|---|
| Stage | Feedback stage; real plan comes later. 30-day horizon. |
| Event | Invite-only hybrid meeting of R&B DEN-2026 contacts; workshop/panel format. |
| Audience | R&B network: solidarity-economy movement + values-aligned capital (USSEN, TDC, BII, Kataly, Center for Community Wealth, Cooperation 5280, et al.). Wariness of extractive capital and co-optation is a design constraint. |
| Architecture (legal form) | **Research output**, not a decision. Working base: US, Colorado-first. |
| Governance | Commitment is to economic democracy and the solidarity economy — **not** one-member-one-vote a priori. Significant governance innovation for the adversarial US context is part of the pitch. |
| Impact accounting | Aggregation stance ("no prior commitment to a scale of aggregation") is the **core research question**, presented as open with candidate formalisms. |
| Research scope | Research executes as workspace threads (here), not delegated away. |
| Research lenses | Network science + cooperative game theory; resilience + panarchy (ecology); Ostrom + solidarity economy (sociology); category theory / sheaves; control / operations research. **Thermodynamics/stat-mech deliberately excluded** from the pitch agenda; planetary models lean industrial-ecology/LCA-style accounting. |
| Demos | Impact accounting calculator; federation network simulator; financial model dashboard. Shared synthetic illustrative federation dataset. |
| Deliverable stack | Slidev (live deck) + Marp (PDF handout) + static site with JS demos. |
| Financial realism | Illustrative unit economics and IRR sketch with explicit assumptions; disclaimers on every artifact. |
| Knowledge repository | **Reversed 2026-10-21 (Brad):** B1–B3 reference materials are integrated into the hypergraph knowledge repository; memo claims cite `doc :: section`. (Original posture: standalone, no ingestion.) |
| Naming/branding | Structurally abstract pitch; naming is a key investor input and buy-in mechanism. "moaiwi" is internal only. Harvest naming input at the workshop. |
| Roles | Nic: main presenter, reviews all outputs before any next phase proceeds. Brad: builds the plan and artifacts, available for questions, not presenting. |

## 2. Gate 0 open items (deferred by Brad, 2026-10-21 — bind at Phase E, not Phase A)

- Exact event date, slot length, workshop-vs-panel balance, and run-of-show expectations.
- Attendee composition: how many capital-side vs movement-side; named orgs if shareable.
- Hybrid platform and AV (screen-share quality for demos; in-room projection).
- Site visibility: public vs unlisted link (recommend unlisted — pre-announcement, structurally abstract).
- Review protocol with Nic: channel (repo docs vs live review), turnaround expectations per gate.

## 3. Roles, gates, and review protocol

- **Rule:** Nic reviews all outputs before dependent work proceeds. Independent parallel work may continue during review.
- **Review package convention:** one page per gate — what was produced (links), 2–4 decisions needed from Nic, recommendation + default if no response. Target ≤30 min review time.
- **Gate calendar** (assumed; Day 1 = Wed 2026-10-21, Day 30 = Fri 2026-11-20):
  - Gate 0 — Tue Oct 22: open items above (now deferred).
  - Gate 1 — Mon Oct 26: framing memo (thesis, tension, abstraction policy, audience register).
  - Gate 2 — staggered: B1 architecture/governance memo Thu Oct 29; B2 impact-accounting memo Mon Nov 2; B3 capital-allocation memo Wed Nov 4.
  - Gate 3 — Wed Nov 11: business-plan content.
  - Gate 4 — Wed Nov 11: demos (shared review window with Gate 3).
  - Gate 5 — Tue Nov 17: rehearsal + final approval (Nic presents).
  - Gate 6 — post-event: feedback synthesis + next-phase backlog.

## 4. Phases

### Phase 0 — Setup (Days 1–2, Oct 21–22) ✅ done 2026-10-21
- Confirm Gate 0 items; freeze calendar. (Deferred — recalibrate when date is known.)
- Scaffold project: `projects/moaiwi-network-poc/` with `AGENTS.md` resume path; `writing/machine/` notes per frontmatter convention; thread entry in workspace `AGENTS.md`. ✅
- Stand up repo structure for deliverables (deck, site, demos, memos) and the disclaimer convention. ✅ (planned layout recorded in project `AGENTS.md`)

### Phase A — Framing (Days 1–5, Oct 21–26) ✅ done 2026-10-21 → Gate 1 awaiting Nic
- Lock pitch thesis and the productive tension (bottom-up formation vs top-down capital direction) as the deck's spine.
- Audience register: movement-compatible language legible to impact capital; capital structurally subordinated to economic democracy; governance innovation as credibility, not footnote.
- Structural abstraction policy: consistent role labels ("the Corporation", "the Federation", "member cooperatives", "the modeling platform"); no names; naming framed as the audience's to contribute.
- **Output:** `projects/moaiwi-network-poc/framing-memo.md`. Dependent: C, E. Independent: B, D scaffolding.

### Phase B — Research sprints (Days 5–14, Oct 26–Nov 4) → Gate 2 (staggered)
Three parallel tracks, each producing an **options memo** (≤3 pp) + **research-proposals list** for the plan's R&D agenda. **All three tracks integrate their downloaded reference materials into the hypergraph knowledge repository** (OpenAlex works via `pipeline.py expand`; manually-downloaded PDFs staged in `papers/incoming/<key>.pdf` with fulltext `mode:"local"`; rebuild with `build_hypergraph.py --force`) **and ground memo claims as `doc :: section`** per the `hypergraph-grounding` skill. Each track runs from its research plan in `projects/moaiwi-network-poc/research-plans/` (work packages + keyword/search strategy), reviewed before any reference downloads — the pre-download gate:
- **B1 Architecture & governance:** comparative scan (Mondragon Corporation; Evergreen/Cleveland; union co-op model; steward ownership; platform co-ops; Colorado co-op + benefit-corporation statutes). Governance innovation requirements for the adversarial US context (investor capital vs democratic control; candidate instruments: non-voting capped preferred, steward-ownership/golden share, reserved-matters classes, patient debt/community shares, layered classes). Candidate architectures with trade-offs; **no final recommendation** — the choice is positioned as the audience's and investors' to shape.
- **B2 Impact accounting:** the aggregation question as the core open research output. Survey: impact-weighted accounts, multi-capital/IRIS+ frameworks, SROI, donut-economics accounting, Ostrom-informed commons accounting; candidate formalisms for "aggregation without prior commitment to scale" (multi-scale with explicit aggregation maps; vector/set-valued impacts; sheaf-theoretic local-to-global composition). Deliver 2–3 candidate formalisms the demos can instantiate.
- **B3 Capital allocation & business process:** OR/control framing of top-down capital direction; network science + cooperative game theory (Shapley/Owen values, coalition structure, network formation) for surplus and solidarity-fund design; business process model of the co-op lifecycle (formation → funding → scaling → replication/exit). Feeds the financial dashboard's structure.

### Phase C — Business plan content (Days 12–21, Nov 2–11) → Gate 3
Assemble from A+B into the plan the pitch presents:
1. Thesis and productive tension.
2. Value proposition; modeling-as-a-product revenue line (served to other co-op networks, investors, municipalities) + internal capital-allocation edge.
3. Impact thesis: how social, environmental, and financial impacts are generated and tracked per co-op and federation-wide without pre-committed aggregation.
4. Architecture and governance options (research framing; Colorado-first base).
5. Illustrative cohort economics: capital stack, per-co-op unit economics, federation-level returns/IRR sketch — all clearly labelled illustrative over synthetic data.
6. R&D agenda (B1–B3 research proposals) as the innovation program that keeps the three impact areas honest.
7. Risks (legal/US context, capital constraints, co-op formation pipeline, model credibility, co-optation) + how the design addresses them.

### Phase D — Demos (Days 5–21, Oct 26–Nov 11) → Gate 4
- **Shared synthetic federation dataset:** one schema (co-ops, members, capital flows, impact measures at several scales), versioned, assumptions documented.
- **D1 Impact accounting calculator:** multi-scale computation over the synthetic federation; aggregation choices visible and adjustable (instantiates B2 candidate formalisms).
- **D2 Federation network simulator:** network growth, capital/solidarity-fund flows, resilience under shocks.
- **D3 Financial model dashboard:** projections, investor returns under candidate instruments, scenario toggles (illustrative).
- **Site:** Astro or Vite static build; demos in-browser (vanilla JS + lightweight viz); unlisted hosting (GitHub Pages from a feature branch — push only with explicit confirmation); demo length ≤90 s each; screenshot fallbacks for hybrid.
- Note: demos can proceed on dataset schema + scaffolding while B2/B3 finalize metric definitions.

### Phase E — Assembly & rehearsal (Days 21–27, Nov 11–17) → Gate 5
- Slidev deck for the session; Marp PDF handout for in-person attendees and the leave-behind.
- Workshop facilitation design: discussion prompts per section; **structured naming/branding capture** (the buy-in moment); feedback capture templates (investor interest signals, objections, offers to help); hybrid facilitation plan (in-room + virtual participation).
- Rehearsal with Nic presenting; harden demos for screen share and bandwidth; run-of-show timing.

### Phase F — Event + feedback capture (Days 28–30, Nov 18–20) → Gate 6
- Deliver workshop/panel; capture feedback live into structured backlog (naming inputs verbatim; investor interest; objections; commitments).
- Post-event synthesis note in `writing/machine/`; output = prioritized backlog for the **next phase** (investor-facing materials, real plan).

## 5. Deliverables checklist

- [x] Framing memo (A) — `projects/moaiwi-network-poc/framing-memo.md`
- [x] B1–B3 research plans (work packages + keyword/search strategy; pre-download gate)
- [ ] Three options memos + research-proposals lists (B1–B3)
- [ ] B1–B3 reference corpus integrated into the knowledge repository (hypergraph rebuilt)
- [ ] Business plan content document (C)
- [ ] Synthetic federation dataset + schema doc (D)
- [ ] Three browser demos (D1–D3)
- [ ] Static site (unlisted) hosting plan + demos (D)
- [ ] Slidev deck (E)
- [ ] Marp PDF handout (E)
- [ ] Workshop facilitation + feedback capture kit (E)
- [ ] Post-event feedback synthesis + next-phase backlog (F)

## 6. Risks & mitigations

| Risk | Mitigation |
|---|---|
| Nic's review bandwidth is the critical path | Compact review packages (≤30 min), staggered gates, defaults-if-silent policy agreed at Gate 0. |
| 30-day compression | Scope discipline: synthetic data, options-not-decisions, corpus ingestion limited to B1–B3 reference needs; demo scope frozen at Gate 4. |
| Audience mis-register (movement wariness of capital) | Framing phase centers economic democracy; capital subordinated; co-optation risk named in the plan, not hidden. |
| Illustrative numbers read as projections | "Illustrative — synthetic federation data" disclaimer on every artifact, slide, and demo. |
| Hybrid tech failure | Static hosting, screenshot fallbacks, PDF handout, offline-capable demo builds. |
| Premature specificity (names, legal form, governance) | Structural abstraction policy (A); options memos never recommend single choices; naming deliberately delegated to the audience. |
| Unnamed-entity confusion in the deck | Fixed role-label glossary in the framing memo, applied everywhere. |

## 7. Workspace integration (during implementation)

- `projects/moaiwi-network-poc/` — project dir + `AGENTS.md` resume path linking `writing/machine/` notes; B1–B3 references integrated into the hypergraph knowledge repository (`projects/knowledge-repository-poc/`).
- `writing/machine/` notes with YAML frontmatter (`title`, `date`, `kind`, `project: moaiwi-network-poc`).
- Thread entry in workspace `AGENTS.md`.
- Git: semantic prefixes; commit only when asked; feature branch only; confirm before any push.

## 8. Out of scope this sprint

Final legal architecture; final governance or investor-instrument decision; real financial projections; name/brand selection; corpus ingestion beyond B1–B3 reference needs; diligence-grade investor materials (that is the next phase, fed by Gate 6 output).
