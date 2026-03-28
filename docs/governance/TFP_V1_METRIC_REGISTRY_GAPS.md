# `output_metric_registry_v1` vs TFP module v1 public keys

**TFP-V1-10 (Olivia):** Cross-check between `assets/config/output_metric_registry_v1.json` and what the **TFP module v1** contract exposes.

## Module v1 outputs (`tfp.v1`)

From `hesperia/modules/tfp/v1.py`:

- `tfp_vector` (dict)
- `tfp_profile` (dict)
- `tfp_conflicts` (list)

These are **engine/module-plane** structures. The registry’s **`session_tfp_stages.*`** and **`structural_batch.*`** planes cover adjacent pipeline artifacts, not every nested key inside `tfp_profile` / `tfp_vector`.

## Gap statement

| Item | Status |
|------|--------|
| `tfp_vector` / `tfp_profile` inner keys | **Partial coverage** by design — same policy as [`OUTPUT_METRIC_REGISTRY_PARTIAL_COVERAGE_v1.md`](OUTPUT_METRIC_REGISTRY_PARTIAL_COVERAGE_v1.md). |
| `tfp_conflicts` | **Waiver** — list of conflict records; register when product plane needs sortable comparables. |

**Action:** No new active.md row for v1; full metric registration = future Grace triage when `/product/tfp` ships structured parity.

`SIGNED: Olivia (registry cross-check) | TFP module v1 | 2026-03-28 | TFP-V1-10`
