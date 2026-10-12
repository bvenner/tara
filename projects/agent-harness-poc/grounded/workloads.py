"""M6 slice 1 — workloads as data + harness-agnostic runner.

The two flagship research workflows (hypergraph-grounding Q&A, island-DT
cross-pillar assembly) become committed JSON manifests under
`workloads/`, and this module executes any registered adapter against a
manifest and scores the result with the existing mechanical evaluators.

Why: the candidate M7 head-to-head (Pydantic-AI researcher vs
researcher-as-plumb, same mechanical scorer) needs an input contract that
is harness-agnostic. A manifest defines the workload; an adapter
implements `question (+lanes) -> GroundedRun(s)`; evaluation keys off the
GroundedRun shape only — so a plumb-side adapter plugs into the identical
scorer.

Adapters:
- static-baseline: parses the recorded opencode artifact (offline).
- mechanical-probe: evals.pillars pillar-union probe (no LLM; plumbing).
- pydantic-agent / pydantic-agent-fanout: the M1/M3 agent stack (cached).
- plumb-agent / plumb-agent-fanout: deliberate M7 stub (NotImplementedError).

Usage:
    uv run python projects/agent-harness-poc/evals/run_workload.py \
        --workload tau-sk-grounding --adapter static-baseline [--out report.json]
"""

from __future__ import annotations

import asyncio
import json
import re
import sys
import time
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from run_grounded import GroundedAnswer, Claim, GroundedRun  # noqa: E402
from run_grounded import INSTRUCTIONS, CLAIM  # noqa: E402

THAR_DIR = Path(__file__).resolve().parents[3]
THREAD_ROOT = Path(__file__).resolve().parents[1]


class CitationRef(BaseModel):
    doc: str
    section: str


class Lane(BaseModel):
    seed_concepts: list[str]
    instructions: str


class Expected(BaseModel):
    load_bearing: list[CitationRef] = Field(default_factory=list)
    pillar_markers: dict[str, str] = Field(default_factory=dict)
    bundle_doc: str | None = None          # workspace-relative path
    static_output: str | None = None       # workspace-relative path
    trace_seeds: list[str] = Field(default_factory=list)


class WorkloadManifest(BaseModel):
    id: str
    title: str
    kind: Literal["grounding-qa", "cross-pillar-assembly"]
    question: str
    instructions_file: str | None = None   # thread-root-relative path
    lanes: dict[str, Lane] = Field(default_factory=dict)
    adapters: list[str] = Field(default_factory=list)
    expected: Expected = Field(default_factory=Expected)

    def instructions_text(self) -> str | None:
        """Instruction content from the manifest's shared file (harness-agnostic)."""
        if self.instructions_file is None:
            return None
        path = THREAD_ROOT / self.instructions_file
        if not path.is_file():
            raise FileNotFoundError(f"manifest instructions_file missing: {path}")
        return path.read_text(encoding="utf-8")


def load_manifest(name: str) -> WorkloadManifest:
    """Load and validate `workloads/<name>.json` (id accepted bare)."""
    path = THREAD_ROOT / "workloads" / f"{name.removesuffix('.json')}.json"
    if not path.is_file():
        raise FileNotFoundError(f"workload manifest not found: {path}")
    return WorkloadManifest.model_validate(json.loads(path.read_text(encoding="utf-8")))


def bundle_from_doc(rel: str) -> set[tuple[str, str]]:
    """Parse a recorded evidence bundle (`### doc :: section` headings)."""
    text = (THAR_DIR / "projects" / rel).read_text(encoding="utf-8")
    headings = re.findall(r"^### (.+?) :: (.+?)$", text, re.MULTILINE)
    return {(doc, sec) for doc, sec in headings}


def _bundle_hit(pair: tuple[str, str], pool: set[tuple[str, str]]) -> bool:
    d, s = pair
    for ad, asec in pool:
        if ad == d and (asec == s or asec.startswith(s[:60]) or s.startswith(asec[:60])):
            return True
    return False


# ── adapters ─────────────────────────────────────────────────────

async def static_baseline(m: WorkloadManifest, refresh: bool = False) -> list[GroundedRun]:
    """Offline: parse the recorded opencode artifact into a GroundedRun."""
    from evals.grounding_eval import parse_baseline, trace_anchors

    md = THAR_DIR / "projects" / m.expected.static_output
    triples = parse_baseline(md)
    claims = [
        Claim(statement=stmt, source=f"{doc} :: {sec}")
        for doc, sec, stmt in triples
    ]
    anchors: list = []
    if m.expected.trace_seeds:
        anchors = trace_anchors("tau->0 vs SK", m.expected.trace_seeds, min_seeds=3)
    return [
        GroundedRun(
            question=m.question,
            answer=GroundedAnswer(
                question=m.question,
                synthesis="(static opencode baseline)",
                claims=claims,
            ),
            anchors=anchors,
            tools_called=["knowledge_trace"],
        )
    ]


async def pydantic_agent(m: WorkloadManifest, refresh: bool = False) -> list[GroundedRun]:
    from run_grounded import ground_run_async

    instructions = m.instructions_text()
    run = await ground_run_async(m.question, refresh=refresh, instructions=instructions)
    return [run]


