#!/usr/bin/env python3
# HESPERIA — Build a zip-safe, portable release bundle.
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
#
# Core goal: eliminate path-length / encoding edge cases by copying the repo
# into a temp dir, excluding problematic paths, and writing a normalized zip.

from __future__ import annotations

import os
import shutil
import zipfile


SRC = "."

EXCLUDE_PREFIXES = [
    ".git",
    "__pycache__",
    "docs/research/_noone_local",
]


def _norm_rel(p: str) -> str:
    # Normalize to forward slashes so zip entries are consistent across OSes.
    return p.replace("\\", "/").lstrip("./")


def should_exclude(rel_path: str) -> bool:
    rel_path_n = _norm_rel(rel_path)
    for e in EXCLUDE_PREFIXES:
        e_n = _norm_rel(e)
        if rel_path_n == e_n:
            return True
        if rel_path_n.startswith(e_n + "/"):
            return True
    return False


def _version_from_env_or_default() -> str:
    v = os.environ.get("HESPERIA_VERSION", "").strip()
    return v if v else "0.5.1"


def main() -> int:
    version = _version_from_env_or_default()
    out_base = f"release_bundle_v{version}"

    # Fast path: zip directly from SRC while excluding known problematic trees.
    # This keeps the bundle portable (normalized entry paths) without the heavy
    # cost of copying the entire repository to a temp directory.
    src_root = os.path.abspath(SRC)
    zip_path = f"{out_base}.zip"
    if os.path.exists(zip_path):
        os.remove(zip_path)

    # ZIP_STORED avoids expensive compression and keeps the bundle portable.
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_STORED) as z:
        for root, _, files in os.walk(src_root):
            for f in files:
                full = os.path.join(root, f)
                rel = os.path.relpath(full, src_root)
                rel_n = _norm_rel(rel)
                if should_exclude(rel_n):
                    continue
                z.write(full, rel_n)
    print(f"build_release_bundle: wrote {zip_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

