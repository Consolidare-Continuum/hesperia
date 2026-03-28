# Operator runbook — archive `research/_noone_local` corpus after `tfp_v1` migration (TFP-DATA-T19)

**Pre:** `bash tools/migrate_research_tfp_to_module_tfp_v1.sh` completed; `MANIFEST.yaml` + DLCR gold pytest green.

**Steps (operator / Abelard):**

1. `tar -czvf tfp_noone_local_archive_$(date +%F).tar.gz research/_noone_local` from Hesperia repo root (store under cluster backup policy, not necessarily in Git).
2. Verify tarball lists `2_cleaned/` and `english_2_cleaned/`.
3. Remove **`research/_noone_local/2_cleaned`** and **`english_2_cleaned`** only if duplicate of `tfp_v1/corpus/original/**` (checksum spot-check).
4. **Do not** delete **`research/reports/`** or other research scopes unless a separate governance row exists.

`SIGNED: Cursor (Abelard lane) | TFP-DATA-T19 | 2026-03-28`
