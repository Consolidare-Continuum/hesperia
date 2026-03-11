# 22_SPEC__V0_3_Core_Math_Contract_v1_0

**Project**: HESPERIA
**Target release**: v0.3
**Date**: 2026-02-22
**Status**: Canonical (implementation contract)

**References**: Lexical stack [19_SPEC Two-Dictionary], Authority [20_SPEC Authority Separation Invariants], Books non-voting [21_SPEC Books Evidence Cloud Non-Voting].

---

## 0. Scope

Defines the only allowed math for:

- SurfaceEnergy fusion (Dict A + Dict B)
- Traversal update dynamics (base + shadow)
- Resolution rules (dominant family/area)
- Metric formulas (governance, loopability, tension_energy, obstacle_score)
- Degraded-state triggers and penalties
- Hard invariants coupling to ΣΓΘ event outputs

**Books retrieval is evidence only and MUST NOT affect any computation in this spec.**

---

## 1. Canonical runtime variables

Universe is the canonical side set SIDES of size ~72k.

Per request:

- **S[i]** — Core seed mass on side i (Dict A projection). S[i] ≥ 0
- **L[i]** — Landing mass on side i (Dict B alias landing). L[i] ≥ 0
- **E0[i]** — Initial surface energy (fusion). E0[i] ≥ 0
- **E[t][i]** — Surface energy at traversal step t. E[t][i] ≥ 0
- **shadow_hops** — Integer count of shadow steps used.
- **guard_events** — Structured counts from ΣΓΘ (no hidden logic).
- **penalties** — Scalar components: P_amb, P_thin, P_shadow, P_disp, P_guard.

No other latent state is allowed to influence resolution or metrics.

---

## 2. Normalization constants

Define **eps** = 1e-9.

- sumS = Σ_i S[i]
- sumL = Σ_i L[i]
- If both sums are 0 → hard-stop failure (no activation).

Normalized projections:

- S'[i] = S[i] / (sumS + eps) if sumS > 0, else S'[i] = 0
- L'[i] = L[i] / (sumL + eps) if sumL > 0, else L'[i] = 0

**Single-source fallback**: If exactly one of sumS, sumL is 0, use the non-zero source only (E0 from S' or L' alone). Do not renormalize the single source to fake confidence; fusion formula still applies with the other term zero.

---

## 3. SurfaceEnergy fusion (hard lock)

**Parameters**: alpha ∈ [0,1] (default 0.65), E_cap global (default 1.0).

**Fusion**: E0[i] = clamp( alpha·S'[i] + (1-alpha)·L'[i], 0, E_cap ). No other mixing, no extra boosts.

---

## 4. Centroid selection (traversal start set)

**Parameters**: K_max (default 5), eta (default 0.02).

- ACTIVE = { i | E0[i] > eta }
- K = min(K_max, |ACTIVE|)
- Start set **C** = top-K sides by E0[i] (descending). Tie-break: smaller side_id first.
- If K = 0 → degraded_state: no_centroid = true (allowed to trigger shadow §6).

---

## 5. Base traversal operator

Row-stochastic **W**: W[i][j] ≥ 0, Σ_j W[i][j] = 1 for all i with outgoing edges; if i has no outgoing, W[i][i] = 1.

**Parameters**: lambda ∈ (0,1] (0.55), decay ∈ [0,1) (0.04), T_steps (8), E_cap.

- E[0] = E0
- For t = 0..T_steps-1:
  - **Diffusion**: D = (1-λ)·E[t] + λ·(E[t] · W)
  - **Decay sink**: E[t+1] = D · (1 - decay)
  - **Clamp**: E[t+1][i] = clamp(E[t+1][i], 0, E_cap)

**I-R2 (conservation)**: Test on D (before decay): sum(D) ∈ [sum(E[t])·(1-εc), sum(E[t])·(1+εc)], εc = 1e-6. Decay is deliberate sink (used in obstacle_score).

---

## 6. Shadow traversal operator (restricted)

Separate row-stochastic **Ws**. Shadow step allowed ONLY if: no_centroid=true, OR dead-end (logged), OR Θ tie-break (explicit event).

- E_shadow = E_current · Ws
- **I-R3**: sum(E_shadow) ≤ sum(E_current) + eps; shadow_hops += 1
- **max_shadow_hops** (default 2). If exceeded → degraded_state: shadow_overuse = true.

---

## 7. Aggregation to family and area

- SidesOfFamily[f], FamiliesOfArea[a]. E_end = E[T_steps] (after any shadow).
- F[f] = Σ_{i ∈ SidesOfFamily[f]} E_end[i]
- **dominant_family** = argmax_f F[f]. Tie-break: higher Σ_{i∈SidesOfFamily[f]∩C} E0[i], then smaller family_id.
- A[a] = Σ_{f ∈ FamiliesOfArea[a]} F[f]
- **dominant_area** = argmax_a A[a]. Tie-break: higher centroid E0 mass for area, then smaller area_id.

