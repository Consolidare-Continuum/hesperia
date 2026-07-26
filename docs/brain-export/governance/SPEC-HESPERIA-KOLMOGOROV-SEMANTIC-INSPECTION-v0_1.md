# Hesperia — Kolmogorov Semantic Inspection (KSI) v0.1

**Document ID:** `24_SPEC__Kolmogorov_Semantic_Inspection_v0_1`  
**Short name:** **KSI** (Kolmogorov Semantic Inspection) / **KSI-Inspector**  
**Status:** FORMALIZATION — **triaged** 2026-06-14. Rows **HES-62-00**, **KSI-01..19** on [active.md](../active.md); gate: **6.1-final** before KSI execution.  
**Authority:** Ethan (governance) + igareosh (operator).  
**Promotion target:** `docs/specs/24_SPEC__Kolmogorov_Semantic_Inspection_v0_1.md` on `igareosh/hesperia`  
**Target release:** HESPERIA 0.6.2 (KSI layer) — builds on 0.6.1 runtime without breaking it.  
**Added:** 2026-06-13.  
**Depends on:** CD v1.0 (`ETHAN-CONCEPT-DICTIONARY-CD-V1-PACKET-2026-03-27.md`), GTP (`23_SPEC__`), IPoW (`22_SPEC__`), `HESPERIA-TFP-YIELDED-PARAMETERS-TABLE.md`, `HESPERIA-TFP-RUNTIME-VARIABLES-TABLE.md`.

---

## 0. Document control

| Field | Value |
|-------|-------|
| **Version** | `0.1.0` |
| **KAN inheritance** | Edge is a function, not a weight. No neural network. No gradient. No backpropagation. |
| **Core object** | Semantic Transfer Function `Φ_e` per directed concept edge. |
| **Central mathematical object** | Semantic Residual `R_j = Expected_j − Observed_j`. |
| **Product name** | Kolmogorov Semantic Inspection / KSI-Inspector (`ksi.v0_1`). |

---

## 1. Scope

### 1.1 What KSI IS

KSI is a **deterministic semantic inspection framework** that:

1. Models every concept-to-concept relation in the Hesperia graph as a **bounded semantic transfer function Φ_e** — not a weight.
2. Computes **expected activations** (forward) and **expected causes** (mirror / backward) from the existing concept graph.
3. Compares expectations against **observed runtime activations**.
4. Produces **semantic residuals** per concept, per route, per family, per area.
5. Classifies residuals into **typed incidents**.
6. Packages incidents as **structured prompts** for an **LLM Teacher**.
7. Accepts **candidate repairs** from the LLM Teacher and validates them through an **acceptance gate** and **sandbox**.

### 1.2 What KSI IS NOT

| Not | Why |
|-----|-----|
| A neural network | No neurons, no layers, no training loop. |
| Gradient descent | No loss function, no backpropagation. |
| KAN (Kolmogorov-Arnold Network) | Borrows the principle (edge = function). Inherits no neural computation. |
| An LLM reasoning layer | LLM is Teacher-on-demand, not the inference engine. |
| A replacement for 0.6.1 propagation | KSI wraps and inspects it; it does not replace it. |
| A new semantic model | KSI inspects the existing concept dictionary, relation graph, and propagation results. |

### 1.3 KAN inspiration — one sentence

The Kolmogorov-Arnold contribution borrowed here is:

> **Relation = behavior, not number.**

Classical semantic graph: `Concept_i —[weight]→ Concept_j`  
KSI graph: `Concept_i —[Φ_e]→ Concept_j`

Where `Φ_e` is a bounded scalar function over parameters that already exist in Hesperia 0.6.1.

---

## 2. Hesperia floor map

KSI sits on top of existing Hesperia floors. It does not modify them.

```
Floor 0 — Markers / lexical (DLCR, dict_a, dict_b)
Floor 1 — Concepts (identity, CD schema)
Floor 2 — Concept Relations (4000+ typed edges)
Floor 3 — Families (F# aggregation)
Floor 4 — Areas (area_id activation, softmax, inhibition)
Floor 5 — Topology (hex, GCS, IPoW, GTP)
Floor 6 — Propagation (propagation_trace, invariant_activation)
Floor 7 — Audit (trace, evidence, sentence_index)
─────────────────────────────────────────────────────────
PENTHOUSE — KSI Layer (this spec)
  • Φ_e transfer functions  (use Floor 1–2 parameters)
  • Expected activation     (use Floor 6 propagation)
  • Mirror cause scoring    (use Floor 2 incoming edges)
  • Semantic Residual       (compare Floor 6 vs. Φ)
  • Incident classification (uses all floors)
  • LLM Teacher interface
  • Acceptance Gate + Sandbox
```

