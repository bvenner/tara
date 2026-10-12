---
title: Fixing the M2 loop — time and LLM-capacity plan (fixtures, replay cache, GLM tier)
date: 2026-10-11
kind: research-plan
project: agent-harness-poc
---

# Plan: addressing the two M2 resource limitations — 2026-10-11

Two limitations surfaced while building M0–M2 (~18 h end-to-end): (1) slow
improvement loop — `grounding_eval.py` full runs took minutes-to-tens-of-minutes,
dominated by backoff waits and repeated full-dataset reruns while debugging the
harness; (2) LLM-capacity/cost — free-tier Gemini quotas (20 req/day on
`gemini-3.8-flash`, saturable RPD on `3.5-flash-lite`) throttle research runs
and repeat-eval work, and moving off opencode means losing its hosted GLM
provider unless the agent stack gets its own cheap key.

Verdict: **both assessments agreed, with refinements** — the time sink is
*feedback latency* (fixture-less debugging + network/backoff + spawn overhead),
not eval design per se; the capacity fix is a paid, cheap, OpenAI-compatible
open-model tier (GLM-5.3-Flash), which removes the quota cliffs entirely.

---

## 1. Where the 18 h actually went (honest accounting)

| Factor | Share | Fix |
|---|---|---|
| Real milestone work (M1 bridge, acceptance evidence) | ~35% | — (irreducible value) |
| Harness-debug cycle rerunning the FULL dataset per bug | ~25% | Fixtures: evaluate agents on frozen artifacts, no LLM, no pipelines |
| Free-tier 429/503 + backoff sleeps inside/around runs | ~20% | Paid GLM tier (no quota walls) + async judges |
| `nix develop` spawn ≈2–4 s per pipeline call × tool loops | ~10% | Pipeline-call memoization |
| Judge serialization (`max_concurrency=1`) + wall latency of weak models | ~10% | Concurrency for judges; faster model |

---

## 2. Fix layer — fixture stack (offline evaluators, no key needed)

Freeze the artifacts we already banked into a **replayable fixture stack**:

- `evals/fixtures/`:
  - `2026-10-10-m1-tau-sk.tools.json` (sidecar) + the run's `GroundedAnswer`
  - the baseline parse (deterministic from `grounded-answer-tau-sk.md`)
  - the judged transcript (`2026-10-10-m2-judged-run.log`) as the judge's
    frozen reference — future judge changes diff against known verdicts
  - one fixture per extra case we later accept.
- `evals/replay.py`: `load_run(name) -> GroundedRun` + fixture-backed
  versions of the three deterministic evaluators.
- Wire into pytest: the full evaluator stack goes over fixtures — **< 5 s,
  no key, no nix**, so harness/evaluator/judge-schema changes validate
  instantly.

Acceptance: every future evaluator modification is testable offline; a broken
change red in seconds.

## 3. Fix layer — replay cache (warm evals, no quota churn)

- **Agent-output cache**: key = (model string, question hash, instructions
  hash, graph `build_meta.json` hash). Store the full `GroundedAnswer` +
  sidecar record per key under `evals/cache/`. `pydantic-evals` task checks
  the cache before calling the LLM; `--refresh` bypasses. Effect: tuning
  evaluators/judges re-evaluates without re-running agents.
- **Pipeline-call memoization**: in `grounded/tools.py`, wrap `_call` with a
  content-addressed disk cache (key = pipeline name + input JSON +
  graph build hash); kills the repeated `nix develop` spawns during a run and
  makes non-agent offline evals (citation-support grading of stored runs)
  instant.
- **Concurrency**: task execution stays serial (agent-dependent quota), but
  judge calls fan out (`asyncio.gather` inside `ClaimEntailmentJudge`).

Budget targets: **cold** judged eval ≈ minutes (instead of 10+ with backoff
walls), **warm** (cached agents) < 2 min, **offline** (fixtures) < 5 s.

## 4. Capacity layer — the GLM tier (the "opencode provider, unshackled")

Verified economics (2026-10-11):

- **Z.ai direct (first-party): GLM-5.3-Flash = $0.150/M input, $0.500/M
  output, $0.030/M cached input.** No RPD quota walls; paid throughput.
- **OpenRouter route** (`z-ai/glm-5.3-flash` / DeepInfra): has alternated
  between $0.075/$0.25 (launch promo) and list — check at sign-up; adds 5.5%
  (Standard) platform fee in exchange for 500+ models behind one key.
- **Model quality**: Artificial-Analysis Intelligence Index ~57, agentic
  performance near Claude-Opus-4.8 class, 320B MoE (18B active), MIT weights
  (self-hostable; 6-figure GGUF downloads — a zero-cost fallback tier).
