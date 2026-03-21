# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any


def calib_mock_openai() -> bool:
    """When true, ``chat_json`` never calls the network (CI / wiring / dry runs)."""
    v = os.environ.get("HESPERIA_CALIB_MOCK_OPENAI", "").strip().lower()
    return v in ("1", "true", "yes")


def _mock_normalize_from_user(user: str) -> dict[str, Any]:
    idx = user.find("Input:\n")
    if idx < 0:
        return {"items": []}
    rest = user[idx + len("Input:\n") :].strip()
    blob = rest.split("\n\n")[0].strip()
    try:
        payload = json.loads(blob)
    except json.JSONDecodeError:
        return {"items": []}
    if not isinstance(payload, list):
        return {"items": []}
    items: list[dict[str, Any]] = []
    for row in payload:
        if not isinstance(row, dict):
            continue
        st = str(row.get("text", ""))
        items.append(
            {
                "source_text": st,
                "normalized": st.strip().lower(),
                "variants": [],
            }
        )
    return {"items": items}


def _mock_propose_from_user(user: str) -> dict[str, Any]:
    marker = "Normalized lexical items:\n"
    idx = user.find(marker)
    if idx < 0:
        return {"concepts": []}
    rest = user[idx + len(marker) :]
    end = rest.find("\n\nReturn")
    if end < 0:
        blob = rest.strip()
    else:
        blob = rest[:end].strip()
    try:
        chunk = json.loads(blob)
    except json.JSONDecodeError:
        return {"concepts": []}
    if not isinstance(chunk, list) or not chunk:
        return {"concepts": []}
    mc_m = re.search(r"Cap total concepts at (\d+)", user)
    cap = int(mc_m.group(1)) if mc_m else 80
    concepts: list[dict[str, Any]] = []
    for ph in chunk[:cap]:
        if not str(ph).strip():
            continue
        p = str(ph).strip()
        concepts.append(
            {
                "concept_id": "mock.lexical.placeholder",
                "labels": [p[:48]],
                "from_lexical": [p],
                "confidence": 0.5,
            }
        )
    return {"concepts": concepts}


def _mock_chat_json(user: str) -> Any:
    """Deterministic stand-in payloads so calibration code runs without OpenAI."""
    if '"add_lexical"' in user or ("Errors:" in user and "Return JSON patch" in user):
        return {
            "add_lexical": [],
            "merge_concepts": [],
            "split_concepts": [],
            "adjust_priorities": [],
            "notes": "HESPERIA_CALIB_MOCK_OPENAI",
        }
    if "Normalized lexical items:" in user and "Return JSON:" in user and "concepts" in user:
        return _mock_propose_from_user(user)
    if "Input:\n" in user and ("items" in user or "source_text" in user):
        return _mock_normalize_from_user(user)
    if "Corpus phrases" in user and "links" in user:
        return {"links": []}
    if (
        "entries" in user
        and "marker" in user.lower()
        and ("return json" in user.lower())
    ):
        return {"entries": []}
    return {}


def load_repo_dotenv() -> None:
    """Load repo-root ``.env`` if present (gitignored); does not override existing env vars."""
    env_path = Path(__file__).resolve().parents[2] / ".env"
    if not env_path.is_file():
        return
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key, val = key.strip(), val.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = val


def get_client():
    try:
        from openai import OpenAI
    except ImportError as e:
        raise ImportError("Install OpenAI SDK: pip install openai") from e
    load_repo_dotenv()
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        raise RuntimeError("OPENAI_API_KEY is not set")
    return OpenAI(api_key=key)


def require_openai_key() -> None:
    """Load repo ``.env`` then fail fast if the key is missing."""
    load_repo_dotenv()
    if not os.environ.get("OPENAI_API_KEY", "").strip():
        raise RuntimeError("OPENAI_API_KEY not set — add to repo .env or export in shell")


def chat_json(
    *,
    system: str,
    user: str,
    model: str | None = None,
    temperature: float = 0.15,
    max_tokens: int | None = None,
) -> Any:
    """Return parsed JSON from model (json_object mode). Large ``links`` payloads need high max_tokens."""
    if calib_mock_openai():
        return _mock_chat_json(user)

    client = get_client()
    model = model or os.environ.get("HESPERIA_CALIB_OPENAI_MODEL", "gpt-4o-mini")
    env_mt = os.environ.get("HESPERIA_CALIB_MAX_OUTPUT_TOKENS", "").strip()
    mt = max_tokens
    if mt is None:
        mt = int(env_mt) if env_mt.isdigit() else 16384
    resp = client.chat.completions.create(
        model=model,
        temperature=temperature,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        max_tokens=mt,
    )
    content = (resp.choices[0].message.content or "").strip()
    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        # Do not issue a second HTTP request with the same (often huge) ``user`` blob: it can fail
        # with 400 "could not parse the JSON body" on the wire, and ru-tfp-align bisection is the
        # correct recovery (smaller phrase batches / higher max_tokens on caller side).
        preview = (content[:240] + "…") if len(content) > 240 else content
        raise RuntimeError(
            f"OpenAI returned non-JSON or truncated JSON ({e!s}); split workload or raise max_tokens. "
            f"assistant_preview={preview!r}"
        ) from e
