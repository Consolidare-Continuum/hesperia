# Output anomaly taxonomy v1 (TFP multi-plane bundle)

**Purpose:** Machine-actionable **status** so JSON that is syntactically valid is not mistaken for **operationally valid**.

## Severity ladder

| Level | Meaning |
|-------|---------|
| `ok` | No anomalies in this plane for this session. |
| `degraded` | Usable with caveats; operator_message required. |
| `failed` | Hard failure for this plane; downstream consumers must not treat as authoritative. |

## Codes (registry: `assets/config/output_anomaly_codes_v1.json`)

| Code | Typical trigger |
|------|-----------------|
| `A001_NO_ATTRIBUTION` | L1 `ATTRIBUTED_TOKENS==0` and no `CALIBRATION_FALLBACK_USED` / calibration_status fallback. |
| `A002_UPSTREAM_NONZERO_DOWNSTREAM_ZERO` | Sealed `hex_activation_map.total_mass==0` while concept prior was non-degenerate. |
| `A003_THRESHOLD_OVERKILL` | Mass or signal lost to clipping/rounding only. |
| `A004_PROFILE_MISMATCH` | Profile hash / registry pin mismatch. |
| `A005_SCALE_CONTRACT_VIOLATION` | Out-of-range vs `output_metric_registry_v1`. |
| `A006_READABILITY_LAYER_MISSING` | Required readout missing under `internal_review` or `product_candidate` gate. |
| `A007_CROSS_PLANE_INCONSISTENCY` | Gold or harness detects rank/coverage drift across planes. |
| `G004_MISSING_BUNDLE_MANIFEST` | Release gate: `00_manifest.json` absent (non-research profiles fail; `research_allow_degraded` skips). |

## Envelope (required on every TFP bundle artifact root)

Each artifact JSON root MUST include `operational_envelope` (may be default-empty):

```json
{
  "operational_envelope": {
    "status": "ok | degraded | failed",
    "anomaly_codes": [],
    "severity": "ok | info | warn | error",
    "blocking": false,
    "operator_message": "",
    "recommended_next_check": "",
    "taxonomy_version": "1.0.0"
  }
}
```

**Rule:** Empty `anomaly_codes` + `status=ok` is explicit good health, not omission.

## Related

- Release gate: `docs/specs/calibration_release_gate_v1.md`
- Goldset: `docs/benchmarks/tfp_calibration_goldset_v1.md`
