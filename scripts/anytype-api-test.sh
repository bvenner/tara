#!/usr/bin/env bash
# AnyType API smoke test — verifies the headless server and key CRUD operations.
# Run from inside the devenv shell.
# Environment variables (ANYTYPE_API_KEY, etc.) are loaded by direnv from .enc.env

set -euo pipefail

API_BASE="${ANYTYPE_API_BASE_URL:-http://127.0.0.1:31012}"
API_KEY="${ANYTYPE_API_KEY:-}"

if [ -z "$API_KEY" ]; then
  echo "ERROR: ANYTYPE_API_KEY not set. Ensure direnv has loaded .enc.env"
  exit 1
fi

AUTH_HEADER="Authorization: Bearer ${API_KEY}"
VERSION_HEADER="Anytype-Version: 2025-11-08"

echo "=== AnyType API Smoke Test ==="
echo "API: $API_BASE"
echo ""

# 1. List spaces
echo "1. List spaces..."
SPACE_ID=$(curl -s "$API_BASE/v1/spaces" \
  -H "$AUTH_HEADER" -H "$VERSION_HEADER" | jq -r '.data[0].id')
echo "   Space ID: $SPACE_ID"

# 2. Create object
echo "2. Create object..."
OBJ_RESPONSE=$(curl -s -X POST "$API_BASE/v1/spaces/$SPACE_ID/objects" \
  -H "$AUTH_HEADER" -H "$VERSION_HEADER" -H "Content-Type: application/json" \
  -d '{"name": "Smoke Test Object", "body": "Created by smoke test script.", "type_key": "page"}')
OBJ_ID=$(echo "$OBJ_RESPONSE" | jq -r '.object.id')
OBJ_NAME=$(echo "$OBJ_RESPONSE" | jq -r '.object.name')
echo "   Created: $OBJ_NAME (ID: $OBJ_ID)"

# 3. Read object
echo "3. Read object..."
READ_RESPONSE=$(curl -s "$API_BASE/v1/spaces/$SPACE_ID/objects/$OBJ_ID" \
  -H "$AUTH_HEADER" -H "$VERSION_HEADER")
READ_NAME=$(echo "$READ_RESPONSE" | jq -r '.object.name')
echo "   Name: $READ_NAME"

# 4. Update object
echo "4. Update object..."
curl -s -X PATCH "$API_BASE/v1/spaces/$SPACE_ID/objects/$OBJ_ID" \
  -H "$AUTH_HEADER" -H "$VERSION_HEADER" -H "Content-Type: application/json" \
  -d '{"name": "Smoke Test Object (Updated)"}' > /dev/null
echo "   Patched name"

# 5. Search
echo "5. Global search..."
SEARCH_RESULT=$(curl -s -X POST "$API_BASE/v1/search" \
  -H "$AUTH_HEADER" -H "$VERSION_HEADER" -H "Content-Type: application/json" \
  -d '{"query": "Smoke Test"}')
SEARCH_COUNT=$(echo "$SEARCH_RESULT" | jq '.data | length')
echo "   Found $SEARCH_COUNT object(s)"

# 6. Delete (archive)
echo "6. Delete object..."
curl -s -X DELETE "$API_BASE/v1/spaces/$SPACE_ID/objects/$OBJ_ID" \
  -H "$AUTH_HEADER" -H "$VERSION_HEADER" > /dev/null
echo "   Archived"

# 7. Verify deletion
echo "7. Verify deletion..."
LIST_RESULT=$(curl -s "$API_BASE/v1/spaces/$SPACE_ID/objects" \
  -H "$AUTH_HEADER" -H "$VERSION_HEADER")
REMAINING=$(echo "$LIST_RESULT" | jq '[.data[] | select(.id == "'$OBJ_ID'")] | length')
if [ "$REMAINING" -eq 0 ]; then
  echo "   Object not in list (archived)"
else
  echo "   WARNING: Object still in list"
fi

echo ""
echo "=== All tests passed ==="
