"""Citation-support check for a grounded-answer run (mechanical, LLM-free).

Rebuilds the anchor universe from the run's tool-output sidecar (recorded by
`run_grounded.py`). For every tool return: structured outputs contribute
(doc, section) pairs (trace hits, query edges) and markdown bundles contribute
`### doc :: section` headings. Each `Claim` line in the run file must anchor
to one of those (doc, section) pairs.

Usage:
    uv run python projects/agent-harness-poc/evals/check_citations.py <run.md>

Exit 0 = every claim supported; 1 = unsupported claims; 2 = input problem.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

HEADING_RE = re.compile(r"^### (.+?) :: (.+?)$", re.MULTILINE)
CLAIM_RE = re.compile(r"^- (.+?) :: (.+?): (.*)$")


def _as_text(content: Any) -> str:
    """Tool markdown arrives as a JSON-quoted string (pipeline.py output)."""
    if not isinstance(content, str):
        return ""
    try:
        unwrapped = json.loads(content)
        return unwrapped if isinstance(unwrapped, str) else content
    except json.JSONDecodeError:
        return content


def anchors_from_sidecar(sidecar: Path) -> set[tuple[str, str]]:
    anchors: set[tuple[str, str]] = set()
    for rec in json.loads(sidecar.read_text()):
        content = rec["content"]
        if isinstance(content, dict):
            for hit in content.get("hits", []):
                anchors.add((hit["doc"], hit["section"]))
            for edge in content.get("edges", []):
                anchors.add((edge["doc"], edge["section"]))
        text = _as_text(content)
        for m in HEADING_RE.finditer(text):
            anchors.add((m.group(1), m.group(2)))
    return anchors


def supported(claim_source: str, anchors: set[tuple[str, str]]) -> bool:
    doc, _, section = claim_source.partition(" :: ")
    section = section.strip()
    for a_doc, a_section in anchors:
        if a_doc != doc:
            continue
        # exact, prefix, or shared-prefix (agent may truncate the section title)
        if (
            a_section == section
            or a_section.startswith(section)
            or section.startswith(a_section[:60])
        ):
            return True
    return False


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_citations.py <run.md>")
        return 2
    run_file = Path(sys.argv[1])
    sidecar = run_file.with_suffix(".tools.json")
    if not run_file.exists() or not sidecar.exists():
        print(f"missing {run_file} or {sidecar}")
        return 2
    anchors = anchors_from_sidecar(sidecar)
    ok = bad = 0
    for line in run_file.read_text().splitlines():
        if not line.startswith("- "):
            continue
        m = CLAIM_RE.match(line)
        if not m:
            continue
        source = f"{m.group(1)} :: {m.group(2)}"
        if supported(source, anchors):
            ok += 1
        else:
            bad += 1
            print(f"UNSUPPORTED: {source}")
    print(f"anchor universe: {len(anchors)} (doc, section) pairs")
    print(f"citation support: {ok}/{ok + bad}")
    return 0 if ok > 0 and bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
