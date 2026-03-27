# `apply_saturation(score, k)` — closed form (CD v1)

Implemented in `hesperia/engine/concept_dictionary/executor.py`:

- Input: `score >= 0`, `k` = `saturation_k` from CD row.
- If `k >= 1.0`: output `quantize(score)` (identity on non-negative branch).
- If `0 < k < 1.0`:  
  `out = score / (1 + (1 - k) * score)`  
  then `quantize(out)`.

Properties: monotone, bounded growth, stable at 0, deterministic with `quantize`.

SIGNED: Dev (Gena) | saturation doc = code | 2026-03-27
