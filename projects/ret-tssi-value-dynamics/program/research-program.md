# Finite-Speed Value: A Research Program in Marxian Econophysics

**Rational extended thermodynamics as a formal framework for the temporal single-system interpretation of the transformation problem**

Bradley Vener — research program document, 2026-08-15
Working repository: `projects/ret-tssi-value-dynamics/`

---

## 1. Overview

Twentieth-century physics and twentieth-century Marxian economics each produced a long-running controversy with the same abstract shape.

In thermodynamics, the classical theory of irreversible processes closes its equations *instantaneously*: the heat flux is slaved to the contemporaneous temperature gradient by Fourier's law. The resulting field equations are parabolic and predict infinite propagation speeds — the "heat paradox." Cattaneo (1948) resolved the paradox by promoting the flux to an independent state variable with a finite relaxation time, producing hyperbolic (telegraph-type) dynamics. Müller and Ruggeri built this move into a systematic framework — **rational extended thermodynamics (RET)** — in which balance laws, constitutive relations restricted by an entropy principle, and a convex entropy extension yield symmetric-hyperbolic systems with well-posed Cauchy problems, finite characteristic speeds, and rigorous relaxation limits: the classical parabolic theory is the zero-relaxation-time singular limit of the extended theory (Ruggeri & Strumia 1981; Chen, Levermore & Liu 1994).

In Marxian value theory, the simultaneous dual-system tradition (Bortkiewicz 1907; Sraffa 1960; Steedman 1977) likewise closes its equations instantaneously: input prices equal output prices by construction, and all magnitudes are determined at a single logical instant by an algebraic fixed point. On this reading, Marx's two aggregate equalities fail and the labor theory of value appears inconsistent or redundant. The **temporal single-system interpretation (TSSI)** (Kliman & McGlone 1999; Freeman 1996) resolves the inconsistency by temporalizing the closure: inputs enter at time *t*, outputs emerge at *t+1*, and values and prices form one interdependent system determined sequentially in historical time. But TSSI, as its sharpest critics note, still lacks a rigorous dynamical foundation: no well-posed evolution system, no precise equilibrium concept, no stability theory (Veneziani 2005; Mohun & Veneziani 2009).

**This program's thesis:** the TSSI stands to simultaneist value theory as RET stands to classical irreversible thermodynamics — and this is a formal correspondence, not a metaphor. Concretely:

- value-price dynamics can be written as a system of **hyperbolic balance laws with relaxation**, in which intersectoral capital fluxes are promoted to state variables obeying Cattaneo-type evolution equations;
- the simultaneist dual-system is recovered as the **τ → 0 singular (relaxation) limit**, which explains both its approximate validity near equilibrium and its pathologies away from it;
- the **entropy methods** of modern hyperbolic theory supply the missing well-posedness and stability theory — including a unifying criterion (a Shizuta–Kawashima-type coupling condition) for when market prices converge to prices of production, a question on which the classical "gravitation" literature has only case-by-case answers.

The program is, by design, a four-discipline enterprise — **physics**, **mathematics**, **economics**, and **computer science** — and its four tracks are the interdisciplinary pairings through which those disciplines actually meet on this problem:

- **Track A — Physics × Economics.** The applied core: build and analyze the hyperbolic (RET-formalized) value-price system.
- **Track B — Mathematics × Physics.** Foundations: category/type-theoretic axiomatization of extended thermodynamics, extending the analogy to the Truesdellian "rational thermodynamics" tradition.
- **Track C — Computer Science × Economics.** Computational and empirical: agent-based simulation, the simulation-to-continuum correspondence, and estimation from input-output data.
- **Track D — Mathematics × Economics.** The formal core in economics' own language: well-posedness and stability of temporal value dynamics as dynamical systems, and the axiomatic theory of the transformation problem.
- **Track E — Physics × Computer Science.** Computational thermodynamics: numerical methods for hyperbolic relaxation systems on networks, and data-driven (machine-learned) discovery of the constitutive closure.
- **Track F — Mathematics × Computer Science.** Certified and executable mathematics: proof-assistant formalization of the program's theorems, and executable categorical models of its compositional structure.

