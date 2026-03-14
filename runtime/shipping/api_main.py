#!/usr/bin/env python3
# HESPERIA — Shipping API. FastAPI; endpoints: POST /analyze, /compare, /batch-analyze, GET /health.
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

"""
Sealed API entry point. No internal endpoints. Uses only core.services.
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any

# Optional: license gate at startup (redistribution friction)
def _license_ok() -> bool:
    try:
        from runtime.shipping.license_check import check_license
        return check_license()
    except Exception:
        return True  # If no license module or env bypass, allow

# In-memory rate limit: max requests per minute per key (optional)
_RATE: dict[str, list[float]] = {}
_RATE_LIMIT = int(os.environ.get("HESPERIA_RATE_LIMIT", "60"))  # requests per minute
_RATE_WINDOW = 60.0

def _rate_limit(key: str = "default") -> bool:
    now = time.monotonic()
    if key not in _RATE:
        _RATE[key] = []
    times = _RATE[key]
    times[:] = [t for t in times if now - t < _RATE_WINDOW]
    if len(times) >= _RATE_LIMIT:
        return False
    times.append(now)
    return True


def _assets_root() -> Path:
    root = os.environ.get("HESPERIA_ASSETS_ROOT")
    if root and Path(root).is_dir():
        d = Path(root) / "lexicon" / "curated"
        if d.is_dir():
            return d
    return Path(__file__).resolve().parents[2] / "lexicon" / "curated"


def _same_dominant(metrics1: dict, metrics2: dict) -> bool:
    v1 = metrics1.get("macro_domain_vector") or metrics1.get("dominant_macro_domain")
    v2 = metrics2.get("macro_domain_vector") or metrics2.get("dominant_macro_domain")
    if isinstance(v1, list) and isinstance(v2, list):
        i1 = max(range(len(v1)), key=lambda i: v1[i]) if v1 else -1
        i2 = max(range(len(v2)), key=lambda i: v2[i]) if v2 else -1
        return i1 == i2
    return False


def _confidence_delta(d1: dict, d2: dict) -> str:
    c1 = d1.get("TRUST_TIER") or d1.get("OUTPUT_TRUST_TAG") or ""
    c2 = d2.get("TRUST_TIER") or d2.get("OUTPUT_TRUST_TAG") or ""
    return "same" if c1 == c2 else "different"


def create_app():
    from fastapi import FastAPI, HTTPException, Request
    from fastapi.responses import JSONResponse
    from pydantic import BaseModel

    app = FastAPI(
        title="HESPERIA API",
        description="Structural analysis. Endpoints: analyze, compare, batch-analyze.",
        version="1.0",
    )

    def _safe_response(data: dict | list):
        from runtime.shipping.schema_guard import validate_against_public_schema
        validate_against_public_schema(data)
        return JSONResponse(
            content=json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False),
            media_type="application/json",
        )

    def _neutral_500() -> JSONResponse:
        return JSONResponse(
            status_code=500,
            content={"error": "internal_processing_error"},
        )

    @app.exception_handler(ValueError)
    def _handle_value_error(request: Request, exc: ValueError) -> JSONResponse:
        return _neutral_500()

    @app.exception_handler(KeyError)
    def _handle_key_error(request: Request, exc: KeyError) -> JSONResponse:
        return _neutral_500()

    @app.exception_handler(TypeError)
    def _handle_type_error(request: Request, exc: TypeError) -> JSONResponse:
        return _neutral_500()

    @app.exception_handler(Exception)
    def _public_error_boundary(request: Request, exc: Exception) -> JSONResponse:
        from fastapi import HTTPException
        if isinstance(exc, HTTPException):
            raise exc
        return _neutral_500()

    @app.on_event("startup")
    def _startup_fingerprint():
        import sys
        try:
            from runtime.shipping.env_guard import check_hesperia_env
            check_hesperia_env(strict=False)
        except Exception:
            pass
        if os.environ.get("HESPERIA_SCHEMA_SHA256"):
            try:
                from runtime.shipping.schema_integrity import verify_public_schema_sha256
                if not verify_public_schema_sha256():
                    print("HESPERIA schema integrity check failed (SHA256 mismatch)", file=sys.stderr)
            except Exception:
                pass
        try:
            from runtime.shipping.version_info import VERSION
            ver = VERSION
        except Exception:
            ver = "0.4.1"
        print("HESPERIA runtime initialized", file=sys.stderr)
        print(f"version: {ver}", file=sys.stderr)
        print("mode: sealed_evaluator", file=sys.stderr)

    class AnalyzeBody(BaseModel):
        text: str = ""

    class CompareBody(BaseModel):
        text1: str = ""
        text2: str = ""

    class BatchAnalyzeBody(BaseModel):
        texts: list[str] = []

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.get("/version")
    def version() -> dict[str, str]:
        try:
            from runtime.shipping.version_info import VERSION, COMMIT, BUILD
            return {"version": VERSION, "commit": COMMIT, "build": BUILD or "unknown"}
        except Exception:
            return {"version": "0.4.1", "commit": "unknown", "build": "unknown"}

    @app.post("/analyze")
    def analyze(body: AnalyzeBody):
        if not _rate_limit():
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
        from core.services.analysis_service import run_structural_analysis
        assets = _assets_root()
        result = run_structural_analysis(body.text, assets_root=assets, stages="full")
        return _safe_response(result)

    @app.post("/compare")
    def compare(body: CompareBody):
        if not _rate_limit():
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
        from core.services.analysis_service import run_structural_analysis
        assets = _assets_root()
        r1 = run_structural_analysis(body.text1, assets_root=assets, stages="full")
        r2 = run_structural_analysis(body.text2, assets_root=assets, stages="full")
        d1 = (r1.get("L7") or {})
        d2 = (r2.get("L7") or {})
        dom1 = (r1.get("usf") or {}).get("raw_metrics") or {}
        dom2 = (r2.get("usf") or {}).get("raw_metrics") or {}
        out = {
            "run": "compare",
            "text1_preview": body.text1[:80],
            "text2_preview": body.text2[:80],
            "result1_trust": d1.get("OUTPUT_TRUST_TAG"),
            "result2_trust": d2.get("OUTPUT_TRUST_TAG"),
            "dominant_match": _same_dominant(dom1, dom2),
            "confidence_delta": _confidence_delta(d1, d2),
        }
        return _safe_response(out)

    @app.post("/batch-analyze")
    def batch_analyze(body: BatchAnalyzeBody):
        if not _rate_limit():
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
        if len(body.texts) > 100:
            raise HTTPException(status_code=400, detail="Maximum 100 texts per request")
        from core.services.analysis_service import run_structural_analysis_batch
        assets = _assets_root()
        results = run_structural_analysis_batch(body.texts, assets_root=assets)
        return _safe_response(results)

    return app


# License gate at app load (fail fast before server binds)
if not _license_ok():
    raise RuntimeError("License check failed; cannot start API")

app = create_app()


if __name__ == "__main__":
    import uvicorn
    host = os.environ.get("HESPERIA_API_HOST", "0.0.0.0")
    port = int(os.environ.get("HESPERIA_API_PORT", "8000"))
    uvicorn.run(app, host=host, port=port)
