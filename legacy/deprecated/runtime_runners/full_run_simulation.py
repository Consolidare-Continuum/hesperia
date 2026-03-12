#!/usr/bin/env python3
"""
HESPERIA v0.3 — full run simulation. Wires fusion → centroid → base traversal
→ aggregation → penalties → metrics. Uses stub topology (or optional S/L from files).
Output: JSON (resolution, metrics, degraded, invariants).
Run from repo root or CLIENTS/hesperia: python3 sphere_rag/full_run_simulation.py [--S path] [--L path] [--out path]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

# Allow running from repo root or from CLIENTS/hesperia
_SCRIPT_DIR = Path(__file__).resolve().parent
if _SCRIPT_DIR.name == "sphere_rag":
    _HESPERIA_ROOT = _SCRIPT_DIR.parent
else:
    _HESPERIA_ROOT = _SCRIPT_DIR

sys.path.insert(0, str(_HESPERIA_ROOT))

from core.math.core_math_legacy import (
    load_config,
    validate_config,
    fusion,
    centroid_indices,
    base_step,
    ambiguity_penalty,
    thin_core_penalty,
    dispersion_penalty,
    guard_penalty,
    P_shadow_value,
    metric_governance,
    metric_loopability,
    metric_tension_energy,
    metric_obstacle_score,
    aggregate_dominant_family_area,
    check_conservation_pre_decay,
    check_shadow_non_creation,
    make_demo_W,
)

try:
    from core.math.core_math_legacy import HAS_NUMPY
except Exception:
    HAS_NUMPY = False


def build_stub_topology(n_sides: int = 72, n_areas: int = 12, n_families_per_area: int = 6) -> tuple[dict[int, list[int]], dict[int, list[int]]]:
    """Build sides_of_family and families_of_area for a ring: area 0..n_areas-1, each with n_families_per_area families; sides 0..n_sides-1 assigned round-robin to families."""
    sides_per_family = max(1, n_sides // (n_areas * n_families_per_area))
    sides_of_family: dict[int, list[int]] = {}
    families_of_area: dict[int, list[int]] = {a: [] for a in range(n_areas)}
    side = 0
    for area_id in range(n_areas):
        for f_local in range(n_families_per_area):
            family_id = area_id * n_families_per_area + f_local
            sides_of_family[family_id] = []
            for _ in range(sides_per_family):
                if side < n_sides:
                    sides_of_family[family_id].append(side)
                    side += 1
            if sides_of_family[family_id]:
                families_of_area[area_id].append(family_id)
    return sides_of_family, families_of_area


def run_full(
    S: list[float],
    L: list[float],
    sides_of_family: dict[int, list[int]],
    families_of_area: dict[int, list[int]],
    cfg: dict,
) -> dict:
    n = len(S)
    assert n == len(L), "S and L length must match"
    E0 = fusion(S, L, cfg)
    sumS = sum(S)
    sumL = sum(L)
    C = centroid_indices(E0, cfg)
    no_centroid = len(C) == 0

    W = make_demo_W(n)
    E = E0[:]
    conservation_failures = 0
    for _ in range(cfg["T_steps"]):
        E, cons_ok = base_step(E, W, cfg)
        if not cons_ok:
            conservation_failures += 1
    E_end = E if not HAS_NUMPY else [float(x) for x in E]

    P_amb, gap, amb_degraded = ambiguity_penalty(E0, cfg)
    P_thin, core_share, thin_degraded = thin_core_penalty(sumS, sumL, cfg)
    P_disp = dispersion_penalty(E_end, cfg)
    guard_count = 0
    P_guard = guard_penalty(0, 0, 0, cfg)
    shadow_hops = 0
    P_shadow = P_shadow_value(shadow_hops, cfg)

    dom_family, dom_area, F, A = aggregate_dominant_family_area(
        E_end, E0, C, sides_of_family, families_of_area, cfg
    )
    F_list = list(F.values()) if F else [0.0]
    gov = metric_governance(P_amb, P_thin, P_shadow, P_disp, P_guard)
    loop = metric_loopability(E_end, C, cfg)
    tension = metric_tension_energy(F_list, cfg)
    obstacle = metric_obstacle_score(E0, E_end, guard_count, shadow_hops, cfg)

    return {
        "resolution": {
            "dominant_family_id": dom_family,
            "dominant_area_id": dom_area,
            "centroid_indices": C,
            "no_centroid": no_centroid,
        },
        "metrics": {
            "governance": gov,
            "loopability": loop,
            "tension_energy": tension,
            "obstacle_score": obstacle,
        },
        "penalties": {"P_amb": P_amb, "P_thin": P_thin, "P_disp": P_disp, "P_shadow": P_shadow, "P_guard": P_guard},
        "degraded": {
            "ambiguity": amb_degraded,
            "thin_core": thin_degraded,
            "no_centroid": no_centroid,
            "shadow_overuse": False,
        },
        "invariants": {
            "conservation_ok": check_conservation_pre_decay(E0, W, cfg),
            "shadow_non_creation_ok": check_shadow_non_creation(E0, W, cfg),
            "conservation_failures_during_traversal": conservation_failures,
        },
        "config_source": "guard_config_v1.json or defaults",
        "shadow_hops": shadow_hops,
        "shadow_triggers": [],
        "topology_source": "stub",
        "acceptance": {
            "shadow_hops_ok": shadow_hops <= cfg.get("max_shadow_hops", 2),
            "conservation_ok": conservation_failures == 0,
        },
    }


def main() -> int:
    import random
    random.seed(0)

    ap = argparse.ArgumentParser(description="HESPERIA v0.3 full run simulation")
    ap.add_argument("--S", type=Path, help="JSON array of core seed mass per side (Dict A)")
    ap.add_argument("--L", type=Path, help="JSON array of landing mass per side (Dict B)")
    ap.add_argument("--n-sides", type=int, default=72, help="Stub topology size (default 72)")
    ap.add_argument("--out", type=Path, help="Write result JSON here")
    args = ap.parse_args()

    cfg = load_config(_HESPERIA_ROOT / "guard_config_v1.json")
    errs = validate_config(cfg)
    if errs:
        print("Config validation failed:", errs, file=sys.stderr)
        return 1

    n = args.n_sides
    if args.S is not None:
        with open(args.S, encoding="utf-8") as f:
            S = json.load(f)
        n = len(S)
    else:
        S = [0.0] * n
        S[0], S[1], S[2] = 1.0, 0.5, 0.2
    if args.L is not None:
        with open(args.L, encoding="utf-8") as f:
            L = json.load(f)
        if len(L) != n:
            print("L length must match S (or n_sides)", file=sys.stderr)
            return 1
    else:
        L = [0.0] * n
        L[0], L[1], L[3], L[4] = 0.3, 0.6, 0.1, 0.05

    sides_of_family, families_of_area = build_stub_topology(n_sides=n, n_areas=12, n_families_per_area=6)
    # Trim to actual n sides: only keep sides < n
    sides_of_family = {f: [i for i in sides if i < n] for f, sides in sides_of_family.items() if any(i < n for i in sides)}
    families_of_area = {a: [f for f in fams if f in sides_of_family] for a, fams in families_of_area.items()}

    result = run_full(S, L, sides_of_family, families_of_area, cfg)
    # Audit-friendly outputs (v0.3 contract)
    assets_dir = _HESPERIA_ROOT / "assets"
    cfg_path = _HESPERIA_ROOT / "guard_config_v1.json"
    config_hash = hashlib.sha256((cfg_path.read_bytes() if cfg_path.exists() else b"") + json.dumps(cfg, sort_keys=True).encode()).hexdigest()
    result["config_hash"] = config_hash
    lex_versions = {}
    for name in ("A_CORE_STAR_MAP_v1.json", "B_SURFACE_LEX_FIELD_v1.json"):
        p = assets_dir / name
        if p.exists():
            lex_versions[name] = hashlib.sha256(p.read_bytes()).hexdigest()
    result["lex_versions"] = lex_versions
    result["books_enabled"] = False

    out_json = json.dumps(result, indent=2, sort_keys=True)

    if args.out:
        args.out.write_text(out_json, encoding="utf-8")
        print("Wrote", args.out, file=sys.stderr)
    else:
        print(out_json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
