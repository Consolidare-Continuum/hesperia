from __future__ import annotations

import hashlib
from dataclasses import dataclass

from .geometry import AREAS, FAMILIES_PER_AREA, TOTAL_FAMILIES, SideCoord, area_left, area_right, side_id_from_coord
from .metrics import RegionMetrics, bridge_retention_ratio, intersection_matrix, region_metrics
from .semantic_engine import SeedResult


def _stable_u32(text: str) -> int:
    h = hashlib.sha256(text.encode("utf-8")).digest()
    return int.from_bytes(h[:4], "big", signed=False)


@dataclass(frozen=True, slots=True)
class PhasePolicy:
    # Phase I traversal
    max_passes: int = 3
    steps_per_pass: int = 12
    families_per_step: int = 3
    sides_per_family_step: int = 2
    cross_area_bonus_tau: float = 0.15
    new_family_bonus_tau: float = 0.10

    # Flood thresholds (fixed policy defaults; override via CLI if needed)
    theta_loopability: float = 0.10
    theta_tension: float = 0.35
    theta_coherence: float = 0.15

    # Phase II cut
    alpha: float = 0.50
    alpha_step_delta: float = 0.05
    max_cut_iters: int = 6
    c_min: float = 0.10
    theta_contradiction: float = 1.0


@dataclass(frozen=True, slots=True)
class FloodEvent:
    triggered: bool
    reason: str | None
    at_pass: int | None
    at_step: int | None
    metrics: RegionMetrics
    loopability: float


@dataclass(frozen=True, slots=True)
class PhaseIResult:
    region_weights: dict[int, float]
    metrics_history: list[dict]
    flood: FloodEvent
    pass_paths: list[dict]


@dataclass(frozen=True, slots=True)
class CutResult:
    alpha_used: float
    total_truth_mass: float
    kept_truth_mass: float
    kept_ratio: float
    k_star: int
    core_weights: dict[int, float]
    reverted: bool
    revert_reason: str | None


@dataclass(frozen=True, slots=True)
class PhaseIIResult:
    metrics_core: RegionMetrics
    stability_score: float
    intersection_before: list[list[int]]
    intersection_after: list[list[int]]
    bridge_retention_ratio: float


@dataclass(frozen=True, slots=True)
class PhaseRunResult:
    seed: SeedResult
    phase_i: PhaseIResult
    cut: CutResult
    phase_ii: PhaseIIResult
    invariants: dict


def _direction_for_pass(pass_idx_1based: int, novelty_cw: int, novelty_ccw: int) -> int:
    if pass_idx_1based == 1:
        return 1
    if pass_idx_1based == 2:
        return -1
    return 1 if novelty_cw >= novelty_ccw else -1


def _area_at(start_area: int, direction: int, step: int) -> int:
    return (start_area + direction * step + AREAS) % AREAS


def _top_families_in_area(family_mass: list[float], area_id: int, k: int) -> list[int]:
    start = area_id * FAMILIES_PER_AREA
    fams = list(range(start, start + FAMILIES_PER_AREA))
    fams.sort(key=lambda f: (family_mass[f], -f), reverse=True)
    # Filter to positive mass first; if none, deterministic fallback later.
    top = [f for f in fams if family_mass[f] > 0.0][:k]
    return top


def _add_side(region: dict[int, float], side_id: int, delta_tau: float) -> bool:
    """Add or strengthen a side. Returns True iff this is a new side."""
    if delta_tau <= 0:
        return False
    if side_id not in region:
        region[side_id] = min(1.0, delta_tau)
        return True
    region[side_id] = min(1.0, region[side_id] + delta_tau)
    return False


