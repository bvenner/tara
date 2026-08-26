#!/usr/bin/env python3
"""JSON Lines worker: download openly-accessible full text and convert to markdown.

Reads one request per stdin line:
  {mode: "doi",   doi, refresh?, strict?}
  {mode: "corpus", limit?, refresh?, strict?}
writes markdown files to <poc>/corpus/fulltext/<openalex_id>.md (with a
provenance header), staging raw PDFs under <repo>/papers/incoming/ (gitignored),
then emits one summary line:
  {mode, found, downloaded, converted, skipped, reasons}

OA policy defaults to strict: download only when the OpenAlex best_oa_location
is genuinely reusable (cc-* license, arXiv, or oa_status=green). Set strict=0
to accept any is_oa location with a pdf_url.
"""
import datetime
import json
import re
import sys
from pathlib import Path

import requests

POC_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[3]
LIB_DIR = Path(__file__).resolve().parent / "lib"
EXT_DIR = POC_ROOT / "corpus" / "external"
FULLTEXT_DIR = POC_ROOT / "corpus" / "fulltext"
INCOMING_DIR = REPO_ROOT / "papers" / "incoming"

sys.path.insert(0, str(LIB_DIR))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.pdf_extractor import extract_from_pdf  # noqa: E402
from schemas import FulltextRequest, FulltextSummary  # noqa: E402

UA = ("Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0 "
      "TARA-knowledge-repository/0.1")
MAX_BYTES = 60 * 1024 * 1024
_OA_STATUS_OK = {"gold", "green"}


def sanitize(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "_", value).strip("_") or "work"


def is_strictly_oa(loc: dict, status: str) -> bool:
    lic = (loc.get("license") or "").lower()
    pdf = loc.get("pdf_url") or ""
    if lic.startswith("cc-") or "arxiv.org" in pdf or status == "green":
        return True
    return False


def find_oa(raw: dict) -> dict:
    """Return the most reliably-downloadable OA location for a work.

    Archive copies (arXiv) sidestep publisher bot-gates and are preferred;
    otherwise the best_oa_location is used when it carries a pdf_url.
    """
    candidates = []
    for loc in raw.get("locations", []):
        if not loc.get("is_oa"):
            continue
        pdf = loc.get("pdf_url") or ""
        if not pdf:
            continue
        cand = {"loc": loc, "pdf": pdf, "arxiv": "arxiv.org" in pdf}
        candidates.append(cand)
    arxiv_matches = [c for c in candidates if c["arxiv"]]
    if arxiv_matches:
        return arxiv_matches[0]["loc"]
    pdf_matches = [c for c in candidates if not c["arxiv"]]
    if pdf_matches:
        return pdf_matches[0]["loc"]
    return {}


def download(url: str, dest: Path) -> bool:
    r = requests.get(url, headers={"User-Agent": UA}, timeout=60,
                     allow_redirects=True, stream=True)
    r.raise_for_status()
    size = 0
    first = b""
    with open(dest, "wb") as f:
        for chunk in r.iter_content(chunk_size=1 << 16):
            size += len(chunk)
            if size > MAX_BYTES:
                r.close()
                dest.unlink(missing_ok=True)
                raise RuntimeError(f"download exceeds {MAX_BYTES} bytes")
            first = first or chunk[:1024]
            f.write(chunk)
    if size and not first.lstrip().startswith(b"%PDF"):
        dest.unlink(missing_ok=True)
        ctype = r.headers.get("content-type", "")
        raise RuntimeError(f"not a PDF (content-type={ctype or 'unknown'}); "
                           "likely a bot-gate/interstitial page")
    return True


def drop_title_line(md: str):
    """Remove docling's leading H1 title line (we emit our own titled header)."""
    lines = md.splitlines()
    for i, ln in enumerate(lines):
        if ln.strip() and ln.startswith("# ") and not ln.startswith("## "):
            return "\n".join(lines[i + 1:]), ln.strip()
    return "\n".join(lines), ""


def header(rec: dict, loc: dict, source: str, status: str) -> str:
    when = datetime.date.today().isoformat()
    lines = [
        f"> OpenAlex full text ({when}) — source: {source}",
        f"> DOI: {rec.get('doi','') or '—'} · license: {loc.get('license','') or '—'} · "
        f"status: {status}",
        "",
    ]
    return "\n".join(lines)


