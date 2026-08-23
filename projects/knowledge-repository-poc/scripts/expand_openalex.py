#!/usr/bin/env python3
"""JSON Lines worker: expand the corpus from OpenAlex (bibliographic truth layer).

Reads one request per stdin line:
  {mode: "topic", topic, limit}
  {mode: "doi",   doi}
  {mode: "arxiv", arxiv_id}
Writes fetched works as records under <poc>/corpus/external/<openalex_id>.json
(idempotent: existing files are skipped), then emits one summary line:
  {mode, matched, written, skipped}

The OpenAlex client comes from the repo's scripts/lib (single bibliographic source).
"""
import json
import re
import sys
from pathlib import Path

POC_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[3]
EXT_DIR = POC_ROOT / "corpus" / "external"

sys.path.insert(0, str(REPO_ROOT / "scripts" / "lib"))
import openalex_client as oa  # noqa: E402


def abstract_text(raw) -> str:
    inv = raw.get("abstract_inverted_index") or {}
    if not inv:
        return ""
    pos = [(i, w) for w, idxs in inv.items() for i in idxs]
    pos.sort()
    return " ".join(w for _, w in pos)


def to_record(raw) -> dict:
    loc = raw.get("primary_location") or {}
    src = loc.get("source") or {}
    return {
        "openalex_id": raw.get("id", ""),
        "doi": raw.get("doi", ""),
        "title": raw.get("display_name", ""),
        "year": raw.get("publication_year"),
        "venue": src.get("display_name", ""),
        "authors": [a["author"]["display_name"]
                    for a in raw.get("authorships", []) if a.get("author", {}).get("display_name")],
        "abstract": abstract_text(raw),
        "citation_count": raw.get("cited_by_count", 0),
    }


def sanitize(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "_", value).strip("_") or "work"


def write_record(rec) -> bool:
    key = sanitize(rec["openalex_id"]) if rec.get("openalex_id") else "doi_" + sanitize(rec.get("doi", ""))
    if not rec.get("title") and not rec.get("abstract"):
        return False
    f = EXT_DIR / f"{key}.json"
    if f.exists():
        return False
    f.write_text(json.dumps(rec, indent=1, default=str))
    return True


def handle(req) -> dict:
    mode = req.get("mode", "topic")
    written = 0
    if mode == "topic":
        topic = req.get("topic", "")
        limit = int(req.get("limit", 5))
        results = oa.search_works(topic, per_page=limit)
    elif mode == "doi":
        raw = oa.get_work_by_doi(req.get("doi", ""))
        results = [raw] if raw else []
    elif mode == "arxiv":
        raw = oa.get_work_by_arxiv(req.get("arxiv_id", ""))
        results = [raw] if raw else []
    else:
        return {"mode": mode, "matched": 0, "written": 0, "skipped": 0}
    matched = len(results)
    seen = set()
    for raw in results:
        rec = to_record(raw)
        ident = rec.get("openalex_id") or rec.get("doi")
        if ident in seen:
            continue
        seen.add(ident)
        if write_record(rec):
            written += 1
    return {"mode": mode, "matched": matched, "written": written,
            "skipped": max(0, matched - written - (matched - len(seen)))}


def main():
    EXT_DIR.mkdir(parents=True, exist_ok=True)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        req = json.loads(line)
        print(json.dumps(handle(req)))
        sys.stdout.flush()


if __name__ == "__main__":
    main()