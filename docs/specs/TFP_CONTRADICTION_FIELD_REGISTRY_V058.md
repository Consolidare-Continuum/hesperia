# TFP Contradiction Field Registry v0.5.8

Canonical registry for contradiction fields. One field name = one meaning.

## Core metrics

| Field | Type | Range/Shape | Meaning | Producer | Consumers | Required when | Deprecated aliases |
|---|---|---|---|---|---|---|---|
| `raw_contradiction_load` | float | 0..1 | contradiction before qualification | `crossplane_contradiction.py` | analyze/inspector/gating | coupling active | none |
| `effective_contradiction_load` | float | 0..1 | operational contradiction burden | `crossplane_contradiction.py` | analyze/inspector/gating | coupling active | none |
| `contradiction_confidence_mean` | float | 0..1 | trust in contradiction evidence | `crossplane_contradiction.py` | analyze/inspector/gating | coupling active | none |
| `global_contradiction_load` | float | 0..1 | canonical global contradiction load | `crossplane_contradiction.py` | analyze/inspector/gating | coupling active | none |
| `cross_area_contradiction_mass` | float | 0..1 | cross-area contradiction coupling mass | `crossplane_contradiction.py` | analyze/topology/inspector | coupling active | none |

## Structural metrics

| Field | Type | Range/Shape | Meaning | Producer | Consumers | Required when | Deprecated aliases |
|---|---|---|---|---|---|---|---|
| `area_contradiction_pressure` | map[str,float] | area->0..1 | area-distributed contradiction pressure | `crossplane_contradiction.py` | inspector | coupling active | none |
| `family_contradiction_pressure` | map[str,float] | family->0..1 | family-distributed contradiction pressure | `crossplane_contradiction.py` | inspector | coupling active | none |
| `family_fragmentation_summary` | object | `{global_family_fragmentation,...}` | family fragmentation overview | `family_contradiction.py` via crossplane package | analyze/inspector | coupling active | none |
| `family_cross_area_bridge_mass` | float | 0..1 | bridge contradiction across areas by family | `family_contradiction.py` | inspector/gating | coupling active | none |
| `family_intra_area_conflict_mass` | float | 0..1 | within-area family contradiction mass | `family_contradiction.py` | inspector | coupling active | none |

## Dynamic metrics

| Field | Type | Range/Shape | Meaning | Producer | Consumers | Required when | Deprecated aliases |
|---|---|---|---|---|---|---|---|
| `segment_contradiction_loads` | list[object] | per segment | contradiction over timeline segments | `topology_contradiction_coupling.py` via crossplane package | topology/inspector | coupling active | none |
| `transition_pressure` | list[float] | 0..1 per transition | contradiction pressure between segment neighbors | `topology_contradiction_coupling.py` via crossplane package | topology/inspector | coupling active | none |
| `activation_conflict_load` | float | 0..1 | overt/activation-level conflict burden | `crossplane_contradiction.py` | analyze/inspector/gating | coupling active | none |
| `latent_conflict_load` | float | 0..1 | latent/suppressed conflict burden | `contradiction_negation.py` via crossplane package | analyze/inspector/gating | coupling active | none |

## Qualification metrics

| Field | Type | Range/Shape | Meaning | Producer | Consumers | Required when | Deprecated aliases |
|---|---|---|---|---|---|---|---|
| `uncertainty_adjusted_conflict_index` | float | 0..1 | contradiction adjusted by uncertainty quality | `contradiction_uncertainty.py` via crossplane package | analyze/inspector | coupling active | none |
| `lexical_semantic_conflict_split` | object | lexical/ambiguity/semantic components | decomposition of contradiction source | `contradiction_uncertainty.py` via crossplane package | analyze/inspector | coupling active | none |
| `runtime_vs_calibration_conflict_split` | object | runtime vs calibration floats | split of likely runtime-real vs calibration-pathology conflict | `contradiction_feedback.py` via crossplane package | analyze/inspector/gating | coupling active | none |
| `contradiction_mode_summary` | object | mode shares | negation/inhibition-driven mode composition | `contradiction_negation.py` via crossplane package | analyze/inspector | coupling active | none |

## Product/governance metrics

| Field | Type | Range/Shape | Meaning | Producer | Consumers | Required when | Deprecated aliases |
|---|---|---|---|---|---|---|---|
| `conflict_integrity_score` | float | 0..1 | integrity quality for promotion | `inspect_tfp_bundle_output.py` | release tools/docs | inspect artifact present | none |
| `promotion_conflict_verdict` | enum | PASS/QUALIFIED_PASS/FAIL | promotion decision from conflict integrity | `inspect_tfp_bundle_output.py` | release tools/docs | inspect artifact present | none |
| `release_conflict_gates` | object | structured gates | machine-readable gate states and reasons | `inspect_tfp_bundle_output.py` + gating helper | release tools/docs | inspect artifact present | none |
| `conflict_release_summary` | object | compact summary | compact failed/warn gate summary | `inspect_tfp_bundle_output.py` | bundle manifest/main context | inspect artifact present | none |

## Forbidden vague synonyms

- `conflict_score`
- `tension_score`
- `semantic_conflict_score`
- `conflict_pressure`
- `contradiction_pressure`
- `semantic_tension`

These are forbidden unless formally added in a future versioned registry update.