All six pairings of the four disciplines are represented. Each track develops the program's shared object — the correspondence between simultaneous/instantaneous determination and temporal/relaxational determination — in the idiom of its two disciplines, and results cross-import between tracks (most directly between A and D, and across the computational cluster E–F–C). Track A Phase 1 doubles as a six-month Master's thesis in applied mathematics.

## 2. Background and gap analysis

### 2.1 The transformation problem and TSSI

The simultaneous determination of values and prices (Bortkiewicz; Sraffa) generated the century-long "transformation problem" and the redundancy critique of the labor theory of value. TSSI answers: determination is sequential (inputs at *t*, outputs at *t+1*) and single-system (values and prices interdependent, linked by the time-varying monetary expression of labor time). Under TSSI, Marx's two aggregate equalities hold, and the falling-rate-of-profit argument survives the Okishio theorem. Freeman (1996) gives the continuous-time formulation: conservation of value as differential equations — the natural substrate for this program.

**Gap G1.** Veneziani (2005): TSSI "lacks both a clear definition of equilibrium and a rigorous analysis of disequilibrium dynamics; the dynamic framework is incomplete." Mohun & Veneziani (2009) add the underdetermination charge: the equations do not pin down their own trajectories. In the language of continuum physics, TSSI has balance laws but no **constitutive theory** and no **well-posedness theory**. This is exactly the gap RET's methodology fills.

### 2.2 Rational extended thermodynamics

RET's structure: balance laws ∂u/∂t + Σ∂F_k(u)/∂x_k = G(u); constitutive relations restricted by an entropy principle (Müller 1967; Liu 1972); a concave entropy density; and the Ruggeri–Strumia theorem (1981): a convex entropy extension renders the system symmetric hyperbolic in the main-field (Lagrange-multiplier) variables — hence finite speeds and a well-posed Cauchy problem. Two further bodies of theory are essential here:

- **Relaxation limits** (Chen–Levermore–Liu 1994): stiff relaxation drives solutions onto the equilibrium manifold; the reduced dynamics is parabolic; the subcharacteristic condition governs admissibility of the limit.
- **Stability** (Hanouzet–Natalini 2003; Ruggeri–Serre 2004; Bianchini–Hanouzet–Natalini 2007): entropy dissipation plus the Shizuta–Kawashima coupling condition gives global existence and decay to equilibrium, with the entropy (plus compensation term) as Lyapunov functional.

**Gap G2.** RET has never been applied outside physics and engineering, and its *foundations* remain un-axiomatized in modern (categorical) terms: the only categorical thermodynamics on record is equilibrium thermostatics (Baez–Lynch–Moeller 2023), and the only categorical continuum thermodynamics treats the Truesdellian, non-extended theory (Lawvere 1986).

### 2.3 Gravitation dynamics

The classical literature on convergence of market prices to prices of production — cross-dual adjustment processes in which profit-rate differentials drive capital reallocation and excess demand drives prices (Steedman 1984; Flaschel & Semmler 1987; Duménil & Lévy 1987) — reaches mixed conclusions: Nikaido-type refutations, Steedman's negative cases, Flaschel–Semmler's positive results for *modified* processes, and Cockshott's (2016) simulations in which some reproduction schemes converge and others do not.

**Gap G3.** No unifying stability criterion exists. All these models slave capital reallocation *instantaneously* to profit-rate differentials — a Fourier-type closure. The hyperbolic (Cattaneo) extension, with the SK condition as the convergence diagnostic, is the natural unifier.

### 2.4 Classical econophysics and finite-speed precedents

Farjoun & Machover (1983) rebuilt political economy probabilistically; Cottrell, Cockshott, Michaelson, Wright & Yakovenko (2009) systematized "classical econophysics" with agent-based models in which value relations are emergent; Wright (2005) reproduces the empirical distribution of profit rates (dispersed, gamma-like — not equalized). The program must also position itself against the statistical-equilibrium tradition in economics proper: Foley (1994) develops markets as maximum-entropy equilibrium, and Scharfenaker & Semieniuk (2017) document stationary, Laplace-distributed (not equalized) firm-level profit rates — both are static endpoints whose time-development these dynamics supply. Two precedents show finite-speed/relaxation methods already accepted in mathematical economics: telegraph-process option pricing (Ratanov 2007), motivated explicitly by the infinite propagation speed of Brownian models; and the Boltzmann-type price-formation model of Burger, Caffarelli, Markowich & Wolfram (2013), proved to converge to the parabolic Lasry–Lions equation as the transaction rate diverges — a rigorous relaxation limit in economics.

