#!/usr/bin/env python3
"""
TARA Phase 1 — PDF Ingestion Pipeline

Usage:
    cd ~/Documents/Research && devenv shell

    # Single paper
    python scripts/ingest_pdf.py papers/incoming/some-paper.pdf

    # With title override (when extraction fails)
    python scripts/ingest_pdf.py papers/incoming/some-paper.pdf --title "Correct Title"

    # Batch: process all PDFs in a directory
    python scripts/ingest_pdf.py papers/incoming/ --batch

    # Dry-run: preview what would be created (no side effects)
    python scripts/ingest_pdf.py papers/incoming/ --batch --dry-run
"""
import os
import sys
import shutil
import json
import argparse
from pathlib import Path
from typing import Optional, Dict, List, Any, Tuple

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
from arxiv_client import get_work_by_arxiv_id
from pdf_metadata import write_pdf_metadata

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


def merge_metadata(
    extracted: Dict[str, Any],
    arxiv_data: Optional[Dict[str, Any]] = None,
    oa_data: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Merge metadata sources: arXiv > OpenAlex > extracted."""
    arxiv = arxiv_data or {}
    oa = oa_data or {}

    title = arxiv.get("title") or oa.get("title") or extracted.get("title") or "Untitled Paper"
    abstract = arxiv.get("abstract") or oa.get("abstract") or extracted.get("abstract") or ""
    doi = arxiv.get("doi") or oa.get("doi") or extracted.get("doi") or ""
    arxiv_id = arxiv.get("arxiv_id") or extracted.get("arxiv_id", "")

    year = ""
    if arxiv.get("published"):
        year = arxiv["published"][:4]
    elif oa.get("publication_year"):
        year = str(oa["publication_year"])

    authors = arxiv.get("authors") or oa.get("authors") or extracted.get("authors") or []
    citation_count = oa.get("citation_count", 0)
    oa_url = arxiv.get("pdf_url") or oa.get("open_access_url", "")
    venue = arxiv.get("journal_ref") or oa.get("venue", "")
    categories = arxiv.get("categories", [])

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
        "categories": categories,
        "full_text": extracted.get("full_text", "")[:5000],
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
    if meta.get("categories"):
        lines.append(f"**Categories:** {', '.join(meta['categories'])}")
    lines.append("")
    if meta.get("abstract"):
        lines.append("## Abstract")
        lines.append(meta["abstract"])
        lines.append("")
    if meta.get("source_path"):
        lines.append(f"## Source")
        lines.append(f"PDF stored at: `{meta['source_path']}`")
    return "\n".join(lines)


def find_existing_paper(meta: Dict[str, Any], space_id: str) -> Optional[str]:
    """Search AnyType for an existing Paper with the same DOI, arXiv ID, or title.
    Returns the object ID if found, None otherwise.
    """
    # 1. Search by DOI (most specific)
    if meta.get("doi"):
        results = search_objects(meta["doi"], limit=10)
        for obj in results:
            name = obj.get("name", "")
            if name.startswith("Paper:") and meta["doi"] in name:
                return obj["id"]

    # 2. Search by arXiv ID
    if meta.get("arxiv_id"):
        query = f"arXiv: {meta['arxiv_id']}"
        results = search_objects(query, limit=10)
        for obj in results:
            if obj.get("name", "").startswith("Paper:"):
                return obj["id"]

    # 3. Search by title
    if meta.get("title"):
        results = search_objects(meta["title"], limit=10)
        for obj in results:
            if obj.get("name", "").lower() == f"paper: {meta['title']}".lower():
                return obj["id"]

    return None


def create_author_objects(authors: List[str], space_id: str, dry_run: bool = False) -> List[str]:
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
                if dry_run:
                    print(f"    [dry-run] Would link existing Author: {name}")
                break
        if found:
            continue

        if dry_run:
            print(f"    [dry-run] Would create Author: {name}")
            ids.append("<dry-run-id>")
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


def ingest_pdf(
    pdf_path: str,
    override_title: Optional[str] = None,
    dry_run: bool = False,
) -> Tuple[bool, str]:
    """Ingest a single PDF.

    Returns:
        (success: bool, message: str)
    """
    pdf = Path(pdf_path)
    if not pdf.exists():
        return False, f"PDF not found: {pdf_path}"

    space_id = _resolve_space_id()
    prefix = "[dry-run] " if dry_run else ""
    print(f"{prefix}Processing: {pdf.name}")
    print(f"  1. Extracting from PDF...")

    extracted = extract_from_pdf(str(pdf))
    print(f"     Title (extracted): {extracted.get('title') or 'N/A'}")
    print(f"     DOI (extracted):   {extracted.get('doi') or 'N/A'}")
    print(f"     arXiv (extracted): {extracted.get('arxiv_id') or 'N/A'}")

    # 2. Enrichment
    arxiv_data = None
    oa_data = None
    arxiv_id = extracted.get("arxiv_id")
    doi = extracted.get("doi")
    title = override_title or extracted.get("title")

    if arxiv_id:
        print(f"  2. Querying arXiv API: {arxiv_id}")
        arxiv_data = get_work_by_arxiv_id(arxiv_id)
        if arxiv_data:
            print(f"     Found: {arxiv_data.get('title')}")
        else:
            print("     Not found by arXiv ID.")

    if not arxiv_id and not arxiv_data:
        if doi:
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
            print("  2. Skipping enrichment (no identifiers found)")

    # 3. Merge metadata
    meta = merge_metadata(extracted, arxiv_data=arxiv_data, oa_data=oa_data)
    print(f"  3. Merged metadata → Title: {meta['title']}")

    # 4. Duplicate detection
    print("  4. Checking for duplicates...")
    existing_id = find_existing_paper(meta, space_id)
    if existing_id:
        print(f"     ⚠️  Duplicate found: {existing_id}")
        print(f"     Skipping creation.")
        return True, f"duplicate:{existing_id}"

    if dry_run:
        print(f"     [dry-run] Would create Paper: {meta['title']}")
    else:
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
            return False, "create_failed"
        print(f"     Paper ID: {paper_id}")

    # 5. Create Author objects
    if meta.get("authors"):
        print("  5. Creating Author objects...")
        author_ids = create_author_objects(meta["authors"], space_id, dry_run=dry_run)
        print(f"     Created/linked {len(author_ids)} author(s)")
    else:
        print("  5. No authors to create.")

    # 6. Move PDF to processed
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    dest = PROCESSED_DIR / pdf.name
    if dry_run:
        print(f"  6. [dry-run] Would move PDF to: {dest}")
    else:
        shutil.move(str(pdf), str(dest))
        print(f"  6. Moved PDF to: {dest}")

        # 7. Write metadata into the PDF itself for portability
        print("  7. Embedding metadata into PDF...")
        try:
            write_pdf_metadata(str(dest), meta)
        except Exception as e:
            print(f"    WARNING: Could not write PDF metadata: {e}")

    print(f"\n✅ {prefix}Ingest complete.")
    if not dry_run:
        print(f"   Paper:  https://anytype.io/{paper_id}")
        print(f"   PDF:    {dest}")
    return True, "success"


def ingest_batch(
    directory: str,
    override_title: Optional[str] = None,
    dry_run: bool = False,
) -> None:
    """Process all PDFs in a directory."""
    dir_path = Path(directory)
    if not dir_path.exists():
        print(f"ERROR: Directory not found: {directory}")
        sys.exit(1)

    pdf_files = sorted(dir_path.glob("*.pdf"))
    if not pdf_files:
        print(f"No PDF files found in {directory}")
        return

    print(f"Found {len(pdf_files)} PDF(s) in {dir_path}\n")
    print("=" * 60)

    results: List[Tuple[str, bool, str]] = []
    for i, pdf in enumerate(pdf_files, 1):
        print(f"\n[{i}/{len(pdf_files)}]")
        ok, msg = ingest_pdf(str(pdf), override_title=override_title, dry_run=dry_run)
        results.append((pdf.name, ok, msg))
        print("-" * 40)

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    successes = sum(1 for _, ok, _ in results if ok)
    failures = len(results) - successes
    print(f"Total:   {len(results)}")
    print(f"Success: {successes}")
    print(f"Failed:  {failures}")

    for name, ok, msg in results:
        status = "✅" if ok else "❌"
        if msg.startswith("duplicate:"):
            status = "⚠️ "
            msg = f"duplicate ({msg.split(':')[1]})"
        print(f"  {status} {name}: {msg}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TARA PDF Ingestion Pipeline")
    parser.add_argument("path", help="Path to PDF file or directory")
    parser.add_argument("--title", help="Override paper title for enrichment lookup")
    parser.add_argument("--batch", action="store_true", help="Process all PDFs in directory")
    parser.add_argument("--dry-run", action="store_true", help="Preview without side effects")
    args = parser.parse_args()

    target = Path(args.path)
    if args.batch or target.is_dir():
        ingest_batch(args.path, override_title=args.title, dry_run=args.dry_run)
    else:
        ok, msg = ingest_pdf(args.path, override_title=args.title, dry_run=args.dry_run)
        if not ok:
            sys.exit(1)
