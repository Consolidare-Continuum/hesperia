"""Deterministic concept-to-hex projection."""

from __future__ import annotations


def project_concepts_to_hex(
    concept_weights: dict[str, float],
    anchor_registry: dict[str, str]
) -> tuple[dict[str, float], list[str]]:
    hex_state: dict[str, float] = {}
    degradation_flags: list[str] = []
    for concept_id, weight in concept_weights.items():
        hex_id = anchor_registry.get(concept_id)
        if not hex_id:
            degradation_flags.append(f"missing_anchor:{concept_id}")
            continue
        hex_state[hex_id] = hex_state.get(hex_id, 0.0) + float(weight)
    return hex_state, degradation_flags

