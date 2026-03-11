# Hesperia v0.4 Release Notes (Consolidation)

## Summary

v0.4 consolidates the **first full L1–L9 stack**: all nine layers (34_SPEC … 42_SPEC) implemented, single full-pass script, output log dir, first run frozen. L10 (43_SPEC) removed; stack is L1–L9 only.

## What’s in v0.4

- **L1–L9**: Instrumentation → geometric traversal → shadow divergence → book evidence → counter-evidence + trig reality → conceptual math & dynamic function → cross-layer limits/aggregates → units/i18n → human reference & brand. Standard: run → output → logged → reportable.
- **Script**: `python3 -m sphere_rag.layers.run_l1_through_l9 --out docs/layer_runs/latest_L1_L9_output.json`
- **Output log dir**: `docs/layer_runs/` — latest JSON + report. See [docs/FREEZE__First_Full_Stack_Run_L1_L9.md](../docs/FREEZE__First_Full_Stack_Run_L1_L9.md).
- **Predefined defaults**: LAYER_1_9_PREDEFINED_DEFAULTS_v1_0 (TXT + JSON) for thresholds and topology.

## How to build

From `CLIENTS/hesperia`: install deps (`pip install -r requirements_v040.txt` if using v0.4.0/v0.4.1 builds). Layer stack needs no separate build. v0.4.0: `python -m sphere_rag.build_v040 ...`; v0.4.1: `python -m sphere_rag.build_v041 ...`. See [RELEASE_NOTES__v0_4.txt](../RELEASE_NOTES__v0_4.txt) and [RUNNABLE.md](../RUNNABLE.md).

## How to use

Full pass: `python3 -m sphere_rag.layers.run_l1_through_l9 --out docs/layer_runs/latest_L1_L9_output.json`. L1-only/L1+L2/L1+L2+L3 runners available. Core math and simulation: see RUNNABLE.md.

## What’s expected

Deterministic: same inputs → same L1–L9 outputs. Stub run (no retrieval) → L4/L5 evidence zero, L9 may show FRAGILE/UNSUPPORTED; with real Dict A/B and Chroma, values populate.

## Compatibility

Additive. v0.3 core and API unchanged. L1–L9 is the new observability stack; no breaking changes to existing serve_v033 or run_simulation entry points.
