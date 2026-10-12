---
title: Pydantic AI Researcher as the top layer over plumbing — transition plan
date: 2026-10-10
kind: research-plan
project: agent-harness-poc
---

# Plan: Pydantic AI Researcher as the Top Layer over Plumbing — 2026-10-10

Proposal to bring the plumbing multi-agent capabilities to the **top of the
stack** — the agentic/research layer — instead of leaving them at the bottom of
the stack as deterministic pipeline machinery. The current top layer is
opencode (interactive CLI harness + `plumb` MCP + `hypergraph-grounding`
skill); this plan replaces it, for research workloads, with a **Pydantic AI**
agent harness. Key motivation: plumbing can already run typed workflows *as
Pydantic AI models* (`persevere.plumbing.provider.PlumbingModel`), so the two
stacks interoperate natively once the model — and everything epidemiological
about the intermediate layers — converges on one typed contract.

References:

- Researcher harness: https://pydantic.dev/docs/ai/harness/researcher/
- Pydantic AI Gateway: https://pydantic.dev/docs/ai/overview/gateway
- Plumbing pydantic examples: https://github.com/quantumsoftwarelab/plumbing/tree/main/examples/pydantic/

---

## 1. What the pieces actually are (verified 2026-10-10)

### Pydantic AI side

- **`pydantic-ai-harness` 0.55.0** — `Researcher` is a combined capability
  stack: default research instructions (replaceable), web search + fetch
  (native provider support with local DuckDuckGo/Markdown fallback so claims
  get checked against sources), `SubAgents` delegation, and
  `ToolOutputLimits` (oversized tool results spill to a workspace dir
  `.pydantic-ai-harness/tool-output/`, gitignored). Composes with a typed
  `output_type`, a run `LocalWorkspace`, and durable execution backends
  (Temporal / DBOS / Prefect).
- **Dependencies:** `pydantic-ai-slim==2.55.0`, which requires
  `pydantic>=2.12` and Python ≥ 3.11 — **both compatible with the workspace's
  pinned `pydantic==2.13.4` and CPython 3.13**. Installed uv-style:
  `uv add "pydantic-ai-harness[researcher]"`.
- **Pydantic AI Gateway:** unified multi-provider access under one key
  (`PYDANTIC_AI_GATEWAY_API_KEY`), model strings with a `gateway/` prefix
  (e.g. `gateway/anthropic:claude-fable-5-1`), failover/load-balanced
  endpoints, cost monitoring in Logfire. Endpoints are OpenAI/Anthropic/Google
  -compatible HTTPS proxies (`gateway-us.pydantic.dev/proxy/<fmt>`), so any
  OpenAI-compatible client can point at them.

### Plumbing side

- **`persevere-plumbing` 1.1.0 on PyPI** with a `[pydantic]` extra exposes:
  - *Bare API*: `pb.call_sync(spec, message)` — run a `.plumb` pipeline
    directly from Python.
  - *`PlumbingModel`*: a plumbing pipeline registered **as a Pydantic AI
    model** (the pipeline plays "the model"); supports stateful multi-turn
    via `message_history`. Early-stage — ideal for evals/benchmarking, not
    yet a research-grade LLM substitute.
- **Local `~/tools/plumbing`** is up to date with upstream (`7a8028c`,
  main == origin) and already contains
  `examples/pydantic/{bare.py, eval.py, pipeline.plumb}` (identity pipeline,
  no API key required). No upstream sync needed for the source; only the pip
  install is missing.

### Current workspace layers (unchanged by this plan)

```
today:
  opencode (LLM + chat + skills + MCP)  →  plumb MCP  →  pipelines/ exec workers
                                                          (tara-python, pydantic schemas)

proposed:
  top:  Pydantic AI agent (Researcher harness, typed output_type)
        ├─ tools: knowledge-repo pipelines (query/trace/trace_report/evidence/expand)
        ├─ (optional) PlumbingModel: pipeline-as-model for evals / deterministic agents
        └─ SubAgents: per-pillar researchers (island-DT), per-track critiques (RET×TSSI)
  down: plumbing (plumb binaries + exec workers)        ← unchanged, stays deterministic
  desc: build_hypergraph.py + graph artifacts           ← unchanged
```

**Two plumbing integration modes, both useful:**

1. **Tool mode (default):** the agent calls pipelines via typed tool functions
   wrapping `pipeline.py` contracts (schemas already live in
   `projects/knowledge-repository-poc/scripts/schemas.py`). Robust,
   deterministic boundaries.
2. **Model mode (`PlumbingModel`):** a whole pipeline plays "the model" —
   early-stage; ideal for `pydantic-evals` benchmarking of pipelines, not
   (yet) for research runs.

---

## 2. Decisions recorded (2026-10-10, Brad)

- **Placement:** new standalone project thread under `projects/`
  (tracked-by-default policy): `projects/agent-harness-poc/`.
  `knowledge-repository-poc/` stays untouched as the reference implementation.
