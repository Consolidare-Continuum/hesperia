# Historical reference (pre-refactor)

# Reading-Scale Structural Audit Architecture (R1–R4)

> **Agent notice:** When using this spec: outputs = JSON per schema only (no table-fill); spec tables are reference. See `docs/AVOID__R1_R4_Spec_Until_Reasonable.md` and AGENTS.md §5a.

## Multi-Pass Structural Analysis — Formal Specification (Reading-Scale Model)

**Version:** 1.0  
**Architect:** Ethan (specification and default-parameter design).  
**Naming convention:** R1–R4 = reading/scale levels (sentence → paragraph → chapter → book). L1–L9 = HESPERIA math layers (34_SPEC … 42_SPEC). Do not use L1–L4 for scale levels to avoid confusion with math layers.

### Consistency Check: Namespace Hygiene

Three namespaces, no cross-contamination:

| Namespace | Scope | Use only for |
|-----------|--------|----------------|
| **R1–R4** | Reading-scale | Sentence, paragraph, chapter, book levels and their units/aggregates. |
| **L1–L9** | Math layers | Instrumentation, traversal, shadow, evidence, … (34_SPEC … 42_SPEC). |
| **Σ / Γ / Θ** | Governance | Structural integrity, consistency guard, shadow/evidence guard. |

Clean three-axis architecture: vertical (R1–R4), horizontal (L1–L9), governance (Σ/Γ/Θ).

**Spec parts:** Part A (§1–§19) — architecture, unit schema, aggregation, turning points, R3 typing, SCI, guards. **Part B** — SI_metrics equations (v1.0). **Part B Addenda** — token→family contract, Top-N, secondary metrics, similarity, compression loss, drift, magnitude. **Part C** — JSON Schema set (Unit, BookProfile, SI_metrics). **Part D** — **Expected Smoothing Model (ESM) v1.0** (Δ_expected, ε_M, corpus/bootstrap, guard integration).

---

## 1. Architectural Model

### 1.1 Hierarchical Reading Levels

Four strictly separated analytical levels:

| Level   | Code | Unit Definition   |
|---------|------|--------------------|
| Micro   | **R1** | Sentence           |
| Meso-1  | **R2** | Paragraph          |
| Meso-2  | **R3** | Chapter            |
| Macro   | **R4** | Book / Part        |

Each reading level is computed independently and normalized (not as recursive smoothing).

---

## 2. Unit Object Specification

All levels produce identical structural objects. Uniform schema across R1–R4.

### 2.1 Canonical Unit Schema

```json
{
  "unit_id": "string",
  "level": "R1|R2|R3|R4",
  "parent_id": "string|null",
  "token_count": "int",

  "top_areas": [
    {"area_id": "A#", "coverage": 0.0, "rank": 1}
  ],

  "top_families": [
    {"family_id": "F##", "coverage": 0.0, "rank": 1}
  ],

  "SI_metrics": {
    "coverage": 0.0,
    "dominance": 0.0,
    "entropy": 0.0,
    "leakage": 0.0,
    "contradiction_pressure": 0.0,
    "stability": 0.0,
    "shadow_deviation": 0.0,
    "trust_tier": "T0–T3"
  },

  "flags": {
    "band": "stable|spiky|fragmented|coherent",
    "decision_code": "string"
  }
}
```

This object must be deterministic and scale-normalized.

### 2.2 Leakage Definition

**Leakage** = proportion of tokens assigned to low-rank families outside the top-N cluster (for that unit).

- Defined per unit from raw token→family attribution; not interpretive.
- Enables compression-loss logic (e.g. Avg_coverage(R1) > Coverage(R3 aggregate)) to be stable and testable.
- **N must remain constant across R-levels.** If N varies by level, compression-loss logic breaks. **Recommendation:** fix N globally (e.g. **N = 3**). Document in implementation.

---

## 3. Expected Reading-Scale Dynamics (Scale Behavior Model)

Structural metrics follow predictable scale dynamics.

### 3.1 Expected Smoothing Law

| Metric                | Expected Direction (↑ scale R1 → R4) |
|-----------------------|--------------------------------------|
| Dominance             | ↑                                    |
| Entropy               | ↓                                    |
| Leakage               | ↓                                    |
| Stability             | ↑                                    |
| Contradiction Pressure| ↓ (unless systemic)                  |

These are structural expectations, not evaluative judgments.

### 3.2 Deviation Detection

**Δ_dev = Δ_observed − Δ_expected**, where Δ_observed = Mean_M(Rk+1) − Mean_M(Rk) (weighted) and **Δ_expected** is defined by the **Expected Smoothing Model (ESM)** — see **Part D**. Only deviations exceeding threshold **ε_M** are structurally meaningful.

### 3.3 Deterministic Aggregation Contract

level_averages and scale_deltas must follow explicit rules so the LLM (and pipelines) do not invent logic.

**3.3.1 Level Aggregation Rule**

For any metric M at reading level Rk:

- **Mean_M(Rk) = weighted_mean(M(unit_i), weight = token_count_i)**
- Never unweighted mean. Otherwise short sentences distort R1.

**3.3.2 Variance Definition (for drift detection)**

- **Var_M(Rk) = weighted_variance(M(unit_i), weight = token_count_i)** (or equivalent explicitly weighted formula).
- Use the same token_count weights as in level aggregation.

**3.3.3 Scale Delta Formula**

For metric M and transition Rk → Rk+1:

- **Δ_Rk→Rk+1(M) = Mean_M(Rk+1) − Mean_M(Rk)** (observed delta).
- **Δ_dev = Δ_observed − Δ_expected** (deviation from expected smoothing).
- Without this formal delta definition, interpretation is underspecified.

**Δ_expected and ε_M** are defined by the **Expected Smoothing Model (ESM)** in **Part D**: corpus-based median of Δ_observed (or H2 bootstrap until corpus exists); ε_M = α·MAD. No remaining gap for definition; implementation must freeze corpus or use bootstrap.

---

## 4. Cross-Scale Analytical Dimensions

These define what the LLM is allowed to reason about.

### A. Scale Consistency

**Definition:** Dominant family persistence across levels.

- dominant_R1 ≈ dominant_R2 ≈ dominant_R3

**Interpretation:**

- **Persistent dominance** → Structural coherence  
- **Shifted dominance** → Mosaic / transition / rhetorical modulation  

### B. Drift Detection

Monitor variance:

- Var_entropy(R3_units)  
- Var_dominance(R3_units)  

