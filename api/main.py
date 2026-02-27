"""
Hesperia Analyze API — FastAPI. GET /health, POST /hesperia/analyze.
GPT Actions compliant: Bearer auth, OpenAPI 3.x, strict body (text only), rate limit + hardening via nginx.
"""
from __future__ import annotations

import logging
import os
import uuid
from pathlib import Path
from typing import Any

# Hesperia root (parent of api/); v0.6 assets at root/assets/v06
_HESPERIA_ROOT = Path(__file__).resolve().parent.parent
_ASSETS_ROOT = _HESPERIA_ROOT / "assets"

from fastapi import Depends, FastAPI, Request, Security
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, ConfigDict, Field

DEFAULT_TEXT_CAP = 10_000
API_VERSION = "0.6.0"

# Bearer token: GPT Actions uses Authentication = API Key, Key type = Bearer.
# HESPERIA_API_KEY = required. HESPERIA_API_KEY_NEXT = optional for rotation (accept either; swap then clear NEXT).
# If both unset, /hesperia/analyze returns 503 (no open-by-default).
API_KEY = os.environ.get("HESPERIA_API_KEY", "").strip()
API_KEY_NEXT = os.environ.get("HESPERIA_API_KEY_NEXT", "").strip()
HTTP_BEARER = HTTPBearer(auto_error=False)


def verify_bearer(credentials: HTTPAuthorizationCredentials | None = Security(HTTP_BEARER)) -> None:
    """Only /hesperia/analyze uses this; /health and /openapi.json have no auth."""
    if not API_KEY and not API_KEY_NEXT:
        raise PermissionError("Server not configured with HESPERIA_API_KEY")
    if not credentials:
        raise PermissionError("Missing Authorization: Bearer")
    token = credentials.credentials
    if token != API_KEY and token != API_KEY_NEXT:
        raise PermissionError("Invalid API key")


