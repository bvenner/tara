---
title: M0–M3 session context preservation (agent-harness arc) — read after a context reset
date: 2026-10-11
kind: context-preservation
project:
  - agent-harness-poc
  - knowledge-repository-poc
  - island-digital-twin
---

# Context Preservation — 2026-10-11 (agent-harness-poc: M0 → M3 + C1)

Session arc and standing facts for resumption. Supersedes thread-local detail
for the agent-harness work; **still read `writing/machine/2026-08-23-context-preservation.md`
plus root `AGENTS.md` first** for the general four-thread picture.

---

## 1. Where the milestones stand (2026-10-11)

- **M0 spike, M1 tool bridge, M2 evals, C1 GLM comparison, M3 fan-out: all
  DONE.** Merged through PR #6/#7/#8; **PR #9 open** (`feat/agent-harness-m3`
  → main, 2 commits: `d167197` test-practices batch, `7515473` M3). Merge
  pending Brad's word. Local `main` has both commits locally (unpushed to
  main directly — the branch carries them), in sync otherwise.
- **Quality verdict (C1, resolved):** Pydantic AI stack ≥ opencode baseline
  mechanically (agent-tau-sk: CitationSupport 1.00 / LoadBearing 1.00 /
  ClaimEntailment 0.80 vs baseline 0.50/1.00/1.00; richer synthesis;
  physics-envy case's one claim judged NOT ENTAILED because it is a
  meta-claim — the judge is right).
- **M3 decision evidence recorded (root AGENTS.md open decision updated):
  fan-out at explicit pillar/track taxonomy granularity solves cross-pillar
  recall mechanically** — mechanical probe 4/4 pillars, 11/13 of the
  recorded bundle; agent-union 13/13 + 16/16 supported claims. Embeddings'
  remaining niche: unanticipated/unknown taxonomies; Phase C not forced.
- **Runtime plan executed:** fixture stack (F1) + replay caches (F2):
  full 3-case judged dataset = **3.3 s steady-state** (cold ~450 s →
  245 s → 3.3 s). Direct plumb spawn (opt-in `TARA_PLUMB_DIRECT=1`,
  ~1200→23–163 ms per uncached call) available but **not adopted as
  default yet** (decide when next touching the surface).

## 2. TDD caveat for LLM-agent systems (verification *not* reduction problems)

During M0–M3, testing grew **bug-driven**; the explicit caveat Brad asked to
revisit is:

1. **Classic TDD is only well-defined over deterministic seams.** Caches,
   parsers, typed boundédaries (the plumb exec boundary's exact-typed
   fatality), evaluator logic, replay/fixture layers — there, test-first
   works normally and we now follow it (property tests whenever a surprise
   changes semantics; regression test lands with the fix).
2. **LLM-gated paths (agent tool loops, judge verdicts) are
   nondeterministic and network-shaped — test-first is inapplicable as a
   guarantee.** The governing structure there is *behavioral evaluation*:
   the pydantic-evals dataset with mechanical evaluators (citation
   support over tool-output sidecars) + LLM-as-judge (claim entailment
   against corpus section text) + frozen fixtures of known-good evidence.
3. **False-confidence danger around LLM calls:** brittle exact-match unit
   tests would "pass" while grounding discipline silently degrades. The
   baseline already demonstrated the failure mode: the stored opencode
   answer rotted to CitationSupport 0.5 after the corpus moved
   (`to_human/` → `writing/machine/` refactor), with no unit test able to
   see it — only the anchors-vs-trace eval caught it. **Green suites do
   not imply grounded answers; grounded-ness must be re-verified against
   the current corpus.**
4. **Adopted practices (recorded in `projects/agent-harness-poc/AGENTS.md`
   §Testing):** layered testing — repo smoke (CI, now with an agent-harness
   offline fixture contract) → `tests/` (22→25 deterministic tests:
   boundary regression, judge schema/cache, run-cache key properties,
   sec_clean, direct-vs-nix equivalence, bundle-parse, 4-pillar property)
   → `evals/` (judged evals + fixture replay for anything LLM-gated).
   Cost discipline integrated: claim caps (≤5), wall-clock cap
   (`TARA_RUN_TIMEOUT`), replay caches so evaluator/judge changes validate
   without LLM spend.
5. **Open questions Brad wants to revisit:**
   - How much *test-first* discipline can be moved around (not into) the
     LLM edge — contract-first tools, schema-first boundary mirrors,
     golden traces, determinism-by-construction?
   - Should fixture staleness be tied to the graph build-hash so invalid
     evidence fails loudly (currently keyed but not asserted in smoke)?
   - Judge-of-record policy: GLM-5.3-Flash judging is cheap and
     discriminating; do we need periodic strong-model (Anthropic) calibration
     to guard against judge drift/systematic bias — and how do we know?
   - The deeper claim worth exploring next research arc: the *grounding
     discipline itself* (claim ⇒ cited section entails it;
     no assertion beyond trace) is a set of formal properties over
     (tool outputs, claims) — i.e., the eval layer is the real "TDD of the
     agent era", and formalizing it (Track F-adjacent) may unify the two
     halves rather than treating LLM paths as exempt.

