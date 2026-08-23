# An Explicit Knowledge Repository for the opencode Research Assistant

**Proposal** — draft for review, 2026-08-23
Author: Bradley Vener (with opencode)
Status: rethink of TARA's knowledge/metadata layer; supersedes the AnyType-elimination and relational-schema direction

**Recorded decisions (2026-08-23):**
1. **plumbing/AGPL-3.0 accepted for now.** Long-term interest in a strongly-typed-language alternative with multi-party session types built in (plumbing is OCaml, typed, but session types are declared/checked, not a native multi-party construct); gaining fluency with plumbing precedes that evaluation.
2. **Phase A scope approved:** proof of concept on the RET×TSSI corpus (~68 docs).
3. **Extraction starts co-occurrence-only.** Phase A builds statistical hyperedges (co-occurring concepts/sections, verifiable, deterministic); LLM relation-typing is enrichment deferred until fidelity is measured.

---

## 1. Framing: the gap this fills

opencode is a strong **agent harness**: session-scoped model context, per-project `AGENTS.md`, a skill system (including the autoresearch lifecycle), MCP support. What it lacks is the thing the last several design efforts kept circling: an **explicit, persistent, queryable knowledge repository** — a first-class artifact that agents read from, write to, and reason over, independent of any model's latent knowledge and inspectable by a person (and a collaborator) at any time.

Three prior attempts, three mismatches:

| Attempt | What it was | Why it didn't stick |
|---|---|---|
| AnyType | Proprietary typed-graph/store + UI + sync | Heavy service, 1 rps API, closed format, dual-store drift, being eliminated |
| Hand-rolled relational (SQLite) | `papers/authors/citations` + plans | Reduplicated a global graph OpenAlex already owns; the relations layer duplicated; schema grew awkward |
| OpenAlex | Global bibliographic graph (works/authors/citations) | Correct for *bibliographic* ground truth, but cannot hold our own entities or higher-order relations |

The common failure is treating "the knowledge base" as a *store to be filled*. This proposal treats it as a **derived structure**: an explicit hypergraph of the research corpus, built automatically by a knowledge-engineering pipeline, coordinated by typed pipelines, and retained in version control.

### Why hypergraphs, not a pairwise graph

Transdisciplinary (wicked) problems are exactly the cases where multi-entity interactions are irreducible to pairs: a mechanistic claim, an intervention+stakeholder+outcome triple, a value-price-flux nexus. Pairwise knowledge graphs force combinatorial pairwise expansions and lose the co-occurrence context. HyperGraphReasoning preserves n-ary relations natively and, on a ~1,100-paper corpus, produced a scale-free hypergraph (power law ~1.23) whose hyperedge intersections gave agents grounded reasoning pathways — e.g. linking cerium oxide to PCL scaffolds via a chitosan intermediate. That is the *shape* of reasoning this research environment needs.

---

## 2. Design principles

