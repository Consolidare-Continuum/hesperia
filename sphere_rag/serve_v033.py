#!/usr/bin/env python3
"""
HESPERIA v0.3.3 — HTTP server (26_SPEC §6 + v0.3.3 attribution).
Filename matches version: serve_v033.py for v0.3.3.
GET /health → {"ok": true, "service": "hesperia", "version": "0.3.3"}
POST /hesperia/analyze → minimal 6-key result or error (3 keys).
Flow: text → normalize → tokenize → attribution → traversal → guards (shadow flag in pipeline) → result.
400 text missing / semantic vacuum; 413 length cap; 500 internal / NaN/Inf.
"""

from __future__ import annotations

import json
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
if _SCRIPT_DIR.name == "sphere_rag":
    _ROOT = _SCRIPT_DIR.parent
else:
    _ROOT = _SCRIPT_DIR
sys.path.insert(0, str(_ROOT))

DEFAULT_TEXT_CAP = 10_000
VERSION = "0.3.3"


class HesperiaHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def _cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Type", "application/json; charset=utf-8")

    def _send_error(self, message: str, code: int):
        self.send_response(code)
        self._cors_headers()
        self.end_headers()
        self.wfile.write(json.dumps({
            "error": True,
            "message": message[:500],
            "code": code,
        }).encode("utf-8"))

    def do_GET(self):
        if self.path == "/health" or self.path.rstrip("/") == "/health":
            self.send_response(200)
            self._cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({
                "ok": True,
                "service": "hesperia",
                "version": VERSION,
            }).encode("utf-8"))
            return
        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        if self.path != "/hesperia/analyze" and self.path.rstrip("/") != "/hesperia/analyze":
            self.send_response(404)
            self.end_headers()
            return
        content_length = int(self.headers.get("Content-Length", 0))
        if content_length > DEFAULT_TEXT_CAP:
            self._send_error("Request body too large", 413)
            return
        body = self.rfile.read(content_length) if content_length else b"{}"
        try:
            data = json.loads(body.decode("utf-8")) if body else {}
        except json.JSONDecodeError:
            self._send_error("Invalid JSON", 400)
            return
        if not isinstance(data, dict):
            data = {}
        text = data.get("text", "")
        if not isinstance(text, str):
            text = str(text)
        if not text.strip():
            self._send_error("text missing", 400)
            return
        try:
            from sphere_rag.analyze_v033 import analyze_v033
            minimal, _extended = analyze_v033(text, text_cap=DEFAULT_TEXT_CAP)
            self.send_response(200)
            self._cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps(minimal).encode("utf-8"))
        except ValueError as e:
            msg = str(e)
            if "text_missing" in msg:
                self._send_error("text missing", 400)
            elif "semantic_vacuum" in msg:
                self._send_error("No tokens matched any dictionary", 400)
            elif "metric_nan_inf" in msg:
                self._send_error("Internal metric error", 500)
            else:
                self._send_error(msg or "Bad request", 400)
        except Exception as e:
            self._send_error(str(e)[:500], 500)

    def log_message(self, format, *args):
        pass


def main():
    port = 8765
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass
    server = HTTPServer(("", port), HesperiaHandler)
    print(f"HESPERIA v0.3.3 server: http://127.0.0.1:{port}/health  POST http://127.0.0.1:{port}/hesperia/analyze")
    server.serve_forever()


if __name__ == "__main__":
    main()
