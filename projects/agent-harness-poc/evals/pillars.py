"""M3 pillar configuration + mechanical pillar-union probe (island-DT).

The island digital-twin literature review has four pillars:
  A  island & urban metabolism (the flow layer)
  B  3D city models & standards (CityGML / Energy ADE, the substrate)
  C  digital twins (urban theory, island practice, EU policy, the container)
  D  participatory planning support & geodesign (the decision process)

Prior recorded result (projects/knowledge-repository-poc/graph/
evidence-trace-island-dt.md): a single composed trace with 6 seeds at
min_seeds=1 produced a 13-section union bundle spanning all four pillars —
while min_seeds=2 grounded ONLY within pillar B. M3 tests the alternative:
*fan-out* — per-pillar queries/traces (or per-pillar agents) whose union is
expected to span the pillars without lowering the gate.

This module is LLM-free: pillar definitions, the mechanical union probe, and
the bundle-comparison metrics.
"""

from __future__ import annotations

import sys
from pathlib import Path

THAR_DIR = Path(__file__).resolve().parents[3]
BUNDLE_MD = THAR_DIR / "projects" / "knowledge-repository-poc" / "graph" / "evidence-trace-island-dt.md"

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from grounded import tools as gr_tools  # noqa: E402

COMPOSED_QUESTION = (
    "Develop an island digital twin: metabolic flow models on a realistic 3D "
    "model of an island, for participatory sustainability planning"
)

PILLARS: dict[str, dict] = {
    "A-metabolism": {"concepts": ["island metabolism", "urban metabolism"]},
    "B-3d-standards": {"concepts": ["city model", "energy ade"]},
    "C-digital-twins": {"concepts": ["digital twin"]},
    "D-geodesign": {"concepts": ["participatory"]},
}

# doc-id prefixes that count as "this pillar was reached" in the bundle metrics
PILLAR_DOC_MARKERS: dict[str, str] = {
    "A-metabolism": "A. Island & urban metabolism",
    "B-3d-standards": "B. 3D city models",
    "C-digital-twins": "C. Digital twins",
    "D-geodesign": "D. Participatory planning support",
}

_BUNDLE_HEADING_RE = None


def prior_bundle() -> set[tuple[str, str]]:
    """Parse the recorded min_seeds=1 union bundle (13 sections) from the
    committed evidence trace (### doc :: section headings)."""
    import re

    text = BUNDLE_MD.read_text(encoding="utf-8")
    headings = re.findall(r"^### (.+?) :: (.+?)$", text, re.MULTILINE)
    return {(doc, sec) for doc, sec in headings}


def pillar_probes() -> dict[str, dict[str, list[tuple[str, str]]]]:
    """Per-pillar grounding at the pillar's natural gate:
    multi-concept pillars try trace at min_seeds=2 first; an empty trace
    falls back to per-concept queries (the researcher move: trace failed to
    co-locate the seeds, so take the union of single-concept evidence)."""
    out: dict[str, dict[str, list[tuple[str, str]]]] = {}
    for name, cfg in PILLARS.items():
        concepts = cfg["concepts"]
        anchors: list[tuple[str, str]] = []
        if len(concepts) >= 2:
            try:
                res = gr_tools.knowledge_trace(
                    topic=COMPOSED_QUESTION, concepts=concepts, min_seeds=2
                )
                anchors = [(h.doc, h.section) for h in res.hits]
            except RuntimeError:
                anchors = []
        if not anchors:
            per_concept: list[tuple[str, str]] = []
            for concept in concepts:
                try:
                    q = gr_tools.knowledge_query(concept)
                    per_concept.extend((e.doc, e.section) for e in q.edges)
                except RuntimeError:
                    continue
            anchors = per_concept
        out[name] = {"anchors": [(a, b) for a, b in dict.fromkeys(anchors)]}
    return out


def union_metrics(probes: dict[str, dict[str, list[tuple[str, str]]]] | None = None) -> dict:
    """Compare the per-pillar union against the recorded min_seeds=1 bundle."""
    probes = probes if probes is not None else pillar_probes()
    bundle = prior_bundle()
    union: set[tuple[str, str]] = set()
    per_pillar: dict[str, int] = {}
    for name, data in probes.items():
        anchors = {(d, s) for d, s in data["anchors"]}
        per_pillar[name] = len(anchors)
        union |= anchors

    def _bundle_hit(a: tuple[str, str], pairs: set[tuple[str, str]]) -> bool:
        d, s = a
        for bd, bs in pairs:
            if bd == d and (bs == s or bs.startswith(s[:60]) or s.startswith(bs[:60])):
                return True
        return False

    bundle_covered = sum(1 for a in bundle if _bundle_hit(a, union))
    pillar_reached = {
        p: any(
            s.startswith(marker)
            for d, s in union
            if d.startswith("island-dt")
        )
        for p, marker in PILLAR_DOC_MARKERS.items()
    }
    return {
        "prior_bundle_sections": len(bundle),
        "bundle_covered_by_union": bundle_covered,
        "union_sections": len(union),
        "pillar_anchor_counts": per_pillar,
        "pillar_reached": pillar_reached,
        "pillars_reached_count": sum(pillar_reached.values()),
    }


if __name__ == "__main__":
    import json

    metrics = union_metrics()
    print(json.dumps(metrics, indent=2))
