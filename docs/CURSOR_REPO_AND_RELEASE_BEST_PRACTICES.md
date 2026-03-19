# Cursor: repo hygiene, release consolidation, and GitHub sync

Use this **before every push** to `origin` (GitHub), especially on sealing branches (`release/v0.5.0-seal`) or after Tasks 1–6 work.

## 1. Principles

| Rule | Why |
|------|-----|
| **One logical change per branch** | Easier review, bisect, and rollback. |
| **No drive-by refactors** with feature work | Reduces churn and fake “done” states. |
| **Boundaries before polish** | Fix imports, projection, and version truth before README/docs-only sweeps. |
| **Never tag without audit artifacts** | Tag only when `release/v0.5.0/final_gate_status.json` allows it (see below). |

## 2. Pre-push checklist (minimum)

Run from repository root after activating your venv (if any).

```bash
# 2.1 Version authority (Task 1)
python3 tools/validate_version_consistency.py

# 2.2 Product surface (Task 4)
python3 tools/audit_public_surface.py

# 2.3 Tests (adjust scope if needed; full suite before merge to main)
python3 -m pytest tests/ -q --tb=no

# 2.4 Optional: Phase 0 inventory (large repo scan)
# python3 tools/seal_phase0_inventory.py
```

**Stop** if any command exits non-zero; fix, then re-run.

## 3. Pre-push checklist (release / seal consolidation)

Do this **before** pushing a branch that claims **v0.5.0 sealed** or updates `release/v0.5.0/`.

```bash
export HESPERIA_RELEASE_BUILD_TIMESTAMP="$(date -u +%Y-%m-%dT%H:%M:%SZ)"   # or a fixed ISO instant for reproducible JSON

# Full audit (no --quick): required for honest seal + release_audit: pass
python3 tools/release/build_release_audit_v0_5_0.py
```

Verify:

- `release/v0.5.0/final_gate_status.json` → `sealed: true`
- `critical_checks.release_audit` → `pass` (not `quick_subset_only`)
- `git status` → **clean** (no uncommitted release artifacts unless you intend to commit them)

**Do not** `git tag v0.5.0` if `sealed` is false or the tree is dirty.

Full execution order: [CODEX_EXECUTION_CHECKLIST_v0_5_0_SEAL.md](CODEX_EXECUTION_CHECKLIST_v0_5_0_SEAL.md).

## 4. Git / GitHub sync (Cursor-friendly)

1. **Fetch and rebase or merge** main before opening a PR:
   - `git fetch origin && git rebase origin/main` (or merge if team policy).
2. **Meaningful commits** — imperative subject, body for *why* when touching boundaries or release files.
3. **No secrets** — never commit API keys, `.env`, or license blobs; `.gitignore` already excludes common cases.
4. **Large binaries** — Docker tars / CLI binaries under `release/` or `dist/` are often gitignored; attach to releases or CI artifacts instead of bloating history.
5. **Push**:
   - `git push -u origin <branch>`
   - Open PR on GitHub; paste checklist results (pytest + validators) in description for seal-related PRs.

## 5. What to commit vs ignore

| Commit | Usually ignore (local / CI) |
|--------|-----------------------------|
| Source, specs, `VERSION.yaml`, policies, tests | `tmp/*` (except `tmp/.gitkeep`), `.venv/`, `outputs/*` |
| Curated `release/v0.5.0/*.json` when sealing | Ad-hoc `tmp/repo_inventory.txt` unless you want a snapshot |
| `assets/artifacts/e2e/*.json` when policy says so | Full dynamics bundles per `GENERATED_ARTIFACT_POLICY.md` |

See [REPO_STRUCTURE_POLICY.md](../REPO_STRUCTURE_POLICY.md), [GENERATED_ARTIFACT_POLICY.md](../GENERATED_ARTIFACT_POLICY.md).

## 6. Cursor-specific tips

- **Workspace root** must be the Hesperia repo root (where `pyproject.toml`, `VERSION.yaml`, `runtime/` live).
- **AGENTS.md** is the canonical agent contract; keep commands in README aligned with it.
- After moves/renames, run **Pyright / Pylance** or `python3 -m compileall` on touched packages.
- Prefer **terminal in repo root** for `python3 -m pytest` and `python3 -m runtime...` so `PYTHONPATH` matches CI.

## 7. README and GitHub

- **Single source for “what the product is”** on GitHub: root **README.md**.
- Deep dives stay in **docs/**; README should link, not duplicate spec text.
- When you change behavior (API paths, CLI name, seal process), **update README in the same PR**.

---

*Hesperia Engine Dynamics v0.5 — inspection and reference only per [LEGAL_NOTICE.md](../LEGAL_NOTICE.md).*
