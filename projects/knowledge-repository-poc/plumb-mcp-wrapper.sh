#!/usr/bin/env bash
# MCP bridge for the knowledge-repository plumbing pipelines.
# Runs the nix-built plumb-mcp with cwd = pipelines/ so `exec` relative
# paths (../scripts/...) resolve regardless of how opencode launches it.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
PLUMB=/home/brad/tools/plumbing
cd "$ROOT/pipelines"
exec nix develop "$PLUMB" -c "$PLUMB/_build/default/bin/mcp/main.exe" --docroot "$ROOT/pipelines"