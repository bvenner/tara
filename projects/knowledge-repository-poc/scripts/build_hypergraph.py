#!/usr/bin/env python3
"""Co-occurrence hypergraph builder (Phase A v1 -> Phase B).

Builds a statistical (no-LLM) hypergraph over a corpus manifest:
  - local markdown roots (projects) listed in corpus.json
  - external OpenAlex work records under corpus/external/*.json

Node kinds: section, keyword, citation, artifact, notation, project,
work (external OpenAlex works), author (from bibliography / work records).
Hyperedges: sets of concepts co-occurring per section of each document.

Outputs (under <poc>/graph/):
  hypergraph.json   — nodes, hyperedges, provenance, HNX-compatible shape
  index.json        — node -> incident edge ids (query sidecar; sha of hypergraph)
  provenance.tsv    — per-hyperedge doc/section provenance
  stats.json        — counts, degree/arity distributions, hub-coverage warning
    
Incremental fast path: a content-hash of every document and the manifest
is stored in graph/build_meta.json; when nothing changed, artifacts are
not rewritten and the stored summary is emitted.

Usage:
    python scripts/build_hypergraph.py [--force] [--compact]
"""
import argparse
import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from schemas import IngestSummary  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_DIR = Path(__file__).resolve().parents[1] / "graph"
DEFAULT_MANIFEST = Path(__file__).resolve().parents[1] / "corpus.json"
META_FILE = OUT_DIR / "build_meta.json"


def _ingest_summary(stats: dict) -> IngestSummary:
    """Validate the compact ingest summary against the .plumb boundary type."""
    return IngestSummary(
        docs=stats.get("docs", 0), nodes=stats.get("nodes", 0),
        edges=stats.get("edges", 0), mean_degree=stats.get("mean_degree", 0),
        max_degree=stats.get("max_degree", 0),
    )

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
                nm = parts[-1]
                if len(nm) >= 2 and nm not in {"et", "al"}:
                    author_names.add(nm)
        ym = re.search(r"year\s*=\s*[{]?\"?(\d{4})", text[m.end():m.end() + 500], re.I)
        entries[key] = {"names": author_names, "year": ym.group(1) if ym else ""}
    return entries


def regex_any(name: str, year: str, text: str, key: str) -> bool:
    if norm(key).split("(")[0].strip() in text:
        return True
    if year and re.search(rf"\b{re.escape(name)}[^.\n]{{0,20}}{year}", text):
        return True
    return bool(year and re.search(rf"{year}[^.\n]{{0,20}}\b{re.escape(name)}", text))


# ── Corpus loading (manifest-driven) ───────────────────────────────

def load_manifest(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"manifest not found: {path}")
    return json.loads(path.read_text())


def collect_docs(manifest: dict) -> list:
    docs = []
    for root in manifest.get("roots", []):
        base = REPO_ROOT / root["dir"]
        exclude = set(root.get("exclude", []))
        for md in sorted(base.glob(root.get("glob", "**/*.md"))):
            if md.name in exclude:
                continue
            rel = md.relative_to(base).as_posix()
            docs.append({
                "name": f"{root['name']}/{rel}",
                "project": root["name"],
                "text": md.read_text(),
                "single_section": False,
            })
    ext_dir = REPO_ROOT / manifest.get("external_dir", "")
    for jf in sorted(ext_dir.glob("*.json")):
        rec = json.loads(jf.read_text())
        title = rec.get("title", "")
        abstract = rec.get("abstract", "")
        docs.append({
            "name": f"openalex/{jf.stem}",
            "project": "openalex",
            "text": f"{title}\n\n{abstract}".strip(),
            "single_section": True,
            "record": rec,
        })
    return docs


def collect_bib(manifest: dict) -> dict:
    entries = {}
    for root in manifest.get("roots", []):
        bib = REPO_ROOT / root["dir"] / manifest.get("bib_glob", "program/references.bib")
        entries.update(parse_bib(bib))
    return entries


def sections_of(doc: dict) -> list:
    if doc.get("single_section"):
        return [(doc["name"], doc["text"])]
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


# ── Build ──────────────────────────────────────────────────────────

