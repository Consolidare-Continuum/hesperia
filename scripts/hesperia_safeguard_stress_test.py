#!/usr/bin/env python3
"""Safeguard stress-test: force the loop safeguard to fire and document results.

Per ETHAN-HESPERIA-STATE-NOW-ASSESSMENT §VII and GRACE-HESPERIA-NEXT-DIRECTION.
Proves: TraversalSafeguard triggers SAFEGUARD_STOP after 3 consecutive failures.
Run from repo root: PYTHONPATH=cluster/chroma-server python3 cluster/chroma-server/hesperia_safeguard_stress_test.py
"""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))


def test_safeguard_fires_after_three_failures() -> dict:
    """Unit test: record_hop(0) x3 → should_stop() True, safeguard_stop() returns SAFEGUARD_STOP."""
    from hesperia_logic import TraversalSafeguard, CONSECUTIVE_FAIL_THRESHOLD

    sg = TraversalSafeguard(region_key=(0, 1))
    for i in range(3):
        sg.record_hop(0, {"step": i, "force_fail": True})
    assert sg.should_stop(), "safeguard should stop after 3 failures"
    out = sg.safeguard_stop({"state": "frozen"}, {"test": True})
    assert out.get("status") == "SAFEGUARD_STOP", "status must be SAFEGUARD_STOP"
    assert out.get("fail_count") == 3, "fail_count must be 3"
    return {"status": "PASS", "fail_count": out["fail_count"], "obstacle_region": out.get("obstacle_region")}


def test_valid_streak_resets_fail_count() -> dict:
    """Valid_streak >= 2 resets fail_count; then one more fail does not trigger stop."""
    from hesperia_logic import TraversalSafeguard, VALID_STREAK_RESET

    sg = TraversalSafeguard()
    sg.record_hop(0, {}); sg.record_hop(0, {})  # fail_count = 2
    sg.record_hop(1); sg.record_hop(1)         # valid_streak = 2 → fail_count = 0
    sg.record_hop(0, {})                        # fail_count = 1
    assert not sg.should_stop(), "one fail after reset must not stop"
    return {"status": "PASS", "fail_count": sg.fail_count, "valid_streak": sg.valid_streak}


def main() -> int:
    results = []
    for name, fn in [
        ("three_failures_trigger_stop", test_safeguard_fires_after_three_failures),
        ("valid_streak_resets_fail_count", test_valid_streak_resets_fail_count),
    ]:
        try:
            out = fn()
            results.append({"test": name, "result": out})
            print(f"PASS: {name}")
        except Exception as e:
            results.append({"test": name, "error": str(e)})
            print(f"FAIL: {name} — {e}", file=sys.stderr)
            return 1
    print("Safeguard stress-test: all passed. Safeguard fires after 3 consecutive failures; valid_streak reset verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