- **First acceptance milestone:** the **grounded research agent** — reproduce
  the quality of the stored opencode-side trace
  `projects/knowledge-repository-poc/graph/grounded-answer-tau-sk.md` from
  pipeline tools only.
- **opencode fate:** undecided for now — keep it in parallel during
  transition; revisit after the existence proof.
- **Provider:** eventually the **Pydantic AI Gateway**, with one caveat
  recorded as a milestone: *plumbing does not support the gateway yet* → the
  "plumbing `agent` morphism routes through the gateway" is an explicit
  downstream milestone (M5). Interim: a direct provider key.

---

## 3. Milestones

- **M0 — Spike (no API key required)** (~1 h)
  `uv add pydantic-ai-harness[researcher]` and `persevere-plumbing[pydantic]`
  into `pyproject.toml`/`uv.lock`; inside `nix develop ~/tools/plumbing` run
  upstream's `bare.py` (bare API) and `eval.py` (`PlumbingModel`) with the
  identity pipeline. **This milestone exists to burn down the biggest unknown:
  the pip-wheels / libzmq / libstdc++ risk.** Exit: both examples print echoed
  output.

- **M1 — Tool bridge** (needs a provider key)
  Typed tool functions wrapping `pipeline.py` for `query`, `evidence`,
  `trace`, `trace_report`, `expand`, schemas derived from
  `scripts/schemas.py` (tara-python still fronts the exec workers). Port the
  `hypergraph-grounding` skill's SKILL.md instructions into agent
  instructions; grounding rule "cite `doc :: section`" becomes the
  `output_type` schema: `GroundedAnswer(claims: list[Claim(source)])`.
  **Acceptance: reproduce the `grounded-answer-tau-sk.md` answer quality with
  the new agent.**

- **M2 — Eval**
  `pydantic-evals` registration of the grounding task (citation-support rate:
 does each cited `doc :: section` actually imply the claim, judged against the
  trace baseline produced by the opencode-side pairing); optionally register
  one pipeline through `PlumbingModel` as a deterministic eval agent.

- **M3 — Multi-pillar fan-out**
  `SubAgents` / `Dynamic Workflow`: parallel researchers per island-DT pillar
  (metabolism / 3D standards / LDT ecosystem / geodesign). Test whether
  fan-out + union evidence matches the `min_seeds=1` union-bundle recall
  measurement (13 sections across four pillars). This generates corpus
  evidence for the open embeddings-vs-Phase-C decision: fan-out may be the
  principled recall-widener instead of embeddings.

- **M4 — Gateway cutover: DEMOTED TO OPTIONAL (2026-10-12, decided post-C1/M3).**
  Original goal: Logfire account → Gateway key (`PYDANTIC_AI_GATEWAY_API_KEY`)
  → model strings become `gateway/...`; spending limits + cost monitoring
  apply from here on.
  Reassessment after the OpenRouter GLM tier proved out: **not needed**.
  - The workhorse (GLM-5.3-Flash, task + judge of record) is *not* a gateway
    built-in provider — it stays OpenRouter-direct regardless, so a cutover
    only ever covers Google/Anthropic traffic we rarely send (fallback tier
    $0; one-off Anthropic calibration ~$5).
  - Cost control already holds at this volume: runs cost pennies, OpenRouter
    top-ups are hard spending caps, its dashboard gives per-request costs.
  - Failover is handled at the architecture layer (agent cache → GLM tier →
    Gemini free tier → OpenRouter free router → Ollama local), which is more
    robust than gateway mid-run failover for short cached runs.
  - M5 does not depend on it: plumbing's `agent` morphism can point at *any*
    OpenAI-compatible endpoint (resource plan §4 Phase C3: config knob, not
    code).
  - The observability value is separable: Pydantic AI instruments to Logfire
    (OpenTelemetry) without `gateway/` strings, if ever wanted.
  - Net residual loss of skipping: ~5.5% OpenRouter fee on the one-off
    Anthropic calibration ≈ $0.28. Immaterial.
  Revisit condition (folded into M6): multi-provider consolidation pain, or a
  recurring Anthropic workload — then Logfire Personal (free, BYOK 0%
  markup) + `gateway/...` strings.

