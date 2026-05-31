# Transdisciplinary Action Research Assistant (TARA)
## Architecture Document — AnyType as User Interface Layer

**Version**: 0.1  
**Date**: 2026-05-31  
**Author**: Dr. Bradley Vener  
**Status**: Draft for evaluation

---

## 1. Executive Summary

This document proposes an architecture for a **Transdisciplinary Action Research Assistant (TARA)** — a system that supports the design of interventions into real-world systems, grounded in Werner Ulrich's vision of "a practicable, although necessarily imperfect, model of practical discourse."

The architecture is **layered and modular**. **AnyType serves as the human-facing structured workspace and knowledge graph**. Heavy computation — PDF extraction, citation graph traversal, semantic search, and system modeling — lives in dedicated local-first tools outside AnyType. Outputs are synced into AnyType as typed objects with relations, making them explorable and editable by human researchers.

**Core principle**: AnyType is the UI layer, not the compute backend.

---

## 2. Context & Goals

### 2.1 Transdisciplinary Action Research (TARA)

Action research is cyclical: **plan → act → observe → reflect**. Transdisciplinary research crosses disciplinary boundaries and involves stakeholders beyond academia. The output is not just knowledge but **designed interventions** into complex systems.

### 2.2 Werner Ulrich's Practical Discourse

Ulrich's Critical Systems Heuristics (CSH) provides a framework for "boundary critique" — surfacing the hidden boundary judgments that determine what counts as relevant fact and value in any intervention. The 12 boundary questions (answered in both "is" and "ought" modes) are the methodological core.

The long-term goal is software support for this reflective practice: an assistant that helps researchers (a) surface boundary judgments, (b) model systems, (c) design interventions, and (d) track cycles of action and reflection.

### 2.3 Near-Term Goal

Support a small number of developers (starting with one) working to design this system. The immediate concrete deliverable is a **PDF processing pipeline and citation graph** to support academic research feeding into intervention design.

### 2.4 Role of AnyType

AnyType is evaluated as the **primary interface between the user and the LLM-based research agent**. Its object-oriented graph structure is well-suited to modeling research artifacts (papers, authors, projects, interventions) and relations between them. Its local-first, encrypted model aligns with research sovereignty. Its API and MCP server allow programmatic population from agent outputs.

---

## 3. Component Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERFACE LAYER                        │
│  ┌──────────────┐  ┌─────────────────┐  ┌────────────────┐  │
│  │   AnyType    │  │  OpenCode CLI   │  │  Zotero (cite) │  │
│  │  (Knowledge  │  │  (Agent command │  │  (Reference    │  │
│  │   graph,     │  │   & skill invoc)│  │   management)  │  │
│  │   projects)  │  │                 │  │                │  │
│  └──────┬───────┘  └─────────────────┘  └────────────────┘  │
└─────────┼─────────────────────────────────────────────────────┘
          │ MCP / REST
┌─────────┼─────────────────────────────────────────────────────┐
│         ▼         AGENT ORCHESTRATION LAYER                  │
│  ┌─────────────────────────────────────────────────────┐     │
│  │              OpenCode + Custom Skills               │     │
│  │  • autoresearch skill (bootstrap→inner→outer→finalize)│   │
│  │  • CSH boundary-critique skill (future)             │     │
│  │  • intervention-design skill (future)                 │     │
│  └────────────────────┬──────────────────────────────────┘     │
│                     │ MCP multiplexing                       │
└─────────────────────┼─────────────────────────────────────────┘
                      │