## 3. Standing facts added this session (do not re-derive)

- **Keys (all gitignored `.env`):** `GOOGLE_API_KEY` (restricted AI Studio
  auth key; `google:gemini-3.8-flash` free tier = 20 req/day,
  `gemini-3.5-flash-lite` larger), `OPENROUTER_API_KEY`
  (`openrouter:z-ai/glm-5.3-flash`, ~$0.15/$0.50 per M list; pennies per
  eval). Z.ai signup geo/identity-blocked for Brad; model string prefix is
  `google:`/`openrouter:` in these Pydantic AI versions;
  `gemini-2.5-*` retired for new accounts. Total LLM spend to M3: a few
  cents.
- **persevere wheels** (libsodium `.so.23` unfixable via LD_LIBRARY_PATH)
  → **pass the Nix-built binary explicitly** via `binary=` (both
  `pb.call_sync` and `PlumbingModel`); resolution order explicit → bundled
  → PATH.
- **plumb exec boundaries are exact-typed: an extra input key is fatal**
  (`morphism_fatal`, no worker traceback). Tools use boundary-mirror
  `TraceInput`/`QueryInput`, NOT `schemas.TraceRequest` (its `max_edges`
  default kills `trace.plumb`). Regression-tested.
- **Cache layout:** `grounded/tools.py` pipeline memoization (TARA_NO_
  PIPELINE_CACHE bypass, graph-hash keyed); `run_grounded.ground_run_async`
  agent cache + judge verdict cache (`evals/cache/`, gitignored;
  `TARA_NO_RUN_CACHE` / `TARA_NO_JUDGE_CACHE` / `--refresh`); both keyed
  on graph build hash → corpus rebuild invalidates automatically.
- **pydantic-evals specifics:** `Dataset(name=…)` required;
  `EvaluatorContext.name` (not `case.name`); evaluators cannot `return
  None`; async judges mandatory inside pydantic-evals (run_sync →
  "event loop is already running"); `report.print()` then serialize via
  (name, scores) from `report.cases`.
- **Fixture stack:** `evals/fixtures/` + `evals/replay.py` — full
  evaluator stack offline <5 s (smoke CI block depends on it).
- **First successful documented flow for a NEW session on this stack:**
  read notes → `uv sync --frozen` → `uv run pytest projects/agent-harness-poc/tests/ -q`
  → `uv run python projects/knowledge-repository-poc/scripts/smoke.py` →
  everything warm: evals are replayed, agents cached, no key burn.

## 4. Open items (ranked)

1. **Merge PR #9** (M3 + test-practices batch) on confirmation; dissolve
   `feat/agent-harness-m3` (+ old `feat/agent-harness-c1-glm` branch too —
   currently still on origin from PR #8... verify: it was deleted? It was
   NOT deleted; remove after confirming `main` has everything).
2. **M4 — Gateway cutover:** create the Logfire Personal org, Gateway key
   (`PYDANTIC_AI_GATEWAY_API_KEY`), BYOK-zero-markup routing for
   Google/Anthropic; switch agent model strings to `gateway/...`;
   GLM continues direct via OpenRouter (not a gateway built-in).
3. **M5 — Plumbing gateway support** (upstream `agent` morphism through
   the gateway proxy) — issue to track upstream plumbing repo now that a
   cheap OpenAI-compatible key exists for pipeline-internal agent work.
4. **Master's sub-problem choice (RET×TSSI M1 default)** — the other
   thread's critical path; agent stack ready to upgrade-ground that work.
5. Repo privacy purpose decision + audio-sharing setup (from 09-28 list)
   — still parked.
6. Older strand: `docs/writing-machine-layout`/`feat/agent-harness-m2`
   branches were dissolved post-merge; keep main-side hygiene when
   dissolving.

## 5. Conventions re-affirmed (stand on these)

- `writing/human/` vs `writing/machine/` split; machine notes live
  centrally with YAML frontmatter (title, date=filename, kind, project
  keyword = `projects/` folder name, list for multi-thread, or
  `workspace`).
- Secrets only in gitignored `.env` (keys never in tool contracts or
  prompts/readmes); if a secret file name EVER lands in staging, untrack +
  gitignore + amend (the process that caught `z-ai-pwd.txt` before push).
- Semantic commit prefixes; commit only when asked; feature branch → PR,
  never push `main`.
