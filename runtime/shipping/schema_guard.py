# HESPERIA — Public schema validation. Fail if internal-revealing key appears before serialization.
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

"""Runtime assertion before serialization. Walks every node in the JSON tree."""

from __future__ import annotations


FORBIDDEN_KEY_SUBSTRINGS = (
    "sphere", "hex", "topology", "bridge", "side_id", "area_id", "family_id",
    "layer_", "adjacency", "propagation_path", "propagation_algorithm", "grid", "graph", "embedding",
    "vector_space", "internal_layer", "topology_index", "area11", "family240",
)

# Module/class names that must never appear in any error response
FORBIDDEN_RESPONSE_SUBSTRINGS = (
    "core.services",
    "runtime.shipping",
    "analysis_service",
)


def _check_key(key: str) -> None:
    """Raise ValueError if key contains a forbidden substring."""
    kl = key.lower()
    for bad in FORBIDDEN_KEY_SUBSTRINGS:
        if bad in kl:
            raise ValueError(f"public_schema_violation: key '{key}' contains forbidden term '{bad}'")


def _walk(obj: object) -> None:
    """
    Walk every node in the JSON tree. Check every dict key; recurse into dict values and list elements.
    Ensures nested structures (comparison output, list-of-dicts, etc.) cannot bypass the guard.
    """
    if isinstance(obj, dict):
        for k, v in obj.items():
            _check_key(k)
            _walk(v)
    elif isinstance(obj, list):
        for item in obj:
            _walk(item)


def validate_against_public_schema(output: dict | list) -> None:
    """
    Validate output before serialization. Walks every node; raises ValueError if any key
    (including nested in lists) contains a forbidden substring.
    """
    _walk(output)
