# Agent Harness PoC — Pydantic AI Top Layer

New thread (2026-10-10): bringing plumbing's multi-agent capabilities to the
top of the stack — a Pydantic AI agent harness (`Researcher`) replacing
opencode as the research-layer, with plumbing exposed via typed tools
(default) and `PlumbingModel` (evals). Full plan, decisions, and milestones
M0–M6: `writing/machine/2026-10-10-pydantic-ai-topleft-plan.md` (frontmatter
`project: agent-harness-poc`).

## Status

- **M0 — Spike: DONE (2026-10-10).** `spike/m0_spike.py` runs the upstream
  identity pipeline through both integration modes with no API key:
  1. Bare API (`pb.call_sync(spec, msg, binary=...)`) — echoed correctly.
  2. Model mode (`PlumbingModel(spec, binary=...)` in a Pydantic AI `Agent`)
     — stateful two-turn echo works (`hello` → `hello`, `world` → `world`;
     `model_name` = `plumbing:<spec path>`).
- **M1 — Tool bridge: DONE (2026-10-10).** `grounded/tools.py` wraps
  `pipeline.py` with canonical worker-contract validation
  (`knowledge_trace`, `knowledge_query`, `knowledge_evidence`,
  `knowledge_trace_report`; `expand` deliberately deferred — it mutates the
  corpus). `run_grounded.py` = cli: grounded agent
  (`google:gemini-3.5-flash-lite` default, `AGENT_MODEL` override),
  `GroundedAnswer{question, synthesis, claims[{statement, source "doc ::
  section", trace_edge_ids}]}`, transient-429/503 retry loop. **Acceptance
  evidence:** `evals/2026-10-10-m1-tau-sk.md` (tau→0 vs SK question) with
  tool sidecar; `evals/check_citations.py` verifies every claim against the
  union anchor universe from the sidecar → **3/3 supported**. Note:
  flash-lite synthesis is thinner than the opencode baseline
  (`graph/grounded-answer-tau-sk.md`) — model-dependent quality is M2's eval
  work (`gemini-3.8-flash` free tier = 20 req/day, resets midnight Pacific).
  Tests: `tests/test_tools.py` (pipeline integration + exact-boundary
  regression), `tests/test_check_citations.py` — 6 passed.
- M1 infra notes: provider key in gitignored `.env` (`GOOGLE_API_KEY`) —
  restricted Google AI Studio auth key; model string prefix is `google:` in
  slim 2.55 and **`gemini-2.5-flash`/`-lite` are retired for new accounts**
  (use `gemini-3.8-flash` [20 free req/day] or `gemini-3.5-flash-lite`
  [larger free tier]).
