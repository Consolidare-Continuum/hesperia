# Hesperia TFP Module Dicts (Mainline)

**Operational SSoT (human + calibration tooling):** `hesperia/modules/tfp/data/tfp_v1/` — populated by `tools/migrate_research_tfp_to_module_tfp_v1.sh` and refreshed by `tools/sync_tfp_module_data.sh` (see `hesperia/modules/tfp/data/README.md`). **Sealed runtime** still reads **`assets/calibration/dicts/<version>/`** until loader code follows `docs/governance/ADR-TFP-DATA-T13-MODULE-LOADER.md`.

Canonical dict artifacts for TFP/module **runtime** are versioned under:

- `assets/calibration/dicts/<version>/dict_a.jsonl`
- `assets/calibration/dicts/<version>/dict_b.jsonl`
- `assets/calibration/dicts/<version>/links.jsonl`
- `assets/calibration/dicts/<version>/metrics.json`

## Runtime switch (single source of truth)

Set one environment variable before running engine/module pipelines:

- `HESPERIA_CALIB_DICT_VERSION=<version>`

Example:

`HESPERIA_CALIB_DICT_VERSION=v0_6_0_clr_v052_2`

When set, runtime dictionary loading resolves from:

- `assets/calibration/dicts/${HESPERIA_CALIB_DICT_VERSION}/dict_a.jsonl`
- `assets/calibration/dicts/${HESPERIA_CALIB_DICT_VERSION}/dict_b.jsonl`

When not set (or missing), runtime falls back to legacy bundled assets under:

- `assets/data/engine_dynamics_v060/...`

## Non-research policy

Mainline runtime/module loading has no dependency on `/research` paths.
Calibration freeze output is consumed from `assets/calibration/dicts/...` only.

## Active calibration pack (`v0_6_0_clr_v052_2`)

**Default runtime** after **2026-03-28** (Ethan / igareosh unfreeze, DICT-CAL-02 B-gap closure): `assets/calibration/dicts/v0_6_0_clr_v052_2/` — same Dict **A** / **links** / **metrics** lineage as `v052_1`, plus **66** appended `dict_b.jsonl` rows (full engine `dict_b_tfp.jsonl` concept inventory). `TFP_CLUSTER_*` rows carry `hex_anchor` **HX-2609**–**HX-2615**.

## Sealed predecessor (`v0_6_0_clr_v052_1`) — immutable

The directory **`assets/calibration/dicts/v0_6_0_clr_v052_1/`** remains **immutable** (historical seal). **Do not edit** without **direct permission from igareosh**. Full rule: **`docs/governance/working/ETHAN-DICT-A-NORM-PROPOSE-ANCHOR-LOCK-2026-03-28.md`** (see amendment for successor pack).

## Module data mirror (interim)

Working copies of corpus + dict bundles live under **`hesperia/modules/tfp/data/tfp_v1/`** after **`tools/migrate_research_tfp_to_module_tfp_v1.sh`** (one-shot: `research/_noone_local` RU/EN corpus + **`sessions/`** → `tfp_v1/corpus/...`) and **`tools/sync_tfp_module_data.sh`** (dict faces from `assets/` only; no `research/`). Large mirrored trees are gitignored; see **`hesperia/modules/tfp/data/README.md`**. Runtime resolution remains `assets/` until loader ADR is implemented.

## After A is green: B then CD

Lexical **A** is closed when calibration validators pass. **Ethan order:** **B before CD** — stabilize concept identity / `dict_b` + calibration links first; **CD** only annotates existing `concept_id`s (see **`docs/governance/working/ETHAN-DICT-LAYER-ORDER-AFTER-A.md`**). Next execution wave: **B** validators + **CD** tests + CD-on smoke — **`tools/run_b_cd_wave_after_a.sh`** from repo root. Model chain: **`docs/governance/cd_v1/MODEL_CARD_CD_PIPELINE.md`** (`A` → `B` → `CD` → `C_agg` → Topology).

---

## v1 authoritative (TFP-V1-06)

This document is **authoritative for mainline TFP dict loading v1** with [`docs/governance/TFP_RESOLUTION_CONTRACT.md`](governance/TFP_RESOLUTION_CONTRACT.md). **`HESPERIA_CALIB_DICT_VERSION`** selects the directory name under `assets/calibration/dicts/`; it must stay consistent with **`VERSION.yaml`** `defaults.active_calibration_dict_pack` and `tfp_module_v1.pinned_calibration_dict_pack` (see `tools/validate_version_consistency.py`).

`SIGNED: Ethan (governance) | TFP module dicts v1 | 2026-03-28 | TFP-V1-06`

