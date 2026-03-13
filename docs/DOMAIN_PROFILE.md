# HESPERIA Domain Profile Layer

**Purpose:** Summarize the structural knowledge characteristics of an entire corpus by aggregating the fingerprints of many documents.

Instead of analyzing **1 document → 41 metrics**, you analyze **N documents → 1 stable domain profile** (mean, std, median, p90 per dimension, profile hash).

---

## 1. Domain Profile Object

| Field | Meaning |
|-------|--------|
| **domainId** | Identifier for the domain/corpus (e.g. `"physics"`, `"law"`) |
| **documentCount** | Number of fingerprints aggregated |
| **meanVector** | Average structural behavior of the domain (length 41) |
| **stdVector** | Variability across texts (sample standard deviation per dimension) |
| **medianVector** | Robust center per dimension |
| **p90Vector** | 90th percentile per dimension (high-end structural capability) |
| **profileHash** | SHA-256 of canonical mean-vector string (deterministic) |

Vector length is **41** (same as document fingerprint).

**Implementation:** `core/domain/models.py` (`DomainProfile`), `core/domain/profile.py` (`build_profile`).

---

## 2. Profile Computation

**Input:** List of `DomainFingerprint` (e.g. one per document in a corpus).

**Computation (per dimension i = 0..40):**

- **mean[i]** = average of `fp.metricValues[i]` across all fingerprints  
- **std[i]** = sample standard deviation of those values (0 if n ≤ 1)  
- **median[i]** = median of those values  
- **p90[i]** = 90th percentile (deterministic: sorted values, index = ceil(0.90×n)−1 clamped)

**profileHash** = SHA-256 of the canonical mean-vector string (6-decimal format, comma-separated).

**Edge case:** Zero fingerprints → profile with `documentCount=0`, all vectors 41 zeros, hash of that zero vector.

---

## 3. What the Domain Profile Represents

A **structural signature of a discipline**. Example patterns:

| Domain | LD | COH | PR | CI |
|--------|----|-----|----|----|
| Physics | high | high | medium | medium |
| Law | medium | high | low | high |
| Philosophy | medium | medium | high | medium |

Profiles become stable around **~200 documents** for typical corpora.

---

## 4. Domain Comparison

**domain_distance(profile_a, profile_b)** = Euclidean distance between the two **mean vectors**.

- `distance(physics, math)` → small  
- `distance(physics, law)` → larger  
- `distance(physics, poetry)` → very large  

**Implementation:** `core/domain/profile.py` → `domain_distance(profile_a, profile_b)`.

---

## 5. Domain Classification

Given a new document fingerprint and a list of domain profiles:

- Compute distance from the document’s metric vector to each profile’s **meanVector**.
- **classify_document(fingerprint, profiles)** returns the **domainId** of the profile with minimum distance.

No ML required; deterministic structural classification.

**Implementation:** `core/domain/profile.py` → `classify_document(fingerprint, profiles)`.

---

## 6. Stability and Drift

- **Stability:** Low `std` for a metric (e.g. `std(KDI)` small in physics) → highly standardized writing in that dimension.
- **Drift detection:** Compare `profile_2020` vs `profile_2030` for the same domainId; `domain_distance(profile_2020, profile_2030)` detects structural evolution.

---

## 7. Where It Fits in E2E

Full architecture:

```
document
   ↓
concept extraction
   ↓
active graph
   ↓
primitive metrics
   ↓
derived metrics
   ↓
document fingerprint
   ↓
domain profiler        ← Domain Profile Layer
   ↓
domain profile (corpus-level)
```

Document-level pipeline remains in `core/domain/pipeline.py` and `sphere/pipeline/pipeline_runner.py`. The Domain Profile layer consumes **existing** fingerprints (e.g. from `run_corpus` or stored reports) and produces one profile per corpus.

---

## 8. API Summary

| Function | Description |
|----------|-------------|
| **build_profile(domain_id, fingerprints)** | Build `DomainProfile` from list of `DomainFingerprint`. |
| **domain_distance(profile_a, profile_b)** | Euclidean distance between two profiles (mean vectors). |
| **classify_document(fingerprint, profiles)** | Return `domainId` of nearest profile; `None` if `profiles` empty. |

**Exports:** `core/domain/__init__.py` (DomainProfile, build_profile, domain_distance, classify_document).

---

## 9. Example Output Shape

```json
{
  "domainId": "physics",
  "documentCount": 1280,
  "meanVector": [0.48, 0.71, 0.13, ...],
  "stdVector": [0.05, 0.03, ...],
  "medianVector": [...],
  "p90Vector": [...],
  "profileHash": "a92f83..."
}
```

---

## 10. What This Enables

- **Corpus characterization:** “What is the structural nature of economics papers?”  
- **Domain similarity maps:** physics ↔ mathematics, law ↔ political science  
- **Theory evaluation:** Does a new theory structurally resemble established work?  
- **Knowledge drift detection:** How physics papers changed across decades  

See also: `docs/DOMAIN_METRICS_REFERENCE.md`, `docs/DOMAIN_E2E_PIPELINE.md`.
