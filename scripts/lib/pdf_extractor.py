"""PDF extraction using Docling."""
import re
from pathlib import Path
from typing import Dict, List, Optional

try:
    from docling.datamodel.document import ConversionResult
    from docling.document_converter import DocumentConverter
    HAS_DOCLING = True
except ImportError:
    HAS_DOCLING = False


def extract_doi(text: str) -> Optional[str]:
    """Find a DOI in raw text."""
    patterns = [
        r"DOI[:\s]+(10\.\d{4,9}/[-._;()/:\w]+)",
        r"doi\.org/(10\.\d{4,9}/[-._;()/:\w]+)",
        r"(10\.\d{4,9}/[-._;()/:\w]+)",
    ]
    for pat in patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            found = m.group(1) if m.lastindex else m.group(0)
            if found.startswith("doi.org/"):
                found = found[8:]
            elif found.lower().startswith("doi"):
                found = re.split(r"[:\s]+", found, maxsplit=1)[-1]
            return found
    return None


def extract_arxiv_id(text: str) -> Optional[str]:
    """Find an arXiv ID in raw text."""
    # Match arXiv:YYYY.NNNNN or arXiv:YYYY.NNNNNvN
    m = re.search(r"ar[xX]iv[:\s]+(\d{4,5}\.\d{4,5}(?:v\d+)?)", text)
    if m:
        return m.group(1).split("v")[0]  # strip version suffix
    return None


def extract_from_pdf(pdf_path: str) -> Dict[str, Optional[str]]:
    """Extract metadata and text from a PDF using Docling."""
    if not HAS_DOCLING:
        raise RuntimeError("Docling is not installed in this environment.")

    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(pdf_path)

    converter = DocumentConverter()
    result = converter.convert(str(path))
    doc = result.document

    # Export full text as markdown
    full_text = doc.export_to_markdown()

    # Heuristic title extraction: skip arXiv header, find first substantial line
    title: Optional[str] = None
    for item in doc.texts:
        text = str(item.text).strip()
        if not text or len(text) < 5:
            continue
        # Skip arXiv header lines
        if re.match(r"ar[xX]iv[:\s]+\d{4,5}\.\d{4,5}", text):
            continue
        # Skip date lines
        if re.match(r"\d{1,2}\s+[A-Za-z]+\s+\d{4}", text):
            continue
        title = text
        break

    # Heuristic abstract extraction
    abstract: Optional[str] = None
    text_lower = full_text.lower()
    abs_start = text_lower.find("abstract")
    if abs_start != -1:
        # Grab up to the next major heading or a reasonable length
        snippet = full_text[abs_start:abs_start + 3000]
        # Cut at next markdown heading or double newline
        for cutoff in ["\n#", "\n##", "\n\n\n"]:
            idx = snippet.find(cutoff, 100)  # skip first 100 chars to avoid "Abstract" word itself
            if idx != -1:
                snippet = snippet[:idx]
                break
        abstract = snippet.strip()

    # DOI and arXiv
    doi = extract_doi(full_text)
    arxiv_id = extract_arxiv_id(full_text)

    # Authors heuristic: look for patterns near the top of the document
    authors: List[str] = []
    top_text = full_text[:2000]
    author_lines = re.findall(r"(?:Authors?[:\s]*|Author[:\s]*)(.+?)(?:\n\n|\n#|\n##|$)", top_text, re.IGNORECASE | re.DOTALL)
    if author_lines:
        raw = author_lines[0].replace("\n", " ").strip()
        authors = [a.strip() for a in re.split(r"[,;]", raw) if len(a.strip()) > 2]

    return {
        "title": title,
        "abstract": abstract,
        "authors": authors,
        "doi": doi,
        "arxiv_id": arxiv_id,
        "full_text": full_text,
        "page_count": len(doc.pages) if hasattr(doc, "pages") else None,
        "source_path": str(path.resolve()),
    }