---

## 3. Core objects

### 3.1 Directed edge

For every directed relation in the concept graph:

```
e = (Concept_i → Concept_j, type_e)
```

- `i` = source concept (from Floor 1 CD)
- `j` = target concept
- `type_e` = relation type (Floor 2)

### 3.2 Semantic Transfer Function Φ_e

**Canonical formula:**

```
Φ_e(A_i, C, Θ_e) = sat( A_i × W_e × R_e × Q_e × S_e × C_e × P_e × D_e − K_e )
```

**Output:** scalar ∈ [0, 1] — the expected contribution from Concept_i to Concept_j activation via edge e.

---

## 4. Parameter definitions and Hesperia floor mapping

### 4.1 Source activation: A_i

| Symbol | Definition | Hesperia source |
|--------|-----------|----------------|
| `A_i` | Observed activation of source concept i ∈ [0, 1] | `invariant_activation.concepts[concept_id]` (Floor 6) |

### 4.2 Base relation weight: W_e

| Symbol | Definition | Hesperia source |
|--------|-----------|----------------|
| `W_e` | Base semantic strength of the edge, as stored on the relation record | CD `effects.amplifies[j]` or relation-level `weight` field (Floor 2) |
| Range | [0, 1] | — |
| Default | 0.5 | CD default `*` |

### 4.3 Relation type coefficient: R_e

| Symbol | Definition | Hesperia source |
|--------|-----------|----------------|
| `R_e` | Multiplicative coefficient derived from relation type | Floor 2 typed edge `type_e` |

**Canonical R_e table (v0.1):**

| Relation type | R_e | Justification |
|---------------|-----|---------------|
| `activates` | 1.00 | Direct trigger |
| `expresses` | 0.80 | Strong semantic signal |
| `co_occurs_with` | 0.60 | Co-presence, not causation |
| `observed_in` | 0.50 | Contextual evidence |
| `defends_against` | 0.40 | Inhibitory context |
| `opposes` | −0.70 | Semantic contradiction |
| `requires` (CD constraint) | 0.90 | Prerequisite — blocks or boosts |
| `family_bias` | 0.55 | Floor 3 family proximity |
| `inhibits` (CD effect) | −0.60 | Direct suppression |
| *(unlisted type)* | 0.50 | Safe default |

`R_e` for `opposes` and `inhibits` is negative — this becomes a **subtraction** inside sat(), captured in the inhibition term `K_e` as well.

### 4.4 Evidence quality: Q_e

| Symbol | Definition | Hesperia source |
|--------|-----------|----------------|
| `Q_e` | Quality of evidence supporting this edge activation | CD `validation.confidence_floor` for source concept; weighted by `min_evidence` count floor |
| Range | [0, 1] | — |
| Formula | `Q_e = clamp(evidence_count / min_evidence, 0, 1) × confidence` | |

If no evidence data, `Q_e = Q_default` (configurable, default 0.6).

### 4.5 Specificity: S_e

| Symbol | Definition | Hesperia source |
|--------|-----------|----------------|
| `S_e` | Specificity of the target concept within the current area/family context | CD `structure.primary_area` match to active area → S_e = 1.0; secondary_areas match → 0.7; no match → 0.4 |
| Range | [0.2, 1] | — |

### 4.6 Context match: C_e

| Symbol | Definition | Hesperia source |
|--------|-----------|----------------|
| `C_e` | How well the current session context matches the relation's expected activation context | `areas` activation of concept j's `primary_area` in current session; scale [0, 1] |
| Practical formula | `C_e = areas[j.primary_area]` from `invariant_activation.areas_final` (Floor 6) | — |

This maps context to the activation field already computed in 0.6.1.

### 4.7 Polarity / contradiction modifier: P_e

