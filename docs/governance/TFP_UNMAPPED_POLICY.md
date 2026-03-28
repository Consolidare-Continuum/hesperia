# TFP unmapped / unknown handling (TFP-GATE-UNMAPPED)

**Policy:** Unknown lexical items must not silently become high-confidence TFP edges.

- **Routing:** Documented in `HESPERIA_TFP_MODULE_DICTS.md` and calibration governance (`DICT-CAL-*`); loader and executor honor `UNKNOWN` / fallback paths per module contract.
- **Audit:** Use `tools/tfp_calibration_audit.py` (DICT-CAL-13) for bundle-level checks; extend with explicit unmapped counters in audit output when implemented.

---

`SIGNED: Cursor (workflow) | TFP-GATE-UNMAPPED | 2026-03-28`
