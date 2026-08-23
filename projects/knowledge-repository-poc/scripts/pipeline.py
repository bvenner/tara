#!/usr/bin/env python3
"""Run a named plumbing pipeline via the nix-built runtime; print the payload.

Usage:
    python scripts/pipeline.py <name> '<json-input>'

Runs pipelines/<name>.plumb with cwd=pipelines/ and prints the decoded
first output value from stdout (runtime telemetry stays on stderr).

This is the opencode-side integration point: any agent that can run bash
can query the knowledge repository. It mirrors plumb-mcp's `call` tool
(source + input) without depending on the MCP server being loaded.
"""
import json
import subprocess
import sys
from pathlib import Path

POC = Path(__file__).resolve().parents[1]
PLUMB = "/home/brad/tools/plumbing"


def main():
    if len(sys.argv) < 3:
        print("usage: pipeline.py <name> '<json-input>'", file=sys.stderr)
        sys.exit(2)
    name, raw_input = sys.argv[1], sys.argv[2]
    if not name.endswith(".plumb"):
        name += ".plumb"
    cmd = ["nix", "develop", PLUMB, "-c",
           f"{PLUMB}/_build/default/bin/plumb/main.exe", name]
    proc = subprocess.run(cmd, input=raw_input + "\n",
                          capture_output=True, text=True, cwd=POC / "pipelines")
    if proc.returncode != 0:
        sys.stderr.write(proc.stderr)
        sys.exit(proc.returncode)
    payload = None
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            payload = json.loads(line)
            break
        except json.JSONDecodeError:
            continue
    if payload is None:
        sys.stderr.write(proc.stdout)
        sys.exit(1)
    print(json.dumps(payload, indent=2, default=str))


if __name__ == "__main__":
    main()