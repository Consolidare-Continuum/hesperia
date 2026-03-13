# HESPERIA Knowledge Metrics Engine (KME) — Formal Deliverable Summary

**Status:** COMPLETE. Integrated into main E2E pipeline.

**Short identifier:** KME  
**Module path:** `hesperia.engine.kme`

---

## Objective

Design and integrate a deterministic structural knowledge metric system that computes a 41-signal fingerprint describing the structural properties of knowledge expressed in text. The engine produces reproducible metrics suitable for:

- document analysis  
- domain comparison  
- knowledge diagnostics  
- LLM grounding  
- scientific corpus profiling  

---

## System Scope

The component computes:

- 6 primitive structural metrics  
- 35 derived structural metrics  
- 41-value fingerprint vector  
- deterministic fingerprint hash  

All metrics operate on the **Active Concept Graph** produced by the HESPERIA semantic pipeline.

---

## Repository Structure (KME)

```
hesperia/
  engine/
    kme/                    ← Knowledge Metrics Engine
      primitives/           # LD, COH, NC, PR, PV, CI
      derived/              # 35 derived metrics
      fingerprint/          # 41-value vector, hash, comparison
      profiling/            # Domain profile (corpus-level)
      validation/           # Validation namespace
      models.py             # DTOs
      extractor.py          # Domain constants
      loader.py             # Load domain graph / frozen constants
      active_graph.py       # Active graph canonicalizer
      bridge.py             # Sphere pipeline → KME bridge
      pipeline.py           # run_document, run_corpus, export
```

**Legacy:** `core.domain` re-exports from `hesperia.engine.kme`. Prefer `from hesperia.engine.kme import ...` for new code.

---

## Metrics Implemented

**Primitive (6):** LD, COH, NC, PR, PV, CI.  
**Derived (35):** KDI, CSI, SPI, TDS, SSS, KCI, CCI, SPS, DCI, CSI2, KEF, ASS, CDR, KCR, TCI, PEI, KE, SCS, CRI, KNS, CII, TEP, KSI, CDD, SSR, TER, CPC, KBS, TRI, IDE, KPS, TBI, KDI2, CDI, KVI.

**Fingerprint:** 41-value vector, fixed ordering, stable rounding, SHA-256 hash.  
**Domain Profile:** mean, std, median, p90 per dimension; profile hash; `domain_distance`, `classify_document`.

---

## Integration Into HESPERIA E2E

Pipeline placement:

1. semantic extraction  
2. relation detection  
3. active graph construction  
4. propagation layer  
5. **KME (metrics engine)**  
6. fingerprint output  

Execution output per document: ActiveGraph, PrimitiveMetrics, DerivedMetrics, DomainFingerprint, JSON report.

---

## Output Format

**MetricReport:** sourceId, primitive metrics, derived metrics, fingerprint vector, fingerprint hash.  
Determinism: same concept hits, relations, domain graph, constants → identical primitive metrics, derived metrics, fingerprint vector, hash.

---

## Performance

Typical runtime cost per document: primitive metrics ~1–2 ms, derived &lt;1 ms, fingerprint &lt;1 ms. Total added pipeline cost ~3 ms per document.

---

## Deliverables Produced

- Primitive metric formulas  
- Derived metric formulas (35)  
- Metric computation engine  
- Validation test suite  
- Domain fingerprint system  
- Domain profiling layer  
- E2E pipeline integration  
- Metric documentation  

All definitions are deterministic, machine-readable, and Codex-ready.

---

## Final Result

The HESPERIA system contains a fully specified module **HESPERIA Knowledge Metrics Engine (KME)** with capabilities for structural knowledge measurement, document fingerprinting, domain profiling, discipline comparison, and knowledge structure diagnostics, wired directly into the main E2E pipeline.

**Reference docs:** `docs/DOMAIN_METRICS_REFERENCE.md`, `docs/DOMAIN_PROFILE.md`, `docs/DOMAIN_E2E_PIPELINE.md`, `AGENTS.md` (§ Knowledge Metrics Engine).
