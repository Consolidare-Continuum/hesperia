#!/usr/bin/env python3
"""Hesperia logical operators and traversal — propositional logic in the sphere.
Implements Area meta-operator, Family operator set, Hex constraint node, Path/Hop operators,
obstacle state machine, VALIDATE/SATISFY/UNSAT/ENTAILS per ETHAN-HESPERIA-OPERATOR-INTERFACE-SPEC.
Loop safeguard: three consecutive logical failures → SAFEGUARD_STOP (ETHAN-HESPERIA-LOOP-SAFEGUARD).
Ref: governance/ETHAN-HESPERIA-OPERATOR-INTERFACE-SPEC.md, ETHAN-HESPERIA-LOOP-SAFEGUARD.md.
"""

from __future__ import annotations

import enum
from typing import Any

# Canonical 12 areas (index 0..11) and six polarity axes per spec §1.1
CANONICAL_AREAS = [
    "GOOD", "HARM", "TRUTH", "DECEIT", "ORDER", "CHAOS",
    "FREEDOM", "CONTROL", "CARE", "INDIFFERENCE", "CREATION", "DESTRUCTION",
]
POLARITY_AXES = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11)]  # (good,harm), (truth,deceit), ...


class ObstacleState(enum.Enum):
    CLEAR = "CLEAR"
    OBSTACLE_CONTRADICTION = "OBSTACLE_CONTRADICTION"
    OBSTACLE_DRIFT = "OBSTACLE_DRIFT"
    OBSTACLE_UNSAT = "OBSTACLE_UNSAT"
    OBSTACLE_INVALID_IMPLICATION = "OBSTACLE_INVALID_IMPLICATION"


# Semantic state: assignment atom -> 0|1. Slice by area: atoms keyed or tagged by area_id.
# path_context: dict with path (list of (area_id, global_id)), optional statement_set (list of formula repr).
def _slice_for_area(state: dict[str, int], area_id: int) -> dict[str, int]:
    """Atoms for this area: keys starting with area prefix or in area's set."""
    prefix = f"a{area_id}_"
    return {k: v for k, v in state.items() if k.startswith(prefix) or k.startswith(CANONICAL_AREAS[area_id].lower() + "_")}


def _has_contradiction_in_slice(slice_state: dict[str, int]) -> bool:
    """Contradiction = same atom both 0 and 1. In single assignment we have one value per key; contradiction = we have both p and ¬p in stated formulas (handled via UNSAT). For state we check no key has conflicting view (e.g. neg key)."""
    for k, v in slice_state.items():
        neg_k = "¬" + k if not k.startswith("¬") else k[1:]
        if neg_k in slice_state and slice_state[neg_k] == v:
            return True
    return False


class Area:
    """Area as meta-operator (semantic field operator). area_id 0..11."""

    def __init__(self, area_id: int):
        self.area_id = area_id % 12
        self.name = CANONICAL_AREAS[self.area_id]

    def enforce(self, state: dict[str, int], path_context: dict[str, Any]) -> tuple[bool, str]:
        """Ensure state satisfies this area's constraint. Returns (success, message)."""
        if self.detect_contradiction(state, path_context):
            return False, f"contradiction in area {self.name}"
        if not self.test_validity(state, path_context):
            return False, f"validity check failed in area {self.name}"
        return True, "ok"

    def test_validity(self, state: dict[str, int], path_context: dict[str, Any]) -> bool:
        """Current path state valid (no assignment in slice falsifies constraint). Minimal: no contradiction."""
        return not self.detect_contradiction(state, path_context)

    def detect_contradiction(self, state: dict[str, int], path_context: dict[str, Any]) -> bool:
        """True if state contains contradiction (p ∧ ¬p) in this area's slice."""
        sl = _slice_for_area(state, self.area_id)
        if _has_contradiction_in_slice(sl):
            return True
        stmts = path_context.get("statement_set") or []
        if stmts and UNSAT(stmts, max_depth=path_context.get("max_deduction_depth", 5)):
            return True
        return False