| Symbol | Definition | Hesperia source |
|--------|-----------|----------------|
| `P_e` | Sign and scale modifier from polarity: direct, reversed, or suppressed activation | CD `interaction.contradiction` list — if target j is in source i's contradiction list, P_e = −1.0; else P_e = +1.0 |
| Range | {−1, +1} or ∈ [−1, +1] for gradient polarity | — |

### 4.8 Distance decay: D_e

| Symbol | Definition | Hesperia source |
|--------|-----------|----------------|
| `D_e` | Exponential decay by topological or conceptual graph distance | `D_e = λ^d` where `d` = hop distance and `λ` = `HESPERIA_LAMBDA` (runtime env, core_math bucket) |
| Range | (0, 1] | — |
| Note | Direct edge (d=1): `D_e = λ`. Two-hop: `D_e = λ²`. | — |

### 4.9 Inhibition / contradiction pressure: K_e

| Symbol | Definition | Hesperia source |
|--------|-----------|----------------|
| `K_e` | Total inhibition pressure on this edge from competing or suppressing signals | `HESPERIA_K_GUARD` (global guard) + CD `effects.inhibits[j]` for source i × active activation of other competing concepts |
| Range | [0, 1] | — |
| Default | `HESPERIA_K_GUARD` (currently in env) | — |

Full formula:

```
K_e = k_guard + Σ (inhibit_weight(m → j) × A_m)
      for all m that inhibit j and are active (A_m ≥ threshold)
```

Where `k_guard = HESPERIA_K_GUARD`.

### 4.10 Saturation function: sat()

**v0.1 (simple bounded):**

```
sat(x) = min(1.0, max(0.0, x))
```

**v0.2 upgrade path (smooth bounded):**

```
sat(x) = x / (1 + |x|)        # smooth, always ∈ (−1, 1)
```

Maps to CD `activation.saturation_k` — when `saturation_k` is configured on the target concept j, use it to tune the boundary gradient:

```
sat_k(x) = x / (1 + saturation_k × |x|)
```

---

## 5. Expected activation (forward)

For target concept j, aggregate all incoming edge contributions:

```
Expected_j = sat( Σ Φ_e(A_i, C, Θ_e) )
             for all e: (i → j) in concept graph
```

Interpretation: **given currently active source concepts and context, what activation should Concept_j receive?**

If no incoming edges exist for j: `Expected_j = 0`.

**Area and family roll-up:**

```
Expected_family_F = Σ Expected_j  for all j ∈ F    (then normalized)
Expected_area_A   = Σ Expected_j  for all j where j.primary_area = A  (then normalized)
```

---

## 6. Mirror expectation (backward)

For an **observed active concept j** (Observed_j ≥ τ_active), score each incoming edge as a potential cause:

```
CauseScore(i → j) = A_j × W_e × R_e × Q_e × C_e × S_e
```

**Note:** No decay D_e in mirror direction — we are asking "which sources explain this activation", not propagating forward.

Ranked list of cause candidates for concept j:

```
Causes_j = sorted [
  (Concept_i, CauseScore(i → j))
  for all e: (i → j)
]
descending by CauseScore
```

**Interpretation:** If Concept_j is active, which upstream concepts should be active to explain it?

**Mirror deficit:**

```
MirrorDeficit_j = Observed_j − Σ CauseScore(i → j)
                  for all i where A_i ≥ τ_active
```

High `MirrorDeficit_j` means: "Concept_j is active but its expected causes are not sufficiently active." This signals a **routing gap** or **missing bridge**.

---

## 7. Semantic Residual

The central mathematical object:

```
Residual_j = Expected_j − Observed_j
```

**Interpretation table:**

| Residual range | Meaning | Incident class |
|----------------|---------|----------------|
| `Residual_j > +τ` | Expected activation far exceeds observed — something blocked it | `UNDER_ACTIVATED` |
| `Residual_j < −τ` | Observed activation exceeds expectation — spurious / unexplained | `OVER_ACTIVATED` |
| `|Residual_j| ≤ τ` | Activation is explained — system coherent | `COHERENT` (no incident) |

Threshold `τ` is a calibration parameter (v0.1 default: `τ = 0.25`).

**Residuals propagate to floors:**

```
Residual_family_F = Expected_family_F − Observed_family_F
Residual_area_A   = Expected_area_A   − Observed_area_A
```

---

## 8. Incident types

### 8.1 Dead concept

