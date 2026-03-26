<!--
HESPERIA — RAD. DLCR-HP canon fragment (INT-001).
-->

# SPEC: Audit output & public slice — v0.6.0

**ID:** `HES-SPEC-DLCR-HP-AUDIT`  
**Normative parent:** [SPEC__DLCR_HP_Master_v0_6_0.md](SPEC__DLCR_HP_Master_v0_6_0.md)

## Purpose

Define **internal-rich** vs **public-safe** summaries (master §Output classes).

## Normative rules

- Internal: full `run_dlcr_pipeline` payload (spans, weights, hex state).
- Public: `hesperia.engine.projection.dlcr_public.project_dlcr_public_summary` — schema-guard-safe keys only.
- Product path merges lexical resolution only when `structural_dlcr_allowed()` (capabilities + env).

## Acceptance

- Resolver/trace JSON validates where schemas apply.
- Default shipping/product measurement unchanged when DLCR env flags are unset.
