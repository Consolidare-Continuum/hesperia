# HESPERIA — LEVEL 10 Session topology (temporal dynamics of activation)
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
"""
Dynamic session topology: segment by token windows, analyze per segment, detect state
transitions, defense shifts, aggression escalation. Trajectory of psychological states.
"""

from __future__ import annotations

from typing import Any

from research.clinical_tfp.interpretation import detect_defense_pattern, DEFENSE_MAP
from hesperia.nlp.session_parser import tokenize_text, normalize_tokens, analyze_session


def segment_session(text: str, window_size: int = 80) -> list[str]:
    """
    Разбить сессию на сегменты по окнам токенов (не перекрывающиеся).
    segment_1 → tokens 0..window_size-1, segment_2 → window_size..2*window_size-1, ...
    Возвращает список строк — текст каждого сегмента (токены склеены пробелом).
    """
    if not text or not isinstance(text, str) or window_size < 1:
        return []
    tokens = tokenize_text(text)
    normalized = normalize_tokens(tokens)
    if not normalized:
        return []
    segments: list[str] = []
    for i in range(0, len(normalized), window_size):
        chunk = normalized[i : i + window_size]
        segments.append(" ".join(chunk))
    return segments


def analyze_session_segments(
    text: str,
    window_size: int = 80,
    marker_index: dict[str, list[tuple[str, float]]] | None = None,
    concept_to_area_family: dict[str, tuple[str, str]] | None = None,
    phrase_index: dict[str, dict[tuple[str, ...], list[tuple[str, float]]]] | None = None,
    normalize_scores: bool = True,
) -> list[dict[str, Any]]:
    """
    Разбить текст на сегменты (token windows), для каждого запустить analyze_session.
    Возвращает список активаций: [ { "areas": {}, "families": {}, "concepts": {} }, ... ].
    """
    segments = segment_session(text, window_size=window_size)
    results: list[dict[str, Any]] = []
    for seg in segments:
        if not seg.strip():
            results.append({"areas": {}, "families": {}, "concepts": {}})
            continue
        r = analyze_session(
            seg,
            marker_index=marker_index,
            concept_to_area_family=concept_to_area_family,
            phrase_index=phrase_index,
            normalize_scores=normalize_scores,
        )
        results.append({
            "areas": r.get("areas", {}),
            "families": r.get("families", {}),
            "concepts": r.get("concepts", {}),
        })
    return results


def _dominant_area(areas: dict[str, float]) -> str:
    if not areas:
        return ""
    return max(areas, key=lambda k: areas[k])


def detect_state_transitions(
    segment_results: list[dict[str, Any]],
) -> list[list[str]]:
    """
    Сравнить доминантные области по сегментам. Вернуть список переходов [from, to].
    """
    if len(segment_results) < 2:
        return []
    prev = _dominant_area(segment_results[0].get("areas") or {})
    transitions: list[list[str]] = []
    for r in segment_results[1:]:
        curr = _dominant_area(r.get("areas") or {})
        if prev and curr and prev != curr:
            transitions.append([prev, curr])
        prev = curr
    return transitions


def detect_defense_shifts(
    segment_results: list[dict[str, Any]],
    defense_map: dict[str, str] | None = None,
) -> list[str]:
    """
    Доминантная защита по каждому сегменту (A3 family → имя из DEFENSE_MAP).
    Возвращает список имён защит по сегментам (timeline).
    """
    m = defense_map or DEFENSE_MAP
    out: list[str] = []
    for r in segment_results:
        families = r.get("families") or {}
        defense = detect_defense_pattern(families, defense_map=m)
        out.append(defense if defense else "")
    return out


def detect_aggression_escalation(
    segment_results: list[dict[str, Any]],
    area_a4: str = "A4",
) -> list[float]:
    """
    Оценка A4 (агрессия) по каждому сегменту. Возвращает список значений.
    Монотонный рост интерпретируется как эскалация.
    """
    return [
        (r.get("areas") or {}).get(area_a4, 0.0)
        for r in segment_results
    ]


def build_session_state_sequence(
    segment_results: list[dict[str, Any]],
) -> list[str]:
    """
    Последовательность доминантных областей по сегментам.
    Пример: ["A2", "A3", "A3", "A4", "A7"] — топология сессии.
    """
    return [
        _dominant_area(r.get("areas") or {})
        for r in segment_results
    ]


def run_session_topology(
    text: str,
    window_size: int = 80,
    marker_index: dict[str, list[tuple[str, float]]] | None = None,
    concept_to_area_family: dict[str, tuple[str, str]] | None = None,
    phrase_index: dict[str, dict[tuple[str, ...], list[tuple[str, float]]]] | None = None,
    normalize_scores: bool = True,
) -> dict[str, Any]:
    """
    Полный прогон LEVEL 10: сегментация по окнам → активация по сегментам →
    переходы областей, кривая агрессии, последовательность состояний, смена защит.

    Возвращает:
    {
      "segments": [ { "areas", "families", "concepts" }, ... ],
      "transitions": [ ["A2","A3"], ["A3","A4"] ],
      "aggression_curve": [ 0.10, 0.22, 0.54, 0.83 ],
      "state_sequence": [ "A2", "A3", "A4" ],
      "defense_timeline": [ "splitting", "projective_identification", ... ]
    }
    """
    segment_results = analyze_session_segments(
        text,
        window_size=window_size,
        marker_index=marker_index,
        concept_to_area_family=concept_to_area_family,
        phrase_index=phrase_index,
        normalize_scores=normalize_scores,
    )
    return {
        "segments": segment_results,
        "transitions": detect_state_transitions(segment_results),
        "aggression_curve": detect_aggression_escalation(segment_results),
        "state_sequence": build_session_state_sequence(segment_results),
        "defense_timeline": detect_defense_shifts(segment_results),
    }
