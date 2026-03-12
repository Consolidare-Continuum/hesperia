# Prolog extension (L9b)

## Relationship between deterministic rules and Prolog reasoning

- **Layer-9 (deterministic):** `sphere.logic` evaluates structural rules over shadow, propagation, and dynamism metrics. It produces **logic_metrics** (triggered_rules, events, logic_diagnostics). This is the **primary** structural logic; it is always run and feeds Layer-10 interpretation.
- **Layer-9b (Prolog):** `sphere.prolog_logic` runs optional **forward-chaining inference** over a small knowledge base. Facts are derived from logic_metrics and interpretation_metrics (e.g. event names, structural_state). Rules (e.g. `structural_focus :- dominant_area, entropy_drop`) derive new facts. Output is **prolog_logic** (derived_facts, rule_traces, prolog_diagnostics). It is **secondary**: it extends analysis and does not replace Layer-9.

## Why Prolog remains secondary

- **Canonical path:** USF and interpretation_metrics are defined by L9 + L10. Prolog results are not merged into logic_metrics or interpretation_metrics; they are attached separately as `result["prolog_logic"]`.
- **Optional:** Prolog runs only when `config.enable_prolog` is true. Default is off so that the core pipeline and all tests remain unchanged when the extension is disabled.
- **Additive:** Prolog can derive higher-level predicates (e.g. structural_focus, transition_risk) for downstream consumers (e.g. explanations or guards) without changing the canonical structural output.

## How inference extends structural analysis

- **Inputs:** logic_metrics (triggered_rules, events), interpretation_metrics (active_events, structural_state), optional shadow_metrics.
- **Facts:** Event names and structural_state are turned into Prolog facts (e.g. `dominant_area`, `entropy_drop`, `structural_state(focused_dominant)`).
- **Rules:** Built-in rules (e.g. `structural_focus :- dominant_area, entropy_drop`) derive new facts. Custom rules can be added via engine parameters.
- **Output:** derived_facts (list of {predicate, args}), rule_traces (inference steps), prolog_diagnostics (iterations, counts, errors).

Pipeline: after Layer-10, if `config.enable_prolog`, call `compute_prolog_inference(logic_metrics, interpretation_metrics, shadow_metrics)` and set `result["prolog_logic"]`. Do not merge with logic_metrics.
