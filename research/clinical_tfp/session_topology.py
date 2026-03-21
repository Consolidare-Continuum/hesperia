# HESPERIA — LEVEL 10 Session topology (temporal dynamics of activation)
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
"""
Dynamic session topology: segment by token windows, analyze per segment, detect state
transitions, defense shifts, aggression escalation. Trajectory of psychological states.

Named **area curves** project ``segments[].areas`` through ``AREA_CURVE_MAP``. Raw activations
stay in ``segments``; curves use **per-segment cross-area competition** (linear share or **softmax**),
optional **adjacent-segment smoothing**, **session-mean deviation** curves, and **entropy-based
dominance confidence** per segment. Operator bands: ``CURVE_CALIBRATION_REFERENCE``.
"""

from __future__ import annotations

import math
from typing import Any

from research.clinical_tfp.interpretation import detect_defense_pattern, DEFENSE_MAP
from hesperia.nlp.session_parser import tokenize_text, normalize_tokens, analyze_session

# Named clinical axes → single Hesperia area (1:1 projection; tune here or pass a custom map).
AREA_CURVE_MAP: dict[str, str] = {
    "aggression": "A4",
    "anxiety": "A2",
    "shame": "A7",
    "control": "A5",
    "identity_diffusion": "A9",
}

# Reference bands for tuning dict weights / thresholds (not automatic classifiers).
CURVE_CALIBRATION_REFERENCE: dict[str, float] = {
    "low_tension": 0.2,
    "conflict_active": 0.5,
    "escalation": 0.8,
}

# Default kwargs for ``run_session_topology`` (reproducibility + manifest / 09_ bundle).
# Does not include ``text`` or optional indexes (marker_index, phrase_index, concept_to_area_family).
DEFAULT_SESSION_TOPOLOGY_RUN_PARAMS: dict[str, Any] = {
    "window_size": 80,
    "normalize_scores": True,
    "area_competition": "softmax",
    "softmax_temperature": 1.0,
    "curve_smooth_alpha": 0.7,
    "curve_session_center": True,
    "apply_token_negation": True,
    "negation_window": 2,
    "negation_multiplier": 0.5,
    "per_concept_score_cap": 8.0,
    "use_log1p_concept_scores": False,
    "evidence_volume_normalize": True,
    "include_curve_projection_meta": True,
}


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
    **analyze_kwargs: Any,
) -> list[dict[str, Any]]:
    """
    Разбить текст на сегменты (token windows), для каждого запустить analyze_session.
    Доп. kwargs передаются в ``analyze_session`` (напр. ``apply_token_negation``, ``per_concept_score_cap``).
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
            **analyze_kwargs,
        )
        results.append({
            "areas": r.get("areas", {}),
            "families": r.get("families", {}),
            "concepts": r.get("concepts", {}),
        })
    return results


def extract_area_curve(
    segment_results: list[dict[str, Any]],
    area_id: str,
) -> list[float]:
    """Per-segment scalar series: activation of ``area_id`` from each segment's ``areas``."""
    out: list[float] = []
    for r in segment_results:
        raw = (r.get("areas") or {}).get(area_id, 0.0)
        try:
            out.append(float(raw))
        except (TypeError, ValueError):
            out.append(0.0)
    return out


def build_area_curves(
    segment_results: list[dict[str, Any]],
    curve_map: dict[str, str] | None = None,
) -> dict[str, list[float]]:
    """Build all named curves from ``curve_map`` (default: ``AREA_CURVE_MAP``)."""
    m = curve_map or AREA_CURVE_MAP
    return {name: extract_area_curve(segment_results, aid) for name, aid in m.items()}


def total_area_activation(areas: dict[str, Any]) -> float:
    """Sum of non-negative area activations in one segment."""
    s = 0.0
    for v in (areas or {}).values():
        try:
            s += max(0.0, float(v))
        except (TypeError, ValueError):
            continue
    return s


def normalize_areas_share_of_total(
    areas: dict[str, Any],
    eps: float = 1e-12,
) -> dict[str, float]:
    """
    Per-segment mix: area_k / sum_j area_j → bounded [0,1], comparable when total mass varies.
    Empty or near-zero total → all zeros.
    """
    t = total_area_activation(areas)
    if t <= eps:
        return {str(k): 0.0 for k in (areas or {})}
    out: dict[str, float] = {}
    for k, v in (areas or {}).items():
        try:
            out[str(k)] = max(0.0, float(v)) / t
        except (TypeError, ValueError):
            out[str(k)] = 0.0
    return out


