# HESPERIA — Engine /analyze contract envelope (HES-61-01 Python path).
# Copyright © 2026 Societatea cu Răspundere Limitată "CONSOLIDARE CONTINUUM" (IDNO 1026023120076). See LEGAL_NOTICE.md.

"""Re-export shim — moved to sphere.router.engine_analyze_bridge 2026-07-31 (core/RAD severance:
sphere/router couldn't import this from here without violating "sphere must not import runtime").
Kept so existing runtime/tools/tests callers importing this path don't break.

Also the attach point for 24_SPEC §10.1's `meta.hesperia_metric` (HESPERIA_METRIC_EMIT=1,
in-scope per release/v0.7.0/RELEASE_SCOPE.md): sphere/router/engine_analyze_bridge.py cannot call
runtime.services.hesperia_metric_emit itself (same RAD rule), so the attach happens here, at the
runtime boundary layer these envelopes are meant for."""

from __future__ import annotations

from typing import Any

from runtime.services.hesperia_metric_emit import attach_hesperia_metric_meta
from sphere.router.engine_analyze_bridge import (
    trace_content_hash,
)
from sphere.router.engine_analyze_bridge import build_engine_analyze_from_raw as _build_engine_analyze_from_raw
from sphere.router.engine_analyze_bridge import run_engine_analyze as _run_engine_analyze


def build_engine_analyze_from_raw(*args: Any, **kwargs: Any) -> dict[str, Any]:
    return attach_hesperia_metric_meta(_build_engine_analyze_from_raw(*args, **kwargs))


def run_engine_analyze(*args: Any, **kwargs: Any) -> dict[str, Any]:
    return attach_hesperia_metric_meta(_run_engine_analyze(*args, **kwargs))


__all__ = [
    "build_engine_analyze_from_raw",
    "run_engine_analyze",
    "trace_content_hash",
]
