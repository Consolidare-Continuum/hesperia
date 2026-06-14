# Hesperia formalization — Geodesic closed sphere and Interior Point of World View

**Document ID:** `22_SPEC__Geodesic_Sphere_and_Interior_Point_of_World_View_v0_1`  
**Status:** FORMALIZATION (brain draft — **no implementation tasks**).  
**Plane:** Geometry + sphere embedding + future observability.  
**Brain source (Grace PoWV):** [SPEC-GRACE-HESPERIA-INTERIOR-POINT-OF-WORLD-VIEW.md](SPEC-GRACE-HESPERIA-INTERIOR-POINT-OF-WORLD-VIEW.md)  
**Promotion target (Hesperia dev repo):** `docs/specs/22_SPEC__Geodesic_Sphere_and_Interior_Point_of_World_View_v0_1.md` on `igareosh/hesperia` after operator review.  
**Policy:** [governance/ETHAN-POLICY-HESPERIA-BRAIN-DEV-LINK.md](../../governance/ETHAN-POLICY-HESPERIA-BRAIN-DEV-LINK.md) — brain holds draft; product canonical copy lives on dev.

**Added:** 2026-05-24. **Triage:** Grace. **No `active.md` rows** until operator approves implementation wave.

---

## 0. Document control

| Field | Value |
|-------|--------|
| **Version** | `0.1.0` |
| **Replaces** | — (greenfield formalization) |
| **Companion geometry** | `20_GEOMETRY__formalized_structure` (product), `40_POLICY__Loopability_and_traversal` (product) |
| **Entities touched (names only)** | `HexSphere`, `Region`, traversal engines, guard subsystem, `sphere/` pipeline, optional `hesperia.geometry` / `sphere.embedding` (future package paths) |

---

## 1. Scope

This specification **formalizes in Hesperia product terms**:

1. **Semantic topology** — unchanged storage and IDs: **12 Areas × 24 Families × 250 HexCells × 6 TruthUnits**.  
2. **Geodesic closed sphere (GCS)** — operator-canonical **perfect soccer-ball-class** surface: **72,240** hexagonal faces + **12** pentagonal faces, frequency **ν = 85**.  
3. **Dual-plane embedding** — semantic coordinates remain authoritative for content; geodesic coordinates are authoritative for **spherical distance**, **PoWV**, and **symmetric spacing** on `HexSphere`.  
4. **`InteriorPointOfWorldView` (IPoW)** — interior stance in the **body ellipsoid** volume; default **`PointZero`**.  
5. **Registry fields** — names for future bundles/schemas (§10); **not implemented** in this document revision.

**Out of scope v0.1:** Code, JSON Schema files, UI, Chroma ingest changes, change to `AREA_IDS` cardinality, clinical claims.

---

## 2. Normative references

| Ref | Hesperia / brain |
|-----|------------------|
| Master invariant grid | `10_MASTER_SPEC__HESPERIA`, `20_GEOMETRY__formalized_structure` |
| Traversal / loopability | `40_POLICY__Loopability_and_traversal` |
| Matrix / Chroma | `13_SPEC__Indexing_and_Coordinates`, layer `hesperia_families` |
| Brain PoWV narrative | [SPEC-GRACE-HESPERIA-INTERIOR-POINT-OF-WORLD-VIEW.md](SPEC-GRACE-HESPERIA-INTERIOR-POINT-OF-WORLD-VIEW.md) |
| Compressed world view | [BOOKS-LAYER-AND-MATRIX-COMPRESSED-WORLD-VIEW.md](../../governance/BOOKS-LAYER-AND-MATRIX-COMPRESSED-WORLD-VIEW.md) |
| Surface runner | Apple hesperides — [TASK-GENA-APPLE-HESPERIDES-PATH-SCRIPTS.md](../../governance/TASK-GENA-APPLE-HESPERIDES-PATH-SCRIPTS.md) |
| Propagation adjacency | `propagation_trace`, `families_propagated`, `areas_propagated` — `hesperia/nlp/tfp_activation.py` |
| GTP / hex orientation | [HESPERIA-FORMALIZATION-GENERAL-THOUGHT-PROPAGATION-v0_1.md](HESPERIA-FORMALIZATION-GENERAL-THOUGHT-PROPAGATION-v0_1.md) (`23_SPEC__`) — depends on this doc; as above so below |

---

## 3. Definitions (Hesperia terms)

