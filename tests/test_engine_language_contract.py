from __future__ import annotations

import pytest

from hesperia.engine.context_guard import GuardedContext
from hesperia.engine.language import language_schema, validate_signals


def test_language_schema_has_ctx_signal_result() -> None:
    schema = language_schema()
    assert set(schema.keys()) == {"ctx", "signal", "result"}
    assert "engine_context" in schema["ctx"]


def test_signal_contract_validation_codes() -> None:
    ok = validate_signals([{"family_id": 3, "strength": 0.4, "source": None}])
    assert ok[0]["family_id"] == 3
    with pytest.raises(ValueError, match="signal_missing_family_id"):
        validate_signals([{"strength": 0.1}])
    with pytest.raises(ValueError, match="signal_invalid_strength_type"):
        validate_signals([{"family_id": 1, "strength": "0.1"}])


def test_engine_context_guard_blocks_mutation() -> None:
    ctx = GuardedContext({"engine_context": {}}, protected_keys={"engine_context"})
    with pytest.raises(ValueError, match="engine_context_readonly_mutation_blocked"):
        ctx["engine_context"] = {"x": 1}
    assert "blocked_mutation:engine_context" in ctx.mutation_log
