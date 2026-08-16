# Findings — The Formal Correspondence

Working synthesis behind `program/research-program.md`. Notation: sectors i = 1..n; p = price vector; A = input matrix; l = direct labor vector; w = wage rate; r = profit rate; K = capital stocks; J = intersectoral capital fluxes; τ (or τ_J) = relaxation time; τ_t (context-dependent) = MELT. Where collision is possible the MELT is written "MELT".

---

## 1. The two paradoxes of simultaneity

**Heat paradox (Cattaneo 1948).** Fourier's constitutive law q = −κ∇T closes the energy balance ρc_v ∂T/∂t + ∇·q = 0 as the *parabolic* heat equation ∂T/∂t = (κ/ρc_v)ΔT. Fundamental solution has unbounded support for t > 0: a localized disturbance is felt everywhere instantly. The defect is traced to the *instantaneous constitutive closure*: the flux q is slaved algebraically to the contemporaneous gradient ∇T. Remedy: promote q to a state variable with its own evolution equation, τ ∂q/∂t + q = −κ∇T. The closed system is the *hyperbolic* telegraph equation τT_tt + T_t = (κ/ρc_v)ΔT, with finite front speed c = √(κ/(ρc_v τ)). Parabolic theory is the singular limit τ → 0.

**Transformation problem (Bortkiewicz 1907–).** Simultaneous determination closes the price system algebraically: p = (1+r)(pA + wl), with input prices = output prices *by construction*. All magnitudes are slaved to one another at a single logical instant; there is no Cauchy problem, no propagation, no initial data. The alleged inconsistencies of Marx's construction (failure of the two aggregate equalities in dual-system readings) arise at this point of instantaneous closure. TSSI remedy: determination is *sequential* — p_{t+1} = F(p_t, current production data) (Kliman–McGlone 1999), or continuous-time conservation dynamics (Freeman 1996). Input and output prices differ; the system propagates forward in historical time.

**Homology.** In both cases: (i) an instantaneous closure creates a pathology (infinite speed / alleged inconsistency and redundancy charges); (ii) the resolution *temporalizes* the closure by giving the slaved quantity its own dynamics; (iii) the orthodox theory is recovered as a limit in which the new dynamical timescale vanishes. The program's claim is that this homology is *formal*, i.e., expressible in a common mathematical framework (hyperbolic balance laws with relaxation), not merely rhetorical.

## 2. The thermodynamic pole (what we borrow)

RET structure (Müller–Ruggeri 1998):
1. **Balance laws:** ∂u/∂t + Σ_k ∂F_k(u)/∂x_k = G(u), u ∈ R^N.
2. **Constitutive theory:** F, G functions of the present local state; admissible constitutive relations selected by the entropy principle (Müller 1967; Liu 1972 Lagrange multipliers).
3. **Entropy extension:** scalar balance law ∂h/∂t + ∇·φ = Σ ≥ 0 with h concave in u.
4. **Ruggeri–Strumia 1981:** convex entropy extension ⇔ main-field variables (Lagrange multipliers) render the system *symmetric hyperbolic* ⇒ finite characteristic speeds + local well-posedness of the Cauchy problem.
5. **Relaxation limit (Chen–Levermore–Liu 1994):** with stiff source G(u)/ε, ε → 0 drives the system onto the equilibrium manifold G(u) = 0; the reduced dynamics is parabolic (Chapman–Enskog). Subcharacteristic condition: reduced-system speeds interlace with full-system speeds.
6. **Stability (Hanouzet–Natalini 2003; Ruggeri–Serre 2004; Bianchini et al. 2007):** entropy dissipation + Shizuta–Kawashima coupling condition (ker DG ∩ eigenspaces of convection = {0}) ⇒ global existence and asymptotic decay of small perturbations to constant equilibrium; entropy + compensation term = Lyapunov functional.

## 3. The economic pole (what we reformulate)

**Simultaneist system.** Algebraic fixed point: p = (1+r)pM, r from the Perron–Frobenius eigenvalue. No time.