No books, embeddings, or LLM may modify this.

---

## 8. Ambiguity score and penalty

e1 ≥ e2 = top two of E0 (if one side, e2 = 0). gap = (e1 - e2)/(e1 + eps). Amb = 1 - clamp(gap, 0, 1).

**Parameters**: delta_gap (0.08), k_amb (0.35). P_amb = k_amb · Amb². If gap < delta_gap → degraded_state: ambiguity = true.

---

## 9. Thin-core score and penalty

CoreShare = sumS / (sumS + sumL + eps). Thin = 1 - CoreShare.

**Parameters**: tau_core (0.25), k_thin (0.30). P_thin = k_thin · Thin. If CoreShare < tau_core → degraded_state: thin_core = true.

---

## 10. Dispersion score and penalty (entropy)

ACTIVE_END = { i | E_end[i] > 0 }, M = |ACTIVE_END|. If M ≤ 1, dispersion = 0.

p[i] = E_end[i] / (Σ_j E_end[j] + eps). H = -Σ p[i]·ln(p[i]). H_norm = H / ln(M). **Parameters**: k_disp (0.25). P_disp = k_disp · H_norm.

---

## 11. Guard penalty coupling (ΣΓΘ)

Counts: sigma_fail_count, gamma_violation_count, theta_reject_count. **Parameter**: k_guard (0.30).

GuardCount = sum of above. P_guard = clamp(k_guard · GuardCount, 0, 1). **Hard-stop (recommended)**: if theta_reject_count > 0 → F4 (coherence breach).

---

## 12. Metrics (before books retrieval)

- **governance** = clamp( 1 - (P_amb + P_thin + P_shadow + P_disp + P_guard), 0, 1 )
- **loopability** = clamp( Σ_{i∈C} E_end[i] / (Σ_j E_end[j] + eps), 0, 1 )
- **tension_energy**: f1 ≥ f2 top F[f]; gapF = (f1-f2)/(f1+eps); tension_energy = clamp( 1 - clamp(gapF,0,1), 0, 1 )
- **obstacle_score**: Loss = 1 - (Σ E_end)/(Σ E0+eps), clamped. P_shadow = clamp( k_shadow · (shadow_hops/max_shadow_hops), 0, 1 ). obstacle_score = clamp( w_decay·Loss + w_guard_obs·clamp(GuardCount,0,1) + w_shadow_obs·clamp(shadow_hops/max_shadow_hops,0,1), 0, 1 ). Defaults: w_decay 0.50, w_guard_obs 0.30, w_shadow_obs 0.20.

---

## 13. Books invariants (non-voting hard lock)

Books retrieval MAY run only after dominant_area, dominant_family, and all four metrics are computed. **CI A/B**: disabling or emptying books index must not change any value above.

---

## 14. Default config (see guard_config_v1.json)

eps 1e-9, alpha 0.65, E_cap 1.0, K_max 5, eta 0.02, lambda 0.55, decay 0.04, T_steps 8, energy_conservation_tolerance 1e-6, delta_gap 0.08, k_amb 0.35, tau_core 0.25, k_thin 0.30, k_disp 0.25, max_shadow_hops 2, k_shadow 0.40, k_guard 0.30, w_decay 0.50, w_guard_obs 0.30, w_shadow_obs 0.20.

---

## 15. Failure classes (binding)

- F1 schema violation (IDs / missing fields)
- F2 authority breach (A outputs family/area; books vote)
- F3 topology breach (alias outside 72k)
- F4 coherence breach (Θ reject)
- F5 degenerate activation (no activation / extreme dispersion)
- F6 shadow overuse (max exceeded)

---

## 16. Required CI checks (from guard_config_v1)

Pipeline must validate:

- alpha ∈ [0, 1]
- lambda ∈ (0, 1]
- decay ∈ [0, 1)
- All penalty weights (k_amb, k_thin, k_disp, k_shadow, k_guard) ∈ [0, 1]
- Obstacle weights (w_decay, w_guard_obs, w_shadow_obs) sum to 1.0 ± tolerance
- max_shadow_hops ≥ 0
- energy_conservation_tolerance < 1e-3 (upper bound guard)
- energy_cap > 0
- Books config: must_not_affect_metrics = true, retrieval_stage = post_resolution_only
- No runtime override of contract parameters without version bump

Invariant tests: I-R2 (conservation on D), I-R3 (shadow non-creation), I-Q2 (books removal does not change resolution or metrics).

---

## 17. Layer-1 instrumentation (v0.4.x)

For deterministic observability: **34_SPEC** (Layer-1) … **38_SPEC** (Layer-5), **39_SPEC** (Layer-6), **40_SPEC** (Layer-7), **41_SPEC** (Layer-8 units), **42_SPEC** (Layer-9). None replace resolution or metrics above.

END
