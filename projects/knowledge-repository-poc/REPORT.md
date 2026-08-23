# Knowledge-Repository POC — Phase A, Step 1

**Co-occurrence hypergraph over the RET × TSSI corpus** — built 2026-08-23, no LLM involved.

## Method

Node rule (**co-occurrence v1**): nodes are
- `section` — every markdown heading in the corpus
- `keyword` — RAKE keyword phrases (deterministic, per document top-15 + per section top-6)
- `citation` — bibliography entries from `program/references.bib` (74 keys), matched in-text by author-year
- `artifact` — theorem tags T1–T4 and Track A–F
- `notation` — curated spine tokens: gravitation, Cattaneo, simultaneism, SK condition, τ_J, subcharacteristic, Fourier, MELT

Hyperedge rule: within each document section, the set of concepts present (arity ≥ 2) is one hyperedge. Provenance is recorded per hyperedge (source doc + section).

## Corpus

32 markdown documents (program doc, critiques, findings, 26 literature notes, research log, to_human notes) across 116 sections; `references.bib` for citation entities.

## Results

| Metric | Value |
|---|---|
| Nodes | 396 (231 keyword · 116 section · 31 citation · 10 artifact · 8 notation) |
| Hyperedges | 114 (arity 2–16) |
| Max / mean degree | 33 / 1.87 (heavy-tailed; leaf-dominated) |
| Degree ≥ 9 nodes | 15 |

Top hubs (hyperedge degree):

| Node | Kind | Degree |
|---|---|---|
| gravitation | notation | 33 |
| Cattaneo | notation | 30 |
| simultaneism | notation | 29 |
| SK condition | notation | 26 |
| T3 | artifact | 23 |
| τ_J | notation | 20 |
| Track B / T4 / Track A / Track C | artifact | 17 |
| subcharacteristic | notation | 13 |
| T1 | artifact | 13 |
| Fourier | notation | 11 |

The hub structure matches the program's intellectual spine (the correspondence: gravitation ⇄ Cattaneo ⇄ simultaneism, with SK condition / τ_J / the theorem set as the technical core) — a sanity signal that section-level co-occurrence already recovers the corpus's central structure.

## Artifacts (`graph/`)

- `hypergraph.json` — `V` (node list), `E` (hyperedge member lists), `hyperedges` (full records with `doc`/`section` provenance). Shape is HNX-loadable (`Hypergraph(V, E)`).
- `provenance.tsv` — per-hyperedge `edge_id / doc / section / arity`.
- `stats.json` — full counts, arity histogram, degree distribution, hub table.

## Rebuild

```
python scripts/build_hypergraph.py            # ≥ Py3.10, stdlib only
```

## Next

- **Step 2:** plumbing pipelines (`ingest`, `query`, `evidence`) over this graph, exposed to opencode via `plumb-mcp`.
- Later: embeddings; then (decision-staged) LLM relation-typing as enrichment.