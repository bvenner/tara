#!/usr/bin/env bash
# Wrapper script for AnyType MCP server
# Ensures Node.js is in PATH before running the MCP server binary

# Load API key from .env if it exists
if [ -f "$(dirname "$0")/.env" ]; then
  set -a
  source "$(dirname "$0")/.env"
  set +a
fi

export PATH="/nix/store/6x6v11xjf0psckgqmyhfyhw9bdma0rn6-nodejs-22.22.2/bin:$PATH"
export ANYTYPE_API_BASE_URL="${ANYTYPE_API_BASE_URL:-http://127.0.0.1:31012}"
export OPENAPI_MCP_HEADERS="{\"Authorization\":\"Bearer ${ANYTYPE_API_KEY}\", \"Anytype-Version\":\"2025-11-08\"}"

exec /home/brad/Documents/Research/node_modules/.bin/anytype-mcp "$@"
