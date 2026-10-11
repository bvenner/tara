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
- M2 infra notes: judge/task ratelimit — flash-lite RPD also saturates
  quickly when running repeat evals; `report.print()` API; EvaluatorContext
  has `name` (not `case.name`); judge must be async inside pydantic-evals
  (run_sync → "event loop is already running").

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

## Conventions

- Semantic commit prefixes; commit only when asked; push feature branch → PR.
- The agent layer stays *research-reading* scope (no shell/file-edit tools)
  until M6's opencode disposition.