```
Condition:
  Expected_j ≥ τ_expected   (default 0.50)
  Observed_j ≤ τ_dead       (default 0.10)

Incident: DEAD_CONCEPT
Meaning:  Concept_j should be active — but it is not. Possible causes:
          missing lexical entry, missing dictionary word, dead route, broken edge.
```

### 8.2 Dead route

```
Condition:
  Source concept i is active (A_i ≥ τ_active)
  Edge e: (i → j) has W_e > 0, R_e > 0
  But Observed_j ≤ τ_dead

Incident: DEAD_ROUTE(i → j)
Meaning:  Transfer function predicts activation across this edge.
          Runtime observed nothing.
          Possible causes: inhibition override, wrong relation weight, bad context score.
```

### 8.3 Over-activated (wrong activation)

```
Condition:
  Observed_j ≥ τ_active     (default 0.50)
  Expected_j ≤ τ_explain    (default 0.15)

Incident: OVER_ACTIVATED
Meaning:  Concept_j is active but no upstream edge explains it.
          Possible causes: spurious lexical hit, wrong dictionary match,
          polarity inversion missing, incomplete exclusion rule.
```

### 8.4 Under-explained activation

```
Condition:
  Observed_j > 0
  Expected_j > 0
  Residual_j > +τ   (significant positive gap)

Incident: UNDER_EXPLAINED_ACTIVATION
Meaning:  Partial explanation — some edges fire, but activation is insufficient.
          Possible causes: missing bridge concepts, low W_e, poor Q_e (evidence quality).
```

### 8.5 Mirror deficit incident

```
Condition:
  Observed_j ≥ τ_active
  MirrorDeficit_j > τ_mirror   (default 0.40)

Incident: MIRROR_DEFICIT(j)
Meaning:  Concept_j is active, but known causal paths cannot account for it.
          Potential unreachable activation — LLM Teacher should probe upstream.
```

### 8.6 Routing conflict

```
Condition:
  Two or more incoming edges to j have P_e = +1 (activating)
  AND P_e = −1 (inhibiting) both firing simultaneously
  AND |Residual_j| > τ

Incident: ROUTING_CONFLICT(j)
Meaning:  Contradictory signals — activation and inhibition colliding on same concept.
```

---

## 9. Missing bridge score

For any pair of concepts (i, j) that **co-appear** in a session without a strong direct edge:

```
BridgeNeed(i, j) =
  CoActivation(i, j)
  × ContextMatch(i, j)
  × FamilyCompatibility(i, j)
  × Residual_j
  × Gap(i, j)
```

**Component definitions:**

| Term | Definition | Hesperia source |
|------|-----------|----------------|
| `CoActivation(i,j)` | Both A_i and A_j ≥ τ_active in same session | `invariant_activation.concepts` (Floor 6) |
| `ContextMatch(i,j)` | Same area or family active | `areas_final` / family overlap (Floors 3–4) |
| `FamilyCompatibility(i,j)` | i and j share family_bias or primary_area | CD `structure` fields (Floor 1) |
| `Residual_j` | From §7 | — |
| `Gap(i,j)` | `1 − ExistingRelationStrength(i,j)` — 1 if no edge, 0 if strong direct edge | Floor 2 relation lookup |

**Threshold:** `BridgeNeed(i,j) ≥ τ_bridge` (default 0.55) → emit `MISSING_BRIDGE(i→j)` incident.

**Interpretation:** The LLM Teacher should consider proposing `Concept_i → Concept_j` as a new candidate edge.

---

## 10. Parameter cross-reference table

All Φ terms mapped to existing Hesperia runtime variables and CD fields:

