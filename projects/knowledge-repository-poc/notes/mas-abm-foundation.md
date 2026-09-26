# MAS/ABM Foundation — architecture memo

Status: working draft (2026-08-29).
Purpose: foundation decision for the larger goal — a tool to **improve
democratic economic planning** — linking the three live projects. Reads as a
companion to `notes/plumbing-vs-lean-dijkstra-automata.md` (the option survey it
draws on).
Three threads being linked: RET×TSSI (`projects/ret-tssi-value-dynamics`),
island digital twin (`projects/island-digital-twin`), knowledge repository +
plumbing (`projects/knowledge-repository-poc`).

---

## 1. The goal, decomposed

A tool to improve democratic economic planning needs three parts:

1. An **agent-based modeling (ABM) platform** that simulates the future states
   of a proposed plan, grounded in a **local digital twin** (real data,
   metabolic flows, infrastructure, topography).
2. **Multi-agent systems (MAS)** that implement adopted plans — real-world
   actors coordinating execution. **A local digital twin is itself a
   multi-agent system**: every real asset/entity has a digital proxy agent that
   mirrors its state.
3. A key alignment goal: the **agent-based modeling language and the
   multi-agent systems must be the same** — the agent description you simulate
   is the agent code you deploy, so model and implementation cannot drift.

The foundation must get this right early, even though it is overkill for the
present research agent.

## 2. What the foundation must provide

| # | Requirement | Why |
|---|---|---|
| R1 | Heterogeneous, stateful, adaptive agents, many instances | Households, firms, planner, environment — the SR-style heterogeneous-agent microfoundation |
| R2 | Simulation performance + statistical method (Monte Carlo, distributions, run/ensemble analysis) | "Simulate many futures of a plan"; validate against known empirical regularities (e.g. Zipf firm size, Laplace growth — already in the corpus) |
| R3 | Typed, checkable coordination protocols | Markets, negotiation, plan allocation among implementing agents |
| R4 | Capability/safety enforcement | Agents that act in the world (resource use, ecological caps, democratic constraints) must have their reachable effects bounded and enforced |
| R5 | Model↔deployment alignment by construction | The core goal (§1.3) — drift-free single source |
| R6 | Data channel to the twin + participatory loop | Grounding in real data; humans in the loop (geodesign-style iteration) |
| R7 | Certification path for safety-critical invariants | Proof-producing; safety claims not just tested |
| R8 | Democratic transparency | Architecture inspectable by people, not latent in prompts/code — "explicit over implicit" |

## 3. Options assessed (detail in `notes/plumbing-vs-lean-dijkstra-automata.md`)

### A. Expanded plumbing (OCaml; session-typed channels; Coq proof seam; TLA+ runtime laws; Eio host; subprocess `exec`)
- **Strong:** R3 (the only option with a *today-executable* typed-protocol +
  verified-compilation story), R6 wiring, R8 (architecture-as-program, drawable
  and checkable).
- **Weak:** R1 (agents are stream transducers; wrong shape for heterogeneous
  behavioral agents), R2 (exec workers too heavy for per-agent-per-step
  numerics; no sim statistics), R4 (shape-only today; capability seam is a §5
  design not an implementation).

### B. Lean→OxCaml (as proposed: Dijkstra capability signatures; refinement-certified automaton ticked by Eio; LLM-written specs)
- **Strong:** R4 at the theoretical limit (capability signatures, refinement
  certificate); the LLM-spec stretch goal suits participatory drafting; aligns
  with the F*/Coq Dijkstra lineage.
- **Weak:** not a simulation platform (R1/R2); OCaml's scientific stack weakest
  of the three hosts; introduces a *third* language into the R5 alignment.
  Best role migrates to Rocq→Rust extraction anyway.

### C. Rocq→Rust + Tokio (coq-rust-extraction; capability gate by construction; Tokio tasks)
- **Strong:** R5 by construction (one language for model, sim, and deployment);
  R1/R2 (performance + scientific ecosystem for heterogeneous-agent sim; Monte
  Carlo headroom); R4 (borrow-checked gate — bypass is a compile error, not a
  runtime possibility); R7 (Rocq extraction gives certified Rust source with
  refinement proof, Dijkstra reasoning carried over from Coq); R6 (PyO3 bridge
  to the Python ABM ecosystem if ever wanted; native performance for the sim).
