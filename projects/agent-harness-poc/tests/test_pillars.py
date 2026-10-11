"""M3 tests — bundle parse + the mechanical fan-out property (skip-guarded)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest  # noqa: E402

from evals.pillars import PILLAR_DOC_MARKERS, prior_bundle, union_metrics  # noqa: E402


def test_prior_bundle_parse() -> None:
    bundle = prior_bundle()
    assert len(bundle) == 13
    # four pillars must be represented in the recorded bundle
    island_secs = {s for d, s in bundle if d.startswith("island-dt")}
    for p, marker in PILLAR_DOC_MARKERS.items():
        assert any(sec.startswith(marker) for sec in island_secs), p


@pytest.mark.skipif(
    not (Path.home() / "tools/plumbing/_build/default/bin/plumb/main.exe").exists(),
    reason="Nix-built plumb binary not present",
)
def test_mechanical_fanout_reaches_all_pillars() -> None:
    """The fan-out hypothesis, fixed as a property: per-pillar grounding with
    the researcher fallback (trace → per-concept queries, per-pillar gate)
    spans all four pillars without a global min_seeds=1 drop."""
    metrics = union_metrics()
    assert metrics["pillars_reached_count"] == 4


@pytest.mark.skipif(
    not (Path.home() / "tools/plumbing/_build/default/bin/plumb/main.exe").exists(),
    reason="Nix-built plumb binary not present",
)
def test_pillar_probes_are_nonempty() -> None:
    probes = __import__("evals.pillars", fromlist=["pillar_probes"]).pillar_probes()
    for name, data in probes.items():
        assert data["anchors"], f"pillar {name} produced no anchors"