| Φ term | Hesperia 0.6.1 source | Configurable via |
|--------|-----------------------|-----------------|
| `A_i` | `invariant_activation.concepts[i]` | CD `activation.base_weight`, `activation.cap` |
| `W_e` | Relation `weight` field or CD `effects.amplifies[j]` | Relation asset / CD calibration |
| `R_e` | Derived from relation `type_e` | KSI `relation_type_coefficients.json` (new asset) |
| `Q_e` | CD `validation.confidence_floor` × `min_evidence` | CD calibration |
| `S_e` | CD `structure.primary_area` match vs active `areas_final` | CD + floor 4 |
| `C_e` | `areas_final[j.primary_area]` | `HESPERIA_ALPHA`, signal_calibration_v2 |
| `P_e` | CD `interaction.contradiction` list | CD calibration |
| `D_e` | `HESPERIA_LAMBDA`^d (hop distance d from propagation_trace) | `HESPERIA_LAMBDA` (core_math env) |
| `K_e` | `HESPERIA_K_GUARD` + CD `effects.inhibits[j]` × A_m | `HESPERIA_K_GUARD`, `HESPERIA_K_DISP` |
| `sat()` | CD `activation.saturation_k` | CD calibration |
| `τ` (residual threshold) | `HESPERIA_DELTA_GAP` (core_math env) or KSI config | `HESPERIA_DELTA_GAP` |
| `τ_active` | CD `activation.threshold` (source) | CD `activation.threshold` |
| `τ_dead` | CD `activation.threshold` × 0.2 (heuristic, v0.1) | KSI config |
| `τ_expected` | `HESPERIA_ALPHA` × 0.5 (heuristic, v0.1) | KSI config |
| `λ` in D_e | `HESPERIA_LAMBDA` | env (core_math) |
| `k_guard` in K_e | `HESPERIA_K_GUARD` | env (core_math) |

---

## 11. Full inspection pipeline

```
Input text
    │
    ▼
Floor 0: Markers / DLCR / dict_a lookup
    │
    ▼
Floor 1–2: Concept activations (A_i) + Relation graph (edges, types)
    │
    ▼
Floor 3–4: Family + Area aggregation (families_final, areas_final)
    │
    ▼
Floor 6: Propagation trace (invariant_activation, propagation_trace)
    │
    ▼  ←─────────────────────────────────────────────┐
KSI Layer:                                            │
    │                                                 │
    ├── Compute Φ_e for all edges          (§4)       │
    │                                                 │
    ├── Compute Expected_j (forward)       (§5)       │
    │                                                 │
    ├── Compute CauseScore + MirrorDeficit (§6)       │
    │                                                 │
    ├── Compute Residual_j (all concepts)  (§7)       │
    │                                                 │
    ├── Classify incidents                  (§8)      │
    │                                                 │
    └── Score missing bridges              (§9)       │
             │                                        │
             ▼                                        │
    Incident bundle (typed, ranked)                   │
             │                                        │
             ▼                                        │
    LLM Teacher (§12)                                 │
             │                                        │
             ▼                                        │
    Proposal (repair candidate)                       │
             │                                        │
             ▼                                        │
    Acceptance Gate (§13)                             │
             │                                        │
             ▼                                        │
    Sandbox Validation (§14)  ───── REJECT ──────────┘
             │
             ▼ ACCEPT
    Relation graph update / CD update
```

---

## 12. LLM Teacher interface

### 12.1 Input packet

```json
{
  "ksi_version": "0.1",
  "session_id": "...",
  "iteration_id": "...",
  "incidents": [
    {
      "incident_type": "DEAD_CONCEPT",
      "concept_id": "SHAME",
      "expected": 0.82,
      "observed": 0.10,
      "residual": 0.72,
      "incoming_edges": [
        { "source": "FAILURE", "type": "activates", "W_e": 0.8, "R_e": 1.0 }
      ],
      "active_concepts_in_session": ["FAILURE", "REJECTION"],
      "context_area": "interpersonal_regulation",
      "mirror_deficit": null
    }
  ],
  "missing_bridges": [
    {
      "concept_i": "REJECTION",
      "concept_j": "WITHDRAWAL",
      "bridge_need_score": 0.71,
      "existing_edge_strength": 0.0
    }
  ]
}
```

### 12.2 Output proposal

```json
{
  "proposals": [
    {
      "action": "add_edge",
      "source": "REJECTION",
      "target": "WITHDRAWAL",
      "type": "activates",
      "W_e_proposed": 0.70,
      "justification": "...",
      "confidence": 0.85
    },
    {
      "action": "update_edge_weight",
      "source": "FAILURE",
      "target": "SHAME",
      "W_e_current": 0.40,
      "W_e_proposed": 0.75,
      "justification": "...",
      "confidence": 0.78
    }
  ]
}
```

### 12.3 LLM Teacher rules

