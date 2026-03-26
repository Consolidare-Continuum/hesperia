# Hesperia Language Schema v1

Authority: `hesperia/engine/language.py`

## Canonical context (`ctx`)

- `text: str`
- `tokens: list[str]`
- `concept_hits: list[str]`
- `families: list[str]`
- `family_scores: dict[str,float]`
- `areas: list[str]`
- `area_scores: dict[str,float]`
- `metrics: dict[str,Any]`
- `artifacts: dict[str,Any]`
- `signals: list[signal]`
- `engine_context: dict[str,Any]` (read-only for modules)
- `tfp_vector: dict[str,float]`
- `tfp_profile: dict[str,Any]`
- `tfp_conflicts: list[str]`

## Canonical signal

- `family_id: int`
- `strength: float`
- `source: str | None`

Ingress validation error codes (deterministic):

- `signals_invalid_type`
- `signal_invalid_type`
- `signal_missing_family_id`
- `signal_missing_strength`
- `signal_invalid_family_id_type`
- `signal_invalid_strength_type`
- `signal_invalid_source_type`
- `engine_context_readonly_mutation_blocked:<key>`

## Canonical result

- `area_vector: list[float]`
- `family_vector: list[float]`
- `dominant_area: int`
- `dominant_family: int`
- `tension: float`
- `loopability: float`
- `stability: float`
- `failure_flags: list[str]`
- `schema_version: str`
- `fingerprint: str`
- `deterministic_hash: str`

Rule: runtime entrypoints and modules must consume these exact keys and types; no duplicate vocabularies.