def custom_openapi():
    from fastapi.openapi.utils import get_openapi
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    openapi_schema["servers"] = [{"url": "https://hesperia.prichindel.com", "description": "Production"}]
    openapi_schema.setdefault("components", {}).setdefault("securitySchemes", {})["bearerAuth"] = {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
        "description": "API Key as Bearer token (GPT Actions: API Key → Bearer)",
    }
    # Only /hesperia/analyze has security; /health and /openapi.json do not. List nginx-emitted codes so builder doesn't treat as unexpected.
    for path, methods in openapi_schema.get("paths", {}).items():
        if "/hesperia/analyze" in path and "post" in methods:
            methods["post"]["operationId"] = "hesperiaAnalyze"
            methods["post"]["security"] = [{"bearerAuth": []}]
            r = methods["post"].setdefault("responses", {})
            r["403"] = {"description": "Method not allowed (nginx limit_except)", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/ErrorBody"}}}}
            r["415"] = {"description": "Content-Type must be application/json", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/ErrorBody"}}}}
            r["429"] = {"description": "Too Many Requests (rate limit)", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/ErrorBody"}}}}
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app = FastAPI(
    title="Hesperia Analyze API",
    version=API_VERSION,
    description="Semantic attribution: POST /hesperia/analyze with Bearer token. GPT Actions: use API Key → Bearer.",
    servers=[{"url": "https://hesperia.prichindel.com", "description": "Production"}],
    openapi_url="/openapi.json",
    docs_url=None,
    redoc_url=None,
)
app.openapi = custom_openapi


@app.on_event("startup")
def _startup_warn_next() -> None:
    """Warn if NEXT key is set so ops don't leave dual-key forever."""
    if API_KEY_NEXT:
        logging.warning("HESPERIA_API_KEY_NEXT is set; rotate then clear it to avoid permanent two-key drift.")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)


class AnalyzeBody(BaseModel):
    """Request body: text (required); r1_r4 (optional) to include R1–R4 reading-scale pipeline in extended."""
    model_config = ConfigDict(extra="forbid")
    text: str = Field(..., min_length=1, max_length=DEFAULT_TEXT_CAP, description="Input text for semantic attribution")
    r1_r4: bool = Field(default=False, description="If true, run R1–R4 pipeline and include units + book_profile in extended")


class ErrorBody(BaseModel):
    error: bool = True
    message: str
    code: int


@app.middleware("http")
async def request_id_middleware(request: Request, call_next):
    rid = request.headers.get("X-Request-ID") or str(uuid.uuid4())
    response = await call_next(request)
    response.headers["X-Request-ID"] = rid
    return response


@app.get(
    "/health",
    response_model=None,
    summary="Health check",
    description="No auth required. Returns service and version.",
)
def health() -> dict[str, Any]:
    return {"ok": True, "service": "hesperia", "version": API_VERSION}


@app.post(
    "/hesperia/analyze",
    response_model=None,
    status_code=200,
    summary="Semantic attribution",
    description="Requires Authorization: Bearer <key>. Returns result (6-key) and extended (second output). Set body.r1_r4=true to include R1–R4 units and book_profile in extended.",
    operation_id="hesperiaAnalyze",
    responses={
        200: {"description": "Success. Body: { result: 6-key, extended: { total_tokens, ... optional r1_r4 } }", "content": {"application/json": {"example": {
            "result": {"dominant_area": 0, "dominant_family": 0, "governance": 0.0, "loopability": 0.0, "tension_energy": 0.0, "obstacle_score": 0.0},
            "extended": {"total_tokens": 0, "matched_tokens": 0, "unmatched_tokens": 0},
        }}}},
        400: {"description": "Bad request (text missing, no tokens matched, etc.)", "model": ErrorBody},
        401: {"description": "Missing or invalid Bearer token", "model": ErrorBody},
        413: {"description": "Request body too large", "model": ErrorBody},
        500: {"description": "Internal error (no stack trace)", "model": ErrorBody},
        503: {"description": "Service not configured (HESPERIA_API_KEY unset)", "model": ErrorBody},
        422: {"description": "Validation error (e.g. extra fields, invalid body)", "model": ErrorBody},
    },
)
async def hesperia_analyze(
    body: AnalyzeBody,
    request: Request,
    _: None = Depends(verify_bearer),
) -> JSONResponse:
    try:
        from sphere_rag.analyze import analyze

        minimal, extended = analyze(
            body.text,
            text_cap=DEFAULT_TEXT_CAP,
            assets_root=_ASSETS_ROOT,
            r1_r4=body.r1_r4,
        )
        return JSONResponse(content={"result": minimal, "extended": extended})
    except ValueError as e:
        msg = str(e)
        if "text_missing" in msg:
            return JSONResponse(status_code=400, content={"error": True, "message": "text missing", "code": 400})
        if "semantic_vacuum" in msg:
            return JSONResponse(
                status_code=400,
                content={"error": True, "message": "No tokens matched any dictionary", "code": 400},
            )
        if "metric_nan_inf" in msg:
            return JSONResponse(status_code=500, content={"error": True, "message": "Internal metric error", "code": 500})
        return JSONResponse(status_code=400, content={"error": True, "message": msg[:500], "code": 400})
    except Exception:
        return JSONResponse(
            status_code=500,
            content={"error": True, "message": "Internal error", "code": 500},
        )


@app.exception_handler(PermissionError)
async def permission_handler(_request: Request, exc: PermissionError) -> JSONResponse:
    msg = str(exc)
    if "not configured" in msg:
        return JSONResponse(status_code=503, content={"error": True, "message": "Service not configured", "code": 503})
    return JSONResponse(
        status_code=401,
        content={"error": True, "message": "Missing or invalid Authorization", "code": 401},
    )


@app.exception_handler(RequestValidationError)
async def validation_handler(_request: Request, exc: RequestValidationError) -> JSONResponse:
    """Stable 422: single boring message. No user input, no Pydantic internals."""
    msg = "Invalid request body"
    for e in exc.errors() or []:
        if e.get("type") == "extra_forbidden" or "extra" in (e.get("msg") or "").lower():
            msg = "Invalid request body: extra fields not permitted"
            break
    return JSONResponse(
        status_code=422,
        content={"error": True, "message": msg, "code": 422},
    )


# 413 from body size is handled by FastAPI when body > max_length (Pydantic); larger payloads may hit nginx first.
# 401 from HTTPBearer (missing/invalid header) is automatic; we override only for wrong key via PermissionError.
