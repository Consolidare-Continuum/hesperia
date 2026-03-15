# LEVEL 1 — AREA STRUCTURE (TFP / Kernberg domain)

**Цель:** Закрепить топологию 10 областей для домена TFP (Transference-Focused Psychotherapy) / теории Кернберга.

**Data:** `spec/area_structure_tfp.yaml` — canonical definition of 10 areas with purpose and adjacency.

---

## T1.1 Define Areas

| Area ID | area_index | Name (EN) |
|---------|------------|-----------|
| A1 | 0 | Drives & Affects |
| A2 | 1 | Object Relations |
| A3 | 2 | Defensive Operations |
| A4 | 3 | Aggression |
| A5 | 4 | Perversions |
| A6 | 5 | Narcissism |
| A7 | 6 | Love / Relational Capacity |
| A8 | 7 | Structural Diagnosis |
| A9 | 8 | Therapeutic Technique |
| A10 | 9 | Treatment Process |

Mapping: `area_index` 0–9 = public operational areas. Topology remains 12-node icosahedral; indices 10–11 are reserved. Outputs and domain semantics use these 10 areas only.

---

## T1.2 Define Area Purpose

Каждая область в `spec/area_structure_tfp.yaml` имеет:

| Field | Description |
|-------|-------------|
| **description** | Short semantic description of the area. |
| **clinical_scope** | What this area covers in clinical/TFP terms. |
| **activation_signals** | Lexical/conceptual signals that activate this area (e.g. keywords, themes). |
| **exclusions** | What is explicitly out of scope or excluded from this area. |

Used for: interpretation labels, diagnostics, propagation semantics, and reporting.

---

## T1.3 Define Area Adjacency

По икосаэдру (12 узлов); для 10 операционных областей (0–9):

| Concept | Description |
|---------|-------------|
| **area_neighbors** | For each area (0–9), list of neighboring area indices (subset of 0–9). Derived from icosahedral adjacency; only operational neighbors are listed. |
| **area_distance** | Shortest-path distance matrix (10×10) or per-area metrics. Computed from full 12-node topology; used for propagation decay and semantic traversal. |

Использование:

- **activation propagation** — L7 propagation uses full 12×12 adjacency; area_neighbors gives the operational view.
- **semantic traversal** — neighbor list defines which areas are one step away.
- **metric calculation** — diameter = 3 (icosahedron); distance matrix from `sphere.topology.metrics.shortest_path_distances` / `graph_diameter`.

Source of truth for adjacency: `sphere/topology/topology_loader.py` (ICOSAHEDRAL_ADJACENCY_LIST, get_icosahedral_adjacency()). The YAML stores the **operational** neighbor list (indices 0–9 only) for reference and tooling.

---

## File layout

```
spec/area_structure_tfp.yaml   # T1.1 + T1.2 + T1.3 (neighbors; distance from topology)
docs/specs/LEVEL1_AREA_STRUCTURE.md  # this spec
```

Runtime: topology loader and propagation use existing 12-node icosahedron; projection layer exposes 10 areas. Domain labels (A1–A10 names, purpose) are read from `area_structure_tfp.yaml` when needed for reporting or diagnostics.

**Loader:** `sphere.topology.area_structure.load_area_structure_tfp(path=None)` — returns full YAML dict. Helpers: `get_operational_area_neighbors(area_index)`, `get_area_distance_matrix()`.