- **M5 — Plumbing agent endpoint: DONE (2026-10-12).** Delivered via pure
  config (no plumbing code change, matching the resource-plan §4 C3
  preposition): `pipelines/agent.plumb` binds the `agent` morphism with
  `provider: "openai"`, `model: "z-ai/glm-5.3-flash"`,
  `api_key: "${OPENROUTER_API_KEY}"`, `endpoint: "https://openrouter.ai/api/v1"`
  — the OpenAI-compatible proxy work already shipped upstream, so the
  "gateway-shaped" M5 aspiration reduces to a config recipe. Plumb `check`
  validates types *and* `${VAR}` presence (doubles as key-presence check);
  `scripts/pipeline.py` now loads the gitignored `.env` (existing env wins)
  so the standard runner and smoke work unchanged. **Live acceptance:**
  typed `{topic} -> {answer, confidence}` round-trip through the fabric
  (GLM answered a TSSI question; correctness spot-checked). Findings:
  GLM-5.3-Flash needs `max_tokens: 4096` (thinking tokens count: a two-
  sentence answer still cost ~1.1k tokens; 256/1024 budgets fail the
  fabric's max_tokens contract, exit 1 — contract correctness observed);
  the agent binary respects `PLUMB_PROVIDER`/`PLUMB_MODEL` env knobs when
  config omits them; telemetry on stderr vs payload on stdout is unchanged.
  Tests: `tests/test_agent_pipeline.py` (spec presence, type-check pass,
  missing-env rejection, dotenv loader) — 29 passed. Smoke: `agent pipeline
  contract (plumb check, key-gated)` check added.

- **M6 — Cutover / disposition**
  Retarget the key workflows (hypergraph-grounding Q&A, island-DT cross-pillar
  assembly) from opencode chat to scripted agent sessions
  (`agent.to_cli_sync()` for interactive use). **Decide opencode's fate here**
  (keep for coding sessions / full replacement) on evidence, per the recorded
  "undecided" decision.

---

## 4. Challenges (ranked)

1. **pip wheels may still be broken** (missing libnorm/libpgm/libsodium
   sonames; libstdc++ needs). Mitigations: install/run inside the
   `nix develop ~/tools/plumbing` environment; or `uv sync` and point
   `LD_LIBRARY_PATH` at the Nix-built sonames. If any transitive dep lands a
   torch-class native wheel, the workspace's CPU-pin discipline applies.

2. **Harness 0.x churn:** `pydantic-ai-harness` may change API between minor
   releases. Pin exact versions in `uv.lock`; upgrades deliberate
   (deprecation warnings + release notes are the upgrade path).

3. **`PlumbingModel` is early:** the example is a stateful identity pipeline;
   real pipelines with strict `exec` boundaries and typed output may reject
   model-shaped traffic. Keep Model mode eval-only until M2 shows otherwise.

4. **Contract fidelity:** exec workers run through `tara-python` with
   exact-typed, pydantic-validated IO and *fatal* mismatches at the boundary;
   tool wrappers must round-trip bytearray-exact JSON, or failures look
   opaque. Initial guess: derive tool schemas from `schemas.py` rather than
   re-typing.

5. **Loss of interactive UX / codex-like guardrails vs opencode:** the raw
   Pydantic AI agent doesn't ship per-AGENTS.md conventions, hot-loaded
   skills, git safety rules, or the coding toolchain. Mitigation: design the
   new agent **read-only-by-construction** (no shell/file-edit tools;
   `Researcher` + `RetryToolOutputLimits`; spills under a gitignored dir) so
   guardrails become unnecessary rather than reimplemented. Agent instructions
   are versioned files inside the new thread. opencode stays live throughout.

6. **CI:** extend `projects/knowledge-repository-poc/scripts/smoke.py` with a
   key-gated agent-layer import check and tool-wrapper contract check, which
   must skip gracefully when no key exists (pattern: the existing
   fulltext-local skip).

7. **Secrets discipline:** provider/Gateway keys via gitignored `.env` /
   environment only; never through worker contracts or commits (repo is
   public). Anything that ever touches commit history gets rotated.

8. **Scope discipline:** the new agent is a *research harness*, not a coding
   agent. Its job: grounded answers, evidence traces, corpus expansion —
   mirroring the skills it replaces. Cross-compile agentic coding (opencode)
   and research (this agent) remain separate until M6 forces a call.

---

## 5. Verification at each step

- M0: examples run inside the nix env, no flakes.
- M1: tau-sk reproduction diffed against the stored trace
  (`grounded-answer-tau-sk.md`); every claim citation resolves to a section
  that grounded it.
- M2: eval score ≥ the opencode-baseline citation-support rate on the same
  task; device reproducible `pytest` ephemeral job.
- M3: cross-pillar union bundle compared to the stored `min_seeds=1`
  measurement; write findings into the island-DT thread.
- Always: `uv run python projects/knowledge-repository-poc/scripts/smoke.py`
  stays green; graph artifacts rebuild deterministically (`ingest`).

---

## 6. Standing-fact reminders (do not re-derive)

- Python stack is uv-managed; never re-add loose `requirements.txt` entries.
  All additions through `uv add` / `pyproject.toml` + a committed `uv.lock`.
- plumbing binaries: Nix source build at `~/tools/plumbing`
  (`nix develop ~/tools/plumbing -c
  ~/tools/plumbing/_build/default/bin/...`). Pip wheels are broken. Pipelines
  assume cwd = `pipelines/`.
- No LLM provider key exists today — M0 is the only milestone unaffected.
- opencode remains the interactive tool until M6; the plumb MCP + skill
  registry stay live (config changed this session requires a restart to
  load).
- Commit conventions: semantic prefixes; commit/PR only when asked; never
  push `main`.