**Gap G4.** Econophysics has no continuum (field) theory of value-price dynamics; the value-theory literature has no finite-speed models. The persistent empirical *dispersion* of profit rates — impossible under instantaneous equalization — is the natural signature of a relaxational system under continuous forcing.

### 2.5 Gap summary

| # | Gap | Track that addresses it |
|---|---|---|
| G1 | TSSI lacks closure/well-posedness/stability (Veneziani critique) | A, D |
| G2 | No non-physical application of RET; no categorical axiomatization of non-equilibrium thermodynamics | A, B |
| G3 | No unifying criterion for gravitation convergence | A, D |
| G4 | No continuum theory in classical econophysics; unexplained profit-rate dispersion | A, C |
| G5 | No numerical infrastructure for hyperbolic value-price dynamics; closures postulated rather than identified from data | E |
| G6 | No machine-checked or executable formalization of value-theoretic dynamics or of extended-thermodynamics foundations | F |

## 3. The core correspondence

| Classical irreversible thermodynamics | Simultaneist value theory |
|---|---|
| Instantaneous closure (Fourier's law) | Instantaneous determination (input prices = output prices; flows slaved to current differentials) |
| Parabolic equations; infinite propagation speed | Algebraic fixed point; "instantaneous equilibration" |
| Heat paradox | Inconsistency/redundancy charges; Okishio-type results |
| Valid near equilibrium, smooth fields | Valid (if at all) near stationary technical conditions |

| Rational extended thermodynamics | TSSI, formalized (this program) |
|---|---|
| Fluxes as state variables; τ ∂q/∂t + q = −κ∇T | Capital fluxes as state variables; τ_J dJ/dt + J = −κ∇_sector r |
| Hyperbolic balance laws; finite characteristic speeds | Sequential determination; finite-speed disturbance propagation on the input-output network |
| Entropy concave in the extended state | Convex functional on deviations from production-price equilibrium (to be constructed) |
| Parabolic theory = τ→0 singular limit | Simultaneist system = τ_J→0 singular limit |
| SK condition ⇔ decay to equilibrium | Capital-mobility coupling condition ⇔ gravitation convergence |
| Entropy principle selects constitutive relations | Closure selection answers the underdetermination charge |

*Convention on "entropy":* throughout, "entropy" denotes the convex structure (a concave density in the state variables) that makes the structural theorems work — the mathematical object behind Ruggeri–Strumia and Ruggeri–Serre. No operational thermodynamic claim (adiabatic accessibility, Carnot efficiency, and the like) is made; no "second law of economics" is asserted. See Track A's A2 for the same disclaimer at the point of use.

The analogy extends one level deeper on the foundations side: just as value theory has rival "rationalizations" (New Interpretation vs. TSSI), non-equilibrium thermodynamics has rival rational reconstructions — Truesdell–Coleman–Noll rational thermodynamics (memory functionals; Clausius–Duhem as constraint on constitutive relations via arbitrary supplies) versus the Müller–Liu–Ruggeri line (extended state space; entropy principle via Lagrange multipliers). Track B axiomatizes both within one categorical framework.

This shared object — the correspondence above — is what the six tracks develop in their respective discipline-pairings: physics and economics in Track A, mathematics and physics in Track B, computer science and economics in Track C, mathematics and economics in Track D, physics and computer science in Track E, mathematics and computer science in Track F.

## 4. Track A — Physics × Economics: the hyperbolic value-price system

**Disciplines.** Physics (rational extended thermodynamics) applied to economics (Marxian value theory).

**Goal.** Construct and analyze a hyperbolic balance-law model of temporal value-price dynamics; deliver the well-posedness, stability, and relaxation-limit theory that TSSI lacks. This is the program's applied core; Track D restates the same results in the vocabulary of mathematical economics, and the two tracks cross-import rather than duplicate.

**Formulation note (network-first).** The rigorous home of the model is a *relaxation system of ODEs on the sector network* — inertial, telegraph-type adjustment dynamics on a graph — not a PDE over a spatial continuum. "Finite propagation speed" means: a shock in sector *i* reaches sector *j* no faster than the graph distance times a per-link transmission speed; hyperbolic-vs-parabolic here distinguishes the spectral structure of the generator (inertial/oscillatory vs. purely diffusive modes), a property any ODE semigroup has or lacks. The "hyperbolic balance laws" language is reserved for the continuum (large-network/mean-field) limit, where the RET theorems apply literally.

**A1 (Phase 1; six months; candidate Master's thesis).** Minimal model: n-sector circulating-capital economy in continuous time (Freeman 1996 base), state u = (p, K, J) with capital-balance continuity equations on the input-output network and Cattaneo closure τ_J dJ_ij/dt + J_ij = κ_ij(r_j − r_i). At τ_J = 0 this closure reduces to the instantaneous cross-dual rule J_ij = κ_ij(r_j − r_i) — the Cattaneo extension thus *nests the entire gravitation literature* (Steedman 1984; Flaschel & Semmler 1987; Duménil & Lévy 1987) as its zero-relaxation-time special case. Deliverables (theorems T1–T4):

- **T1, well-posedness:** local existence/uniqueness for the quasilinear system; global existence near the production-price equilibrium for small data.
- **T2, linear analysis:** spectral structure of the linearization; finite front speeds; semigroup convergence to the parabolic gravitation semigroup as τ_J → 0⁺.
- **T3, relaxation limit (singular):** u^τ → u⁰ with O(τ) error estimates on compact time intervals; the limit system is the simultaneous-closure dynamics whose rest point is the Sraffian fixed point. The limit is *singular* — it changes the type of determination and is not uniformly valid in time; the initial layer (the post-shock transient during which simultaneous closure misprices) is itself an economic result. *This makes precise — and bounds — the sense in which simultaneism is the equilibrium approximation of temporal determination.*
- **T4, stability criterion:** an SK-type coupling condition on (A, κ) equivalent to asymptotic convergence to the equalized-profit-rate state; check that Flaschel–Semmler's stabilizing modifications enforce it and that Nikaido/Cockshott non-convergence cases violate it.
- Small-scale numerics: finite-speed propagation of a sectoral profit shock, contrasted with diffusive spread.

**A2 (Phase 2).** The entropy problem: construct a convex entropy extension for the nonlinear system (candidates: relative-entropy functionals on price-value deviations; distributional entropy à la Farjoun–Machover), or prove obstructions and pass to EIT-style generalized entropies. Success gives symmetric-hyperbolic form (Ruggeri–Strumia) and a genuine H-theorem for value dynamics; the economic interpretation of entropy production (decay of profit-rate differentials as dissipation of arbitrage) is itself a paper. Per §3, "entropy" here means the convex Lyapunov structure that makes the theorems work — the interpretive reading is illustrative, not an operational thermodynamic claim.

**A3 (Phase 3).** Full TSSI closure: endogenous MELT dynamics, fixed capital, joint production; stochastic forcing (persistent dispersion of profit rates as the stationary state of a driven relaxational system — contact with Farjoun–Machover's gamma distribution).

**Methods.** Semigroup theory and singular perturbation for ODE/network systems; symmetric-hyperbolic and entropy methods for the PDE/network extension; standard tools: Chen–Levermore–Liu, Hanouzet–Natalini, Ruggeri–Serre, Boillat–Ruggeri subcharacteristic theory.

**Risks.** R1: no convex entropy exists for natural closures → fall back to Lyapunov-only stability (T4 does not require symmetric hyperbolicity) and EIT-style frameworks. R2: T4's condition may only be sufficient, not characterizing → scope the claim accordingly. Stability results are local (small-perturbation theorems); global dynamics come from simulation (Track C) alone, and no global nonlinear stability claims are made.

## 5. Track B — Mathematics × Physics: foundations of extended thermodynamics

**Disciplines.** Mathematics (category theory, type theory, geometry) applied to physics (thermodynamics).

**Goal.** A category/type-theoretic axiomatization of extended thermodynamics, extending the program's central analogy to the foundations of thermodynamics themselves; the economic application doubles as the test case.

**Geometric pole (GENERIC).** Alongside the operadic/Lawvere route, the axiomatization must engage Grmela–Öttinger's GENERIC and its contact-geometry formulation of multiscale thermodynamics (Grmela & Öttinger 1997 I & II; Grmela 2015, 2018, 2021; Öttinger 2005): GENERIC supplies the geometric architecture — Poisson kinematics, degeneracy conditions, Legendre/contact structure — in which RET and the balance-law view appear as particular realizations. B1's operad and B2's "two procedures" both have natural statements in this setting, and the value→price passage is itself a Grmela-type reduction between levels of description.

- **B1 — Compositional non-equilibrium thermodynamics.** Baez–Lynch–Moeller (2023) axiomatize equilibrium thermostatics as algebras of an operad of convex relations, with entropy maximization as the composition rule. The non-equilibrium extension replaces maximization-on-states by production-on-processes: define extended thermodynamic systems as algebras of an operad of *constrained relaxation processes* (morphisms carry timescales and flux structure); recover Op(Ent) under the forgetful τ→0 functor. Concrete sub-questions: the right categorical home for balance-law systems (structured cospans of networks?); entropy production as a 2-morphism/laxator.
- **B2 — Two procedures theorem.** Coleman–Noll exploitation (quantify over arbitrary supplies) and Müller–Liu exploitation (Lagrange multipliers) as two constructions on a single categorical structure ("balance-law theory with entropy-principle object"); characterize the domains on which they coincide and where they diverge. Side benefit: a precise account of *why* RET's route yields symmetric hyperbolicity while the Truesdellian route does not (cf. recent results that heat-flux relaxation alone does not ensure hyperbolicity).
- **B3 — Formalization (later, opportunistic).** Type-theoretic statement of the balance-law framework and of T1–T4 in Lean/Coq; Lawvere's *Categories in Continuum Physics* (SDG, intensive/extensive duality) as the philosophical frame. Scope deliberately loose; depends on collaborator interest.

**Risks.** R3: categorical machinery may outrun the available theorems → keep B1/B2 tied to concrete Track-A objects. R4: B3 is resource-heavy → explicitly optional.

## 6. Track C — Computer Science × Economics: simulation and empirical estimation

**Disciplines.** Computer science (agent-based modeling, scientific computing, data analysis) applied to economics.

**Goal.** Discriminate hyperbolic from parabolic value-price dynamics in silico and in data.

- **C1 — ABM experiments.** Wright-style agent-based capitalism model; inject localized sectoral shocks; measure propagation (hyperbolic signature: affected region grows linearly in time with a visible front; parabolic: t^{1/2} scaling, no front); estimate the relaxation spectrum; test correlation decay (oscillatory telegraph-type vs. monotone diffusive). Connect the ABM→continuum limit to the telegraph→diffusion (Kac–Goldstein) rescaling. The ABM plays the *kinetic role*: it is the microscopic level whose hydrodynamic limit the continuum model approximates — Track C is the program's microfoundation, not merely its testbed (cf. Track E's E3).
- **C2 — Data.** OECD ICIO / WIOD tables; compute labor values, production prices, sectoral profit-rate dispersion following Cockshott–Cottrell; estimate effective relaxation times τ_J from the dynamics of dispersion; adjacent econometric precedent: Vaona's gravitation studies. Test the distributional predictions of Farjoun–Machover and Scharfenaker–Semieniuk (stationary dispersion, Laplace-like profit rates) against the driven-relaxation picture.
- **C3 — Synthesis.** Calibrate Track-A model parameters from C2; validate T2 spectra against C1 measurements.

**Risks.** R5: ABM noise may swamp front detection → ensemble design with sufficient replication; R6: data are annual and sector-aggregated → treat τ_J estimates as order-of-magnitude only.

## 7. Track D — Mathematics × Economics: the formal theory of value-price dynamics

**Disciplines.** Mathematics (dynamical systems, singular perturbation theory, spectral/network analysis, convex analysis) applied to economics (Marxian value theory, economic dynamics). This track is deliberately free of physics vocabulary: its results must stand as contributions to economic theory in economics' own language.

**Goal.** The rigorous mathematical economics of value-price dynamics: well-posedness and stability of the temporal value recursions as dynamical systems, the axiomatic structure of the transformation problem, and the "equilibrium as relaxation limit of disequilibrium dynamics" theorem as a general result in the theory of economic adjustment.

- **D1 — Well-posedness of temporal value recursions.** Existence, uniqueness, and continuous dependence on data for the TSSI difference-equation system (Kliman–McGlone 1999) and for Freeman's continuous-time system, treated as dynamical systems in their own right; a rigorous proof of the claimed exponential decay of errors from incorrect initial conditions. This answers Veneziani's "the dynamic framework is incomplete" in economics' own terms, without physics.
- **D2 — Axiomatic theory of the transformation problem.** Engage the axiomatic impossibility framing of Mohun & Veneziani (2017): state precisely which axioms yield inconsistency or redundancy, and prove the program's relocation claim — that the simultaneous system is the zero-adjustment-time limit of the temporal system — as a theorem about those axiom systems. Scope is bounded to the formal results, not the interpretive debate.
- **D3 — Equilibrium as a singular limit of disequilibrium dynamics.** The relaxation-limit theorem (T3) stated and proved as a contribution to the theory of economic adjustment: initial-layer analysis (post-shock mispricing regimes), the subcharacteristic condition as an admissibility criterion for equilibrium approximation, and the connection to the classical gravitation and tâtonnement literature (Steedman 1984; Flaschel & Semmler 1987; Duménil & Lévy 1987). Derived jointly with Track A's T3, written for an economics audience.
- **D4 — Network and spectral methods for input-output dynamics.** Perron–Frobenius structure of the IO matrix; spectra of the IO-Laplacian and their role in convergence rates; the SK-type coupling condition (T4) restated as a criterion on (A, κ); positioning against Duncan Foley's statistical-equilibrium program (Foley 1994), for which these dynamics supply the time-development.

**Methods.** Dynamical systems theory; difference and differential equations; singular perturbation theory; convex analysis and Lyapunov methods; network and spectral theory; close reading of the mathematical-economics literature (Sraffian theory, gravitation dynamics, statistical equilibrium, axiomatic value theory).

**Risks.** R7: D2 can become entangled in the interpretive debate — scope it to formal theorems only. R8: overlap with Track A — division of labor is that A derives results with physics tools and D restates them for economics and owns the axiomatic and adjustment-theory contributions; cross-referenced, not duplicated.

## 8. Track E — Physics × Computer Science: computational thermodynamics of value-price dynamics

**Disciplines.** Physics (extended thermodynamics) met by computer science (numerical analysis, scientific computing, machine learning). The algorithmic/numerical realization of Track A, and the data-driven answer to its closure problem.

**Goal.** Build the numerical and computational apparatus for the hyperbolic value-price system, and use computation as an instrument of theory discovery — most importantly, identifying the constitutive closure from data rather than postulating it.

**Status.** Cross-cutting infrastructure for Tracks A–D, not a standalone research agenda: every E sub-project is defined by the A–D problem it serves (E1 verifies A's T2/T3; E2 answers D's underdetermination problem; E3 quantifies C's kinetic role).

- **E1 — Numerical methods for relaxation systems on networks.** Solver design for the Cattaneo-type (telegraph-type) relaxation system on the input-output graph: Jin–Xin-style relaxation schemes, finite-volume methods on graphs, front/shock tracking for finite-speed value-price disturbances. Verifies Track A's T2 (front speeds) and T3 (relaxation limit) numerically.
- **E2 — Data-driven closure identification.** Learn the constitutive relation for intersectoral capital flux from agent-based microdata rather than assuming τ_J: data-driven discovery of closure models (sparse regression, neural closures, physics-informed where possible), including detecting *whether* relaxation structure exists at all. This is the computational answer to the underdetermination critique (see `program/critiques.md`, B2): closure becomes a falsifiable object. Discovery is *constrained*: learn within the admissible class (entropy principle, subcharacteristic condition), and validate forward on unseen regimes (new sector topologies, out-of-distribution shocks) rather than by residual fit alone.
- **E3 — ABM-to-continuum verification.** Numerical verification of the telegraph→diffusion (Kac–Goldstein) hydrodynamic limit: measure convergence rates of Wright-style ABMs (Track C) to the continuum model; quantify the regime in which the parabolic (simultaneist) description fails.

**Methods.** Relaxation schemes (Jin–Xin), finite-volume and front-tracking methods on graphs, sparse regression and physics-informed neural networks, multiscale numerical analysis, high-performance computing.

**Risks.** R9: learned closures may overfit and lack interpretability — favor structured/symbolic discovery with forward validation; R10: hydrodynamic-limit convergence may be slow at accessible ABM scales — report finite-size scaling honestly.

## 9. Track F — Mathematics × Computer Science: certified and executable mathematics

**Disciplines.** Mathematics met by computer science (proof assistants, type theory, functional programming). Computation as an instrument of mathematical rigor, and mathematics as the semantics of computation.

**Goal.** Machine-checked and executable versions of the program's mathematics: formalize its theorems, and implement its categorical/compositional structures as working software.

**Status.** Cross-cutting infrastructure for Tracks A–D, not a standalone research agenda: F1 formalizes D1; F2 implements B1; F3 certifies A's numerics and D's error bounds.

- **F1 — Proof-assistant formalization.** Lean 4 / Coq formalization of the balance-law axioms and of the discrete TSSI recursion theorems (Track D's D1): machine-checked existence, uniqueness, and exponential decay of initial-data errors. A bounded, feasible target; large-scale Lean formalizations of PDE analysis (De Giorgi–Nash–Moser; Leray–Hopf) show the route is now open.
- **F2 — Executable categorical models.** Implement the compositional framework of Track B in AlgebraicJulia (Catlab / AlgebraicDynamics / Decapodes): the extended-thermodynamics operad-algebra as working software that composes balance-law subsystems into economies. Makes the categorical foundations testable rather than decorative.
- **F3 — Verified numerics.** Certified error bounds for Track A's numerics and Track D's relaxation-limit estimates (T3): interval arithmetic and Taylor models inside a proof assistant (the CoqInterval/Flocq tradition), producing rigorous convergence certificates for the E1 solvers.

**Scope.** F does not promise full formalization of the continuum claims (relaxation limits, symmetric hyperbolicity, SK conditions). It certifies the discrete core (F1) and the concrete numerical bounds (F3) — the places where proof-assistant infrastructure is mature enough to deliver.

**Methods.** Lean 4/mathlib and Coq; applied category theory with computable implementations (C-sets, operad algebras); rigorous/verified numerical computation.

**Risks.** R11: formalization is time-intensive — scope F1 to the discrete recursion first (the simplest target); R12: AlgebraicJulia tooling is young — treat F2 as proof-of-concept rather than production infrastructure.

## 10. Phasing, dependencies, publication strategy

- **Year 1:** A1 (Master's thesis). D1 (well-posedness of the discrete TSSI recursion) begins — low-cost, mostly literature. E1 (solver design) begins; C1 prototype in parallel if capacity allows.
- **Year 2:** A2 (entropy problem); D2–D3 (axiomatic transformation theory; the relaxation-limit theorem in economics idiom); E2 (data-driven closure identification, with C1's ABM as the data source); F1 (formalization of the discrete recursion) begins; B1 begins; C1 full experiments. Papers: T1–T4 (applied-math venue, e.g., *Quarterly of Applied Mathematics* / *JMAA*); economics-facing version of the relaxation-limit result (*Cambridge Journal of Economics* / *Metroeconomica*).
- **Year 3:** A3; D4 (network/spectral methods, statistical-equilibrium positioning); E3 (ABM-to-continuum verification); F2 (executable categorical models); B2; C2. Papers: stability criterion + gravitation reinterpretation; closure-identification paper (*Journal of Computational Physics*-class); axiomatic transformation paper (*Journal of Mathematical Economics* / *Metroeconomica*); B1 (*Compositionality*); econophysics version (*Physica A* / *JEDC*).
- **Year 4+:** integration; F3 (verified numerics) and further formalization trails; program-level synthesis (the "two paradoxes" essay for a general scientific audience).

Dependencies: A1 → A2 → A3; A1 and D3 share the relaxation-limit theorem (joint derivation, two audiences); D1 is nearly independent of A; E1 supports A1's numerics; E2 depends on C1's data and feeds A2 (closure) and B2 (underdetermination); F1 formalizes D1; B1/B2 depend only on the literature and A1's model; C2 is independent.

**Scope discipline.** The Master's thesis is deliberately minimal (M1); Tracks B–F are sequenced behind A1, and E/F are cross-cutting infrastructure for A–D, not standalone agendas (§8–§9). Ecological macroeconomics is named only as a future application domain, not as a track. This document is a map, not a promise.

## 11. Master's thesis decision point

Six candidate six-month sub-problems, to be selected after review of this document. M1–M3 are the Track A/B candidates from the original design; M4 arose with Track D; M5–M6 arise with Tracks E/F.

| Candidate | Content | Feasibility | Novelty | Program fit |
|---|---|---|---|---|
| **M1 (default)** Hyperbolic TSSI model | Track A phase 1 (A1): Cattaneo extension, T1–T3 rigorously in the small, T4 for the linear/network case, numerics | High — mostly linear theory + one quasilinear existence result | Solid first application of RET outside physics; first finite-speed value model | Direct: it *is* Track A Phase 1 |
| **M2** Entropy-first | Attack H2 for an existing temporal/cross-dual model: construct or obstruct a convex entropy extension | Medium-low for 6 months — theorem may not exist | High if it succeeds | Skips ahead to A2; riskier |
| **M3** Category-theory warm-up | Track B restricted (B1): categorical reformulation of one exploitation procedure | Medium — well-defined but hard to assess for an applied-math committee | High | Starts Track B; A1 deferred |
| **M4** TSSI recursion analysis | Track D phase 1 (D1): existence, uniqueness, and exponential decay of initial-data errors for the discrete temporal value recursion | High — self-contained, mostly classical analysis | Moderate (rigor over new structure) | Enters via the economics-math pair; the safe alternative to M1 |
| **M5** Relaxation-system numerics | Track E phase 1 (E1): numerical schemes for the Cattaneo-type system on the IO network; front tracking; numerical verification of the τ→0 limit | High — standard numerics applied to the new model | Moderate | Builds the solver infrastructure Track A needs; a computer-science-flavored option |
| **M6** Formalized TSSI recursion | Track F phase 1 (F1): machine-checked well-posedness / exponential decay for the discrete recursion in Lean 4 | Medium — proof-assistant fluency required | High (certified result) | Requires/acquires formal-methods skills; strongest for a CS-adjacent committee |

Recommendation: **M1**, with the entropy question stated as the open problem it leaves behind — the natural Master's-to-PhD bridge. **M4** is the low-risk alternative (classical analysis, no new machinery); **M5** the numerical/computational alternative; **M6** the highest-novelty, highest-skill-bar alternative.

## 12. References

See `program/references.bib` (all entries verified with DOIs or stable URLs, organized by track). Anchor works: Cattaneo (1948); Müller & Ruggeri (1998); Ruggeri & Strumia (1981); Chen, Levermore & Liu (1994); Hanouzet & Natalini (2003); Ruggeri & Serre (2004); Bianchini et al. (2007); Kliman & McGlone (1999); Freeman (1996); Veneziani (2005); Mohun & Veneziani (2009, 2017); Bortkiewicz (1907); Sraffa (1960); Steedman (1977, 1984); Flaschel & Semmler (1987); Duménil & Lévy (1987); Farjoun & Machover (1983); Cottrell et al. (2009); Wright (2005); Cockshott & Cottrell (1998); Cockshott (2016); Foley (1994); Scharfenaker & Semieniuk (2017); Burger et al. (2013); Ratanov (2007); Jin & Xin (1995); Raissi et al. (2019); Pan & Duraisamy (2018); Gupta & Lermusiaux (2021); Bar-Sinai et al. (2019); Brennan & Venturi (2018); Libkind et al. (2022); Morris et al. (2024); Armstrong & Kuusi (2025); Martin-Dorel & Melquiond (2016); van Doorn & Macbeth (2024); Baez, Lynch & Moeller (2023); Lawvere & Schanuel (1986); Coleman & Noll (1963); Coleman (1964); Truesdell (1984); Müller (1967); Liu (1972).
