# Engine API v1 Compatibility Policy

API contract id: `engine_api_v1`  
Authority: `hesperia/engine/api.py`

Rules:

- `ENGINE_API_VERSION` is frozen at `engine_api_v1`.
- Public call: `run_engine_api_v1(text, signals=None) -> dict`.
- Returned payload must include the canonical `HesperiaResult` envelope.
- Breaking any function signature or envelope shape requires a new API id (for example `engine_api_v2`).

Gate:

- `tests/test_engine_api_v1.py` must pass in CI.
