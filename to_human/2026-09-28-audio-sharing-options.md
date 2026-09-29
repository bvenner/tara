# Audio Sharing Options — 2026-09-28

Context: `writing/human/*.m4a` (~240 MB across Informatics1–4, growing each
session) came out of git in commit `e42fafc` and are now gone from the public
repo — but they still need to (a) survive, (b) stay reachable from your
machines, and (c) in some cases be shared with Nic (also Denver). Raw
transcript `.json` joined them; the derived transcripts
(`.txt/.srt/.tsv/.vtt/.md`) remain tracked and are the citable artifact.
Privacy: this is employer-considered / organizing audio — any option below must
stay **out of anything public**, which rules out plain cloud-sync folders wired
into anything repo-like.

---

## Options

### 1. Syncthing P2P (recommended default)

- Continuous, E2E-encrypted, serverless sync folder: laptop ↔ `amon-sul`
  (your NixOS box already runs Docker services; Syncthing has an official
  container or is a nixpkgs service option).
- **Cost:** free. **Effort:** ~1–2 h setup.
- Handles the ongoing need automatically — new recordings sync as they land;
  file versioning (trash-can / simple versioning) protects against clobbering.
- **Nic extension:** Syncthing works over WAN without any server rework — he
  installs the client, joins the device IDs. Nothing you already set up changes.
- Weakness: no off-site durability unless amon-sul itself is backed up.

### 2. rclone → Backblaze B2 / Cloudflare R2 (recommended complement)

- Nightly `rclone sync` into a **crypt** remote (client-side encrypted, so the
  provider sees nothing — matters given the content).
- **Cost:** effectively pennies/month at current scale (~240 MB now; even
  growing to few GB/year stays under a dollar). Fix my earlier "~$0.50–1/GB"
  figure: it was overstated for this payload.
- This is the answer to "what if the single disk dies" — an off-site copy that
  neither depends on your hardware being up nor puts audio back on a public
  forge.
- Share story with Nic: presigned URLs (expiring) or just sync him via Syncthing
  instead (option 1) — don't share the bucket.

### 3. git-annex

- Would re-couple the audio to the repo's identity while keeping big blobs out
  of history.
- **Not recommended:** the repo policy just settled that audio is out-of-band;
  git-annex reintroduces tooling friction (clone-with-annex workflows, remotes)
  that this solo, two-machine workload doesn't need to recoup.

### 4. Plain rsync cron to amon-sul

- `rsync -a --ignore-missing-args writing/human/ amon-sul:stage/writing-media/`
  nightly. Near-zero setup (~10 min), works today.
- Weakness: no versioning (deleted/moved audio vanishes unless `--backup` is
  used), no Nic sharing, no automatic start-on-new-device. A floor option, not
  the target.

---

## Recommendation

**Option 1 as the live sync layer, Option 2 as the durability layer.** They
solve different failure modes (reachability/collaboration vs. catastrophe) and
together cost nothing but setup time.

### Tie-in to the review (Q2 caveat)

The workspace review warned that untracked raw files "can die with the disk".
Until option 2 is running, the tracked transcripts are the only durable record.
Low-tech insurance in the meantime: keep transcript-first discipline (a session
isn't "ingested" until its `.txt/.srt/.tsv/.vtt/.md` are committed) and note the
audio's sha256 in the transcript header so the off-band pairing is verifiable:

```
git hash-object writing/human/Informatics1.m4a   # → record in a small tracking file or the transcript header
```

## Next concrete steps (when you pick)

1. **Syncthing:** enable `services.syncthing` in amon-sul's NixOS config; add
   laptop device ID + shared folder `writing/human/`; set versioning to
   "trash can", 30 days.
2. **rclone:** `rclone config` → create b2/r2 remote → create `crypt` remote
   wrapping it → schedule `rclone sync writing/human/ audio-crypt:writing/`
   via systemd timer on either machine.
