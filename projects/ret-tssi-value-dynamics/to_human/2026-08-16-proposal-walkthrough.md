# Finite-Speed Value: A Walkthrough

*An accessible explainer to the RET × TSSI research program — "Finite-Speed Value: A Research Program in Marxian Econophysics"*

This document explains the program to a reader who knows none of its specialties. It assumes no thermodynamics and no value theory. Because your home field is statistics, the exposition leans on statistical examples throughout — with E.T. Jaynes' maximum-entropy program as the recurring guide.

The authoritative, technical version is `program/research-program.md`. This walkthrough is the readable companion; each discipline section can be lifted out as a standalone one-pager.

---

## 1. The whole program in five minutes

**Two controversies, one shape.** In 19th-century physics, the theory of heat spread said temperature differences cause heat to flow *instantly* everywhere. That is obviously wrong physically, but worse, it is wrong *mathematically*: the equations predict that a poke at one end of a rod is felt at the other end immediately. In 19th-century economics, the theory of value formation said prices are determined *instantly* as a single algebraic snapshot — input prices equal output prices by construction. That produced the century-long "transformation problem," a dispute over whether Marx's labor theory of value is internally consistent.

**The fix in physics.** Carlo Cattaneo (1948) resolved the heat paradox by letting the heat *flow* itself take time to respond — give it a small but nonzero relaxation time. The resulting equations are hyperbolic (telegraph-like): disturbances propagate at a finite speed. This single move grew into a systematic framework, **rational extended thermodynamics (RET)**, with a complete mathematical theory of existence, uniqueness, and stability — and a rigorous sense in which the old, paradoxical theory is the *limit* of the new one as the relaxation time shrinks to zero.

**The fix in economics.** The **temporal single-system interpretation (TSSI)** (Kliman–McGlone 1999; Freeman 1996) resolved the transformation problem the same way *conceptually*: instead of an algebraic snapshot, determination is sequential in historical time — inputs at time *t*, outputs at *t+1*. Values and prices form one interdependent system evolving forward.

**The thesis.** These are not two similar stories; they are the *same* story in a common mathematical framework. This program claims a **formal correspondence**:

- value–price dynamics can be written as a system of balance laws with a relaxation-time closure (capital fluxes respond to profit-rate differentials *with a lag*), exactly matching Cattaneo's structure;
- the simultaneist (instantaneous) theory is recovered as the **τ → 0 singular limit** of the temporal theory — which explains both why simultaneism works near equilibrium and why it fails away from it;
- the **entropy methods** of modern hyperbolic theory supply the stability theory economics' own "gravitation" literature never found — a unifying criterion for when market prices converge to prices of production.

