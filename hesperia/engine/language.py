"""Canonical Hesperia language: context variables and constructors."""

from __future__ import annotations

from typing import Any, TypedDict

TEXT = "text"
TOKENS = "tokens"
CONCEPT_HITS = "concept_hits"
FAMILIES = "families"
FAMILY_SCORES = "family_scores"
AREAS = "areas"
AREA_SCORES = "area_scores"
METRICS = "metrics"
ARTIFACTS = "artifacts"
SIGNALS = "signals"
ENGINE_CONTEXT = "engine_context"
TFP_VECTOR = "tfp_vector"
TFP_PROFILE = "tfp_profile"
TFP_CONFLICTS = "tfp_conflicts"


class HesperiaSignal(TypedDict):
    family_id: int
    strength: float
    source: str | None


class HesperiaResultRef(TypedDict, total=False):
    area_vector: list[float]
    family_vector: list[float]
    dominant_area: int
    dominant_family: int
    tension: float
    loopability: float
    stability: float
    failure_flags: list[str]
    schema_version: str
    fingerprint: str
    deterministic_hash: str


class HesperiaContext(TypedDict):
    text: str
    tokens: list[str]
    concept_hits: list[str]
    families: list[str]
    family_scores: dict[str, float]
    areas: list[str]
    area_scores: dict[str, float]
    metrics: dict[str, Any]
    artifacts: dict[str, Any]
    signals: list[HesperiaSignal]
    engine_context: dict[str, Any]
    tfp_vector: dict[str, float]
    tfp_profile: dict[str, Any]
    tfp_conflicts: list[str]


def build_ctx(text: str) -> HesperiaContext:
    return {
        TEXT: str(text),
        TOKENS: [],
        CONCEPT_HITS: [],
        FAMILIES: [],
        FAMILY_SCORES: {},
        AREAS: [],
        AREA_SCORES: {},
        METRICS: {},
        ARTIFACTS: {},
        SIGNALS: [],
        ENGINE_CONTEXT: {},
        TFP_VECTOR: {},
        TFP_PROFILE: {},
        TFP_CONFLICTS: [],
    }


def language_schema() -> dict[str, Any]:
    return {
        "ctx": {
            TEXT: "str",
            TOKENS: "list[str]",
            CONCEPT_HITS: "list[str]",
            FAMILIES: "list[str]",
            FAMILY_SCORES: "dict[str,float]",
            AREAS: "list[str]",
            AREA_SCORES: "dict[str,float]",
            METRICS: "dict[str,Any]",
            ARTIFACTS: "dict[str,Any]",
            SIGNALS: "list[signal]",
            ENGINE_CONTEXT: "dict[str,Any](read-only for modules)",
            TFP_VECTOR: "dict[str,float]",
            TFP_PROFILE: "dict[str,Any]",
            TFP_CONFLICTS: "list[str]",
        },
        "signal": {"family_id": "int", "strength": "float", "source": "str|None"},
        "result": {
            "area_vector": "list[float]",
            "family_vector": "list[float]",
            "dominant_area": "int",
            "dominant_family": "int",
            "tension": "float",
            "loopability": "float",
            "stability": "float",
            "failure_flags": "list[str]",
            "schema_version": "str",
            "fingerprint": "str",
            "deterministic_hash": "str",
        },
    }


def validate_signal(signal: dict[str, Any]) -> HesperiaSignal:
    if not isinstance(signal, dict):
        raise ValueError("signal_invalid_type")
    if "family_id" not in signal:
        raise ValueError("signal_missing_family_id")
    if "strength" not in signal:
        raise ValueError("signal_missing_strength")
    family_id = signal["family_id"]
    strength = signal["strength"]
    source = signal.get("source")
    if not isinstance(family_id, int):
        raise ValueError("signal_invalid_family_id_type")
    if not isinstance(strength, (int, float)):
        raise ValueError("signal_invalid_strength_type")
    if source is not None and not isinstance(source, str):
        raise ValueError("signal_invalid_source_type")
    return {
        "family_id": int(family_id),
        "strength": float(strength),
        "source": source,
    }


def validate_signals(signals: list[dict[str, Any]] | None) -> list[HesperiaSignal]:
    if signals is None:
        return []
    if not isinstance(signals, list):
        raise ValueError("signals_invalid_type")
    return [validate_signal(s) for s in signals]