def run_phase_i(seed: SeedResult, policy: PhasePolicy) -> PhaseIResult:
    region: dict[int, float] = {s.side_id: s.w for s in seed.seed_sides}
    metrics_history: list[dict] = []
    pass_paths: list[dict] = []

    novelty_cw = 0
    novelty_ccw = 0
    prev_ent = None
    prev_coh = None

    flood_reason: str | None = None
    flood_at_pass: int | None = None
    flood_at_step: int | None = None
    flood_metrics: RegionMetrics | None = None
    flood_loopability: float = 1.0

    for p in range(1, max(1, policy.max_passes) + 1):
        direction = _direction_for_pass(p, novelty_cw, novelty_ccw)
        start_area = seed.start_area_id
        pass_road: list[dict] = []

        new_hits_this_pass = 0
        for t in range(policy.steps_per_pass):
            current_area = _area_at(start_area, direction, t)

            m = region_metrics(region)
            top = _top_families_in_area(m.family_mass, current_area, policy.families_per_step)
            if not top:
                fallback_local = (t + (p * 13)) % FAMILIES_PER_AREA
                top = [current_area * FAMILIES_PER_AREA + fallback_local]

            step_new = 0
            for rank, fam_global in enumerate(top):
                family_local = fam_global % FAMILIES_PER_AREA
                # Deterministic side selection per (pass, step, family, rank).
                hex_index = _stable_u32(f"p{p}|t{t}|f{fam_global}|r{rank}|hex") % 250
                for sidx in range(policy.sides_per_family_step):
                    side_index = (sidx + _stable_u32(f"p{p}|t{t}|f{fam_global}|r{rank}|s{sidx}") % 6) % 6
                    side_id = side_id_from_coord(current_area, family_local, hex_index, side_index)
                    if _add_side(region, side_id, delta_tau=0.25):
                        step_new += 1

                # New family discovery (adjacent family in same area)
                next_local = (family_local + 1) % FAMILIES_PER_AREA
                side_nf = side_id_from_coord(
                    current_area,
                    next_local,
                    hex_index,
                    _stable_u32(f"p{p}|t{t}|nf") % 6,
                )
                if _add_side(region, side_nf, delta_tau=policy.new_family_bonus_tau):
                    step_new += 1

                # Cross-area movement: propagate same family_local to left/right area.
                left_area = area_left(current_area)
                right_area = area_right(current_area)
                side_la = side_id_from_coord(
                    left_area,
                    family_local,
                    hex_index,
                    _stable_u32(f"p{p}|t{t}|la") % 6,
                )
                side_ra = side_id_from_coord(
                    right_area,
                    family_local,
                    hex_index,
                    _stable_u32(f"p{p}|t{t}|ra") % 6,
                )
                if _add_side(region, side_la, delta_tau=policy.cross_area_bonus_tau):
                    step_new += 1
                if _add_side(region, side_ra, delta_tau=policy.cross_area_bonus_tau):
                    step_new += 1

            new_hits_this_pass += step_new

            # Deterministic bookkeeping for "paths of each traversal".
            pass_road.append({"pass": p, "step": t, "area_id": current_area, "new_sides": step_new})

            # Metrics + flood check at each step.
            m2 = region_metrics(region)
            loopability = (new_hits_this_pass / (t + 1)) if (t + 1) else 0.0
            metrics_history.append(
                {
                    "pass": p,
                    "step": t,
                    "active_sides": m2.active_sides,
                    "entropy_a": m2.entropy_a,
                    "coherence": m2.coherence,
                    "tension_energy": m2.tension_energy,
                    "loopability": loopability,
                    "frag_index": m2.frag_index,
                }
            )

            ent_incr_coh_decr = (
                (prev_ent is not None and prev_coh is not None and (m2.entropy_a > prev_ent) and (m2.coherence < prev_coh))
            )
            prev_ent, prev_coh = m2.entropy_a, m2.coherence

            if (
                loopability < policy.theta_loopability
                or m2.tension_energy > policy.theta_tension
                or m2.coherence < policy.theta_coherence
                or ent_incr_coh_decr
            ):
                if flood_reason is None:
                    if loopability < policy.theta_loopability:
                        flood_reason = "loopability_below_threshold"
                    elif m2.tension_energy > policy.theta_tension:
                        flood_reason = "tension_energy_above_threshold"
                    elif m2.coherence < policy.theta_coherence:
                        flood_reason = "coherence_below_threshold"
                    else:
                        flood_reason = "entropy_increasing_while_coherence_decreasing"
                    flood_at_pass = p
                    flood_at_step = t
                    flood_metrics = m2
                    flood_loopability = loopability
                break

        pass_paths.append({"pass": p, "direction": direction, "start_area_id": seed.start_area_id, "road": pass_road})

        # Novelty proxy per pass (deterministic): new sides discovered.
        if direction == 1:
            novelty_cw += new_hits_this_pass
        else:
            novelty_ccw += new_hits_this_pass

        if flood_reason is not None:
            break

    if flood_metrics is None:
        flood_metrics = region_metrics(region)
        flood_loopability = 1.0

    flood = FloodEvent(
        triggered=flood_reason is not None,
        reason=flood_reason,
        at_pass=flood_at_pass,
        at_step=flood_at_step,
        metrics=flood_metrics,
        loopability=flood_loopability,
    )
    return PhaseIResult(region_weights=region, metrics_history=metrics_history, flood=flood, pass_paths=pass_paths)


def waterline_cut(
    region_weights: dict[int, float],
    *,
    alpha: float,
) -> tuple[dict[int, float], dict]:
    items = sorted(region_weights.items(), key=lambda kv: (kv[1], -kv[0]), reverse=True)
    total = sum(w for _, w in items)
    if total <= 0:
        return {}, {"k_star": 0, "total_truth_mass": 0.0, "kept_truth_mass": 0.0, "kept_ratio": 1.0}
    target = max(0.0, min(1.0, alpha)) * total
    kept: dict[int, float] = {}
    cum = 0.0
    k_star = 0
    for side_id, w in items:
        if cum >= target and k_star > 0:
            break
        kept[side_id] = w
        cum += w
        k_star += 1
    return kept, {
        "k_star": k_star,
        "total_truth_mass": total,
        "kept_truth_mass": cum,
        "kept_ratio": (cum / total) if total else 1.0,
    }


