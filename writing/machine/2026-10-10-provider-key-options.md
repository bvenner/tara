# Provider Key Options — 2026-10-10

Context: `agent-harness-poc` M1 (tool bridge + grounded research agent) needs
an LLM provider key; none exists today. Usage profile: **sporadic research
runs** (a few per week, 50–200 model calls each with tool loops, <1M tokens
per run) — cost pressure is low, but self-serve friction and stack
compatibility matter. Gateways/extras status: `pydantic-ai-slim` base is
installed (M0); provider extras (`[google]`, `[anthropic]`, `[openai]`)
pending on choice. Privacy standing rule from the audio note applies: nothing
employer-considered / DSA / transcript material goes through any
free-tier-or-training endpoint.

---

## Options

### 1. Google Gemini free tier (recommended for M1–M2)

- **Cost: $0.** Google AI Studio key, no credit card, no minimum.
- Generous for this profile: Flash models ~1,500 requests/day free (1M TPM);
  grounded Google Search 500 requests/day free on 2.5 Flash/Flash-Lite (the
  free-tier search quota matters — the agent's
  `WebSearch`/`WebFetch` can go native).
- Pydantic AI: `google:gemini-3.8-flash` via `pydantic-ai-slim[google]`
  (prefix is `google:`, not `google-gla:`, in slim 2.55; `gemini-2.5-flash`
  is no longer available to new users as of Oct 2026 — 3.8 Flash is the
  current free-tier workhorse).
- **Caveats:** free-tier prompts/data may be used for model training (fine
  for the public research corpus; the same privacy rule above applies);
  limits are unpublished (shown per project in AI Studio); since
  2026-06-19 unrestricted API keys are rejected — create a **restricted**
  key (Generative Language API only; also good practice).
- M1–M2 run cost at this tier: ~$0 per grounded run.

### 2. Pydantic AI Gateway + Logfire Personal (recommended as the M4 path, adoptable early)

- **Cost: $0 base.** Logfire Personal plan (free, hard-capped): gateway
  included, **BYOK = 0% markup** (up to 3 provider credentials), built-in
  providers = 5% markup, 10M telemetry records/month.
- Route research runs through `gateway/...` model strings / `gateway_provider`
  with one `PYDANTIC_AI_GATEWAY_API_KEY`; failover/load-balancing endpoints
  and request logging (OTel) come with it.
- Practically: create one underlying key (option 1, 3, or 4), register it as
  a BYOK credential, and the agent stack changes only in the model-string
  prefix. **M5 (plumbing `agent` through the gateway)** still benefits.
- Caveat: BYOK still bills the underlying provider; "free" = the gateway
  layer itself.

### 3. Anthropic direct (quality option)

- **Cost: $5 card deposit minimum**, pay-as-you-go after. Claude Sonnet
  ~$5/M in + ~$25/M out (cache hits ~$0.50/M); native web search ~$10/1k
  searches.
- Best-grounded answers for the citation-support eval in M2; no-training
  default. At this profile expect ~$1–3 per grounded run — trivial.
- Pydantic AI: `anthropic:claude-...` via `pydantic-ai-slim[anthropic]`.

### 4. OpenRouter (variety option)

- Free plan: 25+ free models incl. the `openrouter/free` router — but only
  *50 requests/day* on the free plan, too few for a tool-loop research
  agent's sustained runs.
- Standard pay-as-you-go: one key, 500+ models, **5.5% platform fee** on
  tokens, switch models without changing code. Reasonable mid-step if we
  want multiple model families from one key without the gateway.

### Rejected

- **Groq** usable free tier is small (per model: 1k req/day, 200k tokens/day,
  8k TPM — a tool loop exhausts it in 3–4 turns), and self-serve upgrades
  were paused for new paid accounts (last checked 2026-09-16).
- **Ollama/local**: free and offline but slow; weak at structured
  tool-looping; keep as fallback for keyless demos only.
- **DeepSeek**: cheap (~$0.2/M) but a separate ecosystem + data-residency
  considerations; no advantage over Gemini free for this profile.

---

## Recommendation

**Step 1 (now):** get a **restricted Google AI Studio key** (option 1,
~5 min, no card). Set `GOOGLE_API_KEY`. Unblock M1 at zero cost; add
`pydantic-ai-slim[google]`.
**Done 2026-10-10:** key obtained, stored in gitignored `.env`
(`-rw-------`); live check passed with `google:gemini-3.8-flash`. Note:
`python-dotenv` loads `.env` for the workers; a bare `uv run python -c`
needs `set -a && . ./.env && set +a` first.

**Step 2 (at M4 or earlier if convenient):** create a Logfire account
(Personal/free), register the same key as a BYOK gateway credential, switch
model strings to `gateway/google-gla:...` (or `gateway_provider(...)`), set
`PYDANTIC_AI_GATEWAY_API_KEY` + `PYDANTIC_AI_GATEWAY_BASE_URL` (gateway-us).
Zero markup, monitoring + cost trail inline, and M4/M5 stay on the recorded
track.

**Discretionary:** if M2's citation-support eval needs a stronger judge than
Flash, add a $5 Anthropic deposit and route Claude Sonnet as the eval judge
(or through the gateway as a second BYOK credential).

Sources:

- Gateway/Logfire pricing: https://pydantic.dev/pricing ,
  https://pydantic.dev/logfire/ai-gateway ,
  https://pydantic.dev/articles/logfire-pricing-change ,
  https://pydantic.dev/articles/gateway-merging-into-logfire
- Gemini free tier/limits: https://ai.google.dev/gemini-api/docs/rate-limits ,
  https://ai.google.dev/gemini-api/docs/pricing
- OpenRouter free plan: https://openrouter.ai/pricing ,
  https://openrouter.ai/docs/guides/routing/routers/free-router
- Anthropic list prices 2026-08-31: platform.claude.com rate card (PDF)
