from __future__ import annotations

import math
from dataclasses import dataclass

from .geometry import AREAS, FAMILIES_PER_AREA, TOTAL_FAMILIES, SideCoord, neighbors

POLARITY_AXES = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11)]


def clamp01(x: float) -> float:
    return 0.0 if x < 0.0 else 1.0 if x > 1.0 else x


def entropy(probs: list[float]) -> float:
    s = sum(probs)
    if s <= 0:
        return 0.0
    h = 0.0
    for v in probs:
        p = v / s
        if p > 0:
            h -= p * math.log(p)
    return h


def tension_energy(area_mass: list[float]) -> float:
    s = sum(area_mass)
    if s <= 0:
        return 0.0
    a = [v / s for v in area_mass]
    e = 0.0
    for pos, neg in POLARITY_AXES:
        d = a[pos] - a[neg]
        e += d * d
    return e


@dataclass(frozen=True, slots=True)
class RegionMetrics:
    active_sides: int
    area_mass: list[float]  # len 12
    family_mass: list[float]  # len 288
    entropy_a: float
    coherence: float
    tension_energy: float
    components: int
    frag_index: float


def compute_area_family_mass(side_weights: dict[int, float]) -> tuple[list[float], list[float]]:
    area_mass = [0.0 for _ in range(AREAS)]
    family_mass = [0.0 for _ in range(TOTAL_FAMILIES)]
    for side_id, w in side_weights.items():
        c = SideCoord.from_side_id(side_id)
        area_mass[c.area] += w
        family_mass[c.family_global()] += w
    return area_mass, family_mass


def coherence(side_ids: set[int]) -> float:
    """Internal edge density under the local neighbor function.

    C(R) = internal_edges / total_edges_from_R
    """
    if not side_ids:
        return 0.0
    internal = 0
    total = 0
    for s in side_ids:
        nbs = neighbors(s)
        total += len(nbs)
        for nb in nbs:
            if nb in side_ids:
                internal += 1
    if total == 0:
        return 0.0
    return internal / total


def connected_components(side_ids: set[int]) -> int:
    if not side_ids:
        return 0
    remaining = set(side_ids)
    comps = 0
    while remaining:
        comps += 1
        start = next(iter(remaining))
        stack = [start]
        remaining.remove(start)
        while stack:
            cur = stack.pop()
            for nb in neighbors(cur):
                if nb in remaining:
                    remaining.remove(nb)
                    stack.append(nb)
    return comps


def region_metrics(side_weights: dict[int, float]) -> RegionMetrics:
    side_ids = set(side_weights.keys())
    area_mass, family_mass = compute_area_family_mass(side_weights)
    comps = connected_components(side_ids)
    active = len(side_ids)
    coh = coherence(side_ids)
    ent = entropy(area_mass)
    ten = tension_energy(area_mass)
    frag = (comps / active) if active else 0.0
    return RegionMetrics(
        active_sides=active,
        area_mass=area_mass,
        family_mass=family_mass,
        entropy_a=ent,
        coherence=coh,
        tension_energy=ten,
        components=comps,
        frag_index=frag,
    )


def intersection_matrix(side_ids: set[int]) -> list[list[int]]:
    """I[a][b] = number of adjacency edges between sides in area a and b, both in region."""
    mat = [[0 for _ in range(AREAS)] for _ in range(AREAS)]
    if not side_ids:
        return mat
    for s in side_ids:
        a = SideCoord.from_side_id(s).area
        for nb in neighbors(s, allow_radial=False):  # keep bounded
            if nb not in side_ids:
                continue
            b = SideCoord.from_side_id(nb).area
            mat[a][b] += 1
    return mat


def bridge_retention_ratio(i_before: list[list[int]], i_after: list[list[int]]) -> float:
    s_before = sum(sum(row) for row in i_before)
    s_after = sum(sum(row) for row in i_after)
    if s_before <= 0:
        return 1.0 if s_after <= 0 else 0.0
    return s_after / s_before

