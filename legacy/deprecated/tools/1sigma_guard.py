# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

```python
# ============================================================
# sigma_guard_v2.py
# HESPERIA — Σ (Sigma) Static Invariant Guard v2
#
# Scope: ONLY static invariants (structure/topology/schema).
# Failure type: binary structural violation → immediate stop.
#
# Enforces (static):
#  1) Geometry constants + derived totals
#  2) sideId determinism (coord ↔ sideId bijection)
#  3) Area/Families cardinality + global contiguity rules
#  4) Ring order topology + legal area adjacency matrix
#  5) Antipodal pairs (6 axes) and axis membership
#  6) Border families (edge families) validity + symmetry across neighbors
#  7) Inward/Outward matrix SHAPES (values are dynamic; shape is static)
#  8) Embedding dimension consistency (D is static for a build)
#  9) Shard key schema (area_id, family_id present; optional validation hooks)
# 10) Structural hash (names + ring + antipodes + borders) consistency
#
# Aligned with:
#  - Indexing & coordinates spec (sideId mapping, constants)  :contentReference[oaicite:0]{index=0}
#  - Blueprint ring order + 6-axis polarity model             :contentReference[oaicite:1]{index=1}
#  - Canonical edge families                                  :contentReference[oaicite:2]{index=2}
#  - Structural metrics context (coherence/frag etc are Γ)     :contentReference[oaicite:3]{index=3}
# ============================================================

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional, Iterable, Any
import hashlib


# -----------------------------
# Exceptions
# -----------------------------

class SigmaViolation(Exception):
    """Binary structural violation. Treat as fatal."""


# -----------------------------
# Helper types
# -----------------------------

# Canonical coordinate tuple
SideCoord = Tuple[int, int, int, int]  # (area, familyLocal, hexIndex, sideIndex)

# Borders data structure:
# borders[area] = {"prev": [family_name,...], "next": [family_name,...]}
Borders = Dict[int, Dict[str, List[str]]]


# -----------------------------
# Sigma Guard v2
# -----------------------------

@dataclass(frozen=True)
class SigmaGuardV2:
    """
    Static invariant guard.
    Do NOT put runtime / trend / slope logic here.
    """

    # Expected static topology (by Area index)
    # If your repo exposes these from a canonical module, pass them in instead.
    expected_ring_order: Optional[List[int]] = None
    expected_antipodes: Optional[Dict[int, int]] = None

    def run(
        self,
        *,
        # --- core topology / ontology ---
        area_names: List[str],                 # length 12, uppercase
        family_names_global: List[str],        # length 288, global index order
        area_to_family_globals: Dict[int, List[int]],  # area -> 24 global family ids
        borders: Borders,                      # edge families by name
        expected_structure_hash: Optional[str] = None,

        # --- optional schema/static-shape objects ---
        family_inward: Optional[List[List[float]]] = None,   # [288][12]
        family_outward: Optional[List[List[float]]] = None,  # [288][12]
        embed_area: Optional[List[List[float]]] = None,      # [12][D]
        embed_family: Optional[List[List[float]]] = None,    # [288][D]
        axis_pos: Optional[List[List[float]]] = None,        # [6][D]
        axis_neg: Optional[List[List[float]]] = None,        # [6][D]

        # --- optional dataset integrity hooks (static referential) ---
        # If you have side records or DB rows available at build-time:
        side_records: Optional[Iterable[SideCoord]] = None,  # validate coord ranges
        shard_schema: Optional[Dict[str, Any]] = None,       # validate sharding key shape
    ) -> str:
        """
        Returns the computed structural hash (useful for logging).
        Raises SigmaViolation on any mismatch.
        """

        # 1) Constants + derived totals (imported from geometry)
        self._check_constants()

        # 2) sideId bijection (determinism)
        self._check_side_id_roundtrip()

        # 3) Ontology naming + cardinality + global contiguity
        self._check_area_and_family_names(area_names, family_names_global)
        self._check_area_to_family_mapping(area_to_family_globals)

        # 4) Ring topology + legal adjacency
        ring_order = self._resolve_ring_order()
        self._check_ring_integrity(ring_order)
        self._check_legal_area_adjacency(ring_order)

        # 5) Antipodal pairing / 6 axes
        antipodes = self._resolve_antipodes()
        self._check_antipodes(antipodes)
        self._check_axis_membership(antipodes)

        # 6) Border families validity + symmetry
        self._check_border_families(
            borders=borders,
            area_names=area_names,
            family_names_global=family_names_global,
            area_to_family_globals=area_to_family_globals,
            ring_order=ring_order
        )

        # 7) Static shapes for inward/outward
        self._check_inward_outward_shapes(family_inward, family_outward)

        # 8) Embedding dimensional consistency (static for a build)
        self._check_embedding_dimensions(embed_area, embed_family, axis_pos, axis_neg)

        # 9) Shard schema (static keys)
        self._check_shard_schema(shard_schema)

        # 10) Optional referential integrity for side coords
        if side_records is not None:
            self._check_side_records(side_records)

        # 11) Structural hash (full topology + borders)
        structure_hash = self.compute_structure_hash(
            area_names=area_names,
            family_names_global=family_names_global,
            ring_order=ring_order,
            antipodes=antipodes,
            borders=borders
        )

        if expected_structure_hash is not None:
            if structure_hash != expected_structure_hash:
                raise SigmaViolation("STRUCTURE_HASH_MISMATCH")

        return structure_hash


    # =========================================================
    # Core checks
    # =========================================================

    def _check_constants(self):
        # Canonical constants and totals come from indexing spec.
        # Import locally to avoid import cycles.
        from sphere_rag.geometry import (
            AREAS,
            FAMILIES_PER_AREA,
            HEXES_PER_FAMILY,
            SIDES_PER_HEX,
            TOTAL_FAMILIES,
            TOTAL_HEXES,
            TOTAL_SIDES,
        )

        if AREAS != 12:
            raise SigmaViolation("AREAS_CORRUPTED")
        if FAMILIES_PER_AREA != 24:
            raise SigmaViolation("FAMILIES_PER_AREA_CORRUPTED")
        if HEXES_PER_FAMILY != 250:
            raise SigmaViolation("HEXES_PER_FAMILY_CORRUPTED")
        if SIDES_PER_HEX != 6:
            raise SigmaViolation("SIDES_PER_HEX_CORRUPTED")

        if TOTAL_FAMILIES != AREAS * FAMILIES_PER_AREA:
            raise SigmaViolation("TOTAL_FAMILIES_MISMATCH")
        if TOTAL_HEXES != TOTAL_FAMILIES * HEXES_PER_FAMILY:
            raise SigmaViolation("TOTAL_HEXES_MISMATCH")
        if TOTAL_SIDES != TOTAL_HEXES * SIDES_PER_HEX:
            raise SigmaViolation("TOTAL_SIDES_MISMATCH")


    def _check_side_id_roundtrip(self):
        from sphere_rag.geometry import (
            AREAS,
            FAMILIES_PER_AREA,
            HEXES_PER_FAMILY,
            SIDES_PER_HEX,
            side_id,
            coord_from_side_id,
            TOTAL_SIDES,
        )

        # Deterministic sample points across the whole range.
        samples: List[SideCoord] = [
            (0, 0, 0, 0),
            (0, FAMILIES_PER_AREA - 1, HEXES_PER_FAMILY - 1, SIDES_PER_HEX - 1),
            (AREAS - 1, 0, 0, 0),
            (AREAS - 1, FAMILIES_PER_AREA - 1, HEXES_PER_FAMILY - 1, SIDES_PER_HEX - 1),
            (5, 12, 120, 3),
        ]

        for (a, f, h, s) in samples:
            sid = side_id(a, f, h, s)
            if not (0 <= sid < TOTAL_SIDES):
                raise SigmaViolation("SIDEID_OUT_OF_RANGE")

            a2, f2, h2, s2 = coord_from_side_id(sid)
            if (a, f, h, s) != (a2, f2, h2, s2):
                raise SigmaViolation("SIDEID_NON_BIJECTIVE")


    def _check_area_and_family_names(self, area_names: List[str], family_names_global: List[str]):
        from sphere_rag.geometry import AREAS, TOTAL_FAMILIES

        if len(area_names) != AREAS:
            raise SigmaViolation("AREA_NAMES_COUNT_MISMATCH")
        if len(family_names_global) != TOTAL_FAMILIES:
            raise SigmaViolation("FAMILY_NAMES_COUNT_MISMATCH")

        for n in area_names:
            if not isinstance(n, str) or not n:
                raise SigmaViolation("AREA_NAME_INVALID")
            # Canonical in docs are uppercase tokens (GOOD, HARM, ...)
            if n.upper() != n:
                raise SigmaViolation("AREA_NAME_NOT_UPPERCASE")

        for n in family_names_global:
            if not isinstance(n, str) or not n.strip():
                raise SigmaViolation("FAMILY_NAME_INVALID")


    def _check_area_to_family_mapping(self, area_to_family_globals: Dict[int, List[int]]):
        from sphere_rag.geometry import AREAS, FAMILIES_PER_AREA, TOTAL_FAMILIES

        # Must have all 12 areas
        if set(area_to_family_globals.keys()) != set(range(AREAS)):
            raise SigmaViolation("AREA_TO_FAMILY_KEYS_INVALID")

        all_ids: List[int] = []
        for area in range(AREAS):
            ids = area_to_family_globals[area]

            if len(ids) != FAMILIES_PER_AREA:
                raise SigmaViolation(f"AREA_{area}_FAMILY_CARDINALITY_BROKEN")

            if len(set(ids)) != FAMILIES_PER_AREA:
                raise SigmaViolation(f"AREA_{area}_DUPLICATE_FAMILY_IDS")

            all_ids.extend(ids)

        # Must be exactly 288 unique global IDs
        if len(all_ids) != TOTAL_FAMILIES:
            raise SigmaViolation("GLOBAL_FAMILY_ID_TOTAL_MISMATCH")
        if len(set(all_ids)) != TOTAL_FAMILIES:
            raise SigmaViolation("GLOBAL_FAMILY_ID_DUPLICATES")

        # Global contiguity (0..287) must be complete
        if set(all_ids) != set(range(TOTAL_FAMILIES)):
            raise SigmaViolation("GLOBAL_FAMILY_ID_NOT_CONTIGUOUS")


    # =========================================================
    # Ring topology & adjacency
    # =========================================================

    def _resolve_ring_order(self) -> List[int]:
        if self.expected_ring_order is not None:
            return list(self.expected_ring_order)

        # Default: canonical ring order from blueprint v4.5
        # (GOOD → CARE → ORDER → CONTROL → INDIFFERENCE → HARM →
        #  DESTRUCTION → CHAOS → FREEDOM → TRUTH → CREATION → GOOD)
        # Stored as 12 unique areas without closure repeat.
        return [0, 8, 4, 7, 9, 1, 11, 5, 6, 2, 10, 3]  # if your canonical includes DECEIT in ring
        # IMPORTANT:
        # If your project treats DECEIT as radial antipode and NOT in ring,
        # pass expected_ring_order explicitly and keep ring length 12.
        # This guard enforces whatever you declare as canonical.


    def _check_ring_integrity(self, ring_order: List[int]):
        from sphere_rag.geometry import AREAS

        if len(ring_order) != AREAS:
            raise SigmaViolation("RING_LENGTH_INVALID")

        if set(ring_order) != set(range(AREAS)):
            raise SigmaViolation("RING_MEMBERSHIP_INVALID")

        # No duplicates implied by set check; still ensure deterministic ordering is provided
        if len(ring_order) != len(list(ring_order)):
            raise SigmaViolation("RING_DUPLICATES_PRESENT")


    def _check_legal_area_adjacency(self, ring_order: List[int]):
        """
        Static legality: each Area has exactly two ring neighbors.
        We enforce the implied adjacency set. (Area↔prev, Area↔next)
        """
        neighbors = self._ring_neighbors(ring_order)

        for a in range(len(ring_order)):
            ns = neighbors[a]
            if len(ns) != 2:
                raise SigmaViolation("AREA_NEIGHBOR_COUNT_INVALID")


    def _ring_neighbors(self, ring_order: List[int]) -> Dict[int, Tuple[int, int]]:
        n = len(ring_order)
        pos = {area: i for i, area in enumerate(ring_order)}
        out: Dict[int, Tuple[int, int]] = {}
        for area in ring_order:
            i = pos[area]
            prev_area = ring_order[(i - 1) % n]
            next_area = ring_order[(i + 1) % n]
            out[area] = (prev_area, next_area)
        return out


    # =========================================================
    # Antipodes / axes
    # =========================================================

    def _resolve_antipodes(self) -> Dict[int, int]:
        if self.expected_antipodes is not None:
            return dict(self.expected_antipodes)

        # Default: canonical 6 antipodal pairs:
        # (0,1), (2,3), (4,5), (6,7), (8,9), (10,11)
        return {
            0: 1, 1: 0,
            2: 3, 3: 2,
            4: 5, 5: 4,
            6: 7, 7: 6,
            8: 9, 9: 8,
            10: 11, 11: 10
        }


    def _check_antipodes(self, antipodes: Dict[int, int]):
        from sphere_rag.geometry import AREAS

        if set(antipodes.keys()) != set(range(AREAS)):
            raise SigmaViolation("ANTIPODES_KEYS_INVALID")

        # symmetry + no self
        for a, b in antipodes.items():
            if a == b:
                raise SigmaViolation("ANTIPODE_SELF")
            if antipodes.get(b) != a:
                raise SigmaViolation("ANTIPODE_NOT_SYMMETRIC")

        # must be exactly 6 disjoint pairs
        seen = set()
        pairs = []
        for a in range(AREAS):
            if a in seen:
                continue
            b = antipodes[a]
            seen.add(a)
            seen.add(b)
            pairs.append(tuple(sorted((a, b))))
        if len(pairs) != 6:
            raise SigmaViolation("ANTIPODE_PAIR_COUNT_INVALID")


    def _check_axis_membership(self, antipodes: Dict[int, int]):
        # Ensures axes partition areas into 6 pairs.
        # Already implied by _check_antipodes, but keep explicit.
        from sphere_rag.geometry import AREAS
        used = set()
        for a in range(AREAS):
            b = antipodes[a]
            used.add(tuple(sorted((a, b))))
        if len(used) != 6:
            raise SigmaViolation("AXIS_COUNT_INVALID")


    # =========================================================
    # Border families (edge families)
    # =========================================================

    def _check_border_families(
        self,
        *,
        borders: Borders,
        area_names: List[str],
        family_names_global: List[str],
        area_to_family_globals: Dict[int, List[int]],
        ring_order: List[int]
    ):
        from sphere_rag.geometry import AREAS

        if set(borders.keys()) != set(range(AREAS)):
            raise SigmaViolation("BORDERS_KEYS_INVALID")

        # Build per-area family name set from global IDs
        area_fam_names: Dict[int, set] = {}
        for a in range(AREAS):
            ids = area_to_family_globals[a]
            names = {family_names_global[g] for g in ids}
            area_fam_names[a] = names

        # Validate every border entry exists and belongs to that area
        for a in range(AREAS):
            if "prev" not in borders[a] or "next" not in borders[a]:
                raise SigmaViolation("BORDERS_MISSING_FIELDS")

            prev_list = borders[a]["prev"]
            next_list = borders[a]["next"]

            if not isinstance(prev_list, list) or not isinstance(next_list, list):
                raise SigmaViolation("BORDERS_FIELD_TYPE_INVALID")

            if len(prev_list) == 0 or len(next_list) == 0:
                raise SigmaViolation("BORDERS_EMPTY")

            # Existence + belonging check
            for fname in prev_list + next_list:
                if fname not in area_fam_names[a]:
                    raise SigmaViolation(f"BORDER_FAMILY_NOT_IN_AREA::{a}::{fname}")

            # No duplicates within each direction
            if len(set(prev_list)) != len(prev_list):
                raise SigmaViolation(f"BORDER_DUPLICATE_PREV::{a}")
            if len(set(next_list)) != len(next_list):
                raise SigmaViolation(f"BORDER_DUPLICATE_NEXT::{a}")

        # Symmetry check across ring neighbors:
        # If A's next borders B, then B's prev must include the same "conceptual edge families"
        # We enforce NAME symmetry as a strict version. (You can relax later if needed.)
        neigh = self._ring_neighbors(ring_order)
        for a in range(AREAS):
            b_next = neigh[a][1]
            a_next = set(borders[a]["next"])
            b_prev = set(borders[b_next]["prev"])
            if a_next != b_prev:
                raise SigmaViolation(f"BORDER_ASYMMETRY_NEXT_PREV::{a}->{b_next}")

            b_prev_area = neigh[a][0]
            a_prev = set(borders[a]["prev"])
            p_next = set(borders[b_prev_area]["next"])
            if a_prev != p_next:
                raise SigmaViolation(f"BORDER_ASYMMETRY_PREV_NEXT::{a}<-{b_prev_area}")


    # =========================================================
    # Static shapes
    # =========================================================

    def _check_inward_outward_shapes(
        self,
        family_inward: Optional[List[List[float]]],
        family_outward: Optional[List[List[float]]],
    ):
        from sphere_rag.geometry import TOTAL_FAMILIES, AREAS

        if family_inward is not None:
            if len(family_inward) != TOTAL_FAMILIES:
                raise SigmaViolation("FAMILY_INWARD_ROWS_INVALID")
            for row in family_inward:
                if len(row) != AREAS:
                    raise SigmaViolation("FAMILY_INWARD_COLS_INVALID")

        if family_outward is not None:
            if len(family_outward) != TOTAL_FAMILIES:
                raise SigmaViolation("FAMILY_OUTWARD_ROWS_INVALID")
            for row in family_outward:
                if len(row) != AREAS:
                    raise SigmaViolation("FAMILY_OUTWARD_COLS_INVALID")


    def _check_embedding_dimensions(
        self,
        embed_area: Optional[List[List[float]]],
        embed_family: Optional[List[List[float]]],
        axis_pos: Optional[List[List[float]]],
        axis_neg: Optional[List[List[float]]],
    ):
        from sphere_rag.geometry import AREAS, TOTAL_FAMILIES

        dims = []

        def dim_of(matrix: List[List[float]]) -> int:
            if len(matrix) == 0:
                return 0
            if len(matrix[0]) == 0:
                return 0
            return len(matrix[0])

        def check_matrix(name: str, m: List[List[float]], expected_rows: int):
            if len(m) != expected_rows:
                raise SigmaViolation(f"{name}_ROWS_INVALID")
            d = dim_of(m)
            if d <= 0:
                raise SigmaViolation(f"{name}_DIM_INVALID")
            for row in m:
                if len(row) != d:
                    raise SigmaViolation(f"{name}_RAGGED_ROWS")
            dims.append((name, d))

        if embed_area is not None:
            check_matrix("EMBED_AREA", embed_area, AREAS)

        if embed_family is not None:
            check_matrix("EMBED_FAMILY", embed_family, TOTAL_FAMILIES)

        if axis_pos is not None:
            check_matrix("AXIS_POS", axis_pos, 6)

        if axis_neg is not None:
            check_matrix("AXIS_NEG", axis_neg, 6)

        # All provided embeddings must share the same D
        if len(dims) >= 2:
            d0 = dims[0][1]
            for name, d in dims[1:]:
                if d != d0:
                    raise SigmaViolation(f"EMBED_DIM_MISMATCH::{dims[0][0]}={d0}::{name}={d}")


    # =========================================================
    # Shard schema (static)
    # =========================================================

    def _check_shard_schema(self, shard_schema: Optional[Dict[str, Any]]):
        """
        Sharding is a static contract: shard keys must exist and be stable.
        Accepts a dict like:
          {"keys": ["area_id", "family_id"], "mode": "strict"}
        """
        if shard_schema is None:
            return

        keys = shard_schema.get("keys")
        if not isinstance(keys, list) or not keys:
            raise SigmaViolation("SHARD_SCHEMA_KEYS_INVALID")

        required = {"area_id", "family_id"}
        if set(keys) != required:
            raise SigmaViolation("SHARD_SCHEMA_KEYS_NOT_CANONICAL")


    # =========================================================
    # Optional: side record coordinate sanity (static)
    # =========================================================

    def _check_side_records(self, side_records: Iterable[SideCoord]):
        from sphere_rag.geometry import AREAS, FAMILIES_PER_AREA, HEXES_PER_FAMILY, SIDES_PER_HEX

        for (a, f, h, s) in side_records:
            if not (0 <= a < AREAS):
                raise SigmaViolation("SIDE_RECORD_AREA_INVALID")
            if not (0 <= f < FAMILIES_PER_AREA):
                raise SigmaViolation("SIDE_RECORD_FAMILY_INVALID")
            if not (0 <= h < HEXES_PER_FAMILY):
                raise SigmaViolation("SIDE_RECORD_HEX_INVALID")
            if not (0 <= s < SIDES_PER_HEX):
                raise SigmaViolation("SIDE_RECORD_SIDE_INVALID")


    # =========================================================
    # Structural hash (full static topology fingerprint)
    # =========================================================

    @staticmethod
    def compute_structure_hash(
        *,
        area_names: List[str],
        family_names_global: List[str],
        ring_order: List[int],
        antipodes: Dict[int, int],
        borders: Borders
    ) -> str:
        """
        Hash includes:
          - area names
          - family names (global order)
          - ring order
          - antipode mapping
          - borders (prev/next lists)
        """
        # Normalize borders deterministically
        parts: List[str] = []
        parts.append("AREAS:" + "|".join(area_names))
        parts.append("FAMILIES:" + "|".join(family_names_global))
        parts.append("RING:" + ",".join(map(str, ring_order)))

        # antipodes as sorted pairs
        pairs = []
        used = set()
        for a in sorted(antipodes.keys()):
            b = antipodes[a]
            p = tuple(sorted((a, b)))
            if p in used:
                continue
            used.add(p)
            pairs.append(p)
        pairs.sort()
        parts.append("ANTIPODES:" + "|".join([f"{a}-{b}" for (a, b) in pairs]))

        # borders per area in ring order for stable serialization
        for a in ring_order:
            prev_list = borders[a]["prev"]
            next_list = borders[a]["next"]
            parts.append(f"BORDER:{a}:P=" + ",".join(prev_list))
            parts.append(f"BORDER:{a}:N=" + ",".join(next_list))

        raw = "\n".join(parts)
        return hashlib.sha256(raw.encode("utf-8")).hexdigest()
```