def run_phase_ii_with_reverts(phase_i: PhaseIResult, policy: PhasePolicy) -> tuple[CutResult, PhaseIIResult]:
    before_metrics = phase_i.flood.metrics
    i_before = intersection_matrix(set(phase_i.region_weights.keys()))

    alpha = policy.alpha
    reverted = False
    revert_reason: str | None = None
    last_core: dict[int, float] = {}
    last_meta: dict = {}

    for _ in range(max(1, policy.max_cut_iters)):
        core, meta = waterline_cut(phase_i.region_weights, alpha=alpha)
        m_core = region_metrics(core)

        # Required properties after cut (no heuristics; but revert if violated).
        if (
            m_core.coherence + 1e-12 < before_metrics.coherence
            or m_core.entropy_a > before_metrics.entropy_a + 1e-12
            or m_core.tension_energy > before_metrics.tension_energy + 1e-12
        ):
            reverted = True
            revert_reason = "cut_too_aggressive_metrics_regressed"
            alpha = min(0.95, alpha + policy.alpha_step_delta)
            last_core, last_meta = core, meta
            continue

        # Revert condition (contradictionScore not yet wired; deterministic placeholder = 0.0).
        contradiction_score = 0.0
        if m_core.coherence < policy.c_min or contradiction_score > policy.theta_contradiction:
            reverted = True
            revert_reason = "core_below_minimum_or_contradiction"
            alpha = min(0.95, alpha + policy.alpha_step_delta)
            last_core, last_meta = core, meta
            continue

        # Stable.
        i_after = intersection_matrix(set(core.keys()))
        br = bridge_retention_ratio(i_before, i_after)
        stability = m_core.coherence * (1.0 - min(1.0, m_core.tension_energy))
        cut = CutResult(
            alpha_used=alpha,
            total_truth_mass=float(meta["total_truth_mass"]),
            kept_truth_mass=float(meta["kept_truth_mass"]),
            kept_ratio=float(meta["kept_ratio"]),
            k_star=int(meta["k_star"]),
            core_weights=core,
            reverted=reverted,
            revert_reason=revert_reason,
        )
        p2 = PhaseIIResult(
            metrics_core=m_core,
            stability_score=stability,
            intersection_before=i_before,
            intersection_after=i_after,
            bridge_retention_ratio=br,
        )
        return cut, p2

    # If never stable, return last attempt (deterministic).
    core = last_core
    meta = last_meta or {"k_star": 0, "total_truth_mass": 0.0, "kept_truth_mass": 0.0, "kept_ratio": 0.0}
    m_core = region_metrics(core)
    i_after = intersection_matrix(set(core.keys()))
    br = bridge_retention_ratio(i_before, i_after)
    stability = m_core.coherence * (1.0 - min(1.0, m_core.tension_energy))
    cut = CutResult(
        alpha_used=alpha,
        total_truth_mass=float(meta["total_truth_mass"]),
        kept_truth_mass=float(meta["kept_truth_mass"]),
        kept_ratio=float(meta["kept_ratio"]),
        k_star=int(meta["k_star"]),
        core_weights=core,
        reverted=True,
        revert_reason=revert_reason or "max_cut_iters_exhausted",
    )
    p2 = PhaseIIResult(
        metrics_core=m_core,
        stability_score=stability,
        intersection_before=i_before,
        intersection_after=i_after,
        bridge_retention_ratio=br,
    )
    return cut, p2


def run_phases(seed: SeedResult, policy: PhasePolicy | None = None) -> PhaseRunResult:
    policy = policy or PhasePolicy()
    p1 = run_phase_i(seed, policy)
    cut, p2 = run_phase_ii_with_reverts(p1, policy)

    # Invariants (VII) — deterministic checks.
    before_w = sum(p1.region_weights.values())
    after_w = sum(cut.core_weights.values())
    before_side_ids = set(p1.region_weights.keys())
    after_side_ids = set(cut.core_weights.keys())
    before_areas = {SideCoord.from_side_id(s).area for s in before_side_ids}
    after_areas = {SideCoord.from_side_id(s).area for s in after_side_ids}
    before_fams = {SideCoord.from_side_id(s).family_global() for s in before_side_ids}
    after_fams = {SideCoord.from_side_id(s).family_global() for s in after_side_ids}

    invariants = {
        "truth_mass_ratio": (after_w / before_w) if before_w else 1.0,
        "truth_mass_preserved_ge_50pct": (after_w >= 0.5 * before_w) if before_w else True,
        "no_semantic_expansion": after_side_ids.issubset(before_side_ids),
        "area_count_non_increasing": len(after_areas) <= len(before_areas),
        "family_count_non_increasing": len(after_fams) <= len(before_fams),
        "phase2_loopability_core": 0.0,
    }
    return PhaseRunResult(seed=seed, phase_i=p1, cut=cut, phase_ii=p2, invariants=invariants)

