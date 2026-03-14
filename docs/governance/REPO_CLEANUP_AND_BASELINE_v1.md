# Repo cleanup and baseline v1

**Purpose:** Full backup first, then identify minimal active structure, detect unused files, quarantine legacy, tag clean baseline, and maintain remote backups.

---

## 1. Freeze full raw backup (do this first)

Before touching the repository, snapshot everything exactly as it is.

**From repo root:**

```bash
./tools/backup_hesperia_full.sh
```

This creates:

- **git mirror:** `hesperia-backup/git-mirror/hesperia_backup.git` (full commit history, branches, tags, reflog).
- **Working-tree snapshot:** `hesperia-backup/snapshots/hesperia_full_repo_snapshot_YYYYMMDD.tar.gz` (exact state including `.git`).

**Two copies on remote (your credentials, sudo no pass):**

```bash
./tools/sync_backup_to_remotes.sh
```

Syncs the same backup to:

- `fulgusor:/mnt/heimdall/hesperia-backup/`
- `fulgusor:/mnt/arc/hesperia-backup/`

Override backup location or remote with env:

- `HESPERIA_BACKUP_ROOT` — where `hesperia-backup/` is written (default: sibling of repo).
- `HESPERIA_BACKUP_REMOTE` — SSH host (default: `fulgusor`).

---

## 2. What should remain in the clean repo

Minimal active structure:

```
runtime/
core/
lexicon/
assets/
tools/
release/
examples/
docs/governance/
docs/audit/
build_shipping.sh
release_sealed_runtime.sh
requirements*.txt
Dockerfile.shipping
README.md
```

Everything else should be reviewed. If a file is not needed to **run**, **build**, **test**, or **ship**, it does not belong; archive or move to `legacy/`.

---

## 3. Detect unused files automatically

**From repo root:**

```bash
./tools/detect_unused.sh
```

This runs:

- **Vulture:** `pip install vulture` then `vulture .` — unreferenced functions, dead modules, unused variables.
- **Large tracked files:** `git ls-files | xargs du -h | sort -rh | head -30` — find old datasets, unused binaries, legacy builds.
- **Old-script patterns:** files matching `run_*.py`, `*_old.py`, `*_backup.py`, `debug_*.py`.
- **No-import Python files:** `git grep -L "import" -- '*.py'` — often abandoned scripts.

Use the output to decide what to move to `legacy/`.

---

## 4. Move legacy content (do not delete yet)

Create a single quarantine under `legacy/` and move suspected artifacts there first.

Example layout:

```
legacy/
├── old_pipelines/
├── deprecated_scripts/
├── historical_specs/
├── debug_tools/
```

Example:

```bash
git mv path/to/old_thing legacy/deprecated_scripts/
git commit -m "quarantine: move old_thing to legacy"
```

If something breaks later, recovery is trivial (move back or restore from backup).

---

## 5. After verification, remove legacy

Once the system builds and runs correctly:

```bash
./release_sealed_runtime.sh   # must pass
pytest tests/test_sealed_runtime_regression.py -q
```

Then:

```bash
git rm -r legacy
git commit -m "cleanup: remove legacy artifacts"
```

---

## 6. Shrink repository history (optional)

Only if the repo has historically accumulated large blobs:

```bash
pip install git-filter-repo
git filter-repo --strip-blobs-bigger-than 10M
```

**Warning:** This rewrites all commits. Only do it if you understand Git history rewriting. Often unnecessary if the repo is not huge.

---

## 7. Tag a clean baseline

Create a permanent checkpoint:

```bash
git tag -a v0.4.1_clean -m "Clean sealed runtime baseline"
git push origin v0.4.1_clean
```

This becomes the recovery point.

---

## 8. Secondary GitHub mirror (disaster recovery)

Create a private repo (e.g. `hesperia-dev-backup`) and add a mirror remote:

```bash
git remote add backup https://github.com/.../hesperia-dev-backup.git
git push backup --mirror
```

Push regularly (or via CI) for offsite storage and protection against repo corruption.

---

## 9. .gitignore protections

Already present or added:

- `dist/`
- `release/*.tar`, `release/*.tar.gz`, `release/*.bin`
- `*.log`, `*.tmp`
- `__pycache__/`, `*.pyc`

Prevents future junk from being committed.

---

## 10. Final repo layout (target)

```
hesperia/
├── runtime/
├── core/
├── lexicon/
├── assets/
├── tools/
├── examples/
├── release/
├── docs/
│   ├── governance/
│   └── audit/
├── Dockerfile.shipping
├── build_shipping.sh
├── release_sealed_runtime.sh
├── requirements.txt
├── README.md
```

Everything else should be gone (or under `legacy/` until removed after verification).

**Rule:** If a file is not needed to run, build, test, or ship, it does not belong. Archive it as specified in §1 and §8.

---

*See tools/backup_hesperia_full.sh, tools/sync_backup_to_remotes.sh, tools/detect_unused.sh.*
