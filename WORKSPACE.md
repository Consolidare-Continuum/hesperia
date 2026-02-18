# Hesperia workspace — canonical paths and ingest

**Updated**: 2026-02-16

**Formal project**: Hesperia is onboarded as prichindel.com development under prichindel.com brand; author and owner Platonov Igor (igareosh); idea and implementation rights reserved by prichindel.com and igareosh. Governance: [projects/hesperia/](../../projects/hesperia/) (PROJECT-CHARTER, CONTEXT-PACKET, etc.).

---

## hesperia_workspace (canonical)

| What | Path |
|------|------|
| **hesperia_workspace** | **`/data/workspaces/hesperia`** (prichindel) |
| **Role** | Last operational state of all Hesperia files. Git-included clone on prichindel. Canonical codebase and specs. |
| **Cursor brain** | **CLIENTS/hesperia/** in this repo (Proton) — design anchor, docs, numbered specs; feed Gena from here + workspace. |

- **Clone**: hesperia_workspace on prichindel = `/data/workspaces/hesperia` (git repo; remote TBD — see [cluster/GITHUB-REPOS.md](../../cluster/GITHUB-REPOS.md)).
- **Point**: prichindel clone is **pointed at** `/data/workspaces/hesperia`; no separate “prichindel” path as the root — the root **is** `/data/workspaces/hesperia`.

---

## Ingest / sync (prichindel)

- **Check what’s new**: Canonical workspace = `/data/workspaces/hesperia`. Prichindel content moved to cursor repo `prichindel/` (2026-02-09). Sync from workspace root or cursor repo as needed; do not use `-f` when copying.
- **Scope (Grace)**: Sync in repo = documentation, description, scripting only. **Exclude** book .md files in **syzif/** folder from sync into repo. **No semantic layer yet.** Ref: [projects/hesperia/SCOPE-AND-SYNC.md](../../projects/hesperia/SCOPE-AND-SYNC.md).

---

## Archive (Proton text)

- **All and any text** that exists in Proton for Hesperia (i.e. **CLIENTS/hesperia/** in the cursor repo) is **archived** under **CLIENTS/hesperia/archive/**.
- Dated snapshots of Proton-resident hesperia text can be stored in `archive/` (e.g. `archive/YYYY-MM-DD_proton_hesperia/` or tarball) so that:
  - **Last operational state** = `/data/workspaces/hesperia` on prichindel (git, canonical).
  - **Proton** = design anchor + archive of text; archive folder holds snapshots when needed.

See [archive/README.md](archive/README.md).

---

## References

- [CLIENTS.md](../../CLIENTS.md) — clients list, hesperia paths.
- [.cursor/rules/gena-hesperia.mdc](../../.cursor/rules/gena-hesperia.mdc) — Gena when assigned to hesperia.
- [cluster/GITHUB-REPOS.md](../../cluster/GITHUB-REPOS.md) — hesperia local path, OpenAI key location.
