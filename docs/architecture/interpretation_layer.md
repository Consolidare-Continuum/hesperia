# Interpretation Layer (Layer-10) — Architecture

## Role

Layer-10 is **structured interpretation**, not prose. It converts Layer-7 (propagation), Layer-8 (shadow), and Layer-9 (structural logic) outputs into a single canonical structural meaning used by USF and fingerprinting.

## Position in Pipeline

```
L7 propagation → L8 shadow correction → L9 structural logic → L10 structured interpretation → USF / fingerprint / serializer
```

- **Inputs:** logic_metrics (L9), shadow_metrics (L8), propagation_metrics (L7), dynamism_metrics (L6). Optional: legacy_logic_outputs for compatibility bridging only.
- **Outputs:** interpretation_metrics — a deterministic, schema-stable dict (structural_state, dominant_area_id, dominance_strength, entropy_state, tension_state, propagation_state, active_events, interpretation_flags, event_summary, interpretation_diagnostics).

## What Layer-10 Is Not

- It does **not** produce freeform text or natural-language explanations.
- It does **not** implement new numeric formulas; classification is rule-based using existing diagnostics and logic events.
- It does **not** duplicate rule evaluation; it consumes logic_metrics from Layer-9.

## Canonical Upstream for USF

USF generation uses **interpretation_metrics** as the canonical source for structural_state, active_events, interpretation_flags, and related fields. The legacy logic_outputs path is **transitional only** and must not remain the primary source of structural meaning.

## Modules

- **state_classifier.py** — classify_structural_state, classify_entropy_state, classify_tension_state, classify_propagation_state (rule-based, deterministic).
- **event_summarizer.py** — extract_active_events, build_event_summary (flatten L9 events to canonical names and counts).
- **flag_builder.py** — build_interpretation_flags from structural state, events, and diagnostics.
- **diagnostics.py** — build_interpretation_diagnostics (dominant_area_id, dominance_strength, rules_triggered_count, entropy_after_shadow, tension_after_shadow, propagation_spread, structural_state_reason, legacy_logic_bridge_used).
- **engine.py** — compute_interpretation_metrics(...) assembles state, classification, flags, and diagnostics into interpretation_metrics.

## Dependency Rule

- **sphere/interpretation** may depend on sphere/logic, sphere/shadow, sphere/propagation, sphere/dynamism for inputs only.
- **sphere/interpretation** must not implement math; it uses thresholds and existing diagnostic fields only.