- Same family as this opencode session's model — behaviorally familiar.

**Phase C1 — GLM as workhorse + judge (recommended):**
1. Get a **Z.ai standard API key** (pay-as-you-go; NOT the GLM Coding Plan —
   that one's quota model (5-h/weekly prompt windows) is tuned for IDE
   agents and needs credit bookkeeping for API runs; standard API is
   metered per token: ~$0.02–0.20 per full agent run by our token profile).
   **Update 2026-10-11: Z.ai signup blocked Brad out** — alternates verified
   instead, same model family via third-party hosts:
   - **DeepInfra (preferred now):** `zai-org/GLM-5.3-Flash` at an active
     50% discount — **$0.075 in / $0.25 out / $0.015 cached per 1M** (list
     $0.15/$0.50). OpenAI-compatible, base URL
     `https://api.deepinfra.com/v1/openai`, key from dashboard, Google
     sign-in, small usage-based billing.
   - **OpenRouter (fallback/variety):** `z-ai/glm-5.3-flash` (default route
     $0.15/$0.50; cheapest host routes ~$0.04–0.06 in on the model page),
     +5.5% Standard fee, $5 min top-up, 500+ models behind one key —
     useful later for the quality-ceiling calibration without a second
     account.
2. Wire into Pydantic AI as an OpenAI-compatible provider:
   `OpenAIChatModel('glm-5.3-flash', provider=OpenAIProvider(base_url='https://api.z.ai/api/paas/v4', api_key=ZAI_API_KEY))`
   — or set `OPENAI_BASE_URL`+`OPENAI_API_KEY` in `.env` and use
   `openai:glm-5.3-flash` model strings; add `pydantic-ai-slim[openai]` (no
   extra needed beyond the base we already install? — confirm; base already
   bundles `openai` client via slim? — verify at implementation start).
3. Roles: **task model** = `AGENT_MODEL` default → GLM-5.3-Flash;
   **judge** = `AGENT_JUDGE` → GLM-5.3-Flash for eval-of-record; keep
   `gemini-3.8-flash` as free-tier fallback; quality-ceiling judge
   (Anthropic Sonnet/Opus, needs the $5 deposit) **only** for the one-off
   M2-final acceptance calibration.
4. Re-run M2's judged eval on the new tier → fraction-ENTAILED comparison
   (agent vs baseline) — this is the pending "quality verdict" recorded in
   the thread AGENTS.md, now unblocked.

**Phase C2 — cooperative fallbacks** (zero/low cost, no key):
- Ollama local (MIT GLM weights or Qwen3): zero dollar cost for harness
  smoke + fixture validation where structured-output fidelity isn't critical.
- OpenRouter free-router (50 req/day): tiny dev windows.

**Phase C3 — plumbing-side (M5; DONE 2026-10-12)**: the pipeline-internal
`agent` morphism routes through the same OpenAI-compatible endpoint. Delivered
purely as config (`pipelines/agent.plumb`: provider openai, model, api_key
`${OPENROUTER_API_KEY}`, endpoint literal) — no plumbing code change, exactly
as preposed. `scripts/pipeline.py` auto-loads the gitignored `.env`. See the
plan doc M5 section for the acceptance evidence and the max_tokens finding.

**Gateway interplay (M4)**: unchanged for Google/Anthropic (gateway BYOK,
0% markup on Personal). GLM is not a gateway built-in provider; it runs
direct (or via OpenRouter if single-key consolidation matters more than the
5.5–8% fee).

## 5. Execution order

1. F2 (fixtures + replay) — ~1.5 h, zero cost, immediate loop-speedup win.
2. F2 (cache + judges fan-out) — ~2 h, zero cost.
3. C1 key setup + provider config + M2bis judged rerun — external dependency
   (key signup, ~5 min) + ~30 min wiring; output = the pending judge
   comparison between agent and baseline on a **non-quota** tier.
4. Optional: `pydantic-evals` dataset/checklist export for CI (cheap smoke,
   key-gated, mirrors repo smoke).

## 6. Open decisions (for Brad)

- Confirm Z.ai standard API key creation (I'll document the exact steps when
  you say go — analogous to the Gemini key walkthrough).
- Judge-of-record = GLM-5.3-Flash adopted once the C1 comparison passes
  (or after Kimi-style tie-break calibration)?
- Adopt cache-then-LLM as the default eval behavior — mostly transparent,
  but flag if you ever want cold-only evidence.
- Whether the answer-quality ceiling stays Anthropic-optional or we accept
  GLM-tier as good-enough pending corpus evidence.