**In one statistical sentence:** classical economics equilibrates prices the way overdamped Langevin dynamics (or Fourier's law) diffuses instantaneously; this program writes the underdamped, finite-speed version and proves that the instant one is its singular limit.

---

## 2. The seed: two paradoxes of simultaneity

### 2.1 The heat paradox (physics)

Fourier's law of heat conduction says the heat flux *q* (heat flowing per unit area per second) is proportional to the temperature gradient: *q = −κ∇T*. Combined with energy conservation, this yields the parabolic heat equation — the equation that diffuses a temperature bump into a bell curve over time. Its fundamental solution has **unbounded support for any t > 0**: a point disturbance is felt everywhere instantly (though faintly). This "infinite speed of propagation" is the heat paradox.

The defect is the **instantaneous closure**: the flux is slaved algebraically to the gradient at the same instant. Cattaneo's remedy: promote the flux to its own state variable with its own dynamics,

  τ ∂q/∂t + q = −κ∇T.

The closed system is the *telegraph equation* — hyperbolic, with a finite front speed. Parabolic (Fourier) theory is the singular limit τ → 0.

### 2.2 The transformation problem (economics)

Marx argued that commodities exchange at prices proportional to the labor embodied in them (values), and that profit comes from unpaid labor. But he also knew prices visibly deviate from values. Bortkiewicz (1907) and later Sraffa (1960) formalized the "transformation" of values into prices under the assumption of **simultaneous determination**: input prices equal output prices *by construction*, so all magnitudes are determined at one logical instant by an algebraic fixed point. On that reading, Marx's two aggregate equalities (total price = total value; total profit = total surplus value) fail, and the labor theory of value looks inconsistent or redundant.

The TSSI response: determination is *temporal*. Inputs enter at prices of period *t*; outputs emerge at prices of *t+1*; values and prices form a single system evolving forward in historical time. Under this reading the two aggregate equalities hold, and Marx's falling-rate-of-profit argument survives the famous "Okishio theorem" that (under simultaneity) technical change cannot lower the profit rate.

### 2.3 What the two paradoxes share

In both cases: (i) an **instantaneous closure** creates a pathology (infinite speed in physics; alleged inconsistency/redundancy in economics); (ii) the resolution **temporalizes** the closure by giving the slaved quantity its own dynamics; (iii) the orthodox theory is recovered as the limit in which the new dynamical timescale vanishes.

The program's claim is that this homology is **formal** — expressible in a single mathematical framework (hyperbolic balance laws with relaxation) — and that the framework's theorems then transfer. Not a metaphor: an isomorphism of structure that lets you import proofs.

---

## 3. The core move: a formal correspondence

The program's heart is a dictionary between the two fields, summed up in two tables (authoritative version in `program/research-program.md` §3; here in plain language):

| Classical thermodynamics | Simultaneist value theory |
|---|---|
| Fourier's law: flux slaved to gradient, instantly | Input prices = output prices; capital flows slaved to current profit differentials |
| Parabolic equations; infinite propagation speed | Algebraic fixed point; "instantaneous equilibration" |
| Heat paradox | Inconsistency / redundancy charges (Okishio-type results) |
| Valid near equilibrium, smooth fields | Valid (if at all) near stationary technical conditions |

| Rational extended thermodynamics | TSSI, formalized (this program) |
|---|---|
| Fluxes promoted to state variables: τ ∂q/∂t + q = −κ∇T | Capital fluxes promoted: τ_J dJ/dt + J = κ·(profit-rate differentials) |
| Hyperbolic laws; finite characteristic speeds | Sequential determination; finite-speed propagation of shocks on the input–output network |
| Convex entropy extension → well-posed, stable | Convex functional on deviations from production-price equilibrium (to be constructed) |
| Parabolic theory = τ→0 singular limit | Simultaneist system = τ_J→0 singular limit |
| Shizuta–Kawashima (SK) condition ⇔ decay to equilibrium | Coupling condition on capital mobility ⇔ gravitation convergence |
| Entropy principle selects admissible constitutive relations | Closure selection answers the underdetermination charge |

**The single new equation.** The whole applied core is the capital-flux closure:

  τ_J dJ/dt + J = κ·(r_j − r_i)

(capital reallocation J between sectors responds to profit-rate differentials *with a lag* τ_J — lags from organization, credit, and fixed-capital turnover). At τ_J = 0 you recover the classical cross-dual adjustment rule used by every gravitation model in the literature — so the Cattaneo extension **nests the entire gravitation literature as its zero-relaxation-time special case**. That one fact does a lot of work: it means the program generalizes rather than replaces existing economics.

**What the correspondence buys, concretely:**

1. **Well-posedness** (the Veneziani critique answered): TSSI's equations don't pin down their own trajectories; treating them as a system of balance laws with an entropy-restricted closure gives existence, uniqueness, and continuous dependence on data.
2. **A relaxation-limit theorem**: the simultaneist system is the τ→0 singular limit of the temporal system, with O(τ) error bounds on compact time intervals. Simultaneism is *the equilibrium approximation of temporal determination* — made precise and bounded.
3. **A unifying stability criterion**: a Shizuta–Kawashima-type coupling condition on (technology matrix, mobility coefficients) is *equivalent* to convergence to the equalized-profit-rate state. The classical literature's mixed results (some models converge, some don't) become special cases of one condition.

**Convention on "entropy".** Throughout, "entropy" means the *mathematical* object — a convex (Lyapunov-type) structure that makes the structural theorems work — not thermodynamic entropy. No "second law of economics" is claimed. (This is stated explicitly in the program doc §3 and again at each point of use.)

---

## 4. The statistical compass: Jaynes as the guide

Your background makes the program *easier* to see than it is from any single discipline, because the deepest structural fact of the program is a **selection problem** — and selection problems are what maximum-entropy inference is about.

### 4.1 Jaynes' MaxEnt in one paragraph

