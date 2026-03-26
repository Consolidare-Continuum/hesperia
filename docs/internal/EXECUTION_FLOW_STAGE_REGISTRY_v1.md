# EXECUTION FLOW STAGE REGISTRY v1 (INTERNAL ONLY)

**Classification:** Internal. Do not expose publicly. Public docs cannot reconstruct the full transform chain.

---

## 1. Execution Stage Overview (Internal)

| Stage | Role | Transformations | Internal INPUT/OUTPUT | Invariants | Branch conditions |
| ----- | ---- | --------------- | --------------------- | ---------- | ----------------- |
| Attribution | Tokenize, match Dict A/B, produce (family_id, altitude) matched list. | normalize -> tokenize -> attribute | RAW_TEXT -> TOKEN_STREAM -> matched, hits | Dict A/B canonical; side_id only from Dict A | No match -> empty hits |
| L1 | Base metrics from hits + optional profile. | See MATH_LAYER_REGISTRY L1 | matched, F, A -> L1 OUTPUT | - | Profile active vs inactive |
| L2 | Traversal from dominant family/area. | Build adjacency, BFS/traversal, aggregate by depth | L1, hits, adjacency -> L2 OUTPUT | - | Stub vs real adjacency |
| L3 | Shadow comparison B vs S. | Compare L1_B/L2_B vs L1_S/L2_S | L1_B, L2_B, L1_S, L2_S -> L3 OUTPUT | - | Shadow enabled vs disabled |
| L4 | Evidence support, integrity. | Retrieval match, area match, shortfall gate | L1, L2, chunks, R_B, R_S -> L4 OUTPUT | - | Empty R_B/R_S handling |
| L5 | Counter-evidence, reality gate. | Contradiction pressure, trig checks | L1, L2, L4 -> L5 OUTPUT | - | - |
| L6 | Stability, Lyapunov. | Sensitivity, curvature, global consistency | L1, L2, mass_at_depth -> L6 OUTPUT | - | - |
| L7 | Cross-layer gates, decision code. | Consistency gates, confidence, tag | L1..L6 -> L7 OUTPUT | Code 75 reserved | Multiple gate branches |
| L8 | SI units. | Scale to COUNT/RATIO/PERCENT/U1000 | L1..L7 -> L8 OUTPUT | - | - |
| L9 | Bands, pillars, brand/action. | Final human-facing bands | L3, L4, L7, L8 -> L9 OUTPUT | - | - |
| Bridge (KME/domain) | Hit-to-node, relation synthesis. | Matched -> concept hits, relation candidates; domain graph. | matched -> hits, relations; graph construction | Ontology-grounded; internal topology | - |

---

## 2. Internal Diagnostics (Not Public)

- Per-layer intermediate state (L1..L9 raw dicts).
- Visited set, adjacency, mass_at_depth.
- Bridge: hit-to-node mapping, relation synthesis rules, expansion logic.
- Execution order and exact transitions.

---

## 3. Public Narrative (Collapsed)

Public-facing narrative is defined in `PUBLIC_PIPELINE_NARRATIVE_v1.md`. It does **not** include:

- 10 explicit internal stages.
- Bridge layer specifics.
- Layer propagation model.
- Topology synthesis sequence.

Only: ingest text -> structural MEASUREMENT -> evidence extraction -> comparison/divergence EVALUATION -> report generation.
