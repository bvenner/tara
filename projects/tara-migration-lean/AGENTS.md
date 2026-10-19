# tara-migration-lean — certified program-synthesis harness (Lean migration)

New thread (2026-10-18), strictly **parallel** to `agent-harness-poc`: combines
LeetProof (`/home/brad/Projects/LeetProof`, paper arXiv:2604.16584 — vericoding
pipeline over Velvet, a multi-modal verifier embedded in Lean) with the
agent-harness-poc ideas. Lean generates certified multi-agent systems +
**plumb files** running on the existing plumbing OCaml runtime; Lean+mathlib
formalizes the content-addressable hypergraph (Astrolabe-style) for context /
state / resource ingestion. Long-term: plumbing's coordination semantics move
into Lean so the harness can inspect and improve its own orchestration.

## Resume path

1. `writing/machine/2026-10-18-tara-migration-lean-research-plan.md` —
   authoritative scope, recorded decisions (from Brad's answered questions in
   `writing/human/tara-migration-lean-questions.md`), environment facts,
   milestones M0a–M2, open decisions.
2. LeetProof paper arXiv:2604.16584; repo at `/home/brad/Projects/LeetProof/leetproof`
   (Velvet pinned: `verse-lab/velvet` rev `9a61202`, toolchain `lean4:v4.24.0`).
3. Adjacent: `projects/agent-harness-poc/AGENTS.md` (source of coordination
   patterns under formalization; stays live and untouched).

## Status

- **Scoping: DONE (2026-10-18).** Plan doc written (see resume path). No code yet.
- **Next: M0a** — local LeetProof/Velvet build, no LLM spend. Docker absent on
  this box (local elan 4.2.1 / lean / lake present).

## Conventions

- Semantic commit prefixes (`feat:`/`docs:`); commit only when asked; push
  feature branch → PR; never push `main`.
- This project may fail; agent-harness-poc stays the live harness meanwhile.
- LLM budget decision is deferred to the M0a→M0b boundary — do not incur
  prover/API spend before it, without asking.
