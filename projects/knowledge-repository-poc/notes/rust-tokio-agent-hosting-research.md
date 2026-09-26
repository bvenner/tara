# Rocq→Rust vs Lean→OxCaml: evidence base, Rust/Tokio MAS practice, and the missing effects-benefits half

Status: research note (2026-08-30).
Motive: Brad asked for the *basis* of the Rocq/Rust-over-Lean/OxCaml recommendation,
three specific gaps: (1) what already exists for multi-agent simulation in Rust on
Tokio; (2) is an agent a Tokio thread/task, and if not, how *is* an agent modelled
in Tokio; (3) the recommendation priced the *cost* of per-operation effects under
OxCaml but never stated the *benefits* of the algebraic effects system. This note
answers all three and then re-runs the ranking test.

Relation: companion to `notes/plumbing-vs-lean-dijkstra-automata.md` (the option
survey) and `notes/mas-abm-foundation.md` (the architecture memo this note
furnishes the evidence for). Claims here are web-sourced, not corpus-grounded
(none of the Rust/Tokio/OxCaml material is ingested; ACM full texts are gated).
Corpus anchors for the capability/effect half remain the four Dijkstra/effekt
works cited in the survey.

---

## 1. The recommendation basis, restated so it can be attacked

What `mas-abm-foundation.md §3–4` actually claims, decomposed into checkable
assertions:

| # | Claim | Checkable content |
|---|---|---|
| B1 | R5 (model↔deployment alignment) best served by Rocq→Rust | One language for sim + deployment; extraction keeps them the same program |
| B2 | Lean→Rust extraction is not first-class | Lean 4 extraction targets C/C++/OCaml/Haskell/Python, no Rust |
| B3 | The Dijkstra/capability formalism is not Lean-locked | "Dijkstra monads for all" mechanised in Coq and F\* |
| B4 | Rust community owns the ABM/MAS scientific stack for heterogeneous behavioral agents | Real frameworks exist (checked in §3) |
| B5 | Borrow-checked capability gate makes bypass a compile error | `CapabilityGate` owns handles; R4 enforced by typing, not runtime |
| B6 | OxCaml's role (fast ticked automaton) is moot in Rust | Rust unboxes/stack-allocates by default; the residual automaton is a small enum+match |
| B7 | Concurrency: Eio fibres ⇒ Tokio tasks | tasks are the cooperative green-thread analogue (checked in §4) |
| B8 | The two real costs: functional-subset extraction + no built-in scheduler tick | acknowledged in the survey §6 |

