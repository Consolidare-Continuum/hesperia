from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class StopReason(str, Enum):
    NONE = "NONE"
    HALT = "HALT"
    ROLLBACK = "ROLLBACK"
    CORRECT = "CORRECT"
    REQUIRE_REVIEW = "REQUIRE_REVIEW"


@dataclass(slots=True)
class GammaState:
    hops: int = 0
    new_hits_total: int = 0
    drag_streak: int = 0
    obstacle: float = 0.0
    stop_reason: StopReason = StopReason.NONE
    stop_detail: str = ""
    trace: list[dict] = field(default_factory=list)


def gamma_tick(
    st: GammaState,
    *,
    new_hits: int,
    delta_a: float,
    obstacle: float,
    loopability: float,
    frag_index: float,
    tension_energy: float,
    coherence: float,
    theta_loopability: float,
    theta_tension: float,
    theta_coherence: float,
    ent_incr_coh_decr: bool,
) -> StopReason:
    if st.stop_reason != StopReason.NONE:
        return st.stop_reason

    st.hops += 1
    st.new_hits_total += max(0, int(new_hits))
    st.drag_streak = st.drag_streak + 1 if new_hits <= 0 else 0
    st.obstacle = float(obstacle)

    if loopability < theta_loopability:
        st.stop_reason = StopReason.HALT
        st.stop_detail = "loopability_below_threshold"
    elif tension_energy > theta_tension:
        st.stop_reason = StopReason.ROLLBACK
        st.stop_detail = "tension_energy_above_threshold"
    elif coherence < theta_coherence:
        st.stop_reason = StopReason.REQUIRE_REVIEW
        st.stop_detail = "coherence_below_threshold"
    elif ent_incr_coh_decr:
        st.stop_reason = StopReason.CORRECT
        st.stop_detail = "entropy_increasing_while_coherence_decreasing"

    st.trace.append(
        {
            "hop": st.hops,
            "new_hits": int(new_hits),
            "delta_a": float(delta_a),
            "loopability": float(loopability),
            "frag_index": float(frag_index),
            "tension_energy": float(tension_energy),
            "coherence": float(coherence),
            "obstacle": float(obstacle),
            "stop_reason": st.stop_reason.value,
            "stop_detail": st.stop_detail,
        }
    )
    return st.stop_reason


def gamma_finish(st: GammaState, stop_reason: StopReason | None = None) -> dict:
    final_reason = stop_reason or st.stop_reason
    return {
        "ok": final_reason == StopReason.NONE,
        "stop_reason": final_reason.value,
        "stop_detail": st.stop_detail,
        "hops": st.hops,
        "new_hits_total": st.new_hits_total,
        "drag_streak": st.drag_streak,
        "obstacle": st.obstacle,
        "trace_tail": st.trace[-20:],
    }
