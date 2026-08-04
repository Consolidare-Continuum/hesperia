# Wiener feedback on alpha (k_s / k_j)

**Status:** 🟢 LIVE_SUCCESSOR — same idea, different name/formula than any Java ancestor  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Formula / function  
**Responsible (module):** `sphere/propagation/weighting.py:78-127 (`apply_stability_modulation`, `apply_jump_rate_modulation`, `compute_effective_diffusion_rate`)`  
**Value / default:** k_stability=0.5, k_jump=0.3 (defaults)

## In plain words

when the system looks stable, slow the spread; when it jumps a lot, allow slightly more spread.

## Definition

- **Receives:** [lambda (lazy step)](../pages/lambda-lazy-step.md)
- **Does:** effective_α = base_α·(1 − k_stability·stability_index) then ·(1 + k_jump·jump_rate), each clamped to [0,1] — cybernetic feedback on *diffusion* α.
- **Outputs:** `k_stability=0.5, k_jump=0.3 (defaults)` → *sphere/propagation/engine.py (compute_effective_diffusion_rate call)*
- **Exists for:** renamed symbols `k_stability`/`k_jump` (not `k_s`/`k_j`); modulates propagation diffusion α, **not** [alpha (fusion weight)](../pages/alpha-fusion-weight.md)

## Yields (formula)

effective_α = base_α·(1 − k_stability·stability_index) then ·(1 + k_jump·jump_rate), each clamped to [0,1] — cybernetic feedback on *diffusion* α.

## Produced from (inputs)

- [lambda (lazy step)](../pages/lambda-lazy-step.md)

## Needed by (consumers)

- *sphere/propagation/engine.py (compute_effective_diffusion_rate call)*

## See also

- [lambda (lazy step)](../pages/lambda-lazy-step.md)
- [structural analogy (extent term)](../pages/structural-analogy-extent-term.md)

## Origin

Wiener (1948) cybernetic feedback lineage — Theory Explainer: plain_lang: when the system looks stable, slow the spread; when it jumps a lot, allow slightly more spread. author: Norbert Wiener (1948) cybernetics as theory family (not a cited import). extent: structural_analogy. reasoning: renamed symbols `k_stability`/`k_jump` (not `k_s`/`k_j`); modulates propagation diffusion α, **not** [alpha (fusion weight)](../pages/alpha-fusion-weight.md). application: `sphere/propagation/engine.py`, tests in `tests/propagation/test_stability_modulation.py`.

## Notes

**HWIKI-OPEN-02 / DOC-13 resolved 2026-07-23:** Grep for `wiener`/`k_s`/`k_j` as claimed names = zero real hits, but the *formula* lives under `k_stability`/`k_jump` in `weighting.py`. Relocated LIVE_SUCCESSOR — do not cite as DEAD. Not fusion α.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
