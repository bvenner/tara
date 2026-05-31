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

### Phase 2 — Citation Graph (NEXT)
- Local SQLite graph store (papers, authors, citations)
- OpenAlex API or local snapshot enrichment
- Sync citation edges to AnyType relations

### Phase 3 — Research Agent Integration
- Extend autoresearch skill to emit AnyType objects
- Project-based collections in AnyType
- Natural language → structured research output

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
```

---

*Last updated: 2026-05-31 (end of Phase 1) by OpenCode*
