#!/usr/bin/env python3
"""TARA Phase 3 — Sync autoresearch workspace to AnyType.

Reads a research project directory (created by autoresearch skill) and
synchronizes its state into AnyType objects:
  - Project (page object with structured body)
  - Paper objects from literature/ summaries
  - Experiment objects from experiments/
  - Findings appended to Project body

Usage:
    python scripts/sync_research_to_anytype.py /path/to/research-project [--dry-run]
"""
import os
import sys
import argparse
import yaml
from pathlib import Path
from typing import Optional, Dict, List, Any

# Load .env
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

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))

from anytype_client import (
    create_object,
    search_objects,
    update_object,
    list_objects,
    SPACE_ID,
)
from graph_store import GraphStore
import openalex_client


def _resolve_space_id() -> str:
    sid = SPACE_ID
    if not sid:
        from anytype_client import list_spaces
        spaces = list_spaces()
        if spaces:
            sid = spaces[0]["id"]
    return sid


def load_research_state(project_dir: Path) -> Optional[Dict[str, Any]]:
    state_file = project_dir / "research-state.yaml"
    if not state_file.exists():
        return None
    with open(state_file) as f:
        return yaml.safe_load(f)


def find_or_create_project(title: str, body: str, space_id: str, dry_run: bool = False) -> str:
    """Find existing Project by title or create new. Returns object ID."""
    query = f"Project: {title}"
    results = search_objects(query, limit=10)
    for obj in results:
        if obj.get("name") == query:
            print(f"  Found existing Project: {obj['id']}")
            if not dry_run:
                update_object(obj["id"], body=body, space_id=space_id)
            return obj["id"]
    if dry_run:
        print(f"  [dry-run] Would create Project: {query}")
        return "<dry-run-project-id>"
    resp = create_object(name=query, body=body, type_key="page", space_id=space_id)
    oid = resp.get("object", {}).get("id")
    print(f"  Created Project: {oid}")
    return oid


def sync_literature(project_dir: Path, project_id: str, space_id: str,
                    graph: GraphStore, dry_run: bool = False) -> List[str]:
    """Sync papers from literature/ to AnyType. Returns list of Paper object IDs."""
    lit_dir = project_dir / "literature"
    if not lit_dir.exists():
        return []

    paper_ids = []
    for paper_file in sorted(lit_dir.glob("*.md")):
        if paper_file.name == "survey.md":
            continue  # Skip the aggregate survey
        content = paper_file.read_text()
        # Extract title from first H1 or filename
        title = paper_file.stem.replace("-", " ").replace("_", " ")
        for line in content.split("\n"):
            if line.startswith("# "):
                title = line[2:].strip()
                break

        # Look for DOI/arXiv in content
        doi = ""
        arxiv_id = ""
        year = 0
        for line in content.split("\n"):
            if line.lower().startswith("doi:"):
                doi = line.split(":", 1)[1].strip()
            if line.lower().startswith("arxiv:") or line.lower().startswith("arXiv ID:"):
                arxiv_id = line.split(":", 1)[1].strip()
            if line.lower().startswith("year:"):
                try:
                    year = int(line.split(":", 1)[1].strip())
                except ValueError:
                    pass

        # Check if paper already exists in graph or AnyType
        existing = None
        if doi:
            results = search_objects(doi, limit=5)
            for obj in results:
                if obj.get("name", "").startswith("Paper:"):
                    existing = obj["id"]
                    break
        if not existing and arxiv_id:
            results = search_objects(f"arXiv: {arxiv_id}", limit=5)
            for obj in results:
                if obj.get("name", "").startswith("Paper:"):
                    existing = obj["id"]
                    break
        if not existing and title:
            results = search_objects(title, limit=5)
            for obj in results:
                if obj.get("name", "").replace("Paper: ", "") == title:
                    existing = obj["id"]
                    break

        if existing:
            print(f"  Link existing Paper: {title[:60]}")
            paper_ids.append(existing)
            continue

        # Try OpenAlex enrichment if we have identifiers
        oa_data = {}
        if doi:
            raw = openalex_client.get_work_by_doi(doi)
            if raw:
                oa_data = openalex_client.normalize_work(raw)
        elif arxiv_id:
            raw = openalex_client.get_work_by_arxiv(arxiv_id)
            if raw:
                oa_data = openalex_client.normalize_work(raw)

        paper_body = f"# {title}\n\n{content}"
        if dry_run:
            print(f"  [dry-run] Would create Paper: {title[:60]}")
            paper_ids.append(f"<dry-run-{paper_file.stem}>")
            continue

        resp = create_object(
            name=f"Paper: {title}",
            body=paper_body,
            type_key="page",
            space_id=space_id,
        )
        pid = resp.get("object", {}).get("id")
        if pid:
            print(f"  Created Paper: {title[:60]} ({pid})")
            paper_ids.append(pid)
            # Add to local graph
            graph.add_paper({
                "title": title,
                "doi": doi,
                "arxiv_id": arxiv_id,
                "year": year,
                "abstract": content[:2000],
                "anytype_id": pid,
            })
        else:
            print(f"  WARNING: Failed to create Paper: {title[:60]}")
    return paper_ids


