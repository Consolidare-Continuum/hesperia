<!--
HESPERIA — RAD. DLCR-HP canon fragment (INT-001).
-->

# SPEC: L0 raw_text normalization — v0.6.0

**ID:** `HES-SPEC-DLCR-HP-L0`  
**Normative parent:** [SPEC__DLCR_HP_Master_v0_6_0.md](SPEC__DLCR_HP_Master_v0_6_0.md)

## Purpose

**L0** produces canonical text and normalization metadata for deterministic matching.

## Normative rules

- Same raw_text + same normalization resources ⇒ same `canonical_text` for the DLCR chain.
- Implementation: `core.lexical.normalization` (pinned behavior via regression).

## Acceptance

- Unit tests under `tests/lexical_concept/test_normalization.py` pass.
- Version pin recorded in `assets/data/engine_dynamics_v060/VERSION.yaml` (`normalization`).
