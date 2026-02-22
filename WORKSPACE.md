# Hesperia workspace — canonical path and sync

**Updated**: 2026-02-22

**Formal project**: Hesperia is onboarded as prichindel.com development under prichindel.com brand; author and owner Platonov Igor (igareosh); idea and implementation rights reserved by prichindel.com and igareosh. Governance: [projects/hesperia/](../../projects/hesperia/) (PROJECT-CHARTER, CONTEXT-PACKET, etc.).

---

## Canonical repo and workspace

| What | Path / URL |
|------|------------|
| **GitHub (source of truth)** | **`git@github.com:Atomic-Commits-Team/hesperia.git`** |
| **hesperia workspace** | **`/data/workspaces/atomic-commit-hesperia`** (prichindel) |
| **Role** | Single source for specs, sphere_rag, API. Hesperia Analyze API (hesperia.prichindel.com) runs from here. |
| **Cursor brain** | **CLIENTS/hesperia/** in this repo — design anchor, numbered specs; synced from workspace (replace same name, add new). |

- **Old repo** `https://github.com/igareosh/hesperia` is **unlinked** and will be deleted; do not use.

---

## Sync (prichindel)

- **Pull from GitHub**: `cd /data/workspaces/atomic-commit-hesperia && git pull`.
- **Update cursor brain**: Copy specs/docs from workspace into **CLIENTS/hesperia/** (same naming → replace; new files → add). Exclude: `.git`, `venv`, `logs`, `api/` (code stays in hesperia repo). Ref: [projects/hesperia/SCOPE-AND-SYNC.md](../../projects/hesperia/SCOPE-AND-SYNC.md) for scope.

---

## Archive (Proton text)

- **CLIENTS/hesperia/archive/** — archived Proton text. See [archive/README.md](archive/README.md).

---

## References

- [CLIENTS.md](../../CLIENTS.md) — clients list, hesperia path.
- [.cursor/rules/gena-hesperia.mdc](../../.cursor/rules/gena-hesperia.mdc) — Gena when assigned to hesperia.
- [cluster/GITHUB-REPOS.md](../../cluster/GITHUB-REPOS.md) — hesperia path, OpenAI key location.
