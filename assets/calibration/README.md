# Calibration assets (Hesperia)

- **`dynamics_parameter_registry.yaml`** — Class B knobs for `hesperia.extensions.dynamics` (Phases 1–4 + **xi_scale** / Ξ proxy). Governance: [specs/dynamics/HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md](../specs/dynamics/HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md).
- **HCI / grid calibration:** [specs/calibration/hspr_index.md](../specs/calibration/hspr_index.md) §2 · `python3 -m runtime.semantic_field.run_field_calibration` · `runtime/configs/field_calibration_example.json`.
- **`semantic_field_equations_v1.json`** — Normative **SEMANTIC_FIELD_EQUATIONS_v1** parameters (`alpha`, `beta`, `gamma`, `delta`, `mu`, `dt`, `epsilon`, `tau`, …). Spec: [specs/dynamics/semantic_field_dynamics.md](../specs/dynamics/semantic_field_dynamics.md). Code: `hesperia.extensions.dynamics.semantic_field_v1`.
