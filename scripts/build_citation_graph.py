#!/usr/bin/env python3
"""TARA Phase 2 — Build local citation graph from OpenAlex.

Usage:
    python scripts/build_citation_graph.py --init
        Initialize the graph with papers already in AnyType.

    python scripts/build_citation_graph.py --enrich
        For each paper in the graph, fetch references and cited_by
        from OpenAlex and add them as citation edges.

    python scripts/build_citation_graph.py --sync-anytype
        Create AnyType relations (cites) for papers that have
        anytype_ids and citation edges in the local graph.

    python scripts/build_citation_graph.py --stats
        Show graph statistics.

    python scripts/build_citation_graph.py --all
        Run --init, --enrich, and --sync-anytype in sequence.
"""
import argparse
import sys
import os
from pathlib import Path

# Load .env if present (before importing anytype_client)
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

# Ensure scripts/lib is on path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))

from graph_store import GraphStore
from anytype_client import list_objects, create_relation
import openalex_client


def init_graph(graph: GraphStore, space_id: str = None):
    """Pull existing Paper and Author objects from AnyType into the local graph."""
    print("Initializing graph from AnyType...")
    offset = 0
    limit = 50
    count = 0
    count_authors = 0
    count_papers = 0
    while True:
        objs = list_objects(space_id=space_id, limit=limit, offset=offset)
        if not objs:
            break
        for obj in objs:
            # Try to identify Paper/Author objects by type key or name heuristic
            type_key = obj.get("type", {}).get("key", "")
            name = obj.get("name", "")
            if name.startswith("Author: "):
                # Add author to graph
                author_name = name.replace("Author: ", "").strip()
                graph.add_author(author_name, anytype_id=obj.get("id"))
                count += 1
                count_authors += 1
                print(f"  Added author: {author_name}")
                continue
            if type_key not in ("page", "paper") and not name.startswith("Paper:"):
                continue
            # Extract properties if available
            props = obj.get("properties", {})
            doi = props.get("doi", "") if isinstance(props, dict) else ""
            arxiv = props.get("arxiv_id", "") if isinstance(props, dict) else ""
            year = props.get("year", 0) if isinstance(props, dict) else 0
            if isinstance(year, str):
                try:
                    year = int(year)
                except ValueError:
                    year = 0
            paper = {
                "title": name.replace("[Paper] ", "").replace("[Paper]", "").strip(),
                "doi": doi,
                "arxiv_id": arxiv,
                "anytype_id": obj.get("id", ""),
                "year": year,
            }
            # Try to find openalex_id via API lookup
            if arxiv:
                oa = openalex_client.get_work_by_arxiv(arxiv)
                if oa:
                    paper["openalex_id"] = oa.get("id", "")
                    paper["citation_count"] = oa.get("cited_by_count", 0)
            elif doi:
                oa = openalex_client.get_work_by_doi(doi)
                if oa:
                    paper["openalex_id"] = oa.get("id", "")
                    paper["citation_count"] = oa.get("cited_by_count", 0)
            else:
                # Fall back to title search on OpenAlex
                results = openalex_client.search_works(paper["title"], per_page=3)
                if results:
                    best = openalex_client.normalize_work(results[0])
                    paper["openalex_id"] = best.get("openalex_id", "")
                    paper["citation_count"] = best.get("citation_count", 0)
                    paper["doi"] = best.get("doi", "")
                    paper["year"] = best.get("publication_year")
            pid = graph.add_paper(paper)
            count += 1
            count_papers += 1
            print(f"  Added paper: {paper['title'][:60]}")
        offset += limit
        if len(objs) < limit:
            break
    print(f"Initialized {count} object(s) into local graph ({count_authors} authors, {count_papers} papers).")
    return count_papers


def enrich_graph(graph: GraphStore, refs_per_paper: int = 20, cited_by_per_paper: int = 20):
    """Fetch references and cited_by from OpenAlex for all papers in the graph."""
    papers = graph.list_papers(limit=10000)
    print(f"Enriching {len(papers)} paper(s) from OpenAlex...")
    for paper in papers:
        oa_id = paper.get("openalex_id")
        if not oa_id:
            print(f"  Skip (no OpenAlex ID): {paper['title'][:60]}")
            continue
        print(f"  Fetching citations for: {paper['title'][:60]}")
        # References (outgoing)
        refs = openalex_client.get_work_references(oa_id, max_refs=refs_per_paper)
        for ref in refs:
            if not ref.get("title"):
                continue
            ref_paper = {
                "title": ref["title"],
                "doi": ref.get("doi", ""),
                "openalex_id": ref.get("openalex_id", ""),
                "year": ref.get("publication_year"),
                "venue": ref.get("venue", ""),
                "abstract": ref.get("abstract", ""),
                "citation_count": ref.get("citation_count", 0),
            }
            ref_id = graph.add_paper(ref_paper)
            graph.add_citation(paper["id"], ref_id, source="openalex")
        # Cited by (incoming)
        cited_by = openalex_client.get_work_cited_by(oa_id, per_page=cited_by_per_paper)
        for citer in cited_by:
            if not citer.get("title"):
                continue
            citer_paper = {
                "title": citer["title"],
                "doi": citer.get("doi", ""),
                "openalex_id": citer.get("openalex_id", ""),
                "year": citer.get("publication_year"),
                "venue": citer.get("venue", ""),
                "abstract": citer.get("abstract", ""),
                "citation_count": citer.get("citation_count", 0),
            }
            citer_id = graph.add_paper(citer_paper)
            graph.add_citation(citer_id, paper["id"], source="openalex")
    print("Enrichment complete.")


