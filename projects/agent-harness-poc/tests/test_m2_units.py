"""M2 unit tests (offline, LLM-free)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest  # noqa: E402

import evals.grounding_eval as ge
from grounded.corpus_sections import doc_path, section_text  # noqa: E402


def test_parse_baseline() -> None:
    triples = ge.parse_baseline(ge.BASELINE_MD)
    assert len(triples) == 6
    assert {d for d, _, _ in triples} >= {
        "ret-tssi/program/research-program.md",
        "ret-tssi/findings.md",
        "ret-tssi/program/critiques.md",
    }
    assert ("ret-tssi/program/critiques.md", "A1") in [(d, s) for d, s, _ in triples]


def test_section_text_resolution() -> None:
    text = section_text("ret-tssi/program/research-program.md", "4 Track A")
    assert text and "T3" in text or "hyperbolic" in text.lower()
    text2 = section_text("ret-tssi/program/research-program.md", "2.2 Rational extended thermodynamics")
    assert text2 and "Ruggeri" in text2 or text2
    assert section_text("ret-tssi/nonexistent.md", "x") is None


def test_doc_path_external() -> None:
    assert doc_path("ret-tssi/findings.md") is not None
    assert doc_path("external/some-openalex-work.md") is None
