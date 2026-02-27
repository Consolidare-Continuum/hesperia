# R1–R4 Band and decision_code mapping v1.0 (locked per deployment)

**Purpose:** Locked mapping for `Unit.flags.band` and `Unit.flags.decision_code` per spec §B.9 and Gaps table. **Owner:** Ethan (task 7). **Spec:** [SPEC__Reading_Scale_Levels_R1_R4_Structural_Audit_v1_0.md](SPEC__Reading_Scale_Levels_R1_R4_Structural_Audit_v1_0.md).

---

## Band (deterministic from SI_metrics)

Evaluate in order; first match wins.

| Condition | band |
|-----------|------|
| trust_tier == T0 | spiky |
| entropy > 0.6 AND dominance < 0.4 | fragmented |
| dominance > 0.55 AND leakage < 0.15 AND entropy < 0.35 | coherent |
| else | stable |

**Enum:** `stable | spiky | fragmented | coherent` (per Unit.schema.json).

---

## decision_code (guard outcomes)

Compact code from Σ/Γ/Θ guard outcomes. **Locked set:**

| Code | Meaning |
|------|---------|
| OK | No guard failure |
| SIGMA_FAIL_LEAK | Σ: leakage > hard limit |
| SIGMA_FAIL_ENTROPY | Σ: entropy > hard limit |
| SIGMA_FAIL_DOMINANCE | Σ: dominance (R3/R4) < minimum |
| SIGMA_FAIL_SHADOW | Σ: shadow_deviation > hard limit |
| SIGMA_FAIL_CP | Σ: contradiction_pressure > hard limit |
| GAMMA_DRIFT | Γ: drift or scale-delta anomaly |
| GAMMA_MACRO_INSTABILITY | Γ: R3 turbulence (Drift − Drift_expected > ε_drift) |
| THETA_SHADOW_DEV | Θ: shadow/evidence guard flag |

Implementation MUST use only these codes (or document extension). Add new codes via versioned doc update.
