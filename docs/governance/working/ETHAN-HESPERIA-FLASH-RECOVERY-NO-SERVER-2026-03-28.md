# Flash-drive recovery bundle — Hesperia when server / disk recovery is impossible

**Ethan lane — normative scope for Gena implementation.**  
**Assumption:** No prichindel, no GitHub, no cluster; one **USB stick** (or encrypted SSD) is the only artifact. **Build target:** reproduce *buildable + runnable* Hesperia on a clean Linux laptop with Python only.

**Related:** [`GENA-HESPERIA-APOCALYPTIC-ARCHIVE-TRIAGE-2026-03-28.md`](GENA-HESPERIA-APOCALYPTIC-ARCHIVE-TRIAGE-2026-03-28.md) (full `/data/hesperia` tree + `workflows-mirror`). This note **narrows** that picture to **flash-sized tiers** and names what from **`/data/workflows`** (mirrored into the archive) is **non-optional** for “we remember how to run the company + engine.”

---

## 1. Flash layout (single mount point, e.g. `HESPERIA_FLASH/`)

```text
HESPERIA_FLASH/
  README_RECOVERY.txt              # 1 page: Python version, pip install -r, smoke commands
  MANIFEST-SHA256.txt                # sha256 of every file under flash (or per-tar)
  00_git_bundle/
    hesperia_repo.tar.gz             # working tree + .git OR bare mirror + sparse checkout script
  01_min_runtime/
    requirements-pinned.txt          # copy from repo + python version line
    lexicon_curated.tar.gz           # if full repo too big: at least curated subset (see tiers)
  02_calibration/
    dict_pack_<VERSION>.tar.gz       # assets/calibration/dicts/<pack>/ minimal set
    engine_dynamics_v060_subset.tar.gz  # optional if dict pack not self-contained
  03_tfp_module_data/
    tfp_v1_sessions_and_corpus.tar.gz   # clinical + RU/EN if policy allows (Grace)
  04_workflows_mirror/
    (full rsync tree)                # see §4 — this is the “/data/workflows” archive
  05_optional_outputs/
    dict_calibration_redacted.tar.gz # only if size allows; else omit
```

**Rule:** Nothing under `04_workflows_mirror/` is a substitute for `00_git_bundle/` — workflows hold **process + brain links**, not the engine source of truth.

---

## 2. Tiers (pick by stick size; Gena encodes in build script)

| Tier | Goal | Rough order of magnitude (indicative) | Must include |
|------|------|----------------------------------------|--------------|
| **A — Minimal** | Reinstall deps, run unit smoke, read specs | ~2–8 GB if lexicon trimmed | Full repo **or** tarball; `requirements.txt` / lock; **default calibration pack** under `assets/calibration/dicts/<pack>/` as tar; `README_RECOVERY.txt`; **workflows mirror** (§4) |
| **B — TFP lab** | RU corpus + sessions + module `tfp_v1` faces | +5–40 GB | Tier A + `tfp_v1/` corpus/sessions + synced dict faces from `sync_tfp_module_data` equivalent |
| **C — Forensics** | Calibration history + API provenance | +remaining space | Tier B + redacted `outputs/dict_calibration` or `tfp_v1/provenance/.../outputs_dict_calibration_mirror` |

**Ethan order:** ship **Tier A + workflows** before debating B/C. Without workflows mirror, recovery is code without **runbooks, triage, assignments, Cursor rules**.

---

## 3. From `/data/hesperia` — what must land on the stick

1. **Hesperia repository** at a **pinned commit** (tag or `VERSION.yaml` + git SHA in `README_RECOVERY.txt`).
2. **`lexicon/curated`** (or documented subset if Tier A size-bound — Gena lists paths in manifest).
3. **Calibration SSOT** per [`HESPERIA_TFP_MODULE_DICTS.md`](../../HESPERIA_TFP_MODULE_DICTS.md): at minimum `assets/calibration/dicts/<HESPERIA_CALIB_DICT_VERSION>/` files needed for the smoke pipeline the README names.
4. **No secrets on cleartext flash:** exclude `.env`, `.env.*`, keys; recovery README says “copy from owner-encrypted store” only.

---

## 4. From `/data/workflows` (archive into `04_workflows_mirror/`) — Ethan “must carry”

Mirror **whole tree** with Gena’s rsync excludes, but **these classes are explicitly required** if present on source:

| Class | Why (no-server world) |
|-------|------------------------|
| **`.cursor/rules/`**, `.cursor/*.md` | Agent behaviour, Chroma/workflow compliance |
| **`operational/assignments/`**, `operational/partners/` | Triage packets, handoffs, acceptance |
| **`governance/`** (cursor brain) | Heartbeat, MCP policy, agreements |
| **`scripts/`** relevant to workflow / deploy | How to wire MCP, sync, detectors |
| **`AGENTS.md`**, `active.md` (if in repo root) | Entity + task truth |
| **Small skills / docs** under `.cursor` or `agent_mcp_knowledge/` | Setup without network |

**Optional if huge:** historical `archive/`, old FPF artifact trees — manifest-only + “second stick” policy.

---

## 5. Verification before ejecting USB

- `sha256sum` manifest matches tree.
- On **airgapped VM**: extract → `pip install -r` → `python3 -m pytest tests/test_release_version.py` (or agreed minimal set Gena lists).
- Open `04_workflows_mirror/operational/assignments/` and confirm **Grace triage** packet for flash build exists (self-referential check).

---

## 6. Tasking

- **Gena:** Implement `tools/build_flash_recovery_bundle.sh` (or extend mirror script) producing `HESPERIA_FLASH/` tiers A/B/C; consume `WORKFLOWS_SRC` → `04_workflows_mirror/`.
- **Grace:** Approve **clinical** and **PII** inclusion for Tier B/C.
- **Abelard:** Out of scope for flash **content**; in scope if encrypted **offsite copy** of the same tar.

---

`SIGNED: Ethan | governance / recovery scope | 2026-03-28 | flash bundle + workflows mirror requirements`
