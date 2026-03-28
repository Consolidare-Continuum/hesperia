# TFP module v1 — boundary review (vs core)

**TFP-V1-11 (Marcus):** `hesperia/modules/tfp/` import surface:

| File | Imports |
|------|---------|
| `v1.py` | `hesperia.engine.calculus.compute_tfp_bundle` (engine calculus, not `core.*` direct) |
| `module.py` | `hesperia.modules.tfp.v1` |
| `math_v1.py` | stdlib + typing only |
| `seal.py` | stdlib + optional `yaml` for `VERSION.yaml` |

**Verdict:** TFP package does **not** import forbidden `core.*` internals from module code paths above.

**CI:** `python3 tools/check_core_module_boundary.py` runs in `sealed-runtime-gate.yml`. As of 2026-03-28 the tool may report a **pre-existing** violation (`hesperia/engine/module_loader.py` → `hesperia.modules.registry`); that is **outside** TFP module scope and tracked separately if reopened.

`SIGNED: Marcus (boundary) | TFP module v1 | 2026-03-28 | TFP-V1-11`
