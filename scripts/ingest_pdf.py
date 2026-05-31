#!/usr/bin/env python3
"""
TARA Phase 1 — PDF Ingestion Pipeline

Usage:
    cd ~/Documents/Research && devenv shell
    python scripts/ingest_pdf.py papers/incoming/some-paper.pdf

Flow:
    1. Extract text/metadata from PDF (Docling)
    2. Enrich via OpenAlex (DOI or title search)
    3. Create AnyType Paper object + Author objects
    4. Move PDF to papers/processed/

Environment:
    Expects ANYTYPE_API_KEY, ANYTYPE_API_BASE_URL, and ANYTYPE_SPACE_ID
    in the environment (sourced from .env automatically when using devenv).
"""
import os
import sys
import shutil
import json
import argparse
from pathlib import Path
from typing import Optional, Dict, List, Any

# Load .env if present
_env_path = Path(__file__).parent.parent / ".env"
if _env_path.exists():
    with open(_env_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if key not in os.environ:
                    os.environ[key] = value

# Add lib/ to path
sys.path.insert(0, str(Path(__file__).parent / "lib"))

from anytype_client import create_object, search_objects, update_object, list_spaces, SPACE_ID
from pdf_extractor import extract_from_pdf
from openalex_client import get_work_by_doi, get_work_by_arxiv, search_works, normalize_work

# Configuration
INCOMING_DIR = Path("~/Documents/Research/papers/incoming").expanduser()
PROCESSED_DIR = Path("~/Documents/Research/papers/processed").expanduser()


def _resolve_space_id() -> str:
    sid = SPACE_ID
    if not sid:
        spaces = list_spaces()
        if spaces:
            sid = spaces[0]["id"]
            os.environ["ANYTYPE_SPACE_ID"] = sid
        else:
            raise RuntimeError("No AnyType spaces found. Is the server running?")
    return sid


def merge_metadata(extracted: Dict[str, Any], oa: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """Prefer OpenAlex data, fall back to extracted."""
    oa = oa or {}
    title = oa.get("title") or extracted.get("title") or "Untitled Paper"
    abstract = oa.get("abstract") or extracted.get("abstract") or ""
    doi = oa.get("doi") or extracted.get("doi") or ""
    arxiv_id = extracted.get("arxiv_id", "")
    year = oa.get("publication_year") or ""
    authors = oa.get("authors") or extracted.get("authors") or []
    citation_count = oa.get("citation_count", 0)
    oa_url = oa.get("open_access_url", "")
    venue = oa.get("venue", "")
    return {
        "title": title,
        "abstract": abstract,
        "doi": doi,
        "arxiv_id": arxiv_id,
        "year": year,
        "authors": authors,
        "citation_count": citation_count,
        "open_access_url": oa_url,
        "venue": venue,
        "full_text": extracted.get("full_text", "")[:5000],  # truncated for body
        "source_path": extracted.get("source_path", ""),
    }


def build_paper_body(meta: Dict[str, Any]) -> str:
    """Build Markdown body for the Paper object."""
    lines = [
        f"# {meta['title']}",
        "",
    ]
    if meta.get("arxiv_id"):
        lines.append(f"**arXiv:** {meta['arxiv_id']}")
    if meta.get("doi"):
        lines.append(f"**DOI:** {meta['doi']}")
    if meta.get("year"):
        lines.append(f"**Year:** {meta['year']}")
    if meta.get("venue"):
        lines.append(f"**Venue:** {meta['venue']}")
    if meta.get("citation_count"):
        lines.append(f"**Citations:** {meta['citation_count']}")
    if meta.get("open_access_url"):
        lines.append(f"**Open Access URL:** {meta['open_access_url']}")
    if meta.get("authors"):
        lines.append(f"**Authors:** {', '.join(meta['authors'])}")
    lines.append("")
    if meta.get("abstract"):
        lines.append("## Abstract")
        lines.append(meta["abstract"])
        lines.append("")
    if meta.get("source_path"):
        lines.append(f"## Source")
        lines.append(f"PDF stored at: `{meta['source_path']}`")
    return "\n".join(lines)


def create_author_objects(authors: List[str], space_id: str) -> List[str]:
    """Create Author objects in AnyType; return their IDs."""
    ids = []
    for name in authors:
        # Check if author already exists
        existing = search_objects(name, limit=5)
        found = False
        for obj in existing:
            if obj.get("name", "").lower() == f"author: {name}".lower():
                ids.append(obj["id"])
                found = True
                break
        if found:
            continue

        resp = create_object(
            name=f"Author: {name}",
            body=f"# {name}\n\nAuthor object created by TARA ingest pipeline.",
            type_key="page",
            space_id=space_id,
        )
        oid = resp.get("object", {}).get("id")
        if oid:
            ids.append(oid)
            print(f"    Created Author: {name} ({oid})")
        else:
            print(f"    WARNING: Failed to create Author: {name}")
            print(f"    Response: {json.dumps(resp, indent=2)}")
    return ids


def ingest_pdf(pdf_path: str, override_title: Optional[str] = None) -> None:
    pdf = Path(pdf_path)
    if not pdf.exists():
        print(f"ERROR: PDF not found: {pdf_path}")
        sys.exit(1)

    space_id = _resolve_space_id()
    print(f"Space ID: {space_id}")
    print(f"Processing: {pdf.name}")
    print("  1. Extracting from PDF...")

    extracted = extract_from_pdf(str(pdf))
    print(f"     Title (extracted): {extracted.get('title') or 'N/A'}")
    print(f"     DOI (extracted):   {extracted.get('doi') or 'N/A'}")
    print(f"     arXiv (extracted): {extracted.get('arxiv_id') or 'N/A'}")

    # 2. OpenAlex enrichment (try arXiv → DOI → title)
    oa_data = None
    arxiv_id = extracted.get("arxiv_id")
    doi = extracted.get("doi")
    title = override_title or extracted.get("title")

    if arxiv_id:
        print(f"  2. Querying OpenAlex by arXiv ID: {arxiv_id}")
        raw = get_work_by_arxiv(arxiv_id)
        if raw:
            oa_data = normalize_work(raw)
            print(f"     Found: {oa_data.get('title')}")
        else:
            print("     Not found by arXiv ID.")

    if not oa_data and doi:
        print(f"  2. Querying OpenAlex by DOI: {doi}")
        raw = get_work_by_doi(doi)
        if raw:
            oa_data = normalize_work(raw)
            print(f"     Found: {oa_data.get('title')}")
        else:
            print("     Not found by DOI.")

    if not oa_data and title:
        print(f"  2. Querying OpenAlex by title: {title}")
        results = search_works(title, per_page=3)
        if results:
            oa_data = normalize_work(results[0])
            print(f"     Found: {oa_data.get('title')}")
        else:
            print("     Not found by title.")

    if not oa_data:
        print("  2. Skipping OpenAlex (no identifiers found)")

    # 3. Merge
    meta = merge_metadata(extracted, oa_data)
    print(f"  3. Merged metadata → Title: {meta['title']}")

    # 4. Create Paper object
    print("  4. Creating AnyType Paper object...")
    body = build_paper_body(meta)
    paper_resp = create_object(
        name=f"Paper: {meta['title']}",
        body=body,
        type_key="page",
        space_id=space_id,
    )
    paper_id = paper_resp.get("object", {}).get("id")
    if not paper_id:
        print(f"ERROR: Failed to create Paper object.")
        print(f"Response: {json.dumps(paper_resp, indent=2)}")
        sys.exit(1)
    print(f"     Paper ID: {paper_id}")

    # 5. Create Author objects
    if meta.get("authors"):
        print("  5. Creating Author objects...")
        author_ids = create_author_objects(meta["authors"], space_id)
        print(f"     Created/linked {len(author_ids)} author(s)")
    else:
        print("  5. No authors to create.")

    # 6. Move PDF to processed
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    dest = PROCESSED_DIR / pdf.name
    shutil.move(str(pdf), str(dest))
    print(f"  6. Moved PDF to: {dest}")

    print("\n✅ Ingest complete.")
    print(f"   Paper:  https://anytype.io/{paper_id}")
    print(f"   PDF:    {dest}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TARA PDF Ingestion Pipeline")
    parser.add_argument("pdf_path", help="Path to PDF file")
    parser.add_argument("--title", help="Override paper title for OpenAlex lookup")
    args = parser.parse_args()
    ingest_pdf(args.pdf_path, override_title=args.title)
