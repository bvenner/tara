# Plumbing vs. the Lean-Dijkstra-Automata proposal — a grounded comparison

Status: research note (2026-08-29).
Source documents: the proposal **"Compiling Lean specifications into OxCaml
enforcement automata"** (Anil Madhavapeddy, 2026-08-01,
`anil.recoil.org/ideas/lean-dijkstra-automata`), plumbing's verification corpus
(`~/tools/plumbing/doc/`, `proof/`, `tla/`), and four works ingested into this
repository's corpus.

Corpus grounding: claims about the Dijkstra-monad / capability literature are
cited to the OpenAlex records below (each is a "work" node in the hypergraph,
queryable via `query` / `trace`). Claims about plumbing are cited to files in
the plumbing source tree, which is **not** part of this corpus.

## 1. The proposal in one paragraph

A capability-safe replacement for Unix-style pipeline wiring. Each agent's set
of reachable effects is expressed as a **capability signature** built on a
**Dijkstra monad** — an indexed monad whose index is a weakest-precondition
structure, so effect reachability is a logical object, not a runtime guess. The
spec is written once, in Lean 4, and compiled to three artefacts: (1) proof
obligations discharged statically, (2) a **residual enforcement automaton**
(OxCaml) for the obligations that cannot be be decided statically, and (3) a
Lean proof that the automaton refines the spec — every trace the automaton
accepts satisfies the predicate transformer, every violating trace is rejected.
Enforcement is integrated into the runtime by ticking the automaton from Eio's
effect handlers on every IO operation. Policies are composable across layers
(filesystem, parser, socket) by connecting each layer's capability signature.

## 2. Corpus anchors (new, ingested 2026-08-29)

| Work | Corpus doc | What it supplies to the argument |
|---|---|---|
| Dijkstra monads for free (Ahman et al., POPL 2017) | `openalex/https_openalex.org_W2507710874` | Dijkstra monads enable a dependent type theory to specify and verify effectful code via weakest preconditions; derivable "for free" by CPS-translating the underlying monadic effects (F*/EMF* provenance). |
| Dijkstra monads for all (Maillard et al., ICFP 2019) | `openalex/https_openalex.org_W2919561213` | General framework: Dijkstra monads indexed by a **specification monad**; any monad morphism computational-monad → specification-monad yields one; spec monads built by monad transformers over predicate transformers / Hoare pre-post. **Implemented in Coq and F\*.** |
| Dependent types and multi-monadic effects in F\* (Swamy et al., POPL 2016) | `openalex/https_openalex.org_W2267469130` | F*: each primitive effect (state, exceptions, divergence, IO) carries a monadic predicate-transformer semantics; weakest preconditions computed and discharged by SMT + manual proofs; pay-as-you-go. The verified-TLS baseline. |
| Effects as capabilities (Brachthäuser, Schuster, Ostermann, ICFP 2020) | `openalex/https_openalex.org_W3107145433` | Effect types re-read as the **capabilities a computation requires from its context** (Effekt), with second-class functions and capability-passing semantics — the "capability signature not effect declaration" semantics the proposal's Bastion notion builds on. |

Queried this session (verified present): `dijkstra monads` → both POPL/ICFP works
+ keyword nodes; `effect handlers` / `capabilities` → the Effekt work (the only
"capabilities"-labelled node in the graph); `F*` → the multi-monadic work.

The two works that anchor the *enforcement* half of the proposal are **not** in
OpenAlex and are cited by URL only: Bastion (HOPE 2024) and Eio 1.0. The
TU Wien / Brachthäuser "Effects as capabilities" anchor is in.

## 3. Plumbing's verification stack today

Plumbing already runs a verification track parallel to the proposal's vision,
with three concrete evidence kinds (per `~/tools/plumbing/doc/runtime-semantics-and-verification.md`):

1. **Proof-owned compiler seams** (Coq, extracted to live OCaml). The HM type
   inference oracle used by the compiler is proof-owned end-to-end on the
   supported fragment, and the session-type → plumbing-morphism translation is a
   proof-owned seam on the live path (`doc/compiler-verification-status.md`).
   Extraction is real: `proof/*.v` → `proof/extracted/*.ml{,i}` → wired in —
   the "model/code don't drift" property, achieved for the compiler.