┌─────────────────────┼─────────────────────────────────────────┐
│         ▼           │           TOOL & DATA LAYER              │
│  ┌──────────────────┴─────────────────────────────────────┐  │
│  │  MCP Server Mesh (via AgentGateway or direct config)   │  │
│  │  ┌─────────────┐ ┌──────────────┐ ┌─────────────────┐ │  │
│  │  │ AnyType MCP │ │ OpenAlex MCP │ │  Custom PDF MCP │ │  │
│  │  │  (objects)  │ │ (citations)  │ │  (extraction)   │ │  │
│  │  └─────────────┘ └──────────────┘ └─────────────────┘ │  │
│  └────────────────────────────────────────────────────────┘  │
│                                                               │
│  ┌──────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │ OpenAlex API │  │  Docling/Marker │  │  Local Graph    │  │
│  │  (remote +  │  │  (PDF→Markdown  │  │  Store (Kùzu/   │  │
│  │   local snap)│  │   + structure)  │  │   SQLite)       │  │
│  └──────────────┘  └─────────────────┘  └─────────────────┘  │
└───────────────────────────────────────────────────────────────┘
```

### 3.1 Layer Responsibilities

| Layer | Components | Responsibility |
|---|---|---|
| **User Interface** | AnyType Desktop App, OpenCode CLI, Zotero | Human exploration, agent invocation, reference capture |
| **Agent Orchestration** | OpenCode + custom skills | Research lifecycle management, boundary critique prompting, synthesis |
| **MCP Server Mesh** | AnyType MCP, OpenAlex MCP, custom MCPs | Protocol bridges between agents and tools |
| **Tool & Data** | OpenAlex, Docling, Marker, Kùzu/SQLite, local LLMs | Computation: citation graphs, PDF extraction, graph queries, inference |

---

## 4. Component Evaluation

| Component | Role | Pros | Cons | Verdict |
|---|---|---|---|---|
| **AnyType** | User-facing knowledge graph, project tracker, intervention workspace | Local-first, E2E encrypted, rich types/relations, collections, file storage, human-readable | Rate limited (1rps sustained, burst 60), no semantic search, body updates recreate object, no server-side graph queries, requires desktop app or CLI running | **Use as UI layer**, not primary compute store |
| **AnyType CLI** | Headless API server (port 31012) | Bot accounts, isolated from personal vault, ~512MB RAM, systemd service, same API as desktop | New (v0.3.2), bot accounts only (no mnemonic login), gRPC ports hardcoded | **Primary automation backbone** |
| **OpenCode + autoresearch skill** | Agent orchestration, research lifecycle manager | Already in use, skill system exists, MCP support, manual invocation matches action research reflexivity | Skills are editor-bound, no persistent agent memory across sessions | **Extend with new skills**, keep as orchestrator |
| **OpenAlex (API + local)** | Global citation graph, paper metadata, author disambiguation | 450M+ works, CC0, free API, local snapshot available, MCP server exists, abstracts for ~50% | $1/day API limit, snapshot is 200GB+, no full text for most | **Primary citation backbone** |
| **Docling** | PDF→structured text extraction | MIT license, CPU-friendly, preserves tables/structure, `DoclingDocument` programmable, MCP server exists | Slower than MarkItDown on clean PDFs, ~600MB models | **Primary PDF extractor** |
| **Marker** | PDF→markdown (math-heavy) | Best LaTeX/equation handling, high accuracy on academic papers | GPL-3.0 + custom model license, GPU-hungry, slow on CPU | **Secondary/academic specialization** |
| **Zotero** | Personal reference library, citation generation | Mature, Better BibTeX, browser connector, group libraries | Not local-first, no graph view, no API (needs bridge) | **Keep for capture & CSL export; bridge to AnyType** |
| **Kùzu / SQLite** | Local citation/entity graph | Fast graph queries, embeddable, SotAScope proven pattern (SQLite) | Another datastore to maintain | **Start with SQLite** (SotAScope model works), migrate to Kùzu if graph queries become bottleneck |

---

## 5. AnyType Data Model

The following custom types and relations are proposed for TARA. They map academic research artifacts and action research concepts to AnyType's object-oriented structure.

### 5.1 Custom Types

| Type | Key Properties | Purpose |
|---|---|---|
| **Paper** | Title, DOI, Year, Venue, Abstract, OpenAlex ID, Local PDF Path, Ingestion Date | Academic paper as primary research artifact |
| **Author** | Name, ORCID, Affiliation, H-Index | Disambiguated researcher |
| **Project** | Title, Description, Status, Start Date, End Date | A research or intervention project |
| **Research Question** | Question Text, Domain, Priority, Status | Driving question for a project |
| **Intervention** | Title, Target System, Status, Cycle Count | A designed intervention into a real-world system |
| **Stakeholder** | Name, Role, Group, Contact | Person or group affected by or involved in an intervention |
| **Boundary Judgment** | Dimension (CSH 1-12), Is Answer, Ought Answer, Source Claim | Documented boundary critique output |
| **Observation** | Date, Context, Data, Reflection | Action research observation from a cycle |
| **System Model** | Name, Description, Type (causal loop, stock-flow, etc.), File | Formal or informal model of a system |

### 5.2 Key Relations

| Relation | From → To | Semantics |
|---|---|---|
| **authored_by** | Paper → Author | Paper written by author |
| **cites** | Paper → Paper | Directed citation |
| **related_to** | Paper → Paper | Semantic or topical relation (non-citation) |
| **belongs_to** | Paper → Project | Paper is part of a project's literature base |
| **addresses** | Project → Research Question | Project aims to answer this question |
| **designs** | Project → Intervention | Project outputs this intervention |
| **affects** | Intervention → Stakeholder | Stakeholder is affected by intervention |
| **involves** | Intervention → Stakeholder | Stakeholder is involved in designing intervention |
| **informs** | Boundary Judgment → Intervention | Boundary critique informs this intervention |
| **models** | System Model → Intervention | Model represents system this intervention targets |
| **observed_during** | Observation → Intervention | Observation collected during this intervention cycle |

### 5.3 Collections (Sets)

- **Literature Review** — all Papers in a Project
- **Citation Network** — Papers linked by `cites`
- **Active Interventions** — Interventions with status "in progress"
- **Boundary Critique Log** — Boundary Judgments grouped by Intervention
- **Stakeholder Map** — Stakeholders linked to an Intervention

---

## 6. Data Flows

### 6.1 Near-Term: PDF Processing & Citation Pipeline

```
PDF (drop / Zotero)
    │
    ▼
