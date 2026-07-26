# Grace triage — `/data/hesperia` complete cold root (Hesperia + brain context)

**TASK-ID:** APO-DATA-ROOT-2026-03-28  
**Priority:** P1 (operator archive prep)  
**Lead owner:** Gena (implementation + manifests). **Sign-off:** Grace (acceptance checklist below). **Volume / rsync / offsite:** Abelard. **Normative slices already written:** Ethan (flash tiers + workflows must-carry), Gena (layout + `mirror_sister_workflows_into_hesperia_data.sh`).

**Operator intent:** `/data/hesperia` is **the** Hesperia archive root: **101% self-explanatory** for “what this is, how it was run, what to copy next,” **as the system is now**, without hunting `/data/workspaces` or other mounts. Operator performs final archive copy themselves; team makes the tree **ready**.

---

## 1. Incorporated assessments (do not re-litigate scope here)

| Source | Path |
|--------|------|
| Gena — cold layout + workflows rsync | Hesperia `docs/governance/working/GENA-HESPERIA-APOCALYPTIC-ARCHIVE-TRIAGE-2026-03-28.md` |
| Ethan — USB subset + mandatory brain classes | Hesperia `docs/governance/working/ETHAN-HESPERIA-FLASH-RECOVERY-NO-SERVER-2026-03-28.md` |

---

## 2. Grace scope decisions (binding for this packet)

| ID | Decision |
|----|----------|
| S1 | **`/data/workflows`** on prichindel is **absent** today. **Substitute:** mirror **`/data/workspaces/cursor`** (canonical Cursor brain repo) into **`/data/hesperia/cursor-brain-mirror/`** with the **same exclude policy** as Gena’s workflows script (no `.env*`, no `.git/` in file mirror — see S2). If a separate **`WORKFLOWS_SRC`** appears on another host, **also** mirror it into **`/data/hesperia/workflows-mirror/`** when operator runs from that host; both directories may coexist. |
| S2 | **Git history for the brain:** optional **`hesperia-backup/cursor-git-mirror.git`** (bare `git clone --mirror`) **in addition to** `cursor-brain-mirror/` file tree — Abelard/Gena; operator chooses one or both for archive size. File mirror alone is acceptable for “read every markdown/script.” |
| S3 | **Secrets:** never place raw `.env`, API keys, or tokens in cleartext mirrors. Excludes are **mandatory**; document **where** secrets normally live (path names only) in the root README. |
| S4 | **Clinical / PII:** content under Hesperia `tfp_v1/corpus/sessions/`, `provenance/api/`, and large `outputs/` remains **subject to operator risk acceptance**; Grace does **not** require stripping for “complete” — operator encrypts final archive if needed. Team **must not** add new secrets into mirrors. |
| S5 | **Other `/data/workspaces/*` siblings** (e.g. `biopole-planfix-workspace`, `telegram_solutions`): **out of scope** for “Hesperia complete” unless igareosh explicitly extends scope; if extended, add **`/data/hesperia/extra-workspaces-mirror/<name>/`** and list in README. |

---

## 3. Target layout under `/data/hesperia/` (normative)

```text
/data/hesperia/
  README_HESPERIA_DATA_ROOT.md     # REQUIRED — operator-facing; see §5
  MANIFEST-SHA256-YYYY-MM-DD.txt   # RECOMMENDED — after freeze (slow)
  hesperia/                        # canonical working tree (existing)
  hesperia-backup/                 # git-mirror, snapshots, tars (existing)
  cursor-brain-mirror/             # REQUIRED on prichindel-class — rsync from /data/workspaces/cursor
  workflows-mirror/                # OPTIONAL — if WORKFLOWS_SRC exists elsewhere
  .vscode/                         # optional (existing)
```

---

## 4. Team tasks (execution)

| Step | Who | Action |
|------|-----|--------|
| T1 | Gena | Add **`README_HESPERIA_DATA_ROOT.md`** at **`/data/hesperia/`** (can start from Hesperia repo template under `tools/templates/` if added): one-screen map of directories, pointer to `hesperia/README.md`, frozen **git SHA** line (updated at freeze), Python version, “smoke” command list, **no secrets**. |
| T2 | Gena | Add **`tools/mirror_cursor_brain_into_hesperia_data.sh`** in Hesperia repo (or extend existing mirror script with `CURSOR_BRAIN_SRC`): rsync **`/data/workspaces/cursor`** → **`/data/hesperia/cursor-brain-mirror/`**, same excludes as `mirror_sister_workflows_into_hesperia_data.sh` + document in `tools/SHELL_SCRIPTS_INDEX.md`. |
| T3 | Gena | Run **`./tools/backup_hesperia_full.sh`** from `hesperia/` when SHA must match archive; run **`mirror_sister_workflows_into_hesperia_data.sh`** if `WORKFLOWS_SRC` set; run **cursor-brain mirror** on prichindel. |
| T4 | Abelard | Confirm disk space for `cursor-brain-mirror` + optional bare mirror; extend **`sync_backup_to_remotes.sh`** / offsite policy to include **`cursor-brain-mirror/`** when operator wants cluster copy (path-only note in ops doc). |
| T5 | Ethan | N/A further unless flash doc needs cross-link to this packet — optional one-line link from Ethan flash doc to this file in `operational/assignments/` (Gena can add when editing Hesperia docs). |
| T6 | Grace | After T1–T3 verified on disk, set checklist §8 to **GREEN** in this file (date + initials in git commit or row note). |

