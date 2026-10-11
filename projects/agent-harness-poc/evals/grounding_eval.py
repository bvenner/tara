"""M2 grounding-task evaluation (pydantic-evals).

Registers the grounded-answer task with:

Deterministic evaluators (LLM-free):
  - `structure`: at least one claim, non-empty synthesis.
  - `citation_support`: every claim anchors to the run's own tool-output
    sidecar (mechanical half of the grounding discipline).
  - `load_bearing_coverage`: fraction of the opencode-baseline's
    load-bearing sections (graph/grounded-answer-tau-sk.md) covered by the
    agent's claims.

LLM-as-judge evaluator (pluggable via `AGENT_JUDGE` env):
  - `claim_entailment`: per claim, does the cited corpus section's TEXT
    (corpus.json root mapping + heading match) support the claim? Score =
    fraction ENTAILED; INSUFFICIENT verdicts are excluded from the
    denominator.

Cases: the acceptance question (agent run), the same question's
opencode-side baseline as a static case for comparison, and one
out-of-scope probe (physics-envy critique).

Usage:
    uv run python projects/agent-harness-poc/evals/grounding_eval.py [--no-judge] [--out report.json]
"""

from __future__ import annotations

import json
import os
import re
import sys
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pydantic import BaseModel
from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import Evaluator, EvaluatorContext

from evals.check_citations import anchors_from_sidecar, supported
from grounded import tools
from grounded.corpus_sections import section_text
from grounded.judge import build_judge, judge_claim
from run_grounded import (
    ACCEPTANCE_QUESTION,
    GroundedAnswer,
    Claim,
    build_agent,
    dump_tool_outputs,
    run_with_retry_async,
)

BASELINE_MD = (
    Path(__file__).resolve().parents[2]
    / "knowledge-repository-poc"
    / "graph"
    / "grounded-answer-tau-sk.md"
)

TAU_SEEDS = ["tau_J", "sk condition", "subcharacteristic", "gravitation", "T3"]
PHYSICS_ENVY_SEEDS = ["physics envy", "simultaneism"]

# Load-bearing citations of the stored opencode baseline (corpus-mapped subset).
LOAD_BEARING = [
    ("ret-tssi/program/research-program.md", "4. Track A"),
    ("ret-tssi/findings.md", "5. Model skeleton"),
    ("ret-tssi/program/research-program.md", "3. The core correspondence"),
    ("ret-tssi/program/research-program.md", "7. Track D"),
    ("ret-tssi/program/critiques.md", 'A1. "Physics envy'),
]


class GroundedRun(BaseModel):
    question: str
    answer: GroundedAnswer
    anchors: list[tuple[str, str]]
    tools_called: list[str]


def trace_anchors(topic: str, concepts: list[str], min_seeds: int) -> list[tuple[str, str]]:
    result = tools.knowledge_trace(topic=topic, concepts=concepts, min_seeds=min_seeds)
    return [(h.doc, h.section) for h in result.hits]


def parse_baseline(md: Path) -> list[tuple[str, str, str]]:
    """Parse the stored baseline's 'Evidence actually used' bullets into
    (doc, section, statement) triples."""
    triples: list[tuple[str, str, str]] = []
    bullet_re = re.compile(r"^- `(.+?)` (?:§ ?)?(.+?)(?: \([^—]*\))? — (.*)$")
    simple_re = re.compile(r"^- `(.+?)` (?:§ ?)?(.+?) — (.*)$")
    in_section = False
    for line in md.read_text(encoding="utf-8").splitlines():
        if line.startswith("## Evidence actually used"):
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if in_section:
            m = bullet_re.match(line) or simple_re.match(line)
            if m:
                triples.append((m.group(1), m.group(2).strip(), m.group(3).strip()))
    return triples


async def run_grounding(inputs: dict) -> GroundedRun:
    question = inputs["question"]
    if static_md := inputs.get("static_output"):
        triples = parse_baseline(Path(static_md))
        anchors = trace_anchors("tau->0 vs SK", TAU_SEEDS, min_seeds=3)
        return GroundedRun(
            question=question,
            answer=GroundedAnswer(
                question=question,
                synthesis="static opencode-side baseline (from graph/grounded-answer-tau-sk.md)",
                claims=[Claim(statement=stmt, source=f"{doc} :: {sec}") for doc, sec, stmt in triples],
            ),
            anchors=anchors,
            tools_called=["knowledge_trace"],
        )
    agent = build_agent(model=inputs.get("model"))
    result = await run_with_retry_async(agent, question)
    sidecar = Path(os.environ.get("TMPDIR", "/tmp")) / "m2_eval" / f"case-{uuid.uuid4().hex}.tools.json"
    sidecar.parent.mkdir(parents=True, exist_ok=True)
    dump_tool_outputs(result, sidecar)
    anchors = sorted(anchors_from_sidecar(sidecar))
    return GroundedRun(
        question=question,
        answer=result.output,
        anchors=anchors,
        tools_called=sorted({r["tool"] for r in json.loads(sidecar.read_text())}),
    )


