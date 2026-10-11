"""F1: replay fixtures through the deterministic evaluators (offline, <5s)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest  # noqa: E402

from evals.grounding_eval import CitationSupport, LoadBearingCoverage, Structure  # noqa: E402
from evals.replay import available, load_run  # noqa: E402


class _Ctx:
    """Minimal stand-in for EvaluatorContext (these evaluators read only
    `output` and `name`)."""

    def __init__(self, output) -> None:
        self.output = output
        self.name = "fixture"


@pytest.mark.parametrize("name", ["m1-tau-sk"])
def test_fixture_stack_evaluators(name: str) -> None:
    assert name in available()
    run = load_run(name)
    assert run.answer.claims, "fixture must parse with ≥1 claim"
    assert run.anchors, "fixture sidecar must yield anchors"
    ctx = _Ctx(run)
    assert Structure().evaluate(ctx) is True
    assert CitationSupport().evaluate(ctx) == 1.0
    assert LoadBearingCoverage().evaluate(ctx) == 1.0


def test_fixture_missing_raises() -> None:
    with pytest.raises(FileNotFoundError):
        load_run("no-such-fixture")