def sync_anytype(graph: GraphStore, space_id: str = None, dry_run: bool = False):
    """Create AnyType relations for citation edges between papers that have anytype_ids."""
    papers = graph.list_papers(limit=10000)
    anytype_map = {p["id"]: p["anytype_id"] for p in papers if p.get("anytype_id")}
    if not anytype_map:
        print("No papers with AnyType IDs found. Run --init first.")
        return
    print(f"Syncing citations to AnyType for {len(anytype_map)} paper(s)...")
    created = 0
    skipped = 0
    for pid in anytype_map:
        from_at = anytype_map.get(pid)
        if not from_at:
            continue
        citations = graph.get_citations(pid)
        for cited in citations:
            to_at = cited.get("anytype_id")
            if not to_at:
                continue
            if dry_run:
                print(f"  [dry-run] Would link {from_at[:20]}... -> {to_at[:20]}...")
                created += 1
                continue
            try:
                create_relation(from_at, to_at, "cites", space_id=space_id)
                created += 1
                print(f"  Created relation: {from_at[:20]}... -> {to_at[:20]}...")
            except Exception as e:
                print(f"  Failed relation: {e}")
                skipped += 1
    print(f"Sync complete. Created: {created}, Skipped: {skipped}")


def show_stats(graph: GraphStore):
    stats = graph.stats()
    print("\n=== TARA Citation Graph Statistics ===")
    print(f"  Papers:    {stats['papers']}")
    print(f"  Authors:   {stats['authors']}")
    print(f"  Citations: {stats['citations']}")
    # Top cited papers
    with graph._conn() as conn:
        rows = conn.execute(
            """SELECT p.title, COUNT(c.from_paper_id) as cnt
               FROM papers p
               JOIN citations c ON p.id = c.to_paper_id
               GROUP BY p.id
               ORDER BY cnt DESC
               LIMIT 10"""
        ).fetchall()
        if rows:
            print("\n  Top cited papers in graph:")
            for row in rows:
                print(f"    {row['cnt']:3d}  {row['title'][:60]}")
    print()


def main():
    parser = argparse.ArgumentParser(description="TARA Citation Graph Builder")
    parser.add_argument("--init", action="store_true",
                        help="Initialize graph from existing AnyType Paper objects")
    parser.add_argument("--enrich", action="store_true",
                        help="Fetch references and cited_by from OpenAlex")
    parser.add_argument("--sync-anytype", action="store_true",
                        help="Create AnyType 'cites' relations from local graph")
    parser.add_argument("--stats", action="store_true",
                        help="Show graph statistics")
    parser.add_argument("--all", action="store_true",
                        help="Run init, enrich, and sync-anytype in sequence")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview changes without side effects")
    parser.add_argument("--refs-per-paper", type=int, default=20,
                        help="Max references to fetch per paper (default: 20)")
    parser.add_argument("--cited-by-per-paper", type=int, default=20,
                        help="Max cited-by to fetch per paper (default: 20)")
    parser.add_argument("--space-id", default=None,
                        help="AnyType space ID (defaults to env var)")
    args = parser.parse_args()

    if not any([args.init, args.enrich, args.sync_anytype, args.stats, args.all]):
        parser.print_help()
        sys.exit(1)

    graph = GraphStore()

    if args.all:
        args.init = True
        args.enrich = True
        args.sync_anytype = True

    if args.stats:
        show_stats(graph)
    if args.init:
        init_graph(graph, space_id=args.space_id)
    if args.enrich:
        enrich_graph(graph, refs_per_paper=args.refs_per_paper,
                     cited_by_per_paper=args.cited_by_per_paper)
    if args.sync_anytype:
        sync_anytype(graph, space_id=args.space_id, dry_run=args.dry_run)
    if args.stats and (args.init or args.enrich or args.sync_anytype):
        show_stats(graph)


if __name__ == "__main__":
    main()
