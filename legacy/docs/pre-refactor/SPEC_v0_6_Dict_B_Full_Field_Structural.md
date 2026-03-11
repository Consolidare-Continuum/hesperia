# Historical reference (pre-refactor)

# Build Dict B v0.6 — Full-Field Structural Layer (No K)

**Status:** Normative
**Depends on:** Dict A v0.6 calibrated field
**Prohibits:** top-K truncation, sparse projection hacks

## 1. Principle

- Dict A = calibrated probability field over 288 families.
- Dict B = deterministic structural transformation of that full field.
- Every family weight remains in the computation. No truncation.

## 2. Core Philosophy

Preserve the “attitude” of Dict A: continuous, calibrated, fully comparable. No first-entry wins, no sparse collapse, no artificial dominance enforcement. B operates on W = [w_1..w_288], w_i ≥ 0, Σ w_i = 1.

## 3. B v0.6 Structural Transform

**Step 1 — Structural coherence:** For excluded pairs (i,j) (area opposite: ring (a+6)%12), conflict_ij = w_i*w_j; C = Σ conflict_ij; w_i' = w_i - λ*Σ(w_i*w_j) over j excluded with i; clip ≥ 0; renormalize. λ = 0.5.

**Step 2 — Area projection:** area_score[A] = Σ w_i' for family i in area A; normalize.

**Step 3 — Structural metrics:** entropy_family, entropy_area, exclusion_conflict_energy = C, coherence_index = 1 - C_norm.

**Sentence-level:** W_S = mean over tokens (from Dict A v0.6); apply the same structural coherence pass on W_S. No re-softmax, no K.

**Traversal (diffusion):** W_prop = (1-α)*W_S' + α*(A@W_S'); A = normalized same-area adjacency; α = 0.2; renormalize.

**Governance:** From area concentration, low conflict, low entropy_area (weighted mix, clamp [0,1]).

**Loopability:** 1 - delta, delta = L1(W_prop - W_S')/2.

**Tension:** From exclusion conflict energy (bounded).

**Dominance:** Summary only (argmax of W_adjusted), not control input.

## 4. Implementation

| Component | Path |
|-----------|------|
| Exclusion / coherence / area / diffusion / metrics | `sphere_rag/dict_b_v06.py` |
| Wiring (v060 path) | `analyze_v033`: when attribution v060 and family_vector 288, call `run_dict_b_v06_pipeline(W_S)` and use result for 6-key output; then run_pipeline for Sigma/Gamma/Theta. |

## 5. Removed

- top-K truncation
- preferred_family as structural driver
- dominance-based filtering before traversal

## 6. Expected Outcome

- tension_energy no longer ~0 (non-zero conflict energy).
- governance and loopability vary across sentences.
- conflict_power sentences can show higher exclusion energy where opposition is present.
- Full 288 vector preserved at every stage.

## 7. Success Criteria

- Full 288 vector preserved at every stage.
- Conflict energy non-zero for mixed-opposition sentences.
- Loopability varies across domains.
- No artificial truncation anywhere.

**Result (2026-02-24):** 100/100 OK. governance 39 unique (0.36–0.54), loopability 38 unique (0.88–0.92), tension_energy 39 unique (0.13–0.24). Family 228 dominance weakened where structural coherence applies; tension no longer ~0.
