# Eliminating the AnyType Dependency

## Relational Metadata Backbone for TARA

**Status:** Draft for review — 2026-08-23
**Companion to:** `anytype-based-tara/research-assistant-architecture.md`
**Scope:** Replace the AnyType dependency with a SQLite-first metadata system; migrate existing data; decommission AnyType plumbing. Build on the existing `scripts/lib/graph_store.py` SQLite store (the relational metadata system the current architecture already uses behind AnyType).

---

## 1. Executive summary

AnyType currently plays two roles in TARA: (1) the **metadata store** for research artifacts (papers, authors, projects, experiments) and relations, and (2) the **human interface** (typed graph, collections, multi-device sync, bot status updates). Role (1) is already duplicated by the local SQLite graph store (`scripts/lib/graph_store.py`) — AnyType and SQLite both hold Paper/Author/citation data today, which is drift waiting to happen. Role (2) is valuable but comes at the cost of a headless service to run, a 1 req/sec API rate limit, no server-side graph queries, and a closed data format.

**This plan makes SQLite the single source of truth for metadata**, extends its schema to cover every object type AnyType currently holds (projects, experiments, interventions, stakeholders, boundary judgments, observations, system models), replaces the interface role with git + (optionally) a local web dashboard, migrates existing data, and removes all AnyType plumbing. Git becomes the sync engine — which aligns with the repository now being on GitHub with the cappuccinocosmico collaborator.

**Net effect:** one queryable, versionable, diffable metadata store; no background service; no rate limits; git-native collaboration; and a clean migration path that can run with AnyType still in place until verified.

---

## 2. Why — and what AnyType actually provides today

### 2.1 Problems the current design has

- **Two sources of truth.** `ingest_pdf.py` and `build_citation_graph.py` write papers/authors to *both* SQLite and AnyType. Every ingest is two writes; every schema change is two changes; every miss (failed AnyType write, rate-limit error, PATCH body-recreates-object) silently forks the two stores.
- **A service to babysit.** `anytype-cli` must be running (systemd/devenv, ~512 MB RAM, port 31012) or every script fails at `_resolve_space_id()`.
- **A 1 req/sec bottleneck.** Bulk operations (citation sync, project listing) are throttled by the rate limiter built into `anytype_client.py`.
- **No server-side graph queries.** Network traversal happens client-side against paginated `list_objects` calls; the SQLite store already does this properly and fast.
- **Dead `.env` loader.** `ingest_pdf.py`, `build_citation_graph.py`, `research_project.py`, and `sync_research_to_anytype.py` all attempt to load a `.env` file that PROJECT_STATE.md records as deleted (replaced by `.enc.env` via direnv). Dead code, silently no-op.
- **Secrets surface.** Bot account ID and space ID are committed in `PROJECT_STATE.md` on a now-**public** repo. Decommissioning AnyType removes the sensitive surface (the token itself is already SOPS-encrypted).

### 2.2 Inventory of what AnyType provides (must be replaced, not just removed)

| Capability | Where it lives today | Replacement |
|---|---|---|
| Paper / Author / citation metadata | `anytype_client.py` + SQLite (duplicated) | SQLite only (exists) |
| Browseable typed graph + collections | AnyType Desktop UI | local web dashboard (optional, Phase 4) or SQL |
| Project object (research overview) | `Project: {title}` objects | `projects` table + existing markdown workspace (git) |
| Experiment objects | `Experiment: {title}` objects | `experiments` table + existing `experiments/<slug>/` dirs |
| Action-research types (Intervention, Stakeholder, BoundaryJudgment, Observation, SystemModel) | planned AnyType custom types (Phase 4 of old roadmap, not built) | `interventions`, `stakeholders`, `boundary_judgments`, `observations`, `system_models` tables |
| Status updates / notifications | `Status Update` objects | `status_updates` table + `research-log.md`/`to_human/` notes (already the convention) |
| Multi-device sync | AnyType native Vault/Channel sync | git (GitHub); optional Syncthing/WebDAV if phone access is required |
| Citation import/export | — | add `--export-bibtex` to `build_citation_graph.py` |

