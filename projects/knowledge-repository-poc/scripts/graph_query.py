#!/usr/bin/env python3
"""JSON Lines worker for hypergraph plumbing pipelines (the `exec` primitive).

Reads one JSON value per stdin line; emits one JSON value per line on stdout.
Resolves the graph artifact relative to this file, so it works regardless of cwd.

Modes:
  --mode json  : `{concept}`            -> QueryResult (typed record)
  --mode text  : `{concept, max_edges}` -> string (markdown evidence bundle)
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