def sync_experiments(project_dir: Path, project_id: str, space_id: str,
                     dry_run: bool = False) -> List[str]:
    """Sync experiments from experiments/ to AnyType. Returns list of Experiment IDs."""
    exp_dir = project_dir / "experiments"
    if not exp_dir.exists():
        return []

    exp_ids = []
    for subdir in sorted(exp_dir.iterdir()):
        if not subdir.is_dir():
            continue
        protocol_file = subdir / "protocol.md"
        analysis_file = subdir / "results" / "analysis.md"

        hypothesis_name = subdir.name.replace("-", " ").replace("_", " ")
        body_lines = [f"# Experiment: {hypothesis_name}", ""]

        if protocol_file.exists():
            body_lines.append("## Protocol")
            body_lines.append(protocol_file.read_text()[:3000])
            body_lines.append("")

        if analysis_file.exists():
            body_lines.append("## Analysis")
            body_lines.append(analysis_file.read_text()[:3000])
            body_lines.append("")

        body = "\n".join(body_lines)

        # Check if experiment already exists
        existing = None
        results = search_objects(hypothesis_name, limit=5)
        for obj in results:
            if obj.get("name", "").startswith("Experiment:"):
                existing = obj["id"]
                break

        if existing:
            print(f"  Link existing Experiment: {hypothesis_name[:60]}")
            if not dry_run:
                update_object(existing, body=body, space_id=space_id)
            exp_ids.append(existing)
            continue

        if dry_run:
            print(f"  [dry-run] Would create Experiment: {hypothesis_name[:60]}")
            exp_ids.append(f"<dry-run-{subdir.name}>")
            continue

        resp = create_object(
            name=f"Experiment: {hypothesis_name}",
            body=body,
            type_key="page",
            space_id=space_id,
        )
        eid = resp.get("object", {}).get("id")
        if eid:
            print(f"  Created Experiment: {hypothesis_name[:60]} ({eid})")
            exp_ids.append(eid)
        else:
            print(f"  WARNING: Failed to create Experiment: {hypothesis_name[:60]}")
    return exp_ids