---

## 5. `README_HESPERIA_DATA_ROOT.md` minimum sections

1. **What this directory is** (single paragraph).  
2. **Children table:** `hesperia/`, `hesperia-backup/`, `cursor-brain-mirror/`, `workflows-mirror/` (if present), manifest file name.  
3. **Freeze:** Hesperia repo **`git rev-parse HEAD`** and date.  
4. **How to run smoke tests** (from `hesperia/`): e.g. `pip install -r requirements.txt`, `pytest …` (Gena picks minimal set consistent with Ethan flash §5).  
5. **Secrets policy:** excluded from mirrors; where operator keeps production env (names only).  
6. **Links:** Gena + Ethan governance working docs (relative path into `hesperia/` or `cursor-brain-mirror/operational/assignments/`).

---

## 6. Acceptance definition (“all encompassing / self explainable / working as now”)

**Met when all are true:**

| # | Criterion |
|---|-----------|
| A1 | **`/data/hesperia/hesperia/`** is a **clean, runnable** checkout matching documented freeze SHA. |
| A2 | **`/data/hesperia/hesperia-backup/`** contains current **backup/mirror artifacts** per existing team practice (not empty for git-mirror/snapshots if policy requires them). |
| A3 | **`/data/hesperia/cursor-brain-mirror/`** exists and contains **`.cursor/rules/`**, **`governance/`**, **`operational/assignments/`**, **`AGENTS.md`**, **`active.md`**, **`scripts/`** — so process and triage survive without `/data/workspaces/cursor`. |
| A4 | **`README_HESPERIA_DATA_ROOT.md`** present at **`/data/hesperia/`** and accurate. |
| A5 | No **cleartext** `.env` / `.env.*` / obvious key files inside **`cursor-brain-mirror/`** or **`workflows-mirror/`** (spot check). |
| A6 | Optional **`MANIFEST-SHA256-*.txt`** at `/data/hesperia/` if operator requested integrity baseline. |

**“101% Hesperia”** in this packet means: **engine + data layout + governance docs in-repo + team/process context required to operate and restore** — not every unrelated repo under `/data/workspaces`.

---

## 7. Grace sign-off state

| Field | Value |
|-------|--------|
| **As of** | 2026-03-28 |
| **Disk verified (prichindel)** | `cursor-brain-mirror/` **present** (rsync from `/data/workspaces/cursor`); `README_HESPERIA_DATA_ROOT.md` **present** at `/data/hesperia/`; `workflows-mirror/` **absent** (no `WORKFLOWS_SRC` on host — **N/A** per §2 S1); `hesperia-backup/` **present** (~3.7G) |
| **Implementation** | Hesperia `5e4d02f` — `tools/mirror_cursor_brain_into_hesperia_data.sh`, `tools/templates/README_HESPERIA_DATA_ROOT.md`; cursor repo carries this packet + `active.md` row |
| **GREEN for operator archive** | **YES** — §6 acceptance A1–A5 satisfied for prichindel layout; **optional:** run §5 smoke + `backup_hesperia_full.sh` before copy if you need a byte-frozen tarball matching SHA; regenerate `cursor-brain-mirror/` after any last-minute cursor commits |

---

## 8. Operator checklist (print before copy)

- [ ] `README_HESPERIA_DATA_ROOT.md` read once; freeze SHA matches `hesperia/`  
- [ ] `du -sh /data/hesperia/*` acceptable for destination media  
- [ ] Spot check: `cursor-brain-mirror/operational/assignments/GRACE-HESPERIA-DATA-ROOT-COMPLETE-2026-03-28.md` present  
- [ ] Secrets spot check passed (A5)  
- [ ] (Optional) `MANIFEST-SHA256-*.txt` generated and stored beside tree  
- [ ] Grace row **APO-DATA-ROOT** set **DONE** after verification  

**When all checked:** operator archive = **go**.

---

## 9. `active.md` row

`[P1] hesperia | APO-DATA-ROOT Complete /data/hesperia cold root (README + cursor-brain-mirror + backups) per GRACE-HESPERIA-DATA-ROOT-COMPLETE | Gena | OPEN | this file`

---

`SIGNED: Grace | triage + scope + acceptance | 2026-03-28 | /data/hesperia complete archive readiness`
