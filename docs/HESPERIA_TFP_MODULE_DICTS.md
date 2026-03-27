# Hesperia TFP Module Dicts (Mainline)

Canonical dict artifacts for TFP/module runtime are versioned under:

- `assets/calibration/dicts/<version>/dict_a.jsonl`
- `assets/calibration/dicts/<version>/dict_b.jsonl`
- `assets/calibration/dicts/<version>/links.jsonl`
- `assets/calibration/dicts/<version>/metrics.json`

## Runtime switch (single source of truth)

Set one environment variable before running engine/module pipelines:

- `HESPERIA_CALIB_DICT_VERSION=<version>`

Example:

`HESPERIA_CALIB_DICT_VERSION=v0_6_0_clr_v052_1`

When set, runtime dictionary loading resolves from:

- `assets/calibration/dicts/${HESPERIA_CALIB_DICT_VERSION}/dict_a.jsonl`
- `assets/calibration/dicts/${HESPERIA_CALIB_DICT_VERSION}/dict_b.jsonl`

When not set (or missing), runtime falls back to legacy bundled assets under:

- `assets/data/engine_dynamics_v060/...`

## Non-research policy

Mainline runtime/module loading has no dependency on `/research` paths.
Calibration freeze output is consumed from `assets/calibration/dicts/...` only.

## Module data mirror (interim)

Working copies of corpus + dict bundles for the next pipeline steps live under **`hesperia/modules/tfp/data/`** after running `./tools/sync_tfp_module_data.sh` from repo root (sources: `assets/...` plus read-only copy from `research/_noone_local/...` corpus folders). Large mirrored trees are gitignored under that path; see **`hesperia/modules/tfp/data/README.md`**. Runtime resolution remains `assets/` until dict state is fully wired under module architecture.

## After A is green: B then CD

Lexical **A** is closed when calibration validators pass. Next execution wave: **B** (`dict_b` + links in the same `HESPERIA_CALIB_DICT_VERSION` directory, DLCR regression) then **CD** (`concept_dict_cd.jsonl`, `HESPERIA_CD_ENABLED=1`). One-shot check: **`tools/run_b_cd_wave_after_a.sh`** from repo root. Model chain: **`docs/governance/cd_v1/MODEL_CARD_CD_PIPELINE.md`** (`A` → `B` → `CD` → `C_agg` → Topology).