async def pydantic_agent_fanout(m: WorkloadManifest, refresh: bool = False) -> list[GroundedRun]:
    from run_grounded import ground_run_async

    base = m.instructions_text()

    async def lane(name: str, l: Lane) -> GroundedRun:
        instructions = base + (
            f"\n\n## Lane\n{l.instructions}\n"
            "Stay in your lane: every claim must cite an island-dt or "
            "metabolism/3D/twin/geodesign section; ignore whatever lies "
            "outside the lane even if the trace surfaces it."
        )
        return await ground_run_async(m.question, refresh=refresh, instructions=instructions)

    return list(await asyncio.gather(*[lane(n, l) for n, l in m.lanes.items()]))


async def mechanical_probe(m: WorkloadManifest, refresh: bool = False) -> list[GroundedRun]:
    """M3a as an adapter: per-pillar mechanical grounding at natural gates."""
    from evals.pillars import pillar_probes, PILLARS

    probes = pillar_probes()
    runs: list[GroundedRun] = []
    for name in PILLARS:
        anchors = probes[name]["anchors"]
        claims = [
            Claim(statement=f"(mechanical probe) anchor hit for lane {name}", source=f"{d} :: {s}")
            for d, s in anchors
        ]
        runs.append(
            GroundedRun(
                question=m.question,
                answer=GroundedAnswer(
                    question=m.question,
                    synthesis=f"mechanical pillar probe lane {name}",
                    claims=claims,
                ),
                anchors=anchors,
                tools_called=["knowledge_trace"],
            )
        )
    return runs


def plumb_agent(m: WorkloadManifest, refresh: bool = False) -> list[GroundedRun]:
    raise NotImplementedError(
        "plumb adapters arrive with M7 (researcher-as-plumb head-to-head); "
        "the manifest defines the contract, execution deferred"
    )


def plumb_agent_fanout(m: WorkloadManifest, refresh: bool = False) -> list[GroundedRun]:
    raise NotImplementedError(
        "plumb adapters arrive with M7 (researcher-as-plumb head-to-head); "
        "the manifest defines the contract, execution deferred"
    )


ADAPTERS = {
    "static-baseline": static_baseline,
    "pydantic-agent": pydantic_agent,
    "pydantic-agent-fanout": pydantic_agent_fanout,
    "mechanical-probe": mechanical_probe,
    "plumb-agent": plumb_agent,
    "plumb-agent-fanout": plumb_agent_fanout,
}


async def run_workload(m: WorkloadManifest, adapter: str, refresh: bool = False) -> dict:
    fn = ADAPTERS.get(adapter)
    if fn is None:
        raise ValueError(f"unknown adapter: {adapter}")
    t0 = time.monotonic()
    fn_async = asyncio.iscoroutinefunction(fn)
    runs = await fn(m, refresh=refresh) if fn_async else fn(m, refresh=refresh)
    metrics = evaluate(m, runs)
    return {"workload": m.id, "adapter": adapter, "wall_s": round(time.monotonic() - t0, 1), "metrics": metrics}


# ── evaluation (GroundedRun shape only — harness-agnostic) ───────

def evaluate(m: WorkloadManifest, runs: list[GroundedRun]) -> dict:
    from evals.check_citations import supported

    if m.kind == "grounding-qa":
        out: dict = {"runs": []}
        lb = {(r.doc, r.section) for r in m.expected.load_bearing}
        for run in runs:
            claims = run.answer.claims
            pairs = {(d, s) for d, s in run.anchors}
            cs = sum(1 for c in claims if supported(c.source, pairs)) / len(claims) if claims else 0.0
            lb_cov = (
                sum(1 for d, s in lb if supported(f"{d} :: {s}", pairs)) / len(lb)
                if lb
                else None
            )
            out["runs"].append(
                {
                    "claims": len(claims),
                    "anchors": len(run.anchors),
                    "citation_support": round(cs, 3),
                    "load_bearing_coverage": round(lb_cov, 3) if lb_cov is not None else None,
                }
            )
        return out

    # cross-pillar-assembly: union metrics against the recorded bundle
    bundle = bundle_from_doc(m.expected.bundle_doc) if m.expected.bundle_doc else set()
    union: set[tuple[str, str]] = set()
    per_lane: dict[str, dict] = {}
    lane_names = list(m.lanes)
    for i, run in enumerate(runs):
        lane_name = lane_names[i] if i < len(lane_names) else f"run{i}"
        anchors = {(d, s) for d, s in run.anchors}
        union |= anchors
        claims = run.answer.claims
        supported_n = sum(1 for c in claims if supported(c.source, anchors))
        per_lane[lane_name] = {
            "claims": len(claims),
            "anchors": len(run.anchors),
            "citation_support": round(supported_n / len(claims), 3) if claims else None,
        }
    island_sections = {s for d, s in union if d.startswith("island-dt")}
    pillar_reached = {
        p: any(sec.startswith(marker) for sec in island_sections)
        for p, marker in m.expected.pillar_markers.items()
    }
    return {
        "per_lane": per_lane,
        "prior_bundle_sections": len(bundle),
        "bundle_covered_by_union": sum(1 for a in bundle if _bundle_hit(a, union)),
        "union_sections": len(union),
        "pillars_reached": pillar_reached,
        "pillars_reached_count": sum(pillar_reached.values()),
    }


def main() -> int:
    from evals.run_workload import main as cli_main  # CLI lives in evals/

    return cli_main()


if __name__ == "__main__":
    sys.exit(main())
