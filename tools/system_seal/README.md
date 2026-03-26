# System seal (TASK_11)

Authoritative **GO/NO-GO** gate: `hesperia.system.system_seal.run_system_seal_gate`.

## Run

```bash
python3 -m tools.system_seal.run_system_seal
```

Writes `release/v{VERSION.yaml system_version}/system_seal.json` (e.g. `release/v0.5.1/system_seal.json`) and prints the report. Exit **0** iff `status == PASS`.

## Checks

| Key | Intent |
|-----|--------|
| `execution_flow` | Canonical shipping modules must not import/call `sphere.execution_flow.run_pipeline` |
| `hex_dependency` | Product signals reject missing hex tensors |
| `matrices` | Production `L_F/C_F/R_F` load (no stub env) |
| `pch` | Governed sparse non-uniform `P_CH` |
| `energy` | Strict-mode family energy trace monotone |
| `concept` | Sealed path uses `markers_to_concept_activation` |
| `topology` | `hex_topology_v1.json` + invariant match |
| `calibration` | Active profile matches `assets/calibration/profiles_v1.json` |
| `validation` | `pytest tests/physics_validation` (skipped if `skip_physics_subprocess=True`) |
| `product_truth` | Sample `run_structural_analysis` + `schema_guard` |

## Release

`tools/release/build_release_audit_v0_5_0.py` runs the full gate and adds `system_seal_gate_failed` to `reasons_fail` when status ≠ PASS.

## API (optional)

```bash
export HESPERIA_REQUIRE_SYSTEM_SEAL=1
```

FastAPI startup in `runtime/shipping/api_main.py` refuses to serve if the gate fails.
