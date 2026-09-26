# Context Preservation — 2026-08-29 (lean-dijkstra / plumbing / MAS-foundation session)

Session-local context for resumption after compaction/reset. **Read this first
if you resume this thread.** Tie-in to the broader workspace: repo-root
`AGENTS.md` and `to_human/2026-08-23-context-preservation.md` remain the general
entry points.

---

## What this session produced

1. **New grounded note** (the deliverable):
   `projects/knowledge-repository-poc/notes/plumbing-vs-lean-dijkstra-automata.md` —
   compares the Lean-Dijkstra-automata proposal
   (`https://anil.recoil.org/ideas/lean-dijkstra-automata`, Madhavapeddy 2026-08-01:
   capability signatures as Dijkstra monads, spec→proof+automaton extraction,
   Eio/effect-handler enforcement) against plumbing's actual verification stack.
   Contains: proposal summary; corpus anchors; plumbing's Coq/TLA/runtime evidence
   kinds; a mapping+gap table; **glossary** (shape / effect / property / compiler
   seam); where capability verification could attach to the POC; the **in-host
   fibre-embedding** analysis; feasibility/risk; **§6 Rust+Tokio variant**.
2. **Architecture memo** (second deliverable):
   `projects/knowledge-repository-poc/notes/mas-abm-foundation.md` — foundation
   decision linking all three projects for the larger goal (a **democratic
   economic planning** tool: ABM platform simulating plan futures on a local
   digital twin + MAS implementing plans + twin-as-MAS + ABM↔MAS alignment).
   Ranking: **Rocq→Rust/Tokio** = ABM/MAS platform (alignment by construction,
   performance, borrow-checked capability gate, Rocq-extracted certified core);
   **plumbing** = coordination/protocol + knowledge-wiring layer; **Lean→OxCaml**
   = superseded here, role migrates to Rocq→Rust. Includes thread-composition
   diagram and RET×TSSI Track C/E/F role mapping.
3. **Corpus growth:** 4 OpenAlex works ingested via `expand` (mode `doi`):
   - Dijkstra monads for free (10.1145/3009837.3009878)
   - Dijkstra monads for all (10.1145/3341708)
   - Dependent types and multi-monadic effects in F\* (10.1145/2837614.2837655)
   - Effects as capabilities / Effekt (10.1145/3428194)
   Graph rebuilt (`--force`): external works 29→33; **no REPORT.md edit** (per
   Brad's instruction — keep REPORT until asked).
4. **Documented gotcha:** `expand` boundary requires all four of
   `mode/topic/limit/doi` (pydantic defaults ≠ boundary defaults) — added to
   `plumbing-setup.md`.

## Key context-only findings (not derivable from the notes alone)

- **Plumbing's host runtime already runs on Eio.** `bin/plumb` =
  `Eio_main.run`/`Eio.Switch` on a dedicated thread (`lib/plumb/run.ml:602`);
  ZMQ transport pumps socket events into an `Eio.Stream` from a forked fibre
  (`lib/transport/transport_zmq.ml:393`); HTTP/TLS = cohttp-eio
  (`doc/networking.md`). The mismatch with the proposal is therefore not "no
  Eio" but "no per-operation policy hook", and `exec` child internals are opaque
  (they are `Unix.create_process_env` subprocesses, `lib/fabric/inline.ml:943`).
- **Plumbing's verification tower (three evidence kinds):** Coq proof-owned
  compiler seams extracted to live OCaml (HM oracle + session morphism image via
  `Language.Session_contract.plumbing_morphism_image_of_session_type`);
  layered TLA+ corpus for runtime semantics (**offline**, TLC-checked, a
  *companion spec* that may drift from the OCaml); load-time boundary
  shape-checks. Docs: `~/tools/plumbing/doc/compiler-verification-status.md`,
  `runtime-semantics-and-verification.md`, `tla/README.md`.
- **To embed an `exec` worker as an in-host Eio fibre** the code must run in
  the host address space *and* route all blocking I/O through Eio effects.
  Feasible: native OCaml (zero cost), WASM-hosted (non-OCaml, tickable imports),
  tiny embedded DSL already precedented (`Expr.eval` for `map`/`filter`). Not
  feasible in practice: Python (GIL vs cooperative single-domain scheduling).
  Heavy workers (docling `fulltext`) stay subprocesses → capability enforcement
  must then be at the **OS boundary** (seccomp/Landlock).
- **Why the proposal picked Lean over Coq/F\***: not because the Dijkstra
  formalism is missing in Rocq — it is already there (Maillard et al. mechanised
  in Coq + F\*); the choice is toolchain: Lean's default C codegen (fast native
  residual automaton), the LLM-proving wave is Lean-centric (the proposal's
  stated stretch goal), DSL ergonomics, and ecosystem mindshare. F\* is the true
  native home of Dijkstra monads — and the proposal still chose Lean → ecosystem
  bet, not theorem-library bet. This reverses for the Rust variant: Rocq wins
  because Lean→Rust extraction is not first-class and Rocq→Rust extraction is
  published.
