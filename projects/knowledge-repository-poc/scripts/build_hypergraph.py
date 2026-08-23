#!/usr/bin/env python3
"""Phase A, Step 1 — co-occurrence hypergraph over the RET x TSSI corpus.

Builds a statistical (no-LLM) hypergraph: nodes are (c) the corpus's own
named entities (markdown headers, bibliography keys, theorem/track tags,
curated notation tokens) plus (a) RAKE keyword phrases; hyperedges are the
sets of concepts co-occurring within each section of each document.

Outputs (under <poc>/graph/):
  hypergraph.json   — nodes, hyperedges, provenance, HNX-compatible shape
  provenance.tsv    — per-hyperedge doc/section provenance
  stats.json        — counts and degree/arity distributions

Usage:
    python scripts/build_hypergraph.py
"""
import argparse
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

CORPUS_DIR = Path(__file__).resolve().parents[2] / "ret-tssi-value-dynamics"
OUT_DIR = Path(__file__).resolve().parents[1] / "graph"

# ── Text normalization ────────────────────────────────────────────

_CHARMAP = {
    "τ": "tau", "λ": "lambda", "∂": "d", "∇": "grad", "→": "->",
    "–": "-", "—": "-", "'": "", "’": "", "“": '"', "”": '"', "…": "...",
}


