"""M6 slice 1 — workload manifest schema + harness-agnostic runner tests.

LLM-gated adapters (pydantic-agent, mechanical-probe needing pipelines)
are deliberately NOT exercised here; the behavioral evidence lives in the
run-workload CLI reports.
"""
import asyncio
import json
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
        "static-baseline", "opencode-artifact", "pydantic-agent",
        "pydantic-agent-fanout", "mechanical-probe", "plumb-agent",
        "plumb-agent-fanout",
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


def test_plumb_adapters_require_seeds():
    """The plumb arm refuses to run when neither trace seeds nor lanes
    provide concepts (manifest contract)."""
    from pydantic import ValidationError
    from grounded.workloads import WorkloadManifest

    m = WorkloadManifest.model_validate(
        {"id": "x", "title": "t", "kind": "grounding-qa", "question": "q"}
    )
    with pytest.raises(ValueError, match="no seeds"):
        ADAPTERS["plumb-agent"](m)


def test_plumb_payload_parse_offline(tmp_path):
    from run_grounded import GroundedRun  # noqa: F401
    from grounded.workloads import parse_plumb_payload

    sidecar = tmp_path / "trace.jsonl"
    sidecar.write_text(
        '{"topic": "q", "min_seeds": 3, "tags": [], "seeds": [],'
        ' "hits": [{"edge_id": "e1", "doc": "d.md", "section": "S",'
        ' "arity": 2, "seeds": [], "nodes": []}], "distinct_sections": 1}\n'
    )
    payload = {
        "synthesis": "grounded synthesis text",
        "claims": [
            {"statement": "c1", "source": "d.md :: S", "trace_edge_ids": ["e1"]},
            {"statement": "c2", "source": "d.md :: S2"},
        ],
    }
    run = parse_plumb_payload(payload, "q", tmp_path)
    assert isinstance(run, GroundedRun)
    assert run.answer.synthesis == "grounded synthesis text"
    assert len(run.answer.claims) == 2
    assert run.answer.claims[1].trace_edge_ids == []
    assert run.anchors == [("d.md", "S")]


# Cross-arm scorer contract: the SAME support check scores plumb claims.
def test_plumb_claim_scoring_parity():
    from evals.check_citations import supported

    anchors = {("d.md", "S")}
    assert supported("d.md :: S", anchors)
    assert not supported("other.md :: S", anchors)


def test_normalize_claim_source():
    from grounded.workloads import normalize_claim_source

    assert normalize_claim_source("d.md — [Some section]") == "d.md :: Some section"
    assert normalize_claim_source("d.md :: [Some section]") == "d.md :: Some section"
    # section text may itself contain an em-dash — bracket form keeps it whole
    assert normalize_claim_source("d.md — [A. Flow layer — the flow layer]") == \
        "d.md :: A. Flow layer — the flow layer"
    # canonical form passes through untouched
    assert normalize_claim_source("d.md :: S") == "d.md :: S"


def test_research_gate_fallback_offline():
    """The deterministic gate worker: trace miss → per-concept query union,
    with section-content evidence when the resolver is importable. Uses the
    real (committed) graph artifacts; no nix/LLM/key."""
    import subprocess as sp
    import sys as _sys

    script = Path(__file__).resolve().parents[2] / "knowledge-repository-poc" / "scripts" / "research_gate.py"
    if not script.exists():
        pytest.skip("research_gate.py not present")
    p = sp.run([_sys.executable, str(script)],
               input=json.dumps({"topic": "probe", "concepts": ["digital twin"], "min_seeds": 3}) + "\n",
               capture_output=True, text=True, timeout=120)
    assert p.returncode == 0, p.stderr[-300:]
    tr = json.loads(p.stdout.strip().splitlines()[-1])
    assert tr["min_seeds"] in (3, 1)
    assert len(tr["hits"]) > 0            # fallback fire or direct hit
    assert "evidence" in tr               # content prefetch field present


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
