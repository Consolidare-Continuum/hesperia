from __future__ import annotations


def theta_gate(run_result: dict, *, evidence_quality: float | None = None, contradiction_score: float | None = None) -> dict:
    gamma_status = run_result.get("gamma_status", {})
    stop_reason = gamma_status.get("stop_reason", "NONE")

    if stop_reason in {"HALT", "ROLLBACK"}:
        decision = "REJECT"
    elif contradiction_score is not None and contradiction_score > 1.0:
        decision = "REQUIRE_REVIEW"
    elif evidence_quality is not None and evidence_quality < 0.30:
        decision = "REQUIRE_REVIEW"
    else:
        decision = "APPROVE"

    return {
        "decision": decision,
        "stop_reason": stop_reason,
        "evidence_quality": evidence_quality,
        "contradiction_score": contradiction_score,
    }