Claims B1–B6 are static/toolchain facts — established and not re-examined here.
Claims B7–B8 are where §3–§5 of this note add evidence either supporting or
complicating them, plus the OxCaml-benefits asymmetry the recommendation never
balanced (B6's flip side).

---

## 2. Existing Rust / Tokio material for multi-agent simulation (B4)

Two distinct ecosystems, and the distinction matters:

**ABM-scale frameworks (simulation-first, data-parallel, generally NOT Tokio):**

- **Syren** (`AshvinPerera/Syren-ABM-Framework`) — ECS (archetype) storage,
  deterministic stage scheduler over **Rayon**, message specialisations, optional
  GPU (wgpu). Ships a **calibrated macroeconomic model** (multi-market: goods,
  labour, credit, housing; agents: firms/households/banks/central bank/etc.).
  Reproducibility is first-class (byte-identical across thread counts).
- **krABMaga** (formerly Rust-AB) — re-engineers **MASON** in Rust; discrete-event
  simulation, parallel agent scheduling in a step, experiment/parameter-sweep
  runs, Bevy-based visualization, WASM. The "Rust ABM" reference for the MASON
  lineage.
- **swarm_abm** (`docs.rs/swarm-abm`) — spatial ABM (grid/graph/continuous),
  heterogeneous agents via a `MultiAgent` derive macro, **bit-for-bit
  reproducibility even under parallelism** (`decide` phase runs across threads,
  deterministically).
- **rustsim** — "high-performance ABM engine": SoA columnar batch stepping,
  deterministic replay/checkpoint, ensemble/parameter-sweep runner, CUDA/CPU
  compute routing. Built for traffic/crowd/mobility scale.
- **des_cartes** — deterministic discrete-event simulator with a first-class
  **`tokio` runtime-integration feature**, gRPC (tonic), tower, axum.

**Agent-oriented / coordination frameworks (MAS-style, Tokio-aware or actor-led):**

- **Alice Ryhl, "Actors with Tokio"** (`ryhl.io/blog/actors-with-tokio`) — the
  canonical actor pattern: a task owns state, a clonable handle owns an `mpsc`
  sender, messages are an enum, request/response via embedded `oneshot`. Bounded
  channels give backpressure; no `Arc<Mutex>`; natural shutdown on channel close.
- **Assign Onward (blockchain sim)** — builds each **agent as a Tokio task** with
  a role-specific decision loop, communicating through `mpsc` channels in an
  `AgentDirectory`; embeds the *real* protocol server in-process. Direct
  precedent for "deployable agent = tokio task" federating over a real core.
- **multi-agent-engine** (`NickSpyker/`) — lock-free CPU/GPU agent engine;
  dedicated threads per Controller, typed message channels, GPU execute of
  homogeneous agent populations at massive scale.
- **djinn** (`frnsys/djinn`) — distributed ABM: two-phase **decide/update**
  (decide is read-only, updates queued), workers synchronize population state via
  Redis. Demonstrates the distributed-determinism pattern.
- **economic_agents** + **Genesis** — Rust economic-agent stacks: Genesis is a
  deterministic multi-agent economic sim (metabolic costs, Gini, parameter
  sweeps, deterministic replay); the other is AI-agent "economic simulation"
  governance-tooling with async traits. Closest architectural kin to the
  RET×TSSI heterogenous-agent + empirical-validation intent.

**The takeaway for B4:** the ecosystem is *real, current, and actively building
macroeconomic ABMs*, and it is split. The **simulation core is ECS/SOA + Rayon/
GPU + deterministic scheduling — not Tokio and not task-per-agent**. Tokio shows up
where you need **long-lived, autonomous, message-driven agents** (the MAS /
deployment / coordination half). That split is itself the answer to §4.

---

## 3. The agent-as-thread analogy: does it hold?

### The formal literature (BDI concurrency models — Baiardi et al., EMAS 2024 / arXiv 2404.10397)

This is the paper the whole question should anchor on. It formalises "the mapping
between BDI abstractions and the underlying concurrency primitive" as the
**concurrency model** of a MAS framework, and gives a checkable taxonomy:

- **1A1T (one-agent-one-thread):** control delegated to the OS scheduler; the
  interleaving of agent operations is *unpredictable*; "controllability of the MAS
  execution is abysmal"; **determinism is minimal**; active thread count unbounded
  and *degrades* once it exceeds logical processors.
- **AA1T (all-agents-one-thread):** one thread, custom cooperative round-robin
  scheduling of agent steps; renounces parallelism for **controllability,
  determinism, reproducibility** — "a good choice when determinism, reproducibility,
  and predictability are primary concerns; such as in many simulated or time-critical
  scenarios". Constraint: sensing/deliberation/acting must terminate promptly.
- **AA1EL (all-agents-one-event-loop):** FIFO task queue on one event loop;
  conceptually a *fair* AA1T; requires modelling agent activities as tasks.
- **AA1E (all-agents-one-executor):** each atomic operation is a task on a shared
  executor; **agent/action count is decoupled from thread count**; can emulate
  1A1T and AA1EL; finer control of parallelism; "preferable... as the agent count is
  decoupled from the thread count".
- 1A1P (one-agent-one-process): agent control loop genuinely isolated; agents pay
  (de)serialisation for communication.

Their central point: **external concurrency (how control loops map to threads)
constrains the admissible internal concurrency and dominates system properties**
(parallelism, determinism, reproducibility). And one line is a summary verdict:
*"parallelism introduces non-deterministic interleaving of the agent's actions,
undermining predictability and reproducibility, which may be a strict requirement...
such as in multi-agent based simulation."*

### Tokio's own framing

The Tokio docs (`docs.rs/tokio/latest/tokio/task/`) say a task is "similar to an
OS thread, but... managed by the Tokio runtime... another name for this general
pattern is green threads... Go's goroutines, Kotlin's coroutines, or Erlang's
processes." Two further properties matter for agents:

- **Cooperative, not preemptive:** a task runs until it yields at an `.await`.
  A blocking operation in one task stalls the whole worker thread. Tokio provides
  `spawn_blocking` / `block_in_place` for that.
- **`Send` across `.await`:** tasks are the OS-thread analogue only modulo the
  state-carrying discipline.

### So: does the analogy hold?

**It holds at the Erlang level, not the OS-thread level.** "Agent = thread" is the
right shape only if thread is read *loosely*: a schedulable unit of control that
owns its state, communicates by messages, and is cheap to create by the million —
which is exactly Erlang's process, Kotlin's coroutine, and **Tokio's task** (Tokio
explicitly puts itself in that family). The word "thread" in the analogy is doing
injury: **the correct mapping is agent ↔ task (green thread), i.e. the AA1E /
AA1EL pattern, never 1A1T.**

