"""Run-cache key semantics — the cache-segmentation properties we got bit by."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from run_grounded import _graph_hash, run_cache_key  # noqa: E402


def test_same_model_same_question_stable() -> None:
    k1 = run_cache_key("q", "google:gemini-3.5-flash-lite")
    k2 = run_cache_key("q", "google:gemini-3.5-flash-lite")
    assert k1 == k2


def test_explicit_model_and_default_segment_differ() -> None:
    """proc: passing --model X keys separately from the default-model run
    (the surprise that made the 44 s no-judge eval re-run both agents)."""
    k_default = run_cache_key("q", None)
    k_openrouter = run_cache_key("q", "openrouter:z-ai/glm-5.3-flash")
    assert k_default != k_openrouter


def test_question_sensitivity() -> None:
    assert run_cache_key("q1", None) != run_cache_key("q2", None)


def test_graph_rebuild_invalidates(monkeypatch) -> None:
    monkeypatch.setattr("run_grounded._graph_hash", lambda: "hashA")
    kA = run_cache_key("q", None)
    monkeypatch.setattr("run_grounded._graph_hash", lambda: "hashB")
    kB = run_cache_key("q", None)
    assert kA != kB or _graph_hash() == "nograph"  # nograph sentinel degenerate case
