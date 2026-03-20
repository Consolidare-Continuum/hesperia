<!--
HESPERIA — RAD. DLCR-HP canon fragment (INT-001).
-->

# SPEC: L2 concept resolution — v0.6.0

**ID:** `HES-SPEC-DLCR-HP-L2`  
**Normative parent:** [SPEC__DLCR_HP_Master_v0_6_0.md](SPEC__DLCR_HP_Master_v0_6_0.md)

## Purpose

**L2** resolves Dict A hits to at most one winning concept per span with auditable tie-breaks.

## Normative rules

- Output validates against `schemas/lexical_concept/resolver_output.schema.json` where applicable.
- Per-span trace must explain winner selection (master §Core invariants).

## Acceptance

- `tests/lexical_concept/test_resolver.py` and `test_resolver_output_schema.py` pass.
- `run_dlcr_pipeline` emits `span_resolutions` deterministically for fixed assets.