**TSSI system (discrete; Kliman–McGlone).** p_{t+1}x determined from p_tA, w_t, living labor λx; MELT_{t+1} = p_{t+1}x / (MELT_t^{-1}p_tAx + λx). Real profit π_R = MELT_t·s (s = surplus labor). A difference-equation (sequential) closure; underdetermined as written (Mohun–Veneziani): needs constitutive closure for price formation.

**TSSI system (continuous; Freeman 1996).** Conservation of value as differential equations; stocks change by flows; the MELT is a time-varying coupling field between monetary and labor-time measures.

**Gravitation/cross-dual dynamics (Steedman 1984; Flaschel–Semmler 1987; Duménil–Lévy 1987).** Real-time adjustment ODEs:

  dq_i/dt = α_i (r_i − r̄)        (capital/quantity responds to profit differential)
  dp_i/dt = β_i (d_i − q_i)       (price responds to excess demand)

with r_i = (p_i q_i − cost_i)/K_i. Convergence results mixed: Nikaido-type counterexamples; Steedman's negative cases; Flaschel–Semmler's modified stable process; Cockshott (2016) simulations: some converge, some don't. *No unifying stability criterion exists.* Crucially: capital reallocation is slaved **instantaneously** to profit-rate differentials — a Fourier-type closure.

## 4. The correspondence table

| Classical irreversible thermodynamics | Simultaneist/dual-system value theory |
|---|---|
| Fourier law q = −κ∇T (instantaneous closure) | Input prices = output prices (instantaneous determination); capital flows slaved to current profit differentials |
| Parabolic field equations | Algebraic fixed-point system (elliptic/no-time); parabolic adjustment when embedded in tâtonnement |
| Infinite propagation speed (heat paradox) | "Instantaneous equilibration": inconsistency/redundancy charges; Okishio-style results that erase dynamics |
| Equilibrium thermostatics only well-founded | Long-period equilibrium (production prices) only well-defined state |

| Rational extended thermodynamics | Temporal single-system value theory (proposed formalization) |
|---|---|
| Fluxes promoted to state variables (Cattaneo: τq_t + q = −κ∇T) | Capital fluxes J promoted to state variables: τ_J dJ/dt + J = −κ∇_sector r (proposed) |
| Hyperbolic balance laws, finite characteristic speed | Sequential/temporal determination; finite-speed propagation of price-value disturbances across the IO network |
| Entropy concave in extended state (incl. fluxes) | Candidate convex functional on (p, r, J) deviations from production-price equilibrium |
| Parabolic theory = τ→0 singular limit | Simultaneist system = τ_J→0 singular limit (H4) |
| SK condition ⇒ convergence to equilibrium | Coupling condition on capital mobility ⇒ gravitation convergence (H3); explains mixed results |
| Clausius–Duhem as constitutive selection rule | Entropy principle as closure selection rule → answers TSSI underdetermination charge |
| Coleman–Noll vs Müller–Liu procedures | New Interpretation vs TSSI "two rationalizations" (Track B parallel) |

## 5. Model skeleton (Track A, Phase 1 — candidate Master's problem)

Minimal setting: n-sector circulating-capital economy, Freeman-style continuous time.

**State vector:** u = (p, K, J) ∈ R^{3n} (prices, sectoral capitals, intersectoral reallocation fluxes; labor values λ = λ(A,l) fixed parameters at each technical state; MELT as coupling field).

