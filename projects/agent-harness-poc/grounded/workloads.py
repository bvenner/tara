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
    trace_topic: str | None = None         # defaults to the manifest question
    trace_min_seeds: int = 3               # gate for the static arm's anchor rebuild


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
        anchors = trace_anchors(
            m.expected.trace_topic or m.question,
            m.expected.trace_seeds,
            min_seeds=m.expected.trace_min_seeds,
        )
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


# ── plumb-side adapters (M7 slice 1: prefetch architecture) ──────
# Upstream note: exec lowering via agent tool dispatch is not implemented
# (tool_not_supported), so the plumb researcher consumes a deterministically
# prefetched trace (pipelines/researcher.plumb); seeds come from the manifest.

PLUMB_ROOT = Path("/home/brad/tools/plumbing")
PLUMB_BIN = PLUMB_ROOT / "_build/default/bin/plumb/main.exe"
PIPES_DIR = THAR_DIR / "projects" / "knowledge-repository-poc" / "pipelines"
SIDECAR_ROOT = THREAD_ROOT / "evals" / "cache" / "plumb-sidecars"


def normalize_claim_source(src: str) -> str:
    """Shim harness-specific citation formats into the canonical
    `doc :: section` contract (same class as sec_clean): handles
    `doc — [section]`, `doc :: [section]`, and bracket residue."""
    import re

    s = src.strip()
    m = re.match(r"^(.+?)\s+—\s*\[(.+)\]$", s)
    if m:
        return f"{m.group(1).strip()} :: {m.group(2).strip()}"
    m = re.match(r"^(.+?)\s*::\s*\[(.+)\]$", s)
    if m:
        return f"{m.group(1).strip()} :: {m.group(2).strip()}"
    return s


def parse_plumb_payload(payload: dict, question: str, sidecar_dir: Path) -> GroundedRun:
    """Convert the researcher.plumb output + tee'd trace sidecars into a
    GroundedRun (harness-agnostic scorer contract)."""
    from evals.check_citations import anchors_from_sidecar

    claims = [
        Claim(
            statement=c["statement"],
            source=normalize_claim_source(c["source"]),
            trace_edge_ids=c.get("trace_edge_ids", []),
        )
        for c in payload.get("claims", [])
    ]
    recs = []
    for f in sorted(sidecar_dir.glob("*.jsonl")):
        tool = f.stem
        for line in f.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                recs.append({"tool": f"knowledge_{tool}", "content": json.loads(line)})
    sidecar = sidecar_dir / "composite.tools.json"
    sidecar.write_text(json.dumps(recs))
    anchors = sorted(anchors_from_sidecar(sidecar)) if recs else []
    return GroundedRun(
        question=question,
        answer=GroundedAnswer(
            question=question,
            synthesis=payload.get("synthesis", ""),
            claims=claims,
        ),
        anchors=anchors,
        tools_called=["knowledge_trace"] if recs else [],
    )


def _run_researcher_plumb(topic: str, concepts: list[str], min_seeds: int, lane: str) -> dict:
    """Run pipelines/researcher.plumb once (direct binary, nix fallback)."""
    import os
    import subprocess as sp

    sidecar_dir = SIDECAR_ROOT / lane
    sidecar_dir.mkdir(parents=True, exist_ok=True)
    for f in sidecar_dir.glob("*.jsonl"):
        f.unlink()
    env = os.environ.copy()
    env.setdefault("PLUMB_PATH", str(PLUMB_ROOT / "_build/default/stdlib"))
    env["TARA_PLUMB_SIDECAR"] = str(sidecar_dir / "trace.jsonl")
    payload = None
    stdin_text = json.dumps({"topic": topic, "concepts": concepts, "min_seeds": min_seeds}) + "\n"
    proc = None
    if PLUMB_BIN.exists():
        proc = sp.run(
            [str(PLUMB_BIN), "researcher.plumb"],
            input=stdin_text, capture_output=True, text=True, timeout=900, env=env,
            cwd=PIPES_DIR,
        )
    if proc is None or proc.returncode != 0:
        proc = sp.run(
            ["nix", "develop", str(PLUMB_ROOT), "-c", str(PLUMB_BIN), "researcher.plumb"],
            input=stdin_text, capture_output=True, text=True, timeout=900, cwd=PIPES_DIR,
        )
    if proc.returncode != 0:
        raise RuntimeError(f"researcher.plumb failed: {proc.stderr.strip()[-400:]}")
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            cand = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(cand, dict) and "claims" in cand:
            payload = cand
            break
    if payload is None:
        raise RuntimeError("researcher.plumb produced no answer payload")
    return payload


