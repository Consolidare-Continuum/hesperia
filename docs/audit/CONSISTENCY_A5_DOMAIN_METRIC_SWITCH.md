# Consistency A5 — Domain metrics activation

**Block:** A — Functional integrity  
**Goal:** Verify that domain metrics appear only when enabled; projection still applied in both cases.

---

## Procedure

1. **Disabled**
   - Run `run_structural_analysis(text, enable_domain_metrics=False)` (or omit; default is False).
   - **Check:** Output does **not** contain a `domain_metrics` key, or it is null/empty.
   - **Check:** Rest of output is still projected (no internal-only keys such as `side_id`, `hex`, raw topology).

2. **Enabled**
   - Run `run_structural_analysis(text, enable_domain_metrics=True, domain_constants_path=<path>)` with a valid domain constants path if the execution_flow requires it (e.g. `assets/data/domain_constants.json`).
   - **Check:** Output **does** contain a `domain_metrics` key with non-empty, structured content (e.g. 41 signals, hash, or schema-defined shape).
   - **Check:** Rest of output remains projected; `domain_metrics` content itself must be public-safe (no internal topology/coordinates).

3. **Projection**
   - In both runs, confirm absence of forbidden terms in the emitted structure (see SEAL_B1).

---

## Expected summary

- **enable_domain_metrics=False:** `domain_metrics` absent or empty.
- **enable_domain_metrics=True:** `domain_metrics` present and populated.
- **Both:** Full output passes projection (no internal leakage).

---

## Failure interpretation

| Symptom | Likely cause |
|--------|---------------|
| domain_metrics present when disabled | Config not respected; execution_flow always computing domain metrics. |
| domain_metrics absent when enabled | Config not passed; or domain constants path missing/invalid. |
| Internal keys in output | Projection not applied to full summary or to domain_metrics. |

---

## Pass criterion

Domain metrics are absent when disabled and present when enabled; projection is applied in both cases. No remediation required.
