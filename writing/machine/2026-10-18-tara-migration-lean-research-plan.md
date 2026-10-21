# tara-migration-lean — Research Plan (preliminary scope)

---
title: "tara-migration-lean preliminary research plan"
date: 2026-10-18
kind: research-plan
project: tara-migration-lean
---

## What this project is

A certified program-synthesis (vericoding) harness that combines **LeetProof**
(`/home/brad/Projects/LeetProof`; paper
[arXiv:2604.16584](https://arxiv.org/pdf/2604.16584) — staged pipeline over
**Velvet**, a multi-modal verifier embedded in Lean) with the **agent-harness-poc**
ideas (`projects/agent-harness-poc`). The name is intentional: this is the first
slice of migrating TARA itself to Lean.

**Core research delta vs LeetProof:** LeetProof develops its agent-coordination
framework *outside* the vericoding system and therefore cannot continuously
improve. Here Lean holds both the synthesis machinery *and* a formal model of
agent coordination (plumbing's semantics), so the harness can inspect and
continuously improve its own orchestration.

## Recorded decisions (source: `writing/human/tara-migration-lean-questions.md`, answered 2026-10-18)

1. **Coordination semantics:** long-term, formalize *all* of plumbing in Lean
   (self-inspection + continuous improvement of the coordination architecture).
   First slice is the environment/validation route (answers to the four
   follow-ups, 2026-10-18): **M0 = slice (a), infra probe**.
2. **What Lean certifies:** the harness generates certified multi-agent systems
   with compile-time checks that data is properly shaped across seams; the
   harness certifies the shape of its own pipelines.
3. **Runtimes:** the OCaml/plumbing EIO runtime is *kept*; Lean generates
   **plumb files** that execute on the existing runtime. No rewrite of plumbing
   in Lean.
4. **Hypergraph:** formal specification in Lean + mathlib of a hypergraph data
   model, with an eye to usability via a **content-addressable** design
   (Astrolabe, [arXiv:2604.10435](https://arxiv.org/html/2604.10435v1): nerves =
   (id, ref, rec), id = hash of record only, width/depth decompositions,
   Prop 2.4 depth-filtration stabilization). The Lean-spec'd store is a **new
   store** — not a migration of the existing `tara_graph.db` corpus.
5. **Multi-paradigm vericoding:** deferred (not a v1 requirement). Long-term
   target is a *non-dependent* multi-paradigm language (object-oriented /
   functional / imperative — conceptually TypeScript-like), grounded in the
   duality program of Binder et al.
   ([arXiv:2403.06707](https://arxiv.org/abs/2403.06707),
   defunctionalization/refunctionalization) and Brad's
   [`bvenner/codata-agda`](https://github.com/bvenner/codata-agda). Tara-migration-lean
   must stay *compatible* with this track but does not depend on it.
6. **Relationship to open threads:** strictly **parallel** to
   agent-harness-poc; the existing harness stays live; this project may fail.
7. **Deliverable:** if successful, foundational architecture for developing
   multi-agent systems and simulating them in agent-based models — touches all
   existing research projects.
8. **LLM budget:** deliberately deferred until after this preliminary scope.
   Decision lands at the M0a→M0b boundary (see below).
9. **Longer-term vision (out of scope, recorded):** run-time analysis of the
   certified system feeding back a proposed new agent architecture; new
   functional requirements added to the verifier; re-synthesis. Ultimately
   refinement of certified programs using **observational equivalence**, per
   [`scidonia/leanin`](https://github.com/scidonia/leanin). Runtime analysis and
   bisimulation are explicitly out of scope for v1.

## Environment facts (verified 2026-10-18)

- `elan 4.2.1`, `lean`, `lake` are installed locally (user profile,
  devenv-independent). Docker is **absent**.
- LeetProof repo: `/home/brad/Projects/LeetProof/leetproof` — Python pipeline
  (`leetproof/` package: `cli.py`, `container.py`, `agents/`, `prompts/`,
  smoke tests) + `llmgen-experiment/` (Lean side).
- Velvet is **public and pinned**: `https://github.com/verse-lab/velvet`,
  rev `9a61202`, toolchain `leanprover/lean4:v4.24.0` (see
  `llmgen-experiment/lakefile.toml`). A local bare-lean build is feasible;
  the 60 GB Docker artifact is only needed for the paper's exact benchmark
  bundle (semantic-search data, embedding model, pinned Spec-PBT inputs).
- LeetProof's `cli.py` itself checks bare `lean`/`lake` availability and points
  to elan — the Docker path is not architecturally mandatory.

## Milestones

### M0a — Infra probe: LeetProof + Velvet locally, no LLM spend (slice (a), part 1)

- Build Velvet from source with elan (`leanprover/lean4:v4.24.0`), Mathlib
  cache; land `llmgen-experiment` `lake build` clean.
- Run LeetProof's no-key validation paths (per README "Validate the image
  without an API key") with a bare-lean adapter replacing Docker
  (`container.py` / `lean_synth_and_verify.py` inspection; smoke tests in
  `smoke-tests/`).
- Document local-vs-Docker deltas in this project's research log.
- **Exit:** a recorded, reproducible local build + a checklisted list of what
  remains gated behind an API key.

### M0b — One end-to-end vericoding run (slice (a), part 2; **LLM budget decision here**)

- Pick one benchmark (LeetProof has pinned Spec-PBT inputs; the Verina-style
  examples in `llmgen-experiment`).
- Run spec-synthesis → property-based spec-validation → synthesis/proof pipeline
  end-to-end on the local stack with one provider backend (OpenRouter GLM tier
  as default candidate; all staged-pipeline traffic, not yet prover-internal).
- **Exit:** one Lean artifact (program + spec + machine-checked proof) produced
  locally, cost recorded. **This is where the deferred LLM-budget decision is
  made with real numbers.**

### M1 — AstroNet formalization (slice (c), independent of M0b)

- Formalize the six content-addressable hypergraph axioms plus width/depth
  decompositions and Prop 2.4 (stabilization + cycle characterization) in Lean
  with mathlib; usable as the spec of the harness's context/memory layer.
- v1 is the *spec/library* (new store); adapters for existing corpus content are
  explicitly not in scope.

### M2 — Plumbing-semantics subset (slice (b))

- Lean model of a plumbing subset: typed morphism contracts, exact-typed `exec`
  boundaries (the "extra input key is fatal" class), typed multi-agent routing.
- Generate a **certified workload manifest as a plumb file**: Lean program +
  proof that the pipeline wires conform to typed contracts, compiled to
  `.plumb` source executing on the existing plumbing runtime (agent-harness-poc
  M6/M7 manifests as first targets/fixtures).

Order: M0a → M0b; M1 may run in parallel with M0* (it needs no LLM spend).
M2 waits on M0b acceptance + M1 existing as a library. Self-inspection loop,
runtime analysis, observational-equivalence refinement, and the multi-paradigm
target language are all post-v2.

## Open decisions

- LLM budget (resolved at M0b exit; OpenRouter GLM tier is the default
  candidate, plumb `agent` binding already proven there).
- Whether the Lean hypergraph library lands as its own repo or lives inside
  this project's Lean package.
- Interaction protocol for Lean-external prover LLMs (untested raw `lake`
  ↔ OpenRouter loop); only relevant if M0b's budget decision funds prover
  traffic.

## Resume path

1. This doc (scope, decisions, milestones).
2. `writing/human/tara-migration-lean-questions.md` — clarifying-question
   round + answers (the recorded decisions above are its distillation).
3. LeetProof paper: [arXiv:2604.16584](https://arxiv.org/pdf/2604.16584);
   repo README (Docker path) and STATUS/REQUIREMENTS (artifact badges).
4. Adjacent threads: `projects/agent-harness-poc/AGENTS.md` (workloads,
   scorer, M7 comparison — plumbing-side coordination source of truth);
   `projects/tara-migration-lean/AGENTS.md` (project-level resume/status).
