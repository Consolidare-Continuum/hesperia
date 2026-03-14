<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Math Layer — Architecture

## Math Layer Principles

1. **Math is infrastructure.**  
   All numerical algorithms must live in `core/math`. Deterministic, pure numerical operations only. No pipeline logic, no topology assumptions inside `core/math`.

2. **Sphere layers must not implement numerical logic.**  
   Sphere layers orchestrate pipeline behavior by calling `core/math` primitives. They must not contain:
   - Manual entropy formulas
   - Manual matrix multiplication or transition-matrix construction
   - Vector normalization or curvature/stability formulas implemented locally
   - Any numpy/math used to implement algorithms (as opposed to trivial type coercion for passing through to `core/math`).

3. **Allowed dependency direction**
   - `sphere/*` → `core/math`  
   - **Forbidden:** `sphere/*` implementing math internally.

## Architecture Diagram

```
Pipeline
  sphere/topology
  sphere/dynamism
  sphere/propagation
  sphere/logic
  sphere/metrics
  sphere/pipeline
        │
        ▼
   core/math
```

- **core/math** — deterministic numeric infrastructure (entropy, stability, curvature, transition matrices, coverage, dominance, sequence utils).
- **sphere/topology** — graph structure.
- **sphere/dynamism** — behavioral engine (orchestrates math; no formulas).
- **sphere/propagation** — diffusion engine.
- **sphere/metrics** — structural analysis (orchestrates math; no formulas).
- **sphere/logic** — rule system.
- **sphere/pipeline** — orchestration.

No duplicated math. All numerical behavior is implemented once in `core/math` and invoked from sphere.