Where the analogy *breaks* (and why the BDI/ABM literature and the Rust sim
ecosystem independently refuse it):

1. **Determinism.** 1A1T hands scheduling to the OS → unpredictable interleaving →
   simulation results stop being reproducible. All the ABM frameworks above make
   deterministic scheduling the headline feature *instead of* OS threads. This is
   not a Rust quirk: it is the 1A1T verdict of §3.1.
2. **Scale.** Hundreds of thousands of agents as OS threads die; as Tokio tasks
   (or ECS rows) they are fine. The analogy's grain is wrong.
3. **Compute vs autonomy.** In an ABM, the agent is mostly *numerics* (per-step
   fitness/market equations) → SoA/ECS batch stepping wins, and a task/thread per
   agent wastes scheduling on tiny slices. In a MAS/implementing system, the agent
   is mostly *autonomous long-lived behavior + coordination* → task-per-agent is
   right. **The ABM cares about throughput+determinism; the MAS cares about
   autonomy+responsiveness.** The same agent, two executions styles.

### How to model an agent in Tokio, then (B7)

Three layers, matching the ecosystem split in §2:

1. **The ABM core: agent-as-data (ECS/SOA + deterministic stage scheduler).** This
   is what Syren/swarm_abm/rustsim do. Agents are rows in columnar arrays; a
   conflict-free stage scheduler (Rayon) runs batch systems over them in a
   reproducible activation order; step = a set of bulk systems. Tokio's role here
   is desk furniture, not the scheduler — determinism comes from the stage
   scheduler (decide/update two-phase, cf. djinn), not from the runtime.
