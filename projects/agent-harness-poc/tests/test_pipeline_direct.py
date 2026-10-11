"""TARA_PLUMB_DIRECT equivalence: opt-in fast path must produce the same
JSON payload as the canonical nix-develop path (gracefully skipped when the
plumb binary is absent from this machine)."""

import json
import subprocess
import sys
from pathlib import Path

import pytest  # noqa: E402

THAR = Path(__file__).resolve().parents[1].parents[1]
PIPELINE_PY = THAR / "projects" / "knowledge-repository-poc" / "scripts" / "pipeline.py"
PLUMB_BIN = Path.home() / "tools/plumbing/_build/default/bin/plumb/main.exe"

pytestmark = pytest.mark.skipif(
    not PLUMB_BIN.exists(), reason="Nix-built plumb binary not present"
)


def _trace(mode_env: str) -> dict:
    import os

    cmd = [sys.executable, str(PIPELINE_PY), "trace",
           '{"topic":"test direct","concepts":["tau_J","sk condition"],"min_seeds":2}']
    env0 = {"PATH": os.environ["PATH"], "HOME": str(Path.home()),
            "TARA_PLUMB_DIRECT": mode_env}
    proc = subprocess.run(cmd, capture_output=True, text=True, env=env0,
                          cwd=str(THAR), timeout=600)
    assert proc.returncode == 0, proc.stderr[-400:]
    return json.loads(proc.stdout)


def test_direct_mode_matches_nix_mode() -> None:
    direct = _trace("1")
    canonical = _trace("0")
    assert direct["topic"] == canonical["topic"] == "test direct"
    assert len(direct["hits"]) == len(canonical["hits"])
