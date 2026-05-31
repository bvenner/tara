# TARA Project State — Checkpoint 2026-05-31

Use this file to resume work after context resets.

---

## 1. What's Running

| Service | Status | Endpoint | Notes |
|---|---|---|---|
| `anytype-cli` | Running (PID 291113) | `127.0.0.1:31012` | Headless server, started from devenv |
| AnyType MCP | Connected in OpenCode | via wrapper script | Configured in `opencode.jsonc` |

**Restart if needed:**
```bash
cd ~/Documents/Research
devenv shell
anytype serve --listen-address 127.0.0.1:31012 > /tmp/anytype-server.log 2>&1 &
```

---

## 2. Bot Account & Credentials

| Item | Value | Location |
|---|---|---|
| Bot name | `tara-bot` | — |
| Account ID | `AArFZ9fimqpTAJ8s1vEUwfJ2EuRaBFbaxy8vBJ8Bc33VQtVu` | — |
| API key name | `tara-mcp-integration` | — |
| API key | `WGA/MQD1...` | `opencode.jsonc` (DO NOT COMMIT) |
| Space ID | `bafyreidkdyo37nichr3kpkjgm4dmy2c4jvh5g67ubbpk4npt7uxf5i5cvy.2gx7csytgvlvd` | — |

**Security note:** The API key lives in `.env` (gitignored). `anytype-mcp-wrapper.sh` sources `.env` at runtime. `opencode.jsonc` contains no secrets. Do not commit `.env` to a public repo.

---

## 3. Verified Capabilities

- [x] AnyType CLI headless server (`anytype serve`)
- [x] Bot account creation (`anytype auth create`)
- [x] API key generation (`anytype auth apikey create`)
- [x] Space listing via API (`GET /v1/spaces`)
- [x] Object CRUD via API (create, read, update, search, list, delete)
- [x] MCP server connected in OpenCode (`opencode mcp list` → ✓ anytype connected)
- [x] devenv shell with `anytype-cli`, `docling`, `pandas`, `node.js 22`
- [x] Phase 1 PDF pipeline: Docling extraction → OpenAlex enrichment → AnyType Paper/Author objects
- [x] Phase 2 Citation graph: SQLite local store, OpenAlex reference/cited_by enrichment, graph queries
- [x] Phase 3 Research agent integration: autoresearch workspace → AnyType Project/Paper/Experiment objects

---

## 4. Project Files

| File | Purpose |
|---|---|
| `anytype-based-tara/research-assistant-architecture.md` | Full architecture document |
| `devenv.nix` | Reproducible environment definition |
| `devenv.yaml` / `.envrc` | devenv configuration |
| `requirements.txt` | PyPI packages for venv |
| `opencode.jsonc` | OpenCode project config (MCP server) |
| `anytype-mcp-wrapper.sh` | MCP server wrapper (sources `.env` for API key) |
| `scripts/anytype-api-test.sh` | API CRUD smoke test script |
| `scripts/ingest_pdf.py` | Phase 1 PDF→AnyType ingestion pipeline |
| `scripts/lib/anytype_client.py` | AnyType REST API wrapper (rate-limited) |
| `scripts/lib/pdf_extractor.py` | Docling-based PDF text/metadata extraction |
| `scripts/lib/openalex_client.py` | OpenAlex API client (works, DOI, arXiv, title) |
| `scripts/lib/arxiv_client.py` | arXiv API client (metadata by ID, preferred for arXiv papers) |
| `scripts/lib/pdf_metadata.py` | PyPDF2-based PDF metadata writer (embeds title/authors/DOI into processed PDFs) |
| `scripts/lib/graph_store.py` | SQLite citation graph store (papers, authors, citations) |
| `scripts/build_citation_graph.py` | Phase 2 CLI: init/enrich/sync/stats for citation graph |
| `scripts/research_project.py` | Phase 3 CLI: create/sync/status/list research projects |
| `scripts/sync_research_to_anytype.py` | Phase 3 bridge: autoresearch workspace → AnyType objects |
| `papers/incoming/` | Drop PDFs here for processing |
| `papers/processed/` | PDFs moved here after ingestion |
| `PROJECT_STATE.md` | This file |

---

## 5. Next Steps (Architecture Phase Map)

### Phase 0 — Foundation ✅ DONE
Working AnyType ↔ OpenCode MCP connection. Object CRUD verified.

