# Critiques of the Program — Steelman Document

**Purpose:** anticipate the strongest objections to *Finite-Speed Value* from each audience it will face, state them fairly, give the program's response, and record what the program document must change in consequence. This is a working document: critique first, rhetoric second. Where a response is weak, the program — not the critic — gets revised.

Format: **Objection** (steelmanned) / **Force** (why it can't be waved off) / **Response** / **Program impact** (required amendment, if any).

**Revision note (2026-08-16):** original version covered the four-track program. Updated for the six-track program (Tracks E — Physics × CS and F — Mathematics × CS added): new objections C5, C6, D4, E4; existing B2 and D1 responses extended with the computational tracks' answers; amendments list extended (#10, #11). Track letters and § references follow the six-track `research-program.md`.

---

## A. From economics broadly

### A1. "Physics envy — this is a metaphor, not a model"

**Objection.** Econophysics has a track record of importing thermodynamic vocabulary without importing the discipline that makes the vocabulary meaningful. Analogy is not evidence. Nothing about hyperbolic PDEs tells us anything about capitalism.

**Force.** Justified by precedent: decades of loose energy/entropy/economics analogies (from Samuelson's *Foundations* remarks onward) with little yield. A hostile referee can quote the program's own correspondence table as decoration.

**Response.** The program stakes *falsifiable mathematical claims*: either the value-price system admits a convex entropy extension or not (H2); either an SK-type condition characterizes gravitation convergence or not (H3/T4); either the simultaneist system is the τ→0 singular limit or not (H4/T3). The analogy's role is *heuristic* — it identifies which theorems to attempt — not probative. And the methodology is not foreign to mathematical economics: Burger–Caffarelli–Markowich–Wolfram (2013) prove a kinetic→parabolic singular limit for price formation; telegraph models exist in option pricing (Ratanov 2007).

**Program impact.** Keep the correspondence table labeled as conjecture-generating; lead all papers with the theorems, not the analogy. Already substantially reflected in `research-program.md`; ensure the Master's exposé opens with the Veneziani gap (a problem *internal to economics*), not with physics.

### A2. "Category mistake: an economy is not a continuum"

**Objection.** Hyperbolicity, wave fronts, finite propagation speed — these are properties of fields on spatial manifolds. An economy has sectors and agents, not a spatial continuum. The central vocabulary is inapplicable.

**Force.** Partly correct, and the program document invites the misreading by using field language.

**Response.** The rigorous home of the model is a *relaxation system of ODEs on the sector network* — second-order-in-time (inertial/telegraph-type) adjustment dynamics on a graph. "Finite propagation speed" means: a shock in sector i reaches sector j no faster than the graph distance times a per-link transmission speed. This is standard mathematics (kinetic and relaxation systems on networks) and needs no spatial manifold. Parabolic-vs-hyperbolic here distinguishes *spectral structure of the generator* (purely diffusive vs. inertial/oscillatory modes), which is a property any ODE semigroup has or lacks.

**Program impact.** **Amend:** make the network/ODE formulation primary in `research-program.md` §4 and use "relaxation system (telegraph-type)" as the working vocabulary; reserve PDE/field language for the optional continuum (large-network/mean-field) limit. This also pre-empts C2 below.

### A3. "Unobservable parameters, unparsimonious"

**Objection.** τ_J is not in any dataset; annual, sector-aggregated data cannot identify a relaxation spectrum; the model adds parameters where Cockshott–Cottrell showed added parameters (Sraffian capital stocks, TSS input prices) buy little predictive information.

**Force.** Their information-theoretic parsimony critique of TSSI is published and quantitative; it applies a fortiori to a model with a new timescale per link.

**Response.** (a) τ_J is estimated, not assumed: Track C2 uses dispersion dynamics of sectoral profit rates (and Vaona's gravitation econometrics gives adjacent estimates). (b) The model's testable content is in *signatures*, not fitted values: oscillatory vs. monotone correlation decay; front-like vs. diffusive shock propagation across the IO network; the τ→0 collapse. (c) Parsimony: the correct comparison class is dynamical models, and the criterion is out-of-sample prediction of adjustment paths, which simultaneist models do not attempt at all.

**Program impact.** State in the program doc (Track C) that ABM-synthetic data is where the signatures are sharp; ICIO/WIOD estimates are order-of-magnitude only (already risk R6).

### A4. "You're solving a non-problem"

**Objection, from the Sraffian flank.** Steedman: prices of production are computable from physical data alone; values are redundant; the transformation problem is dissolved, not solved. Foundations for TSSI are foundations for an interpretation nobody needs.

**Objection, from the TSSI flank.** Kliman: TSSI already refuted the inconsistency charges; the interpretive question is settled; further mathematics is gilding.

**Force.** Both flanks have publication weight; a referee from either can ask "what question remains?"

**Response.** To the Sraffian: the redundancy result itself rests on simultaneous valuation (the physicalist profit rate omits the Δv/v term — Freeman's point). Exhibiting simultaneism as a *singular limit* relocates the debate: the question becomes the validity regime of an approximation, which is a substantive mathematical question, not an interpretive one. To the temporalist: Veneziani (2005) and Mohun–Veneziani (2009) showed TSSI's dynamics are asserted, not analyzed; the program defends TSSI by *completing* it — well-posedness, equilibrium definition, stability — which no amount of exegesis supplies.

**Program impact.** None — this is already the program's stated motivation (G1). Add one sentence to the program doc framing T3/T4 as the *relocation* of the redundancy debate from interpretation to approximation theory.

### A5. "The relaxation limit vindicates simultaneism"

**Objection.** If the Sraffian system is the τ→0 limit of the temporal system, then Bortkiewicz was right in the relevant regime and the TSSI polemic was overblown. Your T3 is an own goal.

**Force.** This reading is rhetorically available and will be made.

**Response.** The limit is *singular*: it changes the type of determination and is not uniformly valid in time. (a) Under secular technical change the simultaneist and temporal profit rates diverge systematically (the Δv/v term); the approximation error *grows* exactly when the economy is changing fastest. (b) The subcharacteristic condition gives a precise criterion for when the simultaneist approximation is legitimate; near it is not. (c) T3 says simultaneism is the equilibrium closure of a dynamics it cannot itself express — which is the TSSI claim, now with a theorem-shaped statement.

**Program impact.** **Amend** program doc §4 T3: state explicitly "singular limit; non-uniform validity; initial-layer transients have economic content (post-shock mispricing)." This is also the honest mathematical scoping (see C3).

### A6. "Stability theorems reintroduce equilibrium by the back door"

**Objection.** TSSI's whole point was non-equilibrium; the program then proves convergence *to* an equilibrium. Isn't this simultaneism with extra steps?

**Force.** Philosophically live within the school; Naples (1993) made a version of this charge against Kliman–McGlone.

**Response.** Non-equilibrium thermodynamics is the theory of *approach to* (and failure to approach) equilibrium; having a well-defined rest state with a characterized basin is what distinguishes dynamics from stasis-talk. The program's content is about the path: finite-speed propagation, relaxation spectra, conditions for non-convergence (persistent dispersion — the empirically normal case under continuous forcing, per A3/Phase 3). Equilibrium here is the anchor of the analysis, not its conclusion.

**Program impact.** None; already implicit. Consider one clarifying sentence in the program doc §1.

---

## B. From within Marxian economics

### B1. "TSSI is an interpretation of a text, not a dynamical system"

**Objection.** The TSSI debate is hermeneutic — what did Marx mean, and is it consistent? Recasting it as balance laws changes the subject.

**Force.** True as sociology: much of the literature is exegetical.

**Response.** The program brackets exegesis entirely. Its claim is conditional: *if* one adopts the temporal single-system ontology, *then* its dynamical content is such-and-such. Interpretive debates continue unaffected; what the program removes is the argument "TSSI is dynamically incoherent/incomplete" (Veneziani) from the arsenal.

**Program impact.** Add to the eventual econ-facing paper: one paragraph explicitly bracketing exegesis.

### B2. "Your closure is one of infinitely many — why this one?" (underdetermination returns)

**Objection.** Mohun–Veneziani's underdetermination charge applies to the program itself: value conservation plus a Cattaneo closure on capital fluxes is underdetermined by any evidence; infinitely many closures are compatible with the aggregates. Choosing the minimal one is aesthetic.

**Force.** Correct that closure is underdetermined by the conservation laws alone. This is the deepest methodological objection.

**Response.** Four layers. (a) RET's whole point is that constitutive relations are *not* determined by balance laws; they are restricted by the entropy principle and by objectivity-type requirements — the program imports exactly this discipline, so the charge is answered by the methodology, not by the closure's uniqueness. (b) The Cattaneo closure is the *minimal inertial extension* of the universal gravitation closure: every cross-dual model in the literature (Steedman, Flaschel–Semmler, Duménil–Lévy) is recovered at τ_J = 0. It is the conservative choice, not an arbitrary one. (c) Closure identification from ABM microdata (Track C) is the empirical answer, mirroring how kinetic theory motivates moment closures. (d) The computational answer (Track E's E2): closure becomes a *falsifiable object* — detected, identified, and forward-validated from microdata rather than assumed (see D4 for the circularity/admissibility caveats).

**Program impact.** State (b) explicitly in the program doc — "nests the entire gravitation literature at τ_J=0" is a strong, checkable claim; keep it prominent.

### B3. "There is no tendency to equalization at all" (the probabilist flank)

**Objection.** Farjoun–Machover, and empirically Scharfenaker–Semieniuk (2017, *Metroeconomica* 68:465–499 — firm-level profit rates are Laplace-distributed, stationary, not converging): the premise that markets gravitate to an equalized rate is empirically false. Your stability theorems describe a state economies are never in.

**Force.** Firm-level evidence is strong; gamma/Laplace dispersion is robust across samples.

**Response.** The SK-type condition is *diagnostic*, not assumed: where the coupling fails (insufficient capital mobility, demand-constrained sectors), the theory predicts persistent dispersion — precisely the probabilist finding. The framework contains both regimes and says which to expect from structural data (A, κ). In this reading, Farjoun–Machover's stationary distributions are the stationary states of a *driven* relaxational system (Phase A3), and the dispersion's shape constrains the closure.

**Program impact.** Add Scharfenaker–Semieniuk to references and to Track C's empirical targets; add one line in §2.4 acknowledging the Laplace-vs-gamma finding.

### B4. Priority/etiquette within the school

**Objection.** Temporalists may read the program as a hostile takeover: "TSSI stands on its own texts; it doesn't need physicists."

**Force.** Real reception risk, independent of content.

**Response.** Frame throughout as *answering TSSI's critics on TSSI's behalf*, using TSSI's own continuous-time formulation (Freeman 1996) as the substrate. Offer the TSSI community the sharpest version of their claim (T3) rather than a replacement claim.

**Program impact.** Rhetorical only; keep Freeman 1996 central (already done).

---

## C. From mathematics

### C1. The entropy extension probably doesn't exist

**Objection.** Convex entropy extensions are rare even for physically derived systems; for an ad hoc economic closure, the bet that one exists (H2) is poor. Without it, no symmetric hyperbolicity, no Ruggeri–Strumia machinery.

**Force.** Correct as a probability assessment. This is the program's central mathematical risk (already R1).

**Response.** The load-bearing results (T1 well-posedness of the relaxation system, T3 singular limit, T4 linear stability criterion) do not require the entropy extension — they need only the ODE/relaxation structure. The entropy search (A2) is deliberately Phase 2, and an *obstruction* result ("no convex entropy exists for the natural closure ⇒ gravitation stability is structurally fragile") is itself publishable and informative.

**Program impact.** None needed; already scoped. Reaffirm M1's thesis does not depend on H2.

### C2. "Hyperbolic" is overdressed for an ODE system

**Objection.** On a finite network these are second-order ODEs; calling them hyperbolic PDEs is terminological inflation that PDE referees will punish.

**Force.** Deserved if the papers use PDE language for ODE objects.

**Response.** Primary vocabulary: *relaxation system, telegraph-type, inertial adjustment*. "Hyperbolic" survives rigorously in two places: the continuum limit of large networks, and the formal analogy to the Cattaneo law. Jin–Xin relaxation systems are the correct citation home.

**Program impact.** Same amendment as A2 (network-first). Jin & Xin (1995, *CPAM* 48:235–276) added to references; also the anchor scheme for Track E's E1, which makes the network-first framing concrete.

### C3. The singular limit is only locally valid in time

**Objection.** Relaxation-limit error estimates hold on compact time intervals with initial layers; T3 as a slogan ("simultaneism = the limit") overstates.

**Force.** Standard fact (Chen–Levermore–Liu; boundary/initial layers).

**Response.** Scope T3 precisely: compact-time convergence with O(τ) error, initial-layer analysis included. The initial layer is an *economic* result (post-shock regimes where simultaneous closure misprices), not an embarrassment.

**Program impact.** Fold into the A5 amendment (singular limit, non-uniform validity).

### C4. Only small-data stability is within reach

**Objection.** Hanouzet–Natalini/Ruggeri–Serre are small-perturbation results; economies experience large shocks; global stability claims would be irresponsible.

**Force.** Correct.

**Response.** The program claims local theory rigorously and uses ABM (Track C) for the large-deviation regime. No global nonlinear stability claims.

**Program impact.** Add to program doc Track A risks: "stability results are local; global dynamics via simulation only."

### C5. "Formalization is a proof of the obvious" (Track F)

**Objection.** Certifying the discrete TSSI recursion in Lean adds rigor but no knowledge: the well-posedness and exponential-decay claims are not in doubt, so the effort produces a machine-checked statement of a theorem nobody was worried about.

**Force.** For F1 as scoped (the discrete recursion), substantively true — the target was chosen for feasibility, not because the claim is controversial.

**Response.** (a) The value of F1 is trust, exact statement, and skills: it eliminates the *ambiguity* component of the TSSI debate — a machine-checked statement cannot silently change definition mid-proof, which is a live complaint in that literature (cf. B2's underdetermination-as-ambiguity reading). (b) F1 is the deliberately simple *entry point*; the program's long-horizon formalization targets (relaxation limits, entropy-extension structure) are where certification would be non-obvious — F builds the theorem bank for that. (c) The verification-ledger value is real for a multi-track program: certified lemmas are reusable infrastructure across A–F, not per-paper artifacts.

**Program impact.** None to the program doc; scope F1 explicitly as "trust + exactness infrastructure, not new mathematics" in §9 (Track F).

### C6. "Proof assistants aren't ready for the real objects" (Track F)

**Objection.** The load-bearing claims — symmetric hyperbolicity, relaxation limits, SK conditions, entropy extensions — are PDE/functional-analysis results. Formalizing even the discrete recursion requires rebuilding large analysis infrastructure (the De Giorgi–Nash–Moser Lean project alone needed ~20,000 lines of Sobolev-space library). F is a research program inside a research program.

**Force.** Correct as a feasibility statement; the formalization frontier is real.

**Response.** Division of labor within F: (a) F1 targets the *discrete* recursion, where the mathematics is discrete/combinatorial — the sweet spot for proof assistants — not the continuum claims; (b) continuous claims remain pen-and-paper, with F3 supplying *verified numerics* (CoqInterval/Flocq) exactly where concrete error bounds matter (T3's relaxation-limit estimates, E1's solver certificates) — a much smaller, mature, tractable target than formalizing PDE existence theory; (c) F2's executability (Decapodes) is a different, cheaper kind of "certification" (working software over machine-checked proofs). Scoped this way, F1–F3 are each feasible; formalizing the full theorem package is deliberately *not* promised.

**Program impact.** None to the program doc; add a scope sentence to §9 (Track F): "F does not promise full formalization of the continuum claims; it certifies the discrete core and the concrete numerical bounds."

---

## D. From physics / thermodynamics

### D1. No kinetic underpinning

**Objection.** RET earned its closures from the Boltzmann hierarchy (moment methods). Your economic "fluxes" have no microscopic kinetic theory; the moment analogy is hollow.

**Force.** The strongest physics-side objection; without microfoundations the closure hierarchy is unjustified.

**Response.** The ABM (Wright-style) plays the kinetic role: the continuum/relaxation system is the hydrodynamic limit of agent microdynamics, with the telegraph→diffusion rescaling (Kac 1974) as the exact template. Track C is thus not "validation" but the program's kinetic theory; Track E's E3 makes this quantitative — numerical verification of the ABM-to-continuum limit and honest finite-size scaling (risk R10). Note EIT is phenomenological and accepted in physics; not every extended theory needs a Boltzmann.

**Program impact.** One sentence in §6 (Track C) reframing C1 as the microfoundation, not just a testbed.

### D2. "Entropy" is just a Lyapunov function with a borrowed name

**Objection.** Thermodynamic entropy has operational content (adiabatic accessibility, Carnot). A convex functional on price deviations has none; calling it entropy is honorific.

**Force.** Partly deserved; the name invites over-reading (cf. the "entropy law of economics" literature the program does *not* want to join).

**Response.** Concede the operational point; what the program uses is the *convex structure* (the object that makes Ruggeri–Strumia and Ruggeri–Serre work). The name is retained only because the construction route (entropy principle as closure selection) is thermodynamic. No "second law of economics" claims anywhere.

**Program impact.** Add explicit disclaimer where the entropy functional is introduced (program doc §3 table row and A2).

### D3. "Why RET rather than GENERIC?"

**Objection.** From the Grmela–Öttinger school: GENERIC offers the geometrically cleaner, modular framework (L·δE + M·δS with degeneracies), multiscale by construction, contact-geometric. RET is moment-hierarchy-bound. Why build on the less general frame?

**Force.** GENERIC genuinely is the more general architecture; Jou (2020) lists it among the living alternatives.

**Response.** Division of labor: RET supplies the *hyperbolicity discipline* and the mature relaxation-limit/stability theory the program's Phase-1 theorems need; GENERIC supplies the *geometric* architecture and the multiscale/reduction viewpoint, which is the right language for Track B (foundations) and possibly for the large-network limit. The frameworks answer different questions here; the program relates rather than chooses between them. A Grmela-style "reduction between levels of description" is arguably the correct *foundational* reading of the value→price passage — to be developed under Track B.

**Program impact.** This is Brad's next-step item 4; a literature note on GENERIC/multiscale thermodynamics should be added (Grmela–Öttinger 1997 PRE 56:6620/6633; Grmela Entropy 2015, 17:5938; Entropy 2021, 23:165; Öttinger 2005 book) and §5 (Track B) amended to name GENERIC/contact geometry as the geometric pole alongside Lawvere/operads. [Status: literature note done (`literature/grmela-generic-multiscale.md`); §5 amendment pending.]

### D4. "Learned closures are circular or unphysical" (Track E)

**Objection.** E2's data-driven closure identification is doubly suspect. *Circularity:* the ABM supplies the training data, but the ABM was built by us — we recover our own modeling assumptions, and the "discovered" τ_J is a projection of what was put in. *Admissibility:* unconstrained machine-learned closures can violate thermodynamic structure (positive entropy production, subcharacteristic condition, frame-invariance), yielding numerically fitted but physically meaningless constitutive relations.

**Force.** Both halves are well-founded. The circularity charge is the standard objection to ML equation discovery (the physics literature concedes learned closures "discover" assumptions); the admissibility failure is an active, documented problem in scientific ML (generalizability and interpretability are open issues; the closure-discovery literature explicitly wrestles with physical-law adherence).

**Response.** (a) *Breaking circularity:* the ABM must be specified at a genuinely different level from the continuum model — agent rules grounded in micro-behavior, not in the relaxation equations — and the learned closure validated *forward* on unseen regimes (new sector topologies, out-of-distribution shocks), not by residual fit on training data. (b) *Admissibility by construction:* learn within the admissible class — physics-informed penalties or, better, *symbolic/sparse discovery within a constrained dictionary* (cf. Pan–Duraisamy 2018; Gupta–Lermusiaux 2021) so the entropy-principle and subcharacteristic structure is imposed, not left to the optimizer. (c) *Honest deliverable:* E2's primary output is *detection* (is relaxation structure present at all, and is τ_J identifiable?) plus identification of the minimal admissible closure — a falsifiable object, not a "true law."

**Program impact.** None to the program doc's §8 (already flags interpretability in R9); make the constrained-discovery requirement explicit in Track E §8 (E2) — "learn within the admissible class (entropy principle, subcharacteristic condition), validated forward."

---

## E. Meta

### E1. Audience squeeze (now four disciplines)

**Objection.** Too much physics for economists, too much economics for mathematicians, and with the computational tracks: too much methodological machinery for both. Falls between venues.

**Response.** Per-track publication (already §10); the Master's thesis is pure applied math with an economic motivation section; the econ-facing paper leads with the Veneziani gap and cites the math paper for proofs. The four-discipline framing *helps* here: it makes explicit that no single paper speaks to all audiences, and it justifies the per-track venue mapping in §10.

**Program impact.** None.

### E2. Missed neighbors

**Objection (anticipated referee note).** The program ignores the statistical-equilibrium tradition in economics proper: Foley (1994, *JET* 62:321–345), and its empirical branch (Scharfenaker–Semieniuk 2017). These already use maximum entropy in economics seriously.

**Force.** Deserved — Foley 1994 is a 300-citation neighbor currently absent from our bibliography.

**Response.** Engage directly: Foley's statistical equilibrium is the τ→0 *static* endpoint of our dynamics in the same sense that Maxwellian equilibrium is the endpoint of relaxation. Position: we supply the dynamics his equilibrium abstracts from. Add to background §2.4 and references.

**Program impact.** Add Foley (1994) + Scharfenaker–Semieniuk (2017) + Mohun–Veneziani (2017, *J. Econ. Surveys* 31:1387–1420 — the axiomatic "impossibility result" reading of the transformation problem, which the program's relocation move (A4) must cite) to `references.bib`; brief mentions in program doc §2.4 and §4.

### E3. Scope creep (self-critique, sharpened for six tracks)

**Objection.** Six tracks, four disciplines, category theory in the attic, neural closures in the basement — this reads as an everything-and-the-kitchen-sink agenda. Overreach.

**Response.** The Master's thesis is deliberately minimal (M1); Tracks B–F are sequenced behind A1, and E/F are *cross-cutting infrastructure for A–D*, not standalone agendas (see E4). The program document is a map, not a promise. Resist adding ecological macro (Brad's item 2) as anything more than a named future application.

**Program impact.** Add one line to §10 (phasing): scope-discipline statement naming the sequencing and the infrastructure role of E/F.

### E4. "The computational tracks are orthogonal to value theory"

**Objection.** With six tracks, an economist reviewer asks where the economics went: E (numerics, ML closures) and F (proof assistants, category-theory software) look like methodology applicable to *any* system, with value theory reduced to a motivating paragraph. The economic content could be window-dressing.

**Force.** True if E and F are read as independent research programs; each genuinely is transferable technology.

**Response.** E and F are explicitly *servants* of A–D, not free-standing agendas, and each is defined by the value-theory problem it serves: E1's solvers exist to verify Track A's theorems (T2, T3) numerically; E2's closure question exists only because the underdetermination critique (B2) demands it, and its output (relaxation structure, identifiable τ_J) is the model's economic content; F1 formalizes Track D's D1 (the TSSI recursion); F2 implements Track B's B1 (the extended-thermodynamics operad) with the economic system as the test case; F3 certifies the *economic* claims' error bounds. The §8–§9 headers in the program doc should state this dependency explicitly.

**Program impact.** **Amend:** add to §8 (Track E) and §9 (Track F) an explicit "these tracks are infrastructure for A–D; they are not promoted as standalone research agendas" sentence.

---

## Consolidated amendments to `research-program.md` (for Brad's approval)

1. §4/§3: network/ODE formulation primary; "relaxation system (telegraph-type)" vocabulary; PDE language reserved for continuum limits. (A2, C2)
2. §4 T3: state singular-limit scoping — compact-time validity, initial layers, non-uniform-in-time under technical change. (A5, C3)
3. §4: note that the Cattaneo closure nests the entire gravitation literature at τ_J = 0. (B2)
4. §4 risks: stability results are local; global dynamics via simulation. (C4)
5. §2.4 + §6: add statistical-equilibrium neighbors (Foley 1994; Scharfenaker–Semieniuk 2017) and Mohun–Veneziani 2017; reframe C1 as microfoundation ("kinetic role"). (E2, D1, B3)
6. §3/A2: disclaimer — "entropy" = convex Lyapunov structure; no operational thermodynamic claim. (D2)
7. §5: add GENERIC/contact-geometry pole to Track B (Grmela refs). (D3) [lit note done; §5 edit pending]
8. §10 (phasing): scope-discipline line; ecological macro named only as a future application domain. (E3)
9. `references.bib`: add foley1994, scharfenaker-semieniuk2017, mohun-veneziani2017, jin-xin1995, grmela-ottinger1997 (I & II), grmela2015, grmela2021, ottinger2005. [**done** — in the six-track bibliography]
10. §8 (Track E) and §9 (Track F): explicit sentence — these tracks are cross-cutting infrastructure for A–D, not standalone research agendas. (E4)
11. §8 E2: constrained closure discovery (learn within the admissible class — entropy principle, subcharacteristic condition; forward validation on unseen regimes). §9 (Track F): scope note — F certifies the discrete core and concrete numerical bounds, not the full continuum theorem package. (D4, C6)

## Watch list (to read before the exposé)

- Foley (1994) — the neighbor we must position against.
- Mohun & Veneziani (2017), *J. Econ. Surveys* — the axiomatic/impossibility framing.
- Scharfenaker & Semieniuk (2017) — the best current profit-rate distribution empirics.
- Jin & Xin (1995) — relaxation systems vocabulary home; Track E's anchor scheme.
- Grmela (2015, 2021) — multiscale thermodynamics; Track B geometry.
- Naples (1993) — the equilibrium/disequilibrium charge against Kliman–McGlone (A6).
- If **M5** (Track E): Raissi, Perdikaris & Karniadakis (2019) and Pan & Duraisamy (2018) / Gupta & Lermusiaux (2021) — the data-driven-closure toolkit; the "scientific machine learning for closure models" review (Found. Data Sci.) for the interpretability caveats (D4).
- If **M6** (Track F): Libkind et al. (2022, operadic modeling) and Morris et al. (2024, Decapodes) — the executable-categorical toolkit; Martin-Dorel & Melquiond (2016, CoqInterval) — the verified-numerics route; one of the large Lean PDE formalizations (De Giorgi–Nash–Moser or Leray–Hopf) to calibrate effort (C6).