| Term | Definition |
|------|------------|
| **Area** | One of **12** ring nodes; `area_id ∈ {0,…,11}`; name from `AreaName` / `AREA_IDS`. |
| **Family** | One of **24** elevation slots per Area; **`global_id`** unique over 288 rows; `FamilyName`. |
| **HexCell** | One of **250** semantic hex units per Family; **`hex_index ∈ {0,…,249}`** — **semantic invariant**. |
| **TruthUnit** | One of **6** statement sides per HexCell; **`side_id ∈ {0,…,5}`**; authoritative wording slot. |
| **SemanticPlane** | Product storage and engine IDs — **72,000** HexCells, **432,000** TruthUnits. |
| **GeodesicPlane** | Embedding overlay for spherical geometry — **72,240** hex slots + **12** `PentagonPole` sites on **∂Ω**. |
| **∂Ω (surface)** | Boundary of `HexSphere` / body ellipsoid carrying matrix + GCS anchors. |
| **Ω (volume)** | Interior of body ellipsoid; hosts **IPoW**. |
| **HexSphere** | Existing Hesperia entity: loopable semantic surface (hex sides → statements; matrix on ∂Ω). |
| **GeodesicClosedSphere (GCS)** | Formal name for soccer-ball-class mesh: **GCS_ν85** = 72,240 hex + 12 pent. |
| **PentagonPole** | One of **12** non-hex face sites required for closed spherical topology. |
| **InteriorPointOfWorldView (IPoW)** | Calculable interior vector **`powv_position`** + distance fields to anchors on ∂Ω. |
| **PointZero** | Mandatory default IPoW state: center of Ω, unbiased distances. |
| **SurfaceEventBatch** | Traversal step + border passings + guard counts + shadow summary — drives IPoW motion. |
| **Apple** | On-surface virtual runner; path on ∂Ω; does **not** replace IPoW. |

---

## 4. Structural invariants (normative)

These **SHALL NOT** change without operator ADR and version bump.

| ID | Invariant | Value |
|----|-----------|------:|
| **INV-AREA-COUNT** | `len(AREA_IDS)` | **12** |
| **INV-FAM-PER-AREA** | families per area | **24** |
| **INV-FAM-TOTAL** | total families | **288** |
| **INV-HEX-PER-FAM-SEM** | semantic HexCells per Family | **250** |
| **INV-SIDES-PER-HEX** | TruthUnits per HexCell | **6** |
| **INV-HEX-TOTAL-SEM** | semantic hex total | **72,000** |
| **INV-SIDES-TOTAL-SEM** | semantic truth total | **432,000** |
| **INV-PENT-GCS** | PentagonPole count on GCS | **12** |
| **INV-HEX-TOTAL-GCS** | geodesic hex slots | **72,240** |
| **INV-GCS-NU** | geodesic frequency | **85** |
| **INV-FACES-TOTAL-GCS** | hex + pent faces | **72,252** |
| **INV-SIDES-TOTAL-GCS** | TruthUnits if keyed to GCS hex | **433,440** |

**Identity (semantic):**

```text
INV-HEX-TOTAL-SEM = INV-AREA-COUNT × INV-FAM-PER-AREA × INV-HEX-PER-FAM-SEM
                  = 12 × 24 × 250 = 72,000
```

**Identity (GCS hex count):**

```text
INV-HEX-TOTAL-GCS = 10 × INV-GCS-NU² − 10
                  = 10 × 85² − 10 = 72,240
```

**Delta (embedding only until ADR):**

```text
Δ_HEX = INV-HEX-TOTAL-GCS − INV-HEX-TOTAL-SEM = 240
Δ_SIDES = Δ_HEX × INV-SIDES-PER-HEX = 1,440
```

---

## 5. GeodesicClosedSphere (GCS) — formal object

### 5.1 Class

**`GeodesicClosedSphere`** — immutable topology descriptor bound to **`HexSphere`** at embed time.

| Attribute | Type | Value / rule |
|-----------|------|----------------|
| `gcs_id` | string | `"GCS_NU85_v0_1"` |
| `nu` | int | **85** |
| `hex_face_count` | int | **72,240** |
| `pentagon_pole_count` | int | **12** |
| `total_face_count` | int | **72,252** |
| `truth_unit_count_geodesic` | int | **433,440** |
| `scale_sigma` | float | **1.0033333333** (= 72240/72000) |

### 5.2 Meaning in Hesperia language

- **GCS** is the **perfect closed sphere** used for: anchor directions on ∂Ω, IPoW chord distances, loopable soccer-class topology.  
- **SemanticPlane** remains the **authority for content**, dictionary keys, and sealed pipeline IDs.  
- **GCS** is the **authority for spherical spacing** and IPoW math until a future ADR merges planes.