2. **A layered TLA+ corpus** for runtime semantics at explicit observation
   boundaries (operator laws, runtime refinements, theorem-side waypoints),
   checked by TLC, with a `tla/SYNC.md` evidence ledger. Crucially, the doc is
   explicit that the TLA corpus states what the runtime *should* do — it is a
   *specification beside* the code, not compiled into it.
3. **Boundary type-checks at load time.** JSON crossing a channel is shape-checked
   at the boundary; `exec` workers additionally validate requests against
   pydantic contracts (`scripts/schemas.py`). This POC's pipelines lean on this.

Honesty boundary (from plumbing's own docs): the full session-compiler functor
theorem remains the long-range goal; wrapper/desugaring policy sits above the
extracted seam; the running OCaml is the source of truth when specs and code
diverge.

## 4. Mapping proposal → plumbing, and the gaps

| Proposal element | Plumbing equivalent | Gap (what plumbing does not give you) |
|---|---|---|
| Capability signature (effect reachability) as a type-level object | Channel shape types; worker effect vocabulary implicit in `exec` commands | Shapes, not effects. Nothing states *which* effects an agent may perform. |
| Static proof obligations from the spec | Load-time boundary checks (shape only) | No proof obligations; refusal is shape refusal, not property refusal. |
| Residual enforcement automaton, extracted from the spec | TLA corpus states laws; load-time checks enforce shape | TLA is **offline** (TLC), not extracted into the running runtime. Shape is enforced, properties are not. |
| Refinement proof: automaton ⊨ spec | Coq proof that the compiler seam maps linear sessions to plumbing morphisms | Soundness of the *enforcement boundary* (does the runtime monitor refine the stated law?) is unstated. |
| In-runtime policy monitor (Eio effect handlers) | Morphism-level JSON validation / runtime tests | No scheduler-level per-operation policy tick. |
| Cross-layer information-flow policies (fs/parser/socket) | Single-layer JSON transforms between workers | No relation between one layer's effects and another's. |
| Proof assistant | Coq (compiler seam) + TLA+/TLC (runtime) | Lean 4 specifically; Coq/L/TLA triple survives, no Lean interop yet. |

The sharpest contrast: plumbing's philosophy *is* the proposal's — explicit
architecture, type-checked boundaries, no model/code drift — but plumbing holds
the line at **shape**, and its runtime model (TLA) is a *companion spec*, not an
executed artefact. The proposal crosses the line into **effect/capability
semantics** and ties the spec to the runtime by construction (proof-producing
extraction), which is the one drift-plug plumbing's TLA line deliberately does
not claim.

Complementarity in one sentence: plumbing is **ahead of the proposal on compiler
correctness** — it already does proof-producing extraction from a Coq spec into
the live compiler — while the proposal is **ahead on security semantics** —
capability signatures, an enforcement-refinement certificate, and cross-layer
policies that plumbing has no analogue for. The gap column reduces to three
enforcement heights: **load time** (static shape, plumbing), **channel
boundary** (dynamic shape refusal, plumbing), and **per-operation** (effect /
capability policy — the proposal's target; inside unverified `exec` children
this is reachable only at the OS boundary, see §5). The F*/Steel-adjacent
reference "Securing Verified IO Programs Against Unverified Code" (§7) is the
closest published statement of exactly this split — verified host, unverified
children, proof-ruled boundary.

### Glossary (the gap column's vocabulary)

- **Shape** — the syntactic/data form of a value crossing a channel: `{concept:
  string}` has exactly this field set, `total_edges` is a number. Decidable,
  needs no semantics; says nothing about what anyone *does*, only what flows.
  Plumbing checks shapes at load time and at boundaries (`input_type_mismatch`).
- **Effect** — an operational capability an agent can perform in the world: read
  a file under `/data`, contact OpenAlex over the network, write `graph/`, spawn
  a process. Channel types describe the JSON a worker accepts, not the side
  effects it may execute — plumbing's `exec` workers perform effects, but nothing
  declares or restricts them.
- **Property** — a logical claim about behavior, expressed as a predicate /
  weakest precondition / Hoare-style assertion, e.g. "no raw file bytes ever
  cross the socket". The correctness layer: truths that must hold over
  executions, discharged as proof obligations. A property can *mention* effects,
  but is a statement about behavior, not a capability.
- **Compiler seam** — a deliberate cut-point where one implementation meets
  another along a stable interface. A *proof-owned* seam is one generated from a
  theorem rather than handwritten; plumbing's canonical seam is
  `Language.Session_contract.plumbing_morphism_image_of_session_type`, extracted
  from `proof/SessionEndpointLinearMorphismImage.v` into the live compiler, so
  the Coq model and the OCaml code cannot drift at that boundary. Seams cover
  compilation; the runtime's *enforcement boundary* has no such extracted
  artefact.

Example from the POC tying the three together: `query.plumb`'s shape is
`{concept: string}`; its effects are "read hypergraph.json, no network, no
writes"; a property one might verify is *"total_edges = 0 iff no hyperedge
contains the concept"*. None of the three is implied by the others.

## 5. Where capability verification could attach to this POC

The micro-scale mirror of the proposal's static/dynamic split, at the existing
`exec` worker boundaries:

1. **Declare a capability automaton per worker** — the set of effects the worker
   may perform (e.g. `read: corpus/**`, `write: graph/**`, `net: openalex`), as
   plumbing already types the boundary shape.
2. **Specify the acceptance policy in TLA** (reusing the existing `tla/` corpus
   idiom): a state machine whose states are "permitted effect sets per worker".
3. **Check statically at load time** (mirrors the load-time boundary check): a
   `check`-side pass refuses a pipeline whose wired-in `exec` effects are outside
   the worker's declared capability set — the analogue of discharging the static
   obligation.
4. **Dynamic refusal** (the residual-automaton half): at the `exec` boundary,
   refuse an operation whose effect is not in the automaton's current state —
   mechanically the same refusal plumbing already performs for shape, upgraded
   from `input_type_mismatch` to `capability_denied`.

A coarse first cut needs no new machinery: the effect vocabulary is enumerable
from the existing pipeline definitions (`pipelines/*.plumb`), and the TLA module
can be TLC-checked (`~/tools/plumbing` gate: `nix develop .#tla -c make -C tla
check-fast`). It will not reach the proposal's refinement-certificate bar, but it
establishes the *seam* where a real (Lean/Coq) certificate would land.

### Embedding `exec` workers as in-host fibres

Today only the `exec` morphism is a subprocess: `forward_exec`
(`~/tools/plumbing/lib/fabric/inline.ml:943`) calls `Unix.create_process_env` and
bridges ZMQ ↔ Unix pipes. Everything else — `id`, `copy`, `merge`, `barrier`,
`map`, `filter`, … — is already an in-host Eio fibre ("reading from PULL sockets
and writing to PUSH sockets", inline.ml:4-5). Embedding a worker means turning
that spawn into a fibre like the operators, which imposes one rule:

> a fibre is a schedulable unit inside the host process; worker code runs as a
> fibre iff it executes in the host's address space **and** every blocking
> operation routes through an Eio effect. Direct syscalls stall the whole
> single-domain scheduler and are invisible to any enforcement automaton.

Does the worker need to be OCaml? Not necessarily — but effectively yes for the
real (per-operation enforcement) benefit:

1. **Native OCaml worker** — the zero-extra-runtime route: link it as a
   `lib/` module and `Eio.Fiber.fork` it like the structural operators; policy =
   a wrapper fibre ticked on each send/recv. Requires the worker logic to be
   OCaml (or compiled into the host via a Dune library; C stubs cannot yield).
2. **WASM worker** (Rust/C/… → `.wasm`, loaded via a wasm runtime linked into
   the host) — non-OCaml is possible here: wasm memory is already sandboxed and
   its I/O must pass through host-provided *imports*, which you implement as the
   plumbing transport. That is both an isolation boundary and a tickable seam.
   Costs: interpreter overhead; wasm-execution blocks the fibre unless sliced.
3. **Embedded scripting DSL** — precedent already exists: `map`/`filter`
   expressions run a non-OCaml expression language in-host (`Expr.eval`,
   inline.ml:621). A richer statements-and-effects DSL extends the same idea.
4. **Python (or similar) in-process** — linking libpython into the host is
   technically possible, but the GIL and blocking semantics fight Eio's
   cooperative single-domain scheduler: pure-Python code has no yield points and
   real I/O bypasses the transport. It lands on an OS thread anyway, which
   re-introduces a process-like boundary — nothing gained over today's subprocess.

Verdict: full per-operation enforcement needs the worker on the host's fast
path, which means **OCaml, a tiny embedded DSL, or WASM-hosted code**. Heavy
workers (the POC's docling `fulltext` case) stay subprocess `exec` and get
capability enforcement at the **OS boundary** (seccomp/Landlock) instead of the
Eio seam. This is why the proposal pairs OxCaml (fast OCaml codegen) with Eio:
the ticked automaton and the worker share one process and one scheduler.

## 6. Feasibility and risk

- **Proof assistant alignment**: the proposal's spec side is Lean 4; plumbing's
  proof line is Coq and its runtime model is TLA+. "Dijkstra monads for all" is
  mechanised in *both* Coq and F*, so the abstract-Dijkstra index is not locked
  to Lean — a Coq pathway exists if interop with plumbing's `proof/` line
  matters more than adopting Lean.
- **Corpus/grounding gaps**: Bastion (HOPE) and Eio 1.0 are not OpenAlex-indexed;
  ACM full texts are publisher-gated, so grounding is abstract-level only. The
  theory spine (the two Dijkstra-monad papers, F*, Effekt) is fully represented.
- **Enforcement substrate**: the proposal's dynamic half assumes OCaml 5 effect
  handlers (Eio). Plumbing's *host* runtime already runs on Eio — `bin/plumb`
  (`lib/plumb/run.ml` after Eio_main at line 602) drives the fabric with Eio
  fibers/promises/streams, ZMQ transport pumps yields to the scheduler
  (`lib/transport/transport_zmq.ml:393`), HTTP/TLS is cohttp-eio (`doc/networking.md`)
  — so the tick seam exists in principle. What plumbing lacks is a *per-operation
  policy hook* on it: the host sees only messages crossing boundaries, while
  `exec` child internals are opaque (see §5 "Embedding `exec` workers as
  in-host fibres"). Retrofitting that hook is the real engineering cost.
- **LLM-written specs**: the proposal's stretch goal (an LLM writes the Lean)
  mirrors this POC's division of labour — the LLM synthesises, the mechanical
  layer verifies. In the POC today the mechanical layer is shape; the proposal's
  version is property. Same shape of trust boundary, stronger bar.

### Decoding the proposal's enforcement paragraph

> *"Each IO operation performed by an Eio fibre passes through a handler, so we
> could embed an automaton that can be ticked on each operation by the
> scheduler itself. OxCaml then earns its place on the fast path as it can be
> used to unbox and stack-allocate it so that a state transition is fast."*

Three chained claims — the proposal's "safety for free" story:

1. **Guaranteed interception point.** An Eio fibre never calls the OS directly:
   every I/O is an *effect* that suspends the fibre and transfers control to a
   handler owned by the Eio scheduler (which does the actual syscall via
   io_uring/epoll). The handler is the one road between the fibre and the OS —
   enforcement placed there cannot be skipped, because there is no other door.
   (A fibre deliberately bypassing with raw `Unix` is off the sanctioned path —
   precisely what the capability signature is meant to forbid.)
2. **Enforcement moved into the runtime.** Put the state machine inside the
   handler: on every operation run `(state, op) → (state', allowed?)`; allowed ⇒
   perform the I/O, remember `state'`; not allowed ⇒ refuse. "Ticked by the
   scheduler itself" = the check is structural, not a library you must remember
   to call.
3. **Make the tick nearly free (OxCaml).** Per-operation checking is only
   affordable on the hot path if it costs almost nothing. OxCaml compiles the
   automaton *unboxed* (state in machine words/registers, not behind a heap
   pointer) and *stack-allocated* (no GC), so a transition is a compare, a
   branch, a store — nanoseconds. Safety tax ≈ zero, forever.

Mapping to what this POC / the Rust variant can and cannot inherit:

- **Interception point:** plumbing has the channel-boundary analog (every
  message crosses a morphism, `Validate.check`) — but shape-only, per-message,
  not per-operation inside a worker.
- **Enforcement into the runtime:** Tokio has no effect handlers, so claim 1
  must be *rebuilt by construction* — a gate that owns the handles, so the tick
  happens at `gate.perform` and bypass is a compile error (see below).
- **Fast transition:** Rust's codegen already unboxes/stack-allocates by
  default, so the "OxCaml role" disappears in the Rust variant.

### Rust + Tokio variant (collaborator direction, 2026-08-29)

Brad's collaborator works in Rust; assumed verification stack:
**Rocq Rust Extraction** (`github.com/AU-COBRA/coq-rust-extraction`, AUC
Annenkov / Milo / Botsch Nielsen / Spitters, MIT, Rocq ≥ 9.0, MetaRocq-based,
used in ConCert) instead of OxCaml, and **Tokio** instead of Eio. Verdict:
feasible, and for the *enforcement* half arguably a better fit; two real costs.

- **Proof language: re-target Lean 4 → Rocq (Coq).** Lean 4 has no first-class
  Rust extraction backend (targets: C/C++/OCaml/Haskell/Python), whereas
  Rocq→Rust extraction is published and used. "Dijkstra monads for all" is
  already mechanised in Coq, so the capability-signature (abstract-Dijkstra)
  reasoning transfers without loss — and aligns with plumbing's existing `proof/`
  Coq line (§6's Lean interop risk disappears in this variant).
- **Three artefacts, plumbing's pattern, Rust target:** (a) static obligations
  discharged in Rocq; (b) the residual automaton — a pure `(state, op) →
  (state', decision)` transition — extracted to Rust by the plugin (exactly the
  functional shape it handles, its smart-contract niche); (c) the refinement
  proof in Rocq. Same "proof-owned seam" structure plumbing uses, target
  OCaml→Rust.
- **Enforcement seam by construction, not by scheduler.** Eio ticks the
  automaton structurally because every IO op passes through an effect handler.
  Tokio has no effect handlers, so the seam is enforced *by grace of the type
  system*: a `CapabilityGate` owns the `TcpStream`/`File` handles; workers reach
  IO only via `gate.perform(Op::WriteFile, …)`, which runs the automaton check
  first. The raw handles are private and only reachable behind `&mut Gate`, so
  bypassing the tick is a *compile error* — the Dijkstra "commands are the only
  reachable effects" property realised in the type system. The OxCaml
  fast-path/stack-allocation argument is moot: a small extracted enum + match is
  already on Rust's fast path.
- **Concurrency: fibers ⇒ tasks.** Eio fibers become Tokio tasks; `Send`
  obligations across `.await`, `spawn_blocking` for CPU/blocking workers
  (docling-class), `CancellationToken` for shutdown. Single-owner policy design
  avoids locks: one policy task owns automaton state; workers post op-requests
  over channels and the policy task performs the IO — structurally symmetric to
  plumbing's `exec` boundary.
- **Cost 1 — extraction yield is functional-subset only.** The async glue, the
  gate, and Tokio IO are handwritten Rust, exactly as plumbing hand-writes the
  runtime-authoritative OCaml above its extracted seam
  (`doc/compiler-verification-status.md`). Refinement is certified for the
  automaton, not for the gate; closing that needs a *second* certificate
  (Kani/Verus/Creusot for the Rust glue) — a two-verification-stack problem the
  Eio/Lean single-language world does not have.
- **Cost 2 — no built-in scheduler tick.** The Tokio gate is assembled and
  enforced by discipline + type privacy, not provided by runtime structure. It
  is stronger once built, but it is yours to build.
- **Heavy workers unchanged:** subprocesses (`tokio::process::Command`) with
  OS-boundary capabilities (seccomp/Landlock), per §5's verdict.

## 7. Sources

- Proposal: https://anil.recoil.org/ideas/lean-dijkstra-automata
- Bastion (capability signatures via abstract Dijkstra monads): https://anil.recoil.org/papers/2024-hope-bastion
- Eio 1.0: https://anil.recoil.org/papers/2023-ocaml-eio
- Why a sandbox that is just a shell wrapper isn't sufficient (Anil's note; the
  motivation for the capability/OS-boundary gap here — bound to the POC's
  subprocess-`exec` reality): https://anil.recoil.org/notes/claude-copilot-sandbox
- Securing Verified IO Programs Against Unverified Code in F* (Andrici et al.,
  POPL 2024, DOI 10.1145/3632916) — the verified-host / unverified-children
  boundary; cited here by URL, not ingested into the corpus
- Rocq Rust Extraction (AU-COBRA): https://github.com/AU-COBRA/coq-rust-extraction
  — Coq→Rust extraction plugin (MetaRocq); the assumed verification stack for
  the Rust + Tokio variant (§6); companion paper "Extracting functional programs
  from Coq, in Coq" (10.1017/S0956796822000077)
- Plumbing: `~/tools/plumbing/README.md`, `doc/compiler-verification-status.md`, `doc/runtime-semantics-and-verification.md`, `proof/`, `tla/`
- Plan-mode analysis: `to_human/` context is the conversation history; this note supersedes the inline comparison made prior to ingestion.