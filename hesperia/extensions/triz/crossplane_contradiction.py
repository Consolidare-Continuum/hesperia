# HESPERIA — Cross-plane contradiction package (deterministic, v0.5.8 task4).
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

from __future__ import annotations

import math
from typing import Any

from hesperia.engine.tfp_signal_calibration import load_tfp_signal_calibration
from hesperia.extensions.triz.contradiction_coupling import build_area_contradiction_pressure
from hesperia.ontology.dictB.loader import build_concept_to_area_family

_EPS = 1e-15
CROSSPLANE_VERSION = "tfp_v0_5_8_task4"


def _clamp01(x: float) -> float:
    if not math.isfinite(x):
        return 0.0
    return max(0.0, min(1.0, float(x)))


def _mean(xs: list[float]) -> float:
    if not xs:
        return 0.0
    return float(sum(xs)) / float(len(xs))


def _variance(xs: list[float]) -> float:
    if len(xs) < 2:
        return 0.0
    m = _mean(xs)
    return float(sum((x - m) ** 2 for x in xs)) / float(len(xs))


def build_crossplane_contradiction_package(
    activation: dict[str, Any],
    topology: dict[str, Any] | None,
    contradictions: list[dict[str, Any]] | None,
    *,
    concept_to_area_family: dict[str, tuple[str, str]] | None = None,
) -> dict[str, Any]:
    """
    Single canonical contradiction signal for DLCR / sealed multiscale / product (04/05/06),
    aligned with topology (09) when ``topology`` is supplied.
    """
    cfg = load_tfp_signal_calibration()
    area_ids = [str(x) for x in (cfg.get("area_ids") or [])]
    af = concept_to_area_family if concept_to_area_family is not None else build_concept_to_area_family()
    topo = topology or {}

    rows = list(contradictions) if contradictions else []
    coupling_active = bool(activation.get("contradiction_coupling_active"))
    pressure_act = activation.get("contradiction_pressure") or {}
    area_pressure: dict[str, float] = {a: float(pressure_act.get(a, 0.0)) for a in area_ids}
    if rows:
        area_pressure = build_area_contradiction_pressure(rows, af, area_ids)

    seg_loads_raw = topo.get("segment_contradiction_loads") or []
    segment_contradiction_loads: list[dict[str, Any]] = []
    for item in seg_loads_raw:
        if isinstance(item, dict):
            segment_contradiction_loads.append(dict(sorted(item.items())))

    transition_pressure = [float(x) for x in (topo.get("transition_pressure") or []) if isinstance(x, (int, float))]

    loads_norm = [
        _clamp01(float(s.get("contradiction_load_normalized") or s.get("contradiction_load") or 0.0))
        for s in segment_contradiction_loads
    ]
    if not loads_norm and rows:
        g_fallback = _clamp01(max(area_pressure.values()) if area_pressure else 0.0)
        loads_norm = [g_fallback]

    global_contradiction_load = _clamp01(_mean(loads_norm) if loads_norm else max(area_pressure.values()) if area_pressure else 0.0)

    cross_mass_sum = 0.0
    load_sum = 0.0
    for s in segment_contradiction_loads:
        cross_mass_sum += float(s.get("cross_area_contradiction_mass") or 0.0)
        load_sum += float(s.get("contradiction_load") or 0.0)
    if segment_contradiction_loads and load_sum > _EPS:
        cross_area_contradiction_mass = _clamp01(cross_mass_sum / load_sum)
    elif rows:
        cross_area_contradiction_mass = _clamp01(
            min(1.0, sum(area_pressure.values()) / (len(area_ids) * max(1.0, float(len(rows)))))
        )
    else:
        cross_area_contradiction_mass = 0.0

    var_l = _variance(loads_norm)
    mean_tp = _mean(transition_pressure) if transition_pressure else 0.0
    escalation = 0.0
    if len(loads_norm) >= 2:
        for i in range(1, len(loads_norm)):
            if loads_norm[i] > loads_norm[i - 1] + 1e-12:
                escalation += loads_norm[i] - loads_norm[i - 1]
        escalation = _clamp01(escalation / float(len(loads_norm) - 1))

    contradiction_stability_index = _clamp01(
        1.0
        - min(
            1.0,
            0.42 * mean_tp + 0.28 * min(1.0, var_l * 4.0) + 0.15 * escalation + 0.15 * global_contradiction_load,
        )
    )

    topo_summary = (topo.get("curve_projection_meta") or {}).get("contradiction_summary") or {}
    topo_coupling_flag = bool(topo_summary.get("contradiction_coupling_active")) if topo_summary else bool(
        segment_contradiction_loads and rows
    )
    if not rows:
        contradiction_coherence_flag = True
    elif segment_contradiction_loads:
        contradiction_coherence_flag = bool(coupling_active == topo_coupling_flag)
    else:
        contradiction_coherence_flag = bool(coupling_active)

    out: dict[str, Any] = {
        "crossplane_version": CROSSPLANE_VERSION,
        "global_contradiction_load": round(global_contradiction_load, 6),
        "area_contradiction_pressure": {k: round(float(v), 6) for k, v in sorted(area_pressure.items())},
        "cross_area_contradiction_mass": round(float(cross_area_contradiction_mass), 6),
        "segment_contradiction_loads": segment_contradiction_loads,
        "transition_pressure": [round(float(x), 6) for x in transition_pressure],
        "contradiction_stability_index": round(contradiction_stability_index, 6),
        "contradiction_coherence_flag": bool(contradiction_coherence_flag),
        "contradiction_coupling_active": bool(coupling_active or (rows and max(area_pressure.values(), default=0.0) > _EPS)),
    }
    return out
