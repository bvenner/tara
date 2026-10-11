"""LLM-as-judge claim-entailment support (M2).

A judge agent decides whether a cited corpus section supports a claim.
Judge model is pluggable: `AGENT_JUDGE` env var (default
`google:gemini-3.5-flash-lite`; for the real quality verdict use
`google:gemini-3.8-flash` after its free-tier quota resets — 20 req/day —
or an Anthropic key).
"""

from __future__ import annotations

import asyncio
import os
import time
from pathlib import Path

import dotenv
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.exceptions import ModelHTTPError

dotenv.load_dotenv(Path(__file__).resolve().parents[3] / ".env")

JUDGE_MODEL = os.environ.get("AGENT_JUDGE", "google:gemini-3.5-flash-lite")
MAX_SECTION_CHARS = 6000


class Judgement(BaseModel):
    verdict: str = Field(pattern=r"^(ENTAILED|NOT ENTAILED|INSUFFICIENT)$")
    reason: str = Field(max_length=3000, default="")


def build_judge() -> Agent[Judgement]:
    return Agent(
        JUDGE_MODEL,
        instructions=(
            "You assess whether a single corpus section excerpt supports one atomic claim. "
            "Verdicts: ENTAILED (excerpt states or clearly justifies the claim), "
            "NOT ENTAILED (excerpt contradicts or does not support it), "
            "INSUFFICIENT (excerpt lacks the content needed to judge). "
            "Do not use outside knowledge; judge only against the excerpt."
        ),
        output_type=Judgement,
        retries=2,
    )


async def judge_claim_raw(agent: Agent[Judgement], section_text: str, claim: str) -> Judgement:
    if not section_text.strip():
        return Judgement(verdict="INSUFFICIENT", reason="section text unavailable")
    excerpt = section_text[:MAX_SECTION_CHARS]
    question = (
        f"SECTION EXCERPT:\n\"\"\"{excerpt}\"\"\"\n\n"
        f"CLAIM:\n\"\"\"{claim}\"\"\"\n\n"
        "Which verdict is correct for this claim against the excerpt?"
    )
    last_exc: Exception | None = None
    for attempt in range(3):
        try:
            return (await agent.run(question)).output
        except ModelHTTPError as exc:
            if exc.status_code not in (429, 500, 503):
                raise
            last_exc = exc
            await asyncio.sleep(10.0 * (attempt + 1))
    assert last_exc is not None
    return Judgement(verdict="INSUFFICIENT", reason=f"judge rejected after retries: {last_exc}")


# Judge-verdict cache: a (judge model, claim, section-excerpt-hash) address
# deterministically maps to one verdict, so warm eval reruns don't re-call
# the judge. Bypass with TARA_NO_JUDGE_CACHE=1.
def judge_claim(agent: Agent[Judgement], section_text: str, claim: str) -> "asyncio.Future[Judgement]":
    import hashlib

    key = hashlib.sha1(
        f"{JUDGE_MODEL}|{claim}|{section_text[:MAX_SECTION_CHARS]}".encode()
    ).hexdigest()[:16]
    cache_file = _judge_cache_dir() / f"{key}.json"
    no_cache = os.environ.get("TARA_NO_JUDGE_CACHE") == "1"

    if not no_cache and cache_file.exists():
        try:
            cached = Judgement.model_validate_json(cache_file.read_text())
        except Exception:
            cached = None
        if cached is not None:

            async def _hit() -> Judgement:
                return cached

            return _hit()

    async def _miss() -> Judgement:
        verdict = await judge_claim_raw(agent, section_text, claim)
        cache_file.parent.mkdir(parents=True, exist_ok=True)
        cache_file.write_text(verdict.model_dump_json())
        return verdict

    return _miss()


def _judge_cache_dir() -> Path:
    return Path(__file__).resolve().parents[1] / "evals" / "cache" / "judges"
