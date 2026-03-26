# HESPERIA Task 6 — Domain Fingerprint Engine

Produces a **deterministic fingerprint** from PrimitiveMetrics + DerivedMetrics: ordered numeric vector (41 values), metadata, and SHA-256 **vectorHash**. Core invariant: **same raw_text metrics → same fingerprint bytes**.

## Inputs

- **PrimitiveMetrics** — LD, COH, NC, PR, PV, CI
- **DerivedMetrics** — 35 derived metrics
- **domain_release**, **source_id** — optional metadata (trimmed, null → "")

## Output

**DomainFingerprint**: fingerprint_version, domain_release, source_id, metric_names (41), metric_values (41), primitive_map, derived_map, vector_hash.

## Version and order

- **FINGERPRINT_VERSION** = `hesperia_fp_v0_1` (bump if metric order, formula, rounding, or serialization changes)
- **FULL_ORDER** = 6 primitives (LD, COH, NC, PR, PV, CI) then 35 derived (KDI … KVI)

## Numeric policy

- **normalize_metric_value(x)** — NaN/Inf → 0, clamp to [0, 1]
- **round6(x)** — round to 6 decimals for hashing and serialization (reduces byte noise, stabilizes across runtimes)
- Hash and serialization use **round6(value)**, not raw doubles

## Canonical hash payload

`fingerprintVersion|domainRelease|sourceId|v1,v2,...,v41` with each v formatted as `%.6f` (round6). **vectorHash** = SHA-256 hex of UTF-8 payload.

## Usage

```python
from core.domain import build_fingerprint, same_fingerprint
from core.domain import fingerprint_euclidean, fingerprint_manhattan, fingerprint_cosine
from core.domain.models import PrimitiveMetrics
from core.domain.derived_metrics import compute_derived_metrics

p = PrimitiveMetrics(LD=0.42, COH=0.61, NC=0.12, PR=0.27, PV=0.09, CI=0.44)
d = compute_derived_metrics(p)
fp = build_fingerprint(p, d, domain_release="law_v0_3", source_id="doc_001")

# Compare
fp2 = build_fingerprint(p, d, "law_v0_3", "doc_001")
assert same_fingerprint(fp, fp2)
dist = fingerprint_euclidean(fp, fp2)  # 0.0
sim = fingerprint_cosine(fp, fp2)     # 1.0
```

## Comparison

- **same_fingerprint(a, b)** — equality by vector_hash (null-safe)
- **euclidean_distance(a_values, b_values)** — L2
- **manhattan_distance(a_values, b_values)** — L1
- **cosine_similarity(a_values, b_values)** — in [-1, 1]; nonnegative vectors yield [0, 1]

All use round6 for stability. Fingerprint helpers: **fingerprint_euclidean**, **fingerprint_manhattan**, **fingerprint_cosine** take two DomainFingerprint instances.

## Optional labeling

- **band(x)** — very_low / low / medium / high / very_high by round6(x) thresholds (0.2, 0.4, 0.6, 0.8)
- **label_metrics(names, values)** — name → band label (for dashboards)

## JSON

**to_dict()** returns stable field order: fingerprintVersion, domainRelease, sourceId, metricNames, metricValues, primitiveMap, derivedMap, vectorHash.

## Acceptance tests

- **A** — metricValues and metricNames length 41
- **B** — First name LD, last KVI
- **C** — Same inputs → same vectorHash
- **D** — Same inputs → same metricValues
- **E** — Distance to self: euclidean=0, manhattan=0, cosine=1
- **F** — One metric changed → different vectorHash
- **G** — round6(0.1234567)=0.123457, round6(0.1234564)=0.123456

## Summary

After Task 6, the execution_flow is: Domain Graph → Domain Constants → Active Graph → Primitive Metrics → Derived Metrics → **Fingerprint Vector** → Comparison / Profiling. Metric engine baseline is complete.
