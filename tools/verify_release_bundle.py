#!/usr/bin/env python3
# HESPERIA — Verify portable release bundle determinism + integrity.
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
#
# Minimal deterministic checks:
#  - zip opens and internal CRCs pass (ZipFile.testzip)
#  - required files exist inside the archive
#  - zip entry names are globally sorted (deterministic packaging)
#  - prints SHA256 of the zip bytes (optionally writes *.sha256)

from __future__ import annotations

import hashlib
import sys
import zipfile


def main() -> int:
    path = "release_bundle_v0.5.1.zip"

    required = [
        "VERSION.yaml",
        "runtime/shipping/version_info.py",
        "runtime/shipping/cli_main.py",
        "runtime/shipping/api_main.py",
    ]

    try:
        with zipfile.ZipFile(path, "r") as z:
            bad = z.testzip()
            if bad:
                print(f"[FAIL] Corrupt file inside zip: {bad}")
                return 1

            names = z.namelist()
            if names != sorted(names):
                print("[FAIL] Zip entries not sorted (non-deterministic build)")
                return 1

            s = set(names)
            missing = [r for r in required if r not in s]
            if missing:
                print(f"[FAIL] Missing required files in zip: {missing}")
                return 1
    except Exception as e:
        print(f"[FAIL] Zip cannot be opened: {e}")
        return 1

    with open(path, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()

    print("[OK] Zip integrity verified")
    print(f"[OK] SHA256: {h}")

    sha_path = path + ".sha256"
    try:
        with open(sha_path, "w", encoding="utf-8") as w:
            w.write(h + "\n")
    except Exception:
        # Non-fatal: checksum file is optional.
        pass

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

