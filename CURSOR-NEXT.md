# Cursor next — after consolidation

**Repo**: This folder is the consolidated Hesperia repo. All content from cursor CLIENTS/hesperia, atomic-commit-hesperia, and workspaces/hesperia has been merged here (add + update-only; no deletes).

**Ask Cursor to:**

1. **Audit structure** — List duplicates or redundant paths (e.g. `CLIENTS/hesperia/` vs root; `archive/` vs live `scripts/`, `sphere_rag/`).
2. **Suggest .gitignore** — Ignore `.venv*`, `__pycache__`, `.env`, large binaries, `hesperia_lex/raw/*.gz`, etc.
3. **Find missings** — After you connect to Atomic-Commits-Team/hesperia and run (e.g. `api/main.py`, build scripts, tests), report missing deps or broken imports.
4. **Find trash** — Identify files or dirs that are clearly obsolete or safe to archive/remove once a single source of truth is confirmed.

**Key entry points:**

- API: `api/main.py` (hesperia.prichindel.com)
- Deploy: `cluster/hesperia.prichindel.com.conf`, `cluster/hesperia-api.service`
- Scripts: `scripts/context_rag.py`, `scripts/matrix_run.py`, `scripts/ingest_hesperia_families.py`
- Specs: `DOC_INDEX.md`, numbered `*_SPEC__*.txt`, `governance/`

**Consolidation log**: See `CONSOLIDATION.md`.
