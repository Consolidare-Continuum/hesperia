# `co_occurs` soft rule — closed form (Phase 2)

For each active concept `c` with list `co_occurs = [o1, o2, ...]`:

- Let `S = sum(weight[o] for o in co_occurs if o active)`.
- Let `miss = len(co_occurs) - count(active among co_occurs)`.
- **Penalty factor** (deterministic, multiplicative):  
  `penalty = 1.0 / (1.0 + alpha * miss)` with `alpha = 0.25` (versioned in calibration bundle).
- **Boost factor** when all co_occur targets active:  
  `boost = 1.0 + beta * min(1.0, S / (epsilon + sum(weights)))` with `beta = 0.15`, `epsilon = 1e-9`.

Apply order: compute penalties for all `c` in sorted `concept_id` order; multiply `weight[c]` by `penalty` then `boost`; re-quantize.

**MVP**: Phase 1 ignores `co_occurs`; enable only when `HESPERIA_CD_PHASE >= 2` and executor implements this block.

SIGNED: Architect (Ethan) | co_occurs math | 2026-03-27
