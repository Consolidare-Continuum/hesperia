<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA RAD — Architecture Boundaries

After Reference Architecture Definition (RAD), this document defines the **allowed dependency directions** to prevent architectural drift.

## System boundary map

```
core
 ├─ math          (all numeric operations; deterministic primitives)
 ├─ attribution   (normalize, tokenize, Dict A/B, attribute)
 ├─ topology      (invariants, coordinate mapping)
 ├─ contracts     (LayerInput, LayerOutput)
 ├─ policy        (interpretation policy)
 ├─ layers        (L1–L9 implementations)
 ├─ stability     (Δ stability)
 └─ propagation   (shadow layer, R1–R4 segmenters/units, guards)

sphere
 ├─ execution_flow      (orchestration, registry, state, contract/isolation validation)
 ├─ propagation   (diffusion, family projection, weighting)
 ├─ shadow        (correction, suppression)
 ├─ dynamism      (trajectory, transition matrix, curvature, stability)
 ├─ logic         (structural rules)
 ├─ interpretation (L10 metrics)
 ├─ usf           (generate, fingerprint, drift)
 ├─ guards        (sigma, gamma, theta)
 ├─ metrics       (re-exports from core.math where applicable)
 ├─ geometry      (boundary validation, loaders)
 ├─ diagnostics   (instability, monotony, anomaly)
 ├─ prolog_logic  (optional inference)
 ├─ interfaces    (API helpers)
 └─ topology      (adjacency, family→area loaders)

runtime
 ├─ execution_flow      (CLI runners, e2e, R1–R4, analyze wrappers)
 ├─ api           (FastAPI server)
 ├─ runners       (reference execution_flow CLI)
 ├─ dossier       (index, compare, schema)
 └─ provenance    (manifest, info)
```

## Allowed dependency directions

- **runtime → sphere** — Runtime orchestrates and calls sphere (e.g. `sphere.execution_flow.run_pipeline`, sphere’s layer registry).
- **runtime → core** — Runtime may use core for attribution, layers, math when wrapping or testing.
- **sphere → core** — Sphere orchestrates core layers and uses core.math only; no math implemented in sphere.

**Single direction:**

```
  runtime  →  sphere  →  core
```

## Forbidden

- **core → sphere** — Core must not depend on sphere.
- **core → runtime** — Core must not depend on runtime.
- **sphere → runtime** — Sphere must not depend on runtime (orchestration lives in sphere; runtime is entrypoints only).

This keeps measurement in core, reasoning/orchestration in sphere, and entrypoints in runtime.

## Math authority

All numeric operations must originate in **core.math**. No math (formulas, np.sum/np.dot/entropy implementations, etc.) inside **sphere/** or **runtime/** — only orchestration and calls to core.math.

See also: `tests/architecture/test_no_math_in_sphere.py`, `tests/architecture/test_layer_dependencies.py`.

## RAD freeze

Architecture is stable. Future structural changes require design review and should align with this document.

**Tag:** Repo may carry a tag `RAD_FREEZE` to mark that the reference architecture is frozen; changes that affect boundaries or layer order require design review.
