#!/usr/bin/env python3
"""TARA Phase 3 — Research Project Manager.

Creates and manages autoresearch workspaces linked to AnyType.

Usage:
    # Create a new research project
    python scripts/research_project.py create \
        "How do transformer attention patterns change with scale?" \
        --domain "mechanistic interpretability"

    # Sync existing project to AnyType
    python scripts/research_project.py sync ./my-research-project [--dry-run]

    # Show project status
    python scripts/research_project.py status ./my-research-project

    # List all projects in AnyType
    python scripts/research_project.py list
"""
import os
import sys
import argparse
import yaml
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional, Dict, Any, List

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

from anytype_client import create_object, search_objects, update_object, list_objects, SPACE_ID


# ── Configuration ────────────────────────────────────────────

DEFAULT_PROJECTS_DIR = Path.home() / "Documents" / "Research" / "projects"


def _projects_dir() -> Path:
    return DEFAULT_PROJECTS_DIR


def _slugify(text: str) -> str:
    """Convert question to directory-safe slug."""
    return "_".join(
        w.lower() for w in text.split() if w.isalnum() or w in "-_"
    )[:60]


def _resolve_space_id() -> str:
    sid = SPACE_ID
    if not sid:
        from anytype_client import list_spaces
        spaces = list_spaces()
        if spaces:
            sid = spaces[0]["id"]
    return sid


# ── Project creation ───────────────────────────────────────────

RESEARCH_STATE_TEMPLATE = """# Research State — Central Project Tracking
project:
  title: "{title}"
  question: "{question}"
  status: active
  started: "{started}"
  domain: "{domain}"

literature:
  key_papers: []
  open_problems: []
  evidence_gaps: []

hypotheses: []

experiments:
  proxy_metric: ""
  baseline_value: null
  best_value: null
  total_runs: 0
  trajectory: []

outer_loop:
  cycle: 0
  last_direction: null
  last_reflection: ""

workspace:
  findings: "findings.md"
  log: "research-log.md"
  literature_dir: "literature/"
  experiments_dir: "experiments/"
  to_human_dir: "to_human/"
  paper_dir: "paper/"
"""


FINDINGS_TEMPLATE = """# Current Understanding

(Research findings will accumulate here through outer-loop reflections.)

## What we know so far

## Patterns and Insights

## Lessons and Constraints

## Open Questions
"""


LOG_TEMPLATE = """# Research Log

| Date | Event | Notes |
|---|---|---|
| {started} | Project initialized | Question: {question} |
"""


def create_project(question: str, title: Optional[str] = None,
                   domain: str = "", dry_run: bool = False) -> Path:
    """Create a new autoresearch workspace and AnyType Project object."""
    projects_dir = _projects_dir()
    projects_dir.mkdir(parents=True, exist_ok=True)

    project_title = title or question
    slug = _slugify(question)
    project_dir = projects_dir / slug

    if project_dir.exists():
        print(f"ERROR: Project directory already exists: {project_dir}")
        sys.exit(1)

    started = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    # Create directory structure
    if not dry_run:
        project_dir.mkdir()
        (project_dir / "literature").mkdir()
        (project_dir / "experiments").mkdir()
        (project_dir / "to_human").mkdir()
        (project_dir / "paper").mkdir()

        # Write state files
        state_content = RESEARCH_STATE_TEMPLATE.format(
            title=project_title.replace('"', '\\"'),
            question=question.replace('"', '\\"'),
            started=started,
            domain=domain.replace('"', '\\"'),
        )
        (project_dir / "research-state.yaml").write_text(state_content)
        (project_dir / "findings.md").write_text(FINDINGS_TEMPLATE)
        (project_dir / "research-log.md").write_text(LOG_TEMPLATE.format(
            started=started, question=question
        ))

    # Create AnyType Project object
    space_id = _resolve_space_id()
    body = f"# {project_title}\n\n**Question:** {question}\n\n**Domain:** {domain}\n\n**Status:** active\n\n**Started:** {started}"

    if dry_run:
        print(f"[dry-run] Would create AnyType Project: {project_title}")
        print(f"[dry-run] Would create workspace: {project_dir}")
        return project_dir

    resp = create_object(
        name=f"Project: {project_title}",
        body=body,
        type_key="page",
        space_id=space_id,
    )
    project_id = resp.get("object", {}).get("id")
    if project_id:
        print(f"Created AnyType Project: {project_id}")
    else:
        print(f"WARNING: Failed to create AnyType Project")

    print(f"\n✅ Project created: {project_dir}")
    print(f"   AnyType: https://anytype.io/{project_id}")
    print(f"\nNext steps:")
    print(f"   1. cd {project_dir}")
    print(f"   2. Run research: /autoresearch {project_dir}")
    print(f"   3. Sync to AnyType: python scripts/research_project.py sync {project_dir}")
    return project_dir