- **M2 — Eval: DONE (mechanical half) / judge-style implemented (2026-10-10).**
  `evals/grounding_eval.py`: pydantic-evals dataset —
  deterministic evaluators (`structure`, `citation_support`,
  `load_bearing_coverage` vs the opencode baseline's load-bearing list) +
  `claim_entailment` LLM judge (`AGENT_JUDGE` env, async; judge per claim
  against the cited corpus section text resolved via
  `grounded/corpus_sections.py` = corpus.json roots + heading match).
  Cases: agent-tau-sk, baseline-tau-sk-static (parses the stored baseline
  `graph/grounded-answer-tau-sk.md`), agent-physics-envy (out-of-scope
  probe). **Mechanical M2 acceptance met:** agent CitationSupport 1.00 + LoadBearingCoverage 1.00 ≥ baseline (baseline itself scores
  CitationSupport 0.500 post-move — 3/6 of its citations refer to
  `ret-tssi/to_human/`, unresolvable since the writing/machine refactor;
  real corpus-drift finding). **Judge findings (flash-lite judge,
  partial):** agent claims 1/3 ENTAILED — judge caught genuine overreach
  (claims attributing well-posedness to "the SK condition" where §2.2
  credits the Ruggeri–Strumia theorem; A5-citation claim contradicted by
  the section's singular/p diverging argument). baseline judge run
  validates (log + report archived, `evals/2026-10-10-m2-judged-*`).
  Quality verdict needs a stronger judge/task model: `gemini-3.8-flash`
  free = 20 req/day (resets midnight Pacific), Anthropic $5 — **open
  decision**. Tests: `tests/test_m2_units.py` (parser, section resolution,
  doc-path) — 9 passed total; smoke green.
- **M2bis — loop-cost fixes: PARTIAL (2026-10-11).** OpenRouter API key
  stored (gitignored `.env`, `OPENROUTER_API_KEY`); live probe passed —
  `openrouter:z-ai/glm-5.3-flash` (~$0.15/$0.50 per M list; third-party
  routes cheaper). Z.ai signup was geo/identity-blocked for Brad; see
  `writing/machine/2026-10-11-m2-loop-resource-plan.md` §C1 update.
  **Built:** F1 fixture stack (`evals/fixtures/` + `evals/replay.py`;
  evaluators run offline <5 s, no key — verified 1.0/1.0 on m1-tau-sk
  fixture); F2 caches (pipeline-call memoization in `grounded/tools.py`
  keyed on (name, input, graph hash); agent-output cache in
  `run_grounded.ground_run_async` keyed on (model, question, graph hash);
  judge fan-out via `asyncio.gather`).
  **C1 judged run (partial, log (`evals/2026-10-11-m2bis-glm-judged-*`) + tally):**
  GLM judge on the *GLM-run agent*: agent-tau-sk lean-claim score
  **0.600** (6 entailed / 4 not-entailed / 2 insufficient; the judge caught
  genuine overreach incl. SK-well-posedness confusion, CLL direction-of-
  constraint, a REPORT demo-question claim, and a Cockshott attribution);
  baseline **1.000** (5/5; walkthrough cite INSUFFICIENT by design — doc
  moved). GLM judge is far more discriminating than flash-lite was.
  **Halt reason:** the physics-envy agent case ran long (tool-loop heavy,
  12→ claims + openrouter latency); aborted by request. Mitigations
  recorded: the devil is in (a) no claim budget → instructions now cap
  ≤5 claims; (b) run/eval timeout budgets — TODO `--timeout` on
  ground_run_async and per-case wall clock cap; (c) cache — rerun of
  agent-tau-sk is now free (cache hit).
  **Next:** rerun C1 with the 5-claim cap (agent cases cached-where-possible,
  seconds-cheap on OpenRouter); then M3.
- **M2/C1 final rerun (2026-10-11): quality verdict RESOLVED + runtime plan
  executed.**
  - **Quality (GLM-5.3-Flash task + judge, 5-claim cap):** agent-tau-sk =
    CitationSupport 1.00 / LoadBearing 1.00 / ClaimEntailment 0.80 (5
    claims; synthesis correctly separates SK-convergence-certificate vs
    subcharacteristic-limit-validity and flags the A5 contestation);
    baseline = 0.50 / 1.00 / 1.00 (terse meta-claims); physics-envy =
    1.00 / 1.00 (single claim judged NOT ENTAILED — it is a meta-claim
    about the graph, so the judge is right). **Agent ≥ baseline on the
    mechanical metrics, richer synthesis; Pydantic AI stack validated as
    the research top layer.** Report:
    `evals/2026-10-11-c1-glm-report.json`.
  - **Runtime ladder (cold → warm):** 450 s (uncached, pre-cap) → 245 s
    (first warm pass: agents cached, first-ever judge-cache misses) →
    **3.3 s** steady-state full 3-case judged dataset — ~135× loop
    speedup at zero marginal LLM cost. (A 44 s outlier was a fresh
    cache segment for the default google model key, populated after.)
  - **Bugs fixed on the way:** judge `None` return (pydantic-evals rejects
    it) → nothing-verifiable = 0.0; agent-appended edge/node annotations
    in claim `source` now stripped before section resolution
    (`sec_clean`).
  - **Direct plumb spawn (opt-in):** `TARA_PLUMB_DIRECT=1` in
    `knowledge-repository-poc/scripts/pipeline.py` — Nix-built binary +
    `PLUMB_PATH` (built stdlib), saves ~1.0–1.2 s per uncached pipeline
    call (measured 1199 → 23–163 ms), auto-falls back to the canonical
    `nix develop` path on nonzero exit. Equivalence verified end-to-end
    through `grounded/tools.py`; repo smoke green with it off (default).
    Adopt it as the eval default when next milestone work touches this
    surface.
- M2 infra notes: judge/task ratelimit — flash-lite RPD saturates quickly
  on repeat evals; `report.print()` API; EvaluatorContext has `name` (not
  `case.name`); judge must be async inside pydantic-evals (run_sync →
  "event loop is already running").

## Critical finding (do not re-derive)

- **plumb exec boundaries are exact-typed: an extra input key is fatal**
  (`morphism_fatal`, no worker traceback). Example: `trace.plumb` takes
  `{topic, concepts, min_seeds}` — sending `schemas.TraceRequest`'s
  `max_edges: 40` default kills the pipeline. `grounded/tools.py` therefore
  uses boundary-mirror `TraceInput`/`QueryInput` models, not the
  shared schemas. Regression test
  `test_exact_typed_extra_field_is_fatal` covers it.

- **PyPI `persevere-plumbing` 1.1.0 wheels are broken on this machine** —
  the bundled `_bin/plumb` needs `libbsd.so.0`, `libsodium.so.23`,
  `libpgm-5.3.so.0`, `libnorm.so.1`, `libgssapi_krb5.so.2`,
  `libstdc++.so.6`. LD_LIBRARY_PATH fixes libbsd/gssapi/stdc++ but **not**
  libsodium (wheel wants ABI `.so.23`; this Nix store only ships
  libsodium ≥ 1.0.20 = `.so.26`) and libpgm/libnorm are absent entirely.
- **Working setup:** pass the Nix-built binary explicitly —
  `~/tools/plumbing/_build/default/bin/plumb/main.exe` — via the `binary=`
  parameter (both `pb.call_sync`/`run` and `PlumbingModel.__init__` accept
  it; resolution order is explicit → bundled → PATH, no env-var override).
  `spike/m0_spike.py` reads `PLUMB_BIN` env var, defaulting to that path.
- Deps added by M0 (exact-pinned): `pydantic-ai-harness[researcher]==0.55.0`
  (`pydantic-ai-slim==2.55.0`, `pydantic-evals==2.55.0`) and
  `persevere-plumbing[pydantic]` (`pydantic-ai>=0.1`). Compatible with the
  pinned `pydantic==2.13.4` / CPython 3.13 (`pydantic-ai-slim` needs ≥2.12,
  ≥3.11).

- **M3 — pillar fan-out: DONE (2026-10-11).** Island-DT composition
  question refined across the four corpus pillars with per-pillar
  grounding + union evaluation.
  - **Mechanical (M3a, `evals/pillars.py`):** per-pillar traces/queries at
    the pillar's natural gate (fallback trace → per-concept queries) reach
    **4/4 pillars** and cover **11/13** of the recorded min_seeds=1
    bundle — versus the single composed trace at min_seeds=2 that grounded
    only pillar B. Cross-pillar recall is solved by *decomposition*.
  - **Agents (M3b, `evals/fanout_eval.py`):** four pillar-scoped grounded
    researchers run concurrently on the composed question
    (instructions-per-lane; GLM via OpenRouter). UNION of their runs:
    **13/13 bundle sections covered, all 16 claims mechanically
    supported, all four pillar lanes reached** — strictly better than the
    single-process trace at the same precision. Cold wall ≈ 3.5 min for 4
    parallel agents; warm = 5.5 s. Report:
    `evals/2026-10-11-m3-fanout-report.json`.
  - **Decision evidence:** fan-out at pillar granularity is the
    principled recall mechanism when the corpus has an explicit pillar
    taxonomy — embeddings' recall role is not forced here (the corpus
    does have an explicit taxonomy: island-DT pillars, RET×TSSI
    tracks/critique families). Remaining embeddings niche: *unanticipated*
    semantic neighborhoods / unknown taxonomies — see the workspace-level
    open decision note below.
  -   Tests (3 new): bundle-parse (offline), mechanical 4-pillar
    property + nonempty probes (skip-guarded on the binary). 25 passed.

## Testing practice (2026-10-11)

- **Layering:** (1) repo smoke (CI) now includes an *agent harness offline
  contract* — fixture replay through the evaluator stack, no key/nix; (2)
  `tests/` = 22 tests: pipeline integration + exact-boundary regression,
  citation-anchor units, M2 parser/corpus units, fixture replay, judge
  module (schema + cache layer + offline paths), run-cache key semantics
  (incl. the model-segmentation property), `sec_clean`, direct-vs-nix
  plumb equivalence (skips when binary absent); (3) `evals/` = the
  behavioral suite for anything LLM-gated (judged evals, fixtures for the
  LLM-free parts).
- **Practice decision:** classic TDD applies to the deterministic seams
  (caches, parsers, boundary typing, evaluators) — write the regression
  test with the fix, and add a property test when a surprise changes a
  *semantic* (e.g. cache-key segmentation). The LLM-gated paths use
  evals + fixtures, not unit TDD. Test-after remains acceptable when the
  bug defines the spec; keep red-state comments out of the suite.
- Gaps deliberately unwritten: retry/backoff timing (network-shaped,
  covered by live C1 runs), pydantic-eval internals, cache-file pruning.

## Conventions

- Semantic commit prefixes; commit only when asked; push feature branch → PR.
- The agent layer stays *research-reading* scope (no shell/file-edit tools)
  until M6's opencode disposition.
