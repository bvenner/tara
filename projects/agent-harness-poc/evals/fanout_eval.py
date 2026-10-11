"""M3b — pillar fan-out for the island digital-twin composition question.

Runs the four pillar-scoped grounded researchers in parallel (one agent per
pillar of the island-DT corpus, each still bound to the full grounding
discipline but instructed to research its lane) and evaluates the UNION of
their claims/anchors against the recorded min_seeds=1 evidence bundle
(`evidence-trace-island-dt.md`, 13 sections).

Mechanical context (evals/pillars.py): the pillar-union of per-pillar
traces/queries reaches 4/4 pillars and 11/13 of the bundle WITHOUT dropping
the global gate. This eval asks the same question of the AGENT stack: do
parallel grounded researchers — each at its own higher precision — compose
into cross-pillar coverage?

Usage:
    uv run python projects/agent-harness-poc/evals/fanout_eval.py [--refresh] [--out report.json]
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from evals.check_citations import supported  # noqa: E402
from evals.pillars import COMPOSED_QUESTION, PILLARS, prior_bundle  # noqa: E402
from run_grounded import ground_run_async, INSTRUCTIONS  # noqa: E402

GLM_MODEL = os.environ.get("AGENT_MODEL", "openrouter:z-ai/glm-5.3-flash")

LANES: dict[str, str] = {
    "A-metabolism": (
        "Your research lane is pillar A: island & urban metabolism — the "
        "flow layer (metabolic flow analysis, material/energy/water/waste "
        "stocks and flows of islands). Concepts to seed with: 'island "
        "metabolism', 'urban metabolism'. If the trace co-locates nothing "
        "at min_seeds=3, drop to 2, then use knowledge_query per concept."
    ),
    "B-3d-standards": (
        "Your research lane is pillar B: 3D city models & standards — the "
        "geometric + data substrate (CityGML, the Energy ADE, 3D city model "
        "state of the art). Concepts to seed with: 'city model', 'energy ade'."
    ),
    "C-digital-twins": (
        "Your research lane is pillar C: digital twins — the container "
        "(urban theory twin debates, island twin practice such as the "
        "Inishmore peer-to-peer energy twin, EU policy). Concept to seed "
        "with: 'digital twin'."
    ),
    "D-geodesign": (
        "Your research lane is pillar D: participatory planning support & "
        "geodesign — the decision process. Concept to seed with: "
        "'participatory'."
    ),
}

PILLAR_MARKERS = {
    "A-metabolism": "A. Island & urban metabolism",
    "B-3d-standards": "B. 3D city models",
    "C-digital-twins": "C. Digital twins",
    "D-geodesign": "D. Participatory planning support",
}


def _bundle_hit(pair: tuple[str, str], anchors: set[tuple[str, str]]) -> bool:
    d, s = pair
    for ad, asec in anchors:
        if ad == d and (asec == s or asec.startswith(s[:60]) or s.startswith(asec[:60])):
            return True
    return False


async def run_fanout(model: str | None = None, refresh: bool = False) -> list:
    async def lane_run(name: str) -> tuple[str, object]:
        instructions = INSTRUCTIONS + (
            f"\n\n## Lane\n{LANES[name]}\n"
            "Stay in your lane: every claim must cite an island-dt or "
            "metabolism/3D/twin/geodesign section; ignore whatever lies "
            "outside the lane even if the trace surfaces it."
        )
        run = await ground_run_async(
            COMPOSED_QUESTION, model=model, refresh=refresh, instructions=instructions
        )
        return name, run

    results = await asyncio.gather(*[lane_run(n) for n in PILLARS])
    return sorted(results)


def evaluate(results: list) -> dict:
    bundle = prior_bundle()
    union_anchors: set[tuple[str, str]] = set()
    per_pillar: dict[str, dict] = {}
    claims_hit_bundle = 0
    total_claims = 0
    for name, run in results:
        claims = run.answer.claims
        total_claims += len(claims)
        claims_hit_bundle += sum(
            1 for c in claims if _bundle_hit(_split(c.source), bundle)
        )
        supported_n = sum(
            1 for c in claims if supported(c.source, {(d, s) for d, s in run.anchors})
        )
        union_anchors |= {(d, s) for d, s in run.anchors}
        per_pillar[name] = {
            "claims": len(claims),
            "citation_support": round(supported_n / len(claims), 3) if claims else None,
            "anchors": len(run.anchors),
        }
    island_sections = {s for d, s in union_anchors if d.startswith("island-dt")}
    pillar_reached = {
        p: any(sec.startswith(marker) for sec in island_sections)
        for p, marker in PILLAR_MARKERS.items()
    }
    bundle_covered = sum(1 for a in bundle if _bundle_hit(a, union_anchors))
    mechanical = json.loads(
        (Path(__file__).parent / "2026-10-11-m3-fanout-report.json").read_text()
    )["mechanical"] if (Path(__file__).parent / "2026-10-11-m3-fanout-report.json").exists() else None
    return {
        "model": GLM_MODEL,
        "prior_bundle_sections": len(bundle),
        "bundle_covered_by_union": bundle_covered,
        "claims_hit_bundle": claims_hit_bundle,
        "total_claims": total_claims,
        "pillar_reached": pillar_reached,
        "per_pillar": per_pillar,
        "mechanical_probe": mechanical,
    }


def _split(source: str) -> tuple[str, str]:
    doc, _, sec = source.partition(" :: ")
    import re

    sec = re.split(r"\s\((?:edge|nodes)[^)]*\)$", sec)[0].strip()
    return doc, sec


def main() -> int:
    import argparse
    import time

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--model", default=None)
    parser.add_argument(
        "--out", type=Path,
        default=Path(__file__).parent / "2026-10-11-m3-fanout-report.json",
    )
    args = parser.parse_args()
    model = args.model or GLM_MODEL

    from evals.pillars import pillar_probes, union_metrics

    t0 = time.monotonic()
    mechanical = union_metrics(pillar_probes())
    mechanical["wall_s"] = round(time.monotonic() - t0, 1)
    t0 = time.monotonic()
    results = asyncio.run(run_fanout(model=model, refresh=args.refresh))
    agent_wall = round(time.monotonic() - t0, 1)
    evaluation = evaluate(results)
    report = {"model": model,
              "mechanical": mechanical,
              "agent_wall_s": agent_wall,
              "per_pillar": evaluation["per_pillar"],
              "bundle_covered_by_union": evaluation["bundle_covered_by_union"],
              "claims_hit_bundle": evaluation["claims_hit_bundle"],
              "total_claims": evaluation["total_claims"],
              "pillar_reached": evaluation["pillar_reached"]}
    args.out.write_text(json.dumps(report, indent=2, default=str))
    print(json.dumps(report, indent=2, default=str))
    print(f"\nwritten: {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
