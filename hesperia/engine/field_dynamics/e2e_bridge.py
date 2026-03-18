# HESPERIA — RAD. E2E hook: hit-derived injection + optional L4→L5→L6 chain.

from __future__ import annotations

import json

import numpy as np
from dataclasses import replace
from pathlib import Path
from typing import Any

from hesperia.engine.field_dynamics.phase1 import field_dynamics_enabled, step_phase1
from hesperia.engine.field_dynamics.phase2 import field_dynamics_phase2_enabled, step_phase2
from hesperia.engine.field_dynamics.phase3 import (
    blend_hit_with_hex_area,
    blend_hit_with_hex_family,
    field_dynamics_hex_cap_from_env,
    field_dynamics_phase3_enabled,
    step_phase3,
)
from hesperia.engine.field_dynamics.phase4 import (
    apply_cluster_gravity_to_area_injection,
    apply_cluster_gravity_to_family_injection,
    clusters_to_public_rows,
    compute_l8_clusters,
    count_fronts_per_area,
    ephemeral_hex_from_hits,
    field_dynamics_phase4_enabled,
)
from hesperia.engine.field_dynamics.state import FieldDynamicsState, Phase1Theta, Phase3Theta, Phase4Theta

F_FAMILIES = 288
A_AREAS = 12
FAMILIES_PER_AREA = F_FAMILIES // A_AREAS  # 24


def _hits_288(text: str, assets_root: Path) -> list[int]:
    from core.attribution.structural import attribute, load_dict_a, load_dict_b, normalize, tokenize

    dict_a = load_dict_a(assets_root=assets_root) or {}
    dict_b = load_dict_b()
    tokens = tokenize(normalize(text))
    matched, _ = attribute(tokens, dict_a, dict_b)
    hits = [0] * F_FAMILIES
    for fg, _ in matched:
        if 0 <= fg < F_FAMILIES:
            hits[fg] += 1
    return hits


def area_injection_12_from_hits(hits: list[int]) -> list[float]:
    total = float(sum(hits))
    v = [0.0] * A_AREAS
    for f in range(F_FAMILIES):
        a = f // FAMILIES_PER_AREA
        if a < A_AREAS:
            v[a] += hits[f]
    if total > 0:
        return [x / total for x in v]
    return [1.0 / A_AREAS] * A_AREAS


def area_injection_12_from_text(text: str, assets_root: Path) -> list[float]:
    return area_injection_12_from_hits(_hits_288(text, assets_root))


def family_injection_288_from_hits(hits: list[int]) -> list[float]:
    total = float(sum(hits))
    if total > 0:
        return [h / total for h in hits]
    return [1.0 / F_FAMILIES] * F_FAMILIES


def family_injection_288_from_text(text: str, assets_root: Path) -> list[float]:
    return family_injection_288_from_hits(_hits_288(text, assets_root))


def default_state_path(out_dir: Path) -> Path:
    p = out_dir / "field_dynamics_state.json"
    env = __import__("os").environ.get("HESPERIA_FIELD_DYNAMICS_STATE_PATH", "").strip()
    return Path(env) if env else p


