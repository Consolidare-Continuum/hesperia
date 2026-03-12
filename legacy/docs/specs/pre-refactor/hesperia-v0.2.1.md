<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Historical reference (pre-refactor)

# Hesperia v0.2.1 Release Notes

## Summary

v0.2.1 adds **Shadow Layer v1.0** (Core + ΓΘ Addon) on top of v0.2.0.1: degraded-mode traversal plane, topology-preserving, with risk-based activation (Γ), Θ gate (abuse detection, penalties, failure codes).

## Shadow Layer v1.0

- **Spec**: `24_SPEC__Shadow_Layer_v1_0.txt`
- **Code**: `sphere_rag/shadow_layer.py`
- **Behaviour**: Activates when normalized risk R ≥ θ_enter; reduces authority via shadow_mass (decay with hop count); candidate set C = N_shadow(F) ∪ {φ(F)}; shadow-adjusted scores; exit when R ≤ θ_exit and ΔR ≥ δ_min or cap K_max; Θ applies abuse detection and failure codes.
- **Integration**: Call `process_step(ShadowLayerState(), ShadowLayerInput(...), phi=..., n_base=...)` per traversal step; use `out.candidates` and shadow-adjusted metrics. Wire into existing `phase_engine` / Γ runtime where base candidates and metrics are available.

## Failure codes

- `SHADOW_OK_EXIT` — exited shadow successfully
- `SHADOW_FAIL_NO_STABLE_PATH` — hit K_max in shadow
- `SHADOW_FAIL_INVARIANT_VIOLATION` — structural invariant failed
- `SHADOW_FAIL_HARD_RISK` — R ≥ θ_hard in shadow
- `SHADOW_ABORT_ABUSE` — abuse detected (time ratio, enter count, or governance inflation)

## Compatibility

- Backward compatible. Shadow is additive; existing traversal runs unchanged until callers integrate `shadow_layer.process_step`.
