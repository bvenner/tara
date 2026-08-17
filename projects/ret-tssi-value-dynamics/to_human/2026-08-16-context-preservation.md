# Context Preservation — read after a context reset

Everything here is material that existed only in the working conversation and is NOT yet in the research documents (or that has since changed). State as of 2026-08-16.

**Git state (all local, nothing ever pushed):** `f8b10f7` (program + literature + bib v1) → `7550d93` (six-track completion + critiques + track-organized bib) → `9cb8b77` (this note) → `41a6970` (critiques.md six-track revision) → `12b3ffd` (all 11 amendments applied). Working tree clean except the unrelated untracked `anytype-based-tara/research-assistant-architecture-bcv.md`.

**Authoritative current state:** `program/research-program.md` (six tracks, all amendments applied) and `program/critiques.md` are the live documents. `research-log.md` is the chronological record. `findings.md` holds the formal core. The rest of this file covers only what is NOT in those documents.

---

## 1. Project origin (attribution)

**Brad's stated inspiration for the whole research question: the Jou (2020) paper** — "Relationships between rational extended thermodynamics and extended irreversible thermodynamics," *Phil. Trans. R. Soc. A* 378:20190172 (the bib entry notes its explicit invitation to apply extended thermodynamics to "fluxes of capital"). Cite this as the intellectual origin in the Master's exposé introduction.

## 2. Program framing decisions (confirmed with Brad, in order)

1. Master's thesis at a university, **applied mathematics department** → value theory is the application domain, math is home turf.
2. Initially a three-track program; Brad reframed to **four disciplines (physics, mathematics, economics, computer science)** with tracks as interdisciplinary pairings; then completed to **all six pairings** (Tracks A–F). Track letters are stable across refactors.
3. The two last-added tracks are the two **computational** pairings; their roles: Track E = computation as **simulator**, Track F = computation as **certifier**. This symmetry was the rationale for completing the set.
4. Deliverable structure: **Ph.D.-scale research program document first; a specific 6-month Master's exposé deferred** until Brad reviews the program doc and picks a sub-problem.
5. Category/type-theoretic foundations (Track B) added for **mathematical novelty**, extending the RET ↔ Truesdellian rational-thermodynamics parallel.
6. Scope preference: **balanced** — formal theory AND the econophysics second front (ABM + empirical).
7. Formalism depth: **full model specification** in the proposal (state variables, balance laws, Cattaneo constitutive equations, conjectured theorems stated) — not a verbal sketch.

## 3. Master's thesis exposé — format benchmarks (from web research; needed for phase 2)

- ETH Zürich: 10–20 pp, structured, **detailed time plan compulsory**.
- WU Vienna (SEEP): ~10–15 pp incl. 1-p abstract; six sections.
- U Vienna (exposé): 3,000–4,500 words = 10–14 pp, 12 pt, 1.5 spacing.
- Carleton: 3–5 pp single-spaced.
- Sydney: usually ≤2,000 words.
- TU Wien: character-limited sections; **RQ ↔ problem ↔ methods ↔ evaluation traceability** required.
- TU Delft: 15–20 pp, **risks & mitigation, Gantt chart**.
- Common section set: abstract; intro/context; literature review / state of field (with gap table); theory; research questions; methodology & data; expected results; preliminary thesis TOC; timeline; risks; references.

**Agreed target for our exposé: ~12–15 pp / ~5,000 words**, with this structure (in order): Title → Abstract → Introduction & motivation (two paradoxes framing) → State of the field + gap table → Theoretical framework (correspondence) → Research questions → Model specification (full) → Methodology → Expected results & contribution → Preliminary thesis chapter outline → 6-month timeline → Risks & mitigation → References. File path: `proposal/masters-proposal.md`.

## 4. Open next steps (from Brad's list; status)

