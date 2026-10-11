"""Judge module tests — no LLM needed (schema, cache layer, offline paths)."""

import asyncio
import hashlib
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest  # noqa: E402

from grounded import judge  # noqa: E402


def test_judgement_rejects_bad_verdict() -> None:
    from pydantic import ValidationError

    with pytest.raises(ValidationError):
        judge.Judgement(verdict="MAYBE", reason="")


def test_empty_section_is_insufficient_without_network() -> None:
    j = asyncio.run(judge.judge_claim_raw(None, "", "some claim"))  # agent unused on this path
    assert j.verdict == "INSUFFICIENT"
    assert "unavailable" in j.reason


def test_judge_cache_hit_and_bypass(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(judge, "_judge_cache_dir", lambda: tmp_path / "judges")
    # Pre-seed the cache the same way a real judge run would have.
    verdict_file = judge._judge_cache_dir()
    verdict_file.mkdir(parents=True, exist_ok=True)
    key = hashlib.sha1(
        f"{judge.JUDGE_MODEL}|the claim|section text".encode()
    ).hexdigest()[:16]
    (verdict_file / f"{key}.json").write_text(
        json.dumps({"verdict": "ENTAILED", "reason": "cached probe"}))

    agent = object()  # cache hit must never touch the agent
    run = asyncio.run(judge.judge_claim(agent=agent, section_text="section text", claim="the claim"))
    assert run.verdict == "ENTAILED"

    os.environ["TARA_NO_JUDGE_CACHE"] = "1"
    try:
        with pytest.raises(Exception):
            # bypass must actually go to the network; object() as agent fails fast
            asyncio.run(judge_claim(agent=agent, section_text="section text", claim="the claim"))
    finally:
        os.environ.pop("TARA_NO_JUDGE_CACHE", None)