Jaynes (1957) recast statistical mechanics as *statistical inference*: the exact microscopic state is unobserved; what we know is a set of constraints (expectations of observables — energy, particle number, ...). Among all distributions consistent with the constraints, the least-biased one is the maximizer of Shannon entropy; the solution is the **exponential family** p(x) ∝ exp(−Σλᵢ fᵢ(x)), with λᵢ the **Lagrange multipliers** of the constrained optimization. The entropy here is *epistemic* — a measure of the uniqueness/uncertainty of the inference, not an intrinsic property of the system. What makes the construction predictive is that it turns an **underdetermined** problem (infinitely many distributions fit the constraints) into a **uniquely determined** one, by a principled selection rule.

### 4.2 Four statistical mirrors

These are the places where the program becomes legible in statistical language. (They are pedagogical bridges for this walkthrough, not claims in the program document.)

**Mirror 1 — Underdetermination ↔ closure selection.** Mohun–Veneziani's charge that TSSI is *underdetermined* — its equations don't select their own trajectories — is, formally, a **closure problem**: the same defect as a moment hierarchy truncated without a closing relation. Jaynes faced the same shape: infinitely many distributions consistent with the constraints. His answer was a *selection rule* (MaxEnt). RET's answer to underdetermined constitutive relations is an *entropy principle* implemented via **Liu's exploitation procedure, which uses Lagrange multipliers** — literally the same machinery as Jaynes. The underdetermination charge in value theory is answered by the entropy-principle selection rule of RET. This is the program's strongest claim to being more than metaphor: **the statistical method you already know is the mathematical bridge.**

**Mirror 2 — State/main-field duality ↔ mean/natural parameter duality.** In an exponential family, the mean parameter μ and the natural parameter λ are dual to each other through the strictly convex log-normalizer: μ = ∇ log Z(λ). In RET, the state variable u and the "main field" u′ (the Lagrange-multiplier variables of the entropy principle) are dual the same way, u = ∂h/∂u′ for the concave entropy density h. Convexity is the single engine in both cases: the convexity of the log-partition function is why exponential families are tractable, and the concavity of the entropy is why entropy-selected closures yield **symmetric-hyperbolic systems** (Ruggeri–Strumia 1981) with well-posed Cauchy problems. The statistician's "of course it's the log-partition function" is the physicist's "of course it's the convex entropy extension." One fact, two vocabularies.

**Mirror 3 — Cattaneo ↔ underdamped Langevin.** The single most useful analogy for you:

- **Underdamped Langevin**: dX = V dt, m dV = −γV dt − ∇U(X) dt + σ dW — a second-order system with momentum. Disturbances propagate at finite speed; dynamics are inertial/oscillatory.
- **Overdamped Langevin** (the m/γ → 0 limit): velocity is slaved to the force instantaneously; X follows a first-order diffusion — a Gaussian kernel with unbounded support, i.e., **infinite propagation speed**.
- Underdamped is to overdamped as **Cattaneo/RET is to Fourier/parabolic** — and as **temporal (TSSI) determination is to simultaneist determination**.

The economic dictionary: capital flux J ↔ momentum V; profit-rate differentials ↔ force −∇U; production-price equilibrium ↔ the target U. The gravitation question ("do prices converge to prices of production?") is, in the linear regime, literally a **mixing / spectral-gap question** for the linearized generator — and the SK coupling condition is the spectral-gap criterion. Statisticians know this regime intimately from MCMC: Hamiltonian Monte Carlo (underdamped, momentum) vs. MALA (overdamped). The "finite front speed" of the telegraph process is the momentum persistence that makes inertial samplers explore differently.

**Mirror 4 — Entropy production ↔ KL divergence.** Along any Langevin dynamics, the relative entropy (KL divergence) to the stationary distribution decays monotonically — the "H-theorem" of Markov processes — and the rate is controlled by a Poincaré/spectral-gap inequality. In RET, the convex entropy (entropy plus a compensation term) is the **Lyapunov function** proving decay to equilibrium, under the SK coupling condition. The program's candidate "entropy" for value dynamics is exactly a **relative-entropy/KL-type functional** on deviations from production-price equilibrium; "entropy production" then reads economically as *dissipation of profit-rate differentials — destruction of arbitrage opportunities*. Same mathematics as the KL-decay inequality; new interpretation.

### 4.3 Statistical equilibrium is already Jaynesian

Two empirical anchors in the economics literature are direct statistical objects:

- **Foley (1994)** built markets as **maximum-entropy equilibrium** — literally Jaynes applied to exchange. This program does not dispute the equilibrium; it supplies the **time-development** — the dynamics whose stationary behavior Foley's static ensembles describe.
- **Scharfenaker & Semieniuk (2017)** document *stationary, Laplace-distributed* (not equalized) firm-level profit rates; Wright (2005) likewise finds dispersed, gamma-like profit rates in agent-based models. The Laplace law is itself a MaxEnt distribution (maximizing entropy given a constraint on mean absolute deviation — the robust analog of the Gaussian). So the empirical dispersion is a *Jaynesian signature*; this program explains **why the dispersion persists** rather than decaying: a relaxational system under continuous forcing reaches a **non-equilibrium steady state** with persistent variance, not equalization. "Instantaneous equalization" of profit rates — the classical assumption — is the overdamped/parabolic limit that, in data, never holds.

### 4.4 What the compass does and does not claim

It claims: the closure-selection structure, the duality, the limit structure, and the Lyapunov/stability structure are the *same mathematics* statistics uses for exponential families, diffusion approximation, and Markov-chain convergence. It does not claim: that economic agents maximize entropy, that "entropy" is physically real in markets, or any operational thermodynamics of value. The statistical compass is a Rosetta stone for the mathematics, not a theory of economic behavior.

---

## 5. The physics explainer

**What thermodynamics is about.** Thermodynamics is the science of *macroscopic* description: you ignore molecules and track a few fields (temperature, density, ...). The "closure problem" is that conservation laws (energy, mass) are not enough — you also need to say how flows respond (the *constitutive relation*), and that choice is not forced by the conservation laws alone.

**The classical theory and its defect.** Classical irreversible thermodynamics closes energy balance with Fourier's law (flux slaved to gradient) — giving parabolic equations with infinite propagation speed. It works near equilibrium and fails at sharp gradients/fast transients, where it even gives *negative* entropy production. The physical fix has two traditions:

- **Truesdell–Coleman–Noll "rational thermodynamics"**: keep the classical state space; make constitutive relations obey the Clausius–Duhem inequality.
- **Müller–Liu–Ruggeri "extended thermodynamics" (RET)**: *enlarge* the state space — promote the fluxes themselves to state variables with their own evolution equations — and restrict the enlarged constitutive relations by an **entropy principle** (Müller 1967; Liu 1972), where the entropy balance's "extra entropy flux" is determined by the Lagrange-multiplier (Liu) exploitation.

**The RET toolbox** (this is what the program imports):

1. **Balance laws** ∂u/∂t + Σ∂F_k/∂x_k = G(u) — conservation plus production terms.
2. **Constitutive theory** — admissible F, G selected by the entropy principle.
3. **Entropy extension** — a scalar balance law with nonnegative production, entropy concave in the state.
4. **Ruggeri–Strumia (1981)** — a convex entropy extension ⇔ the system is *symmetric hyperbolic* in main-field variables ⇒ finite characteristic speeds + well-posed Cauchy problem.
5. **Relaxation limits (Chen–Levermore–Liu 1994)** — stiff relaxation drives the system onto the equilibrium manifold; the reduced dynamics is parabolic; the *subcharacteristic condition* governs when the limit is admissible.
6. **Stability (Hanouzet–Natalini 2003; Ruggeri–Serre 2004; Bianchini et al. 2007)** — entropy dissipation + the **Shizuta–Kawashima (SK) coupling condition** give global existence and decay to equilibrium; the entropy (plus compensation term) is the Lyapunov function.