1. **Explicit over implicit.** The knowledge structure is written down, drawn, and type-checked — not latent in prompts, callback code, or orchestration scripts. (This is plumbing's stated thesis; adopted wholesale.)
2. **Existing solutions first, open source only.** OpenAlex (CC0), HyperGraphReasoning (Apache-2.0), plumbing (AGPL-3.0), opencode (open core). No proprietary store.
3. **Bibliographic truth lives in OpenAlex.** We never rebuild the citation graph ourselves; we point at it.
4. **Our knowledge is versioned.** Hypergraph artifacts and pipeline definitions live in git (already shared with the collaborator), so the knowledge base is diffable and reproducible.
5. **The research program is the testbed.** The RET×TSSI corpus (already ~68 documents in this repo) is the first corpus.

---

## 3. Proposed architecture

```
                    ┌─────────────────────────────────────────────┐
                    │              HUMAN + COLLABORATOR          │
                    │          (git / GitHub / terminal / docs)  │
                    └───────────────┬─────────────────────────────┘
                                    │
        ┌───────────────────────────▼──────────────────────────────┐
        │              OPENCODE — AGENT HARNESS (unchanged)        │
        │  sessions · AGENTS.md · skills (autoresearch) · MCP      │
        └───────┬───────────────────────────────▲──────────────────┘
                │ MCP (plumb-mcp exposes        │ MCP (agents call
                │  pipelines as tools)          │  tools / traversal)
        ┌───────▼───────────────────────────────┴──────────────────┐
        │          PLUMBING — COORDINATION (typed pipelines)       │
        │  ingest · transform · query · review · verify            │
        │  session-typed JSON across channel boundaries            │
        └───────┬───────────────────────────────▲──────────────────┘
                │ writes/fetch                   │ queries
        ┌───────▼───────────────────────────────┴──────────────────┐
        │  KNOWLEDGE REPOSITORY (explicit, versioned artifacts)    │
        │  ┌─────────────────────────┐  ┌───────────────────────┐  │
        │  │ HYPERGRAPH  (HYPERNETX)│  │  OPENALEX             │  │
        │  │ nodes · hyperedges ·   │  │  bibliographic truth  │  │
        │  │ embeddings · metadata  │  │  (+ optional local    │  │
        │  │  (git-versioned files) │  │   openalex-local)     │  │
        │  └─────────────────────────┘  └───────────────────────┘  │
        └──────────────────────────────────────────────────────────┘
                    Automated knowledge engineering: PDFs/markdown
                    → extraction (schema) → hyperedges → embeddings
```

**Three layers:**

- **Harness — opencode.** Unchanged. It consumes MCP tools and keeps session memory; long-form thought stays in git-tracked markdown workspaces (the existing convention).
- **Coordination — plumbing.** The research *workflow* becomes a typed program: components declared, message shapes checked at load time, routing explicit. Pipelines are themselves processes, so whole research stages compose. `plumb-mcp` exposes the repository's pipelines to opencode as MCP tools, so normal opencode sessions can trigger ingest, traversal, and review without leaving the harness.
- **Knowledge repository — hypergraph built by the HyperGraphReasoning method, over OpenAlex-grounded metadata.** Hypergraph artifacts (nodes, hyperedges, embeddings, provenance per source document) are versioned files in git. OpenAlex supplies works/authors/citations on demand.

---

## 4. Component assessment

| Component | Provides | Maturity | License | Adoption posture |
|---|---|---|---|---|
| opencode (have) | agent harness, skills, MCP | mature | open core | keep as-is |
| **HyperGraphReasoning** | automated corpus→hypergraph pipeline; embeddings; agentic traversal (node-intersection); `HYPERNETX` artifacts and HF dataset | research prototype; notebook-centric; needs LLM API or local GPU | Apache-2.0 | **Adopt the method with our own schema/pipeline**, cross-checked against its reference implementation |
| **plumbing** | typed coordination language+runtime; graph-shaped pipelines; MCP in/out; Python bindings (`persevere-plumbing`); protocol declarations; compose-invariants | early (v0; docs, proofs, TLA corpus exist) | AGPL-3.0 | **Adopt the runtime** for a small set of high-value pipelines first |
| OpenAlex (have client) | works/authors/citation graph; `openalex-local` for offline | mature | CC0 | bibliographic truth layer; keep `openalex_client.py` |

**Licensing note (resolved):** AGPL-3.0 (plumbing) is acceptable for now — fine for private/institutional use and a public *research* repository; the copyleft reach to network-served deployments is a known, accepted constraint. Note for the future: plumbing is itself written in OCaml with session-typed protocol declarations; the long-term direction of interest is a runtime whose host language provides multi-party session types natively (the same pipelines should port cleanly, since `.plumb` files are plain text).

---

## 5. The knowledge-engineering loop

**Build (offline, per corpus):**
1. **Corpus assembly.** Project markdown (already in git) + PDFs; expand with OpenAlex lookups by DOI/arXiv/title (existing `openalex_client`).
2. **PDF→Markdown.** Marker/Docling (both already in `requirements.txt`).
3. **Hypergraph construction (co-occurrence first).** Statistical hyperedge construction from the markdown corpus: nodes from extracted concepts/tokens, hyperedges from section-level co-occurrence — deterministic, verifiable, and cheap. Its scale-free/HGN structure is measured before any LLM is involved. (**Decision 3:** LLM relation-typing is deferred enrichment, added only after Phase A measures the co-occurrence baseline.)
4. **Embed** nodes with a local embedding model (nomic-embed-text-v1.5 class).
5. **Commit** artifacts to git: hyperedges as flat files, a HYPERNETX graph, embeddings, and an extraction log for audit.

**Query (runtime, via opencode):**
- An opencode agent asks for grounding on a question; `plumb-mcp` exposes traversal pipelines (node lookup, hyperedge intersection, k-neighborhood with provenance); the agent receives a "evidence bundle": matching hyperedges + source documents + confidence context.
- Human-in-the-loop review is a pipeline (`draft → critic → verdict`), so review criteria are visible and type-checked.

**Grow (incremental):** new ingests append verified hyperedges and re-embed only the affected neighborhood; a diff is committed. The provenance-per-hyperedge rule is what keeps an LLM-built graph honest.

---

## 6. Phased plan

| Phase | Scope | Output | Est. effort |
|---|---|---|---|
| **A — Proof of concept** | RET×TSSI corpus (~68 docs): build hypergraph, one traversal pipeline, expose via `plumb-mcp` to opencode; one agentic reasoning demo (e.g. using the corpus to ground the τ→0 / SK-condition exposition) | working `opencode ↔ plumbing ↔ hypergraph` loop; committed artifacts; honest calibration of LLM extraction quality | 3–5 days |
| **B — Generalize** | Multi-project corpora; OpenAlex expansion; richer relation schemas (project/experiment/intervention entities as typed nodes); incremental rebuild | repository serving all research workspaces | 1–2 weeks |
| **C — Harden** | Persistent query service or graph backend (only if Phase A's file-based store proves insufficient); review protocols; dashboard; formalization hooks (artifact schemas that Track F of the RET×TSSI program could machine-check) | production posture | open-ended |

Phase A is deliberately small: it *measures* the two unknowns (LLM extraction fidelity on this corpus, plumbing's maturity on this workload) before committing to the design.

---

## 7. Risks and open decisions

1. **Extraction fidelity.** Resolved to reduce this risk to near-zero for Phase A: hyperedges start as **statistical co-occurrence** records (deterministic, verifiable against the corpus, provenance-per-edge), so there is nothing to hallucinate. LLM relation-typing enters only as measured enrichment. If the co-occurrence baseline proves instrumentally weak for reasoning, revisit richer extraction with spot-verification and git-reviewed diffs.
2. **plumbing maturity.** Young codebase; AGPL accepted (Decision 1). Mitigate: adopt for a small toolset first; keep pipeline definitions as readable `.plumb` files that port if the runtime stalls or the future session-typed alternative matures.
3. **HyperGraphReasoning as repo vs method.** The repo is notebook-centric and API-dependent. Recommendation: follow its method, own our schema and pipeline (Apache-2.0 allows this). Phase A can still run its reference notebooks as a benchmark.
4. **Compute/cost.** LLM extraction is the expensive step. Choose per-corpus: API tier or local Llama. Embeddings are cheap/offline.
5. **What happens to in-flight work.** The AnyType-elimination plan (§ its Phase 1+ and relational extension) is superseded: OpenAlex already covers bibliographic ground truth; the SQLite store at most survives as operational scratch, and the Phase-0 dump files stay as the safety net. The RET×TSSI program and walkthrough are unaffected (they live in git markdown).
6. **Scope of "explicit".** Decide how much of the *workspace* (research-state YAML, findings, logs) should be mirrored into hypergraph nodes vs left as git markdown. Recommendation: markdown stays canonical; hypergraph mirrors it as typed nodes with provenance, never the inverse.

---

## 8. Why this fits the research program

Hypergraphs and typed composition are not incidental to this lab's aims. The RET×TSSI program's Track B asks for compositional, categorially-anchored structure for extended thermodynamics; plumbing's "pipelines are processes that compose" is that same composition spine applied at the tooling level, and a hypergraph is the natural substrate for the program's cross-track objects (physics × economics × computation). The proposal is thus not a detour but the infrastructure side of the same research identity: **structure that can be drawn, checked, and reasoned over.**

---

*Existing solutions referenced: lamm-mit/HyperGraphReasoning (Apache-2.0; Stewart & Buehler, arXiv:2601.04878); quantumsoftwarelab/plumbing (AGPL-3.0; Edinburgh / Leith Document Company); OpenAlex (CC0), incl. openalex-local; opencode.*