1. **Download & parse the references** — NOT STARTED. Requires Brad's OK: writes to `papers/incoming/` and runs the TARA `scripts/ingest_pdf.py` pipeline into AnyType + citation graph (outside this project dir). ~half the bib is open access (Freeman MPRA, Cockshott eprints, MDPI Entropy, Jou PMC, arXiv items).
2. **Broaden toward ecological macroeconomics** — DEFERRED, not scoped. Only recorded as a "future application domain" (critiques.md amendment #8). Candidate framing noted in conversation: ecological macro is disequilibrium modeling (stock-flow-consistent, Keen's Minsky ODEs, Giraud's GEMMES); our relaxation framework would give those models a rigorous dynamics foundation.
3. **Critiques** — DONE (`program/critiques.md`).
4. **Grmela / GENERIC multiscale thermodynamics** — literature note done (`literature/grmela-generic-multiscale.md`) **and now integrated** into the program doc as the GENERIC/contact-geometry pole in Track B (amendment #7, applied in `12b3ffd`).

## 5. Status: the consolidated amendments to research-program.md

**ALL 11 APPLIED (commit `12b3ffd`, 2026-08-16)** — no longer pending. critiques.md's amendment list is marked APPLIED. Includes: network-first formulation note (§4), T3 singular-limit scoping, τ_J=0 nesting claim, local-stability caveat, statistical-equilibrium neighbors (§2.4/§6), entropy disclaimer (§3/A2), GENERIC pole (§5), phasing scope-discipline line (§10), E/F infrastructure Status lines (§8/§9), E2 constrained closure discovery, F scope note.

## 6. Open decisions awaiting Brad

- **Master's sub-problem choice**: M1 (default, Track A Phase 1) / M2 (entropy-first) / M3 (category warm-up) / M4 (TSSI recursion analysis, low-risk) / M5 (relaxation-system numerics, CS-flavored) / M6 (formalized recursion in Lean, highest novelty). Table in `research-program.md` §11. **Still open; nothing in the docs settles it.**
- **Git push**: five commits on `main` locally; nothing pushed. Standing rule: never push to main, always a feature branch, and only with confirmation.
- **Ecological macro**: in-scope or not.
- **AnyType ingestion** of papers: needs OK (see §4.1).

## 6.5 Pending commitments (conversation-only, not in any document)

- **DONE (2026-08-16): proposal walkthrough delivered** at `to_human/2026-08-16-proposal-walkthrough.md`. Accessible explainer covering the two paradoxes → the formal correspondence → the six tracks; one section per discipline (physics, mathematics, economics, computer science); a "statistical compass" (§4) using Jaynes' maximum-entropy program as the bridge (closure selection ↔ underdetermination; main-field/state duality ↔ natural/mean parameter duality; Cattaneo ↔ underdamped Langevin, simultaneism = overdamped limit; entropy production ↔ KL decay; SK condition ↔ spectral gap; Foley/Scharfenaker–Semieniuk as Jaynesian endpoints). Each discipline section lifts out as a standalone one-pager. Note: the Langevin/HMC and exponential-family analogies are pedagogical, marked as such in §4.4 — not claims in `research-program.md`. The exposé must still be drafted, with the same accessibility bar.
- **The four-sentence self-identification to preserve**: Brad = "Bradley Vener", go by "Brad", Denver/Mountain time, GitHub `bvenner`, concise communication (see AGENTS.md). Not research content, but relevant to tone of any future writing.

## 7. Working conventions (per AGENTS.md + session)

- Commit only when asked; semantic prefixes (`docs:`/`feat:`); never push without confirmation.
- Ask before destructive commands, git push/checkout, or edits outside the project dir.
- `projects/` is gitignored in the TARA repo; exception added for `projects/ret-tssi-value-dynamics/` (`.gitignore`: `projects/*` + `!projects/ret-tssi-value-dynamics/`).
- Unsupervised-work boundary agreed 2026-08-16: project-dir writes + web research OK; no git, no `papers/` writes, no AnyType/service changes.
- Unrelated untracked file left alone: `anytype-based-tara/research-assistant-architecture-bcv.md`.

## 8. Verification ledger (what was checked, so it isn't re-checked)

- Jou (2020) is **single-author** (was mislabeled Lebon–Jou–Casas-Vázquez).
- Wright (2005) DOI = 10.1016/j.physa.2004.08.006.
- Nikaido's refutation cited as USC mimeo MRG7722 (1978) per Steedman (1984); no published version found.
- Foley (1994) JET 62:321–345, DOI 10.1006/jeth.1994.1018; Scharfenaker–Semieniuk (2017) Metroeconomica 68:465–499; Mohun–Veneziani (2017) J. Econ. Surveys 31:1387–1420.
- Grmela–Öttinger 1997 PRE 56:6620/6633; Grmela Entropy 2015/2021, J. Phys. Commun. 2018. **No Grmela-economics paper found** — do not claim one exists.
- E-track: Raissi et al. 2019 (DOI 10.1016/j.jcp.2018.10.045); Pan–Duraisamy 2018 (10.1137/18M1177263); Gupta–Lermusiaux 2021 (10.1098/rspa.2020.1004); Bar-Sinai et al. 2019 (10.1073/pnas.1814058116); Brennan–Venturi 2018 (10.1016/j.jcp.2018.06.038).
- F-track: Libkind et al. 2022 (arXiv 2105.12282); Morris et al. 2024 (Decapodes, arXiv 2401.17432); Armstrong–Kuusi 2025 Inventiones 242:895–1086 (10.1007/s00222-025-01370-9); van Doorn–Macbeth 2024 ITP (10.4230/LIPIcs.ITP.2024.37); Martin-Dorel–Melquiond 2016 JAR 57:187–217.

## 9. Key intellectual landmarks (theses that must survive)

- The program's spine: **Mohun–Veneziani's underdetermination charge against TSSI is a closure problem; RET's entropy-principle constitutive methodology is the answer** — not just an analogy.
- The correspondence is claimed **formal** (relaxation-limit theorems), not rhetorical.
- Deepest critique: B2 (closure underdetermination) — answered by the Cattaneo closure **nesting the entire gravitation literature at τ_J = 0**.
- Hostile reading to pre-empt (A5): T3 can be read as vindicating simultaneism — it is a *singular* limit, non-uniform in time under technical change; initial layers = post-shock mispricing.
- Probabilist flank (B3): stationary profit-rate dispersion (Scharfenaker–Semieniuk: Laplace, not gamma) is a *prediction* of the driven-relaxation picture, not a refutation.
