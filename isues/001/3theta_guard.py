```python
# ============================================================
# theta_guard.py
# HESPERIA — Θ (Theta) Governance Legitimacy Guard
#
# Position in pipeline:
#   Σ (static invariants)  -> must have passed
#   Γ (dynamic stability)  -> must have passed
#   Θ (governance legitimacy) -> final gate before publish/use
#
# Scope (Θ ONLY):
#   - config integrity & versioning
#   - operator override discipline
#   - ontology / structure hash legitimacy
#   - ingestion contract / schema drift legitimacy
#   - publishability checks (e.g., empty region cannot pass)
#
# Non-overlap:
#   Θ does NOT validate geometry, ring topology, drift trends, entropy, etc.
#   That belongs to Σ and Γ.
# ============================================================

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Dict, Any
import hashlib
import json


# -----------------------------
# Failure modes
# -----------------------------

class ThetaFailMode(str, Enum):
    HALT = "halt"                   # stop now; governance invalid
    REQUIRE_REVIEW = "require_review"  # allow continuation but forbid publish
    CORRECT = "correct"             # trigger correction routine if supported


class ThetaViolation(Exception):
    def __init__(self, code: str, mode: ThetaFailMode = ThetaFailMode.HALT, detail: str = ""):
        super().__init__(f"{code}{'::' + detail if detail else ''}")
        self.code = code
        self.mode = mode
        self.detail = detail


# -----------------------------
# Helpers
# -----------------------------

def stable_hash(obj: Any) -> str:
    """
    Deterministic SHA-256 of JSON-serializable config.
    Use to fingerprint runtime config/contracts for audit.
    """
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _pct_delta(old: float, new: float) -> float:
    if old == 0.0:
        return float("inf") if new != 0.0 else 0.0
    return abs(new - old) / abs(old)


# -----------------------------
# Θ State & Policy
# -----------------------------

@dataclass(frozen=True)
class ThetaState:
    """
    Snapshot of governance-relevant state at decision time.
    Intended to be produced by your pipeline coordinator.
    """

    # "Did upstream pass?"
    sigma_passed: bool
    gamma_passed: bool

    # Fingerprints (must be present in any publishable run)
    config_hash: str            # hash of runtime parameters (thresholds, models, etc.)
    structure_hash: str         # hash of frozen ontology/topology (from Σ guard or canonical builder)
    ingestion_hash: str         # hash of ingestion contract/schema fingerprint

    # For anti-silent-mutation checks
    config_version: Optional[str] = None     # e.g. "v1.0.3" or git SHA
    theta_version: Optional[str] = "v1.0"    # guard version itself (for logs)

    # Operator discipline
    operator_override_count: int = 0
    operator_override_budget: int = 0        # can be embedded in policy too; this is runtime signal

    # Publishability / runtime sanity flags
    region_size: int = 0                     # |R| (number of sides or statements—your choice)
    attempted_publish: bool = True           # if False, Θ can be laxer

    # Optional identity markers for audit
    operator_id: Optional[str] = None
    session_id: Optional[str] = None

    # Optional embedding contract signals
    embedding_model_id: Optional[str] = None
    embedding_dim: Optional[int] = None


@dataclass(frozen=True)
class ThetaPolicy:
    """
    Governance rules. Keep conservative defaults.
    """

    # Hard requirements
    require_sigma_pass: bool = True
    require_gamma_pass: bool = True
    require_config_version: bool = True

    # Publish rules
    forbid_publish_if_empty_region: bool = True
    forbid_publish_if_hash_missing: bool = True

    # Override policy
    max_operator_overrides: int = 0                 # strict by default
    override_excess_mode: ThetaFailMode = ThetaFailMode.REQUIRE_REVIEW

    # Config mutation discipline
    # Expected hashes are the "blessed" targets for this build/version.
    expected_config_hash: Optional[str] = None
    expected_structure_hash: Optional[str] = None
    expected_ingestion_hash: Optional[str] = None

    # If you allow controlled parameter drift, pass a baseline numeric map and tolerances.
    # Example:
    #   baseline_params = {"max_obstacle": 0.85, "min_loopability": 0.05}
    #   allowed_pct_delta = {"max_obstacle": 0.10, "min_loopability": 0.20}
    baseline_params: Optional[Dict[str, float]] = None
    runtime_params: Optional[Dict[str, float]] = None
    allowed_pct_delta: Optional[Dict[str, float]] = None

    # Embedding contract (optional but recommended)
    expected_embedding_model_id: Optional[str] = None
    expected_embedding_dim: Optional[int] = None


# -----------------------------
# Θ Guard
# -----------------------------

class ThetaGuard:
    """
    Final governance gate.

    Typical usage:
        theta = ThetaGuard(policy=ThetaPolicy(...))
        theta.evaluate(theta_state)  # raises ThetaViolation on failure
    """

    def __init__(self, policy: ThetaPolicy):
        self.policy = policy

    def evaluate(self, s: ThetaState) -> None:
        # 0) Preconditions: Σ and Γ must pass (unless policy relaxes it)
        self._require_upstream_pass(s)

        # 1) Required fingerprints / versioning presence
        self._require_identity_and_hashes(s)

        # 2) Hash legitimacy (detect silent mutation)
        self._check_expected_hashes(s)

        # 3) Parameter drift discipline (optional; only if baseline/runtime supplied)
        self._check_param_drift(s)

        # 4) Operator override discipline
        self._check_operator_overrides(s)

        # 5) Publishability checks (empty region cannot be publishable)
        self._check_publishability(s)

        # 6) Embedding contract (optional)
        self._check_embedding_contract(s)


    # --------------------------------------------------------
    # Checks
    # --------------------------------------------------------

    def _require_upstream_pass(self, s: ThetaState) -> None:
        if self.policy.require_sigma_pass and not s.sigma_passed:
            raise ThetaViolation("SIGMA_NOT_PASSED", ThetaFailMode.HALT)

        if self.policy.require_gamma_pass and not s.gamma_passed:
            raise ThetaViolation("GAMMA_NOT_PASSED", ThetaFailMode.HALT)

    def _require_identity_and_hashes(self, s: ThetaState) -> None:
        # Config version is your primary "no silent tuning" control knob.
        if self.policy.require_config_version and not (s.config_version and str(s.config_version).strip()):
            raise ThetaViolation("CONFIG_VERSION_MISSING", ThetaFailMode.HALT)

        # Hashes must exist if publishing is attempted.
        if s.attempted_publish and self.policy.forbid_publish_if_hash_missing:
            if not s.config_hash:
                raise ThetaViolation("CONFIG_HASH_MISSING", ThetaFailMode.HALT)
            if not s.structure_hash:
                raise ThetaViolation("STRUCTURE_HASH_MISSING", ThetaFailMode.HALT)
            if not s.ingestion_hash:
                raise ThetaViolation("INGESTION_HASH_MISSING", ThetaFailMode.HALT)

    def _check_expected_hashes(self, s: ThetaState) -> None:
        p = self.policy

        if p.expected_config_hash is not None and s.config_hash != p.expected_config_hash:
            raise ThetaViolation("CONFIG_MUTATION_UNLOGGED", ThetaFailMode.HALT,
                                 f"expected={p.expected_config_hash} got={s.config_hash}")

        if p.expected_structure_hash is not None and s.structure_hash != p.expected_structure_hash:
            raise ThetaViolation("ONTOLOGY_CHANGE_WITHOUT_HASH_UPDATE", ThetaFailMode.HALT,
                                 f"expected={p.expected_structure_hash} got={s.structure_hash}")

        if p.expected_ingestion_hash is not None and s.ingestion_hash != p.expected_ingestion_hash:
            raise ThetaViolation("INGESTION_SCHEMA_DRIFT", ThetaFailMode.HALT,
                                 f"expected={p.expected_ingestion_hash} got={s.ingestion_hash}")

    def _check_param_drift(self, s: ThetaState) -> None:
        p = self.policy
        if not (p.baseline_params and p.runtime_params and p.allowed_pct_delta):
            return

        for k, base in p.baseline_params.items():
            if k not in p.runtime_params:
                raise ThetaViolation("RUNTIME_PARAM_MISSING", ThetaFailMode.HALT, k)

            newv = p.runtime_params[k]
            allowed = p.allowed_pct_delta.get(k, 0.0)

            d = _pct_delta(base, newv)
            if d > allowed:
                # This is governance-invalid, but you may decide to require review instead of halt.
                raise ThetaViolation("PARAM_DRIFT_OUTSIDE_ALLOWED_RANGE",
                                     ThetaFailMode.REQUIRE_REVIEW,
                                     f"{k} base={base} new={newv} pct={d:.3f} allowed={allowed:.3f}")

    def _check_operator_overrides(self, s: ThetaState) -> None:
        budget = self.policy.max_operator_overrides

        # Runtime may carry budget too; if present, use the tighter of the two.
        if s.operator_override_budget > 0:
            budget = min(budget, s.operator_override_budget) if budget > 0 else s.operator_override_budget

        if budget == 0 and s.operator_override_count > 0:
            raise ThetaViolation("OPERATOR_OVERRIDE_FORBIDDEN",
                                 self.policy.override_excess_mode,
                                 f"count={s.operator_override_count}")

        if budget > 0 and s.operator_override_count > budget:
            raise ThetaViolation("OPERATOR_OVERRIDE_COUNT_EXCEEDED",
                                 self.policy.override_excess_mode,
                                 f"count={s.operator_override_count} budget={budget}")

    def _check_publishability(self, s: ThetaState) -> None:
        if not s.attempted_publish:
            return

        if self.policy.forbid_publish_if_empty_region and s.region_size <= 0:
            raise ThetaViolation("EMPTY_REGION_NOT_ESCALATED", ThetaFailMode.HALT, f"|R|={s.region_size}")

    def _check_embedding_contract(self, s: ThetaState) -> None:
        p = self.policy

        if p.expected_embedding_model_id is not None:
            if not s.embedding_model_id:
                raise ThetaViolation("EMBEDDING_MODEL_ID_MISSING", ThetaFailMode.HALT)
            if s.embedding_model_id != p.expected_embedding_model_id:
                raise ThetaViolation("EMBEDDING_MODEL_CHANGED_SILENTLY", ThetaFailMode.HALT,
                                     f"expected={p.expected_embedding_model_id} got={s.embedding_model_id}")

        if p.expected_embedding_dim is not None:
            if s.embedding_dim is None:
                raise ThetaViolation("EMBEDDING_DIM_MISSING", ThetaFailMode.HALT)
            if s.embedding_dim != p.expected_embedding_dim:
                raise ThetaViolation("EMBEDDING_DIM_CHANGED_SILENTLY", ThetaFailMode.HALT,
                                     f"expected={p.expected_embedding_dim} got={s.embedding_dim}")


# -----------------------------
# Minimal integration wrapper
# -----------------------------

def theta_step(theta: ThetaGuard, state: ThetaState) -> Optional[ThetaViolation]:
    """
    Convenience wrapper: evaluate, return violation (or None).
    """
    try:
        theta.evaluate(state)
        return None
    except ThetaViolation as e:
        return e
```