**Balance laws:**
- Value conservation (Freeman): dp/dt determined by production + MELT dynamics; aggregate constraints Σp_i x_i = Σλ_i x_i·(MELT), profit = surplus value in aggregate (Marx's two equalities as global conservation laws).
- Capital balance: dK_i/dt = Σ_j (J_{ji} − J_{ij}) (continuity equation on the sector network; the IO matrix A gives the network Laplacian structure).
- Cattaneo-type closure (the new constitutive relation):
  τ_J dJ_{ij}/dt + J_{ij} = κ_{ij}(r_j − r_i),  κ ≥ 0
  — capital flux responds to profit-rate differentials with relaxation time τ_J (organization, credit, and fixed-capital turnover lags).

**Fourier-type classical closure** (gravitation literature): J_{ij} = κ_{ij}(r_j − r_i) — recovered at τ_J = 0.

**Linearization about production-price equilibrium u*:** telegraph-type system on the IO network; characteristic speeds c ~ √(κ/τ_J · spectrum(network Laplacian)); dispersion relation shows (i) finite front speed, (ii) τ_J→0 collapses to diffusive (parabolic) gravitation, (iii) damping spectrum governs convergence rate.

**Conjectures to prove (Phase 1):**
- T1 (Well-posedness): local existence/uniqueness for the quasilinear system; global existence near equilibrium for small data.
- T2 (Linear stability + spectra): eigenvalue asymptotics as τ_J → 0⁺; convergence of the semigroup to the parabolic gravitation semigroup (Trotter–Kato / singular perturbation).
- T3 (Relaxation limit): u^{τ} → u^0 with error estimate O(τ_J) on compact time intervals; u^0 solves the simultaneous-closure dynamics; its rest state is the Sraffian fixed point.
- T4 (Stability criterion): an SK-type coupling condition on (A, κ) equivalent to asymptotic convergence to equalized-profit-rate equilibrium; show Flaschel–Semmler modifications enforce it and Nikaido/Cockshott failures violate it.

**Open (hard, Phase 2+):** entropy extension for the full nonlinear system (H2) — candidates: quadratic entropy of the linearization (free), relative-entropy/KL-type functional on price-value deviations, or a Farjoun–Machover distributional entropy; economic meaning of the "entropy production" (dissipation of profit-rate differentials = destruction of arbitrage opportunities?) — interpretive work needed.

## 6. Track B synthesis (foundations)

- Baez–Lynch–Moeller: thermostatic system = (convex space X, concave S: X → R̄); composition via operad Op(ConvRel); equilibrium = joint entropy maximization. **Equilibrium only.**
- RET state: convex space with *flux-graded* structure; dynamics = balance laws; admissibility via entropy *inequality* on processes, not maximization on states.
- B1 problem: define "extended thermostatic/thermodynamic systems" as algebras of an operad of *relaxation processes* (morphisms = constrained decay to equilibrium with timescales), such that the τ→0/forgetful functor recovers Op(Ent). This is a concrete, well-posed categorical question.
- B2 problem: express Coleman–Noll (supply-quantification) and Müller–Liu (Lagrange multipliers) exploitation procedures as two constructions on one categorical structure (e.g., a category of balance-law theories with an entropy principle object); prove when they coincide (they do on overlapping domains per the continuum literature) and where they diverge.
- B3 (later): type-theoretic formalization (Lean/Coq) of the balance-law category and of T1–T4 statements; Lawvere's SDG continuum-physics treatment as the philosophical frame (intensive/extensive as mapping-space structure).

## 7. Track C synthesis (computational/empirical)

- ABM (Wright 2005 architecture): inject a sectoral shock; measure disturbance propagation front speed vs. system size (hyperbolic: linear growth of affected region; parabolic: t^{1/2}); estimate relaxation spectrum; compare correlation decay (oscillatory telegraph-type vs. monotone diffusive).
- Data: WIOD / OECD ICIO tables; Cockshott–Cottrell methodology for values/prices/profit rates; estimate effective τ_J from dispersion dynamics of sectoral profit rates (Vaona's gravitation econometrics is adjacent precedent).
- Link to stochastic microfoundations: telegraph→diffusion (Kac/Goldstein) rescaling mirrors ABM→continuum limit.

## 8. Risk register (program level)

1. **Entropy extension may not exist** for the natural economic closures (H2 failure) — mitigate: EIT-style generalized entropy; or proceed with Lyapunov-only methods (T4 doesn't strictly need symmetric hyperbolicity).
2. **Analogy collapse risk**: the mapping must earn its keep by proving things the value-theory literature couldn't — T4 (unified stability criterion) is the make-or-break deliverable.
3. **Reception risk**: heterodox economics may view the physics as decorative; applied math may view the economics as soft. Mitigate by publishing per-track in disciplinary venues with cross-references.
4. **Data risk**: low — ICIO/WIOD public.
