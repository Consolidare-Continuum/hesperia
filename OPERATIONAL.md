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

## After self-organization

- This repo is the **single variant**.
- **Nuke the rest**: Remove or archive `/data/workspaces/cursor/CLIENTS/hesperia`, `/data/workspaces/hesperia`, `/data/workspaces/atomic-commit-hesperia` once you are happy with this outcome and have pushed to origin.

---

## Quick ops

```bash
cd /data/hesperia/hesperia
git status
git fetch origin
git push origin main   # after commit
```

**Signed: Cursor (Team 10 adoption) | 2026-02-26 | operational**
