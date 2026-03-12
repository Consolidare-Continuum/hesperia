<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Hesperia v0.2.0.1 Release Notes

## Summary

v0.2.0.1 wires the Σ/Γ/Θ guard contract into runnable entrypoints and phase traversal flow.

## Guard Contract

- Mandatory order: **Σ preflight → Γ runtime ticks → Θ final gate**.
- No bypass in `scripts/matrix_run.py`, `scripts/phase_traversal.py`, `scripts/context_rag.py`, and `sphere_rag/phase_engine.py`.
- Final phase result now includes guard outputs:
  - `sigma_status`
  - `gamma_status`
  - `theta_decision`
  - `dynamic_failure_class`
  - `metrics`
