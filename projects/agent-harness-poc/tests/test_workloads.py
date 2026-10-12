"""M6 slice 1 — workload manifest schema + harness-agnostic runner tests.

LLM-gated adapters (pydantic-agent, mechanical-probe needing pipelines)
are deliberately NOT exercised here; the behavioral evidence lives in the
run-workload CLI reports.
"""
import asyncio
from pathlib import Path

import sys
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from grounded.workloads import (  # noqa: E402
    load_manifest,
    bundle_from_doc,
    evaluate,
    ADAPTERS,
)
from run_grounded import GroundedRun, GroundedAnswer, Claim  # noqa: E402


def test_both_manifests_validate():
    for name in ("tau-sk-grounding", "island-dt-crosspillar"):
        m = load_manifest(name)
        assert m.question and m.kind in ("grounding-qa", "cross-pillar-assembly")
        assert m.instructions_file and (Path(__file__).resolve().parents[1] / m.instructions_file).exists()
        if m.lanes:
            assert all(l.seed_concepts and l.instructions for l in m.lanes.values())


def test_manifest_schema_rejects_bad_kind():
    from grounded.workloads import WorkloadManifest
    with pytest.raises(ValueError):
        WorkloadManifest.model_validate(
            {"id": "x", "title": "t", "kind": "bogus", "question": "q"}
        )


def test_load_manifest_missing():
    with pytest.raises(FileNotFoundError):
        load_manifest("no-such-workload")


def test_registry_adapters_complete():
    expected = {
        "static-baseline", "pydantic-agent", "pydantic-agent-fanout",
        "mechanical-probe", "plumb-agent", "plumb-agent-fanout",
    }
    assert set(ADAPTERS) == expected


def test_static_baseline_adapter_offline():
    baseline = (Path(__file__).resolve().parents[2]
                / "knowledge-repository-poc" / "graph" / "grounded-answer-tau-sk.md")
    if not baseline.exists():
        pytest.skip("recorded baseline artifact not present")
    m = load_manifest("tau-sk-grounding")
    runs = asyncio.run(ADAPTERS["static-baseline"](m))
    metrics = evaluate(m, runs)
    run_metrics = metrics["runs"][0]
    # mirrors the recorded M2 static-case values (corpus-drift finding)
    assert run_metrics["citation_support"] == 0.5
    assert run_metrics["load_bearing_coverage"] == 1.0


def test_plumb_adapters_are_m7_stubs():
    m = load_manifest("tau-sk-grounding")
    for adapter in ("plumb-agent", "plumb-agent-fanout"):
        with pytest.raises(NotImplementedError):
            ADAPTERS[adapter](m)


def test_bundle_from_doc():
    bundle = bundle_from_doc("knowledge-repository-poc/graph/evidence-trace-island-dt.md")
    assert len(bundle) == 13          # the recorded min_seeds=1 union bundle


def test_crosspillar_evaluation_shape():
    m = load_manifest("island-dt-crosspillar")
    # synthetic single-lane run over one *real* pillar-A bundle pair → 1 lane
    bundle = dict.fromkeys(sorted(bundle_from_doc(
        "knowledge-repository-poc/graph/evidence-trace-island-dt.md")))
    doc, sec = [p for p in bundle if " :: A." in f"{p[0]} :: {p[1]}"][0]
    run = GroundedRun(
        question=m.question,
        answer=GroundedAnswer(
            question=m.question,
            synthesis="x" * 60,
            claims=[Claim(statement="s", source=f"{doc} :: {sec}")],
        ),
        anchors=[(doc, sec)],
        tools_called=["knowledge_trace"],
    )
    metrics = evaluate(m, [run])
    assert metrics["prior_bundle_sections"] == 13
    assert metrics["bundle_covered_by_union"] == 1
    assert metrics["pillars_reached_count"] == 1
    reached_lane = [k for k, v in metrics["pillars_reached"].items() if v]
    assert reached_lane == ["A-metabolism"]
