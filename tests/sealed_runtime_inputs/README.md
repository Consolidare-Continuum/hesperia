# Sealed runtime regression test set

Fixed corpus of 10–20 representative texts for release verification.

**Usage:**
- During release: run analyze on each, compare pairs, batch-analyze all.
- Verify: deterministic output, schema validity (no forbidden keys), no reflective terms in output.

See `tests/test_sealed_runtime_regression.py` and docs/governance/MAINTENANCE_GUIDELINE_v1.md.
