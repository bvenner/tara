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

**Security note:** The API key is embedded in `anytype-mcp-wrapper.sh` and `opencode.jsonc`. Do not commit these to a public repo.

---

## 3. Verified Capabilities

- [x] AnyType CLI headless server (`anytype serve`)
- [x] Bot account creation (`anytype auth create`)
- [x] API key generation (`anytype auth apikey create`)
- [x] Space listing via API (`GET /v1/spaces`)
- [x] Object CRUD via API (create, read, update, search, list, delete)
- [x] MCP server connected in OpenCode (`opencode mcp list` → ✓ anytype connected)
- [x] devenv shell with `anytype-cli`, `docling`, `pandas`, `node.js 22`

---

## 4. Project Files

| File | Purpose |
|---|---|
| `anytype-based-tara/research-assistant-architecture.md` | Full architecture document |
| `devenv.nix` | Reproducible environment definition |
| `devenv.yaml` / `.envrc` | devenv configuration |
| `requirements.txt` | PyPI packages for venv |
| `opencode.jsonc` | OpenCode project config (MCP server) |
| `anytype-mcp-wrapper.sh` | MCP server wrapper (PATH + env vars) |
| `scripts/anytype-api-test.sh` | API CRUD smoke test script |
| `PROJECT_STATE.md` | This file |

---

## 5. Next Steps (Architecture Phase Map)

### Phase 0 — Foundation ✅ DONE
Working AnyType ↔ OpenCode MCP connection. Object CRUD verified.

### Phase 1 — PDF Pipeline (NEXT)
- Ingest PDF → Docling extraction
- Query OpenAlex by DOI
- Create AnyType `Paper` and `Author` objects
- Store PDF locally, link path in object

### Phase 2 — Citation Graph
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
```

---

*Last updated: 2026-05-31 by OpenCode*
