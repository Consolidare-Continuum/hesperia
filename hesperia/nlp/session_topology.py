# HESPERIA — LEVEL 7 Session topology (temporal activation)
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
"""
Timeline-based activation: segment session text, run activation per segment, compute dynamics.
Enables detection of: shifts in defenses, escalation of aggression, transferential dynamics,
stabilization or integration phases.
"""

from __future__ import annotations

import re
from typing import Any

from hesperia.nlp.session_parser import analyze_session


def segment_session_text(text: str) -> list[str]:
    """
    Разбить текст сессии на сегменты по границам предложений (., ?, !).
    Возвращает список непустых сегментов (после strip).
    """
    if not text or not isinstance(text, str):
        return []
    raw = re.split(r"[.?!]+", text)
    segments = [s.strip() for s in raw if s and s.strip()]
    return segments


def analyze_session_segments(
    text: str,
    marker_index: dict[str, list[tuple[str, float]]] | None = None,
    concept_to_area_family: dict[str, tuple[str, str]] | None = None,
    normalize_scores: bool = True,
    ngram_n: int = 2,
) -> list[dict[str, Any]]:
    """
    Разбить текст на сегменты, для каждого запустить analyze_session, собрать результаты.

    Возвращает список:
    [
      { "segment_id": 1, "text": "...", "areas": {}, "families": {}, "concepts": {} },
      ...
    ]
    """
    segments = segment_session_text(text)
    results: list[dict[str, Any]] = []
    for i, seg in enumerate(segments):
        activation = analyze_session(
            seg,
            marker_index=marker_index,
            concept_to_area_family=concept_to_area_family,
            normalize_scores=normalize_scores,
            ngram_n=ngram_n,
        )
        results.append({
            "segment_id": i + 1,
            "text": seg,
            "areas": activation.get("areas", {}),
            "families": activation.get("families", {}),
            "concepts": activation.get("concepts", {}),
        })
    return results


def _dominant_area(areas: dict[str, float]) -> str | None:
    """Область с максимальной оценкой; None если пусто."""
    if not areas:
        return None
    return max(areas, key=lambda k: areas[k])


def _dominant_family(families: dict[str, float]) -> str | None:
    """Семья с максимальной оценкой; None если пусто."""
    if not families:
        return None
    return max(families, key=lambda k: families[k])


def compute_topology_dynamics(
    segment_results: list[dict[str, Any]],
    aggression_area: str = "A4",
    defense_area: str = "A3",
) -> dict[str, Any]:
    """
    Вычислить динамику между сегментами: сдвиги областей/семей, пики агрессии, точки смены защит.

    Метрики:
    - dominant_area_sequence: доминантная область по каждому сегменту [A2, A3, A4, ...]
    - dominant_family_sequence: доминантная семья по каждому сегменту (опционально)
    - defense_shift_points: индексы сегментов (1-based), где доминантная область меняется на/с A3
    - affect_peaks: индексы сегментов (1-based), где оценка A4 (агрессия) — локальный максимум
    - max_aggression_peak: номер сегмента (1-based), где A4 максимален
    """
    if not segment_results:
        return {
            "dominant_area_sequence": [],
            "dominant_family_sequence": [],
            "defense_shift_points": [],
            "affect_peaks": [],
            "max_aggression_peak": None,
        }

    area_sequence: list[str] = []
    family_sequence: list[str] = []
    aggression_scores: list[float] = []

    for r in segment_results:
        areas = r.get("areas") or {}
        families = r.get("families") or {}
        dom_a = _dominant_area(areas)
        dom_f = _dominant_family(families)
        area_sequence.append(dom_a if dom_a else "")
        family_sequence.append(dom_f if dom_f else "")
        aggression_scores.append(areas.get(aggression_area, 0.0))

    # defense_shift_points: индексы сегментов (1-based), где доминантная область меняется и задействована A3
    defense_shift_points: list[int] = []
    for i in range(1, len(area_sequence)):
        if area_sequence[i] != area_sequence[i - 1] and (
            area_sequence[i] == defense_area or area_sequence[i - 1] == defense_area
        ):
            defense_shift_points.append(i + 1)

    # Локальные пики агрессии (1-based segment_id)
    affect_peaks: list[int] = []
    for i in range(len(aggression_scores)):
        left = aggression_scores[i - 1] if i > 0 else 0.0
        right = aggression_scores[i + 1] if i + 1 < len(aggression_scores) else 0.0
        if aggression_scores[i] >= left and aggression_scores[i] >= right and aggression_scores[i] > 0:
            affect_peaks.append(i + 1)

    # Сегмент с максимальной агрессией (1-based)
    max_aggression_peak: int | None = None
    if aggression_scores:
        idx = max(range(len(aggression_scores)), key=lambda j: aggression_scores[j])
        if aggression_scores[idx] > 0:
            max_aggression_peak = idx + 1

    return {
        "dominant_area_sequence": area_sequence,
        "dominant_family_sequence": family_sequence,
        "defense_shift_points": defense_shift_points,
        "affect_peaks": affect_peaks,
        "max_aggression_peak": max_aggression_peak,
    }


def run_session_topology(
    text: str,
    marker_index: dict[str, list[tuple[str, float]]] | None = None,
    concept_to_area_family: dict[str, tuple[str, str]] | None = None,
    normalize_scores: bool = True,
    ngram_n: int = 2,
) -> dict[str, Any]:
    """
    Полный прогон LEVEL 7: сегментация → активация по сегментам → динамика.

    Возвращает:
    {
      "segments": [ { "segment_id", "text", "areas", "families", "concepts" }, ... ],
      "dynamics": {
        "dominant_area_sequence": [],
        "defense_shift_points": [],
        "affect_peaks": [],
        "max_aggression_peak": ...
      }
    }
    """
    segment_results = analyze_session_segments(
        text,
        marker_index=marker_index,
        concept_to_area_family=concept_to_area_family,
        normalize_scores=normalize_scores,
        ngram_n=ngram_n,
    )
    dynamics = compute_topology_dynamics(segment_results)
    return {
        "segments": segment_results,
        "dynamics": dynamics,
    }