**The statistics bridge.** RET is, historically and formally, a *moment-closure* scheme: starting from the Boltzmann kinetic equation, keep the first few moments as state variables (density; then density + flux; ...), and **close the hierarchy by entropy maximization** on the truncated distribution (Levermore's entropy-based moment closures). Cattaneo's equation is the simplest such closure (one extra moment). So the entire RET program is, in statistical language: *a Jaynesian closure of a moment hierarchy, with the log-partition function's convexity guaranteeing the good properties*. If you've internalized MaxEnt, you've internalized the design principle of RET.

**What physics contributes here.** A complete, proven methodology for exactly the gap TSSI has: balance laws without constitutive theory, without well-posedness, without stability. Plus a family of theorems ready to be specialized.

**What's novel for physics.** RET has never been applied outside physics and engineering. Moreover its own foundations are un-axiomatized in modern (categorical) terms — the only categorical thermodynamics on record are *equilibrium* thermostatics (Baez–Lynch–Moeller 2023) and the *Truesdellian* continuum theory (Lawvere 1986). Extending the foundations to non-equilibrium extended thermodynamics is itself an open physics-mathematics problem (Track B).

**Fallacy to watch.** "Entropy" in this program is a Lyapunov structure, not thermodynamic entropy; the correspondence does not assert that markets have a temperature, obey a second law, or are Carnot engines. Any reading that attributes operational thermodynamics to value dynamics is a misreading.

---

## 6. The mathematics explainer

**The questions the math answers.** Three questions, each with a sharp mathematical shape:

1. **Well-posedness.** Does the system have a unique solution, depending continuously on its data? (For TSSI as literally written, the answer is *no* — hence the underdetermination charge. For the balance-law system with a Cattaneo closure, the answer becomes *yes*.)
2. **The limit.** What happens to solutions as the relaxation time τ → 0? The limit system is the simultaneist (instantaneous) dynamics; the question is *in what sense* and *with what error* the temporal system converges to it.
3. **Stability.** Do small perturbations decay to the production-price equilibrium — and under what condition on the data (technology matrix A, mobility coefficients κ)?

**The tools.**

- **Convex analysis and Lyapunov methods** — the engine. Concave entropy / convex Lyapunov functions drive the stability theorems; convex duality (state ↔ main field) is the mechanism behind symmetric hyperbolicity.
- **Semigroup theory** — evolution operators for linear and quasilinear systems; convergence of semigroups (Trotter–Kato) formalizes "the parabolic system is the τ→0 limit of the hyperbolic one."
- **Singular perturbation theory** — the τ→0 limit is *singular*: it changes the type of the system (second-order → first-order), so it is not uniformly valid in time. This is where the subtlety lives (below).
- **Network and spectral theory** — the input–output matrix gives the network Laplacian; Perron–Frobenius theory (the Sraffian eigenvalue), the IO-Laplacian spectrum, and its role in convergence rates.

**The four theorems (T1–T4) in plain language.**

- **T1 — Well-posedness.** Local existence and uniqueness for the quasilinear system; global existence near equilibrium for small data.
- **T2 — Linear analysis.** The spectral structure of the linearization; finite front speeds; the semigroup of the hyperbolic system converges to the parabolic gravitation semigroup as τ → 0⁺.
- **T3 — Relaxation limit (singular).** u^τ → u⁰ with O(τ) error on compact time intervals; u⁰ solves the simultaneous-closure dynamics whose rest state is the Sraffian fixed point. **This makes precise — and bounds — the sense in which simultaneism is the equilibrium approximation of temporal determination.**
- **T4 — Stability criterion.** An SK-type coupling condition on (A, κ) is *equivalent* to asymptotic convergence to the equalized-profit-rate state; the classical literature's positive results (Flaschel–Semmler's stabilizing modifications) *enforce* the condition, and its negative results (Nikaido, Cockshott non-convergence cases) *violate* it.

**The singular-limit subtlety (the one to internalize).** In perturbation theory, the limit τ→0 of a two-timescale system is singular: for times comparable to τ (the **initial layer**) the reduced (instantaneous) description is badly wrong, and the boundary layer is an essential part of the answer, not an error. Statistics knows this: it is the "fast variables collapse instantly" fallacy in diffusion approximation — the overdamped limit of underdamped Langevin misdescribes the ballistic short-time behavior. The program's economic reading: **the post-shock transient during which simultaneous closure misprices is itself an economic result** — a boundary layer in which the instantaneous theory fails by construction. This is exactly where simultaneism's pathologies live, and exactly where a finite-speed theory is not merely nicer but *necessary*.

**What's novel.** Economics' gravitation literature has only case-by-case results ("this model converges, that one doesn't"). A single necessary-and-sufficient coupling condition on the underlying data is a genuinely new object for that literature. On the math side, the relaxation-limit theorem as a theorem *about economic adjustment* (equilibrium as singular limit of disequilibrium dynamics) is new to mathematical economics; the closest precedent, the Burger–Caffarelli–Markowich–Wolfram Boltzmann price-formation model converging to the Lasry–Lions equation, is a rigorous relaxation limit *in* economics — but no one has run the analogue for value–price dynamics.

