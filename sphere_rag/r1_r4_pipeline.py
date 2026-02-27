# R1–R4 pipeline: segment → L1–L9 → Unit → aggregation → BookProfile. Ref: spec §Implementation Plan item 5.
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .attribution_shared import load_dict_a_surface_map_v033, load_dict_a_v06
from .attribution_v033 import (
    load_dict_a_v033,
    load_dict_b_v033,
    normalize,
    tokenize,
)
from .attribution_v033 import attribute as _attribute_v033
from .attribution_shared import attribute as attribute_with_surface
from .layers import (
    build_canonical_stub_adjacency,
    compute_L1,
    compute_L2,
    compute_L3,
    compute_L4,
    compute_L5,
    compute_L6,
    compute_L7,
    compute_L8,
    compute_L9,
    load_defaults,
)
from .r1_r4_esm_defaults import load_r1_r4_esm_defaults
from .r1_r4_segmenters import (
    get_text_span,
    segment_by_book,
    segment_by_chapters,
    segment_by_paragraphs,
    segment_by_sentences,
)
from .r1_r4_unit import build_unit


def _run_layers_for_text(
    text: str,
    dict_a: dict,
    dict_b: dict,
    defaults: dict,
    F: int,
    A: int,
    eps: float,
    D: int,
    surface_map: dict[str, str] | None = None,
) -> tuple[list[int], dict, dict, dict, dict, dict, dict, dict]:
    """Tokenize, attribute, run L1–L9; return (hits, L1, L2, L3, L4, L5, L6, L7).
    When surface_map is provided, tokens are resolved to structural keys before Dict A lookup (avoids token_count 0 for lemma-keyed input).
    """
    tokens = tokenize(normalize(text))
    if surface_map:
        matched, _ = attribute_with_surface(tokens, dict_a, dict_b, surface_map=surface_map)
    else:
        matched, _ = _attribute_v033(tokens, dict_a, dict_b)
    L1 = compute_L1(len(tokens), matched, F=F, A=A, eps=eps)
    hits = [0] * F
    for fg, _ in matched:
        if 0 <= fg < F:
            hits[fg] += 1
    adj = build_canonical_stub_adjacency(F, A)
    L2 = compute_L2(L1, hits, adjacency=adj, F=F, A=A, MAX_ALLOWED_DEPTH=D, eps=eps)
    visited_B = set(L2.get("VISITED_IDS", []))
    L1_S, L2_S, hits_S = L1, L2, hits[:]
    L3 = compute_L3(L1, L2, hits, L1_S, L2_S, hits_S, F=F, A=A, eps=1e-12, **{
        k: defaults.get(k) for k in ("SHADOW_MAX_DEVIATION", "SHADOW_MAX_CROSS_AREA_DELTA", "SHADOW_ALLOW_AREA_FLIP", "TOP_K") if k in defaults
    })
    R_B, R_S = [], []
    L4 = compute_L4(L1, L1_S, hits, hits_S, R_B, R_S, F=F, A=A, **{
        k: defaults.get(k) for k in ("RETRIEVAL_MODE_ID", "TOP_K", "MAX_SHORTFALL", "MIN_SUPPORT", "MAX_DUP_BOOK_CONC") if k in defaults
    })
    L5 = compute_L5(L1, L4, R_B, [], F=F, A=A, TOP_K=defaults.get("TOP_K", 20), MAX_SHORTFALL=defaults.get("MAX_SHORTFALL", 2), MAX_CONTRADICTION=defaults.get("MAX_CONTRADICTION", 0.50))
    L6 = compute_L6(L1, L2, F=F)
    L7 = compute_L7(L1, L2, L3, L4, L5, L6, visited_B=visited_B, F=F, A=A, **{
        k: defaults.get(k) for k in ("MIN_COVERAGE_RATIO", "MAX_CROSS_AREA_RATIO", "MAX_LYAPUNOV", "HIGH_CONF", "MED_CONF", "MIN_PCS") if k in defaults
    })
    return hits, L1, L2, L3, L4, L5, L6, L7


