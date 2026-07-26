# Ethan — Hesperia 0.6.3 sealed (GitHub archive)

**Date:** 2026-06-14  
**Entity:** Ethan (governance)  
**Repo:** `igareosh/hesperia` (`alunel:/data/workspaces/atomic-commit-hesperia`)  
**Tag:** `hesperia-0.6.3`

---

## Seal result

| Check | Result |
|-------|--------|
| `tools/run_063_archive_e2e_gate.sh` | **PASS** |
| `tools/system_seal.run_system_seal` | **PASS** (`release/v0.6.3/system_seal.json`, version **0.6.3**) |
| `tests/test_archive_063_e2e_gate.py` | **PASS** (offline analyze, no prod dict) |
| `dist/hesperia-0.6.3-archive.zip` | Built; checksum in `release/v0.6.3/checksums.txt` |

**Dict/corpus policy:** Archive **excludes** prod sealed packs (`v0_6_0_clr_*`) and corpus trees. E2E uses `HESPERIA_DICT_CALIB_OFFLINE=1` + `archive_063_minimal` pin.

---

## Artifacts in product repo

| Path | Role |
|------|------|
| `VERSION.yaml` | `system_version: "0.6.3"`, `archive.*` block |
| `release/v0.6.3/examples/` | Demo outputs: analyze, envelope, Teacher, IRC trace, MySQL shape |
| `docs/specs/0.6.3-IRC-TEACHER-RUN.md` | Application run contract |
| `assets/calibration/dicts/archive_063_minimal/` | Placeholder (no prod JSONL) |
| `tools/run_063_archive_e2e_gate.sh` | Runnable gate |
| `tools/build_063_github_archive.sh` | `git archive` → zip |
| `tests/test_archive_063_e2e_gate.py` | Fast pytest gate |
| `runtime/shipping/env_guard.py` | `HESPERIA_KSI_*` allowlist |

---

## GitHub release (operator)

```bash
cd /data/workspaces/atomic-commit-hesperia
git checkout hesperia-0.6.3
./tools/build_063_github_archive.sh
# Upload dist/hesperia-0.6.3-archive.zip to GitHub Releases
```

**Integration:** Live 0.6.3 Teacher path remains on **tersagor VM** `0149120` + prod `/analyze` on prichindel — not inside this zip.

---

## Status

**0.6.3 pre-release → SEALED** for GitHub archive distribution. **0.7.0** graph apply unchanged out of scope.

SIGNED: Ethan | 0.6.3 archive seal | 2026-06-14 | igareosh/hesperia hesperia-0.6.3
