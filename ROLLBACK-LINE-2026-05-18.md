# Rollback line — 2026-05-18

**Commit type:** artificial draw-the-line marker (documentation only; no engine logic change).

## Situation as-is

- **Prod** (`prichindel:/data/hesperia/hesperia`) and **dev** (`alunel:/data/workspaces/atomic-commit-hesperia`) were diverged (+9 local OUT-VIEW / Session Inspector cherry-picks vs +60 on `origin/main` for TMX / hex-matrix).
- **2026-05-18:** merged `origin/main` into prod `main` (keep maximum), deployed Session Inspector (Django `output_views`) + hex-matrix static SPA on `hesperia.prichindel.com`, aligned disks, pushed **`main`** to all three allowed GitHub remotes.
- **Hesperia engine core** (`hesperia/engine/`, sealed product surface) was not rewritten in this event; work was **`output_views/`**, deploy scripts, and static viewer assets.

## GitHub (canonical for further dev)

All three remotes must stay on the same `main` SHA after each publish:

| Remote | Repository |
|--------|------------|
| `origin` | `Atomic-Commits-Team/hesperia` |
| `dev` | `igareosh/hesperia` |
| `backup` | `igareosh/hesperia-dev-backup` |

## Where to rollback

| Marker | Purpose |
|--------|---------|
| **`hesperia/rollback-line-20260518`** | This line — GitHub + disk truth after align/push (tag on this commit). |
| **`hesperia/line-clean-20260518`** | Pre–draw-line product state (`2aa1d43` deploy pins); tag on parent if present on your clone. |
| **`backup/pre-align-20260518`** | Prod disk only — before merge of `origin/main` into OUT-VIEW branch (local tag on prichindel). |
| **`backup/pre-align-20260518-*`** | Alunel disk only — before hard reset to prod (local tag). |

```bash
# Return to this rollback line (after tag exists on remote)
git fetch --all --tags
git checkout main
git reset --hard hesperia/rollback-line-20260518

# Return to pre-merge prod work (prichindel clone only, if tag exists)
git checkout backup/pre-align-20260518
```

Brain repo pointer (team/process, not product code): `cluster/HESPERIA-REPOS-AND-HOSTS.md` in **igareosh/cursor**.

**Live URLs (Authentik):** `https://hesperia.prichindel.com/inspector/1-11-09-2023/` · `https://hesperia.prichindel.com/hex-matrix/`
