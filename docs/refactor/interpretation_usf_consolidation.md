# Interpretation and USF Consolidation

## Why Layer-10 Exists

After Layer-9, **logic_metrics** became the structural truth (triggered rules, events, logic_diagnostics). A separate legacy path still produced **logic_outputs** from `evaluate_rules(facts, rule_spec_path)` for USF and older flows. That split meant:

- Pipeline ended with parallel outputs instead of one canonical structural result.
- USF could be driven by legacy logic_outputs instead of the corrected L7→L8→L9 path.

Layer-10 (structured interpretation) exists to:

1. Consume logic_metrics, shadow_metrics, propagation_metrics, and dynamism_metrics in one place.
2. Produce a single **interpretation_metrics** object (deterministic, schema-stable).
3. Serve as the **canonical upstream** for USF, so structural meaning flows from interpretation_metrics, not from legacy logic_outputs.

## Reconciling logic_metrics and logic_outputs

- **logic_metrics** — Output of the Layer-9 rule engine (corrected vectors, propagation, dynamism). This is the canonical structural signal.
- **logic_outputs** — Legacy format (triggered_rules, logic_flags, structural_diagnostics) from the older evaluate_rules path.

Reconciliation policy:

- **Canonical:** logic_metrics + interpretation_metrics define the structural result.
- **Compatibility:** logic_outputs may be passed into Layer-10 as `legacy_logic_outputs` and appear under USF `compatibility` metadata (e.g. `legacy_logic_outputs_present`, `legacy_logic_bridge_used`). It must not drive state classification.

## Canonical Data Flow

```
propagation_metrics (L7)
  → shadow_metrics (L8)
  → logic_metrics (L9)
  → interpretation_metrics (L10)
  → USF / fingerprint / serializer / comparator
```

USF generation must use interpretation_metrics as the primary source for structural_state, active_events, interpretation_flags, and related fields. logic_outputs remain in the USF artifact for backward compatibility but are not the source of truth for interpretation.

## Backward Compatibility Policy

- When **interpretation_metrics** is present, USF canonical fields (structural_state, active_events, interpretation_flags, etc.) are taken from it.
- When **interpretation_metrics** is absent, build_usf_object still succeeds; canonical interpretation fields are simply not set.
- Legacy logic_outputs can be included in the pipeline and in USF under compatibility metadata; legacy_logic_bridge_used is set to False when interpretation_metrics is the source.

## Future Role of Prolog / Natural-Language Generation

Structured interpretation (Layer-10) is the single deterministic structural summary. Future work may add:

- Prolog or other reasoning over interpretation_metrics.
- Natural-language generation that consumes interpretation_metrics (and optionally logic_metrics) to produce human-readable explanations.

Such layers must sit **downstream** of interpretation_metrics and must not replace or bypass the canonical interpretation path for USF.