- **Weak:** R3 not provided (no shipped typed protocol language — must build or
  adopt one); no built-in scheduler tick (the gate is yours to build; §6 of the
  survey); extraction yield is functional-subset (async glue is handwritten —
  the second-certificate problem).

## 4. Ranking and roles

1. **Rocq→Rust/Tokio = the platform and the language of alignment.** It is the
   only option where the ABM and the MAS are the same program and the safety
   kernel is still certified. Rust hosts the twin-as-MAS, the ABM, and the
   deployed implementing agents.
2. **Expanded plumbing = the coordination fabric on top.** Typed protocols,
   session-typed agent coordination, TLA-checked concurrency laws, and the
   knowledge-repository wiring the whole tool reads its evidence through.
3. **Lean→OxCaml = superseded here** — its enforcement-kernel role is played by
   Rocq→Rust extraction; its LLM-spec angle survives, re-targeted to Rocq.

## 5. How the three threads compose

```
participatory loop (humans, geodesign)      ─  island-DT   (ground truth + process)
        │
        ▼
  TWIN-AS-MAS (data-backed Rust agents)     ─  island-DT   (twin container)
        │ feeds real state
        ▼
   ABM platform (Rust agents; sim many      ─  ret-tssi    (Track C microfoundation,
   futures of the plan; validate vs                     Track E simulator)
   continuum model + empirics)
        │
        ▼   adopted plan
 IMPLEMENTING MAS (same agents, enforced    ─  all three   (R4/R7 kernel: Rocq)
 capabilities; typed coordination)                        (R3 fabric: plumbing)
        │
        ▲
knowledge repository + plumbing pipelines   ─  plumbing   (memory, wiring, protocols,
   (hypergraph, typed pipelines, MCP)         grounding evidence `doc :: section`)
```

Role mapping of the RET×TSSI program's computational tracks onto the stack:

| Program track | Role | Hosted by |
|---|---|---|
| Track C (Computer Science × Economics) | agent-based microfoundation (kinetic level of the continuum model) | Rust ABM |
| Track E (simulator) | simulation → hydrodynamic/continuum correspondence; empirical estimation | Rust ABM + twin data |
| Track F (certifier) | formal certification of results, verified numerics | Rocq kernel (via extraction) |

The three research threads are therefore not alternatives to be merged into one;
they are the theory layer (ret-tssi), the ground-truth + participatory layer
(island-DT), and the infrastructure layer (knowledge-repo/plumbing) of one tool.

## 6. Decisions proposed (to confirm)

- Adopt **Rust + Tokio as the ABM/MAS host language**, with agent model = agent
  deployment by construction (R5).
- Adopt **Rocq (+ coq-rust-extraction) for the certified core**: plan
  invariants and capability policies proved in Rocq, extracted into the Rust
  agents (Refinement proof from the survey's §6 applies; Lean is not the target
  because Lean→Rust extraction is not first-class).
- Keep **plumbing as the coordination/protocol + knowledge-wiring layer**, and
  continue the POC exactly as is (it runs today's research agent; nothing
  changes now).
- Defer: where to cut the certified-kernel boundary (which invariants are Rocq),
  and whether a session-protocol runtime for Rust is built or adopted.

## 7. Sources

- Option survey: `notes/plumbing-vs-lean-dijkstra-automata.md` (§3–§6)
- Corpus anchors for the ABM/epistemic role: SR heterogeneous-agent model
  (`openalex/https_openalex.org_W2017005585`), extended thermodynamics corpus
- Island-DT framing: `projects/island-digital-twin/literature-review.md`
  (metabolism + CityGML-class 3D + participatory geodesign)
- RET×TSSI computational roles: `projects/ret-tssi-value-dynamics/program/research-program.md`
  (Tracks C/E/F), `to_human/2026-08-16-proposal-walkthrough.md`
- Verif. stack: `~/tools/plumbing/doc/compiler-verification-status.md`,
  `runtime-semantics-and-verification.md`