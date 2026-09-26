"""OpenAlex API client for work/author enrichment."""
import json
import time
import urllib.request
import urllib.error
import urllib.parse
from typing import Optional, Dict, List, Any

BASE_URL = "https://api.openalex.org"
_last_request_time = 0.0
_MIN_INTERVAL = 0.25  # 4 req/sec to be polite


def _req(path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    global _last_request_time
    url = f"{BASE_URL}{path}"
    if params:
        qs = urllib.parse.urlencode(params)
        url = f"{url}?{qs}"

    elapsed = time.time() - _last_request_time
    if elapsed < _MIN_INTERVAL:
        time.sleep(_MIN_INTERVAL - elapsed)

    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    _last_request_time = time.time()

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {}
        raise


def get_work_by_doi(doi: str) -> Optional[Dict[str, Any]]:
    """Fetch a work by DOI (with or without doi.org prefix)."""
    clean = doi.replace("https://", "").replace("http://", "").replace("doi.org/", "")
    data = _req(f"/works/doi:{clean}")
    return data if data else None


def get_work_by_arxiv(arxiv_id: str) -> Optional[Dict[str, Any]]:
    """Fetch a work by arXiv ID."""
    clean = arxiv_id.replace("arxiv:", "").strip()
    data = _req(f"/works/arXiv:{clean}")
    return data if data else None


def search_works(query: str, per_page: int = 5) -> List[Dict[str, Any]]:
    """Search works by free-text query."""
    data = _req("/works", {"search": query, "per-page": per_page})
    return data.get("results", [])


def get_work_references(openalex_id: str, max_refs: int = 25) -> List[Dict[str, Any]]:
    """Fetch referenced works for a given OpenAlex work ID.

    OpenAlex stores references as a list of work IDs inside the work object.
    We fetch the work, then resolve each referenced work individually.
    """
    if not openalex_id.startswith("https://openalex.org/"):
        openalex_id = f"https://openalex.org/{openalex_id}"
    wid = openalex_id.split("/")[-1]
    data = _req(f"/works/{wid}")
    refs = data.get("referenced_works", [])[:max_refs]
    if not refs:
        return []
    results = []
    for ref_url in refs:
        ref_id = ref_url.split("/")[-1] if "/" in ref_url else ref_url
        ref_data = _req(f"/works/{ref_id}")
        if ref_data:
            results.append(normalize_work(ref_data))
    return results


def get_work_cited_by(openalex_id: str, per_page: int = 25) -> List[Dict[str, Any]]:
    """Fetch works that cite a given OpenAlex work ID."""
    if not openalex_id.startswith("https://openalex.org/"):
        openalex_id = f"https://openalex.org/{openalex_id}"
    wid = openalex_id.split("/")[-1]
    data = _req("/works", {"filter": f"cites:{wid}", "per-page": per_page})
    return [normalize_work(r) for r in data.get("results", [])]


def normalize_work(raw: Dict[str, Any]) -> Dict[str, Any]:
    """Flatten OpenAlex work into a simple dict."""
    if not raw:
        return {}

    authors: List[str] = []
    for authorship in raw.get("authorships", []):
        author = authorship.get("author", {})
        name = author.get("display_name", "")
        if name:
            authors.append(name)

    open_access = raw.get("open_access", {})
    biblio = raw.get("biblio", {})

    return {
        "openalex_id": raw.get("id", ""),
        "doi": raw.get("doi", ""),
        "title": raw.get("display_name", ""),
        "publication_year": raw.get("publication_year"),
        "citation_count": raw.get("cited_by_count", 0),
        "authors": authors,
        "abstract": raw.get("abstract", ""),
        "venue": raw.get("host_venue", {}).get("display_name", "")
        if raw.get("host_venue")
        else "",
        "open_access_url": open_access.get("oa_url", ""),
        "is_oa": open_access.get("is_oa", False),
        "type": raw.get("type", ""),
        "pages": biblio.get("first_page", ""),
        "volume": biblio.get("volume", ""),
        "issue": biblio.get("issue", ""),
    }
