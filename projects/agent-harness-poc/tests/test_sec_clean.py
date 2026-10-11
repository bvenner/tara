"""Agent output-source annotation cleanup (fix for judge section resolution)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from evals.grounding_eval import sec_clean  # noqa: E402


def test_strips_edge_annotation() -> None:
    src = (
        'A1. "Physics envy — this is a metaphor, not a model" '
        "(edge e35; nodes: T3, T4, gravitation, SK condition)"
    )
    assert sec_clean(src) == 'A1. "Physics envy — this is a metaphor, not a model"'


def test_keeps_plain_sections() -> None:
    assert sec_clean("4. Track A — Physics × Economics") == "4. Track A — Physics × Economics"


def test_paren_without_edge_marker_kept() -> None:
    assert sec_clean("5. Model skeleton (Track A, Phase 1)") == (
        "5. Model skeleton (Track A, Phase 1)"
    )
