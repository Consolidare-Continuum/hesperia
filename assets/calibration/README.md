# Calibration assets (Hesperia)

- **`dynamics_parameter_registry.yaml`** — Class B knobs for `hesperia.extensions.dynamics` (Phases 1–4 + **xi_scale** / Ξ proxy). Governance: [specs/dynamics/HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md](../specs/dynamics/HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md).
- **HCI / grid calibration:** [specs/calibration/hspr_index.md](../specs/calibration/hspr_index.md) §2 · `python3 -m runtime.semantic_field.run_field_calibration` · `runtime/configs/field_calibration_example.json`.
- **`semantic_field_equations_v1.json`** — Normative **SEMANTIC_FIELD_EQUATIONS_v1** parameters (`alpha`, `beta`, `gamma`, `delta`, `mu`, `dt`, `epsilon`, `tau`, …). Spec: [specs/dynamics/semantic_field_dynamics.md](../specs/dynamics/semantic_field_dynamics.md). Code: `hesperia.extensions.dynamics.semantic_field_v1`.
- **Lexical / DLCR dictionary calibration (Ethan):** pipeline `tools/dict_calibration/` · README [tools/dict_calibration/README.md](../../tools/dict_calibration/README.md). Reviewed freezes may live under **`dicts/v*/*.jsonl`** here after human sign-off (`run_pipeline.py freeze`).
- **`dicts/v0_tfp_cal_wave_002/`** — auto wave freeze (RU TFP-oriented Dict A layer + metrics). See bundle [README](dicts/v0_tfp_cal_wave_002/README.md). Smoke: `pytest tests/test_tfp_calibration_wave002_smoke.py`.
