# SEALING SCAN RULES v1

**Status:** Active  
**Purpose:** Catch accidental architectural reflection. Public tree must pass with zero forbidden hits except in approved internal-only zones.

---

## 1. Forbidden Terms (Public Tree)

Scan for these in **public** runtime packages, public docs, public schemas, and any path that is shipped to operators or API consumers:

| Term / pattern | Reason |
|----------------|--------|
| sphere | Geometry-revealing |
| hex | Geometry-revealing |
| hexagon | Geometry-revealing |
| 3D | Geometry-revealing |
| lattice | Topology-revealing |
| side_id | Internal coordinate |
| adjacency path | Internal structure |
| propagation path | Internal method |
| layer1, layer2, … layer9, layer_1 … layer_9 | Revealing pipeline |
| area11, area12, area 11, area 12 | Reserved area leak |
| 12 areas | Internal count |
| reserved families | Internal reserve |
| vector axis | Spatial semantics |
| 288 families | Internal count |

---

## 2. Approved Internal-Only Zones

The following paths are **excluded** from the public scan (they may contain internal terms):

- `docs/internal/`
- `core/layers/` (implementation)
- `core/math/` (implementation)
- `core/domain/` (bridge, etc.)
- `core/topology/` (invariant_catalog, reserve_loader implementation)
- `legacy/`
- `tests/` (may reference internal names for testing)
- Any file or directory marked `INTERNAL_ONLY` or under `internal/`

---

## 3. Scan Tool

Run **tools/sealing_scan.py** to scan the repository. It reports:

- Forbidden term hits with file and line.
- Hits inside approved internal zones (informational only; do not fail).
- Hits outside approved zones → **fail** (must fix or move to internal).

---

## 4. Acceptance Criterion

Public tree passes scan with **zero** forbidden hits outside approved internal-only zones.