class Family:
    """Family as logical operator set. Keyed by (area_name, family_name)."""

    def __init__(self, area_name: str, family_name: str):
        self.area_name = area_name
        self.family_name = family_name

    def normalize(self, statement: str) -> str:
        """Normalize (e.g. p → q ≡ ¬p ∨ q). Stub: return as-is."""
        s = statement.strip()
        if "→" in s:
            parts = s.split("→", 1)
            return f"(¬({parts[0].strip()}) ∨ ({parts[1].strip()}))"
        return s

    def reduce(self, statement: str) -> str:
        """Minimal connective form. Stub: return normalized."""
        return self.normalize(statement)

    def check_equivalence(self, a: str, b: str) -> bool:
        """Equivalent under c3p. Stub: normalize both and compare."""
        return self.normalize(a) == self.normalize(b)

    def detect_unsat(self, statement_set: list[str]) -> bool:
        """True if statement set unsatisfiable (c2p)."""
        return UNSAT(statement_set)


class Hex:
    """Hex as constraint node. evaluate(path, context) -> result dict."""

    def evaluate(self, path: list[tuple[int, int]], context: dict[str, Any]) -> dict[str, Any]:
        """Runs Boolean-style evaluation, deduction chaining, contradiction detection. Returns valid, contradiction, state_after, obstacle."""
        state = context.get("state") or {}
        statement_set = context.get("statement_set") or []
        obstacle = ObstacleState.CLEAR
        for area_id, _ in path:
            ar = Area(area_id)
            if ar.detect_contradiction(state, {"statement_set": statement_set, **context}):
                obstacle = ObstacleState.OBSTACLE_CONTRADICTION
                break
        if UNSAT(statement_set):
            obstacle = ObstacleState.OBSTACLE_UNSAT
        return {
            "valid": obstacle == ObstacleState.CLEAR,
            "contradiction": obstacle in (ObstacleState.OBSTACLE_CONTRADICTION, ObstacleState.OBSTACLE_UNSAT),
            "state_after": state,
            "obstacle": obstacle.value,
        }


class Path:
    """Path with path operators. state + path list."""

    def __init__(self, state: dict[str, int], path_list: list[tuple[int, int]]):
        self.state = dict(state)
        self.path_list = list(path_list)

    def forward_inference(self) -> dict[str, int]:
        """Apply → forward (modus ponens). Stub: return state."""
        return dict(self.state)

    def backward_reduce(self) -> dict[str, int]:
        """Simplify backward. Stub: return state."""
        return dict(self.state)

    def normalize(self) -> dict[str, int]:
        """Apply Family.normalize along path. Stub: return state."""
        return dict(self.state)

    def detect_cycle(self) -> bool:
        """True if path revisits (area_id, global_id)."""
        seen = set()
        for step in self.path_list:
            if step in seen:
                return True
            seen.add(step)
        return False

    def polarize(self) -> dict[int, int]:
        """area_id -> polarity +1/-1 on axis."""
        out: dict[int, int] = {}
        for area_id, _ in self.path_list:
            if area_id not in out:
                for (a, b) in POLARITY_AXES:
                    if area_id == a:
                        out[area_id] = 1
                        break
                    if area_id == b:
                        out[area_id] = -1
                        break
        return out


# Hop operators: (state_in, ...) -> state_out
def hop_negate(state: dict[str, int]) -> dict[str, int]:
    """Invert polarity; detect p∧¬p."""
    out = {}
    for k, v in state.items():
        new_k = "¬" + k if not k.startswith("¬") else k[1:]
        out[new_k] = 1 - v
    return out


def hop_merge(state_a: dict[str, int], state_b: dict[str, int]) -> dict[str, int]:
    """Both must hold (∧I/∧E). Merge; conflict => contradiction."""
    out = dict(state_a)
    for k, v in state_b.items():
        if k in out and out[k] != v:
            out["_contradiction"] = 1
            break
        out[k] = v
    return out


