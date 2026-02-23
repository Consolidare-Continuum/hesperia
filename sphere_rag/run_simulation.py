#!/usr/bin/env python3
"""
Single entry point for HESPERIA v0.3 simulations.
  full   — full_run_simulation.py (stub topology, optional --S/--L)
  chroma — chroma_books_validation_run.py (stub traversal + Chroma books I-Q2)
Usage: python3 sphere_rag/run_simulation.py full [args...]
       python3 sphere_rag/run_simulation.py chroma [args...]
"""

from __future__ import annotations

import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
if _SCRIPT_DIR.name == "sphere_rag":
    _HESPERIA_ROOT = _SCRIPT_DIR.parent
else:
    _HESPERIA_ROOT = _SCRIPT_DIR

sys.path.insert(0, str(_HESPERIA_ROOT))


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: run_simulation.py full [--S path] [--L path] [--out path]", file=sys.stderr)
        print("       run_simulation.py chroma [--no-books-check] [--out path]", file=sys.stderr)
        print("       run_simulation.py serve [port]  # v0.3.3 API: GET /health, POST /hesperia/analyze", file=sys.stderr)
        print("       run_simulation.py pretest       # v0.4.0 + v0.4.1 small builds, core_math test, pytest", file=sys.stderr)
        return 1
    mode = sys.argv[1].lower()
    args = sys.argv[2:]

    if mode == "pretest":
        import subprocess
        pre_test = _HESPERIA_ROOT / "scripts" / "run_hesperia_pre_test.py"
        if not pre_test.exists():
            print(f"Not found: {pre_test}", file=sys.stderr)
            return 1
        return subprocess.run([sys.executable, str(pre_test)], cwd=str(_HESPERIA_ROOT)).returncode

    if mode == "full":
        sys.argv = [str(_SCRIPT_DIR / "full_run_simulation.py")] + args
        import sphere_rag.full_run_simulation as m
        return m.main()
    if mode == "chroma":
        sys.argv = [str(_SCRIPT_DIR / "chroma_books_validation_run.py")] + args
        import sphere_rag.chroma_books_validation_run as m
        return m.main()
    if mode == "serve":
        sys.argv = [str(_SCRIPT_DIR / "serve_v033.py")] + args
        import sphere_rag.serve_v033 as m
        m.main()
        return 0
    print("Unknown mode. Use 'full', 'chroma', 'serve', or 'pretest'.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
