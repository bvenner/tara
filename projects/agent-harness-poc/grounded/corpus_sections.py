"""Corpus section-text access for claim-entailment judging (M2).

Resolves the hypergraph's `doc :: section` citations ('doc' ids like
`ret-tssi/program/research-program.md`) back to real files via
`corpus.json` root mapping, then extracts the cited section's text by
heading match. No LLM involved.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

THAR_DIR = Path(__file__).resolve().parents[3]
CORPUS_JSON = THAR_DIR / "projects" / "knowledge-repository-poc" / "corpus.json"


def corpus_roots(corpus_json: Path = CORPUS_JSON) -> dict[str, Path]:
    data = json.loads(corpus_json.read_text())
    return {r["name"]: THAR_DIR / r["dir"] for r in data["roots"]}


def doc_path(doc_id: str, roots: dict[str, Path] | None = None) -> Path | None:
    """`ret-tssi/program/research-program.md` -> actual project file, or None
    for docs outside mapped roots (external OpenAlex works)."""
    roots = roots if roots is not None else corpus_roots()
    parts = Path(doc_id).parts
    if parts and parts[0] in roots:
        candidate = roots[parts[0]].joinpath(*parts[1:])
        if candidate.exists():
            return candidate
    return None


def _norm(s: str) -> str:
    s = s.lower()
    s = re.sub(r"\s+", " ", s)
    s = s.replace("’", "'")
    # normalize numeric headings: "2.2 Rational..." ~ "2.2 Rational..."
    s = re.sub(r"(\d)\.(?=[\sA-Z])", r"\1", s)
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    return re.sub(r"\s+", " ", s)


_HEADING_RE = re.compile(r"^(#+)\s+(.*)$")


def section_text(doc_id: str, section: str, roots: dict[str, Path] | None = None) -> str | None:
    """Extract the cited section's source text (up to the next heading)."""
    path = doc_path(doc_id, roots)
    if path is None:
        return None
    lines = path.read_text(encoding="utf-8").splitlines()
    target = _norm(section)
    start = None
    level = None
    for i, line in enumerate(lines):
        m = _HEADING_RE.match(line)
        if not m:
            continue
        heading_text = _norm(m.group(2))
        if heading_text == target or heading_text.startswith(target) or target.startswith(heading_text[:40]):
            start, level = i, len(m.group(1))
            break
    if start is None:
        return None
    body: list[str] = []
    for line in lines[start + 1 :]:
        m = _HEADING_RE.match(line)
        if m and len(m.group(1)) <= level:
            break
        body.append(line)
    return "\n".join(body).strip()
