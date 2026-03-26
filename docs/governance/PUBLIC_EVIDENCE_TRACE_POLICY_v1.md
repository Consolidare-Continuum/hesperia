# PUBLIC EVIDENCE TRACE POLICY v1

**Status:** Active  
**Purpose:** Expose evidence for trust without exposing mechanics. Evidence explains conclusions, not the engine.

---

## 1. Principle

Public evidence must support **trust** (reproducibility, auditability, explanation of outcomes) without **disclosure** of internal method (topology, propagation, layer chain, coordinates). The trust line is: **evidence may be visible; method may not.**

---

## 2. What Public Evidence MAY Include

| Allowed | Description |
|---------|--------------|
| Matched text span | The substring or phrase that triggered a match (for explainability). |
| Activated concept / public policy family | Which concept or policy family was activated, using **public** family indices (0–239) or public-safe labels only. |
| Confidence or strength band | Scalar or band (e.g. high/medium/low) for match strength. |
| Document location | Offset, paragraph, or segment reference for where the evidence appears. |
| Report explanation | Short natural-language explanation of why a conclusion was reached (e.g. “emphasis on fairness and order”). |

---

## 3. What Public Evidence MUST NOT Include

| Forbidden | Reason |
|-----------|--------|
| Internal coordinates | No area index, family index (internal 0–287), hex index, or side index. |
| side_id | No raw side_id or internal relation id in any form that reveals structure. |
| Adjacency path | No graph traversal path, neighbor indices, or topology steps. |
| Propagation path internals | No propagation steps, diffusion weights, or layer-by-layer state. |
| Hidden area/family references | No mention of reserved areas (10, 11) or reserved families (240–287). |
| Internal layer names | No L1, L2, … L9 or execution_flow stage names in user-facing evidence. |
| Formula or dependency graph | No exposure of how metrics are computed. |

---

## 4. Implementation

- All evidence that is emitted to **public** reports, API responses, or operator-facing logs must pass through the **public projection layer** (`apply_public_projection` / `sanitize_public_trace`).
- Evidence trace builders must use **public vocabulary** only (macro-domain, policy family, structural position as opaque id if needed).
- Reserved structures are filtered out before any evidence is written; no trace entry may reference a reserved area, family, or side_id.

---

## 5. Acceptance Criterion

**Evidence explains conclusions, not the engine.** A reader of the evidence trace can understand what was matched and where, and can trust that the summary is consistent with the raw_text and calibration, but cannot infer topology, geometry, propagation logic, or internal layer design.
