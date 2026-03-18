# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# See LEGAL_NOTICE.md for full terms.

"""Canonical 12-area icosahedral metrics: adjacency load, shortest-path distance, locality."""

from __future__ import annotations

from collections import deque
from functools import lru_cache
from pathlib import Path
from typing import Any

# Lazy import numpy only when loading file


@lru_cache(maxsize=1)
def _canonical_area_adjacency_default() -> tuple[tuple[int, ...], ...]:
    from sphere.topology.topology_loader import load_area_adjacency as _load_adj
    from hesperia.engine.triz.guards import guard_adjacency_immutable

    adj = _load_adj(None)
    guard_adjacency_immutable(adj)
    return tuple(tuple(int(x) for x in row) for row in adj.tolist())


def load_area_adjacency(data_root: Path | None = None) -> tuple[tuple[int, ...], ...]:
    """Alias for Task 12.1 — canonical icosahedral area adjacency (read-only rows)."""
    return canonical_area_adjacency(data_root)


def canonical_area_adjacency(data_root: Path | None = None) -> tuple[tuple[int, ...], ...]:
    """
    Load canonical 12×12 area adjacency from HESPERIA topology data (read-only).
    """
    if data_root is None:
        return _canonical_area_adjacency_default()
    from sphere.topology.topology_loader import load_area_adjacency as _load_adj
    from hesperia.engine.triz.guards import guard_adjacency_immutable

    adj = _load_adj(data_root)
    guard_adjacency_immutable(adj)
    return tuple(tuple(int(x) for x in row) for row in adj.tolist())


def neighbors_from_adjacency(adj: tuple[tuple[int, ...], ...]) -> dict[int, list[int]]:
    n = len(adj)
    out: dict[int, list[int]] = {}
    for i in range(n):
        out[i] = sorted(j for j in range(n) if adj[i][j] == 1)
    return out


@lru_cache(maxsize=1)
def _neighbor_map() -> dict[int, tuple[int, ...]]:
    adj = canonical_area_adjacency()
    nm = neighbors_from_adjacency(adj)
    return {k: tuple(v) for k, v in sorted(nm.items())}


def area_distance(area_a: int, area_b: int) -> int:
    """Shortest path length on icosahedral area graph; 0 = same, 1 = adjacent."""
    if area_a == area_b:
        return 0
    nm = {k: list(v) for k, v in _neighbor_map().items()}
    if area_a not in nm or area_b not in nm:
        return 12
    q = deque([(area_a, 0)])
    seen = {area_a}
    while q:
        u, d = q.popleft()
        if u == area_b:
            return d
        for v in nm.get(u, ()):
            if v not in seen:
                seen.add(v)
                q.append((v, d + 1))
    return 12


def contradiction_locality_score(area_a: int, area_b: int) -> float:
    """1/(1+d): local contradiction high, cross-domain spread low."""
    d = area_distance(area_a, area_b)
    return round(1.0 / (1.0 + float(d)), 6)


def areas_are_adjacent(area_a: int, area_b: int) -> bool:
    return area_a != area_b and area_distance(area_a, area_b) == 1


def get_area_neighbors() -> dict[int, list[int]]:
    """Canonical adjacency lists (area index → neighbor areas)."""
    return {k: list(v) for k, v in _neighbor_map().items()}


def get_area_adjacency() -> list[list[int]]:
    """12×12 binary adjacency matrix (canonical icosahedral); same source as propagation TRIZ."""
    adj = canonical_area_adjacency()
    return [list(row) for row in adj]