---

## 3. Target architecture

```
┌─────────────────────────────────────────────────────────┐
│  MARKDOWN WORKSPACES (git)                              │
│  projects/<slug>/  research-state.yaml, findings.md,    │
│  research-log.md, literature/*.md, experiments/<slug>/   │
└─────────────────────────┬───────────────────────────────┘
                          │ ingest / sync (scripts)
┌─────────────────────────▼───────────────────────────────┐
│  RELATIONAL METADATA CORE — SQLite (data/tara_graph.db) │
│  papers · authors · paper_authors · citations           │
│  projects · experiments · interventions · stakeholders  │
│  boundary_judgments · observations · system_models      │
│  links (generic relation edges) · status_updates        │
└─────────────────────────┬───────────────────────────────┘
                          │ queries
          ┌───────────────┴───────────────┐
   ┌──────▼──────┐   ┌───────────────┐   ┌▼─────────────────┐
   │ sqlite3 CLI │   │ script CLIs   │   │ web dashboard    │
   │ / opencode  │   │ (ingest,      │   │ (optional,       │
   │ read tools  │   │  graph,       │   │  FastAPI+SQLAlch │
   │             │   │  project)     │   │  SotAScope-style)│
   └─────────────┘   └───────────────┘   └──────────────────┘
```

**Principles:**
- SQLite is the **single source of truth**; markdown workspaces are the human-editable source that sync *into* it (one direction). This matches how the RET×TSSI project already works (markdown in git + this DB for query).
- No background service. Scripts open the DB, do work, close it.
- git (GitHub) is the sync/distribution engine; the repository is already shared with the collaborator.
- The `data/` directory stays gitignored (runtime artifact); schema ships in code (`graph_store.py`) and changes go through git like any code.

---

## 4. The relational schema (extension of `graph_store.py`)

### 4.1 Existing core (unchanged)

`papers`, `authors`, `paper_authors`, `citations` — plus indexes. Only change: **drop the `anytype_id` columns** from `papers` and `authors` after migration (§5).

### 4.2 New catalog tables

```sql
CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    question TEXT,
    domain TEXT,
    status TEXT DEFAULT 'active',
    started TEXT,
    workspace_path TEXT UNIQUE,        -- projects/<slug>/
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE experiments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    slug TEXT NOT NULL,                -- experiments/<slug>/
    hypothesis TEXT,
    status TEXT DEFAULT 'pending',
    proxy_metric TEXT,
    protocol_path TEXT,
    results_path TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (project_id, slug)
);
```

### 4.3 New action-research tables

```sql
CREATE TABLE interventions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    target_system TEXT,
    status TEXT DEFAULT 'proposed',
    cycle_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE stakeholders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    role TEXT,
    group_name TEXT,
    contact TEXT
);

CREATE TABLE intervention_stakeholders (
    intervention_id INTEGER NOT NULL REFERENCES interventions(id) ON DELETE CASCADE,
    stakeholder_id INTEGER NOT NULL REFERENCES stakeholders(id) ON DELETE CASCADE,
    relation TEXT DEFAULT 'involves',  -- 'involves' | 'affects'
    PRIMARY KEY (intervention_id, stakeholder_id)
);

CREATE TABLE boundary_judgments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    intervention_id INTEGER NOT NULL REFERENCES interventions(id) ON DELETE CASCADE,
    dimension INTEGER NOT NULL,        -- 1..12 CSH boundary question
    is_answer TEXT,
    ought_answer TEXT,
    source_claim TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE observations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    intervention_id INTEGER NOT NULL REFERENCES interventions(id) ON DELETE CASCADE,
    date TEXT,
    cycle INTEGER,
    context TEXT,
    data TEXT,
    reflection TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE system_models (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    model_type TEXT,                   -- 'causal loop' | 'stock-flow' | ...
    file_path TEXT
);

CREATE TABLE intervention_models (
    intervention_id INTEGER NOT NULL REFERENCES interventions(id) ON DELETE CASCADE,
    model_id INTEGER NOT NULL REFERENCES system_models(id) ON DELETE CASCADE,
    PRIMARY KEY (intervention_id, model_id)
);
```

