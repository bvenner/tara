"""M5: pipeline-internal `agent` morphism (OpenRouter GLM, config-knob only).

Offline checks: the .plumb survives the plumbing `check` binary's type and
config-interpolation validation. The live OpenRouter call is deliberately
NOT in the suite (network-shaped, non-deterministic, costs cents) — it is
behind tools.test_agent_pipeline_live, invoked manually with the key
exported; acceptance evidence lives in the thread notes.
"""
from pathlib import Path
import os
import subprocess
import textwrap

import pytest

POC = Path(__file__).resolve().parents[2] / "knowledge-repository-poc"
AGENT_SPEC = POC / "pipelines" / "agent.plumb"
PLUMB_CHECK = Path.home() / "tools/plumbing/_build/default/bin/check/main.exe"

requires = pytest.mark.skipif(
    not PLUMB_CHECK.exists(),
    reason="Nix-built plumbing check binary not present",
)


@requires
def test_agent_spec_exists():
    content = AGENT_SPEC.read_text()
    assert "provider: \"openai\"" in content
    assert "z-ai/glm-5.3-flash" in content
    assert "openrouter.ai/api/v1" in content
    assert "${OPENROUTER_API_KEY}" in content


@requires
def test_agent_spec_type_checks():
    """The `check` binary validates types AND every ${VAR} interpolation
    target — this doubles as a key-presence check with the key exported."""
    env = os.environ.copy()
    env.setdefault("OPENROUTER_API_KEY", "dummy-for-validation")
    p = subprocess.run([str(PLUMB_CHECK), str(AGENT_SPEC)],
                       capture_output=True, text=True, env=env, timeout=60)
    # Spec must pass validation. With a dummy key the *value* is wrong but
    # `check` only validates presence, so this is sound for the offline path.
    assert p.returncode == 0, textwrap.shorten(p.stderr or p.stdout, 400)


@requires
def test_agent_spec_rejects_missing_env_var():
    """Deleting the target var must fail validation (config contract)."""
    env = os.environ.copy()
    env.pop("OPENROUTER_API_KEY", None)
    p = subprocess.run([str(PLUMB_CHECK), str(AGENT_SPEC)],
                       capture_output=True, text=True, env=env, timeout=60)
    assert p.returncode != 0 and "OPENROUTER_API_KEY" in p.stderr + p.stdout


def test_pipeline_dotenv_loader(monkeypatch):
    """pipeline.py loads the gitignored .env into os.environ (existing env
    wins) so config-interpolated agents run through the standard runner."""
    import sys
    scripts = str(POC / "scripts")
    if scripts not in sys.path:
        sys.path.insert(0, scripts)
    import pipeline

    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    monkeypatch.setenv("TARA_TEST_ENV", "unset")
    pipeline.load_env_keys()
    if pipeline.ROOT.joinpath(".env").is_file():
        assert os.environ.get("OPENROUTER_API_KEY"), ".env key not loaded"
    # re-load must not clobber an existing env value
    monkeypatch.setenv("GOOGLE_API_KEY", "preset-wins")
    pipeline.load_env_keys()
    assert os.environ["GOOGLE_API_KEY"] == "preset-wins" or not pipeline.ROOT.joinpath(".env").is_file()
