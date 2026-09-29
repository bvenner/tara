# Session Context Preservation — 2026-09-28

Recovered from a crashed opencode session (`Dijkstra vs indexed vs graded
monads`, crashed ~01:06 Sep 28 mid-`rm`). This note captures what that session
was doing and what this recovery session completed. Read alongside root
`AGENTS.md` (updated) and the repo's git log.

## What the crashed session was doing

Executing the "quick wins" of `to_human/2026-09-27-workspace-architecture-review.md`
(written by that same session, which drifted from monad research into a
workspace-architecture review). Its todo list at crash:

1. Untrack `writing/human` audio + raw transcript JSON → **done this session**
2. Prune AnyType debris → **done this session** (`rm` had not executed at crash)
3. Scaffold `projects/means-of-production-working-group/` → **declined by Brad**
   (see below)
4. Write audio-sharing options → **done this session**

## Completed this session (all on origin/main via PR #4, merged `ba8955d`)

- `e42fafc` chore: untrack writing/human media; ignore audio + raw transcript
  JSON (~240 MB out of the public repo; files remain on disk)
- `01f6e17` chore: remove AnyType debris (package.json, node_modules)
- `a9eefd5` docs: architecture review committed + addendum (two findings
  superseded same-day recorded there)
- `53270e0` docs: audio-sharing options note
  (`to_human/2026-09-28-audio-sharing-options.md` — Syncthing ↔ amon-sul live
  layer + encrypted rclone→B2/R2 durability layer recommended)
- Root `AGENTS.md`: AnyType decommission bullet marked done
- PR #4 pushed to feature branch + merged on **Brad's explicit confirmation**;
  `main` synced with origin, working tree clean

## Key corrections to recorded beliefs (don't re-derive)

- Root `opencode.jsonc` / `.opencode/` / `~/.config/opencode/` contain **no
  anytype MCP entry** — the review doc's Appendix claim was already stale.
  Only debris was root `package.json` + `package-lock.json` + `node_modules/`.
- Repo-local `.opencode/package.json` is opencode's own machinery
  (`@opencode-ai/plugin`) — NOT AnyType; do not delete.
- The MoP proposal stays deliberately in `writing/human/` — Brad declined to
  promote it to a project thread (2026-09-28).

## Remaining next steps (ranked, see conversation)

1. Restart opencode to load skills + plumb MCP (config changed, still pending)
2. Audio: implement Syncthing on amon-sul (+ rclone crypt backup) — steps in the note
3. Repo privacy purpose decision (DSA material + class transcripts in public repo) — review §3.1, gates nothing technically but colors content policy
4. POC → `infra/knowledge-repository/` move (Action #4, 30–60 min, audit list in review doc §5)
5. RET×TSSI Master's sub-problem choice (M1–M6; M1 default) + exposé — the research critical path
6. Island-DT deepening; embeddings-vs-Phase-C decision (non-forced)
