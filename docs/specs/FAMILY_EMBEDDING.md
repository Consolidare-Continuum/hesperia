# Family Embedding — Two-Scale Geometry

HESPERIA is a **bounded geometric semantic system**, not only a taxonomy. The embedding answers: *where does each family live on the sphere, and how does activation move through that geometry?*

## The hierarchy

- **Icosahedron vertex** → **Area** (12 vertices; 10 operational + 2 meta).
- **Area** → **Local family field** (24 families per area, arranged in a ring-grid).
- **Family** → **Concepts / hexes** (micro nodes).

So: **areas are vertices; families are local lattices; hexes are internal coordinates.** Cross-area traversal happens through **bridge families** only.

## What *not* to do

Do **not** place 240 families directly on the icosahedron. That would:

- Destroy area identity and adjacency meaning.
- Break traversal logic and interpretability.

The family index must remain **nested under area**: `A3_F6` is *family 6 inside Defensive Operations*, not “family 6 somewhere on the sphere”.

## Two scales

| Scale | Represents | Example |
|-------|------------|--------|
| **1 — Global** | Area-to-area movement | A2 ↔ A3 ↔ A4 ↔ A10 (icosahedral edges). |
| **2 — Local** | Within-area movement | Inside A3: splitting ↔ projection ↔ projective identification ↔ idealization/devaluation. |

## Local arrangement (24 families per area)

Each area is a **local semantic cell** with internal coordinates:

| Zone | Count | Role |
|------|--------|------|
| **center** | 1 | Core structural anchor (e.g. splitting in A3, Diada in A2). |
| **inner_ring** | 6 | Most structural families. |
| **middle_ring** | 8 | Relational extensions; derived organizations. |
| **outer_ring** | 9 | Peripheral; specialized or phenomenological. |

Total: 1 + 6 + 8 + 9 = 24 families per area.

## Artifact

- **File:** `spec/family_embedding_tfp.yaml`
- **Pilot areas:** A2, A3, A4, A10. Expand to all 10 in a later step.
- **Content:**
  - Per area: `center`, `inner_ring`, `middle_ring`, `outer_ring` (lists of local family ids F1..F24).
  - **bridges:** list of `{from, to, type}` (e.g. `A2_F5` → `A3_F1`, `activates`). Cross-area propagation uses only these links.

## Cross-area bridges

Examples:

- **A2 ↔ A3:** identity diffusion (A2_F5), splitting (A3_F1), projective identification (A3_F6).
- **A3 ↔ A4:** projection of aggression, persecutory object, rage escalation.
- **A4 ↔ A10:** acting out, safety risk, frame rupture.

## Activation propagation (target model)

1. **Intra-family:** If one concept activates, nearby concepts in the same family get weak activation.
2. **Intra-area:** If a family activates strongly, neighboring families in the same area (ring topology) get medium propagation.
3. **Cross-area:** If a **bridge** family activates strongly, the linked bridge family in the adjacent area receives propagation.

## Loader

- **Module:** `sphere.topology.family_embedding`
- **Functions:** `load_family_embedding_tfp()`, `get_area_zones(embedding, area_id)`, `get_bridges(embedding)`, `get_composite_family_id(area_id, local_family)`.
- **Constants:** `ZONE_KEYS`, `ZONE_COUNTS`.

## Compatibility with KME

This wiring allows KME to compute:

- **Local density** — families inside an area form clusters.
- **Bridge centrality** — which families carry cross-area flow.
- **Conflict paths** — opposing families co-activating across bridges.
- **Hierarchical structure** — center vs peripheral activation.

Cohesion, Conflict Index, Path Variability etc. then describe not only scores but **movement** and **position** (central vs peripheral, integrated vs fragmented).
