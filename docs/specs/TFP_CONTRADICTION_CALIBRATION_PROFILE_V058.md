# TFP contradiction calibration profile (v0.5.8)

## Purpose

Tasks 1–10 introduce contradiction handling across activation, topology, DLCR, multiscale, product, inspector, feedback, release gating, and contract. This profile provides **one** disciplined surface for **transform** tuning (normalization, coupling weights, governance thresholds) without making **structural** facts (ontology, contract field names, mode enum names) into knobs.

## Structural vs calibratable

### Must remain structural (not tunable via this profile)

- Concept → family → area mappings and ontology sources  
- Contradiction contract field names and artifact authority rules  
- Release gate **categories** and gate identifiers (not numeric thresholds)  
- Contradiction mode **enum names** and row schema  
- Raw contradiction rows as observed evidence; raw vs effective split; latent vs overt split  
- Requirement that outputs remain trace-visible  

### Calibratable transforms (this profile)

- Contradiction pressure normalization mode and smooth compression  
- Family / area / dynamic inhibition coupling influences  
- Uncertainty-based confidence shaping for effective scores  
- Negation/inhibition mode contribution weights (bounded multipliers on derived splits)  
- Topology segment / transition / momentum responsiveness  
- Feedback diagnostic ranking weights (risk scorers)  
- Release gating numeric thresholds (`pass_threshold`, `qualified_pass_threshold`)  

## Canonical files

| File | Role |
|------|------|
| `assets/data/engine_dynamics_v060/tfp/contradiction_calibration_v1.json` | Single source of truth |
| `hesperia/extensions/triz/contradiction_calibration.py` | Load, validate, defaults, snapshot hash, usage trace |

## Sections and consumers

| Section | Consumers |
|---------|-----------|
| `activation` | `contradiction_coupling.build_*`, `invariant_activation.build_invariant_activation` |
| `uncertainty` | `pair_confidence` (via `enrich_contradiction_rows`) |
| `negation_inhibition` | `pair_effective_activation_latent` |
| `family` | Family pressure / fragmentation / bridge scaling in activation |
| `topology` | `topology_contradiction_coupling`, `run_session_topology` |
| `feedback` | `contradiction_feedback.build_contradiction_feedback_signals` |
| `release_gating` | `evaluate_conflict_integrity` (merged with gate verdict) |
| `constraints` | Validator only (`allow_negative_influence`, `max_global_influence`) |

## Trace requirements

- Every bundle run must record `contradiction_calibration_snapshot` (profile name, version, path, SHA-256, active sections) and `contradiction_calibration_usage` (leaf fields differing from built-in defaults).  
- Inspector must surface validity, missing path, hash mismatch, and trace visibility.  

## Forbidden calibration behaviors

- Renaming or bypassing contract fields  
- Hiding calibration while contradiction coupling is active without an explicit audit flag  
- Negative influences unless `constraints.allow_negative_influence` is true  
- Arbitrary extra top-level keys (validator rejects unknown keys)  

---

SIGNED: Gena (main developer) | Hesperia TFP v0.5.8 Task 11 | 2026-04-14 | calibration surface + docs