### 4.4 Generic links + activity

AnyType's loose `relations` (authored_by, belongs_to, addresses, designs, ...) map naturally onto a single typed edge table so new relation types don't require migrations:

```sql
CREATE TABLE links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    predicate TEXT NOT NULL,           -- e.g. 'belongs_to', 'addresses', 'informs'
    subject_type TEXT NOT NULL,
    subject_id INTEGER NOT NULL,
    object_type TEXT NOT NULL,
    object_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (predicate, subject_type, subject_id, object_type, object_id)
);

CREATE TABLE status_updates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER REFERENCES projects(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    kind TEXT DEFAULT 'info',          -- 'progress' | 'findings' | 'request' | ...
    summary TEXT,
    detail TEXT
);
```

The paper↔project relation is `links(predicate='belongs_to', subject=papers)`. Strongly-typed join tables are preferred where relations are load-bearing (papers↔authors, interventions↔stakeholders); the generic `links` table covers everything else, matching AnyType's flexibility without schema churn.

### 4.5 Versioning

Add `PRAGMA user_version` and a small migration runner in `graph_store.py` so schema bumps are applied deterministically (this is the natural place for the "metadata system" to grow over time).

---

## 5. Data migration

Target state: SQLite contains everything metadata-worthy that currently lives in AnyType; AnyType becomes read-only, then headless.

1. **Write `scripts/export_anytype.py`** (one-shot, run while `anytype-cli` is still up):
   - `list_objects` in pages (respecting the 1 rps limiter), classify by name prefix: `Paper:` / `Author:` / `Project:` / `Experiment:` / others.
   - Papers & Authors → `graph.add_paper()` / `graph.add_author()` (dedup against what SQLite already has — `_find_paper` handles DOI/arXiv/title).
   - Projects & Experiments → insert into new tables, extracting metadata from the object body (title, question, status, started, domain) and mapping workable values from `research-state.yaml` when a matching workspace exists.
   - Emit `data/anytype-export-<date>.md` (all object bodies) as a human-readable safety net.
   - **Dry-run first**, report counts (`papers`, `authors`, `projects`, `experiments`, `others`).
2. **Verify**: compare row counts; spot-check three objects per type in SQLite against the AnyType source.
3. **Stop AnyType writes**: set the pipeline scripts to graph-only (Phase 2).
4. **Drop `anytype_id` columns** once export is verified and the CLI is decommissioned.
5. **Rotate/deactivate** the `tara-bot` account + API key once AnyType is fully removed (they are no longer needed; the account ID/space ID in `PROJECT_STATE.md` on a public repo make rotation the right call).

---

## 6. Code impact map

### Modify

| File | Change |
|---|---|
| `scripts/lib/graph_store.py` | Add new tables (§4.2–4.5) + ops for projects/experiments/interventions/etc.; schema versioning; drop `anytype_id` columns |
| `scripts/ingest_pdf.py` | Remove all AnyType imports/paths (`find_existing_paper`, `create_author_objects`, AnyType object creation); duplicate detection via SQLite only; add `--project <slug>` to link paper to a project; remove stale `.env` loader; keep graph write, PDF move, metadata embed |
| `scripts/build_citation_graph.py` | Drop `--init` (AnyType source), `--sync-anytype`, `--all`; keep `--enrich`, `--stats`; add `--export-bibtex` |
| `scripts/research_project.py` | `create`: register project row in SQLite instead of AnyType object; keep workspace scaffolding. `status`: read `research-state.yaml` + SQLite. `list`: SQLite. `sync`: point at successor script |
| `scripts/sync_research_to_anytype.py` | **Rewritten** → `scripts/sync_research_project.py`: catalog project + experiments + literature papers (with `links` edges) into SQLite; regenerate a derived `PROJECT_INDEX.md`; no AnyType objects |

### Delete