- LLM Teacher is **advisory only**. It outputs proposals. It does not write to the graph.
- Proposals are typed: `add_edge`, `remove_edge`, `update_edge_weight`, `add_concept`, `update_cd_field`.
- Each proposal carries a `confidence` score and `justification` string.
- The Teacher prompt MUST include: incident type, concept ids, residual values, active session context. No raw clinical text reaches the Teacher.

---

## 13. Acceptance Gate

For each proposal, all conditions must pass:

| Check | Condition | Block on failure |
|-------|-----------|-----------------|
| **Schema valid** | Proposal matches KSI proposal schema | YES — discard |
| **Type legal** | Proposed edge type exists in `relation_type_coefficients` | YES — discard |
| **W_e range** | 0.0 ≤ `W_e_proposed` ≤ 1.0 | YES — discard |
| **No contradiction loop** | Proposed edge does not create activation-inhibition contradiction cycle | YES — discard |
| **Confidence floor** | `confidence ≥ τ_teacher` (default 0.65) | YES — discard |
| **Human-in-loop flag** | If `action = add_concept` or `remove_edge`, requires operator approval | PAUSE |

Proposals passing all checks → Sandbox.

---

## 14. Sandbox Validation

**Purpose:** Verify that the proposed repair actually improves residuals on known sessions without degrading healthy activations.

```
Input:  One or more gold fixture sessions (from calibration corpus)
        + Accepted proposal (one at a time)

Steps:
  1. Apply proposal to a copy of the concept graph.
  2. Run full KSI pipeline on fixture session.
  3. Compute Residual_j_before and Residual_j_after for all concepts.
  4. Check:
       Residual_j_after < Residual_j_before for the incident concept.
       No new incidents created in non-affected concepts (|ΔResidual| ≤ τ_sandbox for all others).

Accept:  Both checks pass.
Reject:  Any check fails → proposal discarded, incident remains open.
```

Sandbox does not require an LLM call. It is a deterministic re-run of Φ_e + residual computation on fixtures.

---

## 15. KSI output fields (bundle extension)

KSI appends a `ksi` block to the existing TFP / invariant_activation bundle:

```json
{
  "ksi": {
    "version": "0.1",
    "concepts": {
      "SHAME": {
        "expected": 0.82,
        "observed": 0.31,
        "residual": 0.51,
        "incident": "UNDER_EXPLAINED_ACTIVATION"
      }
    },
    "areas": {
      "interpersonal_regulation": {
        "expected": 0.65,
        "observed": 0.44,
        "residual": 0.21,
        "incident": null
      }
    },
    "incidents": [ ... ],
    "missing_bridges": [ ... ],
    "phi_trace": {
      "FAILURE→SHAME": {
        "A_i": 0.85,
        "W_e": 0.40, "R_e": 1.0, "Q_e": 0.90,
        "S_e": 1.0,  "C_e": 0.72, "P_e": 1.0,
        "D_e": 0.80, "K_e": 0.05,
        "phi_raw": 0.854, "phi_sat": 0.854
      }
    }
  }
}
```

This is additive — does not change existing `tfp_vector`, `areas`, `families`, `propagation_trace` fields.

---

## 16. New configuration assets

Assets produced by this spec (no existing HESPERIA assets modified):

| Asset | Purpose | Location (Hesperia product repo) |
|-------|---------|----------------------------------|
| `ksi_config_v01.json` | Global thresholds (τ, τ_active, τ_dead, τ_bridge, τ_teacher), version pin | `assets/data/ksi/ksi_config_v01.json` |
| `relation_type_coefficients_v01.json` | R_e table (§4.3) — all known relation types → coefficient | `assets/data/ksi/relation_type_coefficients_v01.json` |
| `ksi_proposal_schema.json` | LLM Teacher proposal schema (§12.2) | `schemas/ksi_proposal_schema.json` |
| `ksi_incident_schema.json` | Incident bundle schema (§8) | `schemas/ksi_incident_schema.json` |

New env variables to add to `ALLOWED_HESPERIA_ENV`:

