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

The program has three tracks: **A**, applied analysis (build and analyze the hyperbolic value-price system); **B**, foundations (category/type-theoretic axiomatization of extended thermodynamics, extending the analogy to the Truesdellian "rational thermodynamics" tradition); **C**, computational and empirical validation (agent-based simulation and input-output data). Track A Phase 1 doubles as a six-month Master's thesis in applied mathematics.

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

Farjoun & Machover (1983) rebuilt political economy probabilistically; Cottrell, Cockshott, Michaelson, Wright & Yakovenko (2009) systematized "classical econophysics" with agent-based models in which value relations are emergent; Wright (2005) reproduces the empirical distribution of profit rates (dispersed, gamma-like — not equalized). Two precedents show finite-speed/relaxation methods already accepted in mathematical economics: telegraph-process option pricing (Ratanov 2007), motivated explicitly by the infinite propagation speed of Brownian models; and the Boltzmann-type price-formation model of Burger, Caffarelli, Markowich & Wolfram (2013), proved to converge to the parabolic Lasry–Lions equation as the transaction rate diverges — a rigorous relaxation limit in economics.

**Gap G4.** Econophysics has no continuum (field) theory of value-price dynamics; the value-theory literature has no finite-speed models. The persistent empirical *dispersion* of profit rates — impossible under instantaneous equalization — is the natural signature of a relaxational system under continuous forcing.

### 2.5 Gap summary

| # | Gap | Track that addresses it |
|---|---|---|
| G1 | TSSI lacks closure/well-posedness/stability (Veneziani critique) | A |
| G2 | No non-physical application of RET; no categorical axiomatization of non-equilibrium thermodynamics | A, B |
| G3 | No unifying criterion for gravitation convergence | A |
| G4 | No continuum theory in classical econophysics; unexplained profit-rate dispersion | A, C |

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

The analogy extends one level deeper on the foundations side: just as value theory has rival "rationalizations" (New Interpretation vs. TSSI), non-equilibrium thermodynamics has rival rational reconstructions — Truesdell–Coleman–Noll rational thermodynamics (memory functionals; Clausius–Duhem as constraint on constitutive relations via arbitrary supplies) versus the Müller–Liu–Ruggeri line (extended state space; entropy principle via Lagrange multipliers). Track B axiomatizes both within one categorical framework.

## 4. Track A — Applied analysis

**Goal.** Construct and analyze a hyperbolic balance-law model of temporal value-price dynamics; deliver the well-posedness, stability, and relaxation-limit theory that TSSI lacks.

