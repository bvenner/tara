#!/usr/bin/env bash
# Wrapper script for AnyType MCP server
# Environment variables (ANYTYPE_API_KEY, etc.) are loaded by direnv from .enc.env
# See: .envrc for load_encrypted_env() function

export PATH="/nix/store/6x6v11xjf0psckgqmyhfyhw9bdma0rn6-nodejs-22.22.2/bin:$PATH"
export ANYTYPE_API_BASE_URL="${ANYTYPE_API_BASE_URL:-http://127.0.0.1:31012}"
export OPENAPI_MCP_HEADERS="{\"Authorization\":\"Bearer ${ANYTYPE_API_KEY}\", \"Anytype-Version\":\"2025-11-08\"}"

exec /home/brad/Documents/Research/node_modules/.bin/anytype-mcp "$@"
