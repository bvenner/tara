#!/usr/bin/env python3
"""TARA — one-shot AnyType export (Phase 0 of the AnyType-elimination plan).

Copies every object out of AnyType into the local SQLite metadata store
(GraphStore) plus a markdown + JSON safety-net dump under data/.

Prereqs (from the project repo root, devenv shell active):
    anytype serve --listen-address 127.0.0.1:31012 > /tmp/anytype-server.log 2>&1 &

Usage (default is dry-run — lists and classifies, writes nothing):
    python scripts/export_anytype.py
    python scripts/export_anytype.py --commit   # write to SQLite + dump files
    python scripts/export_anytype.py --verify   # print current AnyType + SQLite counts
"""
import sys
import os
import json
import re
import sqlite3
import argparse
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

for _k in ("ANYTYPE_API_BASE_URL", "ANYTYPE_API_KEY", "ANYTYPE_SPACE_ID"):
    _v = os.environ.get(_k, "")
    if _v.startswith('"') and _v.endswith('"'):
        os.environ[_k] = _v[1:-1]

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))

import anytype_client as at
from graph_store import GraphStore

PROJECTS_TABLES = """
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    question TEXT,
    domain TEXT,
    status TEXT DEFAULT 'active',
    started TEXT,
    workspace_path TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS experiments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER REFERENCES projects(id) ON DELETE CASCADE,
    slug TEXT NOT NULL,
    hypothesis TEXT,
    status TEXT DEFAULT 'pending',
    proxy_metric TEXT,
    protocol_path TEXT,
    results_path TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (project_id, slug)
);
"""


def slugify(text: str) -> str:
    return "_".join(w.lower() for w in text.split() if w.isalnum() or w in "-_")[:60]


def field_from_body(body: str, key: str) -> str:
    prefix = f"**{key}:**"
    for line in body.splitlines():
        s = line.strip()
        if s.startswith(prefix):
            return s[len(prefix):].strip()
    return ""


def section_from_body(body: str, heading: str) -> str:
    out, inside = [], False
    for line in body.splitlines():
        if line.strip().startswith("## " + heading):
            inside = True
            continue
        if inside and line.strip().startswith("## "):
            break
        if inside:
            out.append(line)
    return "\n".join(out).strip()


def fetch_all_objects() -> list:
    objs, offset, limit = [], 0, 50
    while True:
        page = at.list_objects(limit=limit, offset=offset)
        if not page:
            break
        objs.extend(page)
        if len(page) < limit:
            break
        offset += limit
    return objs


def fetch_detail(obj: dict) -> dict:
    try:
        return at.get_object(obj["id"]).get("object", {})
    except Exception:
        return {}


def classify(name: str) -> str:
    for prefix in ("Paper:", "Author:", "Project:", "Experiment:"):
        if name.startswith(prefix):
            return prefix.rstrip(":")
    return "Other"


def parse_host(kind: str, name: str, det: dict) -> dict:
    rec = {"id": det.get("id") or name, "name": name, "body": det.get("markdown", ""),
           "archived": bool(det.get("archived")), "type_key": (det.get("type") or {}).get("key", "")}
    if kind == "Paper":
        title = name[len("Paper:"):].strip()
        doi = field_from_body(rec["body"], "DOI")
        rec["fields"] = {
            "title": title,
            "doi": doi,
            "arxiv_id": field_from_body(rec["body"], "arXiv"),
            "year": (lambda y: int(y) if y.isdigit() else None)(field_from_body(rec["body"], "Year")),
            "venue": field_from_body(rec["body"], "Venue"),
            "citation_count": (lambda c: int(c) if c.isdigit() else 0)(field_from_body(rec["body"], "Citations")),
            "abstract": section_from_body(rec["body"], "Abstract"),
        }
    elif kind == "Project":
        rec["fields"] = {
            "title": name[len("Project:"):].strip(),
            "question": field_from_body(rec["body"], "Research Question"),
            "status": field_from_body(rec["body"], "Status") or "active",
            "domain": field_from_body(rec["body"], "Domain"),
            "started": field_from_body(rec["body"], "Started"),
        }
    elif kind == "Experiment":
        rec["fields"] = {
            "title": name[len("Experiment:"):].strip(),
        }
    elif kind == "Author":
        rec["fields"] = {"name": name[len("Author:"):].strip()}
    return rec