| Variable | Bucket | Role |
|----------|--------|------|
| `HESPERIA_KSI_ENABLED` | ksi | Master gate for KSI layer |
| `HESPERIA_KSI_CONFIG` | ksi | Path to `ksi_config_v01.json` |
| `HESPERIA_KSI_PHI_TRACE` | ksi | Include `phi_trace` in bundle output |
| `HESPERIA_KSI_LLM_TEACHER` | ksi | Enable LLM Teacher call |
| `HESPERIA_KSI_TEACHER_MODEL` | ksi | LLM model for Teacher |
| `HESPERIA_KSI_SANDBOX_FIXTURES` | ksi | Path to sandbox fixture sessions |
| `HESPERIA_KSI_TAU` | ksi | Residual threshold τ override |
| `HESPERIA_KSI_TAU_BRIDGE` | ksi | Bridge need threshold override |
| `HESPERIA_KSI_TAU_TEACHER` | ksi | Teacher confidence floor override |

---

## 17. Relation to existing HESPERIA modules

| Existing module | KSI interaction | KSI changes it? |
|-----------------|----------------|-----------------|
| CD v1.0 (concept dictionary) | Provides `base_weight`, `saturation_k`, `threshold`, `amplifies`, `inhibits`, `contradiction` | **No** — read-only |
| `propagation_trace` | Provides observed activations `A_i`, hop distances d | **No** — read-only |
| `invariant_activation` | Primary source of `Observed_j` per concept, `areas_final`, `families_post_hex` | **No** — read-only |
| `signal_calibration_v2.json` | Provides area/concept calibration basis for C_e | **No** — read-only |
| `area_inhibition_matrix` | Feeds K_e in aggregate (area-level) | **No** — read-only |
| GTP (`23_SPEC__`) | Path discovery; Ψ coherence field — potential future hook into C_e | **No** in v0.1 |
| IPoW (`22_SPEC__`) | Interior point — future hook into context relevance for C_e | **No** in v0.1 |
| Session Inspector (`SPEC-ETHAN`) | Display surface for KSI incidents + residuals — Pane 2 extension | **Extension** in v0.2 |

---

## 18. Phased delivery

| Phase | Scope | Release |
|-------|-------|---------|
| **KSI-P0** | Φ_e formula engine (pure Python, no side effects); unit tests on fixture concept pairs; `phi_trace` output | 0.6.2-alpha |
| **KSI-P1** | Forward Expected_j for all concepts in a session; Residual computation; DEAD_CONCEPT + OVER_ACTIVATED incident classification; KSI bundle block | 0.6.2-beta |
| **KSI-P2** | Mirror CauseScore + MirrorDeficit; MIRROR_DEFICIT incidents; Missing bridge scoring | 0.6.2-rc |
| **KSI-P3** | LLM Teacher packet generation (no LLM call yet — packet only); Acceptance Gate schema validation | 0.6.2 |
| **KSI-P4** | Live LLM Teacher call; Sandbox validation; full repair loop | 0.7.0 |
| **KSI-P5** | Session Inspector Pane 2 extension (residual visualization, incident strip) | 0.7.x |

---

## 19. Task decomposition (for Grace triage)

Tasks to be triaged into `active.md` after this spec is confirmed:

| ID | Owner | Description |
|----|-------|-------------|
| **KSI-01** | Gena | Freeze `relation_type_coefficients_v01.json` — all Floor 2 relation types → R_e coefficients (§4.3). |
| **KSI-02** | Gena | Implement `phi_e(A_i, W_e, R_e, Q_e, S_e, C_e, P_e, D_e, K_e) → float` — pure function, full parameter set, `sat()` v0.1. Unit tests with fixtures. |
| **KSI-03** | Felix | `ksi_config_v01.json` schema + default values for all τ thresholds (§16). |
| **KSI-04** | Felix | `ksi_incident_schema.json` + `ksi_proposal_schema.json` (§16). |
| **KSI-05** | Gena | `compute_expected_j(j, concept_graph, activations, config) → float` — forward aggregation of Φ_e over all incoming edges (§5). |
| **KSI-06** | Gena | `compute_residual(j, expected_j, observed_j) → float` + incident classification (§7–8). |
| **KSI-07** | Gena | `compute_mirror_cause_scores(j, concept_graph, activations, config) → list` + MirrorDeficit (§6). |
| **KSI-08** | Gena | `compute_bridge_need(i, j, session_state, config) → float` — missing bridge scorer (§9). |
| **KSI-09** | Felix | Wire KSI pipeline into bundle: `ksi` block in invariant_activation output (§15). Env gate: `HESPERIA_KSI_ENABLED`. |
| **KSI-10** | Felix | `phi_trace` in bundle output when `HESPERIA_KSI_PHI_TRACE=1` (§15). |
| **KSI-11** | Gena | LLM Teacher packet serializer — incidents + missing bridges → structured JSON prompt (§12.1). |
| **KSI-12** | Felix | Acceptance Gate (§13) — schema + cycle check + confidence floor + PAUSE on operator-required changes. |
| **KSI-13** | Gena | Sandbox Validation (§14) — deterministic replay of Φ_e on gold fixtures, before/after residual check. |
| **KSI-14** | Noah | Gold fixture sessions for KSI sandbox (minimum 3 labelled sessions with known concept activations). |
| **KSI-15** | Sophia | Risk review — no clinical text in LLM Teacher packet; PII gate on concept labels. |
| **KSI-16** | Marcus | Operator runbook — how to review KSI incidents, how to approve proposals, how to trigger sandbox. |
| **KSI-17** | Ethan | Add `HESPERIA_KSI_*` env variables to `ALLOWED_HESPERIA_ENV` in `env_guard.py` (§16). |
| **KSI-18** | Felix | Gold tests — fixed concept activation inputs → known Φ_e, Expected_j, Residual_j, incident type. Deterministic. |
| **KSI-19** | Ava | Session Inspector Pane 2 extension design — KSI residual strip + incident chip (Phase P5, after 0.6.2 stable). |