- **Conceptual scaffold** (earlier in-conversation answers): Dijkstra ≡ indexed
  monad over predicate transformers; graded ⊂ indexed; the "three enforcement
  heights" = load-time / channel-boundary / per-operation; plumbing ahead on
  compiler correctness, the proposal ahead on security semantics. OxCaml's
  "whole point" = unbox + stack-allocate the ticked automaton so per-op checks
  are ns-cheap; the proposal's enforcement paragraph is claims 1 guaranteed
  interception point (effect handler) → 2 tick in the scheduler → 3 OxCaml fast
  path.
- **MAS/ABM assessment reasoning** (behind the memo): the three options
  specialize — Rust/Tokio = platform + alignment language; plumbing =
  coordination/protocols + wiring; Lean→OxCaml = capability kernel whose role
  migrates to Rocq→Rust. The RET×TSSI Track C (agent-based microfoundation) /
  E (simulator) / F (certifier) roles host naturally on Rust / Rocq.

## Decisions & state

- Both notes live in the POC (`notes/plumbing-vs-lean-dijkstra-automata.md`,
  `notes/mas-abm-foundation.md`); REPORT.md untouched (Brad: "don't alter the
  report for now"). `plumbing-setup.md` gotcha appended (ops doc, not REPORT).
- Nothing committed. Git branch: `feat/fulltext-ingestion-v2` (per repo AGENTS;
  commit only when asked, push feature branch only).
- Verification: `uv run python projects/knowledge-repository-poc/scripts/smoke.py`
  → all 13 checks pass (incl. build determinism).
- Open items offered but not done: next step toward the §5 capability sketch
  (`capability_denied` refusals); memo §6 items (certified-kernel cut,
  session-protocol-in-Rust) — await Brad.
- **Post-compaction task (explicit, agreed 2026-08-29):** write a higher-level
  **strategic doc** distilling this foundation work into material for a **public
  blog entry** — audience-appropriate, not project-internal jargon.

## Resume quick-start (this thread)

- Read first: `notes/plumbing-vs-lean-dijkstra-automata.md`, then
  `notes/mas-abm-foundation.md`, then this file's remaining sections.
- After compaction: proceed to the **strategic doc → blog entry** task above.
- Grounding queries: `python scripts/pipeline.py query {"concept":"dijkstra monads"}`
  (cwd `pipelines/`; both Dijkstra works surface).
- The two enforcement-half references (Bastion HOPE 2024, Eio 1.0) are **not** in
  OpenAlex — cited by URL; ACM full texts are publisher-gated (abstracts only).
- The Lean-vs-Rocq reasoning, MAS ranking, and proposal-paragraph decoding are
  context-only unless/until they reach the strategic doc — re-derivable from the
  two notes but faster here.