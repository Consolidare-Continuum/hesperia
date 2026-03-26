<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Context RAG — packet JSON schema

**Purpose**: Contract for the **input_context packet** returned by `cluster/chroma-server/context_rag.py`. Cursor and automation can rely on this shape. **Ref**: [HESPERIA-RAG-DAEMON-MVP-PROPOSAL-ETHAN.md](HESPERIA-RAG-DAEMON-MVP-PROPOSAL-ETHAN.md). **Core mode (areas and families only)**: [ETHAN-HESPERIA-CORE-MODE-MVP.md](ETHAN-HESPERIA-CORE-MODE-MVP.md) — no retrieval, no statements/books; outputs for logic tests.

---

## 1. Top-level keys

| Key | Type | Always present | Description |
|-----|------|----------------|-------------|
| `matrix_source` | string | Yes | `"csv"` or `"chroma"` (source of matrix data for calculable block). |
| `calculable` | object | Yes | Geometry, path, road, borders, traversal, loopability (same shape as matrix_run output). |
| `coherence_hints` | object | Yes | Short block for agent to adjust input_context: current_area_id, suggested_adjacent_areas, traversal_summary, border_passings_count. |
| `observability` | object | Yes | Telemetry only (v0.1): loopability_band, entropy_metric, border_passings_count, direction, ring_distance_from_start, safeguard_events_count. Ref: projects/hesperia/HESPERIA_OBSERVABILITY_EXTENSION_v0_1.md. |
| `retrieval` | object | No | Present when CLI used with --query or --area_id or --family_name. Contains families[] and optionally chunks[]. |

---

## 2. `calculable` (object)

Same topology as the JSON returned by `matrix_run.py` (without the top-level `matrix_source` duplicated). All fields from matrix_run are under `calculable`:

| Key | Type | Description |
|-----|------|-------------|
| `geometry` | object | AREA_COUNT, FAMILIES_PER_AREA, HEXES_PER_FAMILY, SIDES_PER_HEX, TOTAL_FAMILIES, TOTAL_HEXES, TOTAL_SIDES, STEPS_PER_PASS. |
| `hex_unit` | object | count_per_family, total_hexes. |
| `truth_unit` | object | sides_per_hex, total_sides, side_id_range. |
| `borders` | object | area_ring: list of {area_id, area_name, left_area_id, right_area_id}. |
| `path_params` | object | start_area_id, direction, steps. |
| `road_coordinates` | array | List of {step, area_id, global_id, area_name, family_name} in visit order. |
| `border_passings` | object | area_border_passings, family_border_passings (lists of crossing events). |
| `traversal_length` | number | Number of steps in the path. |
| `is_loop` | boolean | True if path is a closed loop (e.g. one full ring). |
| `loopability` | object | formula_ref, requires_activation_data, note; **L_full** (number, optional) when activation data provided via --activation (40_POLICY §11: L_full = G_F[p] / STEPS_PER_PASS). |

---

## 3. `coherence_hints` (object)

| Key | Type | Description |
|-----|------|-------------|
| `current_area_id` | number | Area id (0..11) at the end of the path (current position). |
| `current_area_name` | string | Area name at current position. |
| `suggested_adjacent_areas` | array | [{area_id, area_name, direction: "CCW"|"CW"}, ...] — ring neighbours. |
| `traversal_summary` | string | Short summary, e.g. "one full ring CW" or "N steps from area X (CW|CCW)". |
| `border_passings_count` | object | {area_border_passings: number, family_border_passings: number}. |

---

## 4. `observability` (object, v0.1)

Read-only telemetry; no engine modification. Ref: [projects/hesperia/HESPERIA_OBSERVABILITY_EXTENSION_v0_1.md](../projects/hesperia/HESPERIA_OBSERVABILITY_EXTENSION_v0_1.md).

| Key | Type | Description |
|-----|------|-------------|
| `loopability_band` | string | `"stable"` \| `"transitional"` \| `"unstable"` \| `"unknown"` (from L_full when present). |
| `entropy_metric` | number | unique_areas_visited / steps; report only. |
| `border_passings_count` | object | {area_border_passings: number, family_border_passings: number}. |
| `direction` | number | Path direction (1 = CW, -1 = CCW). |
| `ring_distance_from_start` | number | Distance along ring from start area to current (0..11 area units). |
| `safeguard_events_count` | number | Count of safeguard-relevant events (0 when context_rag run without safeguard). |

---

## 5. `retrieval` (object, optional)

Present only when context_rag.py is invoked with --query, --area_id, or --family_name.

| Key | Type | Description |
|-----|------|-------------|
| `families` | array | List of family items from Chroma layer=hesperia_families. Each item: id, area_id, area_name, family_name, global_id, concept, document (truncated text if any). |
| `chunks` | array | Book chunks from layer=books when retrieval requested; each item: text, source, area_name, family_name, concept (bounding from first family). Use --books-chunks-limit (default 10). |

---

## 6. Error output

On failure (e.g. matrix_run fails and CSV missing), the script may print to stderr a JSON object with key `error` (string). Exit code non-zero.

---

## 7. CLI (reference)

```
context_rag.py [--path] [--start N] [--direction 1|-1] [--steps N] [--query "..."] [--area_id N] [--family_name X] [--chroma] [--data-dir PATH] [--families-limit K]
```

- **--path**: No-op (calculable always included). Kept for compatibility.
- **--start**, **--direction**, **--steps**: Passed to matrix_run (path params).
- **--query**: Optional; triggers retrieval and semantic search over layer=hesperia_families.
- **--area_id**, **--family_name**: Optional filters for retrieval (Chroma where).
- **--chroma**: Use Chroma for matrix data (matrix_run --chroma); fallback to CSV.
- **--data-dir**: Override data dir for CSV (matrix_run).
- **--families-limit**: Max families in retrieval (default 20).

---

**SIGNED: Developer (Gena) | input_context RAG packet schema | 2026-02-17 | governance**