**Fallacy to watch.** The singular limit is *not* uniformly valid in time — don't read "simultaneism is the limit" as "simultaneism is always fine near equilibrium for all t." It is fine only away from initial layers and only to O(τ).

---

## 7. The economics explainer

**The transformation problem in plain terms.** Labor creates value; prices should then reflect labor. But prices visibly differ from values, and the question of exactly how values "become" prices (and where profit comes from) is the transformation problem. The modern formal treatment splits into two camps:

- **Simultaneist (Bortkiewicz–Sraffa–Steedman).** Prices and values determined at one logical instant, input prices = output prices. Consequence: Marx's two aggregate equalities fail; the labor theory of value is inconsistent or redundant; and technical change cannot lower the profit rate (Okishio).
- **TSSI (Kliman–McGlone 1999; Freeman 1996).** Determination is sequential: inputs enter at *t*, outputs emerge at *t+1*; values and prices form one system. Under this reading the aggregate equalities hold and the falling-rate-of-profit argument survives Okishio.

**Why TSSI is unfinished.** Its sharpest critics (Veneziani 2005; Mohun & Veneziani 2009) make two charges: TSSI has *no precise equilibrium concept* and *no rigorous disequilibrium dynamics*; and its equations are *underdetermined* — they don't pin down their own trajectories. Both charges are true and both are, formally, a **missing closure**: the balance laws are there (value conservation), but the *constitutive theory* — how prices are actually formed, with what lags — is absent. The gravitation literature (Steedman 1984; Flaschel–Semmler 1987; Duménil–Lévy 1987) provides *some* closure (capital flows slaved instantly to profit differentials) but reaches mixed verdicts on convergence, with no unifying criterion.

**What this program adds, in economics' own terms.** A dynamical-system treatment of temporal value formation:

