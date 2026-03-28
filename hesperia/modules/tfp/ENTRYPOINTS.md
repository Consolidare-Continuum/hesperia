# `hesperia.modules.tfp` — supported public entrypoints (v1)

**TFP-V1-02:** Import **only** the symbols below for integrations. Other modules under this package are implementation details and may change without a minor bump policy until seal.

| Symbol | Path | Stability |
|--------|------|-----------|
| `create` | `hesperia.modules.tfp.module` / `hesperia.modules.tfp` | **Stable v1** — registry shim for `tfp` alias |
| `TFPModule` | `hesperia.modules.tfp.v1` | **Stable v1** — class `name="tfp.v1"` |
| `create` (same instance) | `hesperia.modules.tfp.v1` | **Stable v1** — `create()` → `TFPModule()` |

**Registry:** `hesperia.modules.registry` maps `tfp` and `tfp.v1` → `hesperia.modules.tfp.v1`.

**Not public API:** `math_v1.py`, internal `data/` mirror trees, tests-only helpers.