def hop_branch(state: dict[str, int]) -> list[dict[str, int]]:
    """Create alternative paths (∨). Return list of states (e.g. same state as single branch)."""
    return [dict(state)]


def hop_exclusive(state_a: dict[str, int], state_b: dict[str, int]) -> dict[str, int] | None:
    """Exactly one of two. Return state_a or state_b; if both/neither, None."""
    return state_a  # stub: prefer first


def hop_infer(state: dict[str, int], antecedent: str, consequent: str) -> dict[str, int]:
    """Modus ponens: if antecedent true, set consequent. Stub: return state."""
    return dict(state)


def hop_sync(state_a: dict[str, int], state_b: dict[str, int]) -> dict[str, int]:
    """Bidirectional consistency. Stub: merge."""
    return hop_merge(state_a, state_b)


# Higher-level semantic operators (bounded depth)
DEFAULT_MAX_DEPTH = 10


def _atoms_in(s: str) -> set[str]:
    """Crude atom extraction for simple formulas."""
    for c in "¬∧∨⊕→↔()":
        s = s.replace(c, " ")
    return set(x for x in s.split() if x and not x.isdigit())


def UNSAT(statement_set: list[str], max_depth: int = DEFAULT_MAX_DEPTH) -> bool:
    """True if statement set unsatisfiable (c2p). Bounded: check for {p, ¬p} or trivial clash."""
    if not statement_set:
        return False
    atoms: set[str] = set()
    neg_atoms: set[str] = set()
    for s in statement_set:
        for a in _atoms_in(s):
            if a.startswith("¬"):
                neg_atoms.add(a[1:])
            else:
                atoms.add(a)
    if atoms & neg_atoms:
        return True
    # Could add simple DPLL here with depth limit; for now only direct p/¬p.
    return False


def SATISFY(constraints: list[str], max_depth: int = DEFAULT_MAX_DEPTH) -> dict[str, int] | None:
    """One consistent assignment or None (c2p). Stub: return trivial model if no direct clash."""
    if UNSAT(constraints, max_depth):
        return None
    model: dict[str, int] = {}
    for s in constraints:
        for a in _atoms_in(s):
            if not a.startswith("¬") and a not in model:
                model[a] = 1
    return model


def VALIDATE(state: dict[str, int], area_or_path: Area | Path) -> bool:
    """Tautological in area (c2p). Stub: no contradiction in state."""
    if isinstance(area_or_path, Area):
        return not area_or_path.detect_contradiction(state, {})
    # Path: no contradiction in path state
    for area_id in {p[0] for p in area_or_path.path_list}:
        if Area(area_id).detect_contradiction(state, {}):
            return False
    return True


def ENTAILS(sigma: list[str], phi: str, max_depth: int = DEFAULT_MAX_DEPTH) -> bool:
    """Σ ⊨ φ via Σ ∧ ¬φ unsatisfiable (c3p)."""
    return UNSAT(sigma + [f"¬({phi})"], max_depth)


# Hazard map (area_id, family_id) -> CLEAR | TENSION | UNSAFE (Wumpus layer)
class HazardLevel(enum.Enum):
    CLEAR = "CLEAR"
    TENSION = "TENSION"
    UNSAFE = "UNSAFE"


def hazard_map_update(
    hazard_map: dict[tuple[int, int], HazardLevel],
    area_id: int,
    family_id: int,
    has_contradiction: bool,
) -> None:
    """Update hazard map: if no contradiction in area, adjacent safe; else mark UNSAFE/TENSION."""
    key = (area_id, family_id)
    if has_contradiction:
        hazard_map[key] = HazardLevel.UNSAFE
    else:
        hazard_map[key] = HazardLevel.CLEAR


# --- Loop safeguard (ETHAN-HESPERIA-LOOP-SAFEGUARD) ---
CONSECUTIVE_FAIL_THRESHOLD = 3
VALID_STREAK_RESET = 2


class SafeguardStop(Exception):
    """Raised or returned when fail_count >= CONSECUTIVE_FAIL_THRESHOLD. Traversal must freeze."""


