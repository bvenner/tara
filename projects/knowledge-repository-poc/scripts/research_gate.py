#!/usr/bin/env python3
"""M7 research gate: the researcher's deterministic evidence move as a worker.

trace(topic, concepts, min_seeds) at the requested gate; if the trace
grounds nothing, fall back to per-concept queries and return the union —
exactly the move evals/pillars.py's mechanical probe uses (and the researcher
instructions describe). Union output keeps the plumb fabric's exact-typed
Trace shape: every per-concept edge becomes a Hit with seeds=[the concept].

stdin:  {"topic": string, "concepts": [string], "min_seeds": number}
stdout: TraceResult JSON ({topic, min_seeds, seeds, hits, distinct_sections,
evidence: [{doc, section, text}] — section source text for grounded answers;
external works (openalex docs) have no local file, so no evidence entry).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from graph_query import Hit, collect, load, match_nodes, trace

# Section-text resolver: re-uses the agent-harness thread's heading-match
# reader when present (graceful degradation: evidence list omitted).
try:
    _THAR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    sys.path.insert(0, os.path.join(_THAR, "agent-harness-poc"))
    from grounded.corpus_sections import section_text  # noqa: E402

    _SECTION_TEXT = True
except Exception:  # pragma: no cover - thin environment
    _SECTION_TEXT = False


TEXT_BUDGET = 1200  # chars per section, bounded so the agent context stays small
EVIDENCE_MAX = 16



def main():
    g, edge_by_id, index = load()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        req = json.loads(line)
        t = trace(g, edge_by_id, index, req["topic"], req["concepts"],
                  int(req["min_seeds"]), max_edges=req.get("max_edges", 40))
        if not t.hits:
            concept_hits = []
            for concept in req["concepts"]:
                nids = match_nodes(g, concept)
                edges = collect(index, nids, req.get("max_edges", 40))
                for e in edges:
                    concept_hits.append({
                        "edge_id": e["id"], "doc": e["doc"], "section": e["section"],
                        "arity": e["arity"],
                        "seeds": [concept],
                        "nodes": [g["nodes"][n].get("label", n) for n in e["nodes"]],
                    })
            if concept_hits:
                # rebuild as proper models (avoid seed/hits type warnings)
                t = trace(g, edge_by_id, index, req["topic"], req["concepts"],
                          int(req["min_seeds"]), max_edges=req.get("max_edges", 40))
                t.hits = [Hit(**h) for h in concept_hits]
                t.min_seeds = 1
                t.distinct_sections = len({(h["doc"], h["section"]) for h in concept_hits})
        evidence = []
        if _SECTION_TEXT:
            seen = set()
            for h in t.hits:
                key = (h.doc, h.section)
                if key in seen:
                    continue
                seen.add(key)
                text = section_text(h.doc, h.section) or ""
                if text:
                    evidence.append({
                        "doc": h.doc,
                        "section": h.section,
                        "text": text[:TEXT_BUDGET],
                    })
                if len(evidence) >= EVIDENCE_MAX:
                    break
        print(json.dumps({**t.model_dump(), "evidence": evidence}))
        sys.stdout.flush()


if __name__ == "__main__":
    main()
