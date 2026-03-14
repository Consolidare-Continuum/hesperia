# PIPELINE LAYER REGISTRY v1 (INTERNAL ONLY)

**Classification:** Internal. Do not expose publicly. Public docs cannot reconstruct the full transformation chain.

---

## 1. Pipeline Stage Overview (Internal)

| Stage | Role | Transformations | Internal inputs/outputs | Invariants | Branch conditions |
|-------|------|-----------------|--------------------------|------------|-------------------|
| Attribution | Tokenize, match Dict A/B, produce (family_id, altitude) matched list. | normalize → tokenize → attribute | text → tokens → matched, hits | Dict A/B canonical; side_id only from Dict A | No match → empty hits |
| L1 | Base metrics from hits + optional profile. | See MATH_LAYER_REGISTRY L1 | matched, F, A → L1 output | — | Profile active vs inactive |
| L2 | Traversal from dominant family/area. | Build adjacency, BFS/traversal, aggregate by depth | L1, hits, adjacency → L2 output | — | Stub vs real adjacency |
| L3 | Shadow comparison B vs S. | Compare L1_B/L2_B vs L1_S/L2_S | L1_B, L2_B, L1_S, L2_S → L3 output | — | Shadow enabled vs disabled |
| L4 | Evidence support, integrity. | Retrieval match, area match, shortfall gate | L1, L2, chunks, R_B, R_S → L4 output | — | Empty R_B/R_S handling |
| L5 | Counter-evidence, reality gate. | Contradiction pressure, trig checks | L1, L2, L4 → L5 output | — | — |
| L6 | Stability, Lyapunov. | Sensitivity, curvature, global stability | L1, L2, mass_at_depth → L6 output | — | — |
| L7 | Cross-layer gates, decision code. | Consistency gates, confidence, tag | L1..L6 → L7 output | Code 75 reserved | Multiple gate branches |
| L8 | SI units. | Scale to COUNT/RATIO/PERCENT/U1000 | L1..L7 → L8 output | — | — |
| L9 | Bands, pillars, brand/action. | Final human-facing bands | L3, L4, L7, L8 → L9 output | — | — |
| Bridge (KME/domain) | Hit-to-node, relation synthesis. | Matched → concept hits, relation candidates; domain graph. | matched → hits, relations; graph construction | Ontology-grounded; internal topology | — |

---

## 2. Internal Diagnostics (Not Public)

- Per-layer intermediate state (L1..L9 raw dicts).
- Visited set, adjacency, mass_at_depth.
- Bridge: hit-to-node mapping, relation synthesis rules, expansion logic.
- Pipeline order and exact transitions.

---

## 3. Public Narrative (Collapsed)

Public-facing narrative is defined in PUBLIC_PIPELINE_NARRATIVE_v1.md. It does **not** include:

- 10 explicit internal stages.
- Bridge layer specifics.
- Layer propagation model.
- Topology synthesis sequence.

Only: ingest text → structural analysis → evidence extraction → comparison/divergence evaluation → report generation.