**Grace**: triage KSI-01 through KSI-18 with priority. KSI-02 and KSI-05 are blockers for all downstream. KSI-01 unblocks KSI-02.

---

## 20. Open questions (not blocking v0.1 spec)

| ID | Question | Proposed resolution |
|----|---------|---------------------|
| **OQ-1** | Should `Q_e` be per-edge or per-concept? | Per-concept (source CD `validation`) for v0.1; per-edge in v0.2 if relation-level evidence becomes available. |
| **OQ-2** | Should family/area residuals generate separate incidents or aggregate from concept residuals? | Aggregate from concept in v0.1 (§5 roll-up). Separate family-level thresholds in v0.2. |
| **OQ-3** | GTP Ψ as C_e input? | Not in v0.1. After GTP-05 lands, evaluate using Ψ as context signal in C_e calculation. |
| **OQ-4** | Multi-hop Φ_e chains (concept paths, not direct edges)? | Only direct edges (d=1) in v0.1. Two-hop paths computed as compound D_e (λ²) in v0.2. |
| **OQ-5** | Should `opposes` R_e = −0.70 appear in K_e instead? | For v0.1, negative R_e is absorbed by K_e. v0.2 may separate polarity and inhibition more cleanly. |

---

## Appendix A — Canonical formula summary (one-page reference)

```
Semantic Transfer Function:
  Φ_e = sat( A_i × W_e × R_e × Q_e × S_e × C_e × P_e × D_e − K_e )

Forward expectation:
  Expected_j = sat( Σ Φ_e )  for all e: i → j

Mirror cause score:
  CauseScore(i→j) = A_j × W_e × R_e × Q_e × C_e × S_e

Semantic residual:
  Residual_j = Expected_j − Observed_j

Mirror deficit:
  MirrorDeficit_j = Observed_j − Σ CauseScore(i→j)  for active i

Missing bridge:
  BridgeNeed(i,j) = CoActivation × ContextMatch × FamilyCompatibility × Residual_j × Gap(i,j)

Saturation (v0.1):
  sat(x) = min(1, max(0, x))

Decay:
  D_e = HESPERIA_LAMBDA ^ d

Inhibition:
  K_e = HESPERIA_K_GUARD + Σ (inhibit_weight(m→j) × A_m)
```

---

## Appendix B — Doctrine statement

> Kolmogorov Semantic Inspection in HESPERIA models each concept relation as a bounded semantic transfer function Φ_e. The Inspector compares forward expected activation and mirror expected causes against observed runtime activation. The difference becomes a semantic residual, used to detect dead concepts, wrong activations, weak relations, and missing bridges. All parameters are sourced from existing Hesperia floors (CD, relation graph, propagation trace, area activations). No neural computation. No training loop. No gradient.

---

`SIGNED: Developer (Felix) | Claude Code context | 2026-06-13 | HESPERIA KSI v0.1 spec — brain repo governance`
