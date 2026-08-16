# Research Log

## 2026-08-15 — Project initialization and program document

**Task (from Brad):** Develop a research proposal in Marxian econophysics: apply rational extended thermodynamics (RET) to the temporal single-system interpretation (TSSI) of the transformation problem; working analogy = hyperbolic (RET) vs parabolic (classical) PDEs ~ temporal (TSSI) vs simultaneous (dual-system) determination.

**Decisions recorded:**
- Venue: Ph.D.-scale research program document first; 6-month Master's thesis exposé (applied mathematics department) deferred to phase 2, sub-problem to be chosen after program review (candidates M1/M2/M3 in §8 of the program doc).
- Mathematical-novelty track added at Brad's direction: category-theoretic / type-theoretic foundations of RET, extending the RET ↔ Truesdellian "rational thermodynamics" parallel.
- Formalism depth: full model specification. Scope: balanced theory + econophysics/empirical second front.
- Home discipline: applied mathematics → value theory framed as application domain.

**Work done:**
1. Explored workspace; no prior Marxian-econophysics material found (workspace is TARA/AnyType research-assistant infrastructure + one interpretability project).
2. Literature research (web): four strands — TSSI/transformation debate; RET mathematics; classical econophysics; gravitation dynamics + finite-speed precedents in economics; plus foundations (categorical thermostatics, Lawvere, Coleman–Noll tradition). ~20 anchor sources identified.
3. Scaffolded project per autoresearch convention (`research-state.yaml`, `literature/`, `findings.md`, `program/`, `to_human/`).
4. Wrote 18 literature summaries with verified citations.
5. Wrote `findings.md`: formal correspondence table, model skeleton, conjectures T1–T4, track syntheses, risk register.
6. Wrote `program/research-program.md` (main deliverable) and `program/references.bib`.

**Citation corrections during verification:**
- The RET/EIT comparison survey (PMC7134952) is **Jou (2020)**, *Phil. Trans. R. Soc. A* 378:20190172, single author — not "Lebon, Jou & Casas-Vázquez (2019)". Fixed in lit note; bib uses correct entry. Bonus: Jou explicitly invites extended-thermodynamics applications to "fluxes of capital" in social sciences.
- Wright (2005) DOI corrected to 10.1016/j.physa.2004.08.006 (arXiv cond-mat/0401053).
- Nikaido's refutation cited as USC mimeo MRG7722 (1978), as referenced in Steedman (1984) — no published version verified; flagged accordingly.
- Unverified page numbers omitted rather than guessed (e.g., Veneziani 2005).

**Key structural insight recorded:** the Mohun–Veneziani "underdetermination" charge against TSSI is precisely a *closure problem*; RET's entropy-principle-as-constitutive-selection-rule is therefore not just an analogy but the missing methodology. Also: Burger–Caffarelli–Markowich–Wolfram (2013) provides an existing rigorous relaxation limit (kinetic → parabolic) in price formation — a citation shield for the methodology.

**Next steps:**
- Brad reviews `program/research-program.md`.
- Choose Master's sub-problem (default recommendation: M1 = Track A Phase 1).
- Draft `proposal/masters-proposal.md` (exposé format, ~12 pp, 6-month timeline).
- Optional: ingest anchor PDFs via `scripts/ingest_pdf.py` into the AnyType citation graph.

## 2026-08-16 — Git commit + critiques document

**Git:** committed on main as `f8b10f7` ("docs: add RET-TSSI research program"). Note: `projects/` was gitignored ("non-TARA projects"); changed to `projects/*` with an explicit exception for this project directory. Not pushed (per standing rule). Unrelated untracked file (`anytype-based-tara/research-assistant-architecture-bcv.md`) left alone.

