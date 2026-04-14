# HESPERIA — Contradiction coupling for TFP area activation (deterministic).
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

from __future__ import annotations

import math
from typing import Any

_EPS = 1e-15


def _extract_pair_and_score(row: dict[str, Any]) -> tuple[str | None, str | None, float]:
    """Parse contradiction row: ``pair`` or ``concept_a``/``concept_b``; score keys in fixed order."""
    ca: str | None = None
    cb: str | None = None
    raw_pair = row.get("pair")
    if isinstance(raw_pair, (list, tuple)) and len(raw_pair) >= 2:
        ca = str(raw_pair[0]) if raw_pair[0] is not None else None
        cb = str(raw_pair[1]) if raw_pair[1] is not None else None
    else:
        if row.get("concept_a") is not None:
            ca = str(row["concept_a"])
        if row.get("concept_b") is not None:
            cb = str(row["concept_b"])
    score = 0.0
    if "raw_contradiction_score" in row and row["raw_contradiction_score"] is not None:
        score = float(row["raw_contradiction_score"])
    elif "score" in row and row["score"] is not None:
        score = float(row["score"])
    if not math.isfinite(score):
        score = 0.0
    return ca, cb, score


def _sort_contradiction_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Stable deterministic ordering before accumulation."""

    def key_fn(idx_row: tuple[int, dict[str, Any]]) -> tuple[str, str, float, int]:
        idx, row = idx_row
        ca, cb, sc = _extract_pair_and_score(row)
        if ca is None or cb is None:
            return ("", "", 0.0, idx)
        a0, b0 = (ca, cb) if ca <= cb else (cb, ca)
        return (a0, b0, -sc, idx)

    enumerated = list(enumerate(rows))
    enumerated.sort(key=key_fn)
    return [row for _, row in enumerated]


def _resolve_area(concept_id: str, concept_to_area_family: dict[str, tuple[str, str]]) -> str | None:
    af = concept_to_area_family.get(concept_id)
    if not af:
        return None
    return str(af[0])


def count_contradiction_rows_used(
    contradictions: list[dict[str, Any]] | None,
    concept_to_area_family: dict[str, tuple[str, str]],
    area_ids: list[str],
) -> int:
    """Rows with positive score and both concepts resolving to known areas."""
    if not contradictions:
        return 0
    valid_areas = set(area_ids)
    n = 0
    for row in _sort_contradiction_rows(list(contradictions)):
        ca, cb, sc = _extract_pair_and_score(row)
        if ca is None or cb is None or sc <= _EPS:
            continue
        aa = _resolve_area(ca, concept_to_area_family)
        ab = _resolve_area(cb, concept_to_area_family)
        if aa is None or ab is None:
            continue
        if aa not in valid_areas or ab not in valid_areas:
            continue
        n += 1
    return n


def build_area_contradiction_pressure(
    contradictions: list[dict[str, Any]] | None,
    concept_to_area_family: dict[str, tuple[str, str]],
    area_ids: list[str],
) -> dict[str, float]:
    """Per-area pressure in [0, 1], max-normalized over observed contradiction scores."""
    accum = {a: 0.0 for a in area_ids}
    valid_areas = set(area_ids)
    if not contradictions:
        return accum

    for row in _sort_contradiction_rows(list(contradictions)):
        ca, cb, sc = _extract_pair_and_score(row)
        if ca is None or cb is None or sc <= _EPS:
            continue
        aa = _resolve_area(ca, concept_to_area_family)
        ab = _resolve_area(cb, concept_to_area_family)
        if aa is None or ab is None or aa not in valid_areas or ab not in valid_areas:
            continue
        accum[aa] += sc
        if aa != ab:
            accum[ab] += sc

    max_p = max(accum.values()) if accum else 0.0
    if max_p <= _EPS:
        return {a: 0.0 for a in area_ids}
    return {a: float(accum[a]) / max_p for a in area_ids}


def build_dynamic_inhibition_delta(
    contradictions: list[dict[str, Any]] | None,
    concept_to_area_family: dict[str, tuple[str, str]],
    area_ids: list[str],
) -> list[list[float]]:
    """Symmetric off-diagonal inhibition delta, max-normalized."""
    n = len(area_ids)
    delta = [[0.0 for _ in range(n)] for _ in range(n)]
    index = {aid: i for i, aid in enumerate(area_ids)}
    valid_areas = set(area_ids)

    if not contradictions:
        return delta

    for row in _sort_contradiction_rows(list(contradictions)):
        ca, cb, sc = _extract_pair_and_score(row)
        if ca is None or cb is None or sc <= _EPS:
            continue
        aa = _resolve_area(ca, concept_to_area_family)
        ab = _resolve_area(cb, concept_to_area_family)
        if aa is None or ab is None or aa not in valid_areas or ab not in valid_areas:
            continue
        i, j = index[aa], index[ab]
        if i == j:
            continue
        delta[i][j] += sc
        delta[j][i] += sc

    max_cell = max(delta[i][j] for i in range(n) for j in range(n))
    if max_cell <= _EPS:
        return delta
    inv = 1.0 / max_cell
    return [[delta[i][j] * inv for j in range(n)] for i in range(n)]


def _apply_area_inhibition_matrix(
    area_raw: dict[str, float],
    *,
    matrix: list[list[float]],
    area_ids: list[str],
    inhibition_scale: float,
) -> dict[str, float]:
    vector = [max(0.0, float(area_raw.get(area_id, 0.0))) for area_id in area_ids]
    scale = max(0.0, float(inhibition_scale))
    inhibited: dict[str, float] = {}
    n = len(area_ids)
    for i, area_id in enumerate(area_ids):
        inhibition = 0.0
        for j in range(n):
            inhibition += float(matrix[i][j]) * vector[j]
        inhibited[area_id] = max(0.0, vector[i] - inhibition * scale)
    return inhibited


def apply_contradiction_coupling(
    areas_raw: dict[str, float],
    base_matrix: list[list[float]],
    contradiction_pressure: dict[str, float],
    dynamic_delta: list[list[float]],
    area_ids: list[str],
    *,
    inhibition_scale: float = 1.0,
) -> dict[str, Any]:
    """
    Apply pressure attenuation, combine inhibition matrices, run inhibition pass.

    When combined matrix max exceeds 1.0, scale all entries down uniformly (diagonal stays zero).
    """
    n = len(area_ids)
    # Pressure-adjusted raw areas
    areas_pressure_adjusted: dict[str, float] = {}
    for aid in area_ids:
        raw_v = max(0.0, float(areas_raw.get(aid, 0.0)))
        p = min(1.0, max(0.0, float(contradiction_pressure.get(aid, 0.0))))
        areas_pressure_adjusted[aid] = max(0.0, raw_v * (1.0 - p))

    base: list[list[float]] = []
    for i in range(n):
        row = list(base_matrix[i]) if i < len(base_matrix) else []
        if len(row) < n:
            row = row + [0.0] * (n - len(row))
        base.append([float(row[j]) for j in range(n)])

    dlt: list[list[float]] = []
    for i in range(n):
        row = list(dynamic_delta[i]) if i < len(dynamic_delta) else []
        if len(row) < n:
            row = row + [0.0] * (n - len(row))
        dlt.append([float(row[j]) for j in range(n)])

    dynamic: list[list[float]] = []
    for i in range(n):
        dynamic.append([base[i][j] + dlt[i][j] for j in range(n)])
        dynamic[i][i] = 0.0

    mx = max(dynamic[i][j] for i in range(n) for j in range(n))
    if mx > 1.0 + _EPS:
        inv = 1.0 / mx
        dynamic = [[dynamic[i][j] * inv for j in range(n)] for i in range(n)]
        for i in range(n):
            dynamic[i][i] = 0.0

    areas_inhibited = _apply_area_inhibition_matrix(
        areas_pressure_adjusted,
        matrix=dynamic,
        area_ids=area_ids,
        inhibition_scale=inhibition_scale,
    )

    return {
        "areas_pressure_adjusted": areas_pressure_adjusted,
        "inhibition_matrix_dynamic": dynamic,
        "areas_inhibited": areas_inhibited,
        "contradiction_pressure": dict(contradiction_pressure),
        "dynamic_inhibition_delta": dlt,
    }
