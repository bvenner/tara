#!/usr/bin/env python3
"""CI/local smoke for the knowledge-repository Python stack (Job 1).

Runs the cheap, deterministic worker-contract checks over the committed
artifacts — the "does it turn on" layer. Deliberately does NOT load docling
models, expand the whole corpus, or run the nix plumbing runtime (that's the
heavier manual/Job-2 territory). Run from anywhere:

    uv run python projects/knowledge-repository-poc/scripts/smoke.py

Exit 0 iff every check passes; each failure names the broken contract.
"""
import json
import subprocess
import sys
from pathlib import Path

POC = Path(__file__).resolve().parents[1]
ROOT = POC.parents[1]
SHIM = POC / "bin" / "tara-python"
PYTHON = [str(SHIM)]
WORKERS = POC / "scripts"

# schemas must be importable for the shape assertions below
sys.path.insert(0, str(POC / "scripts"))
import schemas  # noqa: E402

FAILED = []


def worker(name: str) -> list[str]:
    """argv prefix pointing a shim at a worker script (resolve relative to POC)."""
    return [str(SHIM), str(WORKERS / name)]


def check(name: str, fn) -> None:
    try:
        fn()
        print(f"ok      {name}")
    except Exception as e:  # noqa: BLE001
        FAILED.append(name)
        print(f"FAIL    {name}: {e}")


def run(py_args: list[str], req, timeout: int = 180) -> dict | str:
    """Run a worker via the shim and return the parsed stdout payload."""
    p = subprocess.run(py_args, input=json.dumps(req),
                       capture_output=True, text=True, timeout=timeout)
    if p.returncode != 0:
        raise RuntimeError(f"worker exited {p.returncode}: "
                           f"{p.stderr.strip().splitlines()[-1]}")
    lines = [l for l in p.stdout.splitlines() if l.strip()]
    if not lines:
        raise RuntimeError("worker produced no stdout")
    try:
        return json.loads(lines[-1])
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"non-JSON stdout: {lines[-1][:200]}") from exc


def expect_validation_error(py_args: list[str], req) -> None:
    p = subprocess.run(py_args, input=json.dumps(req),
                       capture_output=True, text=True, timeout=60)
    if p.returncode == 0:
        raise RuntimeError("expected a validation failure, got exit 0")
    if "ValidationError" not in p.stderr and "Input should" not in p.stderr:
        raise RuntimeError(f"unexpected failure mode: {p.stderr[-300:]}")


# ── 0. stack boot ─────────────────────────────────────────────────

def imports_ok():
    import pydantic  # noqa: F401
    import requests  # noqa: F401
    import docling  # noqa: F401
    import torch  # noqa: F401


# ── 1. worker contracts (one smoke per contract) ───────────────────

def query_contract():
    out = run(worker("graph_query.py") + ["--mode", "json"],
              {"concept": "Cattaneo"})
    schemas.QueryResult.model_validate(out)
    if not out["edges"]:
        raise RuntimeError("query returned no hyperedges")


def evidence_contract():
    out = run(worker("graph_query.py") + ["--mode", "text"],
              {"concept": "Cattaneo", "max_edges": 3})
    if not isinstance(out, str) or len(out) < 50:
        raise RuntimeError("evidence bundle not a substantial string")


def trace_contract():
    out = run(worker("graph_query.py") + ["--mode", "trace"],
              {"topic": "island digital twin",
               "concepts": ["island", "digital twin", "metabolism"],
               "min_seeds": 1})
    schemas.TraceResult.model_validate(out)
    if not out["hits"]:
        raise RuntimeError("trace returned no hits")


def trace_report_contract():
    out = run(worker("graph_query.py") + ["--mode", "trace-text"],
              {"topic": "island digital twin",
               "concepts": ["island", "digital twin", "metabolism"],
               "min_seeds": 1})
    if not isinstance(out, str) or "# Evidence trace" not in out:
        raise RuntimeError("trace-report not a markdown trace")


def expand_contract():
    out = run(worker("expand_openalex.py"),
              {"mode": "doi", "topic": "", "limit": 5,
               "doi": "10.3390/en17225541"})
    schemas.ExpandSummary.model_validate(out)
    if out["matched"] != 1:
        raise RuntimeError(f"expected 1 OpenAlex match, got {out['matched']}")


def fulltext_contract():
    out = run(worker("fetch_fulltext.py"),
              {"mode": "doi", "doi": "10.1103/physreve.96.042143",
               "limit": 0, "refresh": 0, "strict": 1})
    schemas.FulltextSummary.model_validate(out)
    if out["converted"] != 0:
        raise RuntimeError("fulltext smoke should take the skip path "
                           "(already converted)")


def ingest_contract():
    out = run(worker("build_hypergraph.py") + ["--compact"], None)
    schemas.IngestSummary.model_validate(out)
    if out["docs"] < 1:
        raise RuntimeError("ingest summary has no docs")


# ── 2. rejection paths (validation must reject) ───────────────────

def reject_empty_concept():
    expect_validation_error(worker("graph_query.py") + ["--mode", "json"],
                            {"concept": ""})


def reject_negative_limit():
    expect_validation_error(worker("expand_openalex.py"),
                            {"mode": "topic", "topic": "x", "limit": -5,
                             "doi": "", "arxiv_id": ""})


def reject_empty_concepts():
    expect_validation_error(worker("graph_query.py") + ["--mode", "trace"],
                            {"topic": "t", "concepts": [], "min_seeds": 1})


# ── 3. determinism (build twice, byte-identical) ──────────────────

def determinism():
    hg = POC / "graph" / "hypergraph.json"
    first = subprocess.run(worker("build_hypergraph.py") + ["--force"],
                           capture_output=True, text=True, timeout=300)
    if first.returncode != 0:
        raise RuntimeError(f"first build failed: {first.stderr[-300:]}")
    sha_before = _sha256(hg)
    again = subprocess.run(worker("build_hypergraph.py") + ["--force"],
                           capture_output=True, text=True, timeout=300)
    if again.returncode != 0:
        raise RuntimeError(f"second build failed: {again.stderr[-300:]}")
    sha_after = _sha256(hg)
    if sha_before != sha_after:
        raise RuntimeError("hypergraph.json changed across identical builds")


def _sha256(p: Path) -> str:
    import hashlib
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    print("TARA stack smoke (Job 1)")
    checks = [
        ("imports (pydantic/requests/docling/torch)", imports_ok),
        ("query contract (QueryResult)", query_contract),
        ("evidence contract (markdown)", evidence_contract),
        ("trace contract (TraceResult)", trace_contract),
        ("trace-report contract (markdown)", trace_report_contract),
        ("expand contract (ExpandSummary)", expand_contract),
        ("fulltext contract (FulltextSummary, skip path)", fulltext_contract),
        ("ingest contract (IngestSummary)", ingest_contract),
        ("reject empty concept", reject_empty_concept),
        ("reject negative limit", reject_negative_limit),
        ("reject empty concepts", reject_empty_concepts),
        ("build determinism", determinism),
    ]
    for name, fn in checks:
        check(name, fn)
    print()
    if FAILED:
        print(f"{len(FAILED)} check(s) failed: {', '.join(FAILED)}")
        sys.exit(1)
    print("all checks passed")


if __name__ == "__main__":
    main()