**Critiques:** wrote `program/critiques.md` — 14 steelmanned objections in five groups (A economics, B Marxian flank, C mathematics, D physics, E meta), each with objection/force/response/program-impact. Deepest: B2 (closure underdetermination — answered by constitutive-theory discipline + nesting of gravitation literature at τ_J=0) and C1 (entropy extension may not exist — load-bearing theorems don't need it).

**Verification finds:**
- Foley (1994, JET 62:321–345, DOI 10.1006/jeth.1994.1018) — statistical equilibrium theory of markets; 300+ citations; was missing from our background. Referee-visible neighbor.
- Scharfenaker & Semieniuk (2017, Metroeconomica 68:465–499) — firm-level profit rates are Laplace-distributed and stationary; strengthens B3 critique and Track C targets.
- Mohun & Veneziani (2017, J. Econ. Surveys 31:1387–1420) — axiomatic "impossibility result" reading of the transformation problem.
- GENERIC verified: Grmela–Öttinger PRE 56:6620/6633 (1997); Grmela Entropy 2015/2021; J. Phys. Commun. 2018 guide; Öttinger 2005 book. No Grmela-economics paper found; don't assert one exists.

**Bib:** appended 10 entries (foley1994, scharfenaker-semieniuk2017, mohun-veneziani2017, jin-xin1995, grmela-ottinger1997a/b, grmela2015, grmela2018, grmela2021, ottinger2005).

**Pending Brad's approval:** 9 consolidated amendments to `research-program.md` (listed at end of critiques.md). Uncommitted: critiques.md + bib update + this log entry — left unstaged per standing git rule.

## 2026-08-16 — Track refactor (3 → 4 tracks, four-discipline framing)

**Per Brad:** reframe the program as a four-discipline enterprise (physics, mathematics, economics, computer science) with tracks as interdisciplinary pairings.

**Result** (`program/research-program.md`):
- **Track A — Physics × Economics:** hyperbolic (RET-formalized) value-price system (the applied core; unchanged content).
- **Track B — Mathematics × Physics:** categorical/type-theoretic foundations of extended thermodynamics (unchanged content).
- **Track C — Computer Science × Economics:** simulation and empirical estimation (unchanged content).
- **Track D — Mathematics × Economics:** NEW — the formal core in economics' own language. Sub-projects D1 (well-posedness of the discrete/continuous TSSI recursions — answers Veneziani without physics vocabulary), D2 (axiomatic transformation theory, engaging Mohun–Veneziani 2017), D3 (equilibrium as singular limit of disequilibrium dynamics — economics-facing restatement of T3), D4 (network/spectral methods, positioning vs Foley's statistical equilibrium).
- Overview §1, gap table (§2.5: G1, G3 now also D), §3 closing note, phasing §8 (Year 1 adds D1; Year 2 adds D2–D3; Year 3 adds D4), and decision point §9 all updated; sections renumbered (§7 phasing → §8; §8 decision → §9; §9 references → §10).
- **New Master's candidate M4** added (Track D Phase 1: TSSI recursion analysis) — consequence of Track D. Recommendation stays M1; M4 is the low-risk alternative.
- critiques.md amendment list: phasing reference updated to §8.

**Note:** the 9 pending amendments from critiques.md were NOT applied (awaiting Brad's review of that document). Some overlap with this refactor is possible; reconcile after his approval.

## 2026-08-16 — Six-track completion + bibliography reorganization

**Per Brad:** fold the two remaining discipline-pairs (Physics × CS, Mathematics × CS) into the program as Tracks E and F, completing all six pairings of the four disciplines; reorganize references.bib by track; find new references for the two new tracks.

**Program document (`research-program.md`):**
- **Track E — Physics × Computer Science** (§8): computational thermodynamics of value-price dynamics. E1 numerical methods for relaxation systems on networks (Jin–Xin relaxation schemes, front tracking); E2 data-driven closure identification (sparse regression / neural / physics-informed) — the computational answer to the underdetermination critique; E3 ABM-to-continuum (Kac–Goldstein) verification.
- **Track F — Mathematics × Computer Science** (§9): certified and executable mathematics. F1 proof-assistant formalization (Lean 4/Coq) of the discrete TSSI recursion theorems; F2 executable categorical models (AlgebraicJulia/Catlab/Decapodes); F3 verified numerics (CoqInterval/Flocq tradition).
- Overview, §3 closing, gap table (new G5, G6), phasing, and decision point updated; new Master's candidates **M5** (relaxation-system numerics) and **M6** (formalized TSSI recursion). Sections renumbered (§8 phasing → §10; §9 decision → §11; §10 references → §12).

**Bibliography (`references.bib`):** reorganized into six track sections (75 entries, braces balanced). 12 new entries verified during search:
- Track E: raissi2019 (PINNs, JCP 378:686–707, DOI 10.1016/j.jcp.2018.10.045); pan-duraisamy2018 (SIAM JADS 17:2381–2413, DOI 10.1137/18M1177263); gupta-lermusiaux2021 (Proc. R. Soc. A 477:20201004, DOI 10.1098/rspa.2020.1004); bar-sinai2019 (PNAS 116:15344–15349, DOI 10.1073/pnas.1814058116); brennan-venturi2018 (JCP 372:281–298, DOI 10.1016/j.jcp.2018.06.038); jin-xin1995 moved from earlier draft into E.
- Track F: libkind-etal2022 (Operadic modeling of dynamical systems, arXiv 2105.12282); morris-etal2024 (Decapodes, arXiv 2401.17432); armstrong-kuusi2025 (Inventiones 242:895–1086, DOI 10.1007/s00222-025-01370-9); coarsegraining-lean and lerayhopf-lean (GitHub repos, @misc); vandoor-macbeth2024 (ITP 2024, LIPIcs 309:37, DOI 10.4230/LIPIcs.ITP.2024.37); martin-dorel-melquiond2016 (J. Automated Reasoning 57:187–217).

**Uncommitted:** research-program.md, references.bib, critiques.md (one § ref fix), research-log.md, literature/grmela-generic-multiscale.md. Per standing rule, left unstaged for Brad.