def write_dumps(records: list, stamp: str) -> tuple:
    data_dir = Path(os.path.dirname(__file__)).parent / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    md_path = data_dir / f"anytype-export-{stamp}.md"
    js_path = data_dir / f"anytype-export-{stamp}.json"
    md_lines = [f"# AnyType export — {stamp}", "", f"Total objects: {len(records)}", ""]
    for r in records:
        md_lines += [
            f"## {r['name']}", "",
            f"- AnyType ID: `{r['id']}`",
            f"- Type key: `{r['type_key']}`",
            f"- Archived: {r['archived']}",
            "",
            (r["body"] or "(empty body)").strip(),
            "",
            "---", "",
        ]
    md_path.write_text("\n".join(md_lines))
    js_path.write_text(json.dumps(records, indent=2, default=str))
    return md_path, js_path


def ensure_tables(graph: GraphStore):
    with graph._conn() as conn:
        conn.executescript(PROJECTS_TABLES)


def export_paper(graph: GraphStore, rec: dict) -> str:
    f = rec["fields"]
    paper = {**f, "anytype_id": rec["id"]}
    try:
        pid = graph.add_paper(paper)
        return f"paper#{pid}"
    except sqlite3.IntegrityError as e:
        if "anytype_id" not in str(e):
            raise
        with graph._conn() as conn:
            conn.execute("UPDATE papers SET anytype_id=NULL WHERE anytype_id=?", (rec["id"],))
        pid = graph.add_paper(paper)
        return f"paper#{pid} (stale anytype link cleared)"


def _paper_preference(rec: dict) -> int:
    """Score a Paper record: prefer real arXiv identifiers and sane years."""
    ar = rec["fields"].get("arxiv_id", "")
    year = rec["fields"].get("year")
    score = 0
    if re.match(r"^\d{4}\.\d{4,5}", ar):
        score += 3
    if isinstance(year, int) and 1980 <= year <= 2024:
        score += 2
    if rec["fields"].get("doi"):
        score += 1
    return score


def dedupe_papers(records: list) -> tuple:
    """Keep one record per normalized paper title; return (kept, dropped)."""
    kept, dropped = [], []
    by_title = {}
    for r in records:
        if classify(r["name"]) != "Paper":
            kept.append(r)
            continue
        t = r["fields"]["title"].lower()
        if t not in by_title:
            by_title[t] = r
            continue
        cur = by_title[t]
        if _paper_preference(r) > _paper_preference(cur):
            dropped.append(cur)
            by_title[t] = r
        else:
            dropped.append(r)
    kept = [r for r in kept if classify(r["name"]) != "Paper"] + list(by_title.values())
    return kept, dropped


def export_author(graph: GraphStore, rec: dict) -> str:
    aid = graph.add_author(rec["fields"]["name"], anytype_id=rec["id"])
    return f"author#{aid}"


def export_project(graph: GraphStore, rec: dict) -> str:
    f = rec["fields"]
    with graph._conn() as conn:
        row = conn.execute("SELECT id FROM projects WHERE title=? LIMIT 1", (f["title"],)).fetchone()
        if row:
            conn.execute(
                "UPDATE projects SET question=?, status=?, domain=?, started=?, updated_at=CURRENT_TIMESTAMP WHERE id=?",
                (f.get("question"), f.get("status"), f.get("domain"), f.get("started"), row["id"]),
            )
            return f"project#{row['id']} (updated)"
        cur = conn.execute(
            "INSERT INTO projects (title, question, status, domain, started) VALUES (?, ?, ?, ?, ?)",
            (f["title"], f.get("question"), f.get("status"), f.get("domain"), f.get("started")),
        )
        return f"project#{cur.lastrowid} (new)"