class TraversalSafeguard:
    """Per-context loop safeguard: three consecutive logical failures → STOP.
    Attach one instance per traversal context (hex, family, area cross-polarity).
    hop_result: 1 = valid, 0 = invalid (UNSAT, CONTRADICTION, ENTAILMENT_FAIL, POLARITY_CONFLICT, no satisfiable continuation).
    """

    def __init__(
        self,
        hazard_map: dict[tuple[int, int], HazardLevel] | None = None,
        region_key: tuple[int, int] | None = None,
    ):
        self.fail_count = 0
        self.valid_streak = 0
        self.fail_trace: list[dict[str, Any]] = []  # last 3 hop states
        self._max_trace = 3
        self.hazard_map = hazard_map
        self.region_key = region_key
        self.stopped = False

    def record_hop(self, hop_result: int, state_snapshot: dict[str, Any] | None = None) -> None:
        """hop_result: 1 = valid, 0 = invalid. Updates fail_count, valid_streak; may append to fail_trace."""
        if self.stopped:
            return
        if hop_result == 1:
            self.valid_streak += 1
            if self.valid_streak >= VALID_STREAK_RESET:
                self.fail_count = 0
        else:
            self.fail_count += 1
            self.valid_streak = 0
            if state_snapshot is not None:
                self.fail_trace.append(dict(state_snapshot))
                if len(self.fail_trace) > self._max_trace:
                    self.fail_trace.pop(0)

    def should_stop(self) -> bool:
        """True if fail_count >= CONSECUTIVE_FAIL_THRESHOLD (call safeguard_stop next)."""
        return self.fail_count >= CONSECUTIVE_FAIL_THRESHOLD

    def safeguard_stop(self, state: dict[str, Any], context: dict[str, Any]) -> dict[str, Any]:
        """Freeze traversal; mark region LOGICAL_OBSTACLE_CLUSTER (UNSAFE); keep last 3 states; return STOP payload."""
        self.stopped = True
        if self.hazard_map is not None and self.region_key is not None:
            self.hazard_map[self.region_key] = HazardLevel.UNSAFE
        return {
            "status": "SAFEGUARD_STOP",
            "fail_count": self.fail_count,
            "fail_trace": list(self.fail_trace),
            "obstacle_region": self.region_key,
            "state": state,
            "context_keys": list(context.keys()),
        }


def hop_result_from_hex_eval(eval_result: dict[str, Any]) -> int:
    """Map Hex.evaluate() result to hop_result: 1 = valid, 0 = invalid."""
    return 1 if eval_result.get("valid", False) else 0


def run_traversal_with_safeguard(
    path: list[tuple[int, int]],
    context: dict[str, Any],
    hazard_map: dict[tuple[int, int], HazardLevel] | None = None,
    region_key: tuple[int, int] | None = None,
) -> dict[str, Any]:
    """Run path through Hex.evaluate step-by-step; one TraversalSafeguard per context.
    Each step = one hop; record_hop(hop_result); if fail_count >= 3 → safeguard_stop and return.
    Returns either { status: 'OK', state, path, steps_done } or safeguard_stop payload (status: 'SAFEGUARD_STOP', ...).
    """
    hex_node = Hex()
    sg = TraversalSafeguard(hazard_map=hazard_map, region_key=region_key or (path[0] if path else (0, 0)))
    state = dict(context.get("state") or {})
    for i in range(len(path)):
        path_so_far = path[: i + 1]
        ctx_step = {**context, "state": state}
        result = hex_node.evaluate(path_so_far, ctx_step)
        state = result.get("state_after") or state
        hop_result = hop_result_from_hex_eval(result)
        sg.record_hop(
            hop_result,
            {"path": path_so_far, "state_after": state, "obstacle": result.get("obstacle")},
        )
        if sg.should_stop():
            return sg.safeguard_stop(state, ctx_step)
    return {
        "status": "OK",
        "state": state,
        "path": path,
        "steps_done": len(path),
    }
