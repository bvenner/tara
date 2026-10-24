---
title: "Session context: pre-compaction state before the moaiwi v3 rewrite"
date: 2026-10-24
kind: context-preservation
project: moaiwi-network-poc
---

# Session context — before the v3 rewrite

**Purpose:** conversation-only state preserved before window compaction (2026-10-24), immediately before starting the v3 rewrite specified in `writing/human/moaiwi-revision-proposal.md`. Durable decisions are already in files; this note covers what is not.

## 1. Next action (queued, not started)

Brad's instruction, given and then held pending compaction: **create a branch named `moaiwi-v3-rewrite`** and begin the revision process in `writing/human/moaiwi-revision-proposal.md`. The branch does **not** exist yet. Sequence per the proposal and the project `AGENTS.md` "v3 rewrite" section:

1. `git checkout -b moaiwi-v3-rewrite` from `main` (currently `dec9785`, in sync with origin).
2. Move `writing/machine/2026-10-21-moaiwi-network-poc-meta-plan.md` → `projects/moaiwi-network-poc/` (keep the filename; it stays as the historical v2 record).
3. Write the **v3 meta-plan from scratch** in `projects/moaiwi-network-poc/` (proposed name `meta-plan-v3.md`; Brad has not confirmed the filename).
4. **Stop for review** — `framing-memo-v3.md` comes only after the meta-plan is revised and reviewed.
5. Fate of `research-plans/` (B1–B4) is explicitly **undecided**; do not fold them into v3 or delete them.

Primary sources are `writing/human/MOAIWI-{1,2,3}.md` (MOAIWI-4 for the near-term product discussion); the revision proposal wins any conflict; the old meta-plan is reviewable input but the new draft should be a genuine fresh draft, not a re-skin.

## 2. Decisions I was mid-way through, not yet settled

- **Does the conference sprint survive into v3?** The revision proposal never mentions the R&B DEN-2026 5–10 minute overview (it describes the conference only as the *origin* of the Moaiwi product). The v2 meta-plan's combined sprint, 5–10 min slot + brief demo, and show-ready deck/site are therefore not carried forward by the proposal and not contradicted by it. My inclination: treat the overview as a milestone inside Moaiwi's first phase rather than as the organizing objective of the whole plan — but this is a synthesis choice, not a decision Brad has made. Ask, or present it as an option in the v3 draft.
- **File naming:** proposal says "create a 'v3' version of this file"; existing convention in the project dir is `framing-memo.md` / `framing-memo-v2.md`, so `meta-plan-v3.md` and later `framing-memo-v3.md` fit. Not confirmed by Brad.

## 3. Loose ends flagged, no decision

- ~~`writing/human/mycor-development-proposal.md` is tracked but **0 bytes**~~ — **resolved 2026-10-24:** Brad deleted the placeholder.
- **Primary sources expanded (Brad, 2026-10-24):** the revision proposal now names **four** transcripts (`MOAIWI-{1,2,3,4}.md`) **plus `writing/human/Informatics1Readable.md`**, and requires that conflicts be **noted**, not just resolved by fiat. It also records Fortress's source locations (`/home/brad/Projects/fortress`, `codeberg.org/proletariat/fortress`) and reframes Fortress as **the basis for Moaiwi** — one configurable codebase for a home-network server or a business server — rather than merely an idea source with a shared core. Watch for a truncated sentence in the current draft: "the Develop process will be based on the repository at We intend to develop…".
- **mycor.io ↔ proletariat.tech relationship unconfirmed.** Brad said on 2026-10-22 that Nic is lead developer at Mycorrhiza Cooperative (mycor.io); the revision proposal (2026-10-24) names the developer as **proletariat.tech (PT)** with Nic as lead developer. Both statements are recorded; the review doc's §8 entry now says the relationship must be confirmed rather than assumed. Do not silently pick one.
- Nic's pronouns are **they/them** (per the revision proposal). All *our* prose was updated; the transcripts remain verbatim and say "Nick" in the M4 raw.
- No PR is open. `feat/workspace-cleanup-2026-09-28` is still unmerged and untouched this session.

## 4. Tooling quirks learned this session (not in the plan docs)

- `scripts/pipeline.py` fails here (plumb `morphism_fatal`, exit 1, no stderr). Workers run fine invoked directly: `cd projects/knowledge-repository-poc/pipelines && printf '{"mode":"topic","topic":"<q>","limit":10,"doi":""}' | ../bin/tara-python ../scripts/expand_openalex.py`. (Recorded in B1 plan §4.4.)
- `fulltext mode:"local"` **requires a DOI**; it derives the key from the OpenAlex record. No-DOI works need a direct call: `fetch_fulltext.convert_local_pdf(rec, key, fetch_fulltext.get_converter)` — note it takes the converter **factory** (`get_converter`), not a converter instance. (The factory quirk is *not* in the plan docs.)
- `graph_query.py` matches **single concepts, not phrases**: `"cooperative federation governance"` → nothing; `"federation"` → nodes. Worth a note in the grounding skill eventually.
- OpenAlex full-text retrieval: institutional repositories with DSpace REST APIs are scriptable (Helsinki worked via `/server/api/core/...`), while Springer / ScienceDirect / AgEcon / SSRN are JS/Cloudflare bot walls — assume manual browser download then `fulltext mode:"local"`.
- OpenAlex `topic` mode is plain full-text search; query phrasing determines precision. Validated Block A queries: `Mondragon secondary cooperative`, `cooperative federation governance`, `inter-cooperation worker cooperative`, `cooperative federation structural change`. Noisy, avoid: `worker cooperative federation`, `cooperative holding company structure`.

## 5. Workflow conventions in effect

- Comment workflow (active earlier this session): Brad types comments in chat; I apply them immediately to the named document and report **one line per change** (he chose this over the OpenCode diff-suppression options); commit only when signalled.
- Git: semantic prefixes; commit when asked; never push `main`; feature branches only; **merge commits for PRs** (preserves SHAs); PRs via `gh`; merge order matters when stacked.
- `smoke.py` runs locally only for `agent-harness-poc` work (rule in both AGENTS.md files); CI covers pushes/PRs.
- `Audio/` stays ignored except the two committed transcription scripts; raw transcripts live in `Audio/transcripts/` and cleaned versions in `writing/human/`.

## 6. Where the durable state already lives (do not duplicate)

- `projects/moaiwi-network-poc/AGENTS.md` — resume path, the **v3 rewrite section** (structure: projects Moaiwi/Hyphae/Cooptopia × meta-processes Research/Develop/Deploy/Reflect; PT; Fortress span; $50k/yr goal; meta-process realizations), locked 2026-10-22 decisions marked as governing v2 only.
- `writing/human/moaiwi-revision-proposal.md` — the authoritative rewrite directive.
- `writing/machine/2026-10-22-moaiwi-session-context.md` — earlier comment-phase state (updated 2026-10-24 to mark §5 fully decided).
- `writing/machine/2026-10-22-moaiwi-transcripts-review.md` — N1–N37 + §5/§7 decisions; §8 name resolutions (Marie = mom (she), "Lebert" = Lawvere, "My Carriza" = Mycorrhiza Cooperative).
- Workspace `AGENTS.md` thread 5 — points at the v3 rewrite as the current phase and at PRs #14/#15 as merged.
- `projects/moaiwi-network-poc/research-plans/B1-screening-2026-10-22.md` and `B1-p0-readings-2026-10-22.md` — Phase B corpus screening and the two-paper P0 summary (Mondragon multistakeholder governance; Finnish companization).
