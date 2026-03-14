#!/usr/bin/env python3
# HESPERIA — Sealing scan. Catch forbidden terms in public tree.
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

"""
Scan repository for forbidden architecture-revealing terms.
Public tree must pass with zero hits; internal-only zones may contain them.
Usage: python3 tools/sealing_scan.py [--repo PATH] [--public-only]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Forbidden terms (case-insensitive substrings in public tree)
FORBIDDEN_TERMS = [
    "sphere",
    "hexagon",
    r"\bhex\b",
    "3D",
    "lattice",
    "side_id",
    "adjacency path",
    "propagation path",
    "layer1", "layer2", "layer3", "layer4", "layer5", "layer6", "layer7", "layer8", "layer9",
    "layer_1", "layer_2", "layer_3", "layer_4", "layer_5", "layer_6", "layer_7", "layer_8", "layer_9",
    "area11", "area12", "area 11", "area 12",
    "12 areas",
    "reserved families",
    "288 families",
    "vector axis",
    "grid",
    "graph",
    r"\bpropagation\b",  # word boundary to avoid matching "propagated"
    "embedding",
    "vector_space",
    "internal_layer",
    "topology_index",
]

# Files that define or enforce forbidden terms (excluded from scan)
SCAN_SKIP_FILES = [
    "tools/sealing_scan.py",
    "runtime/shipping/schema_guard.py",
]

# Paths that are internal-only (hits here are allowed)
INTERNAL_ONLY_SUBDIRS = [
    "docs/internal",
    "core/layers",
    "core/math",
    "core/domain",
    "core/topology",
    "core/propagation",
    "core/attribution",
    "legacy",
    "tests",
    ".git",
    "__pycache__",
    "node_modules",
]


def _is_internal_path(file_path: Path, repo_root: Path) -> bool:
    try:
        rel = file_path.resolve().relative_to(repo_root.resolve())
    except ValueError:
        return True
    s = str(rel).replace("\\", "/")
    if any(s == f or s.endswith("/" + f) for f in SCAN_SKIP_FILES):
        return True
    return any(s.startswith(d) or ("/" + d + "/") in ("/" + s + "/") for d in INTERNAL_ONLY_SUBDIRS)


def scan_file(file_path: Path, repo_root: Path, patterns: list[tuple[re.Pattern, str]]) -> list[tuple[int, str, str]]:
    hits = []
    if _is_internal_path(file_path, repo_root):
        return hits
    try:
        text = file_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return hits
    for i, line in enumerate(text.splitlines(), 1):
        for pat, label in patterns:
            if pat.search(line):
                hits.append((i, line.strip()[:80], label))
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description="Sealing scan: find forbidden terms in public tree.")
    ap.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1], help="Repo root")
    ap.add_argument("--public-only", action="store_true", help="Only report hits in public tree (default: same, exit 1 on hit)")
    ap.add_argument("--list-internal", action="store_true", help="List internal-only paths and exit")
    args = ap.parse_args()
    repo = args.repo

    if args.list_internal:
        for d in INTERNAL_ONLY_SUBDIRS:
            print(d)
        return 0

    patterns = []
    for t in FORBIDDEN_TERMS:
        if t.startswith("\\") or "\\" in t:
            patterns.append((re.compile(t, re.IGNORECASE), t))
        else:
            patterns.append((re.compile(re.escape(t), re.IGNORECASE), t))

    public_hits: list[tuple[Path, int, str, str]] = []
    for py in repo.rglob("*.py"):
        if not py.is_file():
            continue
        for line_no, line_preview, label in scan_file(py, repo, patterns):
            public_hits.append((py, line_no, line_preview, label))
    for md in repo.rglob("*.md"):
        if not md.is_file() or _is_internal_path(md, repo):
            continue
        for line_no, line_preview, label in scan_file(md, repo, patterns):
            public_hits.append((md, line_no, line_preview, label))
    for json_path in repo.rglob("*.json"):
        if not json_path.is_file() or _is_internal_path(json_path, repo):
            continue
        for line_no, line_preview, label in scan_file(json_path, repo, patterns):
            public_hits.append((json_path, line_no, line_preview, label))

    if public_hits:
        for path, line_no, preview, label in public_hits[:50]:
            try:
                rel = path.relative_to(repo)
            except ValueError:
                rel = path
            print(f"{rel}:{line_no}: [{label}] {preview}")
        if len(public_hits) > 50:
            print(f"... and {len(public_hits) - 50} more")
        print(f"Total: {len(public_hits)} forbidden hits in public tree.", file=sys.stderr)
        return 1
    print("Sealing scan: no forbidden terms in public tree.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