def run_field_dynamics_e2e_artifact(
    text: str,
    assets_root: Path,
    out_dir: Path,
    *,
    theta: Phase1Theta | None = None,
) -> dict[str, Any]:
    """
    Load prior state; optional L4 (Phase 3) → L5 (Phase 2) or L6 (Phase 1); persist.
    """
    if not field_dynamics_enabled():
        return {"_skipped": True, "reason": "HESPERIA_FIELD_DYNAMICS not set"}

    state_path = default_state_path(out_dir)
    state_path.parent.mkdir(parents=True, exist_ok=True)

    if state_path.exists():
        try:
            raw = json.loads(state_path.read_text(encoding="utf-8"))
            state = FieldDynamicsState.from_serializable(raw)
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            state = FieldDynamicsState.initial_uniform()
    else:
        state = FieldDynamicsState.initial_uniform()

    hits = _hits_288(text, assets_root)
    injection = area_injection_12_from_hits(hits)
    fam_inj = family_injection_288_from_hits(hits)

    import os

    use_triz = os.environ.get("HESPERIA_FIELD_DYNAMICS_TRIZ", "1").strip().lower() not in (
        "0",
        "false",
        "no",
    )
    triz_meta: dict[str, Any] = {}
    if use_triz:
        from hesperia.engine.field_dynamics.triz_signal import (
            contradiction_signal_12_from_con_rows,
            fetch_triz_contradiction_rows,
        )

        rows, triz_meta = fetch_triz_contradiction_rows(text)
        c_sig = contradiction_signal_12_from_con_rows(rows)
        from hesperia.engine.field_dynamics.xi_proxy import (
            apply_xi_to_contradiction_signal,
            field_dynamics_xi_enabled,
        )

        xi_meta: dict[str, Any] = {}
        if field_dynamics_xi_enabled() and rows:
            c_sig, xi_meta = apply_xi_to_contradiction_signal(c_sig, rows)
        triz_meta = {**triz_meta, **xi_meta}
    else:
        c_sig = [0.0] * A_AREAS
        triz_meta = {"triz_skipped": True}

    th3 = Phase3Theta(hex_cap=field_dynamics_hex_cap_from_env())
    th4 = Phase4Theta()
    p3 = field_dynamics_phase3_enabled()
    p4 = field_dynamics_phase4_enabled()
    p2 = field_dynamics_phase2_enabled()

    state_work = state
    stack: list[str] = []
    l8_rows: list[dict[str, Any]] = []
    fronts_12: list[int] = []
    new_l8_prev: dict[str, float] = dict(state.l8_cluster_mass_prev)

    if p3:
        state_work = step_phase3(state_work, hits, c_sig, theta=th3)
        stack.append("L4")
        w_blend = th3.hex_hit_blend
        fam_inj = blend_hit_with_hex_family(fam_inj, state_work.hex_x, w_blend)
        injection = blend_hit_with_hex_area(injection, state_work.hex_x, w_blend)

    if p4:
        hx = dict(state_work.hex_x) if p3 else ephemeral_hex_from_hits(hits, th4.ephemeral_cap)
        clusters, new_l8_prev = compute_l8_clusters(hx, state_work.l8_cluster_mass_prev, theta=th4)
        injection = apply_cluster_gravity_to_area_injection(injection, clusters, th4.gravity_epsilon)
        if p2:
            fam_inj = apply_cluster_gravity_to_family_injection(
                fam_inj, clusters, th4.gravity_epsilon * 0.85
            )
        l8_rows = clusters_to_public_rows(clusters)
        fronts_12 = count_fronts_per_area(hx)
        stack.append("L8")

    if p2:
        state_next = step_phase2(
            state_work,
            injection,
            fam_inj,
            contradiction_signal_area=c_sig,
            theta1=theta,
        )
        stack.extend(["L5", "L6"])
    else:
        state_next = step_phase1(state_work, injection, contradiction_signal=c_sig, theta=theta)
        stack.append("L6")

    phase_tag = 4 if p4 else (3 if p3 else (2 if p2 else 1))

    if p4:
        state_next = replace(state_next, l8_cluster_mass_prev=new_l8_prev)

    state_path.write_text(
        json.dumps(state_next.to_serializable(), indent=2),
        encoding="utf-8",
    )

    def _by_area(vec: list[float]) -> list[float]:
        out = []
        for a in range(A_AREAS):
            s = sum(float(vec[FAMILIES_PER_AREA * a + k]) for k in range(FAMILIES_PER_AREA))
            out.append(round(s, 6))
        return out

    out: dict[str, Any] = {
        "input": {
            "text_preview": text[:200] + ("..." if len(text) > 200 else ""),
            "length": len(text),
        },
        "HESPERIA_FIELD_DYNAMICS": True,
        "dynamics_phase": phase_tag,
        "dynamics_stack": "+".join(stack),
        "hex_cap": th3.hex_cap if p3 else None,
        "state_t": state_next.t,
        "delta_t": 1,
        "trend_window": [round(float(x), 6) for x in state_next.area_a.tolist()],
        "stability_window": [round(state_next.stab, 6)],
        "area_state": [round(float(x), 6) for x in state_next.area_a.tolist()],
        "area_pressure": [round(float(x), 6) for x in state_next.p_a.tolist()],
        "stab": round(state_next.stab, 6),
        "concept_mass": round(state_next.concept_mass, 6),
        "injection_12": [round(float(x), 6) for x in injection],
        "contradiction_signal_12": [round(float(x), 6) for x in c_sig],
        "triz_contradiction_meta": triz_meta,
        "state_path": str(state_path.resolve()),
    }
    if p3:
        hx = state_next.hex_x
        out["hex_active_count"] = len(hx)
        out["hex_field_peak"] = round(max(hx.values()), 6) if hx else 0.0
        out["hex_pressure_peak"] = round(max(state_next.hex_p.values()), 6) if state_next.hex_p else 0.0
    if p2:
        ff = state_next.f_f.tolist()
        pf = state_next.p_family.tolist()
        out["family_mass_by_area"] = _by_area([float(x) for x in ff])
        out["family_pressure_by_area"] = _by_area([float(x) for x in pf])
    if p4:
        out["l8_clusters"] = l8_rows
        out["l8_fronts_per_area"] = fronts_12
        out["l8_cluster_count"] = len(l8_rows)
        out["dominant_l8_cluster"] = l8_rows[0]["id"] if l8_rows else None

    if __import__("os").environ.get("HESPERIA_SEMANTIC_FIELD_EQUATIONS_V1", "").strip() in (
        "1",
        "true",
        "yes",
    ):
        from hesperia.engine.field_dynamics.semantic_field_v1 import semantic_field_e2e_bundle

        prev_ff = np.asarray(state.f_f, dtype=np.float64).reshape(F_FAMILIES)
        bundle = semantic_field_e2e_bundle(
            f0=prev_ff,
            source_288=fam_inj,
            hits_as_source=False,
            n_steps=int(__import__("os").environ.get("HESPERIA_SEMANTIC_FIELD_V1_STEPS", "1") or "1"),
        )
        out["SEMANTIC_FIELD_EQUATIONS_v1"] = True
        out["semantic_field_v1"] = bundle
    return out
