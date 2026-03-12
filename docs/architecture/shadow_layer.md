# Shadow Correction (Layer-8) — Architecture

## Role

Layer-8 Shadow Correction filters weak propagation noise, reinforces dominant topology, and stabilizes entropy so that downstream (e.g. Layer-9 rule engine) sees cleaner structural signals.

## Flow

1. **Input:** `propagated_area_vector`, `propagated_family_counts`, `propagation_diagnostics` (from Layer-7).
2. **Tail suppression** — Zero out area mass below a structural threshold; report count suppressed and mass retained.
3. **Dominant area reinforcement** — Boost the dominant area (from `core.math.vector_ops`), then L1-renormalize.
4. **Entropy stabilization** — Blend with a peaked (dominant-only) distribution to cap entropy increase from diffusion.
5. **Project to families** — Use `sphere.propagation.family_projection.project_area_to_families` so corrected area vector becomes `corrected_family_counts`.
6. **Tension** — Recompute structural tension after correction via `core.math.stability_metrics.compute_structural_tension`.

## Outputs

- `corrected_area_vector` (length 12)
- `corrected_family_counts` (length 288)
- `shadow_diagnostics` (tail_suppression_count, entropy/tension before/after, etc.)

## Placement

- **Math:** All numeric operations live in `core/math` (vector_sum, detect_dominant_area, normalize_l1, compute_entropy, compute_structural_tension). No duplicate math in `sphere/shadow`.
- **Behavior:** `sphere/shadow` orchestrates suppression, dominance filter, entropy correction, and projection; calls propagation’s `project_area_to_families` for area→family.

Pipeline runs shadow correction after propagation and attaches `shadow_metrics` to the result. Later, Layer-9 and logic can use `corrected_area_vector` / `corrected_family_counts` for more stable rule triggers.
