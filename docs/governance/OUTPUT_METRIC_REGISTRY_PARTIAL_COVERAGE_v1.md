# Output metric registry — partial coverage (v1 waiver)

**Status:** Accepted for `registry_version` **1.0.0**  
**Authority:** Ethan / product governance (G-REG-01 closure)

## Fact

`assets/config/output_metric_registry_v1.json` does **not** enumerate every numeric or scalar key that may appear in **projected public JSON** or internal diagnostics. It **does** define semantics for selected artifact paths used in TFP / structural batch / sealed hex / product analyze / KME primitives (see `artifacts` keys in the JSON).

## Policy

- **Consumers** (UI, downstream analytics, compliance checks) **must not** treat absence from the registry as “invalid output.” Unknown keys may appear under projection evolution or profile-specific paths until a future registry bump.
- **New product-critical metrics** should be added to the registry when they become stable contract surfaces (Olivia / Gena workflow).
- **v1.1+** may widen coverage or split wildcard entries (e.g. `kme.report.primitives` → per-primitive rows).

## Relation to CI

Sealed runtime and schema guards enforce **shape / projection** rules; the metric registry is **semantic documentation**, not a full JSON Schema for every leaf key.

---

*See also: `docs/PUBLIC_PRODUCT_SURFACE.md`, `assets/config/output_metric_registry_v1.json`.*

SIGNED: Cursor | GAP-WIRE-06 waiver artifact | 2026-03-28 | Hesperia governance
