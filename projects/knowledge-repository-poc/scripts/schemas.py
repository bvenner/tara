"""Pydantic schemas for the JSON-Lines worker contracts.

Every `exec` worker in `pipelines/*.plumb` reads one JSON value per stdin line
and emits one JSON value per line. These models are the canonical boundary:
requests are validated on entry (a clear ValidationError instead of a silent
morphism_fatal or undefined-behaviour downstream), and summaries are validated
before emit. Keep the field names/shapes in lockstep with the `.plumb` type
annotations — the plumbing runtime enforces the same shapes, this module is the
Python-side mirror.
"""
from typing import List, Optional

from pydantic import BaseModel, Field


# ── expand.plumb ──────────────────────────────────────────────────

class ExpandRequest(BaseModel):
    mode: str = "topic"
    topic: str = ""
    limit: int = Field(5, ge=0, le=1000)
    doi: str = ""  # also carries arxiv_id via mode="arxiv"
    arxiv_id: str = ""


class ExpandSummary(BaseModel):
    mode: str
    matched: int = Field(ge=0)
    written: int = Field(ge=0)
    skipped: int = Field(ge=0)


# ── fulltext.plumb ───────────────────────────────────────────────

class FulltextRequest(BaseModel):
    mode: str = "corpus"
    doi: str = ""
    limit: int = Field(0, ge=0)
    refresh: int = Field(0, ge=0, le=1)
    strict: int = Field(1, ge=0, le=1)


class FulltextSummary(BaseModel):
    mode: str
    found: int = Field(ge=0)
    downloaded: int = Field(ge=0)
    converted: int = Field(ge=0)
    skipped: int = Field(ge=0)
    reasons: str = ""


# ── query/evidence.plumb (graph_query.py) ────────────────────────

class QueryRequest(BaseModel):
    concept: str = Field(min_length=1)
    max_edges: int = Field(50, ge=1, le=500)


class NodeRef(BaseModel):
    node_id: str
    label: str
    kind: str


class Edge(BaseModel):
    edge_id: str
    arity: int = Field(ge=0)
    doc: str
    section: str
    nodes: List[str]


class QueryResult(BaseModel):
    concept: str
    matched_nodes: List[NodeRef]
    total_edges: int = Field(ge=0)
    edges: List[Edge]


# ── trace/trace_report.plumb (graph_query.py) ────────────────────

class TraceRequest(BaseModel):
    topic: str = ""
    concepts: List[str] = Field(min_length=1)
    min_seeds: int = Field(2, ge=1)
    max_edges: int = Field(40, ge=1, le=500)


class Seed(BaseModel):
    concept: str
    matched_nodes: List[str]


class Hit(BaseModel):
    edge_id: str
    doc: str
    section: str
    arity: int = Field(ge=0)
    seeds: List[str]
    nodes: List[str]


class TraceResult(BaseModel):
    topic: str
    min_seeds: int = Field(ge=1)
    seeds: List[Seed]
    hits: List[Hit]
    distinct_sections: int = Field(ge=0)


# ── ingest.plumb (build_hypergraph.py --compact) ─────────────────

class IngestSummary(BaseModel):
    docs: int = Field(ge=0)
    nodes: int = Field(ge=0)
    edges: int = Field(ge=0)
    mean_degree: float = Field(ge=0)
    max_degree: int = Field(ge=0)


def apply(model: type[BaseModel]):
    """Decorator: parse+validate stdin JSON lines, pass model instances to fn.

    Mirrors the `exec` boundary: one request per line, one summary per line
    (validated again before print, so a bad summary fails loudly and locally).
    """
    def deco(fn):
        def wrapper():
            import json as _json
            import sys as _sys
            for line in _sys.stdin:
                line = line.strip()
                if not line:
                    continue
                req = model.model_validate(_json.loads(line))
                out = fn(req)
                print(out.model_dump_json())
                _sys.stdout.flush()
        return wrapper
    return deco