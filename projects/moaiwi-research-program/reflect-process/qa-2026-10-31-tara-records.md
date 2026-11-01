# QA session record — the meta-processes (round 1, exchange 1): TARA as a records management system

**Date.** 2026-10-31 · **Participants.** Brad + agent · **Process.** Meta-process review round 1 · **Stopping point.** Proposed by agent, accepted by Brad ("I accept your proposed stopping point. Please apply.").

**Input.** Brad's `writing/human/polarity-research-proposal-notes.md` (revised — now three sections: *String diagrams as syntax*, *TARA as a records management system*, *Asides*; the Asides are **not normative** to the topic per Brad's reading instructions) and Karpathy's *LLM Wiki* gist (https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), read into context at Brad's request. **Topic order:** TARA-as-records first (Brad's time today was limited); the string-diagram topic is **parked with its questions standing** (restated below).

## Decisions

- **D1 — T14 absorbs the topic; research is the full design space (Q2).** T14 (in the meta-process cluster, hence revisable in this process) takes the records-management material. The **"no-full-rewrite" constraint is dropped as a research constraint** and retained as a **development-sequencing fact** (no dev resources on a TARA rewrite until Moaiwi Develop/Deploy are more realized). Research outputs = **options**; the migration path = a future **Develop-process** deliverable. (Convergence with the house idiom: "options, never decisions, on architecture.")
- **D2 — immutability reframed as traceability (Q4).** The agent's proposed split (immutable records / external lifecycle metadata) is **withdrawn**; git's revision history provides traceability of every record to its original (ISO 15489 equivalent to verify — L16). **One repository = the whole knowledge system ("the wiki is the repository")**, consistent with Obsidian practice. **The git DAG ↔ hypergraph relation is a first-class open research question** (L17): Brad's initial take is *sync the git DAG with the hypergraph* — which would make a NARA-style **self-contained, implementation-independent export** possible (history as data, not git internals). Binaries (images, audio, PDFs) live **outside git** — a public-facing store (Zenodo or an IPFS-class equivalent) with the hypergraph carrying **fixity** references (L21).
- **D3 — record model (Q3 + sub-question).** **All markdown files are records**, human- or machine-authored alike (L19) — the agent's derived-vs-human record-status distinction is retired (the *authority* question survives separately as T14.a). **Conversion intermediates are archived** (L20): every "image-to-text" conversion (PDF, audio, future modalities) makes non-deterministic choices that cannot be recomputed; the intermediate text is the evidence. Concrete instance in-house: the MOAIWI transcripts + the `Audio/transcribe-*.ts` conversion processes.
- **D4 — governing requirement (Q1): (c) records management** — the care and feeding of the hypergraph is at the center of downstream design. (a) and (b) become **subordinated problem statements**, recorded in T14 as **(P-Obsidian)** can a TARA-compatible repository also be Obsidian-compatible (via materializing markdown out of the hypergraph) and **(P-NARA)** archive format *compatible with NARA's goals* (self-describing, implementation-independent, documented, fixity-carrying) — **not** that NARA currently accepts it.
- **D5 — materialization under development (Q1 tail).** Git is the authoritative source *while the repository is being developed*, so the hypergraph must be **materialized in a text-based format** (existing JSON vs. a hypergraph interchange format — research item) with **rules that don't churn the history** (diff-stable serialization, incremental materialization, commit batching) — L24. The question of what is authoritative *after* development is recorded open (L25 → T14.d).
- **D6 — Q3 authority lean + notation.** Derived content leans **hypergraph-canonical** (markdown as materialized view); residual = the ingestion direction for human-authored prose (→ T14.a). **Notation:** lettering convention kept for sub-questions in dialogue; short-code sub-headings (`[[RT##sub-question]]`-style) **deferred** pending the Obsidian literature (L22); **RT topic headings are now bare topic numbers** (applied this stopping point, per Brad's URL-anchor request); the polarity note's wikilinks translated to Markdown links (applied).

## Deferred-changes ledger (L15–L25; L1–L14 closed at round 0)

| # | Item | Disposition |
|---|---|---|
| L15 | Bio: most of Brad's career at the **U.S. EPA**; thinking colored by it | **Applied** (global `AGENTS.md`, "About me") |
| L16 | ISO 15489 equivalent of "traceable" (candidates: chain of custody, provenance, fixity/integrity) | Recorded → **T14.e** (open research item) |
| L17 | git DAG ↔ hypergraph relation (sync hypothesis; multi-store custody representation) | Recorded → **T14.b** (open) |
| L18 | Q3's questions (authority a/b/c; record status; derived-vs-human) into the topic | Recorded → **T14.a/T14.f** |
| L19 | "All markdown = records" (authorship irrelevant to record status) | **Applied** (T14 working position) |
| L20 | Conversion intermediates archived (non-determinism rationale) | **Applied** (T14 working position) |
| L21 | Multi-store archive: git + Zenodo/IPFS; hypergraph carries fixity + external refs | **Applied** (T14 working positions + T14.b/T14.f) |
| L22 | Short-code sub-heading scheme + Wikilink translation, sourced from Obsidian literature | **Partially applied** (wikilinks translated; RT headings bare); sub-heading scheme **deferred** |
| L23 | Q1 resolved: (c) governs; (P-Obsidian)/(P-NARA) problem statements | **Applied** (T14 governing requirement) |
| L24 | Text materialization of the hypergraph + churn-controlled rules | Recorded → **T14.c** (open) |
| L25 | Post-development authority (git forever vs. future system store) | Recorded → **T14.d** (open) |
| (old) | Round-0 L14 tail: T18 motivation edit (origin question, Nic/Brad tension, Brandom item) | **Still open** — next batch |

## Parked — string diagrams as syntax (questions standing)

- **Q1.** Target of the string-diagram question: (i) a *doctrine* (NMMS material-base syntax drawn as string diagrams with compositional semantics), (ii) a *translation test* (embed NMMS into SDR I–III machinery; find where it breaks — negatives count), or (iii) a *pragmatic choice* (nearest workable diagrammatic representation for TARA's hypergraph now)?
- **Q2.** Is the agenda item *"which symmetric monoidal setting admits an NMMS string-diagram doctrine — SMC, or the double/triple-categorical generalizations (Myers' double operadic systems theory; surface diagrams)"*, with Brown's reconstruction examined as evidence rather than verdict?
- **Q3.** Is the pyNMMS fallback (adopt the material-base framing without categorical semantics) the **end-state decision** or a **parallel track** (prototype candidate (b) now regardless of the doctrine search)?

## Amendment — 2026-10-31, later: goals check (Brad)

Brad had the agent state its understanding of the process's larger goals and corrected it; the corrected version is memorialized as **"Purpose and larger goals"** in `reflect-process-instruction.md`. Key corrections, governing over earlier instructions:

1. The under-review topics are **listed explicitly** (T13, T14, T15, T16, T17, T18) — no range math ("T13–T18 + T16" was redundant).
2. **Scope narrowed:** goals 1 (self-application on the program's process-structure) and 3 (the X → F(X) recursion / specifying the four processes) are **too large for this process** — it is focused on **revising a research plan**. *This dialogue overrides previous instructions to the contrary* (including the Comments §2 coalgebra framing).
3. Whether "everything serves the autonomy terminal object" is an **open question**, not an assumption — T16 is itself under revision here.
4. The process's outputs are exactly: **a QA record** and **a revision of research-topics-v3.md** ("research-plan-v3"); additional artifacts only if necessary, with a decision on where they live.

**Aside (Brad, 2026-10-31):** if a revised TARA is structured more like a wiki, the current **folder-based factorization** (one directory per research question) will need to be revisited — a benefit being less time spent deciding where files live. Recorded in T14.f.

## Applied at this stopping point

T14's revision (records-management absorbed; full design space; options-out; sub-questions T14.a–f) · RT topic headings → bare topic numbers with titles as bold lead lines · polarity note's wikilinks → Markdown links (body references; notation examples left as notation) · Asides routed to `democracy-as-regime/asides-input-2026-10-31.md` (non-normative there too — input, not decision) · AGENTS pointers updated · this record.

**Noted, not changed:** the polarity note's prose path `./project/agent-harness-poc` should read `./projects/agent-harness-poc` (left verbatim — Brad's file). **Uncommitted** on `main` (this batch rides with the next commit).