### 5.3 PentagonPole

| Attribute | Rule |
|-----------|------|
| `pentagon_id` | **0..11** |
| `extra_hex_budget` | **20** per pole (`240 / 12`) |
| Role | Closes mesh; anchors wedge for **+240** hex budget |

---

## 6. Semantic ↔ geodesic mapping (12 × 24)

### 6.1 Mean densities (decimal — calculable)

| Symbol | Hesperia field (proposed) | Value |
|--------|---------------------------|------:|
| **σ** | `gcs_scale_sigma` | 1.0033333333 |
| **h̄** | `gcs_mean_hex_per_family` | 250.8333333333 |
| **ȧ** | `gcs_mean_hex_per_area` | 6020.0 |
| **δ** | `gcs_hex_fractional_delta_per_family` | 0.8333333333 |
| **ε_area** | `gcs_extra_hex_per_area` | 20 |

### 6.2 Integer family slot rule (exact)

For each **`area_id`** and **`family_index_in_area`**:

| Condition | `gcs_hex_slot_count` | `semantic_hex_index` range |
|-----------|----------------------:|---------------------------|
| Family in **250-slot** set (48 total, 4 per area) | **250** | **0..249** only |
| All other families (240 total) | **251** | **0..249** + **`geodesic_extra_index = 250`** |

**Verification:**

```text
240 × 251 + 48 × 250 = 72,240 = INV-HEX-TOTAL-GCS
```

**Default 250-slot selection (candidate — freeze in anchor map):**

```text
family_index_in_area % 6 == 0   → 4 families per area × 12 areas = 48
```

Implementations **MAY** instead bind 250-slot families to the four Family sites nearest each **PentagonPole** wedge if anchor map demands — **one rule per `gcs_id`**, documented in `anchor_map_v1`.

### 6.3 Per-family spacing factor (decimal)

```text
if gcs_hex_slot_count == 250:
  spacing_factor = 250 / gcs_mean_hex_per_family   ≈ 0.996688
else:
  spacing_factor = 251 / gcs_mean_hex_per_family   ≈ 1.000663
```

---

## 7. InteriorPointOfWorldView (IPoW)

### 7.1 Entity

**`InteriorPointOfWorldView`** — runtime-calculable state, **read-only** w.r.t. lexical assets (HC-10 pattern).

| Field (proposed) | Type | Description |
|------------------|------|-------------|
| `powv_position` | `Vec3` | **(x, y, z)** in body frame; **‖powv_position‖ ≤ 1** on unit ball |
| `powv_step` | int | Iteration / traversal step index |
| `powv_point_zero` | bool | **true** iff at **PointZero** |
| `powv_update_mode` | enum | `point_zero` \| `surface_pull` \| `direct_set` \| `aggregate_invert` |
| `powv_gcs_id` | string | e.g. `"GCS_NU85_v0_1"` |
| `powv_distances` | struct | Tiered: areas, families, hexes (GCS), pentagons, concepts |
| `powv_barycentric_areas` | float[12] | Optional fast ring view |

### 7.2 PointZero (normative default)

When IPoW is **created** (new session, new iteration, reset):

| Rule | Value |
|------|--------|
| `powv_position` | **(0, 0, 0)** |
| `powv_point_zero` | **true** |
| `powv_update_mode` | **`point_zero`** |
| Chord distance to each unit-sphere anchor | **1.0** (symmetric embed) |
| `powv_barycentric_areas[i]` | **1/12** |

IPoW **SHALL NOT** drift until first **`SurfaceEventBatch`** or **`direct_set`**.

### 7.3 Distance tiers (on GCS ∂Ω)

For anchor **a** with unit direction **s_a** from center:

```text
powv_distance[a] = || powv_position − s_a ||     # default: chord
powv_distance_relative[a] = powv_distance[a] / (sum_b powv_distance[b] + ε)
```

**Anchor tiers:** `AreaAnchor` (12), `FamilyAnchor` (288), `HexAnchor` (72,240 GCS), `PentagonPole` (12), `ConceptAnchor` (dynamic).

---

## 8. Coupling to Hesperia execution planes