If R3 variance remains high → macro instability.  

### C. Compression Loss

If:

- Avg_coverage(R1) > Coverage(R3 aggregate)

Then: signal degradation or dictionary coarseness (conceptual compression destroying signal; structural washout).

### D. Contradiction Localization

**Classification logic:**

| Pattern              | Interpretation                |
|----------------------|------------------------------|
| CP spike at R1 only  | Local rhetorical tension     |
| Elevated baseline at R3 | Systemic chapter inconsistency |
| Elevated at R4       | Thesis-level contradiction   |

### E. Leakage Interpretation

- **Leakage(R1) high + Leakage(R4) low** → Noisy micro language, clear macro thesis  
- **Leakage(R4) high** → Domain discipline breakdown  

---

## 5. Book Profile Object (Reading-Based)

Single composite artifact built from all units. This object becomes the single macro reasoning substrate.

```json
{
  "book_id": "string",

  "level_averages": {
    "R1": {},
    "R2": {},
    "R3": {},
    "R4": {}
  },

  "scale_deltas": {
    "R1_to_R2": {},
    "R2_to_R3": {},
    "R3_to_R4": {}
  },

  "turning_points": [
    {
      "chapter_id": "string",
      "delta_type": "dominance_shift|entropy_jump",
      "magnitude": 0.0
    }
  ],

  "structural_signature": {
    "stable_families": [],
    "variance_profile": {},
    "author_fingerprint": {}
  }
}
```

This is the only object the LLM may interpret at macro level.

### 5.1 Turning Point Detection (Rigorous Definition)

turning_point entries use delta_type: **dominance_shift** | **entropy_jump**.

**Detection rule:** A turning point is recorded if:

1. **|Δ_dev| > ε_M** for metric M (dominance or entropy), and  
2. **The change persists for ≥ 2 consecutive R3 units** (e.g. two adjacent chapters).

This prevents false positives from single-unit noise. **Optional:** require minimum magnitude relative to variance: **|Δ_dev| > k · std_dev(R3, M)** to reduce false triggers in high-noise books (k fixed per spec).

### 5.2 R3 Structural Classification Rules (Mathematical Definitions)

Chapter (R3) typing must be deterministic. Define:

| Type | Condition (numerical) |
|------|------------------------|
| **Coherent Dominant** | dominance > 0.55, entropy < 0.35, leakage < 0.15 |
| **Dual-Tension** | top2_dominance_gap < 0.1, contradiction_pressure > threshold_CP |
| **Fragmented** | entropy > 0.6, dominance < 0.4 |
| **Transitional** | Δ_dev large relative to previous chapter (e.g. \|Δ_dev\| > ε_M for dominance or entropy) |

Thresholds (0.55, 0.35, 0.15, 0.1, 0.6, 0.4, threshold_CP, ε_M) must be: **calibrated on corpus**, **locked per version**, **guarded by Σ**. Otherwise classification drifts across deployments.

### 5.3 Structural Coherence Index (SCI)

Single scalar summary for macro (R4) or per-level comparison:

**SCI = (dominance_mean − entropy_mean − leakage_mean − CP_mean)** normalized to [0, 1].

**Requirement:** All SI_metrics must be **normalized to [0, 1]** prior to SCI computation. Otherwise dominance (0–1) and entropy (e.g. 0–log K normalized) mismatch. Use Mean_M(R4) for each metric; then linear combination and clamp.

Interpretation:

- **High SCI** → Coherent text  
- **Low SCI** → Fragmented text  
- **Patterns** → Propaganda-like (high dominance, low entropy) vs philosophical dialectic (elevated CP, dual-tension).  
One number for structural character.

---

## 6. Constrained Reading-Scale Reasoning Order

The LLM must produce output in this order:

1. **Micro Findings (R1 anomalies)** — Identify spike sentences; report anomaly clusters.

2. **Paragraph Synthesis (R2 clustering)** — Cluster sentences by family dominance; detect local theme formation.

3. **Chapter Structural Type (R3 classification)** — Classify each chapter: Coherent Dominant | Dual-tension | Fragmented | Transitional.

4. **Macro Thesis Structure (R4 optimization profile)** — Describe structural optimization: domain optimized, stability pattern, persistent family cluster.

5. **Cross-Scale Deltas (R1→R4 transitions)** — Explicitly report: dominance shifts, entropy anomalies, leakage anomalies, CP escalation or resolution.

6. **Human-consistent interpretation** — Grounded in deltas. No macro interpretation without delta grounding. No aesthetic summaries before structural validation.

---

## 7. Output Artifacts

### 7.1 Structural Dashboard

Per R-level (R1–R4):

- Mean dominance, mean entropy  
- Worst units (instability), best units (stability)  

### 7.2 Scale Delta Table

| Transition  | ΔDominance | ΔEntropy | ΔLeakage | ΔCP |
|-------------|------------|----------|----------|-----|
| R1→R2       |            |          |          |     |
| R2→R3       |            |          |          |     |
| R3→R4       |            |          |          |     |

### 7.3 Narrative Segmentation

Chapters grouped via:

- Dominance vector similarity  
- Entropy variance proximity  

---

## 8. Core Strength of This Architecture

You obtain:

- Deterministic turning points (not literary intuition)  
- Author domain fingerprint  
- Rhetorical pressure maps  
- Structural coherence index  
- Fragmentation quantification  

This moves analysis from subjective summary → structural audit.

---

## 9. Critical Constraint (Trap Avoidance)

**Rule:** Rk metrics must be computed from the **raw token distribution of that unit level**, not by aggregation of lower-level vectors.

**Explicitly prohibit:**

- Vector averaging of lower-level outputs as the input to Rk  
- Dominance smoothing (e.g. reusing R1 dominance as R2 input)  
- Entropy inheritance (e.g. R3 entropy from R2 values instead of R3 tokens)  

Paragraph/chapter passes MUST NOT:

- Reuse smoothed sentence vectors directly.  
- Derive metrics from simple concatenation.  
- Treat smoothing as signal.  

Each level (R1–R4) must recompute metrics independently using its own token distribution. Comparison uses **deviation-from-expected smoothing**, not raw value comparison.

This is essential when connecting to L1–L9 (e.g. shadow layer): each R-unit runs attribution + L1–L9 on its own token stream.

---

## 10. Operational Principle

You are not analyzing text.  
You are analyzing **reading-scale structure**.  
Meaning emerges from R1→R4 deltas.  
Without deltas: statistics.  
With deltas: structural intelligence.

