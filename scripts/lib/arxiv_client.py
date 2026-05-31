"""arXiv API client for paper metadata."""
import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse
from typing import Optional, Dict, List, Any

BASE_URL = "http://export.arxiv.org/api/query"


def _fetch(ids: List[str]) -> Optional[ET.Element]:
    """Query arXiv API for one or more IDs."""
    if not ids:
        return None
    id_list = ",".join(ids)
    url = f"{BASE_URL}?id_list={urllib.parse.quote(id_list)}&max_results={len(ids)}"
    req = urllib.request.Request(url, headers={"Accept": "application/atom+xml"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return ET.fromstring(resp.read())
    except Exception:
        return None


def _ns(tag: str) -> str:
    """Build namespaced tag for Atom/arxiv namespaces."""
    # arXiv API uses: http://www.w3.org/2005/Atom
    # arxiv extension: http://arxiv.org/schemas/atom
    ATOM_NS = "http://www.w3.org/2005/Atom"
    ARXIV_NS = "http://arxiv.org/schemas/atom"
    if ":" in tag:
        prefix, local = tag.split(":", 1)
        if prefix == "arxiv":
            return f"{{{ARXIV_NS}}}{local}"
    return f"{{{ATOM_NS}}}{tag}"


def get_work_by_arxiv_id(arxiv_id: str) -> Optional[Dict[str, Any]]:
    """Fetch metadata for a single arXiv ID."""
    root = _fetch([arxiv_id])
    if root is None:
        return None
    entry = root.find(_ns("entry"))
    if entry is None:
        return None
    return _parse_entry(entry)


def _parse_entry(entry: ET.Element) -> Dict[str, Any]:
    """Parse an Atom entry into a flat dict."""
    def text(tag: str) -> str:
        el = entry.find(_ns(tag))
        return el.text.strip() if el is not None and el.text else ""

    authors: List[str] = []
    for author in entry.findall(_ns("author")):
        name = author.find(_ns("name"))
        if name is not None and name.text:
            authors.append(name.text.strip())

    # arXiv categories
    categories: List[str] = [
        cat.get("term", "")
        for cat in entry.findall(_ns("category"))
        if cat.get("term")
    ]

    # Links
    pdf_url = ""
    for link in entry.findall(_ns("link")):
        if link.get("title") == "pdf" or link.get("type") == "application/pdf":
            pdf_url = link.get("href", "")
            break

    # arxiv-specific fields
    doi = ""
    doi_el = entry.find(_ns("arxiv:doi"))
    if doi_el is not None and doi_el.text:
        doi = doi_el.text.strip()

    journal_ref = ""
    journal_el = entry.find(_ns("arxiv:journal_ref"))
    if journal_el is not None and journal_el.text:
        journal_ref = journal_el.text.strip()

    return {
        "title": text("title").replace("\n", " ").strip(),
        "abstract": text("summary").strip(),
        "authors": authors,
        "arxiv_id": text("id").split("/")[-1].replace("arxiv:", ""),
        "published": text("published"),
        "updated": text("updated"),
        "doi": doi,
        "journal_ref": journal_ref,
        "categories": categories,
        "pdf_url": pdf_url,
        "primary_category": categories[0] if categories else "",
    }
