# HESPERIA Task 4 — Derived Metric Engine

Computes **35 derived metrics** from **6 primitives** (LD, COH, NC, PR, PV, CI). Strict bounded regime: every output is `clamp01()`, every division uses `safeDiv()`. Pure algebra over primitives only; no graph access.

## Raw_text

**PrimitiveMetrics** — LD, COH, NC, PR, PV, CI (all in [0, 1]).

## Output

**DerivedMetrics** — 35 fields in canonical order: KDI, CSI, SPI, TDS, SSS, KCI, CCI, SPS, DCI, CSI2, KEF, ASS, CDR, KCR, TCI, PEI, KE, SCS, CRI, KNS, CII, TEP, KSI, CDD, SSR, TER, CPC, KBS, TRI, IDE, KPS, TBI, KDI2, CDI, KVI.

**Marketable subset (14):** For dashboards and external users, use the 14 market-facing metrics (interpretability, non-redundancy, business meaning). List: `core/domain/fingerprint.py` → `MARKETABLE_DERIVED_ORDER`. Helper: `marketable_derived_from_map(derived_map)`. Full definitions and criteria: `docs/DOMAIN_MARKETABLE_METRICS.md`, `docs/DOMAIN_METRICS_REFERENCE.md` §4.

## Utilities

- **clamp01(x)** — clamp to [0, 1]; NaN/Inf → 0.0.
- **safeDiv(num, den)** — division; invalid or den ≤ 0 → 0.0.

## Usage

```python
from core.domain import compute_derived_metrics, to_derived_vector, to_full_fingerprint
from core.domain.models import PrimitiveMetrics

p = PrimitiveMetrics(LD=0.5, COH=0.6, NC=0.4, PR=0.3, PV=0.5, CI=0.2)
d = compute_derived_metrics(p)

# 35-dim vector (canonical order)
vec = to_derived_vector(d)

# 41-signal fingerprint (6 primitives + 35 derived)
fp = to_full_fingerprint(p, d)
```

## Null and zero

- **Null raw_text** → `zero_derived_metrics()` (all 35 = 0.0).
- **All-zero primitives** → all derived = 0.0.

## Acceptance tests

- **A** — Null raw_text → all derived 0.0.
- **B** — All-zero primitives → all derived 0.0.
- **C** — All-one primitives → all derived 1.0 (multiplicative and division-based).
- **D** — Zero denominators (e.g. NC=0, PV=0) → SSS, ASS, KEF, CDD, SSR, CPC, KBS, KVI = 0; no NaN/Inf.
- **E** — Monotonicity: LD↑ ⇒ KDI, DCI, CSI2, TCI, TEP not decreasing; COH↑ ⇒ KDI, CCI, SPS, CRI, KPS not decreasing; PV↑ ⇒ SSS, ASS, PEI, CDD, SSR not increasing.

## Summary

After Task 4, HESPERIA has the full **derived market layer**: 35 derived metrics from 6 primitives, deterministically. Mathematical core is assembled.
