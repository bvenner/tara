---
name: hypergraph-grounding
description: Ground research answers in the RET x TSSI knowledge repository. Use when answering a substantive research question about the program (or its corpus) where claims should be traceable to its documents; also use when the corpus/pipeline needs to grow or be re-queried.
---

# Hypergraph grounding

The RET × TSSI research program has an explicit knowledge repository at
`projects/knowledge-repository-poc/`: a co-occurrence hypergraph built from the
corpus (markdown + OpenAlex works), served by typed plumbing pipelines. Use it
to *ground* answers instead of relying on unverified recollection or on any LLM
asserting structure the corpus does not support.

## When to use

- Answering a question about the program's content (theorems T1–T4, the
  correspondence, gravitation, tracks, critiques) where a claim should cite
  specific document sections.
- Expanding or re-building the repository after corpus edits.

## How to query (both paths are equivalent)

1. **MCP (if the `plumb` server is loaded):** call `plumb:call` with
   `{source: <contents of the .plumb file>, input: {...}}`.
2. **bash helper (always available):**
   ```
   python projects/knowledge-repository-poc/scripts/pipeline.py trace_report '<input-json>'
   python projects/knowledge-repository-poc/scripts/pipeline.py query       '{"concept":"..."}'
   python projects/knowledge-repository-poc/scripts/pipeline.py trace       '<input-json>'
   ```

Pipeline inputs:

| Pipeline | Input | Output |
|---|---|---|
| `query` | `{concept}` | matched nodes + hyperedges with `doc`/`section` provenance |
| `trace` / `trace_report` | `{topic, concepts:[...], min_seeds}` | sections where ≥ `min_seeds` concepts co-occur (intersection grounding) |
| `evidence` | `{concept, max_edges}` | markdown bundle |
| `ingest` | `null` | rebuild summary |
| `expand` | `{mode:topic\|doi\|arxiv, ...}` | OpenAlex corpus expansion |

Pipelines read `graph/hypergraph.json`; cwd must be `pipelines/` (the helper and
the MCP wrapper handle this).

## Conventions

- Cite grounded answers as `doc :: section` (e.g. `research-program.md §4 Track A`).
- Do not assert content beyond what the trace/query returns or the cited section states.
- After corpus edits, regenerate first: `python scripts/build_hypergraph.py --force`
  (the `--compact`/default fast path skips unchanged corpora; `--force` overrides).
- "Entropy" in this program means convex Lyapunov structure, not thermodynamic entropy.
- Determinism: everything here is LLM-free until an LLM provider key exists; the
  LLM is the *reader/synthesizer*, never the structure-builder.