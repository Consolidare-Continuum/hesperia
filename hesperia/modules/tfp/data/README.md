# TFP module data (`hesperia/modules/tfp/data/`)

**Target layout (module-only `tfp_v1/`):** [`TFP_V1_LAYOUT.md`](TFP_V1_LAYOUT.md).

## Populate

1. **First-time / full tree:** `bash tools/migrate_research_tfp_to_module_tfp_v1.sh` (one-shot; read-only on `research/` if still present).
2. **Refresh dict faces from assets:** `bash tools/sync_tfp_module_data.sh`  
   - Optional **`HESPERIA_TFP_SYNC_STRICT=1`** — fail if `tfp_v1/dict_a/runtime/dict_a.jsonl` missing after sync.

**Canonical runtime** still loads from **`assets/`** until loader ADR [`ADR-TFP-DATA-T13-MODULE-LOADER.md`](../../../../docs/governance/ADR-TFP-DATA-T13-MODULE-LOADER.md) is implemented in code.

## Legacy mirror (`corpus/`, `dicts/`)

Older **`corpus/*`** / **`dicts/*`** paths may remain empty or stale; **`tfp_v1/`** is the operational SSoT per [`ETHAN-TFP-MODULE-ONLY-DICT-SSOT-2026-03-28.md`](../../../../docs/governance/working/ETHAN-TFP-MODULE-ONLY-DICT-SSOT-2026-03-28.md).

Large trees are **gitignored** under `tfp_v1/`; run migrate/sync after clone.

**Session transcripts** (clinical `.md`): `tfp_v1/corpus/sessions/` — populated by `tools/noone_sessions_ingest.py` or rsync from `research/_noone_local/sessions/` during migrate.

## Resolver

**`HESPERIA_TFP_MODULE_DATA_ROOT`** — see `tools/tfp_v1_paths.py` and the ADR above.
