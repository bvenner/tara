"""Local SQLite graph store for TARA citation graph.

Follows SotAScope pattern: lightweight, local-first, easily queryable.
Schema: papers, authors, paper_authors (many-to-many), citations.
"""
import sqlite3
import os
from typing import Optional, List, Dict, Any, Tuple
from contextlib import contextmanager

DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "data", "tara_graph.db")


class GraphStore:
    def __init__(self, db_path: Optional[str] = None):
        self.db_path = db_path or os.path.abspath(DEFAULT_DB_PATH)
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._init_schema()

    @contextmanager
    def _conn(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()

    def _init_schema(self):
        with self._conn() as conn:
            conn.executescript(SCHEMA)

    # ── Paper operations ─────────────────────────────────────────

    def add_paper(self, paper: Dict[str, Any]) -> int:
        """Insert or update a paper. Returns the paper id."""
        with self._conn() as conn:
            # Check for existing by openalex_id, doi, arxiv_id, or title
            existing = self._find_paper(conn, paper)
            if existing:
                pid = existing["id"]
                # Merge any new fields
                updates = {
                    k: v for k, v in paper.items()
                    if v is not None and v != "" and k != "id"
                }
                if updates:
                    cols = ", ".join(f"{k}=?" for k in updates)
                    conn.execute(
                        f"UPDATE papers SET {cols} WHERE id=?",
                        (*updates.values(), pid),
                    )
                return pid

            def _nullify(val):
                return val if val else None
            cursor = conn.execute(
                """
                INSERT INTO papers
                (title, doi, arxiv_id, openalex_id, year, venue, abstract,
                 citation_count, local_pdf_path, anytype_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    paper.get("title", ""),
                    _nullify(paper.get("doi") or paper.get("DOI")),
                    _nullify(paper.get("arxiv_id")),
                    _nullify(paper.get("openalex_id")),
                    paper.get("year") or paper.get("publication_year"),
                    paper.get("venue"),
                    paper.get("abstract"),
                    paper.get("citation_count", 0),
                    paper.get("local_pdf_path"),
                    _nullify(paper.get("anytype_id")),
                ),
            )
            return cursor.lastrowid

    def _find_paper(self, conn: sqlite3.Connection, paper: Dict[str, Any]) -> Optional[sqlite3.Row]:
        for key in ("openalex_id", "doi", "arxiv_id"):
            val = paper.get(key) or paper.get(key.upper())
            if val:
                row = conn.execute(
                    f"SELECT * FROM papers WHERE {key}=? LIMIT 1", (val,)
                ).fetchone()
                if row:
                    return row
        # Fall back to title match (case-insensitive), but ignore "Paper:" prefix
        title = paper.get("title", "")
        if title:
            clean_title = title.replace("Paper: ", "").replace("Paper:", "").strip()
            row = conn.execute(
                "SELECT * FROM papers WHERE LOWER(title)=LOWER(?) LIMIT 1",
                (clean_title,),
            ).fetchone()
            if row:
                return row
            # Also try matching against the raw title in case it's already clean
            row = conn.execute(
                "SELECT * FROM papers WHERE LOWER(title)=LOWER(?) LIMIT 1",
                (title,),
            ).fetchone()
            if row:
                return row
        return None

    def get_paper(self, paper_id: int) -> Optional[Dict[str, Any]]:
        with self._conn() as conn:
            row = conn.execute(
                "SELECT * FROM papers WHERE id=?", (paper_id,)
            ).fetchone()
            return dict(row) if row else None

    def list_papers(self, limit: int = 100) -> List[Dict[str, Any]]:
        with self._conn() as conn:
            rows = conn.execute(
                "SELECT * FROM papers ORDER BY created_at DESC LIMIT ?",
                (limit,),
            ).fetchall()
            return [dict(r) for r in rows]

    def paper_by_anytype_id(self, anytype_id: str) -> Optional[Dict[str, Any]]:
        with self._conn() as conn:
            row = conn.execute(
                "SELECT * FROM papers WHERE anytype_id=? LIMIT 1",
                (anytype_id,),
            ).fetchone()
            return dict(row) if row else None

    # ── Author operations ──────────────────────────────────────

    def add_author(self, name: str, orcid: Optional[str] = None,
                   openalex_id: Optional[str] = None,
                   anytype_id: Optional[str] = None) -> int:
        with self._conn() as conn:
            # Try to find existing
            if openalex_id:
                row = conn.execute(
                    "SELECT id FROM authors WHERE openalex_id=? LIMIT 1",
                    (openalex_id,),
                ).fetchone()
                if row:
                    return row["id"]
            row = conn.execute(
                "SELECT id FROM authors WHERE LOWER(name)=LOWER(?) LIMIT 1",
                (name,),
            ).fetchone()
            if row:
                return row["id"]
            cursor = conn.execute(
                "INSERT INTO authors (name, orcid, openalex_id, anytype_id) VALUES (?, ?, ?, ?)",
                (name, orcid, openalex_id, anytype_id),
            )
            return cursor.lastrowid

    def link_paper_author(self, paper_id: int, author_id: int, position: int = 0):
        with self._conn() as conn:
            conn.execute(
                """INSERT OR IGNORE INTO paper_authors (paper_id, author_id, position)
                   VALUES (?, ?, ?)""",
                (paper_id, author_id, position),
            )

    def get_paper_authors(self, paper_id: int) -> List[Dict[str, Any]]:
        with self._conn() as conn:
            rows = conn.execute(
                """SELECT a.*, pa.position FROM authors a
                   JOIN paper_authors pa ON a.id = pa.author_id
                   WHERE pa.paper_id=?
                   ORDER BY pa.position""",
                (paper_id,),
            ).fetchall()
            return [dict(r) for r in rows]

    # ── Citation operations ────────────────────────────────────

    def add_citation(self, from_paper_id: int, to_paper_id: int,
                     source: str = "openalex") -> bool:
        """Add a citation edge. Returns True if inserted, False if already existed."""
        with self._conn() as conn:
            try:
                conn.execute(
                    """INSERT INTO citations (from_paper_id, to_paper_id, source)
                       VALUES (?, ?, ?)""",
                    (from_paper_id, to_paper_id, source),
                )
                return True
            except sqlite3.IntegrityError:
                return False

    def get_citations(self, paper_id: int) -> List[Dict[str, Any]]:
        """Papers cited by paper_id (outgoing)."""
        with self._conn() as conn:
            rows = conn.execute(
                """SELECT p.*, c.source FROM papers p
                   JOIN citations c ON p.id = c.to_paper_id
                   WHERE c.from_paper_id=?""",
                (paper_id,),
            ).fetchall()
            return [dict(r) for r in rows]

    def get_cited_by(self, paper_id: int) -> List[Dict[str, Any]]:
        """Papers citing paper_id (incoming)."""
        with self._conn() as conn:
            rows = conn.execute(
                """SELECT p.*, c.source FROM papers p
                   JOIN citations c ON p.id = c.from_paper_id
                   WHERE c.to_paper_id=?""",
                (paper_id,),
            ).fetchall()
            return [dict(r) for r in rows]

    def citation_count(self, paper_id: int) -> Tuple[int, int]:
        """Returns (outgoing_citations, incoming_citations)."""
        with self._conn() as conn:
            out_ = conn.execute(
                "SELECT COUNT(*) FROM citations WHERE from_paper_id=?", (paper_id,)
            ).fetchone()[0]
            in_ = conn.execute(
                "SELECT COUNT(*) FROM citations WHERE to_paper_id=?", (paper_id,)
            ).fetchone()[0]
            return out_, in_

    # ── Graph queries ────────────────────────────────────────────

    def get_citation_network(self, paper_ids: List[int], depth: int = 1) -> Dict[str, List[Dict]]:
        """Get citation network around given paper IDs up to depth."""
        nodes = set(paper_ids)
        edges = []
        frontier = set(paper_ids)
        for _ in range(depth):
            new_frontier = set()
            for pid in frontier:
                with self._conn() as conn:
                    # outgoing
                    for row in conn.execute(
                        "SELECT to_paper_id FROM citations WHERE from_paper_id=?", (pid,)
                    ).fetchall():
                        edges.append({"from": pid, "to": row[0], "direction": "out"})
                        new_frontier.add(row[0])
                    # incoming
                    for row in conn.execute(
                        "SELECT from_paper_id FROM citations WHERE to_paper_id=?", (pid,)
                    ).fetchall():
                        edges.append({"from": row[0], "to": pid, "direction": "in"})
                        new_frontier.add(row[0])
            frontier = new_frontier - nodes
            nodes |= frontier
        with self._conn() as conn:
            paper_rows = conn.execute(
                f"SELECT * FROM papers WHERE id IN ({','.join('?'*len(nodes))})",
                tuple(nodes),
            ).fetchall()
            papers = [dict(r) for r in paper_rows]
        return {"papers": papers, "edges": edges}

    def stats(self) -> Dict[str, int]:
        with self._conn() as conn:
            papers = conn.execute("SELECT COUNT(*) FROM papers").fetchone()[0]
            authors = conn.execute("SELECT COUNT(*) FROM authors").fetchone()[0]
            citations = conn.execute("SELECT COUNT(*) FROM citations").fetchone()[0]
            return {"papers": papers, "authors": authors, "citations": citations}


# ── SQL Schema ─────────────────────────────────────────────────

SCHEMA = """
CREATE TABLE IF NOT EXISTS papers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    doi TEXT UNIQUE,
    arxiv_id TEXT UNIQUE,
    openalex_id TEXT UNIQUE,
    year INTEGER,
    venue TEXT,
    abstract TEXT,
    citation_count INTEGER DEFAULT 0,
    local_pdf_path TEXT,
    anytype_id TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    orcid TEXT UNIQUE,
    openalex_id TEXT UNIQUE,
    anytype_id TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS paper_authors (
    paper_id INTEGER NOT NULL REFERENCES papers(id) ON DELETE CASCADE,
    author_id INTEGER NOT NULL REFERENCES authors(id) ON DELETE CASCADE,
    position INTEGER DEFAULT 0,
    PRIMARY KEY (paper_id, author_id)
);

CREATE TABLE IF NOT EXISTS citations (
    from_paper_id INTEGER NOT NULL REFERENCES papers(id) ON DELETE CASCADE,
    to_paper_id   INTEGER NOT NULL REFERENCES papers(id) ON DELETE CASCADE,
    source TEXT DEFAULT 'openalex',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (from_paper_id, to_paper_id)
);

CREATE INDEX IF NOT EXISTS idx_papers_doi ON papers(doi);
CREATE INDEX IF NOT EXISTS idx_papers_arxiv ON papers(arxiv_id);
CREATE INDEX IF NOT EXISTS idx_papers_oa ON papers(openalex_id);
CREATE INDEX IF NOT EXISTS idx_papers_anytype ON papers(anytype_id);
CREATE INDEX IF NOT EXISTS idx_citations_from ON citations(from_paper_id);
CREATE INDEX IF NOT EXISTS idx_citations_to ON citations(to_paper_id);
"""
