# HESPERIA E2E Integration — Pipeline and Export

**Goal:** Run the full metric pipeline from document inputs (concept hits + relation candidates) and export all 41 metrics, fingerprint vector, hash, and JSON report.

**Pipeline:**  
Text corpus (hits + relations) → Active Graph → Primitive Metrics (6) → Derived Metrics (35) → Fingerprint (41 + hash) → Export (JSON).

---

## 1. Pipeline entry point

**Runner:** `HesperiaPipelineRunner(domain_graph, domain_constants)`  
- **run_pipeline(source_id, hits, relations, domain_release="")** → `DomainFingerprint`  
- **run_document(source_id, hits, relations, domain_release="")** → `MetricReport`

**One-shot functions (no runner instance):**  
- **run_pipeline(domain_graph, domain_constants, source_id, hits, relations, domain_release="")** → `DomainFingerprint`  
- **run_document(domain_graph, domain_constants, source_id, hits, relations, domain_release="")** → `MetricReport`  
- **run_corpus(documents, domain_graph, domain_constants, domain_release="")** → `list[MetricReport]`

---

## 2. Inputs and outputs

**Document input:** `DocumentInput(source_id, hits, relations)`  
- `hits`: `list[ConceptHit]` (concept_id, token_index)  
- `relations`: `list[RelationCandidate]` (concept_a, concept_b, relation_type)

**Metric report:** `MetricReport(source_id, primitive_map, derived_map, fingerprint)`  
- **primitive_map:** 6 entries (LD, COH, NC, PR, PV, CI), round6  
- **derived_map:** 35 entries, round6  
- **fingerprint:** `DomainFingerprint` (41 values, vectorHash, metadata)

---

## 3. JSON export

- **metric_report_to_dict(report)** → dict suitable for `json.dumps` (sourceId, primitives, derived, fingerprint).  
- **export_metric_report_json(path, report)** → writes deterministic JSON (sort_keys, stable format) to file.

**Example shape:**

```json
{
  "sourceId": "paper_001",
  "primitives": { "LD": 0.421, "COH": 0.613, "NC": 0.102, "PR": 0.287, "PV": 0.092, "CI": 0.481 },
  "derived": { "KDI": 0.258, "CSI": 0.029, "...": "...", "KVI": 0.821 },
  "fingerprint": {
    "fingerprintVersion": "hesperia_fp_v0_1",
    "domainRelease": "",
    "sourceId": "paper_001",
    "metricNames": ["LD", "COH", ...],
    "metricValues": [0.421, 0.613, ...],
    "primitiveMap": { ... },
    "derivedMap": { ... },
    "vectorHash": "2e43f3c2..."
  }
}
```

---

## 4. Batch mode

**run_corpus(documents, domain_graph, domain_constants, domain_release="")**  
- `documents`: `list[DocumentInput]`  
- Returns `list[MetricReport]`, one per document.

---

## 5. Performance target

Per document (on a modern CPU):  
- Graph build &lt; 10 ms  
- Primitive metrics &lt; 2 ms  
- Derived metrics &lt; 1 ms  
- Fingerprint &lt; 1 ms  
- **Total &lt; 15 ms per document**

---

## 6. Usage example

```python
from core.domain import (
    run_document,
    run_corpus,
    export_metric_report_json,
    load_domain_graph_from_json,
    load_frozen_constants,
)
from core.domain.models import DocumentInput, ConceptHit, RelationCandidate

domain = load_domain_graph_from_json("assets/data/domain_graph.json")
constants = load_frozen_constants("assets/data/domain_constants.json")

hits = [ConceptHit("contract_law", 0), ConceptHit("law", 1), ...]
relations = [RelationCandidate("contract_law", "law", "is_subdomain"), ...]

report = run_document(domain, constants, "paper_001", hits, relations, domain_release="law_v0_3")
export_metric_report_json("reports/paper_001.json", report)

# Batch
docs = [DocumentInput("doc_1", hits1, rels1), DocumentInput("doc_2", hits2, rels2)]
reports = run_corpus(docs, domain, constants)
for r in reports:
    export_metric_report_json(f"reports/{r.source_id}.json", r)
```

---

## 7. Completion criteria

- Pipeline runs from concept hits + relations → metrics and fingerprint  
- All 41 metrics computed (6 primitives + 35 derived)  
- Fingerprint vector and deterministic hash generated  
- JSON export stable (deterministic)  
- Batch mode supported  
- E2E test passes: `tests/domain/test_e2e_pipeline.py`

**Delivered system:** 6 primitive metrics, 35 derived metrics, 41-signal fingerprint, deterministic hash, JSON export — complete knowledge metric engine.

---

## 8. Main E2E run integration

Metrics run as a **stage of the normal E2E run**, not a separate tool.

**Sphere pipeline:** When `config["enable_domain_metrics"]` is true, after guards the pipeline runs the domain metrics stage: bridge pipeline state (matched token→family list) to ConceptHits and a synthetic domain graph (288 family nodes), then runs primitives → derived → fingerprint and sets **result["domain_metrics"]** with the same shape as a MetricReport (sourceId, primitives, derived, fingerprint). No separate runner process.

**Bridge** (`core/domain/bridge.py`): `synthetic_domain_graph_for_topology(F)` builds a minimal domain graph (nodes f_0..f_{F-1}, no edges). `pipeline_matched_to_hits_relations(matched, F)` converts the pipeline’s `matched` list to `list[ConceptHit]` and empty `list[RelationCandidate]`.

**Config:** Set `enable_domain_metrics=True`. Optionally set `domain_constants_path` (e.g. `assets/data/domain_constants.json`); if missing, defaults to constants for F nodes. Optionally set `domain_release`.

**run_e2e_all:** The unified E2E runner now includes **run_e2e_domain_metrics**: it runs the main pipeline with `enable_domain_metrics=True` and writes **run_output_e2e_domain_metrics.json** with the full domain_metrics payload. So every `python3 -m runtime.pipeline.run_e2e_all` produces 6 artifacts including the metric report.

**Determinism:** Same input (same text, document_id, config) → same domain_metrics (same primitives, derived, fingerprint, vectorHash).

---

## 9. Domain Profile (corpus-level)

After you have many document fingerprints (e.g. from `run_corpus` or from stored reports), use the **Domain Profile** layer to aggregate them into one corpus-level profile per domain:

- **build_profile(domain_id, fingerprints)** → `DomainProfile` (mean, std, median, p90 vectors, profileHash).
- **domain_distance(profile_a, profile_b)** → Euclidean distance between two profiles.
- **classify_document(fingerprint, profiles)** → domainId of the profile whose mean is closest to the document.

See `docs/DOMAIN_PROFILE.md` for full specification.
