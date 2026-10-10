"""Fast offline tests for the citation anchor extraction and matching."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from evals.check_citations import anchors_from_sidecar, supported  # noqa: E402

SIDE = {
    "tool": "knowledge_trace",
    "content": {
        "hits": [
            {"doc": "ret-tssi/findings.md", "section": "5. Model skeleton (Track A, Phase 1 — candidate Master's problem)"}
        ]
    },
}
SIDE_TEXT = {
    "tool": "knowledge_trace_report",
    "content": json.dumps(
        "### ret-tssi/program/critiques.md :: A1. \"Physics envy — this is a metaphor, not a model\"\nmore"
    ),
}


def test_sidecar_anchor_extraction(tmp_path) -> None:
    sidecar = tmp_path / "run.tools.json"
    sidecar.write_text(json.dumps([SIDE, SIDE_TEXT]))
    anchors = anchors_from_sidecar(sidecar)
    assert ("ret-tssi/findings.md", "5. Model skeleton (Track A, Phase 1 — candidate Master's problem)") in anchors
    assert ("ret-tssi/program/critiques.md", "A1. \"Physics envy — this is a metaphor, not a model\"") in anchors


def test_supported_matches() -> None:
    anchors = {("ret-tssi/findings.md", "5. Model skeleton (Track A, Phase 1)")}
    assert supported("ret-tssi/findings.md :: 5. Model skeleton (Track A, Phase 1)", anchors)
    assert supported("ret-tssi/findings.md :: 5. Model skeleton", anchors)  # prefix
    assert not supported("ret-tssi/findings.md :: 9. Unrelated", anchors)
