"""Fixture stack: replay banked evaluation artifacts without any LLM/pipeline.

`load_run(name)` reconstructs a `GroundedRun` (same shape the live eval task
produces) from two committed artifacts under `evals/fixtures/`:

  <name>.md           the rendered grounded answer (run_grounded._render)
  <name>.tools.json   the tool-output sidecar (run_grounded.dump_tool_outputs)

Result: the deterministic evaluators (structure / citation_support /
load_bearing_coverage) and the judge *schema* can be tested/developed
offline in seconds — the loop-speedup layer of
`writing/machine/2026-10-11-m2-loop-resource-plan.md`.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from evals.check_citations import CLAIM_RE, anchors_from_sidecar  # noqa: E402
from run_grounded import GroundedAnswer, Claim, GroundedRun  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def available() -> list[str]:
    return sorted(p.name[: -len(".tools.json")] for p in FIXTURES.glob("*.tools.json"))


def load_run(name: str) -> GroundedRun:
    run_md = FIXTURES / f"{name}.md"
    sidecar = FIXTURES / f"{name}.tools.json"
    for f in (run_md, sidecar):
        if not f.exists():
            raise FileNotFoundError(f"fixture missing: {f}")

    # sidecar → anchors + tools called
    anchors = sorted(anchors_from_sidecar(sidecar))
    tool_names = sorted({rec["tool"] for rec in json.loads(sidecar.read_text())})

    # markdown → question, synthesis, claims
    question = synthesis = ""
    section = None
    claims: list[Claim] = []
    for line in run_md.read_text(encoding="utf-8").splitlines():
        h = line.lstrip("#").strip()
        if line.startswith("## "):
            section = h
            continue
        if section == "Question" and line.strip() and not question:
            question = line.strip()
        elif section == "Synthesis" and line.strip():
            synthesis += (" " if synthesis else "") + line.strip()
        elif section == "Claims" and line.startswith("- "):
            m = CLAIM_RE.match(line)
            if m:
                source = f"{m.group(1)} :: {m.group(2)}"
                statement = m.group(3).strip()
                statement = statement.rsplit(" (edges:", 1)[0].strip()
                claims.append(Claim(statement=statement, source=source))

    if not claims or not synthesis:
        raise ValueError(f"fixture {name}: unparsed claims or synthesis")

    return GroundedRun(
        question=question,
        answer=GroundedAnswer(question=question, synthesis=synthesis, claims=claims),
        anchors=anchors,
        tools_called=tool_names,
    )