class Structure(Evaluator):
    def evaluate(self, ctx: EvaluatorContext) -> bool:
        run: GroundedRun = ctx.output
        return bool(run.answer.claims) and len(run.answer.synthesis) > 50


class CitationSupport(Evaluator):
    def evaluate(self, ctx: EvaluatorContext) -> float:
        run: GroundedRun = ctx.output
        claims = run.answer.claims
        if not claims:
            return 0.0
        pairs = {(d, s) for d, s in run.anchors}
        ok = sum(1 for c in claims if supported(c.source, pairs))
        return ok / len(claims)


class LoadBearingCoverage(Evaluator):
    def evaluate(self, ctx: EvaluatorContext) -> float:
        run: GroundedRun = ctx.output
        if not run.anchors:
            return 0.0
        pairs = set(run.anchors)
        covered = sum(1 for doc, sec in LOAD_BEARING if supported(f"{doc} :: {sec}", pairs))
        return covered / len(LOAD_BEARING)


class ClaimEntailmentJudge(Evaluator):
    def __init__(self) -> None:
        self._agent = build_judge()

    async def evaluate(self, ctx: EvaluatorContext) -> float | None:
        run: GroundedRun = ctx.output
        claims = run.answer.claims
        if not claims:
            return None
        verdicts: list[str] = []
        for claim in claims:
            doc, _, sec = claim.source.partition(" :: ")
            text = section_text(doc, sec)
            judgement = await judge_claim(self._agent, text or "", claim.statement)
            verdicts.append(judgement.verdict)
            print(
                f"[judge] {ctx.name}: {doc.split('/')[-1]} :: {sec[:50]}\n"
                f"        claim: {claim.statement[:90]}\n"
                f"        verdict: {judgement.verdict} ({judgement.reason[:120]})",
                flush=True,
            )
        entailed = verdicts.count("ENTAILED")
        insufficient = verdicts.count("INSUFFICIENT")
        denom = len(verdicts) - insufficient
        return entailed / denom if denom else None


def build_dataset(judge: bool, task_model: str | None = None) -> Dataset:
    evaluators = [Structure(), CitationSupport(), LoadBearingCoverage()]
    if judge:
        evaluators.append(ClaimEntailmentJudge())
    cases = [
        Case(
            name="agent-tau-sk",
            inputs={
                "question": ACCEPTANCE_QUESTION,
                "concepts": TAU_SEEDS,
                **({"model": task_model} if task_model else {}),
            },
            metadata={"load_bearing": LOAD_BEARING},
        ),
        Case(
            name="baseline-tau-sk-static",
            inputs={"question": ACCEPTANCE_QUESTION, "static_output": str(BASELINE_MD)},
            metadata={"load_bearing": LOAD_BEARING},
        ),
        Case(
            name="agent-physics-envy",
            inputs={
                "question": "How does the program answer the charge that the "
                "thermodynamic analogy is only a metaphor?",
                "concepts": PHYSICS_ENVY_SEEDS,
                **({"model": task_model} if task_model else {}),
            },
            metadata={},
        ),
    ]
    return Dataset(name="grounding-eval-m2", cases=cases, evaluators=evaluators)


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-judge", action="store_true")
    parser.add_argument("--model", default=None, help="override the grounded agent model")
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    dataset = build_dataset(judge=not args.no_judge, task_model=args.model)
    report = dataset.evaluate_sync(task=run_grounding, name="grounding-eval-m2", max_concurrency=1)
    report.print()
    if args.out:
        summary = {
            "averages": report.averages,
            "cases": [
                {
                    "name": c.name,
                    "scores": {k: v for k, v in (c.scores or {}).items()},
                }
                for c in report.cases
            ],
        }
        args.out.write_text(json.dumps(summary, indent=2, default=str))
        print(f"written: {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
