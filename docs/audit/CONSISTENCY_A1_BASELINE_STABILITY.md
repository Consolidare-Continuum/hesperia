# Consistency A1 — Baseline output stability

**Block:** A — Functional integrity  
**Goal:** Ensure identical raw_text produces identical projected outputs across repeated runs (no hidden nondeterminism, writer path inconsistency, or projection mutation).

---

## Procedure

1. **Setup:** From repo root, ensure `PYTHONPATH` or `sys.path` includes the repo (e.g. `export PYTHONPATH=/path/to/hesperia` or run via `python3 -m` from repo root).

2. **Fixed raw_text:** Choose a single canonical raw_text, e.g.  
   `text = "justice lie fairness truth good order harm freedom"`

3. **Triple invocation:** Call  
   `analysis_service.run_structural_analysis(text)`  
   three times with the same arguments (same `assets_root`, no profile, `stages="full"`).

4. **Capture outputs:** Store the three returned dicts as `out1`, `out2`, `out3`.

5. **Checks:**
   - **Identical projected outputs:** `out1 == out2` and `out2 == out3` (deep equality of full dict).
   - **Identical checksum values:** If the outputs contain or you compute a checksum/hash (e.g. over JSON-serialized payload), all three must match.
   - **Stable evidence count:** If an evidence count or equivalent is present (e.g. in `usf`, `interpretation_metrics`, or a derived field), it must be the same in all three runs.
   - **Stable metric vectors:** Any list/vector fields (e.g. `macro_domain_vector`, `policy_family_counts`, or nested vectors in `usf`) must be identical across the three runs.

---

## Expected summary

- **output_checksum:** stable (same value for all three runs).
- **evidence_count:** stable.
- **metric vectors:** identical (no floating-point or ordering variance that would indicate nondeterminism).

---

## Failure interpretation

| Symptom | Likely cause |
|--------|---------------|
| Output dicts differ | Hidden nondeterminism (e.g. dict iteration order, random seed, time-based value). |
| Checksums differ | Writer path inconsistency or projection mutating output. |
| Evidence count or vectors differ | Non-deterministic execution_flow step or unstable projection. |

---

## How to run (example)

```python
from pathlib import Path
from core.services.analysis_service import run_structural_analysis

ROOT = Path(__file__).resolve().parents[2]  # repo root
assets = ROOT / "lexicon" / "curated"
text = "justice lie fairness truth good order harm freedom"

out1 = run_structural_analysis(text, assets_root=assets, stages="full")
out2 = run_structural_analysis(text, assets_root=assets, stages="full")
out3 = run_structural_analysis(text, assets_root=assets, stages="full")

assert out1 == out2, "A1: run1 vs run2 differ"
assert out2 == out3, "A1: run2 vs run3 differ"
# Optional: compute and compare checksums over json.dumps(out1, sort_keys=True)
```

---

## Pass criterion

All three outputs are identical (deep equality). No remediation required.
