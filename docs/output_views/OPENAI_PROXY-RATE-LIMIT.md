# OpenAI proxy — env and rate limit (T50 / T25)

**Feature flag:** `HESPERIA_OUTPUT_VIEWS_OPENAI_PROXY` — default `False`. When `True`, POST `/inspector/<session_id>/openai-proxy/` forwards the built `messages[]` to `https://api.openai.com/v1/chat/completions`.

| Variable | Role |
|----------|------|
| `HESPERIA_OUTPUT_VIEWS_OPENAI_PROXY` | `1` / `true` to enable proxy route |
| `OPENAI_API_KEY` | Required when proxy enabled (env only; never commit) |
| `OPENAI_PROXY_MODEL` | Default `gpt-4o-mini` |
| `OPENAI_PROXY_RATE_PER_MINUTE` | Max POSTs per client IP per rolling minute bucket (default **30**) |

**Implementation:** `django.core.cache` LocMem (per-process). **Production:** replace with Redis-backed cache for multi-worker accuracy (Abelard).

**Logging (T25):** Success path logs `model` and elapsed **ms** only — **no** full segment or message bodies.

`SIGNED: Gena | Hesperia | 2026-04-07 | T50`
