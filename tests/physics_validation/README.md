# Physics validation harness (TASK_6_10 §9)

Deterministic checks for stability, sensitivity, contradiction, propagation, reproducibility, plus governed **topology** and **calibration** bundles.

## Run

From repository root:

```bash
python3 -m pytest tests/physics_validation/ -q
```

Or:

```bash
python3 -m tests.physics_validation.run_all
```

Thresholds: `specs/validation_thresholds.json`.

## Strict public key allowlist

Optional envelope check when projecting public JSON:

```bash
export HESPERIA_PUBLIC_SCHEMA_STRICT_KEYS=1
```

Uses `runtime/shipping/schema_guard.py` + `schemas/public/public_output_schema.json` property keys.
