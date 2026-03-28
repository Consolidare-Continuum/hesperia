# `/data/hesperia` — Hesperia cold data root

**Purpose:** Single directory that holds the **Hesperia product tree**, **backups**, and a **read-only mirror of the Cursor brain repo** (rules, governance, operational assignments) so recovery does not depend on `/data/workspaces/cursor`.

**Freeze (update when archiving):**

| Field | Value |
|-------|--------|
| Date | `YYYY-MM-DD` |
| Hesperia `git` SHA | `RUN: git -C hesperia rev-parse HEAD` |

## Layout

| Path | Contents |
|------|----------|
| `hesperia/` | Canonical Hesperia git working tree (`Atomic-Commits-Team/hesperia`). |
| `hesperia-backup/` | Git mirror, tar snapshots, cold copies per team scripts. |
| `cursor-brain-mirror/` | Rsync of `/data/workspaces/cursor` (no `.git/`, no `.env*`). Regenerate: `hesperia/tools/mirror_cursor_brain_into_hesperia_data.sh`. |
| `workflows-mirror/` | Optional; only if `WORKFLOWS_SRC` was mirrored from another host (`mirror_sister_workflows_into_hesperia_data.sh`). |
| `MANIFEST-SHA256-*.txt` | Optional integrity manifest over this tree. |

## Smoke (from `hesperia/`)

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python3 -m pytest tests/test_release_version.py
```

(Adjust if your environment uses a different minimal test set; see Ethan flash recovery doc in `hesperia/docs/governance/working/`.)

## Secrets

Mirrors **exclude** `.env` and `.env.*`. Production secrets stay in operator-controlled stores only — not in this tree.

## References (inside `hesperia/`)

- `docs/governance/working/GENA-HESPERIA-APOCALYPTIC-ARCHIVE-TRIAGE-2026-03-28.md`
- `docs/governance/working/ETHAN-HESPERIA-FLASH-RECOVERY-NO-SERVER-2026-03-28.md`
- `operational/assignments/GRACE-HESPERIA-DATA-ROOT-COMPLETE-2026-03-28.md` (under `cursor-brain-mirror/` after mirror)
