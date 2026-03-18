# Commercial TRIZ products (decision intelligence)

**Broader product taxonomy (structural, narrative, fingerprint, domain topology):** [HESPERIA_PRODUCT_LINES.md](HESPERIA_PRODUCT_LINES.md).

Raw engine outputs (`contradictions`, `innovation_clusters`, `narratives`, `atomic_metrics`) are extended with **`commercial_intelligence`** on every `run_triz_analysis_complete` response.

## Core customer signals (`core_signals`)

| Signal | Source formula |
|--------|----------------|
| `policy_tension_index` | mean(contradiction_scores) |
| `policy_coherence_score` | 1 − contradiction_density |
| `innovation_radar_peak_score` | max cluster innovation_score |
| `innovation_pressure_index` | contradiction_density × activation_mass |
| `narrative_penetration_score` | activated_families / total_families |
| `narrative_spillover_index` | spillover_strength (neighbor/source after step 1) |
| `system_tension_index` | semantic_pressure |
| `cross_area_contradiction_rate` | cross-area conflicts / total conflicts |
| `activation_energy` | Σ concept_activation |

## Product groups (under `commercial_intelligence`)

1. **policy_contradiction_products** — tension, coherence, conflict map (hotspots, family density, cross-area), regulatory pair list  
2. **innovation_intelligence_products** — innovation radar ranking, pressure, cross-domain bridging clusters, idea novelty scores  
3. **narrative_intelligence_products** — penetration, propagation speed, spillover, stability, route length  
4. **system_stability_products** — system tension, domain coupling map, structural instability flag  
5. **comparative_intelligence_products** — pointer to `/api/v1/triz/compare`; use `hesperia.engine.triz.compare_triz_corpora(dm_a, dm_b)` for deltas  
6. **monitoring_products_schema** — fields to track in time-series dashboards  

## Data API (Bearer), POST body `{ "triz": <analyze response triz> }`

| Path | Payload |
|------|---------|
| `/api/v1/triz/signals/core` | `core_signals` only |
| `/api/v1/triz/signals/contradiction-index` | tension + density + cross-area + count |
| `/api/v1/triz/signals/innovation-clusters` | commercial radar + raw clusters |
| `/api/v1/triz/signals/narrative-penetration` | narrative intelligence slice |

Module: `hesperia.engine.triz.commercial_intelligence`.
