# HESPERIA topology storage contract (Chroma)

One-page spec for what must exist in Chroma (or equivalent) to support membership and optional adjacency for v0.3.

## 1. Two topology artifacts

| Artifact | Purpose | Required for |
|----------|---------|--------------|
| **Membership** | side_id → family_id → area_id | Aggregation (§7): F[f], A[a], dominant_family, dominant_area |
| **Adjacency** | side graph W (or edge list with weights) | Base traversal (§5); without it, traversal uses stub W |

If Chroma does not provide adjacency, the run is **membership from Chroma + traversal stub**. Label `topology.adjacency_from_chroma = false` and `topology_source = "membership_chroma"` (mixed).

## 2. Membership docs (required for aggregation)

**Collection**: `hesperia_topology` (recommended) or `knowledge` with strict `layer` filter.

**Document shape** (per side):

| Field | Description |
|-------|-------------|
| `id` | `side:<side_id>` (e.g. `side:0`, `side:12345`) |
| `metadata.layer` | `hesperia_topology` |
| `metadata.type` | `membership` |
| `metadata.side_id` | integer or string per side_id_format |
| `metadata.family_id` | integer |
| `metadata.area_id` | integer |

**Completeness**: Every side_id in the canonical set (0..N-1 or equivalent) must have exactly one membership doc. Incomplete membership → aggregation is partial; document coverage.

## 3. Adjacency docs (optional; for real traversal)

**Option A — per-side adjacency list**

| Field | Description |
|-------|-------------|
| `id` | `adj:<side_id>` |
| `metadata.layer` | `hesperia_topology` |
| `metadata.type` | `adjacency` |
| `metadata.side_id` | integer or string |
| `document` (or JSON blob) | `{"neighbors": [{"to": <side_id>, "w": 0.2}, ...]}` row-stochastic: sum of `w` for same `side_id` = 1 |

**Option B — per-family adjacency (coarser)**
Then traversal is on families, not sides; resolution and metrics must align with that. Pick one representation and stick to it.

## 4. Separation from evidence

- **hesperia_lex**: Dict A / Dict B only (no books).
- **hesperia_topology**: membership + adjacency only (no books, no lex).
- **hesperia_books** (or `knowledge` with `layer=books`): evidence only; retrieval **after** resolution; must not affect metrics (I-Q2).

If using a single collection: **hard filter by `layer` on every query**; CI must assert books retrieval cannot see lex/topology and lex/topology cannot see books.

## 5. Versioning

- Ingest version / dump date of topology source.
- Checksum or version tag of membership and adjacency payloads.
- No automatic updates; changes require version bump and CI pass.