def build():
    ap = argparse.ArgumentParser(description="Build co-occurrence hypergraph over a corpus manifest")
    ap.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    ap.add_argument("--doc-keys", type=int, default=15, help="RAKE keywords kept per document")
    ap.add_argument("--sec-keys", type=int, default=6, help="RAKE keywords kept per section")
    ap.add_argument("--force", action="store_true", help="Rebuild even if the corpus is unchanged")
    ap.add_argument("--compact", action="store_true",
                    help="Emit only a summary JSON line (for plumbing `exec` pipelines)")
    args = ap.parse_args()

    manifest = load_manifest(args.manifest)
    docs = collect_docs(manifest)
    bib = collect_bib(manifest)

    manifest_sha = hashlib.sha256(json.dumps(manifest, sort_keys=True).encode()).hexdigest()
    doc_hashes = {d["name"]: hashlib.sha256(d["text"].encode()).hexdigest() for d in docs}
    current = {"manifest_sha": manifest_sha, "docs": doc_hashes, "n_docs": len(docs)}
    previous = {}
    if META_FILE.exists():
        try:
            previous = json.loads(META_FILE.read_text())
        except Exception:
            previous = {}

    if not args.force and previous.get("manifest_sha") == current["manifest_sha"] \
            and previous.get("docs") == current["docs"] \
            and (OUT_DIR / "hypergraph.json").exists():
        cached = previous.get("stats", {})
        if args.compact:
            print(_ingest_summary(cached).model_dump_json())
        else:
            print("unchanged:", json.dumps(cached, default=str))
        return

    nodes = {}
    edges = []
    sections_total = 0
    doc_kw = {d["name"]: rake_top(d["text"], args.doc_keys) for d in docs}

    def node_id(label: str, kind: str) -> str:
        nid = f"{kind}:{norm(label)}"
        if nid not in nodes:
            nodes[nid] = {"id": nid, "label": label, "kind": kind}
        return nid

    for doc in docs:
        sections_total += len(sections_of(doc))
        project_name = doc["project"]
        record = doc.get("record")

        for heading, body in sections_of(doc):
            section_norm = norm(body)
            present = {node_id(project_name, "project")}

            if doc.get("single_section") and record:
                title = record.get("title", "")
                ident = norm(record.get("doi") or record.get("openalex_id") or title)
                present.add(node_id(title, "work"))
                for aname in record.get("authors", []):
                    if aname:
                        present.add(node_id(aname, "author"))
            else:
                present.add(node_id(f"[{heading}]", "section"))

            for kw in doc_kw[doc["name"]] + rake_top(body, args.sec_keys):
                if norm(kw) in section_norm:
                    present.add(node_id(kw, "keyword"))

            for key, en in bib.items():
                if not en["names"]:
                    continue
                if any(norm(n) and regex_any(n, en["year"], section_norm, key) for n in en["names"]):
                    present.add(node_id(key + (f" ({en['year']})" if en["year"] else ""), "citation"))
                    for n in sorted(en["names"]):
                        present.add(node_id(n, "author"))

            for m in ARTIFACT_RE.finditer(section_norm):
                present.add(node_id(m.group(1).upper(), "artifact"))
            for m in TRACK_RE.finditer(section_norm):
                present.add(node_id("Track " + m.group(1).upper(), "artifact"))
            for nid, (pat, label) in NOTATIONS.items():
                if re.search(pat, section_norm):
                    present.add(node_id(label, "notation"))

            if len(present) >= 2:
                edges.append({
                    "id": f"e{len(edges)}",
                    "nodes": sorted(present),
                    "doc": doc["name"],
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
    top_hubs = sorted(degree.items(), key=lambda x: x[1], reverse=True)[:15]
    degree_hist = {}
    for lo, hi in [(1, 1), (2, 2), (3, 5), (6, 10), (11, 20), (21, 50),
                   (51, 100), (101, 500), (501, None)]:
        label = f"{lo}+" if hi is None else (str(lo) if lo == hi else f"{lo}-{hi}")
        cnt = sum(c for c in degree.values() if c >= lo and (hi is None or c <= hi))
        if cnt:
            degree_hist[label] = cnt
    hub_coverage = round(max(
        (c for n, c in degree.items() if nodes[n]["kind"] == "keyword"), default=0) / len(edges), 3) if edges else 0

    stats = {
        "docs": len(docs),
        "sections": sections_total,
        "nodes": len(nodes),
        "edges": len(edges),
        "node_kinds": dict(kind_counts),
        "arity_hist": dict(sorted(arity_hist.items())),
        "mean_degree": round(sum(degree.values()) / len(nodes), 3) if nodes else 0,
        "max_degree": max(degree.values()) if degree else 0,
        "top_hubs": [{"node": n, "kind": nodes[n]["kind"], "label": nodes[n]["label"], "degree": d}
                     for n, d in top_hubs],
        "degree_hist": degree_hist,
        "hub_coverage": hub_coverage,
        "bib_entries": len(bib),
        "projects": [root["name"] for root in manifest.get("roots", [])],
        "external_works": sum(1 for d in docs if d.get("single_section")),
        "node_rule": "co-occurrence v2 (project/root + headers + RAKE keywords + citations+ "
                     "authors + artifacts + notations + external OpenAlex works)",
    }

    # ── Write artifacts ─────────────────────────────────────────────
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if args.compact:
        current["stats"] = stats
        META_FILE.write_text(json.dumps(current, indent=1, default=str))
        print(_ingest_summary(stats).model_dump_json())
        return

    graph = {
        "meta": {
            "manifest": args.manifest.name,
            "node_rule": stats["node_rule"],
            "format": "hypergraph-json-v1 (HNX-compatible: V, E, He)",
        },
        "V": [{"id": nid, **node} for nid, node in nodes.items()],
        "E": [{"id": e["id"], "members": e["nodes"]} for e in edges],
        "nodes": nodes,
        "hyperedges": edges,
    }
    graph_json = json.dumps(graph, indent=1, default=str)
    (OUT_DIR / "hypergraph.json").write_text(graph_json)
    index = {}
    for e in edges:
        for n in e["nodes"]:
            index.setdefault(n, []).append(e["id"])
    index_art = {"hypergraph_sha": hashlib.sha256(graph_json.encode()).hexdigest(), "index": index}
    (OUT_DIR / "index.json").write_text(json.dumps(index_art, indent=1, default=str))
    with (OUT_DIR / "provenance.tsv").open("w") as f:
        f.write("edge_id\tdoc\tsection\tarity\n")
        for e in edges:
            f.write(f"{e['id']}\t{e['doc']}\t{e['section'].replace(chr(9), ' ')}\t{e['arity']}\n")
    (OUT_DIR / "stats.json").write_text(json.dumps(stats, indent=1, default=str))

    current["stats"] = stats
    META_FILE.write_text(json.dumps(current, indent=1, default=str))
    print(json.dumps(stats, indent=1, default=str))


if __name__ == "__main__":
    build()