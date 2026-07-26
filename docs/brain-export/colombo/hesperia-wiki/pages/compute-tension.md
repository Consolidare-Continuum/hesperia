# compute_tension

**Status:** 🟢 LIVE_SUCCESSOR — same idea, different name/formula than any Java ancestor  
**Category:** [Tension and Bipolar Adversity](../categories/Tension-and-Bipolar-Adversity.md)  
**Type:** Formula / function  
**Responsible (module):** `core/result/contract.py:63-65`  
**Value / default:** —

## Yields (formula)

pairs = (i, i+6) for i in 0..5 on the 12-area vector; tension = Σ|A[i]-A[i+6]| (L1 abs-sum).

## Produced from (inputs)

- [Icosahedral Surface Graph](../pages/Icosahedral-Surface-Graph.md)
- *A_vec[12] (area activation vector)*
- [OPPOSITE_OFFSET](../pages/OPPOSITE-OFFSET.md)

## Needed by (consumers)

- *Modular tension output (hesperia.result.v1)*

## Origin

Java 21_MATH `bipolarAxes`: B[k]=A[2k]-A[2k+1], tensionEnergy=ΣB[k]² — interleaved pairing + L2 squares

## Notes

**HWIKI-OPEN-01 resolved 2026-07-23:** `(i,i+6)` is **not** geometrically antipodal after `get_aligned_area_coordinates`. Ran alignment on canonical adj: geometric antipodes remain `(0,3)(1,2)(4,7)(5,6)(8,11)(9,10)` (dot=-1); `(i,i+6)` dots are ±0.447 (~0.35π / ~0.65π), not antipodal. Live pairing is the combinatorial [OPPOSITE_OFFSET](../pages/OPPOSITE-OFFSET.md)=6 index convention for exclusion/tension — not a claim that area i faces area i+6 on the sphere. Differs from Java also in aggregator (L1 abs-sum vs L2 squares).

---
[← back to category](../categories/Tension-and-Bipolar-Adversity.md) · [wiki home](../index.md)
