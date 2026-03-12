#!/usr/bin/env python3

# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
HESPERIA pre-test / whole run (small, no big builds).
Runs: v0.4.0 build (small) → v0.4.1 Dict B build (small) → core_math test → pytest sphere_rag/tests.
Use from CLIENTS/hesperia with: python scripts/run_hesperia_pre_test.py
Or: .venv_v040/bin/python scripts/run_hesperia_pre_test.py
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

def _root() -> Path:
    return Path(__file__).resolve().parents[2]

def _run(cmd: list[str], cwd: Path, label: str) -> bool:
    print(f"\n--- {label} ---")
    r = subprocess.run(cmd, cwd=cwd)
    ok = r.returncode == 0
    if not ok:
        print(f"FAILED: {label} (exit {r.returncode})")
    return ok

def main() -> int:
    root = _root()
    py = sys.executable
    venv_py = root / ".venv_v040" / "bin" / "python"
    if venv_py.exists():
        py = str(venv_py)

    # 1. v0.4.0 build (small)
    ok = _run(
        [py, "-m", "sphere_rag.build_v040",
         "--assets-root", "lexicon/curated",
         "--out-dir", "assets/v040",
         "--allow-small-build"],
        root,
        "v0.4.0 build (Dict A → anchors → Dict B → surface)",
    )
    if not ok:
        return 1

    # 2. v0.4.1 Dict B build (small)
    ok = _run(
        [py, "-m", "sphere_rag.build_v041",
         "--assets-root", "assets",
         "--out-dir", "assets/v041",
         "--allow-small-build"],
        root,
        "v0.4.1 Dict B build (preferred + possible_relaxed)",
    )
    if not ok:
        return 1

    # 3. Core math test
    ok = _run(
        [py, "sphere_rag/hesperia_v03_core_math.py", "test"],
        root,
        "v0.3 core math tests",
    )
    if not ok:
        return 1

    # 4. Pytest sphere_rag/tests (optional; skip if pytest not installed)
    pytest_cmd = [py, "-m", "pytest", "sphere_rag/tests", "-v", "--tb=short", "-q"]
    try:
        check = subprocess.run([py, "-c", "import pytest"], cwd=root, capture_output=True)
        if check.returncode != 0:
            print("\n--- pytest sphere_rag/tests (skipped: pip install pytest) ---")
        else:
            ok = _run(pytest_cmd, root, "pytest sphere_rag/tests")
            if not ok:
                return 1
    except Exception as e:
        print(f"\n--- pytest skipped ({e}) ---")

    print("\n--- Pre-test done: all steps passed ---")
    return 0

if __name__ == "__main__":
    sys.exit(main())