# ── Project sync ──────────────────────────────────────────────

def sync_project(project_dir: str, dry_run: bool = False):
    """Delegate to sync_research_to_anytype script."""
    import subprocess
    cmd = [sys.executable, "scripts/sync_research_to_anytype.py", project_dir]
    if dry_run:
        cmd.append("--dry-run")
    result = subprocess.run(cmd, cwd=Path(__file__).parent.parent)
    sys.exit(result.returncode)


# ── Project status ────────────────────────────────────────────

def show_status(project_dir: str):
    project_path = Path(project_dir).expanduser().resolve()
    state_file = project_path / "research-state.yaml"

    if not state_file.exists():
        print(f"ERROR: Not a research project: {project_path}")
        sys.exit(1)

    with open(state_file) as f:
        state = yaml.safe_load(f)

    project = state.get("project", {})
    experiments = state.get("experiments", {})
    hypotheses = state.get("hypotheses", [])
    outer = state.get("outer_loop", {})

    print(f"\n{'='*50}")
    print(f"Project: {project.get('title', 'Untitled')}")
    print(f"{'='*50}")
    print(f"Question: {project.get('question', '')}")
    print(f"Status:   {project.get('status', 'unknown')}")
    print(f"Domain:   {project.get('domain', '')}")
    print(f"Started:  {project.get('started', '')}")
    print(f"\nHypotheses: {len(hypotheses)}")
    for h in hypotheses:
        print(f"  [{h.get('status', '?')}] {h.get('statement', '')[:50]}")
    print(f"\nExperiments: {experiments.get('total_runs', 0)} runs")
    print(f"  Best: {experiments.get('best_value', 'N/A')}")
    print(f"  Baseline: {experiments.get('baseline_value', 'N/A')}")
    print(f"\nOuter loop cycles: {outer.get('cycle', 0)}")
    print(f"Last direction: {outer.get('last_direction', 'none')}")
    print(f"{'='*50}\n")


# ── List projects ─────────────────────────────────────────────

def list_projects():
    """List Project objects in AnyType."""
    space_id = _resolve_space_id()
    print("\nResearch Projects in AnyType:")
    print("-" * 50)
    offset = 0
    limit = 50
    count = 0
    while True:
        objs = list_objects(space_id=space_id, limit=limit, offset=offset)
        if not objs:
            break
        for obj in objs:
            name = obj.get("name", "")
            if name.startswith("Project:"):
                print(f"  {name.replace('Project: ', '')}")
                print(f"    ID: {obj['id']}")
                print(f"    URL: https://anytype.io/{obj['id']}")
                count += 1
        offset += limit
        if len(objs) < limit:
            break
    print(f"\nTotal: {count} project(s)")


# ── Main ──────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="TARA Research Project Manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # create
    create_parser = subparsers.add_parser("create", help="Create a new research project")
    create_parser.add_argument("question", help="Research question")
    create_parser.add_argument("--title", help="Project title (defaults to question)")
    create_parser.add_argument("--domain", default="", help="Research domain")
    create_parser.add_argument("--dry-run", action="store_true")

    # sync
    sync_parser = subparsers.add_parser("sync", help="Sync project to AnyType")
    sync_parser.add_argument("project_dir", help="Path to project directory")
    sync_parser.add_argument("--dry-run", action="store_true")

    # status
    status_parser = subparsers.add_parser("status", help="Show project status")
    status_parser.add_argument("project_dir", help="Path to project directory")

    # list
    subparsers.add_parser("list", help="List all projects in AnyType")

    args = parser.parse_args()

    if args.command == "create":
        create_project(args.question, title=args.title, domain=args.domain,
                        dry_run=args.dry_run)
    elif args.command == "sync":
        sync_project(args.project_dir, dry_run=args.dry_run)
    elif args.command == "status":
        show_status(args.project_dir)
    elif args.command == "list":
        list_projects()


if __name__ == "__main__":
    main()