### Phase 1 — PDF Pipeline ✅ DONE
- Ingest PDF → Docling extraction
- Query **arXiv API** by arXiv ID (best source for arXiv papers)
- Query OpenAlex by DOI / arXiv ID / title (fallback for non-arXiv papers)
- Create AnyType `Paper` and `Author` objects
- Store PDF locally, link path in object
- Supports `--title` override for bad extractions
- arXiv ID detected from filename or PDF text
- **Batch mode**: process all PDFs in a directory
- **Dry-run mode**: preview without side effects
- **Duplicate detection**: skip papers already in AnyType (by DOI/arXiv ID/title)
- **PDF metadata embedding**: title, authors, abstract, DOI, arXiv ID written into processed PDFs

### Phase 2 — Citation Graph ✅ DONE
- Local SQLite graph store (`scripts/lib/graph_store.py`)
  - Tables: `papers`, `authors`, `paper_authors`, `citations`
  - Indexed by DOI, arXiv ID, OpenAlex ID, AnyType ID
  - Deduplication by identifier or title
- OpenAlex enrichment: fetch `referenced_works` and `cited_by` for each paper
- Graph queries: outgoing references, incoming citations, network traversal
- AnyType sync: create `cites` relations between papers (dry-run supported)
- `ingest_pdf.py` now writes to graph automatically on every ingest
- CLI tool: `scripts/build_citation_graph.py` with `--init`, `--enrich`, `--sync-anytype`, `--stats`

### Phase 3 — Research Agent Integration ✅ DONE
- `scripts/research_project.py`: create / sync / status / list CLI for research projects
- `scripts/sync_research_to_anytype.py`: bridge autoresearch workspace → AnyType objects
  - Reads `research-state.yaml`, `findings.md`, `literature/`, `experiments/`
  - Creates/updates `Project:` page object with structured body
  - Creates/links `Paper:` objects from literature summaries
  - Creates `Experiment:` objects from `experiments/{slug}/protocol.md`
- `anytype_client.py` update: `update_object` uses `markdown` field (AnyType PATCH API)
- Naming conventions for object types (using `page` type):
  - `Project: {title}` — research project overview
  - `Paper: {title}` — academic paper (Phase 1, linked to project)
  - `Experiment: {title}` — research experiment protocol + analysis

### Phase 4 — Action Research / CSH (NEXT)
- Custom OpenCode skill for Ulrich's 12 boundary questions
- AnyType types: `Intervention`, `Stakeholder`, `BoundaryJudgment`, `Observation`
- Plan-Act-Observe-Reflect cycle tracking

### Phase 4 — Action Research / CSH
- Custom OpenCode skill for Ulrich's 12 boundary questions
- AnyType types: `Intervention`, `Stakeholder`, `BoundaryJudgment`, `Observation`
- Plan-Act-Observe-Reflect cycle tracking

---

## 6. Quick Commands

```bash
# Enter the environment
cd ~/Documents/Research && devenv shell

# Check anytype server is running
ss -tlnp | grep 31012

# Test API directly
./scripts/anytype-api-test.sh

# Check MCP connection
opencode mcp list

# List spaces
curl -s http://127.0.0.1:31012/v1/spaces \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Anytype-Version: 2025-11-08"

# Ingest a PDF (auto extract + OpenAlex lookup)
python scripts/ingest_pdf.py papers/incoming/some-paper.pdf

# Ingest with title override (when extraction fails)
python scripts/ingest_pdf.py papers/incoming/some-paper.pdf --title "Correct Paper Title"

# Batch process all PDFs in incoming/
python scripts/ingest_pdf.py papers/incoming/ --batch

# Dry-run: preview what would be created (no side effects)
python scripts/ingest_pdf.py papers/incoming/ --batch --dry-run

# Citation graph: initialize from AnyType, enrich from OpenAlex, sync relations
python scripts/build_citation_graph.py --all

# Graph stats
python scripts/build_citation_graph.py --stats

# Graph dry-run (preview AnyType relation creation)
python scripts/build_citation_graph.py --sync-anytype --dry-run

# Research project: create a new project workspace + AnyType object
python scripts/research_project.py create "Research question" --domain "field"

# Research project: sync workspace to AnyType
python scripts/research_project.py sync /path/to/project [--dry-run]

# Research project: show status
python scripts/research_project.py status /path/to/project

# Research project: list all projects in AnyType
python scripts/research_project.py list
```

---

*Last updated: 2026-05-31 (end of Phase 3) by OpenCode*