def plumb_agent(m: WorkloadManifest, refresh: bool = False) -> list[GroundedRun]:
    if m.kind == "cross-pillar-assembly" and m.lanes:
        raise NotImplementedError("use plumb-agent-fanout for lane workloads")
    seeds = m.expected.trace_seeds or [c for lane in m.lanes.values() for c in lane.seed_concepts]
    if not seeds:
        raise ValueError(f"manifest {m.id} provides no seeds for the plumb arm")
    payload = _run_researcher_plumb(m.question, seeds, 3, lane=m.id)
    return [parse_plumb_payload(payload, m.question, SIDECAR_ROOT / m.id)]


def plumb_agent_fanout(m: WorkloadManifest, refresh: bool = False) -> list[GroundedRun]:
    if not m.lanes:
        raise NotImplementedError("no lanes in this manifest")
    import concurrent.futures

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(m.lanes)) as ex:
        futs = {
            name: ex.submit(_run_researcher_plumb, m.question, lane.seed_concepts, 2, f"{m.id}-{name}")
            for name, lane in m.lanes.items()
        }
        payloads = {name: f.result() for name, f in futs.items()}
    return [parse_plumb_payload(payloads[name], m.question, SIDECAR_ROOT / f"{m.id}-{name}")
            for name in m.lanes]


ADAPTERS = {
    "static-baseline": static_baseline,
    "opencode-artifact": static_baseline,   # opencode arm: committed grounded artifact
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


async def run_workload_full(m: WorkloadManifest, adapter: str, refresh: bool = False, judge: bool = False) -> dict:
    report = await run_workload(m, adapter, refresh=refresh)
    if judge:
        fn = ADAPTERS[adapter]
        runs = await fn(m, refresh=refresh) if asyncio.iscoroutinefunction(fn) else fn(m, refresh=refresh)
        report["metrics"]["judged"] = await evaluate_judged(m, runs)
    return report


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
    aligned = len(runs) == len(lane_names)
    for i, run in enumerate(runs):
        lane_name = lane_names[i] if aligned else f"run{i}"
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


async def evaluate_judged(m: WorkloadManifest, runs: list[GroundedRun]) -> dict:
    """Claim-entailment judging on any arm's claims (LLM judge, cached; keyed
    by claim content so arms share verdicts)."""
    import sys

    from grounded.corpus_sections import section_text
    from grounded.judge import build_judge, judge_claim
    from evals.grounding_eval import sec_clean

    agent = build_judge()
    out: dict = {}
    for idx, run in enumerate(runs):
        verdicts = []
        for claim in run.answer.claims:
            doc, _, sec = claim.source.partition(" :: ")
            text = section_text(doc, sec_clean(sec)) or ""
            j = await judge_claim(agent, text, claim.statement)
            verdicts.append(j.verdict)
        entailed = verdicts.count("ENTAILED")
        insufficient = verdicts.count("INSUFFICIENT")
        denom = len(verdicts) - insufficient
        out[f"run{idx}" if not m.lanes else (list(m.lanes)[idx] if idx < len(m.lanes) and len(runs) == len(m.lanes) else f"run{idx}")] = {
            "claims": len(claims := run.answer.claims),
            "judge_score": round(entailed / denom, 3) if denom else 0.0,
            "verdicts": verdicts,
        }
    return out


def main() -> int:
    from evals.run_workload import main as cli_main  # CLI lives in evals/

    return cli_main()


if __name__ == "__main__":
    sys.exit(main())