def segment_results_areas_as_share(
    segment_results: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Shallow copy each segment; replace ``areas`` with share-of-total (families/concepts unchanged)."""
    out: list[dict[str, Any]] = []
    for r in segment_results:
        d = dict(r)
        d["areas"] = normalize_areas_share_of_total(r.get("areas") or {})
        out.append(d)
    return out


def normalize_areas_softmax(
    areas: dict[str, Any],
    temperature: float = 1.0,
) -> dict[str, float]:
    """
    Cross-area competition: softmax over non-negative activations (sharper dominant than linear share).
    """
    tau = max(float(temperature), 1e-6)
    items = [(str(k), max(0.0, float(v))) for k, v in (areas or {}).items()]
    if not items:
        return {}
    mx = max(v for _, v in items)
    exps = [(k, math.exp((v - mx) / tau)) for k, v in items]
    s = sum(e for _, e in exps) or 1e-12
    return {k: e / s for k, e in exps}


def segment_results_areas_for_curve_competition(
    segment_results: list[dict[str, Any]],
    mode: str,
    softmax_temperature: float = 1.0,
) -> list[dict[str, Any]]:
    """
    ``mode``: ``share`` | ``softmax`` | ``none`` — how per-segment ``areas`` are reduced before curve extraction.
    """
    m = (mode or "none").strip().lower()
    out: list[dict[str, Any]] = []
    for r in segment_results:
        d = dict(r)
        raw = r.get("areas") or {}
        if m == "share":
            d["areas"] = normalize_areas_share_of_total(raw)
        elif m == "softmax":
            d["areas"] = normalize_areas_softmax(raw, temperature=softmax_temperature)
        else:
            na: dict[str, float] = {}
            for k, v in raw.items():
                fv = _float_or_skip(v)
                if fv is not None:
                    na[str(k)] = max(0.0, fv)
            d["areas"] = na
        out.append(d)
    return out


def _float_or_skip(v: Any) -> float | None:
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def areas_to_positive_probs(areas: dict[str, Any]) -> list[float]:
    vals: list[float] = []
    for v in (areas or {}).values():
        fv = _float_or_skip(v)
        if fv is not None and fv > 0:
            vals.append(fv)
    t = sum(vals)
    if t <= 1e-15:
        return []
    return [x / t for x in vals]


def entropy_shannon(ps: list[float]) -> float:
    return -sum(p * math.log(p + 1e-15) for p in ps)


def dominance_confidence_from_areas(areas: dict[str, Any]) -> float:
    """Higher when one area dominates (low entropy of normalized positive mass). ~0..1."""
    ps = areas_to_positive_probs(areas)
    if len(ps) < 2:
        return 0.62 if len(ps) == 1 else 0.35
    h = entropy_shannon(ps)
    h_max = math.log(len(ps))
    if h_max <= 1e-12:
        return 0.5
    return max(0.0, min(1.0, 1.0 - h / h_max))


def center_curves_by_session_mean(curves: dict[str, list[float]]) -> dict[str, list[float]]:
    """Per named curve: subtract session mean (deviation-from-baseline along session)."""
    out: dict[str, list[float]] = {}
    for name, series in curves.items():
        if not series:
            out[name] = []
            continue
        mu = sum(float(x) for x in series) / len(series)
        out[name] = [float(x) - mu for x in series]
    return out


def smooth_curve_adjacent(
    values: list[float],
    alpha_current: float = 0.7,
) -> list[float]:
    """
    s[0] = raw[0]; s[t] = α·raw[t] + (1−α)·raw[t−1]. Reduces spike noise along the session axis.
    """
    if not values:
        return []
    a = float(alpha_current)
    b = 1.0 - a
    out: list[float] = [float(values[0])]
    for i in range(1, len(values)):
        out.append(a * float(values[i]) + b * float(values[i - 1]))
    return out


def postprocess_area_curves(
    segment_results: list[dict[str, Any]],
    curve_map: dict[str, str] | None = None,
    *,
    area_competition: str = "share",
    softmax_temperature: float = 1.0,
    smooth_alpha: float | None = 0.7,
    session_center_curves: bool = True,
    include_dominance_confidence: bool = True,
) -> tuple[dict[str, list[float]], dict[str, Any], dict[str, list[float]]]:
    """
    Build named curves after per-segment area competition (share / softmax / none), optional
    temporal smoothing, optional session-mean centering (returned as third dict).
    """
    m = curve_map or AREA_CURVE_MAP
    mode = (area_competition or "none").strip().lower()
    base = segment_results_areas_for_curve_competition(
        segment_results,
        mode,
        softmax_temperature=softmax_temperature,
    )
    curves = build_area_curves(base, curve_map=m)
    conf_series: list[float] = []
    if include_dominance_confidence:
        for row in base:
            conf_series.append(dominance_confidence_from_areas(row.get("areas") or {}))
    meta: dict[str, Any] = {
        "area_competition": mode,
        "softmax_temperature": float(softmax_temperature) if mode == "softmax" else None,
        "smooth": None,
        "session_center": None,
        "segment_dominance_confidence": conf_series if include_dominance_confidence else None,
    }
    if smooth_alpha is not None:
        curves = {
            name: smooth_curve_adjacent(series, alpha_current=float(smooth_alpha))
            for name, series in curves.items()
        }
        meta["smooth"] = {"mode": "adjacent_raw", "alpha_current": float(smooth_alpha)}
    rel: dict[str, list[float]] = {}
    if session_center_curves and curves:
        rel = center_curves_by_session_mean(curves)
        meta["session_center"] = "mean_subtracted_per_named_curve"
    return curves, meta, rel


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
    return extract_area_curve(segment_results, area_a4)


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
    *,
    area_competition: str = "softmax",
    softmax_temperature: float = 1.0,
    curve_smooth_alpha: float | None = 0.7,
    curve_session_center: bool = True,
    apply_token_negation: bool = True,
    negation_window: int = 2,
    negation_multiplier: float = 0.5,
    per_concept_score_cap: float | None = 8.0,
    use_log1p_concept_scores: bool = False,
    evidence_volume_normalize: bool = True,
    include_curve_projection_meta: bool = True,
) -> dict[str, Any]:
    """
    Полный прогон LEVEL 10: сегментация по окнам → активация по сегментам →
    переходы областей, кривая агрессии, последовательность состояний, смена защит.

    **Сигнал:** по умолчанию — потолок на концепт, демпф негации в окне токена, конкуренция
    областей (``softmax`` или ``share``), сглаживание по сессии, кривые отклонения от среднего
    сессии в ``area_curves_session_relative``. Сырые ``segments[].areas`` — выход движка до
    softmax на кривых (после max-norm в ``analyze_session`` если ``normalize_scores``).

    Legacy-only кривые: ``area_competition="none"``, ``curve_smooth_alpha=None``,
    ``curve_session_center=False``, ``apply_token_negation=False``, ``per_concept_score_cap=None``,
    ``evidence_volume_normalize=False``.

    Возвращает:
    {
      "segments": [ { "areas", "families", "concepts" }, ... ],
      "transitions": [ ["A2","A3"], ["A3","A4"] ],
      "area_curves": { ... },
      "area_curves_session_relative": { ... },  # if curve_session_center
      "aggression_curve": [...],
      "curve_projection_meta": { ... },
      "state_sequence": [ ... ],
      "defense_timeline": [ ... ]
    }
    """
    segment_results = analyze_session_segments(
        text,
        window_size=window_size,
        marker_index=marker_index,
        concept_to_area_family=concept_to_area_family,
        phrase_index=phrase_index,
        normalize_scores=normalize_scores,
        apply_token_negation=apply_token_negation,
        negation_window=negation_window,
        negation_multiplier=negation_multiplier,
        per_concept_score_cap=per_concept_score_cap,
        use_log1p_concept_scores=use_log1p_concept_scores,
        evidence_volume_normalize=evidence_volume_normalize,
    )
    area_curves, cmeta, rel = postprocess_area_curves(
        segment_results,
        area_competition=area_competition,
        softmax_temperature=softmax_temperature,
        smooth_alpha=curve_smooth_alpha,
        session_center_curves=bool(curve_session_center),
        include_dominance_confidence=True,
    )
    out: dict[str, Any] = {
        "segments": segment_results,
        "transitions": detect_state_transitions(segment_results),
        "area_curves": area_curves,
        "aggression_curve": area_curves["aggression"],
        "state_sequence": build_session_state_sequence(segment_results),
        "defense_timeline": detect_defense_shifts(segment_results),
    }
    if curve_session_center and rel:
        out["area_curves_session_relative"] = rel
    if include_curve_projection_meta:
        out["curve_projection_meta"] = {
            **cmeta,
            "calibration_reference_bands": dict(CURVE_CALIBRATION_REFERENCE),
            "engine_params": {
                "window_size": window_size,
                "normalize_scores": normalize_scores,
                "area_competition": area_competition,
                "softmax_temperature": softmax_temperature,
                "curve_smooth_alpha": curve_smooth_alpha,
                "curve_session_center": curve_session_center,
                "apply_token_negation": apply_token_negation,
                "negation_window": negation_window,
                "negation_multiplier": negation_multiplier,
                "per_concept_score_cap": per_concept_score_cap,
                "use_log1p_concept_scores": use_log1p_concept_scores,
                "evidence_volume_normalize": evidence_volume_normalize,
                "include_curve_projection_meta": include_curve_projection_meta,
            },
            "area_curve_map": dict(AREA_CURVE_MAP),
            "lexical_controls": {
                "apply_token_negation": apply_token_negation,
                "negation_window": negation_window,
                "negation_multiplier": negation_multiplier,
                "per_concept_score_cap": per_concept_score_cap,
                "use_log1p_concept_scores": use_log1p_concept_scores,
                "evidence_volume_normalize": evidence_volume_normalize,
            },
            "note": (
                "Bands are operator tuning targets. segment_dominance_confidence is entropy-based "
                "peakiness after area_competition, not clinical certainty."
            ),
        }
    return out
