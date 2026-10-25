#!/usr/bin/env python3
"""Convert a manually-staged PDF when the fulltext worker's mode "local" cannot.

mode "local" in fetch_fulltext.py requires a DOI: it derives the corpus key from a
live OpenAlex lookup. Two cases fall outside it:

  1. Works with a corpus record but no DOI (repository-only papers, preprints).
  2. Non-OpenAlex documents (e.g. a philosopher's essay retrieved by URL).

Usage (repo interpreter; from projects/knowledge-repository-poc/pipelines):

  ../bin/tara-python ../scripts/convert_no_doi.py <key>
  ../bin/tara-python ../scripts/convert_no_doi.py <key> --pdf /path/to/file.pdf \\
      --title "..." --authors "A; B" --year 1997 --venue "..."

Staging convention: papers/incoming/<key>.pdf unless --pdf is given.
Output: corpus/fulltext/<key>.md with status "manual" (same as mode "local").
If corpus/external/<key>.json exists it supplies the metadata; otherwise pass
--title etc. Batch multiple keys in one invocation to load the converter once
(docling model loading is expensive).

Quirk preserved from the worker: convert_local_pdf takes the converter FACTORY
(fetch_fulltext.get_converter), not a converter instance.
"""
import argparse
import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
sys.path.insert(0, str(SCRIPTS / "lib"))
import fetch_fulltext as F  # noqa: E402
from lib.pdf_extractor import extract_from_pdf  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("keys", nargs="+", help="corpus keys, e.g. https_openalex.org_W2111485456")
    ap.add_argument("--pdf", help="explicit PDF path (default papers/incoming/<key>.pdf)")
    ap.add_argument("--title")
    ap.add_argument("--authors", help="semicolon-separated")
    ap.add_argument("--year")
    ap.add_argument("--venue")
    ap.add_argument("--doi")
    args = ap.parse_args()

    F.INCOMING_DIR.mkdir(parents=True, exist_ok=True)
    F.FULLTEXT_DIR.mkdir(parents=True, exist_ok=True)

    for key in args.keys:
        rec_file = F.EXT_DIR / f"{key}.json"
        if rec_file.exists():
            rec = json.loads(rec_file.read_text())
        else:
            rec = {
                "openalex_id": "", "doi": args.doi or "",
                "title": args.title or key, "year": args.year or "",
                "venue": args.venue or "",
                "authors": [a.strip() for a in (args.authors or "").split(";") if a.strip()],
            }

        pdf = Path(args.pdf) if args.pdf else F.INCOMING_DIR / f"{key}.pdf"
        if not pdf.exists():
            print(f"{key}: {pdf} not found — stage the PDF first", file=sys.stderr)
            continue

        md = extract_from_pdf(str(pdf), converter=F.get_converter())
        full = md.get("full_text") or ""
        if len(full.strip()) < 500:
            print(f"{key}: conversion too short ({len(full)} chars), skipped")
            continue

        out = F.FULLTEXT_DIR / f"{key}.md"
        if rec_file.exists():
            F.write_markdown(rec, {}, key, "manual", out, full)
        else:
            head = (
                "> Manual full text (non-OpenAlex) — source: staged PDF\n"
                f"> file: {pdf.name} · license: — · status: manual\n\n"
                f"# {rec['title']}\n\n"
            )
            if rec.get("authors"):
                head += f"**Authors:** {', '.join(rec['authors'])}\n"
            if rec.get("venue") or rec.get("year"):
                head += f"**{rec.get('venue', 'undated')}** · {rec.get('year', '')}\n"
            if rec.get("doi"):
                head += f"**DOI:** {rec['doi']}\n"
            out.write_text(head + "\n" + full + "\n")
        print(f"{key}: converted ({len(full)} chars) -> {out}")


if __name__ == "__main__":
    main()
