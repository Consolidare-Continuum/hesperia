#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from sphere_rag.phase_engine import PhasePolicy, run_phases  # noqa: E402
from sphere_rag.semantic_engine import keywords_to_seed  # noqa: E402


def test_determinism() -> None:
    keywords = ["Altruism", "Truth", "Order"]
    seed1 = keywords_to_seed(keywords, families_table_path=REPO_ROOT / "31_FAMILIES__area_family_table_full.txt")
    seed2 = keywords_to_seed(keywords, families_table_path=REPO_ROOT / "31_FAMILIES__area_family_table_full.txt")
    assert seed1 == seed2, "seed must be deterministic"

    policy = PhasePolicy(alpha=0.50)
    r1 = run_phases(seed1, policy)
    r2 = run_phases(seed2, policy)
    assert r1.invariants == r2.invariants, "phase run must be deterministic at invariant surface"
    assert r1.cut.k_star == r2.cut.k_star, "cut cardinality must be deterministic"
    assert abs(r1.invariants["truth_mass_ratio"] - r2.invariants["truth_mass_ratio"]) < 1e-12


def test_half_mass_preserved() -> None:
    keywords = ["Compassion", "Fraud", "Freedom", "Control"]
    seed = keywords_to_seed(keywords, families_table_path=REPO_ROOT / "31_FAMILIES__area_family_table_full.txt")
    r = run_phases(seed, PhasePolicy(alpha=0.50))
    assert r.invariants["truth_mass_preserved_ge_50pct"], "Phase II must preserve >= 50% truth mass"
    assert r.invariants["no_semantic_expansion"], "Phase II must not expand region"


def main() -> int:
    tests = [
        ("determinism", test_determinism),
        ("half_mass_preserved", test_half_mass_preserved),
    ]
    results = []
    for name, fn in tests:
        try:
            fn()
            results.append({"test": name, "status": "PASS"})
            print(f"PASS: {name}")
        except Exception as e:
            results.append({"test": name, "status": "FAIL", "error": str(e)})
            print(f"FAIL: {name} — {e}", file=sys.stderr)
            print(json.dumps({"results": results}, indent=2), file=sys.stderr)
            return 1
    print(json.dumps({"results": results}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

