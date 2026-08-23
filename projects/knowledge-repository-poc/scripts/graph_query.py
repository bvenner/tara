#!/usr/bin/env python3
"""JSON Lines worker for hypergraph plumbing pipelines (the `exec` primitive).

Reads one JSON value per stdin line; emits one JSON value per line on stdout.
Resolves the graph artifact relative to this file, so it works regardless of cwd.

Modes:
  --mode json  : `{concept}`            -> QueryResult (typed record)
  --mode text  : `{concept, max_edges}` -> string (markdown evidence bundle)
  --mode trace : `{topic, concepts, min_seeds}` -> Trace (hyperedge intersections)
  --mode trace-text : same             -> string (markdown evidence trace)
"""
import argparse
import json
import re
import sys
from pathlib import Path

GRAPH = Path(__file__).resolve().parents[1] / "graph" / "hypergraph.json"

_cache = None


def load():
    global _cache
    if _cache is None:
        g = json.loads(GRAPH.read_text())
        index = {}
        for e in g["hyperedges"]:
            for n in e["nodes"]:
                index.setdefault(n, []).append(e)
        _cache = (g, index)
    return _cache


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.lower()).strip()


def match_nodes(g, concept: str) -> list:
    c = norm(concept)
    if not c:
        return []
    return [nid for nid, node in g["nodes"].items()
            if c in norm(nid) or c in norm(node["label"])]


def collect(index, nids: list, max_edges: int):
    seen, out = set(), []
    for nid in nids:
        for e in index.get(nid, []):
            if e["id"] in seen:
                continue
            seen.add(e["id"])
            out.append(e)
    out.sort(key=lambda e: e["arity"], reverse=True)
    return out[:max_edges]


def to_json(g, concept, nids, edges):
    return {
        "concept": concept,
        "matched_nodes": [
            {"node_id": nid, "label": g["nodes"][nid]["label"], "kind": g["nodes"][nid]["kind"]}
            for nid in nids
        ],
        "total_edges": len(edges),
        "edges": [
            {
                "edge_id": e["id"], "arity": e["arity"], "doc": e["doc"],
                "section": e["section"],
                "nodes": [g["nodes"][n].get("label", n) for n in e["nodes"]],
            }
            for e in edges
        ],
    }


def to_text(g, concept, nids, edges):
    lines = [f"## Query: {concept}", ""]
    if not nids:
        lines.append("No concepts matched.")
        return "\n".join(lines)
    lines.append(f"Matched concepts ({len(nids)}):")
    for nid in nids:
        n = g["nodes"][nid]
        lines.append(f"- {n['label']} [{n['kind']}]")
    if not edges:
        lines.append("\nNo hyperedges contain these concepts.")
        return "\n".join(lines)
    lines.append(f"\nHyperedges ({len(edges)}):")
    for e in edges:
        lines.append(f"- [{e['arity']} members] {e['doc']} :: {e['section']}")
        lines.append(f"    {', '.join(g['nodes'][n].get('label', n) for n in e['nodes'])}")
    return "\n".join(lines)


def trace(g, index, topic, concepts, min_seeds, max_edges=40):
    seeds = []
    for c in concepts:
        nids = match_nodes(g, c)
        seeds.append({"concept": c, "matched_nodes": [g["nodes"][n]["label"] for n in nids]})
    edge_hits = {}
    for si in range(len(concepts)):
        for nid in match_nodes(g, concepts[si]):
            for e in index.get(nid, []):
                if e["id"] not in edge_hits:
                    edge_hits[e["id"]] = set()
                edge_hits[e["id"]].add(si)
    hits = []
    for eid, sids in edge_hits.items():
        if len(sids) < min_seeds:
            continue
        e = next(e for e in g["hyperedges"] if e["id"] == eid)
        hits.append({
            "edge_id": e["id"], "doc": e["doc"], "section": e["section"],
            "arity": e["arity"],
            "seeds": [concepts[i] for i in sorted(sids)],
            "nodes": [g["nodes"][n].get("label", n) for n in e["nodes"]],
        })
    hits.sort(key=lambda h: (len(h["seeds"]), h["arity"]), reverse=True)
    hits = hits[:max_edges]
    return {
        "topic": topic, "min_seeds": min_seeds, "seeds": seeds, "hits": hits,
        "distinct_sections": len({(h["doc"], h["section"]) for h in hits}),
    }


def trace_text(t, concept_labels=None):
    lines = [f"# Evidence trace — {t['topic']}", ""]
    lines.append(f"Seed concepts ({len(t['seeds'])}; min seeds per edge = {t['min_seeds']}):")
    for s in t["seeds"]:
        if s["matched_nodes"]:
            lines.append(f"- `{s['concept']}` -> {', '.join(s['matched_nodes'])}")
        else:
            lines.append(f"- `{s['concept']}` -> (no match)")
    if not t["hits"]:
        lines.append("\nNo hyperedge contains enough of these seeds together.")
        return "\n".join(lines)
    lines.append(f"\nIntersecting hyperedges ({len(t['hits'])}; across {t['distinct_sections']} sections):\n")
    by_section = {}
    for h in t["hits"]:
        by_section.setdefault((h["doc"], h["section"]), []).append(h)
    for (doc, section), hs in by_section.items():
        lines.append(f"### {doc} :: {section}")
        for h in hs:
            lines.append(f"- [{h['arity']} members; seeds: {', '.join(h['seeds'])}]")
            lines.append(f"    {', '.join(h['nodes'])}")
        lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", default="json")
    ap.add_argument("--max-edges", type=int, default=50)
    args = ap.parse_args()
    g, index = load()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        req = json.loads(line)
        if args.mode in ("trace", "trace-text"):
            t = trace(g, index, req.get("topic", ""), req.get("concepts", []),
                      int(req.get("min_seeds", 2)), max_edges=int(req.get("max_edges", 40)))
            print(json.dumps(trace_text(t) if args.mode == "trace-text" else t))
        else:
            concept = req.get("concept", "")
            max_edges = int(req.get("max_edges", args.max_edges))
            nids = match_nodes(g, concept)
            edges = collect(index, nids, max_edges)
            if args.mode == "text":
                print(json.dumps(to_text(g, concept, nids, edges)))
            else:
                print(json.dumps(to_json(g, concept, nids, edges)))
        sys.stdout.flush()


if __name__ == "__main__":
    main()