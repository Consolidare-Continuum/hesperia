# Calibration assets (Hesperia)

- **`dynamics_parameter_registry.yaml`** — Class B knobs for `hesperia.engine.field_dynamics` (Phases 1–4 + **xi_scale** / Ξ proxy). Governance: [docs/specs/HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md](../docs/specs/HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md).
- **HCI / grid calibration:** [docs/specs/HSPR_CALIBRATION_INDEX_v1.md](../docs/specs/HSPR_CALIBRATION_INDEX_v1.md) · `python3 -m runtime.semantic_field.run_field_calibration` · `configs/field_calibration_example.json`.
- **`semantic_field_equations_v1.json`** — Normative **SEMANTIC_FIELD_EQUATIONS_v1** parameters (`alpha`, `beta`, `gamma`, `delta`, `mu`, `dt`, `epsilon`, `tau`, …). Spec: [docs/specs/SEMANTIC_FIELD_EQUATIONS_v1.md](../docs/specs/SEMANTIC_FIELD_EQUATIONS_v1.md). Code: `hesperia.engine.field_dynamics.semantic_field_v1`.
