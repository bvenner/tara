---
title: "M7 slice 1: researcher-as-plumb head-to-head — three-arm comparison on the same manifests and scorer"
date: 2026-10-12
kind: review
project:
  - agent-harness-poc
  - knowledge-repository-poc
---

# M7 slice 1 — three-arm comparison (2026-10-12)

Same workload manifests (`workloads/*.json`), same shared instruction file
(`workloads/instructions/grounding.md`), same mechanical scorer
(citation-support over each arm's own evidence anchors + load-bearing min-1
entailment judge GLM-5.3-Flash, cached). Three arms: **opencode** (committed
artifacts, parsed), **Pydantic AI agent** (M1/M3 stack), **plumb** (M7
`researcher.plumb` prefetch architecture).

## Architecture found by the experiment

Upstream plumbing does not yet implement exec lowering via agent tool
dispatch (`tool_not_supported`), so the plumb arm cannot run the
tool-calling loop the Pydantic arm runs. M7 slice 1 therefore adopted the
**prefetch architecture**, and it turns out to be a discovery rather than a
fallback: with the newly-added `scripts/research_gate.py` worker
(trace at the manifest gate → per-concept-query fallback, the same move the
mechanical M3a probe uses) **plus section-content prefetch** (evidence
texts, 1200-char budget), the deterministic stage supplies a bounded
in-fabric agent with a full evidence envelope. Prefetch-with-content was
necessary and sufficient: before it, the plumb arm's judge scores were
scattered 0/INSUFFICIENT (the agent was citing section titles it could not
read).

## Results

tau-sk-grounding (`2026-10-12-m7-tau-sk-*-report.json`):

| arm | claims | citation_support | load_bearing | judge-entail | wall |
|---|---|---|---|---|---|
| opencode-artifact (stored baseline) | 6 | 0.50 (corpus drift, known) | 1.0 | 0.80 | 1.4 s |
| pydantic-agent (fresh instructions) | 2 | 0.50 | 1.0 | 0.00 | 14 s |
| plumb-agent | 13 | 1.00 | 1.0 | **1.00** | 114 s |

island-dt-crosspillar (`2026-10-12-m7-island-*-report.json`):

| arm | claims | citation_support | bundle | pillars | judge-avg | wall |
|---|---|---|---|---|---|---|
| opencode-artifact (authored this session) | 7 | 1.0 | **13/13** | 4/4 | **1.00** | 1.4 s |
| pydantic-agent-fanout | 14 | 1.0 ×4 | 11/13 | 4/4 | 0.55 | 186 s |
| plumb-agent-fanout | 27 | 1.0 ×4 | 11/13 | 4/4 | **0.89** | 229 s |

## Findings (do not re-derive)

1. **The plumb arm is competitive — the categorical claim is dead.**
   Researcher-as-plumb (config-only) matched or beat the Pydantic arms on
   every metric on this sample set, including judged entailment. The
   division-of-labor question M7 posed — "can a `.plumb` file host a
   researcher?" — resolves: yes, under prefetch + content, within ~2-4 min
   wall per workload.
2. **Single samples are not benchmark-grade.** The pydantic tau-sk run's
   regression (2 claims, judge 0.0 — vs 3 claims 1.0 in the M6 banked run
   on near-identical instructions) is sample variance on a
   non-deterministic LLM, not an architecture verdict. Firm M7 conclusions
   need a repeat protocol (n≥3 per cell) — slice 2 work.
3. **Claim budgets leak on the plumb side** (13 claims vs the ≤5
   instruction) — the in-fabric agent has no mechanism to enforce the
   claim budget; consider a plumb-side post-filter stage or accept and
   score as-is.
4. **The opencode arm's 13/13 bundle is partly an artifact of its flexible
   gate** (its artifact author used min_seeds=1 with 6 seeds); the
   fan-out arms held higher gates (min_seeds=2 per lane) and covered 11/13.
   Comparators should either unify gates or report gate-dependent metrics —
   recorded, not hidden.
5. Anchor-universe formats are a real cross-harness contract: the plumb arm
   initially emitted `doc — [section]` (0.0 citation support, correctly);
   `normalize_claim_source` shims it into the canonical contract, and the
   plumb prompt now states the format explicitly — cs went 0.0 → 1.0.

## Where each arm wins (working division of labor, updated by evidence)

- **opencode**: strongest when a human-in-the-loop interactive researcher
  curates seeds/gates (its artifact beat both scripted arms on bundle +
  judge). Coding work remains native.
- **plumb**: best scripted single-shot quality on this sample; the
  deterministic evidence stage is reusable by *any* arm (the
  `research_gate.py` worker is a repository service now)
- **pydantic**: still required for anything needing in-loop tool
  orchestration beyond the prefetch (seed autonomy, docstore browsing,
  dynamic pipelines); fan-out machinery (M3) lives there.

## Artifacts

- Reports: `agent-harness-poc/evals/2026-10-12-m7-*.json` (7 files)
- Plumb researcher: `knowledge-repository-poc/pipelines/researcher.plumb`
- Deterministic gate worker: `knowledge-repository-poc/scripts/research_gate.py`
- Opencode island artifact: `knowledge-repository-poc/graph/grounded-answer-island-dt.md`
- Sidecars: `agent-harness-poc/evals/cache/plumb-sidecars/` (per lane)
