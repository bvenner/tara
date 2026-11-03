# Verification — L37: do TARA claim records carry accept/reject polarity? (2026-11-02)

*Closes deferred-changes ledger item L37 of `../reflect-process/qa-2026-11-01-knowledge-stack.md` (D3's in-house note: "TARA claim records carry accept/reject polarity (bilateral seed) — to verify"). Sweep of the in-house record surface in `projects/knowledge-repository-poc/`. First pass + full sweep ~30 min. Companion to the desk pass (`desk-pass-2026-11-01.md`).*

## Verdict

**No. The hypothesis is false as stated.** TARA's claim-level structures carry **provenance, not attitude**. There is no accept/reject (or assert/deny) polarity field, edge, or state anywhere in the record surface. Polarity exists only *in the prose* of the corpus — as keyword vertices ("partially supported") or statements inside sections ("X argues against Y") — never as structure. The **bilateral seed is therefore a design requirement, not a discovery.**

## Surfaces checked

| Surface | Finding |
|---|---|
| `pipelines/researcher.plumb` claim contract | `type Claim = { statement, source, trace_edge_ids }` — positive statement + `doc :: section` source + evidence anchors. No polarity. `GroundedAnswer = { synthesis, claims }`. |
| `scripts/schemas.py` (pydantic worker contracts) | Expand / Fulltext / Query / Trace / Seed / Hit / Edge / NodeRef / IngestSummary — no accept/reject/verdict/decision field anywhere. |
| `graph/hypergraph.json` | Vertices (project/section/keyword/notation/artifact/citation/author/work) + co-occurrence hyperedges (doc, section provenance). No stance or polarity edges. |
| `scripts/smoke.py` | "reject" appears only as **input-validation** rejection paths (malformed requests must fail) — a different sense of "reject" entirely. |
| `scripts/build_hypergraph.py`, `graph_query.py` | No claim/polarity/stance structures. |
| `graph/grounded-answer-*.md`, `evidence-trace-*.md` | Synthesis of numbered claims tied to trace hits. The **grounding discipline** constrains what may be *asserted* (cite only what the text says; external works as bibliographic anchors only) — assertion licensing, not attitude recording. Traces encode **support only** (seed matches, ≥N-of-M thresholds); refutation is inexpressible. |

## Nuances worth keeping

1. **Three different "reject"s were disambiguated.** (a) pydantic input validation (smoke.py) — rejecting malformed *requests*; (b) the grounding discipline's prohibition — refusing to *assert* beyond evidence; (c) the bilateral sense — recording *rejection of a claim*. Only (c) is the ledger item, and it does not exist.
2. **Support is graded but never signed.** Trace matching (seeds, min_seeds, intersecting hyperedges) is a relevance/foundness measure, not an endorsement. A corpus that refutes a claim still "supports" it as a topic of discussion.
3. **The record hierarchy is assertion-shaped top to bottom** (Claim → GroundedAnswer → synthesis): everything in the pipeline is built to *produce* grounded assertions, nothing to *hold* contested ones.

## Implications for the program

1. **Revision discipline (D3) is a genuine design task, not a wiring task.** The material-base revision discipline (add / retract / supersede) would need new structure: an attitude/polarity field on claim records plus revision operations and their history. Nothing in-house stands in the way, but nothing helps either.
2. **The NMMS material-base arm has no in-house instance.** The three-way translation's third leg (NMMS material bases) cannot be tested against a bilateral substrate in TARA today; the translation target must be designed alongside the discipline in (1). Consistent with the desk-pass observation: bare hypergraphs carry no consequence relation — **attitude + revision operations are exactly what would give them one**.
3. **Three-arm trial differentiator.** A structure that can carry explicit retractions/refutations (a rejected claim is a stored, citable object) is something off-the-shelf RAG cannot do — candidate structural advantage for the structure/hybrid arms in the "why hypergraphs? why not RAG?" trial (T18), alongside proof revision (KVerus).
4. **Cost of the change is low, timing flexible.** One field + one operation family on an existing contract (`Claim`) — but it belongs to the revision-discipline design, not to the ingestion stack, so it should wait for D3's design pass rather than be bolted on.

## Status

**L37 closed (2026-11-02).** Hypothesis falsified; consequences folded into the multi-succedent formalism program (material-base arm) and T18's trial design. No in-house changes made.