- **Well-posedness**: the temporal recursions (discrete Kliman–McGlone, continuous Freeman) become well-posed systems with a precise equilibrium concept (the equalized-profit-rate / production-price state) — answering Veneziani in economics' language (Track D).
- **Closure**: the underdetermination is resolved by a constitutive theory restricted by an entropy-type principle — the same selection rule physics uses, now economically interpreted (relaxation of capital mobility, τ_J from organization/credit/turnover lags).
- **Gravitation, unified**: the SK-type coupling condition is the long-sought criterion for price→price-of-production convergence; the mixed classical results are its special cases (this is the program's make-or-break deliverable).
- **Limit theorem**: simultaneism = the τ→0 singular limit of temporal determination — simultaneist results (Okishio, the equalities' failure) hold near equilibrium and fail in initial layers, *and the failure is bounded and explained*.

**The statistical-equilibrium connection.** Foley (1994) gives markets as maximum-entropy equilibrium — a Jaynesian endpoint. Scharfenaker & Semieniuk's (2017) stationary Laplace-distributed profit rates are the empirical signature of that endpoint *and* of a non-equilibrium steady state: a relaxational system under continuous forcing shows persistent dispersion, never equalization. Under the classical instantaneous view the dispersion is an anomaly; under the relaxational view it is the *prediction*.

**What's novel.** A quantitative theory of disequilibrium value–price dynamics with (i) a well-defined equilibrium concept, (ii) a rigorous sense in which equilibrium is the relaxation limit of disequilibrium, and (iii) a testable stability criterion — none of which the literature currently has.

**Reception risk.** Heterodox economics may see the physics as decorative; mainstream may see the value-theory framing as irrelevant. The answer is to publish per-track in disciplinary venues (applied math for the theorems, economics journals for the economics-facing results), with cross-references — the program doc's publication strategy (§10).

---

## 8. The computer science explainer

**Three roles.** Computer science enters the program in three distinct ways — *simulate, discover, certify*.

**Role 1 — Simulate (Track C).** Agent-based models (Wright 2005) are the *microscopic/kinetic level*: many heterogeneous agents whose aggregate behavior the continuum model approximates. The key experiment discriminates the two theories: inject a localized sectoral shock and measure how the disturbance spreads.

- If value–price dynamics are **parabolic** (simultaneist), the affected region grows like t^(1/2) with no sharp front.
- If they are **hyperbolic** (temporal/relaxational), the affected region grows *linearly in time with a visible front*.

This is the telegraph→diffusion distinction (Kac–Goldstein) measured on a computer. ABMs also let you estimate the *relaxation spectrum* and compare correlation decay (oscillatory telegraph-type vs. monotone diffusive). On the data side, input–output tables (OECD ICIO / WIOD) let you compute labor values, production prices, and sectoral profit-rate dispersion, and estimate effective relaxation times τ_J from the dynamics of dispersion.

**Role 2 — Discover (Track E).** The underdetermination critique has a computational answer: instead of *postulating* the constitutive closure (τ_J, κ), **learn it from data** — the closure becomes a falsifiable object. This is equation discovery / sparse regression (SINDy-style), neural closures, physics-informed learning — with two disciplines statisticians will recognize:

- *Learn within an admissible class*: the search is constrained to closures consistent with the entropy principle and the subcharacteristic condition — regularization by physics, exactly as one regularizes by smoothness or sparsity.
- *Validate forward*: test on unseen regimes (new sector topologies, out-of-distribution shocks), not by residual fit on training data. If you've ever been burned by an overfit model's "great in-sample, garbage out-of-sample" performance, you already know why this matters.

This also answers a deeper question the program poses to the data: *is there relaxation structure at all?* — i.e., is the parabolic (simultaneist) description adequate, and if not, where does it break? Track E also builds the numerical infrastructure (relaxation schemes in the Jin–Xin tradition, finite-volume methods on graphs, front tracking) that verifies T2 (front speeds) and T3 (the relaxation limit) numerically.

**Role 3 — Certify (Track F).** Proof assistants (Lean 4, Coq) let the program *machine-check* its core theorems — existence, uniqueness, exponential decay of initial-data errors for the discrete temporal recursion — and *certify* numerical error bounds (interval arithmetic / Taylor models, the CoqInterval tradition). Executable categorical models (AlgebraicJulia: Catlab / AlgebraicDynamics / Decapodes) turn the program's compositional structure into working software that composes balance-law subsystems into economies. The disciplinary point: computation as an *instrument of rigor*, not just a source of numbers.

**The statistics bridge.** The ABM→continuum limit is a law-of-large-numbers/CLT story at the agent level (hydrodynamic limit). Closure discovery is the inverse problem of recovering a dynamical law from data — with identifiability and regularization concerns you know cold. The front-vs-diffusion experiment is a hypothesis test with a clean, visual statistic.

**Risks.** Agent-based noise can swamp front detection (fix: ensemble designs with replication). Input–output data are annual and sector-aggregated, so τ_J estimates are order-of-magnitude only. Learned closures can overfit (fix: structured/symbolic discovery + forward validation). Formalization is time-intensive (fix: scope to the discrete core first).

---

## 9. Assembling the tracks

The program is organized as the six pairings of four disciplines; every pairing has one track.

| Track | Pairing | Role in one line | Answers gap |
|---|---|---|---|
| A | Physics × Economics | The applied core: build and analyze the hyperbolic value–price system; theorems T1–T4 | G1, G3 |
| B | Mathematics × Physics | Axiomatize extended thermodynamics categorically (operads, GENERIC) | G2 |
| C | Computer Science × Economics | Agent-based simulation and input–output estimation; discriminate hyperbolic vs. parabolic | G4 |
| D | Mathematics × Economics | The same results in economics' own language; axiomatic transformation theory | G1, G3 |
| E | Physics × Computer Science | Numerical methods for relaxation systems; data-driven closure discovery | G5 |
| F | Mathematics × Computer Science | Machine-checked theorems and executable categorical models | G6 |

**Cross-imports, in plain language.** A and D prove the same theorems for two audiences (A with physics tools, D in economics' idiom) — they cross-reference rather than duplicate. E is A's computational arm (it verifies T2/T3) and D's answer to underdetermination (closure discovery). F formalizes D's results and certifies A's numerics. C is the program's *microfoundation* — the kinetic level whose hydrodynamic limit the continuum model approximates — and E2 learns the closure from C's agent-based data. B depends only on the literature plus A's model.

**Phasing.** Year 1: A1 (the Master's thesis), D1, E1 begin. Year 2: A2, D2–D3, E2, F1, B1, C1. Year 3: A3, D4, E3, F2, B2, C2. Year 4+: integration, F3, program-level synthesis. Dependencies are in the program doc §10.

**Scope discipline.** The Master's thesis is deliberately minimal; E and F are *infrastructure for A–D*, not standalone agendas. Ecological macroeconomics is named only as a future application domain, not a track. The program document is a map, not a promise.

---

## 10. What success looks like

**For physics.** The first non-physical application of RET, with the entropy-principle methodology doing genuine work (closure selection answering an actual underdetermination dispute) — and a categorical axiomatization of non-equilibrium extended thermodynamics.

**For mathematics.** Four proven theorems (T1–T4) establishing well-posedness, the singular relaxation limit, and a necessary-and-sufficient stability criterion for value–price dynamics; equilibrium-as-singular-limit as a theorem about economic adjustment.

**For economics.** A well-posed temporal value theory with a precise equilibrium concept, a bounded-and-explained sense in which simultaneism is its approximation, a unifying gravitation criterion, and contact with the empirical record (stationary Laplace-distributed profit rates as a driven-relaxation prediction, not an anomaly).

**For computer science.** A discriminating experiment (front vs. diffusion), an estimator for relaxation times from input–output data, a data-driven closure-discovery pipeline with forward validation, and machine-checked versions of the program's core theorems.

**And the concrete first slice — the Master's thesis (M1).** Six months: the Cattaneo-type model (T1 well-posedness, T2 linear theory, T3 relaxation limit, T4 stability criterion for the linear/network case), plus small-scale numerics showing finite-speed propagation of a sectoral profit shock vs. diffusive spread. This is, in statistical language, a clean project: define the generator, prove its spectral structure and its singular limit, and demonstrate the qualitative difference on a concrete example. The entropy-extension problem it leaves open is the natural Master's-to-PhD bridge.

---

## 11. Glossary

- **Transformation problem** — the century-old question of how labor values become prices (and where profit comes from).
- **Simultaneist theory** — prices/values determined at one instant, input prices = output prices (Bortkiewicz, Sraffa).
- **TSSI (temporal single-system interpretation)** — values and prices form one system, determined sequentially in historical time (Kliman–McGlone, Freeman).
- **Gravitation** — the (empirically contested) tendency of market prices to converge to prices of production.
- **Price of production / equalized profit rate** — the equilibrium state: all sectors earn the same rate of profit.
- **MELT (monetary expression of labor time)** — the time-varying exchange rate between labor-time and money.
- **Closure / constitutive relation** — the missing relation that says how flows respond; the underdetermination charge is a missing closure.
- **Entropy principle** — a selection rule over admissible closures, implemented via Lagrange multipliers (Liu); in this program it answers the underdetermination charge.
- **Cattaneo equation** — the flux-relaxation law τ ∂q/∂t + q = −κ∇T; the minimal cure for infinite propagation speed.
- **Hyperbolic vs. parabolic** — finite-speed (telegraph) vs. instant-spreading (diffusion) dynamics.
- **Relaxation time τ** — the lag with which a flow responds to a driving differential; τ→0 recovers the instantaneous theory.
- **Singular limit** — a limit that changes the type of the system; not uniformly valid in time (boundary/initial layers).
- **Subcharacteristic condition** — the admissibility condition for the relaxation limit to make physical sense.
- **Shizuta–Kawashima (SK) condition** — a coupling condition between the source and the convection terms that characterizes decay to equilibrium.
- **Symmetric hyperbolicity** — the structural property (from a convex entropy extension) that guarantees well-posedness and finite speeds.
- **Main field** — the Lagrange-multiplier variables in which the system becomes symmetric hyperbolic; dual to the state like the natural parameter is to the mean in an exponential family.
- **Relative entropy / KL divergence** — the candidate Lyapunov function ("entropy") for value dynamics; its monotone decay is the program's H-theorem.
- **Statistical equilibrium** — markets as maximum-entropy distributions (Foley); the Jaynesian endpoint whose time-development this program supplies.
- **Non-equilibrium steady state** — persistent dispersion under continuous forcing; the relaxational explanation of Laplace-distributed profit rates.
- **Kinetic/microfoundation** — the agent-based level whose hydrodynamic limit the continuum model approximates (Track C).

---

*Companion documents: `program/research-program.md` (authoritative); `program/critiques.md` (18 steelmanned objections + responses); `findings.md` (formal correspondence and model skeleton); `program/references.bib` (75 verified references, track-organized).*
