# LEVEL 14 — Clinical ActiveGraph Bridge to KME

Final integration layer between the clinical/NLP subsystem and the HESPERIA mathematical core. Converts propagated activation state into a KME-compatible hierarchical graph.

## Purpose

- **Raw_text:** Propagated activation after NLP + topological propagation (`concepts`, `families`, `areas`).
- **Output:** A graph with three node levels (concept, family, area) and typed edges, suitable for inspection, visualization, and feeding into KME metrics.
- **Execution Flow:** Session text → Dict-A/Dict-B → activation → propagation → **Clinical ActiveGraph** → (optional) KME primitives/derived/fingerprint.

## Node levels

| Level   | Example id   | node_type | Fields |
|--------|---------------|-----------|--------|
| Concept | B_A3_F1_001 | concept   | id, weight, area_id, family_id, label?, metadata |
| Family  | A3_F1        | family   | id, weight, area_id, family_id, metadata |
| Area    | A3           | area     | id, weight, area_id, metadata |

Rules:

- Concept nodes use propagated concept weights.
- Family nodes use propagated family weights.
- Area nodes use propagated area weights.
- Only nodes with score ≥ **ACTIVATION_THRESHOLD** (default **0.01**) are created.

## Edge types

| Edge type            | Description                    | Weight rule |
|----------------------|--------------------------------|-------------|
| belongs_to_family    | Concept → Family               | concept_weight |
| belongs_to_area      | Family → Area                  | family_weight |
| activates, opposes, … | Concept ↔ Concept (from concept_relations) | min(src, tgt) or active×0.5 if other inactive |
| intra_area_adjacent  | Family ↔ Family (same area, zone neighbors) | min(source, target) |
| bridge               | Family ↔ Family (cross-area from family_embedding) | min(source, target) |
| area_adjacent        | Area ↔ Area (icosahedral topology) | min(source, target); only if both areas ≥ **AREA_ACTIVE_THRESHOLD** (0.05) |

## Weighting rules

- **Concept–concept:** If both concepts active: `weight = min(source_weight, target_weight)`. If only one active: `weight = active_weight * 0.5`. Deterministic.
- **Family–family (intra + bridge):** `weight = min(family_weight_source, family_weight_target)`.
- **Area–area:** `weight = min(area_weight_source, area_weight_target)`.

## Merging and determinism

- **No duplication:** The same logical edge `(source, target, edge_type)` can be produced from multiple sources (e.g. hierarchy and topology). Edges are merged by keeping the **maximum** weight for that key. Documented in code.
- **Determinism:** Nodes sorted by `id`. Edges sorted by `(source, target, edge_type)`.

## Thresholds

| Constant               | Default | Meaning |
|------------------------|--------|---------|
| ACTIVATION_THRESHOLD   | 0.01   | Do not create nodes/edges below this (noise). |
| AREA_ACTIVE_THRESHOLD  | 0.05   | Minimum area score to include in area-adjacency edges. |

## Sources

- **Concept nodes/relations:** `hesperia/ontology/dictB/concept_nodes.yaml`, `concept_relations.yaml`.
- **Family topology:** `specs/canon/family_embedding_tfp.yaml` (zones + bridges).
- **Area topology:** `specs/canon/area_structure_tfp.yaml` (area_neighbors).

## Output shape

```json
{
  "nodes": [
    { "id": "B_A3_F1_001", "node_type": "concept", "weight": 0.82, "area_id": "A3", "family_id": "A3_F1" },
    { "id": "A3_F1", "node_type": "family", "weight": 0.91, "area_id": "A3" },
    { "id": "A3", "node_type": "area", "weight": 1.0 }
  ],
  "edges": [
    { "source": "B_A3_F1_001", "target": "A3_F1", "edge_type": "belongs_to_family", "weight": 0.82 },
    { "source": "A3_F1", "target": "A3", "edge_type": "belongs_to_area", "weight": 0.91 }
  ],
  "metadata": {
    "source": "clinical_bridge",
    "node_count": 3,
    "edge_count": 2,
    "levels": ["concept", "family", "area"]
  }
}
```

## Integration with KME

- **Hierarchical graph:** `build_clinical_active_graph_hierarchical(activation_result)` returns the dict above. Use for visualization or custom metrics.
- **Concept-only KME path:** Existing `build_clinical_active_graph(activation_result, domain_graph)` returns the KME `ActiveGraph` (concept nodes only) for `compute_primitives` / fingerprint.
- **End-to-end from text:**
  - `analyze_session_to_kme_graph(text, embedding=...)` → hierarchical graph (with optional propagation if `embedding` is provided).
  - `run_session_kme_pipeline(text, source_id=..., embedding=...)` → `analyze_session` (with propagation) → `run_kme_from_activation` → MetricReport (primitives, derived, fingerprint).

## Functions (clinical_bridge.py)

- `load_clinical_relation_sources(...)` — Load concept nodes, concept relations, family embedding, area structure.
- `build_active_concept_nodes`, `build_active_family_nodes`, `build_active_area_nodes` — Node builders.
- `build_hierarchical_edges` — concept→family, family→area.
- `build_concept_relation_edges` — concept↔concept from concept_relations.
- `build_family_topology_edges` — intra_area_adjacent + bridge from family_embedding.
- `build_area_topology_edges` — area_adjacent from area_structure.
- `build_clinical_active_graph_hierarchical(activation_result, ...)` — Full execution_flow; returns dict with nodes, edges, metadata.
- `analyze_session_to_kme_graph(text, embedding=..., **kwargs)` — text → session measurement → hierarchical graph.
- `run_session_kme_pipeline(text, source_id=..., embedding=...)` — text → session measurement → KME MetricReport.

## Summary

After LEVEL 14, the full wiring is:

```
session text
  → Dict-A markers
  → Dict-B concepts
  → family / area activation
  → topological propagation
  → Clinical ActiveGraph (hierarchical)
  → [optional] KME concept graph → primitives / derived / fingerprint
  → trajectory / report
```

The clinical semantic engine is fused with the mathematical core at the Clinical ActiveGraph boundary.