def build_project_body(state: Dict[str, Any], findings_text: str) -> str:
    """Build Markdown body for the Project object."""
    project = state.get("project", {})
    lines = [
        f"# {project.get('title', 'Untitled Project')}",
        "",
        f"**Research Question:** {project.get('question', '')}",
        f"**Status:** {project.get('status', 'active')}",
        f"**Domain:** {project.get('domain', '')}",
        f"**Started:** {project.get('started', '')}",
        "",
    ]

    # Hypotheses summary
    hypotheses = state.get("hypotheses", [])
    if hypotheses:
        lines.append("## Hypotheses")
        for h in hypotheses:
            status = h.get("status", "pending")
            stmt = h.get("statement", "")
            lines.append(f"- [{status.upper()}] {stmt}")
        lines.append("")

    # Experiment summary
    experiments = state.get("experiments", {})
    if experiments:
        lines.append("## Experiments")
        lines.append(f"- Total runs: {experiments.get('total_runs', 0)}")
        lines.append(f"- Proxy metric: {experiments.get('proxy_metric', '')}")
        best = experiments.get("best_value")
        baseline = experiments.get("baseline_value")
        if best is not None:
            lines.append(f"- Best value: {best}")
        if baseline is not None:
            lines.append(f"- Baseline: {baseline}")
        lines.append("")

    # Outer loop
    outer = state.get("outer_loop", {})
    if outer:
        lines.append("## Outer Loop")
        lines.append(f"- Cycles: {outer.get('cycle', 0)}")
        lines.append(f"- Last direction: {outer.get('last_direction', 'none')}")
        last = outer.get("last_reflection", "")
        if last:
            lines.append(f"- Last reflection: {last}")
        lines.append("")

    # Findings
    if findings_text:
        lines.append("## Findings")
        lines.append(findings_text[:5000])
        lines.append("")

    # Literature summary
    lit = state.get("literature", {})
    key_papers = lit.get("key_papers", [])
    if key_papers:
        lines.append("## Key Papers")
        for paper in key_papers:
            lines.append(f"- {paper.get('title', '')} ({paper.get('authors', '')}, {paper.get('year', '')})")
        lines.append("")

    return "\n".join(lines)


def sync_project(project_dir: str, dry_run: bool = False):
    project_path = Path(project_dir).expanduser().resolve()
    if not project_path.exists():
        print(f"ERROR: Project directory not found: {project_path}")
        sys.exit(1)

    state = load_research_state(project_path)
    if not state:
        print(f"ERROR: No research-state.yaml found in {project_path}")
        print("Is this an autoresearch workspace?")
        sys.exit(1)

    space_id = _resolve_space_id()
    graph = GraphStore()

    prefix = "[dry-run] " if dry_run else ""
    print(f"{prefix}Syncing project: {project_path}")
    print(f"  Title: {state.get('project', {}).get('title', 'Untitled')}")
    print(f"  Status: {state.get('project', {}).get('status', 'unknown')}")

    # Read findings
    findings_path = project_path / "findings.md"
    findings_text = findings_path.read_text() if findings_path.exists() else ""

    # Build project body
    body = build_project_body(state, findings_text)

    # Create/update Project object
    print("\n1. Project object...")
    project_title = state.get("project", {}).get("title", "Untitled Project")
    project_id = find_or_create_project(project_title, body, space_id, dry_run=dry_run)

    # Sync literature
    print("\n2. Literature papers...")
    paper_ids = sync_literature(project_path, project_id, space_id, graph, dry_run=dry_run)
    print(f"   Linked {len(paper_ids)} paper(s)")

    # Sync experiments
    print("\n3. Experiments...")
    exp_ids = sync_experiments(project_path, project_id, space_id, dry_run=dry_run)
    print(f"   Linked {len(exp_ids)} experiment(s)")

    # Summary
    print(f"\n{'='*50}")
    print(f"✅ {prefix}Sync complete")
    print(f"   Project:  {project_id}")
    print(f"   Papers:   {len(paper_ids)}")
    print(f"   Experiments: {len(exp_ids)}")
    if not dry_run:
        print(f"   URL: https://anytype.io/{project_id}")
    print(f"{'='*50}")


def main():
    parser = argparse.ArgumentParser(description="Sync autoresearch workspace to AnyType")
    parser.add_argument("project_dir", help="Path to autoresearch project directory")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview without creating AnyType objects")
    args = parser.parse_args()
    sync_project(args.project_dir, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