def _weighted_mean(values: list[float], weights: list[float], eps: float = 1e-9) -> float:
    if not weights or sum(weights) <= 0:
        return 0.0
    return sum(v * w for v, w in zip(values, weights)) / (sum(weights) + eps)


def _weighted_variance(values: list[float], weights: list[float], mean: float, eps: float = 1e-9, cap: float = 0.25) -> float:
    if not weights or sum(weights) <= 0:
        return 0.0
    total_w = sum(weights) + eps
    var = sum(w * (v - mean) ** 2 for v, w in zip(values, weights)) / total_w
    return min(cap, max(0.0, var))


def _aggregate_level(units: list[dict[str, Any]], metric_keys: list[str]) -> dict[str, Any]:
    """Aggregate units to level_summary: token_count_total, SI_means, SI_variances, SCI."""
    if not units:
        return {
            "token_count_total": 0,
            "SI_means": {k: 0.0 for k in metric_keys},
            "SI_variances": {k: 0.0 for k in metric_keys},
            "SCI": 0.0,
        }
    weights = [u["token_count"] for u in units]
    si_means = {}
    si_variances = {}
    for k in metric_keys:
        vals = [u["SI_metrics"].get(k, 0.0) for u in units]
        m = _weighted_mean(vals, weights)
        si_means[k] = round(min(1.0, max(0.0, m)), 6)
        v = _weighted_variance(vals, weights, m)
        si_variances[k] = round(v, 6)
    # SCI = clamp01((dominance_mean - entropy_mean - leakage_mean - contradiction_pressure_mean + 1) / 2)
    sci_raw = (
        si_means.get("dominance", 0.0) - si_means.get("entropy", 0.0)
        - si_means.get("leakage", 0.0) - si_means.get("contradiction_pressure", 0.0)
    )
    sci = round(min(1.0, max(0.0, (sci_raw + 1.0) / 2.0)), 6)
    return {
        "token_count_total": sum(weights),
        "SI_means": si_means,
        "SI_variances": si_variances,
        "SCI": sci,
    }


def _zero_delta(metric_keys: list[str]) -> dict[str, Any]:
    return {k: 0.0 for k in metric_keys}


