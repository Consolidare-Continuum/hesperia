# HESPERIA — calibration protocol (governed dynamics)

**Copyright © 2026 igareosh.com.** See `LEGAL_NOTICE.md`.

## Purpose

Bind tunable coefficients for semantic-field and hex-reference dynamics to **versioned profiles** under `assets/calibration/`, with **active profile** declared in `VERSION.yaml` (`calibration.active_profile`).

## Tunable parameters (family semantic field, `equations.SemanticFieldParams`)

| Symbol   | Role                          | Typical range | Notes |
|----------|-------------------------------|---------------|-------|
| `alpha`  | Graph Laplacian diffusion     | ≥ 0           | Smoothing across adjacency |
| `beta`   | Diagonal resistance           | ≥ 0           | Damping per family |
| `gamma`  | Contradiction (nonlinear)     | ≥ 0           | `F ⊙ (C F)` term |
| `delta`  | Source coupling               | ≥ 0           | Drive toward injection |
| `dt`     | Explicit Euler step           | > 0           | Use with energy control when strict |
| `epsilon`| Numerical convergence ‖ΔF‖    | > 0           | Stop threshold |
| `tau`    | Contradiction pressure ‖P‖₁   | > 0           | Stop threshold |
| `clip_mode` | Safeguard clip [0,1]      | bool          | Not a stability substitute (Task 5) |

## Fixed invariants (not calibration knobs)

- **Topology:** 12 areas, 288 families, 250 hexes/family — `core.topology.invariant_catalog`
- **Matrices:** `L_F`, `C_F`, `R_F` bundles under `assets/matrices/production/` (VERSION `matrices.production_bundle`)
- **Concept→Hex:** `P_CH` under `assets/matrices/pch/` (VERSION `matrices.pch_bundle`)
- **Hex adjacency:** ring-per-family per `assets/topology/hex_topology_v1.json`

## Objective metrics (optimization targets)

Calibration studies SHOULD report:

1. **Stability** — convergence within `max_steps`, energy trace monotone (strict mode).
2. **Sensitivity** — Lipschitz-like response to small injection perturbations.
3. **Contradiction activation** — `contradiction_pressure` responds to conflicting injections.
4. **Propagation realism** — spatial spread on hex lattice (entropy / hotspot structure) not collapsed.

## Files

| File | Role |
|------|------|
| `assets/calibration/profiles_v1.json` | Named profiles |
| `VERSION.yaml` → `calibration.active_profile` | Active binding |
| `hesperia/engine/calibration_profile.py` | Loader API |

## Validation

- Changing `active_profile` or profile coefficients MUST produce **measurably** different trajectories on fixed fixtures.
- Same profile + fixed matrices + fixed seed text → **bitwise-reproducible** outputs when timestamps pinned.
