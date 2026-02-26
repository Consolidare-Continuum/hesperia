# Hesperia consolidation — single repo (Abelard)

**Date**: 2026-02-26  
**Task**: Move all Hesperia-related content into this repo (`/data/hesperia/hesperia`). No deletes; overwrite only when a newer version was brought in. Cursor files preserved where present. Next: connect to one Atomic Commits repo and run to find missings/trash; Cursor to handle files.

---

## Sources merged (bottom-up)

| Source | What was done |
|--------|----------------|
| **This repo** | Existing content kept. Base: scripts/, governance/, project/, sphere_rag/, archive/v0.1. |
| **`/data/workspaces/cursor/CLIENTS/hesperia`** | Rsync with `--update`: added all missing files; updated only where source was newer. Excluded: `.git`, `.venv*`, `__pycache__`, `*.pyc`, `.env`. |
| **`/data/workspaces/atomic-commit-hesperia`** | Same rsync rules: merge into this repo (newer/missing only). |
| **`/data/workspaces/hesperia`** | Same rsync rules: merge into this repo. |
| **Cursor cluster config** | Copied `hesperia.prichindel.com.conf` and `hesperia-api.service` into **`cluster/`** in this repo. |

---

## What is in this repo now

- **Root**: Numbered specs (00–52), ACADEMIC.md, AGENTS.md, DOC_INDEX.md, WORKSPACE.md, RUNNABLE.md, VARIABLES.md, OPERATIONAL_INDEX, guard_config, requirements-*, etc.
- **api/** — Hesperia Analyze API (FastAPI): `main.py`, GPT-ACTIONS-SETUP.md, README_ACTIONS.md (hesperia.prichindel.com).
- **cluster/** — Deploy: `hesperia.prichindel.com.conf`, `hesperia-api.service`.
- **scripts/** — matrix_run, context_rag, ingest_hesperia_families, hesperia_logic, phase_traversal, plus archive scripts (canonicalize_surface_v040, run_build_v040_embeddings, etc.).
- **sphere_rag/** — Core engine, layers, tests (geometry, phase_engine, semantic_engine, build_v040, attribution, etc.).
- **hesperia_lex/** — Dict A/B, curated, frozen, definitions (v0412, v0413, v0414), scripts.
- **assets/** — v040, v0413, v0414, v06, v060 (surface maps, dict_b, manifests, reports).
- **governance/** — All task and report docs (CONTEXT-RAG, RAG-DAEMON-MVP, FAMILIES-CHROMA, etc.).
- **project/** — Charter, CONTEXT-PACKET, SCOPE-AND-SYNC, etc.
- **docs/** — Freeze docs, procedures, operational specs, runtime output.
- **archive/** — v0.1, api, docs, hesperia_lex, layer_runners, releases, scripts, sphere_rag.
- **calibration/** — Data and README.
- **releases/** — Release notes.
- **CLIENTS/hesperia/** — Nested copy (from atomic-commit workspace); can be pruned or kept for reference.

---

## Cursor files

- **.cursor/** in the cursor-repo copy (`/data/workspaces/cursor/CLIENTS/hesperia/.cursor`) was not copied (path/glob issue or missing). If you need it, copy manually from there into this repo.
- No other Cursor-specific files were deleted; existing ones in this repo are unchanged.

---

## Policy applied

- **No deletes** of existing files.
- **Overwrite only** when the incoming file was newer (rsync `--update`).
- **Add-only** for everything that did not exist here.

---

## Next steps (you)

1. **Connect this repo to one Atomic Commits repo** (e.g. set `origin` to `git@github.com:Atomic-Commits-Team/hesperia.git` and pull/push as needed).
2. **Run against it** — run builds/tests/API to surface **missings** or **trash**.
3. **Let Cursor handle files** — open this repo in Cursor; use it to audit structure, duplicates, and cleanup (e.g. CLIENTS/hesperia, archive vs live, .gitignore).

**Signed: Abelard (consolidation) | 2026-02-26 | this repo**
