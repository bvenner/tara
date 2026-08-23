"""Write extracted metadata into a PDF's document info dictionary.

This makes metadata portable when files are moved to S3 or other backends.
Uses PyPDF2 (lightweight, no heavy dependencies).
"""
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime

try:
    from PyPDF2 import PdfReader, PdfWriter
    HAS_PYPDF2 = True
except ImportError:
    HAS_PYPDF2 = False


def write_pdf_metadata(pdf_path: str, meta: Dict[str, Any]) -> None:
    """Embed metadata into an existing PDF file (overwrites in place).

    Fields written:
        /Title      → meta['title']
        /Author     → meta['authors'] (comma-joined)
        /Subject    → meta['abstract'] (truncated to 2000 chars)
        /Keywords   → meta['doi'], meta['arxiv_id'], meta['categories']
        /Creator    → "TARA PDF Pipeline"
        /CreationDate → ISO 8601 from meta['year'] if available
        /ModDate    → current ISO 8601 timestamp
    """
    if not HAS_PYPDF2:
        raise RuntimeError("PyPDF2 is not installed. Add it to requirements.txt and re-enter devenv.")

    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(pdf_path)

    reader = PdfReader(str(path))
    writer = PdfWriter()

    # Copy all pages
    for page in reader.pages:
        writer.add_page(page)

    # Build document info dict
    info: Dict[str, Any] = {}

    if meta.get("title"):
        info["/Title"] = meta["title"]

    if meta.get("authors"):
        authors = meta["authors"]
        if isinstance(authors, list):
            info["/Author"] = ", ".join(authors)
        else:
            info["/Author"] = str(authors)

    if meta.get("abstract"):
        abstract = meta["abstract"]
        if len(abstract) > 2000:
            abstract = abstract[:1997] + "..."
        info["/Subject"] = abstract

    # Keywords: DOI, arXiv ID, categories
    keywords: list[str] = []
    if meta.get("doi"):
        keywords.append(f"DOI:{meta['doi']}")
    if meta.get("arxiv_id"):
        keywords.append(f"arXiv:{meta['arxiv_id']}")
    if meta.get("categories"):
        cats = meta["categories"]
        if isinstance(cats, list):
            keywords.extend(cats)
        else:
            keywords.append(str(cats))
    if keywords:
        info["/Keywords"] = "; ".join(keywords)

    info["/Creator"] = "TARA PDF Pipeline"

    # Dates
    year = meta.get("year", "")
    if year:
        try:
            dt = datetime(int(year), 1, 1)
            info["/CreationDate"] = f"D:{dt.strftime('%Y%m%d%H%M%S')}"
        except (ValueError, TypeError):
            pass

    now = datetime.now()
    info["/ModDate"] = f"D:{now.strftime('%Y%m%d%H%M%S')}"

    # Preserve existing info if present
    if reader.metadata:
        existing = reader.metadata
        for key, val in existing.items():
            # Only preserve keys we haven't set
            if key not in info and val is not None:
                info[key] = val

    writer.add_metadata(info)

    # Overwrite original
    out_path = path.with_suffix(".tmp.pdf")
    with open(out_path, "wb") as f:
        writer.write(f)
    out_path.rename(path)
    print(f"     Wrote metadata to PDF: {path.name}")