---

## 11. Mapping to HESPERIA and Guard Integration (Σ / Γ / Θ)

- **Math layers:** L1–L9 (34_SPEC … 42_SPEC) — instrumentation, traversal, shadow, evidence, etc.  
- **Reading/scale levels:** R1–R4 — sentence, paragraph, chapter, book.  
- R-level units receive L1–L9 outputs (and SI_metrics) per unit; book profile and scale_deltas consume R-level aggregates.  

**Guard integration (enforceable pipeline):**

| Guard | Scope | R1–R4 mapping |
|-------|--------|----------------|
| **Σ (Structural Integrity)** | Entropy bounds, dominance minimum, leakage maximum | Apply to each unit’s SI_metrics; hard fail if out of range. |
| **Γ (Consistency Guard)** | Cross-scale persistence, Δ_dev threshold checks | dominant_R1 ≈ R2 ≈ R3; \|Δ_dev\| ≤ ε_M per transition; persist over ≥2 R3 units for turning points. Optional: **R3 variance ceiling** (e.g. Var_M(R3_units) ≤ bound). |
| **Θ (Shadow/Evidence Guard)** | Shadow deviation bounds, trust tier validation | Map L3/L7 shadow deviation and trust tier into unit flags / SI_metrics; enforce bounds. |

This converts the architecture into an enforceable pipeline aligned with HESPERIA Σ/Γ/Θ.

---

## 12. What This Architecture Enables

With the refinements above, the system can compute:

- **Author structural fingerprint** — variance + dominance vector profile across R-levels.  
- **Turning points** — from math (Δ_dev, ε_M, persistence), not intuition.  
- **Writing mode classification** — dialectical vs rhetorical vs fragmented via R3 typing and SCI.  
- **Structural maturity index** — comparable across books (SCI, variance_profile).  
- **Dictionary failure detection** — via compression-loss (Avg_coverage(R1) > Coverage(R3 aggregate)).  

This is no longer “analysis”; it becomes a **scale-aware semantic instrumentation engine**.

---

## 13. Final Structural Summary

The system has three dimensions:

| Dimension | Content |
|-----------|---------|
| **Horizontal** | HESPERIA math layers (L1–L9) |
| **Vertical** | Reading-scale hierarchy (R1–R4) |
| **Governance** | Σ / Γ / Θ |

**Output:** Deterministic Book Profile object (level_averages, scale_deltas, turning_points, structural_signature).

Architecturally clean: one unit schema, weighted aggregation, formal deltas, numerical R3 types, SCI, and guard mapping.

---

## 14. Determinism Audit

The following remove interpretive degrees of freedom and constitute correct engineering discipline:

- Weighted aggregation (token_count)
- Explicit variance weighting (Var_M(Rk))
- Formal delta definition (Δ_Rk→Rk+1(M) = Mean_M(Rk+1) − Mean_M(Rk))
- Δ_dev definition (Δ_observed − Δ_expected)
- ε_M threshold
- Persistence ≥ 2 R3 units for turning points
- Numerical R3 typing (Coherent Dominant, Dual-Tension, Fragmented, Transitional)
- Explicit leakage definition (proportion outside top-N; N constant)
- SCI scalar (with [0,1] normalization requirement)

---

## 15. Structural Soundness by Section (Summary)

| Item | Status | Note |
|------|--------|------|
| **Leakage** | Defined, scale-safe | Proportion outside top-N; **N constant across R-levels** (recommend N=3). |
| **Smoothing law** | Defined (Part D ESM) | Δ_expected = median_corpus(Δ_observed); ε_M = α·MAD; bootstrap tables until corpus. |
| **R3 typing** | Numeric thresholds | Must be calibrated, locked per version, guarded by Σ. |
| **SCI** | Workable | All SI_metrics normalized to [0,1] before subtraction. |
| **Turning points** | Defined | \|Δ_dev\| > ε_M and persist ≥ 2 R3 units; optional \|Δ_dev\| > k·std_dev(R3,M). |

---

## 16. Guard Mapping Validation

| Guard | Mapping | Validation |
|-------|---------|------------|
| **Σ (Structural Integrity)** | Entropy bounds, leakage max, dominance minimum on each unit’s SI_metrics | Correct. |
| **Γ (Consistency Guard)** | dominant_R1 ≈ R2 ≈ R3; \|Δ_dev\| ≤ ε_M; optional R3 variance ceiling | Correct. |
| **Θ (Shadow/Evidence Guard)** | shadow_deviation + trust_tier per unit (from L3/L7) | Correct integration point. |

---

## 17. Conceptual Integrity: 3D Semantic Instrumentation Model

- **Vertical axis:** R1–R4 (reading-scale hierarchy)
- **Horizontal axis:** L1–L9 (math layers)
- **Governance axis:** Σ / Γ / Θ

This forms a **3D semantic instrumentation model**. The architecture is coherent.

---

## 18. What Is Still Missing (Strictly Technical)

**Resolved in Part B:** SI metric equations (entropy, dominance, CP, stability, shadow_deviation, trust_tier). **Resolved in Part D (ESM v1.0):** Δ_expected (corpus median or H2 bootstrap), ε_M (α·MAD or bootstrap), deviation classification, drift model, shadow baseline flat.

**Remaining (freeze in implementation):**

- **Contradiction graph C** (F×F); **Δ_expected table** and **ε bands** (corpus-calibrated or bootstrap per Part D).
- **Band and decision_code** mapping (example in Part B; lock per deployment).
- TopN tie-break (family_id ascending) — Part B Addenda.

---

## 19. Engineering Evaluation and Final Position

**Engineering evaluation:** The specification has moved from a “multi-pass analysis idea” to a **deterministic multi-scale semantic audit protocol**. That is a real architectural step—system-level structure, not a cosmetic rewrite.

**Final position:** Buy decision remains valid. The specification is:

- **Clean** (namespace hygiene; three axes)
- **Deterministic** (weighted aggregation, formal deltas, numerical typing)
- **Guard-aware** (Σ/Γ/Θ mapping)
- **Scale-aware** (R1–R4; expected smoothing)
- **Non-recursive** (each R-level from own tokens)
- **Numerically constrained** (thresholds, N, ε_M, SCI normalization)
- **Pipeline-compatible** (unit schema, book profile, turning points)

It is not hand-wavy. It is not rhetorical. **It is an enforceable contract.**

---