def export_experiment(graph: GraphStore, rec: dict) -> str:
    f = rec["fields"]
    slug = slugify(f["title"])
    with graph._conn() as conn:
        row = conn.execute(
            "SELECT id FROM experiments WHERE slug=? AND project_id IS NULL LIMIT 1", (slug,)
        ).fetchone()
        if row:
            return f"experiment#{row['id']} (exists)"
        cur = conn.execute("INSERT INTO experiments (slug, hypothesis) VALUES (?, ?)", (slug, f.get("title")))
        return f"experiment#{cur.lastrowid} (new)"


def main():
    ap = argparse.ArgumentParser(description="Export AnyType objects into the SQLite metadata store")
    ap.add_argument("--commit", action="store_true", help="Write to SQLite and write dump files (default: dry-run)")
    ap.add_argument("--verify", action="store_true", help="Print AnyType + SQLite counts and exit")
    args = ap.parse_args()

    try:
        at.list_spaces()
    except Exception as e:
        print(f"ERROR: cannot reach AnyType server ({e}). Start it with:\n  anytype serve --listen-address 127.0.0.1:31012")
        sys.exit(1)

    raw = fetch_all_objects()
    if not raw:
        print("No objects found in AnyType. Nothing to export.")
        return

    counts = Counter(classify(o.get("name", "")) for o in raw)
    print(f"AnyType has {len(raw)} object(s): {dict(counts)}")

    if args.verify:
        print("Verification counts from SQLite:", GraphStore().stats())
        return

    records = []
    for o in raw:
        det = fetch_detail(o)
        rec = parse_host(classify(o.get("name", "")), o.get("name", "(unnamed)"), det or o)
        records.append(rec)

    if not args.commit:
        print("\nDRY-RUN — no writes. Would export:")
        for kind in ("Paper", "Author", "Project", "Experiment", "Other"):
            subset = [r for r in records if classify(r["name"]) == kind]
            if not subset:
                continue
            print(f"\n  [{kind}] {len(subset)}")
            for r in subset:
                name = r.get("fields", {}).get("title") or r.get("fields", {}).get("name") or r["name"]
                flag = " [archived]" if r["archived"] else ""
                print(f"    - {name}{flag}")
        print("\nRun with --commit to write to SQLite and data/ dump files.")
        return

    graph = GraphStore()
    ensure_tables(graph)

    records, dropped = dedupe_papers(records)
    if dropped:
        print(f"\nDeduplicating papers by title: {len(dropped)} duplicate object(s) kept only in the dump files:")
        for d in dropped:
            f = d["fields"]
            print(f"  - {f['title'][:70]} (arxiv:{f.get('arxiv_id') or '-'} year:{f.get('year') or '-'})")

    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")

    print(f"\nExporting {len(records)} object(s) into SQLite and data/anytype-export-{stamp}.*")
    results = []
    by_kind = {"Paper": None, "Author": None, "Project": None, "Experiment": None, "Other": None}
    for r in records:
        kind = classify(r["name"])
        try:
            outcome = {"Paper": export_paper, "Author": export_author,
                       "Project": export_project, "Experiment": export_experiment}[kind](graph, r)
            results.append(f"  [OK ] {kind}  {outcome}  —  {r['name'][:70]}")
        except Exception as e:
            results.append(f"  [FAIL] {kind}  {r['name'][:70]}  ({e})")

    print("\n".join(results))

    md_path, js_path = write_dumps(records, stamp)
    print(f"\nDump files written:\n  {md_path}\n  {js_path}")

    print("\nPost-export SQLite state:")
    with graph._conn() as conn:
        for tbl in ("papers", "authors", "projects", "experiments"):
            n = conn.execute(f"SELECT COUNT(*) FROM {tbl}").fetchone()[0]
            print(f"  {tbl}: {n}")

    print("\nNext: spot-check 3+ objects per type in SQLite (see plan §5, step 2).")
    print("AnyType now becomes a read-only reference until decommission (Phase 3).")


if __name__ == "__main__":
    main()