2. **The MAS / implementing agents: agent-as-task (actor pattern).** This is Alice
   Ryhl's actor pattern + §2's precedent. Each agent = `tokio::spawn` of a
   `run()` loop over an `mpsc::Receiver<Message>`; the handle is the public API;
   `Send` attaches a `oneshot` reply channel; bounded channels give backpressure;
   channel-close gives natural shutdown; each task is a panic boundary (an agent
   dying doesn't kill the MAS — the Erlang property, in Rust by construction).
   The *deployed* implementing agents from the foundation memo are this layer.
3. **The capability gate (R4): sits between them.** The gate owns the
   resource handles; both the ABM stepping *and* the actor tasks reach the world
   only via `gate.perform(...)` which ticks the enforcement automaton first —
   bypass is a compile error. This is B5/B6: the "automaton" is a small enum+match,
   and it threads through *both* execution styles.

So the recommendation's "fibres ⇒ tasks" (B7) is right but crude: in the sim core
it is **agents-as-data**, in the coordination layer it is **agents-as-tasks**, and
the two share the gate. That is a more honest picture than "many Tokio tasks
coalesced from Eio fibres", and it *strengthens* the Rust choice for a heterogeneous-
agent economic ABM (the sim core wants ECS + Rayon determinism far more than it
wants green threads).

---

## 4. The missing half: what OCaml 5 / OxCaml algebraic effects actually buy you

The survey priced per-operation-effect enforcement as a *cost* to be optimised
away (unbox+stack-allocate the automaton) and then dismissed OxCaml's role as
moot under Rust codegen (B6). That is the correct *narrow* reading, but it skips
what the effects system is **for** — the benefits half, which is exactly the
proposal's architectural spine:

1. **Direct-style concurrency (no monad).** OCaml 5 effect handlers let concurrent
   code be written in the same style as plain code — real stacks and real
   backtraces, `try ... with` and the rest of the language work in concurrent code.
   Eio exists because of this; the OCaml effect tutorial and Eio 1.0 both state the
   three concrete advantages: performance (no heap-simulated stack), direct style,
   language features working in concurrent code. (Sources: ocaml.org/manual/effects,
   ocaml-multicore/eio, tarides.com blog.)
2. **Schedulers become libraries.** Because effect handlers expose delimited
   continuations, a concurrency primitive is *user code*, not VM machinery — Eio
   (direct-style IO), Domainslib (nested parallelism), a custom cooperative
   scheduler, or — the proposal — **a ticked automaton inside the effect handler**.
   The compiler does not hardcode "thread". This is *the* feature the proposal
   leans on: the handler *is* the interception point.
3. **Composability of schedulers (research layer).** Ande & Sivaramakrishnan,
   "Composing Schedulers using Effect Handlers" (OCaml 2022), built scheduler-
   agnostic MVars/channels by agreeing on a single Suspend/Resume convention, so
   Eio + Domainslib tasks interoperate instead of re-splitting the ecosystem the
   way Lwt/Async did. The design pressure toward Picos continues this. Practical
   upshot: several schedulers (IO, parallel, and the automation ticking the
   automaton) can coexist in one process.
4. **Effects-as-capabilities — the semantic match.** This is the loaded one:
   the proposal *is* the Effekt/CPS line. "Effects as capabilities"
   (Brachthäuser et al., ICFP 2020, in-corpus) reads effect types as *the
   capabilities a computation requires from its context*; "What You See Is What
   You Get: practical effect handlers in capability-passing style" (Schuster,
   Brachthäuser, Ostermann, ESOP 2021) shows handler implementations can be
   passed explicitly, giving lexical reasoning about effects. **In this reading,
   a capability signature is not something bolted on — it is the effect system's
   native type.** The enforcement automaton ticked in the handler is the runtime
   half of exactly that semantics. Rust has no such native notion; the gate is a
   re-invention (see §5's rebalance).
5. **Efficient handlers (research layer).** "Effect Handlers, Evidently" (Xie et
   al., ICFP 2020) proves an *evidence translation* (handler implementations passed
   down, dict-style, like typeclass dictionaries) with scoped resumptions,
   opening the way to efficient handler compilation — the "automaton tick is cheap"
   story has a published mechanism, not just an OxCaml implementation hope.
6. **OxCaml's performance substrate** (Jane Street blog, oxcaml.org) — because
   B6 argues Rust makes OxCaml's fast path moot, the precise claims deserve a fair
   read: OxCaml = Jane Street's production OCaml branch (Flambda2; stack allocation
   with the `stack_` keyword and locality modes; **unboxed types** incl. SIMD-holding
   unions; a kind system; fearless concurrency / race checking). Its whole purpose
   is *performance engineering in OCaml*: deterministic allocation, cache efficiency,
   zero-GC fast paths. For the proposal it is the thing that lets the ticked
   automaton live unboxed/stack-allocated in the hot path *without* leaving the
   language the spec is written in — which is the deeper reason Lean chose OxCaml
   (one language, spec → extraction → fast residual, no second runtime).