# Part B: SI Metric Equations — Formal Specification (v1.0)

This defines deterministic, scale-agnostic **SI_metrics** computed per unit at any reading level (R1–R4) from raw token→family/area attribution. **Part B Addenda (v1.0.1)** below adds the token→family attribution contract, Top-N locking, secondary metrics (top2 gap, dominance vector), similarity, compression loss, drift indices, and turning-point magnitude.

**Assumptions:**

- Universe: 12 Areas, 288 Families (HESPERIA boundary condition).
- Each token is attributed to exactly one family (hard attribution) or a distribution over families (soft attribution). Both supported; equations are identical if counts are treated as expected counts.

**Notation (per unit u):**

- T(u) = token_count
- Families indexed by f ∈ F, Areas by a ∈ A
- c_f = (expected) number of tokens attributed to family f in unit u
- p_f = c_f / T
- c_a = Σ_{f∈a} c_f, p_a = c_a / T
- TopN_f(u) = set of N families with largest p_f (N fixed by spec, e.g. N=3 or 5)
- **All metrics below must be normalized to [0,1].**

---

## B.0 Base Preconditions (Hard Determinism)

- **If T = 0:** All metrics = 0; trust_tier = T0; flags.band = "spiky" (or "invalid") per convention.
- **If T < T_min** (e.g. 12 tokens): Mark trust_tier at most T1 (low confidence); do not fail.

---

## B.1 Coverage

**Definition:** “How much of the unit is structurally captured by the dictionary signal?” Use Top-N family mass (simple, stable, scale-safe).

**1.1 Coverage (Top-N Family Mass)**

- **coverage = Σ_{f ∈ TopN_f(u)} p_f**
- In [0,1]. Higher = “unit has a clear structural center.” Used for compression-loss comparisons.
- (If “dictionary coverage vs unknown” is needed, extend with an unknown bucket; this equation remains valid if unknown is a family.)

---

## B.2 Dominance

**Definition:** “How concentrated is the unit in its single strongest family?”

**2.1 Dominance (Max Family Share)**

- **dominance = max_f p_f**
- In [0,1].

---

## B.3 Entropy

**Definition:** “How diversified is the distribution?” Use normalized Shannon entropy over families.

**3.1 Family Entropy (Normalized Shannon)**

- K = |{ f : p_f > 0 }| (active families in the unit).
- **If K ≤ 1:** entropy = 0.
- **Else:** H = − Σ_{f: p_f>0} p_f · ln(p_f); H_max = ln(K); **entropy = H / H_max**
- So entropy ∈ [0,1]. Using K compares fairly for short units. For stricter comparability across units, H_max = ln(|F|) is possible but short units then bias low; ln(K) is usually better for R1.

---

## B.4 Leakage

**Definition:** “How much token mass is outside the top structural cluster?”

**4.1 Leakage (Outside Top-N)**

- **leakage = 1 − Σ_{f ∈ TopN_f(u)} p_f** ⇒ **leakage = 1 − coverage** (intended dual).
- If “tail mass excluding unknown” is desired, define TopN over known families only. Keep deterministic.

---

## B.5 Contradiction Pressure (CP)

CP must be deterministic and must not rely on LLM “meaning.” Define CP as simultaneous activation of mutually contradictory families.

**Requirements:**

- A fixed **contradiction relation C ⊂ F×F** (symmetric, no self-pairs), from Dict-B / shadow layer or curated pairs.
- A fixed activation threshold τ for “present” (e.g. p_f ≥ 0.08), or use continuous form below.

**5.1 CP (Continuous Pair Energy)**

- S = { f | p_f > 0 }.
- **CP_raw = Σ_{(i,j) ∈ C, i<j} (p_i · p_j)**
- Normalize to [0,1]: **CP_max = 0.25** (product p_i·p_j maximized at 0.5·0.5 = 0.25 for one strongest pair).
- **contradiction_pressure = min(1, CP_raw / CP_max)**