┌─────────────────┐
│ Docling (CPU)   │ → Structured Markdown + JSON metadata
│ or Marker (GPU) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Metadata Extract  │ → DOI, title, authors
│ (regex / header)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ OpenAlex API      │ → Work ID, references, cited_by, abstract
│ (or local snap)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Local Graph Store │ → Paper/Author/Citation nodes & edges
│ (SQLite / Kùzu)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ AnyType Sync Agent│ → Creates/updates AnyType objects
│ (respects 1rps)   │    Paper, Author, Citation relations
└─────────────────┘
```

### 6.2 Long-Term: Action Research / Intervention Design

```
Intervention Proposal
    │
    ▼
┌──────────────────────────┐
│ CSH Boundary Critique Skill│ → 12 boundary questions (is/ought)
│ (OpenCode custom skill)    │    structured Boundary Judgment objects
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ System Modeling Tools      │ → Causal loop diagrams, stock-flow
│ (external or agent-built)  │    stored as System Model objects
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│ AnyType Workspace          │ → Intervention, Stakeholder, Boundary
│                            │    Judgment, System Model linked
└────────┬─────────────────┘
         │
         ▼
Plan → Act → Observe → Reflect cycles
    │
    ▼
Each cycle creates: Observation objects
                     linked to Intervention
                     with date, data, reflection
