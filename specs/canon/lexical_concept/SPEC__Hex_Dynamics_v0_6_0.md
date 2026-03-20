<!--
HESPERIA — RAD. DLCR-HP canon fragment (INT-001).
-->

# SPEC: L4 hex dynamics — v0.6.0

**ID:** `HES-SPEC-DLCR-HP-L4`  
**Normative parent:** [SPEC__DLCR_HP_Master_v0_6_0.md](SPEC__DLCR_HP_Master_v0_6_0.md)

## Purpose

**L4** applies deterministic dynamics (e.g. decay) to hex state and emits concentration/dispersion indices.

## Normative rules

- Dynamics operate on L3 hex activations only; parameters versioned with DLCR resource pins.

## Acceptance

- `tests/lexical_concept/test_hex_dynamics.py` passes.
- `run_dlcr_pipeline` includes `hex_concentration`, `hex_dispersion`, `degradation_flags` from projection.