def norm(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    for k, v in _CHARMAP.items():
        text = text.replace(k, v)
    return text.lower().strip()


_WORD_RE = re.compile(r"[a-z][a-z0-9-]{0,40}")

# ── RAKE (mini, deterministic) ─────────────────────────────────────

STOP = set("""
a about after again all also an and any are as at be because been before being
between both but by can could did do does during each for from further had has
have having he her here hers herself him himself his how i if in into is it its
itself just me more most my myself no nor not now of off on once only or other
our ours ourselves out over own same she should so some such than that the their
theirs them themselves then there these they this those through to too under
until up very was we were what when where which while who whom why will with you
your yours yourself yourselves
also over under within without between each per via new must may might can
across among for from into onto upon along around before behind below beneath
beside beyond down inside near outside throughout towards upward
""".split())


def rake_top(section_text: str, limit: int) -> list:
    """Return ranked keyword phrases in a text (top `limit`)."""
    text = norm(section_text)
    words = _WORD_RE.findall(text)
    phrases, cur = [], []
    for w in words:
        if w in STOP or len(w) < 3:
            if cur:
                phrases.append(" ".join(cur))
                cur = []
        else:
            cur.append(w)
    if cur:
        phrases.append(" ".join(cur))
    freq, deg = Counter(), Counter()
    for ph in phrases:
        for w in ph.split():
            freq[w] += 1
            deg[w] += len(set(ph.split())) - 1
    sc = {w: freq[w] * deg[w] for w in freq}
    seen = set()
    ranked = []
    for ph in phrases:
        if ph in seen:
            continue
        seen.add(ph)
        score = sum(sc.get(w, 0) for w in ph.split())
        ranked.append((ph, score))
    ranked.sort(key=lambda x: x[1], reverse=True)
    return [ph for ph, _ in ranked[:limit]]


# ── Named entities ─────────────────────────────────────────────────

ARTIFACT_RE = re.compile(r"\b(t[1-4])\b")
TRACK_RE = re.compile(r"\btracks? ([a-f])\b")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$")

NOTATIONS = {
    "tau_j": (r"\btau[ _]?j\b", "tau_J"),
    "melt": (r"\bmelt\b", "MELT"),
    "cattaneo": (r"\bcattaneo\b", "Cattaneo"),
    "fourier": (r"\bfourier\b", "Fourier"),
    "sk_condition": (r"\b(sk|shizuta.{0,3}kawashima)\b", "SK condition"),
    "subcharacteristic": (r"\bsubcharacteristic\b", "subcharacteristic"),
    "gravitation": (r"\bgravitation\b", "gravitation"),
    "simultaneism": (r"\bsimultanei[a-z]*\b", "simultaneism"),
}


def parse_bib(bib_path: Path) -> dict:
    """Return {key: {'names': [..], 'year': str}} from a .bib file."""
    entries = {}
    if not bib_path.exists():
        return entries
    text = bib_path.read_text()
    for m in re.finditer(r"@\w+\{([^,]+),\s*author\s*=\s*[{]\"?([^}\"]+)", text, re.I):
        key = m.group(1).strip()
        authors = re.sub(r"[{}]", "", m.group(2))
        author_names = set()
        for token in re.split(r"\s+and\s+", authors):
            parts = _WORD_RE.findall(norm(token))
            if parts:
                author_names.add(parts[-1])
        ym = re.search(r"year\s*=\s*[{]?\"?(\d{4})", text[m.end():m.end() + 500], re.I)
        entries[key] = {"names": author_names, "year": ym.group(1) if ym else ""}
    return entries


# ── Document / section decomposition ───────────────────────────────

def split_documents(root: Path, exclude: set) -> list:
    docs = []
    for md in sorted(root.rglob("*.md")):
        if md.name in exclude:
            continue
        text = md.read_text()
        docs.append({"path": md, "text": text})
    return docs


def sections_of(doc: dict) -> list:
    """Yield (heading, body) blocks. Leading text becomes heading 'HEAD'."""
    blocks, cur_head, cur_lines = [], "HEAD", []
    for line in doc["text"].splitlines():
        hm = HEADING_RE.match(line)
        if hm:
            blocks.append((cur_head, "\n".join(cur_lines)))
            cur_head = hm.group(1).strip()
            cur_lines = []
        else:
            cur_lines.append(line)
    blocks.append((cur_head, "\n".join(cur_lines)))
    return [(h, b) for h, b in blocks if b.strip()]


def build():
    ap = argparse.ArgumentParser(description="Build co-occurrence hypergraph over RET x TSSI corpus")
    ap.add_argument("--doc-keys", type=int, default=15, help="RAKE keywords kept per document")
    ap.add_argument("--sec-keys", type=int, default=6, help="RAKE keywords kept per section")
    ap.add_argument("--compact", action="store_true",
                    help="Emit only a 5-field summary JSON line (for plumbing `exec` pipelines)")
    args = ap.parse_args()

    bib = parse_bib(CORPUS_DIR / "program" / "references.bib")
    docs = split_documents(CORPUS_DIR, exclude={"AGENTS.md"})

    nodes = {}            # id -> {label, kind}
    edges = []            # {id, nodes:[...], doc, section}
    doc_manifest = []

    def node_id(label: str, kind: str) -> str:
        nid = f"{kind}:{norm(label)}"
        if nid not in nodes:
            nodes[nid] = {"id": nid, "label": label, "kind": kind}
        return nid

    doc_kw = {}
    for doc in docs:
        doc_kw[doc["path"]] = rake_top(doc["text"], args.doc_keys)

    for doc in docs:
        rel = doc["path"].relative_to(CORPUS_DIR).as_posix()
        doc_manifest.append({"doc": rel, "chars": len(doc["text"])})
        for heading, body in sections_of(doc):
            section_norm = norm(body)
            present = set()

            present.add(node_id(f"[{heading}]", "section"))

            for kw in doc_kw[doc["path"]] + rake_top(body, args.sec_keys):
                if norm(kw) in section_norm:
                    present.add(node_id(kw, "keyword"))

            for key in bib:
                en = bib[key]
                if not en["names"]:
                    continue
                if any(norm(n) and regex_any(n, en["year"], section_norm, key) for n in en["names"]):
                    present.add(node_id(key + (f" ({en['year']})" if en["year"] else ""), "citation"))

            for m in ARTIFACT_RE.finditer(section_norm):
                present.add(node_id(m.group(1).upper(), "artifact"))
            for m in TRACK_RE.finditer(section_norm):
                present.add(node_id("Track " + m.group(1).upper(), "artifact"))
            for nid, (pat, label) in NOTATIONS.items():
                if re.search(pat, section_norm):
                    present.add(node_id(label, "notation"))

            if len(present) >= 2:
                eid = f"e{len(edges)}"
                edges.append({
                    "id": eid,
                    "nodes": sorted(present),
                    "doc": rel,
                    "section": heading,
                    "arity": len(present),
                })

    # ── Stats ──────────────────────────────────────────────────────
    kind_counts = Counter(n["kind"] for n in nodes.values())
    arity_hist = Counter(e["arity"] for e in edges)
    degree = Counter()
    for e in edges:
        for n in e["nodes"]:
            degree[n] += 1
    deg_hist = Counter(degree.values())
    top_hubs = sorted(degree.items(), key=lambda x: x[1], reverse=True)[:15]
    hubs = [{"node": n, "kind": nodes[n]["kind"], "label": nodes[n]["label"], "degree": d}
            for n, d in top_hubs]

    stats = {
        "docs": len(docs),
        "sections": sum(1 for d in docs for _ in sections_of(d)),
        "nodes": len(nodes),
        "edges": len(edges),
        "node_kinds": dict(kind_counts),
        "arity_hist": dict(sorted(arity_hist.items())),
        "degree_hist": {str(k): v for k, v in sorted(deg_hist.items())[:25]},
        "mean_degree": round(sum(degree.values()) / len(nodes), 3) if nodes else 0,
        "max_degree": max(degree.values()) if degree else 0,
        "top_hubs": hubs,
        "bib_entries": len(bib),
        "node_rule": "co-occurrence v1 (headers + RAKE keywords + citations + artifacts + notations)",
    }

    # ── Write artifacts ─────────────────────────────────────────────
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.compact:
        print(json.dumps({
            "docs": stats["docs"], "nodes": stats["nodes"], "edges": stats["edges"],
            "mean_degree": stats["mean_degree"], "max_degree": stats["max_degree"],
        }, default=str))
        return

    graph = {
        "meta": {
            "corpus_dir": str(CORPUS_DIR),
            "built_at": None,
            "node_rule": stats["node_rule"],
            "format": "hypergraph-json-v1 (HNX-compatible: V, E, He)",
        },
        "V": [{"id": nid, **node} for nid, node in nodes.items()],
        "E": [{"id": e["id"], "members": e["nodes"]} for e in edges],
        "nodes": nodes,
        "hyperedges": edges,
    }
    (OUT_DIR / "hypergraph.json").write_text(json.dumps(graph, indent=1, default=str))

    with (OUT_DIR / "provenance.tsv").open("w") as f:
        f.write("edge_id\tdoc\tsection\tarity\n")
        for e in edges:
            f.write(f"{e['id']}\t{e['doc']}\t{e['section'].replace(chr(9), ' ')}\t{e['arity']}\n")

    (OUT_DIR / "stats.json").write_text(json.dumps(stats, indent=1, default=str))

    print(json.dumps(stats, indent=1, default=str))


def regex_any(name: str, year: str, text: str, key: str) -> bool:
    if norm(key).split("(")[0].strip() in text:
        return True
    if year and re.search(rf"\b{re.escape(name)}[^.\n]{{0,20}}{year}", text):
        return True
    return bool(year and re.search(rf"{year}[^.\n]{{0,20}}\b{re.escape(name)}", text))


if __name__ == "__main__":
    build()