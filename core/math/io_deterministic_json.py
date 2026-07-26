# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""Deterministic JSON output helpers for build artifacts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def write_json_deterministic(path: Path | str, obj: Any) -> None:
    """Write UTF-8 JSON in a byte-stable format with trailing newline."""
    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(
        obj,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )
    out_path.write_text(f"{payload}\n", encoding="utf-8")

