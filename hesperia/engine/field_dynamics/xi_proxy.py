# HESPERIA — RAD. Ξ / L3 tension proxy → L7 contradiction drive (Ethan compact H8).
# Full Ξ = Σ K_ij c_i c_j − ω Σ W_ij c_i c_j requires graph state; TRIZ rows proxy tension.

from __future__ import annotations

from typing import Any

NUM_AREAS = 12


def _xi_scale_from_env() -> float:
    import os

    v = os.environ.get("HESPERIA_FIELD_DYNAMICS_XI_SCALE", "").strip()
    if not v:
        return 0.14
    try:
        return max(0.0, min(0.5, float(v)))
    except (TypeError, ValueError):
        return 0.14


def xi_proxy_from_triz_rows(rows: list[dict[str, Any]]) -> tuple[float, list[float]]:
    """
    Global tension scalar + per-area profile from contradiction topology rows.
    Returns (xi_global in [0,1], xi_area[12] normalized peak=1).
    """
    if not rows:
        return 0.0, [0.0] * NUM_AREAS
    total_score = 0.0
    per = [0.0] * NUM_AREAS
    for r in rows:
        try:
            sc = min(1.0, max(0.0, float(r.get("score") or 0.0)))
        except (TypeError, ValueError):
            sc = 0.0
        total_score += sc
        for ak in ("area_a", "area_b"):
            a = r.get(ak)
            if isinstance(a, int) and 0 <= a < NUM_AREAS:
                per[a] += sc
    xi_global = min(1.0, total_score / max(8.0, float(len(rows))))
    m = max(per) if per else 0.0
    if m <= 0:
        pern = [0.0] * NUM_AREAS
    else:
        pern = [min(1.0, x / m) for x in per]
    return xi_global, pern


def apply_xi_to_contradiction_signal(
    c_sig_12: list[float],
    triz_rows: list[dict[str, Any]],
    *,
    xi_scale: float | None = None,
) -> tuple[list[float], dict[str, Any]]:
    """
    Boost L7 area contradiction drive toward TRIZ-localized tension (Ξ proxy).
    ``xi_scale``: if None, uses env ``HESPERIA_FIELD_DYNAMICS_XI_SCALE`` (default 0.14).
    """
    xs = float(xi_scale) if xi_scale is not None else _xi_scale_from_env()
    g, per = xi_proxy_from_triz_rows(triz_rows)
    meta = {
        "xi_proxy_global": round(g, 6),
        "xi_scale": round(xs, 6),
    }
    if not triz_rows:
        return list(c_sig_12), meta
    out = []
    for a in range(NUM_AREAS):
        boost = xs * (0.35 * g + 0.65 * per[a])
        out.append(min(1.0, max(0.0, float(c_sig_12[a]) + boost)))
    return out, meta


def field_dynamics_xi_enabled() -> bool:
    import os

    v = os.environ.get("HESPERIA_FIELD_DYNAMICS_XI", "1").strip().lower()
    return v not in ("0", "false", "no")
