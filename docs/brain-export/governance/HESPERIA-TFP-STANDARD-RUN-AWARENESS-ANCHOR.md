# Hesperia TFP standard run — awareness anchor

Purpose: MCP/Chroma retrievable anchor for the canonical TFP bundle run that writes full tweakable artifacts into one datetime directory.

Scope: Hesperia repo at `/data/hesperia/hesperia`.

## Canonical command

```bash
cd /data/hesperia/hesperia
python3 tools/tfp_pipeline_standard_run.py -i path/to/session.md
```

Calibration subtree:

```bash
python3 tools/tfp_pipeline_standard_run.py -i path/to/session.md --calibration
```

## Canonical output roots

- `assets/artifacts/tfp_pipeline_runs/<YYYYMMDD_HHMMSS>/`
- `assets/artifacts/tfp_pipeline_runs/calibration/<YYYYMMDD_HHMMSS>/`

## Required run directory contents

- Pipeline numbered JSON (`00_manifest.json`, `01_`…`09_`, `12_*` when topology+TRIZ activation is on)
- `terminology_tfp.json`
- `tfp_values_ratios_and_parameters.json`
- `input_source.<ext>`

## Sidecar intent

- `terminology_tfp.json`: one-file terminology reference (`TFP_STAGES`, area labels, defense/object maps).
- `tfp_values_ratios_and_parameters.json`: one-file inspection point for calibration knobs, flags, env snapshot, operational envelope, errors, and `dict_states_snapshot`.
- `input_source.<ext>`: immutable copy of the source input used for this run.

## Awareness anchors (code paths)

- `/data/hesperia/hesperia/tools/tfp_pipeline_standard_run.py`
- `/data/hesperia/hesperia/hesperia/engine/tfp_run_sidecars.py`
- `/data/hesperia/hesperia/runtime/pipeline/run_tfp_file_pipeline.py`
- `/data/hesperia/hesperia/tools/inspect_tfp_bundle_output.py` → writes `99_tfp_bundle_inspect.json` (machine normality + layer coherence); optional `--inspect` on standard run
- `/data/hesperia/hesperia/assets/calibration/TFP_VALUES_LIST`

## Cursor MCP runbook (agent procedure)

- Brain repo: `scripts/SCRIPT-RUNBOOK-hesperia-tfp-bundle-inspection.md`
- **get_runbook** id: `SCRIPT-RUNBOOK-hesperia-tfp-bundle-inspection`

## Full-options-on intent

Standard runner enforces testing posture with:

- full pipeline branches enabled (`with_kme`, `with_triz`, `with_topology`, `with_r1_r4`)
- `HESPERIA_ANALYZE_DLCR_EVIDENCE=1`
- `HESPERIA_SEALED_DLCR_SIDECAR=1`
- TFP DLCR domain pack active