| Plane / subsystem | Role w.r.t. GCS + IPoW |
|-------------------|-------------------------|
| **Lexical → concept → family → area** | Unchanged; feeds activations only |
| **HexSphere / structural (`sphere/`)** | Hosts ∂Ω embedding; future `embed_gcs_on_hex_sphere()` |
| **Traversal engine** | Emits **`SurfaceEventBatch`** (road coordinates, border passings) |
| **Guards (Sigma, Gamma)** | Counted on surface; may block IPoW pull |
| **Shadow (`HESPERIA_K_SHADOW_PERTURB`)** | Bounded perturbation on `powv_position` or distances |
| **`propagation_trace`** | Graph propagation — **MAY** inform anchor weights; **MUST NOT** duplicate IPoW semantics |
| **Apple hesperides** | Surface path only; IPoW **reads** path events |
| **`matrix_run` / context RAG** | Supplies geometry constants + path params |

**Normative separation:**

```text
Apple.path  ⊆  ∂Ω     (surface)
IPoW        ∈  Ω      (volume)
GCS         →  ∂Ω     (embedding)
Semantic    →  IDs    (content)
```

---

## 9. Proposed registry block — `geodesic_sphere` + `interior_point_of_world_view`

*For future `schemas/` and iteration bundles — **not wired in v0.1**.*

### 9.1 `geodesic_sphere` (static descriptor per run)

```json
{
  "gcs_id": "GCS_NU85_v0_1",
  "nu": 85,
  "hex_face_count": 72240,
  "pentagon_pole_count": 12,
  "total_face_count": 72252,
  "semantic_hex_count": 72000,
  "delta_hex": 240,
  "truth_unit_count_geodesic": 433440,
  "truth_unit_count_semantic": 432000,
  "delta_sides": 1440,
  "gcs_scale_sigma": 1.0033333333,
  "gcs_mean_hex_per_family": 250.8333333333,
  "gcs_mean_hex_per_area": 6020,
  "families_gcs_251": 240,
  "families_gcs_250": 48,
  "extra_hex_per_pentagon_pole": 20
}
```

### 9.2 `interior_point_of_world_view` (runtime)

Align with brain artifact `interior_point_of_world_view_v1` — [SPEC-GRACE §5.1](SPEC-GRACE-HESPERIA-INTERIOR-POINT-OF-WORLD-VIEW.md).

Hesperia export path (proposed): `modules["sphere.ipow.v0_1"]` or `meta.interior_point_of_world_view` on iteration scope.

---

## 10. Comparison to classic soccer ball (informative)

| Object | Hex faces | Pent faces |
|--------|----------:|-----------:|
| Truncated icosahedron (FIFA class) | 20 | 12 |
| **Hesperia GCS_NU85** | **72,240** | **12** |
| **Hesperia SemanticPlane** | 72,000 (product) | — |

Same topology **class**; GCS is high-frequency instance aligned to semantic inventory.

---

## 11. ADR gates (before implementation)

| Change | Requires |
|--------|----------|
| Renumber semantic HexCells / Families / Areas | Operator ADR + schema version |
| Store 251 semantic rows per family in DB | ADR + migration |
| Merge SemanticPlane and GeodesicPlane counts | ADR |
| Clinical interpretation of IPoW distances | Explicit non-claim policy (§7) + Sophia review |

Until ADR: **+240** hex **SHALL** appear only as embedding (`geodesic_extra_index`, anchor map, or parallel GCS index).

---

## 12. Promotion checklist (dev repo — when tasked)

1. Copy this file to `igareosh/hesperia` → `docs/specs/22_SPEC__Geodesic_Sphere_and_Interior_Point_of_World_View_v0_1.md`.  
2. Cross-link from `docs/DOC_INDEX.md` and `20_GEOMETRY__formalized_structure` §addendum.  
3. Add constants to geometry registry / `VERSION.yaml` pins if used.  
4. Implement `anchor_map_v1` + IPoW only after operator approves implementation wave (brain `IPoV-*` rows).

---

## 13. Traceability

| Brain (Grace) | Hesperia formal (this doc) |
|---------------|----------------------------|
| PoWV | `InteriorPointOfWorldView` (IPoW) |
| Point zero | `PointZero` / `powv_point_zero` |
| 72,240 hex sphere | `GeodesicClosedSphere` / `GCS_NU85_v0_1` |
| 12×24×250 | `SemanticPlane` / structural invariants |
| σ, h̄, 240/48 split | §6 `gcs_*` fields |
| `interior_point_of_world_view_v1` JSON | §9.2 |

---

**SIGNED: Product/Triage (Grace) | Hesperia formalization GCS + IPoW v0.1 | 2026-05-24 | brain draft — no tasks**