def convert_md(rec: dict, loc: dict, key: str, converter_factory) -> tuple[str, str]:
    """Download pdf_url, convert to markdown; return (md, stage_pdf_rel)."""
    pdf = INCOMING_DIR / f"{key}.pdf"
    if not download(loc["pdf_url"], pdf):
        return "", ""
    md = extract_from_pdf(str(pdf), converter=converter_factory())
    full = md.get("full_text") or ""
    return full, pdf.name


def handle(req: FulltextRequest, converter_factory) -> FulltextSummary:
    mode = req.mode
    refresh = bool(req.refresh)
    strict = bool(req.strict)
    limit = req.limit
    reasons = []

    candidates = []
    if mode == "doi":
        doi = req.doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
        if doi:
            candidates = [(doi, doi)]
    else:
        for jf in sorted(EXT_DIR.glob("*.json")):
            rec = json.loads(jf.read_text())
            doi = (rec.get("doi") or "").replace("https://doi.org/", "").replace("http://doi.org/", "")
            if doi:
                candidates.append((doi, rec.get("title", "")))

    found, downloaded, converted = 0, 0, 0
    if limit:
        candidates = candidates[:limit]

    # Live OpenAlex lookup per DOI: the external records predate best_oa_location
    # capture, so fetch the work fresh rather than trusting stale files.
    import openalex_client as oa  # noqa: E402  (LIB_DIR already on sys.path)

    for doi, title in candidates:
        found += 1
        raw = oa.get_work_by_doi(doi)
        if not raw:
            reasons.append(f"{doi}: no OpenAlex record")
            continue
        loc = find_oa(raw)
        if not loc:
            reasons.append(f"{doi}: not openly accessible")
            continue
        if strict and not is_strictly_oa(loc, (raw.get("open_access") or {}).get("oa_status", "")):
            reasons.append(f"{doi}: no permissive license (strict mode)")
            continue
        rec = {
            "openalex_id": raw.get("id", ""),
            "doi": raw.get("doi", ""),
            "title": raw.get("display_name", title),
            "year": raw.get("publication_year"),
            "venue": (raw.get("primary_location") or {}).get("source", {}).get("display_name", ""),
            "authors": [a["author"]["display_name"]
                        for a in raw.get("authorships", []) if a.get("author", {}).get("display_name")],
        }
        key = sanitize(rec["openalex_id"] or ("doi_" + sanitize(doi)))
        md_path = FULLTEXT_DIR / f"{key}.md"
        if md_path.exists() and not refresh:
            reasons.append(f"{key}: already converted")
            continue
        try:
            md, stage = convert_md(rec, loc, key, converter_factory)
        except Exception as e:  # noqa: BLE001
            reasons.append(f"{key}: convert failed ({e.__class__.__name__})")
            continue
        if len(md.strip()) < 500:
            reasons.append(f"{key}: conversion too short, skipped")
            continue
        downloaded += 1
        status = (raw.get("open_access") or {}).get("oa_status", "")
        md_body, _title = drop_title_line(md)
        head = header(rec, loc, loc["pdf_url"], status)
        meta = [f"# {rec['title']}", ""]
        if rec.get("authors"):
            meta.append(f"**Authors:** {', '.join(rec['authors'])}")
        if rec.get("venue") or rec.get("year"):
            meta.append(f"**{rec.get('venue','undated')}** · {rec.get('year','')}")
        if rec.get("doi"):
            meta.append(f"**DOI:** {rec['doi']}")
        body = head + "\n".join(meta) + "\n\n" + md_body + "\n"
        FULLTEXT_DIR.mkdir(parents=True, exist_ok=True)
        md_path.write_text(body)
        converted += 1

    return FulltextSummary(
        mode=mode, found=found, downloaded=downloaded, converted=converted,
        skipped=len(candidates) - converted,
        reasons="; ".join(reasons)[:500],
    )


_converter = None


def get_converter():
    """Lazily create the docling converter (model load is expensive)."""
    global _converter
    if _converter is None:
        from docling.document_converter import DocumentConverter
        _converter = DocumentConverter()
    return _converter


def main():
    INCOMING_DIR.mkdir(parents=True, exist_ok=True)
    FULLTEXT_DIR.mkdir(parents=True, exist_ok=True)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        req = FulltextRequest.model_validate(json.loads(line))
        print(handle(req, get_converter).model_dump_json())
        sys.stdout.flush()


if __name__ == "__main__":
    main()