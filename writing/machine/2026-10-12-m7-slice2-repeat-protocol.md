---
title: "M7 slice 2: repeat protocol (n=3) — firm per-arm rankings, budget compliance, and the judge-quota lesson"
date: 2026-10-12
kind: review
project:
  - agent-harness-poc
  - knowledge-repository-poc
---

# M7 slice 2 — repeat protocol results (2026-10-12)

Extension of the M7 slice-1 comparison (see
`2026-10-12-m7-slice1-comparison.md` for architecture). Same manifests,
scorer, shared instruction file, GLM task + judge. New: **n=3 fresh runs
per scripted cell** (`run_workload.py --judge --n 3`; caches bypassed per
repeat; judge verdicts cached, keyed by judge model + claim + section
excerpt), judged on every repeat; **claim-budget compliance (≤5) scored as
a metric** instead of enforced by truncation. Reports:
`2026-10-12-m7s2-*.json` (4 files).

## Results (mean over 3 repeats, range in parens)

| cell | citation_support | judge-entailment | budget-ok | bundle/pillars |
|---|---|---|---|---|
| tau-sk / pydantic-agent | 1.0 (stable) | **0.278** (0.0–0.5) | 3/3 | — |
| tau-sk / plumb-agent | 1.0 (stable) | **1.000** (1.0–1.0) | **0/3** (12–13 claims) | — |
| island / pydantic-agent-fanout | 1.0 (stable) | **0.733** (0.69–0.78) | 20/20 | 13/13, 4/4 every repeat |
| island / plumb-agent-fanout | 1.0 (stable) | **0.799** (0.75–0.875) | **0/3** | 11/13, 4/4 every repeat |

(opencode arm unchanged: deterministic committed artifacts, single-authored
per slice 1 — not repeatable by protocol; it stays the interactive third arm.)

## Firm findings (out-weighing the slice-1 caveat)

1. **Citation support is 1.0 everywhere, with zero variance** across 3
   samples × 4 cells — the grounding *discipline* (cite-what-your-tools-
   returned) is statistically solid in both scripted harnesses.
2. **Judge-entailment is where arms differ, and the ranking is real:**
   - tau-sk: plumb 1.00 stable beats pydantic 0.28 — under the
     deterministic evidence envelope, GLM produces fully-entailed claims;
     the tool-driving pydantic agent's fresh-sample claims are
     half-entailed at best. (Slice-1's pydantic "regression" is
     reproduced at n=3, so it was a property of the fresh instruction
     text + samples, not a one-off.)
   - island: plumb mean 0.80 vs pydantic 0.73 — overlapping ranges
     (plumb max 0.875): a tie within sampling noise, with plumb the
     slight edge.
3. **Budget compliance is the real division-of-labor differentiator:**
   pydantic 100% ≤5-claims; plumb 0% (12–13 claims, unrelated to
   instruction effort — the in-fabric agent has no enforcement mechanism;
   a post-filter stage or upstream cap is needed).
4. Wall-clock: plumb cells are the slowest (637–1240 s per n=3 cell),
   pydantic tau cheap (153 s). Fan-out dominating cost confirms the
   parallel-judge necessity introduced during this slice.

## Infrastructure bugs found and fixed during the sweep (do not re-derive)

- **Judge fell back to the exhausted Gemini tier silently** — two cells
  were scored by a broken judge (INSUFFICIENT-everywhere signature).
  Fix practice: always pass `AGENT_JUDGE=openrouter:z-ai/glm-5.3-flash`
  in judged sweeps; the judge-cache key includes the judge model so stale
  verdicts do not poison re-runs.
- **The n3 plumb cell "hang":** `subprocess.run(timeout=…)` fires but
  only kills plumb — agent grandchildren inherit the capture pipes, and
  `communicate()` blocks until every fd holder dies (no upstream HTTP
  request timeout). Fixed with `start_new_session` + `os.killpg` in
  `run_guarded`; `TARA_PLUMB_SUBPROC_TIMEOUT` parameterized.
- **Judge fan-out**: the M2-style `asyncio.gather` judging now applied in
  the workload runner (sequential per-claim judging made n=3 unusable).

## Updated working division of labor

- **tau-sk-class single-question grounding**: plumb (prefetch) is the
  stronger scripted arm, at higher wall-clock cost and a budget caveat.
- **cross-pillar assembly**: tie; plumb slightly ahead on entailment,
  pydantic ahead on budget compliance and wall-clock.
- **claim-budget-sensitive uses**: pydantic until plumb-side enforcement
  exists.
- **interactive research / coding**: opencode (unchanged).
- Slice-2 does not change the M6-opencode disposition input; the
  compression is that glue-richness now demonstrably lives outside the
  Python harness for bounded workloads.