| File | Reason |
|---|---|
| `scripts/lib/anytype_client.py` | AnyType REST client no longer needed |
| `scripts/anytype-api-test.sh` | Smoke test against dead service |
| `anytype-mcp-wrapper.sh` | AnyType MCP bridge |
| `opencode.jsonc` → `mcp.anytype` block | MCP server goes away |
| `package.json` → anytype-mcp dependency | node module; remove via `npm uninstall` |
| `.enc.env` → `ANYTYPE_*` keys | no secrets left to hold (keep rclone/S3 keys) |
| `devenv.nix` → anytype-cli service/config | service gone |
| `PROJECT_STATE.md` references | update checklist + quick commands |

### Optional (Phase 4)

- `app/` — FastAPI + SQLAlchemy read-only dashboard (SotAScope pattern from the architecture doc §9.1), browsing the same SQLite file via `sqlite:///data/tara_graph.db` with WAL.
- Rename `anytype-based-tara/` (historical folder name) — cosmetic, defer.

---

## 7. Interface & sync replacement

- **Human exploration:** until a dashboard exists, the `sqlite3` CLI and opencode's read tools query the DB directly; all long-form content stays in git-tracked markdown (rendered by GitHub for the collaborator).
- **Multi-device:** git. This is already the only sync mechanism the research workspaces use once the repo is shared. If phone/tablet read access is genuinely needed, add Syncthing later — flagged as a decision, not assumed.
- **Status updates:** autoresearch already writes `research-log.md` + `to_human/` notes (the RET×TSSI project does exactly this). A `status_updates` table is available for programmatic events (e.g., experiment completions) surfaced by the future dashboard.

---

## 8. Implementation phases

| Phase | Deliverable | Est. effort |
|---|---|---|
| **0: Freeze & export** | `export_anytype.py` (dry-run + run), verify counts, commit. From here AnyType is read-only reference only | 1 day |
| **1: Schema** | `graph_store.py` extended (catalog + action-research + links + status_updates + versioning); smoke test against a copy of the DB | 1–2 days |
| **2: Script refactor** | `ingest_pdf.py`, `build_citation_graph.py`, `research_project.py` de-AnyTyped; `sync_research_project.py` written; remove stale `.env` loaders | 2–3 days |
| **3: Decommission** | Delete AnyType client/wrapper/test/MCP config/dep/secrets; update `PROJECT_STATE.md`; commit removals | 0.5 day |
| **4: UI & extras** | Optional FastAPI dashboard; `--export-bibtex`; S3 backup now covers SQLite + `papers/` (drop vault backup); rename `anytype-based-tara/` if desired | 3–5 days |

Total ≈ **7–11 days**. Phases 0–3 are sequential; 4 is independent. Phase 0 is safe to run today — AnyType stays intact until Phase 3.

---

## 9. Risks & mitigations

| Risk | Mitigation |
|---|---|
| Data loss in migration | Export to a fresh DB copy first; keep AnyType running until Phase 3 verified; emit markdown dumps as fallback |
| Lost graph-exploration UX | SQLite is queryable now; optional dashboard in Phase 4 with zero impact on data |
| Lost native mobile sync | Decide explicitly (§7); git-first, add Syncthing only if mobile read access is required |
| Secrets in public repo | Remove `.env`/AnyType tokens; rotate tara-bot account/key at decommission; verify `.env` was never in git history (`git log --all -- .env`) |
| `.dec.env` edits during transition | Only `ANYTYPE_*` keys removed; rclone/S3 credentials untouched |
| `data/` DB lost | gitignored on purpose; `backup-to-s3.sh` extended to include `data/tara_graph.db` (+ `papers/`) |

---

## 10. Decisions requested

1. **Project workspaces in git?** `projects/*` is currently ignored except RET×TSSI. For the collaborator experience, track each project's markdown workspace (state/log/findings/literature) — or keep workspaces local and share only the DB exports?
2. **Mobile access** required, or is git + desktop enough?
3. **Public repo** is intended for this research-sharing use case?
4. Build the **Phase 4 dashboard** now or defer?
5. **Rename** `anytype-based-tara/` after decommission?

---

*Companion: `anytype-based-tara/research-assistant-architecture.md` (superseded in its data-layer/interface sections by this plan).*