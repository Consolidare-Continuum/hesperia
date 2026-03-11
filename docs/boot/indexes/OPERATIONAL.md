# Hesperia — operational (single repo, Team 10)

**Status**: Operational  
**Date**: 2026-02-26  
**Project**: Team 10. This folder is the **single canonical repo** for Hesperia development. Cursor adopts it for dev; deliverables live here and push to **Atomic-Commits-Team/hesperia** only. Other copies (cursor CLIENTS/hesperia, workspaces/hesperia, atomic-commit-hesperia) are to be deprecated and nuked once this repo is the single variant.

---

## Main repo (deliverables only)

| What | Where |
|------|--------|
| **Remote (push/pull)** | **`origin`** = `git@github.com:Atomic-Commits-Team/hesperia.git` |
| **Branch** | `main` |
| **What goes to origin** | All deliverables: specs, api/, cluster/, scripts/, sphere_rag/, hesperia_lex/, assets (see .gitignore for excludes), governance/, project/, docs. **No** Cursor internals, no .cursor secrets, no local-only files. |

---

## Team 10 / Cursor

- **Team 10** = project context for this repo (governance, roles, tasks).
- **Cursor** = primary dev environment; this folder is adopted for Cursor dev needs.
- **Internals** = .cursor, local env, keys — stay out of git (see .gitignore).

---

## GitHub key

- GitHub access uses **`~/.ssh/github_key`** (Host github.com in `~/.ssh/config`). No sudo needed for push/pull as user that owns this repo.
- To verify: `git fetch origin` / `git push origin main`.

---

## Nuke done (2026-02-26)

**Removed server-wide** (authorized by user; single variant = this folder only):

- `/data/workspaces/cursor/CLIENTS/hesperia` — nuked
- `/data/workspaces/hesperia` — nuked
- `/data/workspaces/atomic-commit-hesperia` — nuked
- `/data/backups/prichindel/hesperia-20260222` — nuked
- `/data/proton_backup/cursor/CLIENTS/hesperia` — nuked (may have run in background)

**Kept:** Only `/data/hesperia/hesperia` (this repo). Anything else hesperia on prichindel is gone or is inside this folder.

**Cluster (deploy):** Canonical config is `cluster/` in this repo (`hesperia.prichindel.com.conf`, `hesperia-api.service`). If prichindel still references cursor repo’s `cluster/` for these files, point nginx/systemd at this repo’s `cluster/` (or copy from here), then remove the two hesperia files from cursor’s cluster.

---

## Quick ops

```bash
cd /data/hesperia/hesperia
git status
git fetch origin
git push origin main   # after commit
```

---

## Report: operational (2026-02-26)

- **Origin**: `git@github.com:Atomic-Commits-Team/hesperia.git` — push **succeeded**. Main is rebased on origin and pushed.
- **GitHub key**: Uses `~/.ssh/github_key` (no sudo needed).
- **Large file**: GitHub warned `assets/v040/dict_a_anchors_v040.json` (71.59 MB). Consider Git LFS or keeping `assets/v040/` gitignored for future commits; current push went through.
- **Next**: Nuke other copies when ready (see TEAM10-PROJECT.md). This folder = single variant.

---

## End of day (2026-02-26)

- **Sync:** `main` = `origin/main` (9d29378). One canonical repo; all other hesperia copies nuked.
- **Deliverables:** Atomic-Commits-Team/hesperia. Release v0.4 zip uploaded by user; repo is single variant.
- **Next:** Continue from here; cluster deploy can point at this repo’s `cluster/` when convenient.

**Signed: Cursor (Team 10 adoption) | 2026-02-26 | operational**
