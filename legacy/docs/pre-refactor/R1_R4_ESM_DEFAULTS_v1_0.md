# Historical reference (pre-refactor)

# R1–R4 ESM defaults v1.0 — location and version

**Purpose:** Canonical R1–R4 Expected Smoothing Model defaults (Part D + D Addenda). Freeze for pipeline use; replace with corpus-calibrated values when available (ESM v1.1). **Owner:** Ethan (task 1). **Spec:** [SPEC__Reading_Scale_Levels_R1_R4_Structural_Audit_v1_0.md](SPEC__Reading_Scale_Levels_R1_R4_Structural_Audit_v1_0.md).

---

## Location

| Artifact | Path |
|----------|------|
| Defaults JSON | `sphere_rag/r1_r4_esm_defaults_v1_0.json` |
| This doc | `docs/R1_R4_ESM_DEFAULTS_v1_0.md` |

---

## Contents (from spec Part D)

- **top_n:** 3 — Top-N for leakage/coverage; constant across R-levels (spec §2.2).
- **delta_expected:** Per-transition (R1→R2, R2→R3, R3→R4) for dominance, entropy, leakage, contradiction_pressure, stability, shadow_deviation (D Add.1).
- **epsilon:** Tolerance bands per metric (D Add.2); |Δ_dev| ≤ ε = normal; ε < |Δ_dev| ≤ 2ε = moderate anomaly; > 2ε = strong anomaly.
- **drift_baseline** + **epsilon_drift:** R3 turbulence (D Add.3); Drift_index − Drift_expected > ε_drift → Γ flag.
- **sigma_hard_limits:** Integrity guard (D Add.4); fail if violated.
- **r3_typing:** Coherent Dominant, Dual-Tension, Fragmented thresholds (D Add.5); else Transitional.
- **sci:** SCI_raw and clamp formula (D Add.6).
- **trust_tier:** T_min_valid=12, T_good=60; τ thresholds (D Add.7).
- **shadow_smoothing_rule:** Δ_expected_shadow = 0 (D Add.8).

Pipeline and validation MUST use this file (or a copy) until ESM v1.1 (corpus calibration).
