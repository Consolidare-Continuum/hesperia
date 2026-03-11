# Historical reference (pre-refactor)

# HESPERIA v0.3 Release Gate Audit

**Date**: 2026-02-23
**Auditor**: Gena (consolidation run)
**Target**: 22_SPEC__V0_3_Core_Math_Contract_v1_0

---

## TASK 1 — Contract Conformance Audit

**Goal**: Implementation matches 22_SPEC. No extra terms; no books pre-resolution; guard once; shadow never increases energy.

### File → line mappings (hesperia_v03_core_math.py)

| Formula | SPEC § | File:Line | Implementation |
|--------|--------|-----------|----------------|
| Fusion | §3 | 157–171 | `E0[i] = clamp(alpha*S'[i] + (1-alpha)*L'[i], 0, E_cap)` |
| Ambiguity | §8 | 248–262 | `gap = (e1-e2)/(e1+eps)`, `Amb = 1 - clamp(gap,0,1)`, `P_amb = k_amb * Amb²` |
| Thin-core | §9 | 268–277 | `CoreShare = sumS/(sumS+sumL+eps)`, `Thin = 1 - CoreShare`, `P_thin = k_thin * Thin` |
| Dispersion | §10 | 284–298 | `p[i]=E_end[i]/total`, `H = -Σ p·ln(p)`, `H_norm = H/ln(M)`, `P_disp = k_disp * min(H_norm,1.0)` |
| Loopability | §12 | 318–322 | `clamp(Σ_{i∈C} E_end[i] / (Σ E_end+eps), 0, 1)` |
| Tension | §12 | 325–334 | `gapF = (f1-f2)/(f1+eps)`, `tension_energy = clamp(1 - clamp(gapF,0,1), 0, 1)` |
| Obstacle | §12 | 338–355 | `Loss = clamp(1 - sumE_end/sumE0, 0, 1)`; `obs = w_decay*Loss + w_guard_obs*... + w_shadow_obs*...` |

### Verification

- **No additional hidden boosts**: Only the above terms appear in metrics. governance = 1 - (P_amb + P_thin + P_shadow + P_disp + P_guard) — no extra terms.
- **No books influence pre-resolution**: Books are not passed to fusion, base_step, centroid_indices, or aggregate_dominant_family_area. full_run_simulation and chroma_books_validation_run call books only after resolution (query_books_post_resolution).
- **Guard penalties applied exactly once**: full_run_simulation.py line 100: `P_guard = guard_penalty(0, 0, 0, cfg)`; single use in metric_governance.
- **Shadow never increases energy**: I-R3 in shadow_step (lines 227–242): `non_creation_ok = sum(E_shadow) <= sum(E) + eps`.

### Deviations

- **Dispersion**: Code uses `min(H_norm, 1.0)` before multiplying by k_disp. SPEC says `P_disp = k_disp * H_norm` only. Capping H_norm at 1 is conservative (reduces penalty), not an extra boost. **Accepted.**

**TASK 1: PASS**

---

## TASK 2 — Determinism Audit: **PASS**

- Two runs `run_simulation.py full --n-sides 72`: stdout **byte-identical**.
- No timestamp fields in output JSON.
- Only `random.seed(0)` in full_run_simulation; dict iteration deterministic; `sort_keys=True` for JSON.

---

## TASK 3 — Lexical Integrity Audit: **PASS**

- ci_lexical.sh passed. Lemmas 3, total seeds 3, aliases 6; max 3 seeds per lemma; weights in (0, cap]; canonical lemma grade A; no duplicate alias; side_id format int; no family_id/area_id in A. Violations: 0.

---

## TASK 4 — Books Non-Voting (I-Q2): **PASS**

- chroma_books_validation_run runs pipeline twice, asserts strict equality of resolution, metrics, penalties. I_Q2_books_do_not_affect_metrics and I_Q2_strong_run_twice set from comparison.

---

## TASK 5 — Energy Invariants Stress Test: **PASS**

- sphere_rag/tests/energy_invariants_stress.py: five S/L cases; conservation, no negative energy, no E > E_cap, shadow non-creation. All hold.

---

## TASK 6 — Failure Mode Enforcement: **PASS**

- F2 enforced by loader/validate_lexical (no family_id/area_id in A). F3 by canonical set and alias uniqueness. F5 by fusion ValueError. Hard-stop vs degraded per guard_config.

---

## TASK 7 — Topology Honesty: **PASS**

- chroma_books_validation_run docstring and README: stub traversal; topology from Chroma only if ingested. No adjacency assumed unless in contract.

---

## TASK 8 — Freeze Record Consistency: **PASS**

- SHA256 of A, B, guard_config match actual files. repo_commit stored in FREEZE_RECORD. Version consistent.

---

## TASK 9 — Dependency Surface Check: **PASS**

- hesperia_v03_core_math imports only json, math, pathlib, typing, optional numpy. No LLM, embedding, or books in core pipeline.

---

## TASK 10 — Release Gate Summary

See **docs/HESPERIA_V03_RELEASE_GATE_REPORT.md**. Overall: **RELEASE APPROVED**.
