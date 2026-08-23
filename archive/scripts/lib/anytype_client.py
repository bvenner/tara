"""Simple AnyType REST API client with rate-limit awareness."""
import os
import json
import time
import urllib.request
import urllib.error
from typing import Optional, List, Dict, Any

API_BASE = os.environ.get("ANYTYPE_API_BASE_URL", "http://127.0.0.1:31012")
API_KEY = os.environ.get("ANYTYPE_API_KEY", "")
API_VERSION = "2025-11-08"
SPACE_ID = os.environ.get("ANYTYPE_SPACE_ID", "")

# Rate limit: 1 req/sec sustained; burst 60
_last_request_time = 0.0
_MIN_INTERVAL = 1.05  # seconds between requests


def _req(
    method: str,
    path: str,
    body: Optional[Dict[str, Any]] = None,
    retries: int = 2,
) -> Dict[str, Any]:
    global _last_request_time
    url = f"{API_BASE}{path}"
    data = json.dumps(body).encode("utf-8") if body else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {API_KEY}")
    req.add_header("Anytype-Version", API_VERSION)
    if data:
        req.add_header("Content-Type", "application/json")

    # Rate-limit throttle
    elapsed = time.time() - _last_request_time
    if elapsed < _MIN_INTERVAL:
        time.sleep(_MIN_INTERVAL - elapsed)

    for attempt in range(retries + 1):
        try:
            _last_request_time = time.time()
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries:
                time.sleep(2 ** attempt)
                continue
            raise
    return {}  # unreachable


def list_spaces() -> List[Dict[str, Any]]:
    """Return list of spaces."""
    resp = _req("GET", "/v1/spaces")
    return resp.get("data", [])


def create_object(
    name: str,
    body: str = "",
    type_key: str = "page",
    space_id: Optional[str] = None,
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Create an object in AnyType."""
    sid = space_id or SPACE_ID
    payload: Dict[str, Any] = {"name": name, "body": body, "type_key": type_key}
    if tags:
        # AnyType API may not support tags directly on creation;
        # we will attempt and fall back gracefully.
        payload["tags"] = tags
    return _req("POST", f"/v1/spaces/{sid}/objects", payload)


def get_object(object_id: str, space_id: Optional[str] = None) -> Dict[str, Any]:
    sid = space_id or SPACE_ID
    return _req("GET", f"/v1/spaces/{sid}/objects/{object_id}")


def search_objects(query: str, limit: int = 20) -> List[Dict[str, Any]]:
    """Global search across spaces."""
    resp = _req("POST", "/v1/search", {"query": query, "limit": limit})
    return resp.get("data", [])


def list_objects(space_id: Optional[str] = None, limit: int = 100, offset: int = 0) -> List[Dict[str, Any]]:
    """List objects in a space (paginated)."""
    sid = space_id or SPACE_ID
    resp = _req("GET", f"/v1/spaces/{sid}/objects?limit={limit}&offset={offset}")
    return resp.get("data", [])


def create_relation(from_id: str, to_id: str, relation_key: str,
                    space_id: Optional[str] = None) -> Dict[str, Any]:
    """Create a relation (link) between two objects.

    AnyType API may support this via object properties or a dedicated
    relation endpoint.  This implementation tries the most common
    patterns and falls back gracefully.
    """
    sid = space_id or SPACE_ID
    # Attempt 1: PATCH object with relation in properties
    payload = {"relations": {relation_key: [to_id]}}
    try:
        return _req("PATCH", f"/v1/spaces/{sid}/objects/{from_id}", payload)
    except Exception:
        pass
    # Attempt 2: dedicated relation endpoint (if supported in future API)
    try:
        return _req("POST", f"/v1/spaces/{sid}/objects/{from_id}/relations", {
            "relation_key": relation_key,
            "target_id": to_id,
        })
    except Exception:
        return {}


def update_object(
    object_id: str,
    name: Optional[str] = None,
    body: Optional[str] = None,
    space_id: Optional[str] = None,
) -> Dict[str, Any]:
    sid = space_id or SPACE_ID
    payload: Dict[str, Any] = {}
    if name is not None:
        payload["name"] = name
    if body is not None:
        # AnyType API uses "markdown" for body updates on PATCH
        payload["markdown"] = body
    return _req("PATCH", f"/v1/spaces/{sid}/objects/{object_id}", payload)


def delete_object(object_id: str, space_id: Optional[str] = None) -> None:
    sid = space_id or SPACE_ID
    _req("DELETE", f"/v1/spaces/{sid}/objects/{object_id}")