def _compute_scale_deltas(
    level_averages: dict[str, Any],
    metric_keys: list[str],
    esm_defaults: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Compute scale_deltas: delta_observed (Rk+1 mean − Rk mean), delta_expected from ESM, delta_deviation = observed − expected."""
    esm = esm_defaults or load_r1_r4_esm_defaults() or {}
    delta_expected_by_transition = esm.get("delta_expected", {})
    transitions = [("R1", "R2", "R1_to_R2"), ("R2", "R3", "R2_to_R3"), ("R3", "R4", "R3_to_R4")]
    scale_deltas = {}
    for r_lo, r_hi, key in transitions:
        sum_lo = level_averages.get(r_lo, {}).get("SI_means", {})
        sum_hi = level_averages.get(r_hi, {}).get("SI_means", {})
        exp = delta_expected_by_transition.get(key, {}) if isinstance(delta_expected_by_transition, dict) else {}
        delta_observed = {k: round((sum_hi.get(k, 0.0) - sum_lo.get(k, 0.0)), 6) for k in metric_keys}
        delta_expected = {k: round(float(exp.get(k, 0.0)), 6) for k in metric_keys}
        delta_deviation = {k: round(delta_observed[k] - delta_expected[k], 6) for k in metric_keys}
        scale_deltas[key] = {
            "delta_observed": delta_observed,
            "delta_expected": delta_expected,
            "delta_deviation": delta_deviation,
        }
    return scale_deltas


def _run_units_for_spans(
    text: str,
    spans: list[tuple[int, int]],
    level: str,
    parent_id: str | None,
    unit_id_prefix: str,
    dict_a: dict,
    dict_b: dict,
    defaults: dict,
    F: int,
    A: int,
    eps: float,
    D: int,
    surface_map: dict[str, str] | None = None,
) -> list[dict[str, Any]]:
    """Run L1–L9 for each span and return list of Units."""
    units = []
    metric_keys = ["coverage", "dominance", "entropy", "leakage", "contradiction_pressure", "stability", "shadow_deviation"]
    for i, span in enumerate(spans):
        segment_text = get_text_span(text, span)
        if not segment_text.strip():
            continue
        hits, L1, L2, L3, L4, L5, L6, L7 = _run_layers_for_text(
            segment_text, dict_a, dict_b, defaults, F, A, eps, D, surface_map=surface_map
        )
        token_count = sum(hits)
        unit_id = f"{unit_id_prefix}_{i + 1}"
        unit = build_unit(unit_id, level, parent_id, token_count, hits, L1, L2, L3, L4, L5, L6, L7, F=F, A=A)
        units.append(unit)
    return units


def run_full_pipeline(
    text: str,
    book_id: str = "book",
    dict_a: dict | None = None,
    dict_b: dict | None = None,
    assets_root: Path | None = None,
    levels: list[str] | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """
    Run R1–R4 pipeline: segment at each level, run L1–L9 per segment, build Units, aggregate level_averages and scale_deltas.
    levels: subset of ["R1","R2","R3","R4"]; default all. Returns (all_units, book_profile).
    """
    _here = Path(__file__).resolve().parent
    root = _here.parent
    assets = assets_root or root / "hesperia_lex" / "curated"
    # Prefer v06 dict when available so per-segment counts match main analyze (lemma-keyed tokens).
    v06_path = (Path(assets) / "v06" / "dict_a_v06.jsonl") if assets else None
    if v06_path and v06_path.exists():
        dict_a = dict_a or load_dict_a_v06(assets) or {}
    else:
        dict_a = dict_a or load_dict_a_v033(assets_root=assets) or {}
    dict_b = dict_b or load_dict_b_v033(assets_root=assets) or {}
    surface_map = load_dict_a_surface_map_v033(assets_root=assets) or None
    defaults = load_defaults()
    F = int(defaults.get("F", 288))
    A = int(defaults.get("A", 12))
    eps = float(defaults.get("eps", 1e-9))
    D = int(defaults.get("MAX_ALLOWED_DEPTH", 8))
    metric_keys = ["coverage", "dominance", "entropy", "leakage", "contradiction_pressure", "stability", "shadow_deviation"]
    if levels is None:
        levels = ["R1", "R2", "R3", "R4"]

    all_units = []
    by_level = {"R1": [], "R2": [], "R3": [], "R4": []}

    if "R1" in levels:
        spans = segment_by_sentences(text)
        units_r1 = _run_units_for_spans(
            text, spans, "R1", None, "R1:sent", dict_a, dict_b, defaults, F, A, eps, D, surface_map=surface_map
        )
        by_level["R1"] = units_r1
        all_units.extend(units_r1)

    if "R2" in levels:
        spans = segment_by_paragraphs(text)
        if spans:
            units_r2 = _run_units_for_spans(
                text, spans, "R2", None, "R2:para", dict_a, dict_b, defaults, F, A, eps, D, surface_map=surface_map
            )
            by_level["R2"] = units_r2
            all_units.extend(units_r2)

    if "R3" in levels:
        spans = segment_by_chapters(text)
        if spans:
            units_r3 = _run_units_for_spans(
                text, spans, "R3", None, "R3:ch", dict_a, dict_b, defaults, F, A, eps, D, surface_map=surface_map
            )
            by_level["R3"] = units_r3
            all_units.extend(units_r3)

    if "R4" in levels:
        spans = segment_by_book(text)
        if spans:
            units_r4 = _run_units_for_spans(
                text, spans, "R4", None, "R4:book", dict_a, dict_b, defaults, F, A, eps, D, surface_map=surface_map
            )
            by_level["R4"] = units_r4
            all_units.extend(units_r4)

    level_averages = {
        "R1": _aggregate_level(by_level["R1"], metric_keys),
        "R2": _aggregate_level(by_level["R2"], metric_keys),
        "R3": _aggregate_level(by_level["R3"], metric_keys),
        "R4": _aggregate_level(by_level["R4"], metric_keys),
    }
    esm = load_r1_r4_esm_defaults()
    scale_deltas = _compute_scale_deltas(level_averages, metric_keys, esm)

    stable_families = []
    for u in all_units[:30]:
        for tf in u.get("top_families", [])[:1]:
            fid = tf.get("family_id")
            if fid and fid not in stable_families:
                stable_families.append(fid)
    book_profile = {
        "book_id": book_id,
        "level_averages": level_averages,
        "scale_deltas": scale_deltas,
        "turning_points": [],
        "structural_signature": {
            "stable_families": stable_families[:20],
            "variance_profile": {},
            "author_fingerprint": {},
        },
    }
    return all_units, book_profile


def run_r1_pipeline(
    text: str,
    book_id: str = "book",
    dict_a: dict | None = None,
    dict_b: dict | None = None,
    assets_root: Path | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """
    Run R1 (sentence-level) pipeline: segment text into sentences, run L1–L9 per sentence, build Units, aggregate BookProfile.
    Returns (units, book_profile).
    """
    _here = Path(__file__).resolve().parent
    root = _here.parent
    assets = assets_root or root / "hesperia_lex" / "curated"
    dict_a = dict_a or load_dict_a_v033(assets_root=assets) or {}
    dict_b = dict_b or load_dict_b_v033(assets_root=assets) or {}
    surface_map = load_dict_a_surface_map_v033(assets_root=assets) or None
    defaults = load_defaults()
    F = int(defaults.get("F", 288))
    A = int(defaults.get("A", 12))
    eps = float(defaults.get("eps", 1e-9))
    D = int(defaults.get("MAX_ALLOWED_DEPTH", 8))

    spans = segment_by_sentences(text)
    units = []
    metric_keys = ["coverage", "dominance", "entropy", "leakage", "contradiction_pressure", "stability", "shadow_deviation"]

    for i, span in enumerate(spans):
        segment_text = get_text_span(text, span)
        if not segment_text.strip():
            continue
        hits, L1, L2, L3, L4, L5, L6, L7 = _run_layers_for_text(
            segment_text, dict_a, dict_b, defaults, F, A, eps, D, surface_map=surface_map
        )
        token_count = sum(hits)
        unit_id = f"R1:sent_{i + 1}"
        unit = build_unit(unit_id, "R1", None, token_count, hits, L1, L2, L3, L4, L5, L6, L7, F=F, A=A)
        units.append(unit)

    r1_summary = _aggregate_level(units, metric_keys)
    level_averages = {
        "R1": r1_summary,
        "R2": _aggregate_level([], metric_keys),
        "R3": _aggregate_level([], metric_keys),
        "R4": _aggregate_level([], metric_keys),
    }
    scale_deltas = {
        "R1_to_R2": {"delta_observed": _zero_delta(metric_keys), "delta_expected": _zero_delta(metric_keys), "delta_deviation": _zero_delta(metric_keys)},
        "R2_to_R3": {"delta_observed": _zero_delta(metric_keys), "delta_expected": _zero_delta(metric_keys), "delta_deviation": _zero_delta(metric_keys)},
        "R3_to_R4": {"delta_observed": _zero_delta(metric_keys), "delta_expected": _zero_delta(metric_keys), "delta_deviation": _zero_delta(metric_keys)},
    }
    stable_families = []
    if units:
        seen = set()
        for u in units[:20]:
            for tf in u.get("top_families", [])[:1]:
                fid = tf.get("family_id")
                if fid and fid not in seen:
                    seen.add(fid)
                    stable_families.append(fid)
    book_profile = {
        "book_id": book_id,
        "level_averages": level_averages,
        "scale_deltas": scale_deltas,
        "turning_points": [],
        "structural_signature": {
            "stable_families": stable_families[:20],
            "variance_profile": {},
            "author_fingerprint": {},
        },
    }
    return units, book_profile


def run_r1_pipeline_to_json(
    text: str,
    book_id: str = "book",
    out_units: Path | None = None,
    out_profile: Path | None = None,
    out_units_jsonl: Path | None = None,
) -> dict[str, Any]:
    """Run R1 pipeline and optionally write units and book_profile to JSON. Returns {"units": [...], "book_profile": {...}}.
    If out_units_jsonl is set, write one unit per line (jsonl) for streaming/safe context (avoid large single JSON)."""
    units, book_profile = run_r1_pipeline(text, book_id=book_id)
    result = {"units": units, "book_profile": book_profile}
    if out_units:
        out_units.parent.mkdir(parents=True, exist_ok=True)
        out_units.write_text(json.dumps(units, indent=2), encoding="utf-8")
    if out_units_jsonl:
        out_units_jsonl.parent.mkdir(parents=True, exist_ok=True)
        with open(out_units_jsonl, "w", encoding="utf-8") as f:
            for u in units:
                f.write(json.dumps(u, ensure_ascii=False) + "\n")
    if out_profile:
        out_profile.parent.mkdir(parents=True, exist_ok=True)
        out_profile.write_text(json.dumps(book_profile, indent=2), encoding="utf-8")
    return result


def run_full_pipeline_to_json(
    text: str,
    book_id: str = "book",
    levels: list[str] | None = None,
    out_units: Path | None = None,
    out_profile: Path | None = None,
    out_units_jsonl: Path | None = None,
    validate: bool = False,
) -> dict[str, Any]:
    """Run full R1–R4 pipeline; optionally write and validate. Returns {"units": [...], "book_profile": {...}, "validation": {...}}.
    If out_units_jsonl is set, write one unit per line (jsonl) for streaming/safe context (avoid large single JSON)."""
    units, book_profile = run_full_pipeline(text, book_id=book_id, levels=levels)
    result = {"units": units, "book_profile": book_profile}
    if out_units:
        out_units.parent.mkdir(parents=True, exist_ok=True)
        out_units.write_text(json.dumps(units, indent=2), encoding="utf-8")
    if out_units_jsonl:
        out_units_jsonl.parent.mkdir(parents=True, exist_ok=True)
        with open(out_units_jsonl, "w", encoding="utf-8") as f:
            for u in units:
                f.write(json.dumps(u, ensure_ascii=False) + "\n")
    if out_profile:
        out_profile.parent.mkdir(parents=True, exist_ok=True)
        out_profile.write_text(json.dumps(book_profile, indent=2), encoding="utf-8")
    if validate:
        result["validation"] = _validate_units_and_profile(units, book_profile)
    return result


def _validate_units_and_profile(units: list[dict], book_profile: dict) -> dict[str, Any]:
    """Validate units and book_profile against Part C schemas if jsonschema available. Returns {"units_ok": bool, "profile_ok": bool, "errors": [...]}."""
    try:
        import jsonschema
    except ImportError:
        return {"units_ok": None, "profile_ok": None, "errors": ["jsonschema not installed; skip validation"]}
    _here = Path(__file__).resolve().parent
    root = _here.parent
    schema_dir = root / "schema"
    errors = []
    unit_ok = True
    for i, u in enumerate(units):
        try:
            with open(schema_dir / "Unit.schema.json", encoding="utf-8") as f:
                schema = json.load(f)
            jsonschema.validate(u, schema)
        except Exception as e:
            unit_ok = False
            errors.append(f"Unit[{i}] {u.get('unit_id', i)}: {e}")
    profile_ok = True
    try:
        with open(schema_dir / "BookProfile.schema.json", encoding="utf-8") as f:
            schema = json.load(f)
        jsonschema.validate(book_profile, schema)
    except Exception as e:
        profile_ok = False
        errors.append(f"BookProfile: {e}")
    return {"units_ok": unit_ok, "profile_ok": profile_ok, "errors": errors}
