# Grounded answer — τ→0 relaxation limit versus the SK condition

Produced by the opencode agent (LLM side) from repository evidence only: the
question was posed, the knowledge repository returned the grounding trace
(hyperedge intersections, ≥3 of 5 seed concepts), and this synthesis is drawn
strictly from the sections that trace surfaced. Reproduce with:

```
python scripts/pipeline.py trace_report '{"topic":"How does the tau->0 relaxation limit relate to the SK condition for gravitation convergence?","concepts":["tau_J","sk condition","subcharacteristic","gravitation","T3"],"min_seeds":3}'
```

## Question

How does the τ→0 relaxation limit relate to the SK condition for gravitation convergence?

## Synthesis

The two are **different convergence diagnostics on the same system**, and they answer different questions about it:

1. **SK condition — stability of the target state.** The Shizuta–Kawashima coupling condition is the criterion for whether small disturbances around the extended (hyperbolic) system *decay* to equilibrium — here, convergence of market prices to production prices with an equalized profit rate. It is restated as a condition on the technology matrix and mobility coefficients (A, κ) (**program §4 Track A**; **program §7 Track D**; the correspondence table maps "SK condition ⇔ decay to equilibrium"**.

2. **T3 / relaxation limit — validity of the instantaneous approximation.** The τ→0 limit is *singular*: temporal dynamics converge to the simultaneous-closure dynamics at rate O(τ) on compact time intervals, but not uniformly in time — an initial layer (the post-shock transient during which simultaneism misprices) is an unavoidable boundary-layer effect and is itself an economic result (**program §4 Track A**; **findings §5**; **walkthrough §6 mathematics explainer**).

3. **Their relationship.** SK tells us the τ-system *settles* where it should; the relaxation limit tells us when the reduced (instantaneous, simultaneous) description is a good stand-in and precisely where it fails. The **subcharacteristic condition** governs *admissibility* of the reduced limit — the relaxation-limit speeds interlace correctly — without which the τ→0 reduction would not be the right approximation (**program §2.2**, surfaced via the trace's §6/§11 entries). Together: **the extended system must both be stable (SK) and reduce faithfully (subcharacteristic + O(τ) bound)** for the program's claim — "simultaneism is the equilibrium approximation of temporal determination" — to hold with both directions made rigorous.

## Evidence actually used (trace hits)

18 intersecting sections; the load-bearing ones:

- `ret-tssi/program/research-program.md` §4 Track A (all five seeds: τ_J, SK, subcharacteristic, gravitation, T3) — T3 singular-limit statement and T4 SK-criterion statement
- `ret-tssi/findings.md` §5 — model skeleton, T3/T4 conjectures
- `ret-tssi/program/research-program.md` §3 — correspondence table (SK ⇔ gravitation convergence; τ→0 ⇔ simultaneist limit)
- `ret-tssi/program/research-program.md` §7 Track D — stability criterion in economics' language
- `ret-tssi/program/critiques.md` A1 — "physics envy" defence (simultaneism-vindication flank)
- `ret-tssi/to_human/2026-08-16-proposal-walkthrough.md` §6 mathematics explainer — singular-limit subtlety, §11 glossary

## Grounding discipline

Any assertion above is tied to a section found by the trace; none goes beyond it.
Regenerate the trace (and if the corpus has changed, `python scripts/build_hypergraph.py --force`) before reusing this synthesis.