**The honest one-line benefit the recommendation under-stated:** effects are not
only a performance problem; they are the *semantics* (capability signatures as
effect types) and the *mechanism* (handler = guaranteed interception point,
scheduler-as-library, evidence translation) of the whole proposal. Losing them in
Rust is losing the native form of the core idea, not just "no effect handlers".

---

## 5. Rebalance: does the recommendation survive this evidence?

Each missing piece changes the ranking test, but the ranking holds — with the
trade exposed honestly:

- **§2 (ecosystem) supports B4 and refines it.** Rust owns the *ABM core* (ECS/SOA,
  deterministic schedulers, macro models) — exactly what the foundation memo's
  Track C/E (heterogeneous-agent microfoundation, simulator) need. But it also shows
  the sim core is *Rayon/ECS*, not Tokio: B7's "fibres ⇒ tasks" should be read as
  "fibres ⇒ (ECS systems in the core; tasks in the coordination layer)", which the
  memo already implied under R1/R2.
- **§3 (agent-as-task) supports B7 conditionally and strengthens the Rust case for
  the ABM.** The correct mapping is agent ↔ task/green-thread (AA1E/AA1EL), never
  OS-thread (1A1T); the BDI literature and the Rust ecosystem independently
  converge on "deterministic batch / executor scheduling, not per-agent OS
  threads". A heterogeneous-agent economic sim is carried better by ECS+stage
  scheduler than by green threads — so the *sim* half of the recommendation is
  *more* right than the survey said.
- **§4 (effects benefits) is the real counterweight to B6.** The Rust variant
  does NOT carry over: native capability-signature typing, handler-as-interception-
  point, evidence-translation efficiency, or scheduler-as-library. It must rebuild
  them as: `CapabilityGate` (a re-invention of the CPS/capability-passing idea,
  enforced by type privacy + borrow checking rather than by effect typing),
  discipline-based tick points, and a monolithic runtime. That is a genuine,
  named cost — and it is the "second-certificate" problem's semantic cousin: Rust
  moves enforcement from *effect semantics* to *ownership discipline*, and
  ownership discipline is exactly what Kani/Verus/Creusot would then be certifying.

Why it still ranks 1 (Rocq→Rust) over 2 (Lean→OxCaml) for this purpose:

1. The R5 goal (model = deployment) is *the* core requirement; it is met only by
   a platform whose language is also the runtime (Rust) or by extraction into it
   (Rocq→Rust). Lean 4 → OxCaml keeps OCaml as a second language in the alignment
   loop, and Lean→Rust is not first-class (B2), which is the original and still
   the decisive wedge.
2. §2 shows the ABM half Rust genuinely leads; §3 shows the concurrency question
   resolves *in Rust's favour* for the sim core.
3. §4 is the strongest argument *against* Rust — but its benefits are OCaml-language
   effects, and adopting OCaml reintroduces a third language into R5 and reopens the
   scientific-stack gap that already ranked the OCaml host bottom in the memo
   (option B weak on R1/R2). The proposal's *own* premise (OxCaml/Eio enforcement)
   could be ported to plumbing/OCaml later as a protocol+gate service — but for the
   ABM/MAS platform the ranking stands.

