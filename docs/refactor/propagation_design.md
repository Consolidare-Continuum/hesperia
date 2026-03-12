# Propagation Design (Layer-7)

## Model Chosen

- **Area-level:** One-step diffusion  
  `new_area = (1 - α) * area_vector + α * (area_vector @ W)`  
  where `W` is a row-stochastic matrix built from the area adjacency matrix (and optional edge weights). Only adjacent areas receive flow; no adjacency → no diffusion.

- **Family-level (Option A — area-driven):**  
  Propagate at area level, then distribute each area’s mass uniformly over its families using the family→area mapping.  
  `propagated_family_counts[f] = propagated_area_vector[a] / count(families in area a)` with `a = family_to_area[f]`.  
  Total family mass equals total area mass; dimensions 12 and 288 are preserved.

## Formulas / High-Level Logic

1. **Edge weight matrix**  
   `W = row_normalize(adjacency * edge_weights)` (or `row_normalize(adjacency)` if no weights).  
   Uses `core/math.matrix_utils.row_normalize`. No flow off edges.

2. **Effective diffusion coefficient**  
   `α_eff = base_α` then:  
   - Stability modulation: `α_eff = α_eff * (1 - k_stability * stability_index)` (high stability → less spread).  
   - Jump-rate modulation: `α_eff = α_eff * (1 + k_jump * jump_rate)` (more jumps → slightly more spread).  
   Clamped to [0, 1]. Deterministic.

3. **Area diffusion**  
   Single step: `v_next = (1 - α_eff) * v + α_eff * (v @ W)` via `core/math.diffusion.diffuse_step`.  
   Non-negativity preserved; optional L1 normalization via `core/math.normalization.normalize_l1`.

4. **Family projection**  
   For each area `a`, mass `propagated_area_vector[a]` is split equally among all families in `a`; other families get 0.  
   Preserves total mass (sum over families = sum over areas).

## Why Family Propagation Uses Area Projection

- **Simplicity and auditability:** One clear path: area diffusion → area vector → project to families.  
- **Fits current architecture:** Topology and dynamism are area/sequence-based; family→area is given.  
- **Consistency:** Propagated family counts are fully determined by propagated areas and the canonical mapping; no separate family graph.

## What Is Conserved

- **Without normalization:** `sum(propagated_area_vector)` = `sum(area_vector)` within numerical tolerance (convex combination with row-stochastic W).  
- **With normalization:** Mass is explicitly renormalized to 1; diagnostics record `normalization_applied`, `mass_before`, `mass_after`.

## What Is Normalized

- When `normalize_output=True` (default): both propagated area vector and (after projection) propagated family counts are L1-normalized so their sums are 1. Diagnostics state this.

## Future Upgrades

- Multi-step diffusion (T steps) with configurable T.  
- Option B: direct family propagation on an induced family graph from area adjacency.  
- Per-edge or per-area weights from external data.  
- Optional conservation-only mode (no normalization) with explicit diagnostics.