**5.2 Optional (Thresholded CP):** P = { f | p_f ≥ τ }; CP = (# contradictory pairs in P) / max_pairs. Continuous CP is smoother and less brittle.

---

## B.6 Stability

**Definition:** “Is the unit structurally steady or turbulent?” For a single unit, stability is from its distribution only (not neighboring units).

**6.1 Stability (Entropy-Inverted)**

- **stability = 1 − entropy**
- Clean, deterministic, scale-safe.

**6.2 Alternative (Dominance–Leakage Blend):** stability = clamp01( 0.5·dominance + 0.5·(1 − leakage) ) = clamp01( 0.5·dominance + 0.5·coverage ). **Pick one and lock it.**

---

## B.7 Shadow Deviation

**Definition:** “How far is the unit’s realized attribution from the expected (or ‘surface’) attribution?”

- Two distributions: **p_f^surface** (Dict-A surface), **p_f^shadow** (Dict-B / shadow).
- Use **Jensen–Shannon divergence** (bounded, symmetric).

**7.1 Shadow Deviation (JSD)**

- P = p^surface, Q = p^shadow; M = 0.5·(P+Q). KL with ln base e.
- **JSD(P,Q) = 0.5·KL(P||M) + 0.5·KL(Q||M)**; JSD ∈ [0, ln 2].
- **shadow_deviation = JSD(P,Q) / ln(2)** ∈ [0,1].
- **If shadow layer not available:** shadow_deviation = 0; trust_tier capped at T2 (no structural proof claim).

---

## B.8 Trust Tier (T0–T3)

Deterministic classifier from token_count and guard metrics. Example thresholds (lock per spec):

- T_min_valid = 12, T_good = 60
- τ_shadow = 0.35, τ_leak = 0.25, τ_entropy = 0.65, τ_CP = 0.35

**8.1 Trust Tier Rules (Deterministic)**

| Condition | trust_tier |
|-----------|------------|
| T < T_min_valid | T0 |
| Else if shadow missing | T1 |
| Else if (leakage > τ_leak OR entropy > τ_entropy OR contradiction_pressure > τ_CP OR shadow_deviation > τ_shadow) | T2 |
| Else if T ≥ T_good | T3 |
| Else | T2 |

**Interpretation:** T0 = too short/invalid; T1 = measurable but no shadow evidence; T2 = usable but flagged; T3 = strong, stable, evidence-backed.

---

## B.9 Band and Decision Code (Deterministic Flags)

Bands = pure functions of SI_metrics. Example:

- If trust_tier == T0: band = "spiky"
- Else if entropy > 0.6 and dominance < 0.4: band = "fragmented"
- Else if dominance > 0.55 and leakage < 0.15 and entropy < 0.35: band = "coherent"
- Else: band = "stable"

Decision code = compact code from guard outcomes (e.g. SIGMA_FAIL_LEAK, GAMMA_DRIFT, THETA_SHADOW_DEV, OK). **Lock the mapping.**

---

## B.10 Area-Level Metrics (Optional)

top_areas already emitted. Can define: area_dominance = max_a p_a; area_entropy (same Shannon normalized); area_leakage (outside top-N areas). **Family-based SI_metrics remain canonical; areas are summary.**

---

## B.11 Implementation Notes (Non-optional)

- **TopN selection:** Tie-break by family_id ascending.
- **Floating outputs:** Round to fixed decimals (e.g. 6) for deterministic JSON.
- **Token attribution:** If soft attribution, probabilities sum to 1 per token; generated deterministically (no sampling).

---

## B.12 Minimal SI_metrics Contract (Final)

Per unit u, compute:

| Metric | Formula |
|--------|---------|
| coverage | Σ_{f∈TopN} p_f |
| dominance | max_f p_f |
| entropy | H / H_max (normalized Shannon) |
| leakage | 1 − coverage |
| contradiction_pressure | min(1, Σ_{(i,j)∈C} p_i·p_j / 0.25) |
| stability | 1 − entropy (or locked alternative) |
| shadow_deviation | JSD(surface, shadow) / ln(2) |
| trust_tier | From deterministic rules (§B.8) |

This is enough to make R1–R4 profiling and Σ/Γ/Θ enforcement real.

---

# Part B Addenda — SI Metric Equations (v1.0.1)

Operational layer: **exact inputs** (token→family attribution contract) and **derived/secondary metrics** the R1–R4 architecture depends on (top2 gap, dominance vectors, similarity, segmentation, compression loss, drift, turning-point magnitude).

---

## A. Token→Family Attribution Contract (Input Layer)

### A.1 Hard Attribution (Deterministic)

- Each token t maps to exactly one family: **fam(t) ∈ F**.
- Counts: **c_f = |{ t : fam(t)=f }|**, **T = Σ_f c_f**.
- Yields **p_f = c_f / T**.

### A.2 Soft Attribution (Deterministic)

- Each token yields a distribution: **w(t,f) ≥ 0**, **Σ_f w(t,f) = 1**.
- Expected counts: **c_f = Σ_t w(t,f)**; **p_f = c_f / T**.
- **Rule:** Soft attribution must be produced without sampling; ties resolved deterministically.

### A.3 Unknown / Out-of-Dict Handling

- If a token has no valid family: assign it to special family **F00_UNKNOWN**.
- Keeps **Σ_f p_f = 1** always true and stabilizes coverage/leakage.

---

## B. Lock the “Top-N Cluster” Definition

### B.1 TopN Selection

- N fixed globally (e.g. 3 or 5).
- **Sort** families by **(p_f desc, family_id asc)**.
- **TopN_f(u) =** first N families in sorted list with p_f > 0 (if fewer exist, take all).
- Prevents non-determinism on ties and short units.

### B.2 Tail Mass / Low-Rank Threshold (Optional)

- low-rank set = families with rank > N; leakage = tail mass as already defined. No extra thresholds needed.

---

## C. Secondary Metrics (Formalize)

### C.1 Top-2 Dominance Gap (for Dual-Tension typing)

- Top families by mass: f1, f2; p1 = p_f1, p2 = p_f2 (0 if missing).
- **top2_dominance_gap = p1 − p2** ∈ [0,1].

### C.2 Dominance Vector (for similarity/segmentation)

- Fixed-length over families: **v(u) ∈ R^{|F|}**, **v_f = p_f** (sparse but fixed-length).
- For areas: **v_A(u) ∈ R^{|A|}**, **v_a = p_a**.

---

## D. Similarity Measures (Narrative Segmentation)

### D.1 Cosine Similarity (Family Distribution)

- For units u, v: **sim_cos(u,v) = (v(u)·v(v)) / (||v(u)|| · ||v(v)||)**.
- **Edge case:** if norm is 0 (T=0), similarity = 0.

### D.2 Jensen–Shannon Similarity (Distributional)

- **sim_js(u,v) = 1 − (JSD(p_u, p_v) / ln 2)** ∈ [0,1]. More stable than cosine for probability vectors.
- **Pick one and lock it.** JSD-sim is usually better.

---

## E. Compression Loss Formalization

- Spec: “Avg_coverage(R1) > Coverage(R3 aggregate)” — both sides must be defined.

### E.1 Weighted Mean Coverage at Level Rk

- **Mean_coverage(Rk) = Σ_i (T_i / Σ_j T_j) · coverage(u_i)** (per aggregation contract).

### E.2 Aggregate-Distribution Coverage at Level Rk (Stronger)

- **C_f(Rk) = Σ_i c_f(u_i)**; **P_f(Rk) = C_f(Rk) / Σ_i T_i**.
- **Coverage_agg(Rk) = Σ_{f∈TopN(P(Rk))} P_f(Rk)**.
- Avoids “mean of means” artifacts.

### E.3 Compression Loss Metric

- **compression_loss(Rk→Rk+1) = Mean_coverage(Rk) − Coverage_agg(Rk+1)**.
- Positive and large ⇒ washout / coarseness / over-compression.

---

## F. Drift Formalization

### F.1 Dominance Drift Index (DDI)

- At R3: **DDI_R3 = sqrt(Var_dominance(R3_units))**.
- Higher = more structural turbulence.

### F.2 Entropy Drift Index (EDI)

- **EDI_R3 = sqrt(Var_entropy(R3_units))**.
- Reportable drift indices.

---

## G. Turning Point “Magnitude” (Real Formula)

- Magnitude stored per turning point; must be deterministic.

### G.1 Magnitude for Metric M at Chapter i

- Δ_dev_i(M) = deviation between chapter i−1 and i (R3 units).
- **magnitude = min(1, |Δ_dev_i(M)| / ε_M)**.
- = 1 means “at or beyond threshold”; 1 is clamped. Persistence across ≥2 chapters already required.

---

# Part C: JSON Schema Set for Validation (v1.0)

A strict **JSON Schema 2020-12** set for validating pipeline outputs before any LLM or analyst touches them. Deterministic-friendly and guard-compatible.

**Location:** `schema/` in repo root.

| Schema | Purpose |
|--------|---------|
| **SI_metrics.schema.json** | Reusable definition for all SI_metrics (bounds [0,1]; trust_tier enum T0\|T1\|T2\|T3). |
| **Unit.schema.json** | R1–R4 unit object: unit_id, level (R1\|R2\|R3\|R4), parent_id, token_count, top_areas, top_families, SI_metrics, flags (band, decision_code). |
| **BookProfile.schema.json** | Composite: book_id, level_averages, scale_deltas, turning_points, structural_signature. |

**Conventions:**

- All normalized metrics [0,1]; **trust_tier** enum T0|T1|T2|T3; **level** enum R1|R2|R3|R4.
- **top_areas** / **top_families**: arrays of ranked items (area_id/family_id, coverage, rank) with stable typing (e.g. area_id pattern `^A\d+$`, family_id `^F\d+$`).
- Optional fields explicitly marked; everything else required.
- **unit_id**: structured format `R<level>:<id>` (e.g. R1:sent_1, R3:CH04); pattern `^R[1-4]:.+`.

**Hard fixes applied:**

- **SI_means** (in level_summary): each metric bounded [0,1].
- **SI_variances** (in level_summary): each metric bounded [0, 0.25] (variance of [0,1] r.v. ≤ 0.25).
- **delta_expected**: required; fill with **0.0** or use **ESM bootstrap values (Part D)** until corpus-based calibration is available.
- **unit_id**: pattern enforced for stable IDs.

**Validation:** Use these schemas to validate pipeline outputs (Unit per R1–R4 unit, BookProfile for the composite) before passing to LLM or reporting. Unit.schema.json validates every R1/R2/R3/R4 unit; BookProfile.schema.json validates the composite only.

---

# Part D: Expected Smoothing Model (ESM) v1.0

**Goal:** Define **Δ_expected(M, Rk→Rk+1)** for each SI metric M and each transition (R1→R2, R2→R3, R3→R4), and define **ε_M** tolerance bands. This closes the last conceptual gap between “metrics” and a real structural engine. Requirements: **deterministic**, **calibratable**, **guard-compatible**, **not hand-wavy**, **not theory-fiction**.

---

## D.1 What Smoothing Actually Means

When scale increases (more tokens aggregated):

- **Dominance** ↑ (law of concentration)
- **Entropy** ↓ (law of averaging)
- **Leakage** ↓
- **CP** ↓ (local contradictions wash out)

This is multinomial math, not philosophy. We use an **empirical structural baseline** (reference corpus) rather than a theoretical derivation.

---

## D.2 Model Structure (Three Layers)

**Layer A — Observed Delta**

For metric M and transition Rk→Rk+1:

- **Δ_observed(M, Rk→Rk+1) = Mean_M(Rk+1) − Mean_M(Rk)**  
  Weighted means only (per §3.3).

**Layer B — Expected Delta**

Expected smoothing is **corpus-calibrated**:

- **Δ_expected(M, Rk→Rk+1) = median_corpus(Δ_observed)**  
  Median is taken over the **reference corpus**, same transition, same metric. Smoothing is structurally grounded, not guessed.

**Layer C — Tolerance Band (ε_M)**

Use robust dispersion (scale-adaptive):

- **MAD = median(|Δ_i − median|)**  
- **ε_M = α · MAD**, with **α ∈ [2.5, 3.5]** (default **3.0**).

---

## D.3 Why Median + MAD

- Distribution of deltas is not Gaussian; heavy tails exist; literary books vary widely.
- Mean + std misbehaves. **Median + MAD is stable.**

---

## D.4 Required Corpus Size

- **Minimum** to stabilize smoothing: **50 books** (usable); **100+** preferred; mix genres.
- Per metric M and transition T, compute and then **freeze per version**:  
  **Δ_expected[M][T]**, **ε[M][T]**.

---

## D.5 Default Bootstrap Model (Until Corpus Exists)

If no reference corpus exists yet, use the **default Δ_expected** and **default ε** in **Part D Addenda** below. **Temporary**; replace with corpus-based calibration when available. Summary: dominance/entropy/leakage/CP/stability/shadow_deviation per transition; fixed ε per metric.

---

## D.6 Deviation Definition (Final)

For metric M:

- **Δ_dev = Δ_observed − Δ_expected**

**Classification:**

| Condition | Interpretation |
|-----------|----------------|
| \|Δ_dev\| ≤ ε | Normal smoothing |
| \|Δ_dev\| > ε | Structural anomaly |
| \|Δ_dev\| > 2ε | Strong anomaly |

**Turning points** (per §5.1): **\|Δ_dev\| > ε** **and** persists ≥ 2 R3 units.

---

## D.7 Scale Consistency Formalization

- **Dominant at Rk** = argmax_f P_f(Rk aggregate).
- **Scale consistency** holds if: dominant_R1 = dominant_R2 = dominant_R3, or same family in Top2 consistently.
- Deviation here is **categorical** (family identity), not numeric.

---

## D.8 Drift Model (R3 Turbulence)

- **Drift_index_R3(M) = sqrt(Var_M(R3_units))** (per Part B Addenda §F).
- **Drift_expected(M)** = baseline from corpus (when available).
- **Drift_dev = Drift_index − Drift_expected**
- If **Drift_dev > ε_drift** → macro instability (Γ flag).

---

## D.9 Shadow Deviation Behavior

- **Δ_expected_shadow = 0** across scale. Shadow deviation should **not** systematically change with scale.
- Any consistent drift of shadow_dev across scale suggests: dictionary inconsistency, shadow mapping instability, or structural re-interpretation. Shadow smoothing baseline is **flat**.

---

## D.10 Mathematical Sanity Check

This model satisfies:

- **Deterministic** (given frozen Δ_expected and ε)
- **Corpus-calibratable** (median + MAD from reference corpus)
- **Not dependent on text semantics**
- **Independent per metric**
- **Compatible with Σ / Γ / Θ**

---

## D.11 Integration into Guards

| Guard | Integration |
|-------|-------------|
| **Σ (Integrity)** | Reject if entropy > hard upper bound or leakage > hard upper bound. Independent of smoothing. |
| **Γ (Consistency)** | Flag if \|Δ_dev\| > ε; dominant family shift; Drift_dev > ε_drift. |
| **Θ (Shadow)** | Flag if shadow_dev > threshold; or shadow_dev increases across scale. |

---

## D.12 What This Model Enables

With ESM in place you can:

- Detect **structural turning points**
- Detect **mosaic books**
- Detect **rhetorical fragmentation**
- Detect **dictionary compression failure**
- Detect **systemic contradiction**
- Detect **scale instability**

All without subjective interpretation.

---

## D.13 Final Missing Piece (After ESM)

To make the system **mathematically complete**, freeze:

1. **Contradiction graph C** (F×F pairs)
2. **Δ_expected table** (corpus-based, or default table below until then)
3. **ε bands** per transition (corpus MAD-based, or default ε below)

After that: you no longer have an “analysis system”—you have a **calibrated structural instrument**.

---

# Part D Addenda: Default Parameters and Bounds (v1.0)

Applies until corpus-calibrated model replaces it. **No corpus required; no empirical calibration required; no probabilistic behavior.** System behaves conservatively. Later replace Δ_expected and ε with corpus-calibrated values.

---

## D Add.1 Default Δ_expected Table

**1.1 R1 → R2**

| Metric | Δ_expected |
|--------|------------|
| dominance | +0.04 |
| entropy | −0.07 |
| leakage | −0.04 |
| contradiction_pressure | −0.02 |
| stability | +0.07 |
| shadow_deviation | 0.00 |

**1.2 R2 → R3**

| Metric | Δ_expected |
|--------|------------|
| dominance | +0.05 |
| entropy | −0.08 |
| leakage | −0.05 |
| contradiction_pressure | −0.03 |
| stability | +0.08 |
| shadow_deviation | 0.00 |

**1.3 R3 → R4**

| Metric | Δ_expected |
|--------|------------|
| dominance | +0.03 |
| entropy | −0.05 |
| leakage | −0.03 |
| contradiction_pressure | −0.02 |
| stability | +0.05 |
| shadow_deviation | 0.00 |

**Coverage:** Since coverage = 1 − leakage (Part B), **Δ_expected_coverage = −Δ_expected_leakage** per transition (e.g. R1→R2: +0.04).

---

## D Add.2 Default ε (Tolerance Bands)

Uniform conservative bands. Use for all transitions until corpus MAD-based ε available.

| Metric | ε |
|--------|---|
| dominance | 0.05 |
| entropy | 0.06 |
| leakage | 0.05 |
| contradiction_pressure | 0.05 |
| stability | 0.06 |
| shadow_deviation | 0.08 |

**Interpretation:**

| Condition | Interpretation |
|-----------|----------------|
| \|Δ_dev\| ≤ ε | Normal smoothing |
| ε < \|Δ_dev\| ≤ 2ε | Moderate anomaly |
| \|Δ_dev\| > 2ε | Strong anomaly |

---

## D Add.3 Default Drift Baseline (R3 Turbulence)

Until corpus calibration:

| Metric | Drift_expected |
|--------|----------------|
| dominance | 0.08 |
| entropy | 0.10 |
| leakage | 0.08 |
| contradiction_pressure | 0.07 |

**Drift ε:** ε_drift = 0.05

If **Drift_index_R3(M) − Drift_expected(M) > ε_drift** → **macro instability** (Γ flag).

---

## D Add.4 Default Hard Σ Bounds (Integrity Guard)

Absolute caps; independent of smoothing. **Fail** (Σ reject) if violated.

| Metric | Hard limit |
|--------|------------|
| entropy | > 0.85 → fail |
| leakage | > 0.75 → fail |
| dominance (R3/R4) | < 0.15 → fail |
| shadow_deviation | > 0.85 → fail |
| contradiction_pressure | > 0.80 → fail |

These prevent pathological outputs.

---

## D Add.5 Default R3 Typing Thresholds (Locked)

| Type | Condition |
|------|-----------|
| **Coherent Dominant** | dominance > 0.55 AND entropy < 0.35 AND leakage < 0.15 |
| **Dual-Tension** | top2_gap < 0.10 AND contradiction_pressure > 0.25 |
| **Fragmented** | entropy > 0.60 AND dominance < 0.40 |
| **Transitional** | \|Δ_dev\| > ε_M for dominance or entropy (relative to previous chapter); or unclassified by above |

No ambiguity. Evaluate in order; first match wins, or Transitional.

---

## D Add.6 Default SCI Normalization

**SCI_raw** = dominance_mean − entropy_mean − leakage_mean − contradiction_pressure_mean

**SCI** = clamp01( (SCI_raw + 1) / 2 )

Guarantees **SCI ∈ [0, 1]**.

---

## D Add.7 Default Trust Tier Thresholds

| Condition | Tier |
|-----------|------|
| token_count < 12 | T0 |
| no shadow layer | T1 |
| shadow_dev > 0.35 OR leakage > 0.40 OR entropy > 0.70 | T2 |
| token_count ≥ 60 AND shadow_dev ≤ 0.35 (and none of the T2 conditions) | T3 |
| otherwise | T2 |

---

## D Add.8 Shadow Smoothing Rule (Locked)

**Δ_expected_shadow = 0** for all transitions.

Shadow deviation must **not** drift with scale. Any consistent drift → Γ flag (dictionary inconsistency or shadow mapping instability).

---

## D Add.9 Deterministic Behavior Summary

With these defaults:

- **No corpus required**
- **No empirical calibration required**
- **No probabilistic behavior**
- **No unstable sensitivity**
- System behaves **conservatively**

Later: replace Δ_expected and ε with corpus-calibrated values.

---

## D Add.10 Final State

With Part A–D and this addenda you have:

| Component | Status |
|-----------|--------|
| SI metric equations | Part B |
| JSON schemas | Part C |
| Deterministic aggregation | §3.3 |
| Turning point rules | §5.1, D.6, D Add.2 |
| Drift rules | D.8, D Add.3 |
| Guard thresholds | §11, D.11, D Add.4 |
| Default smoothing model | D.5, D Add.1 |
| Default ε bands | D Add.2 |
| Default drift baseline | D Add.3 |
| Default Σ bounds | D Add.4 |
| Default R3 typing | D Add.5 |
| Default SCI normalization | D Add.6 |
| Default trust tier | D Add.7 |
| Shadow smoothing rule | D Add.8 |

**There are no undefined quantities left.** The system can run end-to-end without missing values.

---

*Next steps (if required): replace defaults with corpus-calibrated Δ_expected/ε/drift in implementation; freeze C; integration mapping into HESPERIA Σ/Γ/Θ guard framework.*

---

## Appendix: Buy / No-Buy Reflection (Ethan)

### Verdict: **Buy**

**Why we buy it**

1. **Clean separation from math layers** — R1–R4 (sentence → book) are explicitly not L1–L9. No naming collision; the spec is a reading-scale *consumer* of L1–L9 outputs (SI_metrics, bands, decision_code), not a replacement.

2. **Single unit schema** — One canonical unit object for R1–R4 (unit_id, level, top_areas, top_families, SI_metrics, flags) gives a stable contract for pipelines: run L1–L9 per segment, attach results to that schema, then aggregate. No schema drift per level.

3. **Expected smoothing law** — Dominance ↑, entropy ↓, leakage ↓, stability ↑ with scale is a testable structural hypothesis. We get deviation detection (Δ_expected, ε) instead of ad hoc interpretation. That supports automated checks and guard-style thresholds (Σ/Γ/Θ).

4. **Constrained reasoning order** — R1 anomalies → R2 clustering → R3 classification → R4 thesis → cross-scale deltas → human interpretation. LLM (or any analyst) is forced to ground macro claims in R1→R4 deltas. “No macro interpretation without delta grounding” reduces unsupported summary.

5. **Book profile as single macro substrate** — level_averages, scale_deltas, turning_points, structural_signature (stable_families, variance_profile, author_fingerprint) give one composite artifact for “whole book” reasoning and reporting. No proliferation of ad hoc book metrics.

6. **Trap avoidance** — Each R-level recomputes from its own token distribution; no reuse of smoothed sentence vectors as signal. That keeps R2/R3/R4 from being trivial echoes of R1 and keeps comparisons on deviation-from-expected, not raw value drift.

**What we get**

| Outcome | Use |
|--------|-----|
| Deterministic turning points | Chapter/part boundaries and “where structure shifts” from deltas, not taste. |
| Author domain fingerprint | structural_signature.author_fingerprint for comparison and consistency checks. |
| Rhetorical pressure maps | CP/leakage/dominance by R-level and transitions (R1→R2, etc.). |
| Structural coherence index | Scale consistency (dominant_R1 ≈ R2 ≈ R3) + variance/drift. |
| Fragmentation quantification | Bands (spiky/fragmented/coherent), worst/best units, R3 variance. |
| Dashboard + delta table + narrative segmentation | Reportable artifacts; chapters grouped by dominance/entropy similarity. |

**Risks / conditions**

- **Implementation** — R2/R3/R4 require segmenters (paragraph, chapter, book/part). The spec assumes these exist; they are out of scope for the spec itself.
- **SI_metrics and L1–L9** — The unit schema references SI_metrics (coverage, dominance, entropy, leakage, etc.). We must map L1–L9 (and L8 SI_*) into this schema; the spec’s §11 acknowledges this and leaves the mapping to implementation.
- **ε and Δ_expected** — Defined in **Part D (Expected Smoothing Model v1.0)**: corpus median + MAD (or H2 bootstrap); freeze per version for full determinism.

**Summary** — We buy the R1–R4 reading-scale model because it gives a deterministic, schema-driven, delta-grounded way to analyze structure across scales, fits HESPERIA’s L1–L9 and guards, and avoids the “smoothing as signal” trap. What we get is a clear contract for multi-pass structural analysis and reportable artifacts (dashboard, deltas, book profile) that move from subjective summary to structural audit.

---

## Reflection on Gaps (Before Plan)

**Saved state:** This specification is complete for v1.0: all SI metrics defined (Part B + Addenda), aggregation and scale-delta contract fixed (§3.3), ESM with default Δ_expected and ε (Part D + Part D Addenda), JSON schemas (Part C), guard integration (Σ/Γ/Θ), and default bounds (Σ hard limits, R3 typing, SCI, trust tier, shadow rule). No undefined quantities remain for running the pipeline with defaults.

**What is still missing or deferred (by design):**

| Gap | Status | Notes |
|-----|--------|------|
| **Corpus-calibrated ESM** | Deferred | Replace default Δ_expected and ε (and drift baseline) with corpus median + MAD once ≥50–100 books available. |
| **Contradiction graph C** | To freeze | Fixed F×F relation (curated or Dict-B); required for CP. Lock in implementation. |
| **Segmenters** | Out of scope | R2/R3/R4 need paragraph/chapter/book segmenters; spec assumes they exist. |
| **L1–L9 → Unit schema mapping** | Implementation | Map L8 SI_* and L1–L7 outputs into Unit.SI_metrics and flags; spec references, does not define. |
| **Band/decision_code mapping** | Lock per deployment | Example in Part B; final code set (e.g. SIGMA_FAIL_LEAK, GAMMA_DRIFT) to be locked. |
| **theoretical_smoothing_change (analytic)** | Optional | ESM uses empirical baseline (or bootstrap); analytic model (e.g. Dirichlet) could be added later. |

**Conclusion:** The spec is **implementation-ready**. Remaining work is to freeze C, implement segmenters and L→Unit mapping, and optionally replace defaults with corpus calibration.

---

## Implementation Plan

1. **Freeze and persist defaults** — Commit default Δ_expected table (D Add.1), ε (D Add.2), drift baseline (D Add.3), Σ bounds (D Add.4), R3 typing (D Add.5), SCI formula (D Add.6), trust tier (D Add.7), and shadow rule (D Add.8) as the canonical v1.0 default set (e.g. in `sphere_rag` or a dedicated config under version control).
2. **Contradiction graph C** — Define or import C ⊂ F×F (symmetric, no self-pairs); persist as a versioned artifact; wire into CP computation (Part B.5).
3. **Segmenters** — Implement or integrate paragraph, chapter, and book/part segmenters so R2/R3/R4 units can be produced; document segmenter contract (input: full text or token stream; output: span or token ranges per unit).
4. **L1–L9 → Unit mapping** — For each segment (R1–R4), run L1–L9 (or minimal set L1, L8 for SI_*); map outputs into canonical Unit schema (Unit.schema.json); validate with Part C schemas.
5. **Pipeline end-to-end** — Build pipeline: segment → per-segment L1–L9 → Unit objects → aggregation (weighted means/variances) → scale_deltas (Δ_observed, Δ_expected from defaults) → Δ_dev, turning points, book profile; validate BookProfile against schema.
6. **Optional: corpus calibration** — When corpus exists, compute Δ_expected and ε (and drift baseline) per metric/transition; replace defaults; re-version ESM (e.g. v1.1).

**Architect:** Ethan. Proceed on this plan.