**A1 (Phase 1; six months; candidate Master's thesis).** Minimal model: n-sector circulating-capital economy in continuous time (Freeman 1996 base), state u = (p, K, J) with capital-balance continuity equations on the input-output network and Cattaneo closure τ_J dJ_ij/dt + J_ij = κ_ij(r_j − r_i). Deliverables (theorems T1–T4):

- **T1, well-posedness:** local existence/uniqueness for the quasilinear system; global existence near the production-price equilibrium for small data.
- **T2, linear analysis:** spectral structure of the linearization; finite front speeds; semigroup convergence to the parabolic gravitation semigroup as τ_J → 0⁺.
- **T3, relaxation limit:** u^τ → u⁰ with error estimates; the limit system is the simultaneous-closure dynamics whose rest point is the Sraffian fixed point. *This makes precise the sense in which simultaneism is the equilibrium approximation of temporal determination.*
- **T4, stability criterion:** an SK-type coupling condition on (A, κ) equivalent to asymptotic convergence to the equalized-profit-rate state; check that Flaschel–Semmler's stabilizing modifications enforce it and that Nikaido/Cockshott non-convergence cases violate it.
- Small-scale numerics: finite-speed propagation of a sectoral profit shock, contrasted with diffusive spread.

**A2 (Phase 2).** The entropy problem: construct a convex entropy extension for the nonlinear system (candidates: relative-entropy functionals on price-value deviations; distributional entropy à la Farjoun–Machover), or prove obstructions and pass to EIT-style generalized entropies. Success gives symmetric-hyperbolic form (Ruggeri–Strumia) and a genuine H-theorem for value dynamics; the economic interpretation of entropy production (decay of profit-rate differentials as dissipation of arbitrage) is itself a paper.

**A3 (Phase 3).** Full TSSI closure: endogenous MELT dynamics, fixed capital, joint production; stochastic forcing (persistent dispersion of profit rates as the stationary state of a driven relaxational system — contact with Farjoun–Machover's gamma distribution).

**Methods.** Semigroup theory and singular perturbation for ODE/network systems; symmetric-hyperbolic and entropy methods for the PDE/network extension; standard tools: Chen–Levermore–Liu, Hanouzet–Natalini, Ruggeri–Serre, Boillat–Ruggeri subcharacteristic theory.

**Risks.** R1: no convex entropy exists for natural closures → fall back to Lyapunov-only stability (T4 does not require symmetric hyperbolicity) and EIT-style frameworks. R2: T4's condition may only be sufficient, not characterizing → scope the claim accordingly.

## 5. Track B — Foundations

**Goal.** A category/type-theoretic axiomatization of extended thermodynamics, extending the program's central analogy to the foundations of thermodynamics themselves; the economic application doubles as the test case.

- **B1 — Compositional non-equilibrium thermodynamics.** Baez–Lynch–Moeller (2023) axiomatize equilibrium thermostatics as algebras of an operad of convex relations, with entropy maximization as the composition rule. The non-equilibrium extension replaces maximization-on-states by production-on-processes: define extended thermodynamic systems as algebras of an operad of *constrained relaxation processes* (morphisms carry timescales and flux structure); recover Op(Ent) under the forgetful τ→0 functor. Concrete sub-questions: the right categorical home for balance-law systems (structured cospans of networks?); entropy production as a 2-morphism/laxator.
- **B2 — Two procedures theorem.** Coleman–Noll exploitation (quantify over arbitrary supplies) and Müller–Liu exploitation (Lagrange multipliers) as two constructions on a single categorical structure ("balance-law theory with entropy-principle object"); characterize the domains on which they coincide and where they diverge. Side benefit: a precise account of *why* RET's route yields symmetric hyperbolicity while the Truesdellian route does not (cf. recent results that heat-flux relaxation alone does not ensure hyperbolicity).
- **B3 — Formalization (later, opportunistic).** Type-theoretic statement of the balance-law framework and of T1–T4 in Lean/Coq; Lawvere's *Categories in Continuum Physics* (SDG, intensive/extensive duality) as the philosophical frame. Scope deliberately loose; depends on collaborator interest.

**Risks.** R3: categorical machinery may outrun the available theorems → keep B1/B2 tied to concrete Track-A objects. R4: B3 is resource-heavy → explicitly optional.

## 6. Track C — Computational and empirical

**Goal.** Discriminate hyperbolic from parabolic value-price dynamics in silico and in data.

- **C1 — ABM experiments.** Wright-style agent-based capitalism model; inject localized sectoral shocks; measure propagation (hyperbolic signature: affected region grows linearly in time with a visible front; parabolic: t^{1/2} scaling, no front); estimate the relaxation spectrum; test correlation decay (oscillatory telegraph-type vs. monotone diffusive). Connect the ABM→continuum limit to the telegraph→diffusion (Kac–Goldstein) rescaling.
- **C2 — Data.** OECD ICIO / WIOD tables; compute labor values, production prices, sectoral profit-rate dispersion following Cockshott–Cottrell; estimate effective relaxation times τ_J from the dynamics of dispersion; adjacent econometric precedent: Vaona's gravitation studies.
- **C3 — Synthesis.** Calibrate Track-A model parameters from C2; validate T2 spectra against C1 measurements.

**Risks.** R5: ABM noise may swamp front detection → ensemble design with sufficient replication; R6: data are annual and sector-aggregated → treat τ_J estimates as order-of-magnitude only.

## 7. Phasing, dependencies, publication strategy

- **Year 1:** A1 (Master's thesis). C1 prototype in parallel if capacity allows.
- **Year 2:** A2 (entropy problem); B1 begins; C1 full experiments. Papers: T1–T4 (applied-math venue, e.g., *Quarterly of Applied Mathematics* / *JMAA*); econ-facing version of the relaxation-limit result (*Cambridge Journal of Economics* / *Metroeconomica*).
- **Year 3:** A3; B2; C2. Papers: stability criterion + gravitation reinterpretation; B1 (*Compositionality*); econophysics version (*Physica A* / *JEDC*).
- **Year 4+:** integration; B3 optional; program-level synthesis (the "two paradoxes" essay for a general scientific audience).

Dependencies: A1 → A2 → A3; C1 informs A3 parameters; B1/B2 depend only on the literature and A1's model; C2 is independent.

## 8. Master's thesis decision point

Three candidate six-month sub-problems, to be selected after review of this document:

| Candidate | Content | Feasibility | Novelty | Program fit |
|---|---|---|---|---|
| **M1 (default)** Hyperbolic TSSI model | A1 as above: Cattaneo extension, T1–T3 rigorously in the small, T4 for the linear/network case, numerics | High — mostly linear theory + one quasilinear existence result | Solid first application of RET outside physics; first finite-speed value model | Direct: it *is* Track A Phase 1 |
| **M2** Entropy-first | Attack H2 for an existing temporal/cross-dual model: construct or obstruct a convex entropy extension | Medium-low for 6 months — theorem may not exist | High if it succeeds | Skips ahead to A2; riskier |
| **M3** Category-theory warm-up | B1 restricted: categorical reformulation of one exploitation procedure | Medium — well-defined but hard to assess for an applied-math committee | High | Starts Track B; A1 deferred |

Recommendation: **M1**, with the entropy question stated as the open problem it leaves behind — the natural Master's-to-PhD bridge.

## 9. References

See `program/references.bib` (all entries verified with DOIs or stable URLs). Anchor works: Cattaneo (1948); Müller & Ruggeri (1998); Ruggeri & Strumia (1981); Chen, Levermore & Liu (1994); Hanouzet & Natalini (2003); Ruggeri & Serre (2004); Bianchini et al. (2007); Kliman & McGlone (1999); Freeman (1996); Veneziani (2005); Mohun & Veneziani (2009); Bortkiewicz (1907); Sraffa (1960); Steedman (1977, 1984); Flaschel & Semmler (1987); Duménil & Lévy (1987); Farjoun & Machover (1983); Cottrell et al. (2009); Wright (2005); Cockshott & Cottrell (1998); Cockshott (2016); Burger et al. (2013); Ratanov (2007); Baez, Lynch & Moeller (2023); Lawvere & Schanuel (1986); Coleman & Noll (1963); Coleman (1964); Truesdell (1984); Müller (1967); Liu (1972).
