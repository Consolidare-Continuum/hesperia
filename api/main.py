# Hesperia Analyze API — POST /hesperia/analyze (OpenAI GPT contract)
from __future__ import annotations

import json
import logging
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse

from .analyze import build_analyze_response
from .schemas import HesperiaAnalyzeRequest, HesperiaAnalyzeResponse

# Service-wide single log file, Apache-style with timestamping
LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "hesperia-api.log"
_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%d/%b/%Y:%H:%M:%S"))
_log = logging.getLogger("hesperia_api")
_log.setLevel(logging.INFO)
_log.addHandler(_handler)
_log.propagate = False


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    # no startup/shutdown needed; Chroma is external


HESPERIA_VERSION = "0.2.0.1"

app = FastAPI(
    title="Hesperia Analyze API",
    description="HESPERIA semantic analysis for natural language text. Exposed for OpenAI GPT.",
    version=HESPERIA_VERSION,
    lifespan=lifespan,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS", "HEAD"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.get("/health")
def health():
    """Boring, compatible health for all clients (OpenAI fetcher, etc.). Always 200 JSON."""
    return JSONResponse(
        content={"ok": True, "service": "hesperia", "version": HESPERIA_VERSION},
        status_code=200,
        media_type="application/json",
    )


@app.options("/health")
@app.options("/hesperia/analyze")
def options_preflight():
    """CORS preflight: return 200 so OpenAI/browsers get Allow + CORS headers."""
    return JSONResponse(content={}, status_code=200, media_type="application/json")


PRIVACY_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Privacy — Hesperia (hesperia.prichindel.com)</title>
</head>
<body>
  <h1>Privacy &amp; terms</h1>
  <p><strong>Hesperia Analyze API</strong> (hesperia.prichindel.com) is developed under the <strong>MIT License</strong> by <strong>Atomic Commit Team</strong>.</p>
  <ul>
    <li>Not a public service; not sellable.</li>
    <li>You may use it as is. All rights reserved. No guarantees given.</li>
    <li>OpenAI main and basic policies must be respected when using this API.</li>
    <li>Research project with possible industrial use.</li>
  </ul>
  <p>See the repository for full license text. Data sent to <code>/hesperia/analyze</code> is processed for semantic analysis and is not stored for purposes other than serving the request.</p>
</body>
</html>
"""


@app.get("/privacy", response_class=HTMLResponse)
def privacy():
    """Privacy and terms: MIT, Atomic Commit Team, not public/sellable, use as is, no guarantees, OpenAI policies respected, research project."""
    return PRIVACY_HTML


def _trunc(s: str, max_len: int = 500) -> str:
    s = (s or "").replace("\n", " ").strip()
    return s[:max_len] + ("..." if len(s) > max_len else "")


# Max request text length (return 413 if exceeded)
MAX_TEXT_LEN = 10_000


def _error_json(code: int, message: str) -> JSONResponse:
    """Stable JSON error envelope for Actions (no HTML, no plain text)."""
    return JSONResponse(
        content={"error": True, "message": message, "code": code},
        status_code=code,
        media_type="application/json",
    )


@app.exception_handler(HTTPException)
def http_exception_handler(request, exc: HTTPException):
    """Ensure all HTTP errors return JSON (Actions-friendly)."""
    return _error_json(exc.status_code, exc.detail)


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc: RequestValidationError):
    """Invalid request (e.g. missing/invalid body) → 400 JSON."""
    try:
        err = exc.errors()[0] if exc.errors() else {}
        msg = err.get("msg", "Invalid request")
    except Exception:
        msg = "Invalid request"
    return _error_json(400, str(msg))


@app.exception_handler(Exception)
def unhandled_exception_handler(request: Request, exc: Exception):
    """Last-resort JSON errors so clients never receive HTML on failures."""
    _log.error('"%s %s" 500 unhandled_error=%s', request.method, request.url.path, json.dumps(str(exc)))
    return _error_json(500, "Internal server error")


@app.post("/hesperia/analyze", response_model=HesperiaAnalyzeResponse)
def hesperia_analyze(req: HesperiaAnalyzeRequest):
    """POST only. Content-Type: application/json. Body: {"text": "..."}. Returns 200 JSON or stable error JSON."""
    asked = _trunc(req.text)
    if len(req.text) > MAX_TEXT_LEN:
        _log.warning('"POST /hesperia/analyze" 413 asked_len=%d', len(req.text))
        return _error_json(413, "Request text too large")
    try:
        options = req.options
        out = build_analyze_response(
            req.text,
            include_supporting_statements=options.include_supporting_statements if options else True,
            max_supporting_statements=options.max_supporting_statements if options else 10,
            return_region_coordinates=options.return_region_coordinates if options else True,
            return_metrics=options.return_metrics if options else True,
        )
        result_dict = HesperiaAnalyzeResponse.model_validate(out).model_dump()
        _log.info(
            '"POST /hesperia/analyze" 200 asked=%s returned=%s',
            json.dumps(asked),
            json.dumps(result_dict),
        )
        return JSONResponse(
            content=result_dict,
            status_code=200,
            media_type="application/json",
        )
    except Exception as e:
        _log.error(
            '"POST /hesperia/analyze" 500 asked=%s error=%s',
            json.dumps(asked),
            json.dumps(str(e)),
        )
        return _error_json(500, str(e))
