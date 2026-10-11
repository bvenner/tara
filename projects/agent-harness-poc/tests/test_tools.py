"""Integration tests: the tool bridge hits the real pipelines (LLM-free)."""

import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pytest  # noqa: E402

from grounded import tools  # noqa: E402


def test_knowledge_query() -> None:
    result = tools.knowledge_query("tau_J")
    assert result.concept == "tau_J"
    assert result.matched_nodes


def test_knowledge_trace() -> None:
    result = tools.knowledge_trace(
        topic="test trace",
        concepts=["tau_J", "sk condition"],
        min_seeds=2,
    )
    assert result.topic == "test trace"
    assert result.hits


def test_knowledge_evidence_and_report() -> None:
    bundle = tools.knowledge_evidence("tau_J", max_edges=3)
    assert "tion" in bundle  # any markdown text at all
    report = tools.knowledge_trace_report(
        topic="test", concepts=["tau_J", "T3"], min_seeds=2
    )
    assert "tech" in report or "hyperedge" in report.lower() or len(report) > 100


def test_exact_typed_extra_field_is_fatal() -> None:
    """Guard the exact-typed boundary: extra `max_edges` key must fail the morphism."""
    req = '{"topic":"t","concepts":["tau_J"],"min_seeds":1,"max_edges":40}'
    proc = subprocess.run(
        [sys.executable, str(tools.PIPELINE_PY), "trace", req],
        capture_output=True,
        text=True,
        timeout=600,
        cwd=str(tools.THAR_DIR),
    )
    assert proc.returncode != 0
