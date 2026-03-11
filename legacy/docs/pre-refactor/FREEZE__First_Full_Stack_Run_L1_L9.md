# Historical reference (pre-refactor)

# Freeze — First full stack run (L1–L9)

**Date**: 2026-02-24  
**Status**: Frozen. This state is the first complete L1–L9 pipeline run.

## What is frozen

- **Stack**: Attribution → L1 → L2 → … → L9 (34_SPEC … 42_SPEC). No L10/43_SPEC.
- **Script**: `sphere_rag/layers/run_l1_through_l9.py`. Entry: `python3 -m sphere_rag.layers.run_l1_through_l9 --out <path>`.
- **Layer code**: `sphere_rag/layers/layer_1.py` … `layer_9.py`, `defaults.py`. Predefined defaults: `LAYER_1_9_PREDEFINED_DEFAULTS_v1_0.txt` / `layer_1_9_predefined_defaults_v1_0.json`.
- **Output log dir**: `artifacts/layer_runs/`. First run output: `latest_L1_L9_output.json` + `REPORT__L1_L9_Full_Pass.md`.

## First run output (canonical location)

- **Dir**: [artifacts/layer_runs/](../artifacts/layer_runs/)
- **JSON**: [latest_L1_L9_output.json](layer_runs/latest_L1_L9_output.json)
- **Report**: [REPORT__L1_L9_Full_Pass.md](layer_runs/REPORT__L1_L9_Full_Pass.md)

## Repo sync

Brain repo: pull then push. Single source (Proton Drive / GitHub igareosh/cursor). After this freeze, commit and push so both local and origin reflect first full stack run.
