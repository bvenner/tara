"""Typed tool wrappers over the knowledge-repository plumbing pipelines.

This is the M1 "tool bridge": each function mirrors one `.plumb` pipeline via
`scripts/pipeline.py` (nix-built `plumb`, cwd=pipelines/), validates the
boundary with the canonical worker contracts in
`knowledge-repository-poc/scripts/schemas.py`, and returns a pydantic model.
No LLM is involved at this layer.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import os
from pathlib import Path

from pydantic import BaseModel, Field

THAR_DIR = Path(__file__).resolve().parents[3]
POC = THAR_DIR / "projects" / "knowledge-repository-poc"
PIPELINE_PY = POC / "scripts" / "pipeline.py"
# F2 memoization: pipeline calls are content-addressed on (name, input, graph
# build hash); the knowledge repo is deterministic in those, so a cached
# stdout is semantically identical to a fresh nix-develop spawn. Bypass with
# TARA_NO_PIPELINE_CACHE=1.
PIPELINE_CACHE = THAR_DIR / "projects" / "agent-harness-poc" / ".cache" / "pipelines"


def _graph_hash() -> str:
    build_meta = POC / "graph" / "build_meta.json"
    if build_meta.exists():
        return hashlib.sha1(build_meta.read_bytes()).hexdigest()[:12]
    return "nograph"


def _cache_key(name: str, raw_json: str) -> str:
    raw = f"{name}|{raw_json}|{_graph_hash()}"
    return hashlib.sha1(raw.encode()).hexdigest()


def _call(name: str, raw_json: str) -> str:
    cache_dir = PIPELINE_CACHE
    cache_file = cache_dir / f"{name}-{_cache_key(name, raw_json)}.out"
    if os.environ.get("TARA_NO_PIPELINE_CACHE") != "1" and cache_file.exists():
        return cache_file.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(PIPELINE_PY), name, raw_json],
        capture_output=True,
        text=True,
        timeout=600,
        cwd=str(THAR_DIR),
    )
    if proc.returncode != 0:
        raise RuntimeError(f"pipeline {name} failed:\n{proc.stderr}")
    if not proc.stdout.strip():
        raise RuntimeError(f"pipeline {name} returned nothing")
    if os.environ.get("TARA_NO_PIPELINE_CACHE") != "1":
        cache_dir.mkdir(parents=True, exist_ok=True)
        cache_file.write_text(proc.stdout, encoding="utf-8")
    return proc.stdout

sys.path.insert(0, str(POC / "scripts"))
import schemas as worker  # noqa: E402  (canonical boundary contracts)


class TraceReportRequest(BaseModel):
    """Input type of trace_report.plumb ({topic, concepts, min_seeds})."""

    topic: str
    concepts: list[str] = Field(min_length=1)
    min_seeds: int = Field(2, ge=1)


class TraceInput(BaseModel):
    """Exact input type of trace.plumb (schemas.TraceRequest's max_edges
    default would add a fatal extra key at the exec boundary)."""

    topic: str
    concepts: list[str] = Field(min_length=1)
    min_seeds: int = Field(2, ge=1)


class QueryInput(BaseModel):
    """Exact input type of query.plumb ({concept} — no max_edges)."""

    concept: str = Field(min_length=1)


def _call(name: str, raw_json: str) -> str:
    proc = subprocess.run(
        [sys.executable, str(PIPELINE_PY), name, raw_json],
        capture_output=True,
        text=True,
        timeout=600,
        cwd=str(THAR_DIR),
    )
    if proc.returncode != 0:
        raise RuntimeError(f"pipeline {name} failed:\n{proc.stderr}")
    if not proc.stdout.strip():
        raise RuntimeError(f"pipeline {name} returned nothing")
    return proc.stdout


def _call_model(name: str, req: BaseModel, out: type[BaseModel]) -> BaseModel:
    payload = _call(name, req.model_dump_json())
    try:
        decoded = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"pipeline {name}: invalid JSON: {payload[:200]}") from exc
    return out.model_validate(decoded)


def knowledge_trace(
    topic: str, concepts: list[str], min_seeds: int = 3
) -> worker.TraceResult:
    """Find hyperedges where at least `min_seeds` of the seed concepts co-occur.

    The core grounding operation for a reasoning question: pick 2-5 seed
    concepts from the question, then read the returned hits' `doc` and
    `section` fields as the citation anchors.
    """
    req = TraceInput(topic=topic, concepts=concepts, min_seeds=min_seeds)
    out: worker.TraceResult = _call_model(
        "trace", req, worker.TraceResult  # type: ignore[arg-type]
    )
    return out


def knowledge_query(concept: str, max_edges: int = 50) -> worker.QueryResult:
    """Query the hypergraph for one concept: matched nodes + hyperedges with doc/section provenance."""
    # query.plumb takes {concept} only (exact-typed boundary).
    req = QueryInput(concept=concept)
    return _call_model("query", req, worker.QueryResult)  # type: ignore[arg-type]


def knowledge_evidence(concept: str, max_edges: int = 20) -> str:
    """Render an evidence bundle (markdown) for one concept.

    Arguable alternative to `knowledge_query` when all that is needed is a
    readable citation bundle for a single concept.
    """
    req = worker.QueryRequest(concept=concept, max_edges=max_edges)
    return _call("evidence", req.model_dump_json())


def knowledge_trace_report(topic: str, concepts: list[str], min_seeds: int = 3) -> str:
    """Human-readable evidence trace (markdown) for a reasoning question.

    Same intersection semantics as `knowledge_trace` with the results rendered
    as a markdown bundle: use it to re-check a trace in readable form before
    composing the final answer.
    """
    req = TraceReportRequest(topic=topic, concepts=concepts, min_seeds=min_seeds)
    return _call("trace_report", req.model_dump_json())