**Recommendation as refined by this note (things to change in the memo's §6):**
state B7 correctly ("ECS agents in the sim core + task agents in the MAS layer,
sharing the capability gate", citing §3's taxonomy and the Rust-ABM ecosystem);
record §4 explicitly as the known, accepted cost ("Rust re-implements capability
passing as a borrow-engineered gate; OCaml-effect semantics not carried over") —
turning a hidden asymmetry into a recorded decision.

---

## 6. Open questions this note leaves

- Where the capability-dimension matters *most* (implementing MAS, §3.2): does a
  verified gate over TCP (protocol-level, cf. plumbing's session-morphism seam)
  recover the "handler = interception point" guarantee that OCaml effects give
  in-process? This is the build-vs-adopt question already deferred in the memo.
- Whether any Rust ABM framework's determinism guarantee (Syren/swarm_abm) holds
  when *deployed* agents (tasks) drive *simulated* agents (ECS rows) through the
  same gate — i.e. does the decide/update abstraction survive the mixed model.
- The macro model in Syren (calibrated multi-market) is a candidate *sanity-check
  baseline* against RET×TSSI Track E expectations — worth probing for empirical
  regularities it encodes (Zipf/Laplace), as the memo's R2 asks.

## Sources

- BDI external-concurrency taxonomy: Baiardi, Burattini, Ciatto, Pianini, Ricci,
  Omicini, "On the External Concurrency of Current BDI Frameworks for MAS",
  EMAS 2024 / arXiv:2404.10397; full version
  `emas.in.tu-clausthal.de/2024/assets/papers/EMAS_2024_paper_14.pdf`
- Syren ABM framework: `github.com/AshvinPerera/Syren-ABM-Framework` (+ macro-
  economy example, `docs.rs/crate/syren`); krABMaga: `github.com/krABMaga/krABMaga`;
  swarm_abm: `docs.rs/swarm-abm`; rustsim: `docs.rs/rustsim`; des_cartes:
  `docs.rs/des-cartes` (tokio feature)
- djinn (distributed ABM): `github.com/frnsys/djinn`; multi-agent-engine:
  `github.com/NickSpyker/multi-agent-engine`; Assign Onward (agents as Tokio
  tasks): `mangocats.com/ao/RustBlockchainSimulator.html`; economic agents:
  `github.com/AndrewAltimit/template-repo`; Genesis (deterministic economic sim):
  `github.com/FTHTrading/Genesis`
- Tokio task docs (green threads, cooperative scheduling): `docs.rs/tokio/latest/tokio/task/`
- Actor pattern: Ryhl, "Actors with Tokio", `ryhl.io/blog/actors-with-tokio/`;
  Rust Cookbook actor recipe
- OCaml 5 effect handlers: `ocaml.org/manual/5.4/effects.html`; tutorial
  `github.com/ocaml-multicore/ocaml-effects-tutorial`; Eio: `github.com/ocaml-multicore/eio`,
  Tarides "Eio 1.0" blog (2024-03-20)
- Scheduler composition: Ande & Sivaramakrishnan, "Composing Schedulers using
  Effect Handlers", OCaml 2022, `kcsrk.info/papers/compose_ocaml22.pdf`
- Effects as capabilities: Brachthäuser, Schuster, Ostermann, ICFP 2020,
  DOI 10.1145/3428194 (**in corpus**: `openalex/https_openalex.org_W3107145433`);
  Schuster/Brachthäuser/Ostermann, "What You See Is What You Get: practical
  effect handlers in capability-passing style", ESOP 2021
  (`doi.org/10.1007/978-3-030-83128-8_3`)
- Efficient handlers: Xie, Brachthäuser, Hillerström, Schuster, Leijen, "Effect
  Handlers, Evidently", ICFP 2020 (`xnning.github.io/papers/icfp20evidently.pdf`)
- OxCaml: Jane Street "Introducing OxCaml" (2025-06), `blog.janestreet.com`;
  `oxcaml.org` (unboxed types, stack allocation, kinds, modes docs)
- Note-internal grounding: the four Dijkstra/effect corpus works and plumbing's
  verification corpus (`notes/plumbing-vs-lean-dijkstra-automata.md`)