```

---

## 7. Critical Gaps & Risks

| Gap | Risk | Mitigation |
|---|---|---|
| AnyType API rate limits (1rps sustained, burst 60) | Bulk imports of large citation graphs are slow | Batch via script with sleeps; use local graph store for analysis, only sync summaries to AnyType |
| No semantic search in AnyType | Cannot find semantically similar papers inside AnyType | Semantic search lives in OpenAlex-local or custom vector DB; AnyType stores OpenAlex IDs as properties |
| AnyType requires desktop app or CLI running | Headless automation needs a service | Use `anytype-cli` as systemd service (port 31012); bot accounts are isolated |
| No block-level API editing | Fine-grained updates to long research notes are clunky | Keep notes as smaller atomic objects; use Markdown body for final reports only |
| CSH has no software implementation | Boundary critique is manual | Build as OpenCode skill using Ulrich's 12 questions as structured prompt template |
| Bobrik / AI Ally is alpha-only | Native AnyType agent not ready | Use MCP-based external agents (OpenCode, Claude) via `anytype-cli` API for now |
| `anytype-cli` is new (v0.3.2) | API may change, bugs possible | Pin version in devenv, follow releases, contribute issues upstream |

---

## 8. Implementation Phases

| Phase | Deliverable | Components | Est. Effort |
|---|---|---|---|
| **0: Foundation** | Working AnyType ↔ OpenCode MCP connection | Install `anytype-cli` as service, configure AnyType MCP in OpenCode, verify object CRUD | 1 day |
| **1: PDF Pipeline** | PDF ingestion → Docling → AnyType paper objects | Docling wrapper script, define AnyType `Paper`/`Author` types, test on sample PDFs | 2–3 days |
| **2: Citation Graph** | Local OpenAlex + graph queries → AnyType collections | OpenAlex MCP or local snapshot, SQLite graph schema, sync agent | 3–5 days |
| **3: Research Agent Integration** | OpenCode autoresearch outputs structured objects to AnyType | Extend autoresearch skill to emit AnyType objects; project-based collections | 3–5 days |
| **4: Action Research** | CSH boundary critique skill, intervention types in AnyType | Custom skill for 12 boundary questions; AnyType types for interventions, stakeholders, observations | 5–7 days |

---

## 9. Tradeoff Decisions & Recommendations

### 9.1 Graph Store: Kùzu vs SQLite

**Recommendation: Start with SQLite**.

The SotAScope project proves SQLite handles academic citation graphs well (FastAPI + SQLAlchemy + SQLite WAL). Kùzu is faster for complex graph traversals but adds a dependency. Migrate if query patterns demand it.

### 9.2 PDF Extractor: Docling vs Marker vs Both

**Recommendation: Docling primary, Marker conditional.**

Docling is MIT-licensed, CPU-friendly, and preserves structure well. Its `DoclingDocument` intermediate representation is programmatically useful. Marker is superior for LaTeX/math-heavy papers but is GPL-3.0 with a custom model license and needs GPU. Use a router: Docling by default, Marker only for detected academic PDFs with heavy math.

### 9.3 AnyType Sync Direction

**Recommendation: Mostly one-way (compute → AnyType) with selective bidirectional links.**

User tags and manual annotations in AnyType can propagate back to the local graph. Bulk citation data and agent outputs flow into AnyType. This avoids rate limit pain and data model mismatches.

### 9.4 MCP Strategy: Direct vs Multiplexed Gateway

**Recommendation: Direct to start.**

Configure AnyType MCP, OpenAlex MCP, and custom PDF MCP directly in OpenCode. Add AgentGateway or Composio-style gateway only if server sprawl becomes unmanageable (likely after Phase 3+).

---

## 10. Related Projects & Prior Art

| Project | Relevance | URL |
|---|---|---|
| **Orchestra Research AI-Research-SKILLs** | Two-loop autonomous research architecture; basis for autoresearch skill | github.com/Orchestra-Research/AI-research-SKILLs |
| **SotAScope** | Local-first citation graph dashboard; SQLite + FastAPI + React pattern | github.com/jonkro/SotAScope |
| **OpenAlex Local** | 284M-work local database with semantic search | github.com/ywatanabe1989/openalex-local |
| **AnyType Mind** | AnyType + Claude Code structured brain; lifecycle hooks and subagents | github.com/imcvampire/anytype-mind |
| **AnyType MCP Server** | Official MCP bridge; converts OpenAPI to MCP tools | github.com/anyproto/anytype-mcp |
| **AnyType MCP Plus** | Enhanced community MCP with 34 tools, bug fixes | github.com/MAB2908/anytype-mcp-plus |
| **Docling** | IBM's MIT-licensed PDF→structured text extractor | github.com/docling-project/docling |
| **Marker** | Datalab's accuracy-first PDF→markdown converter | github.com/datalab-to/marker |
| **OpenAlex MCP Server** | MCP server for scholarly database search and citation traversal | github.com/SMABoundless/openalex-mcp-server |
| **Agent-Tektology** | Coalgebraic formalization of agent-organization coupling (Brad's own) | ~/Projects/agent-tektology |

---

## 11. Appendices

### A. AnyType API Endpoints Relevant to TARA

| Endpoint | Purpose | Limitation |
|---|---|---|
| `POST /v1/auth/challenges` | Generate auth challenge for API key | Requires desktop app or CLI running |
| `POST /v1/auth/api_keys` | Obtain bearer token | One-time pairing per client |
| `GET /v1/spaces` | List spaces | Bot account only sees joined spaces |
| `POST /v1/spaces` | Create new space | — |
| `GET /v1/spaces/{id}/types` | List custom types | — |
| `POST /v1/spaces/{id}/types` | Create custom type | Key must be camelCase, unique |
| `GET /v1/spaces/{id}/objects` | List objects (paginated) | Dynamic filtering experimental |
| `POST /v1/spaces/{id}/objects` | Create object | Body is Markdown; properties in request |
| `PATCH /v1/spaces/{id}/objects/{id}` | Update object | Body update recreates object (new ID) |
| `POST /v1/search` | Global search across spaces | Matches name + snippet only; no semantic |
| `POST /v1/spaces/{id}/lists/{id}/objects` | Add object to collection | — |

### B. CSH Boundary Questions (Ulrich, 1983)

Twelve boundary categories across four dimensions:

1. **Sources of motivation** — Who ought to be the beneficiary? Who is?
2. **Sources of power** — Who ought to be involved? Who is?
3. **Sources of knowledge** — Who ought to be considered competent? Who is?
4. **Sources of legitimation** — Who ought to be the guarantor? Who is?
5. **System boundaries** — What is the relevant whole? What is considered?
6. **Environment boundaries** — What is the relevant environment? What is considered?
7. **Context of application** — What is the context of responsible action? What is assumed?
8. **Universe of discourse** — What is the total conceivable universe? What is assumed?
9. **Stakeholder stakes** — What improvements ought to be sought? What is sought?
10. **Stakeholding issues** — What risks ought to be taken? What are taken?
11. **Decision environment** — What guarantees ought to be given? What are given?
12. **Planning concerns** — What worldviews ought to be considered? What are considered?

Each question is answered in **"is"** mode (actual) and **"ought"** mode (ideal). Differences reveal boundary judgments to critique.

---

*End of document*
