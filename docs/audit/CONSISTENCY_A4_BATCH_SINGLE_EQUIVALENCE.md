# Consistency A4 — Batch vs single run equivalence

**Block:** A — Functional integrity  
**Goal:** For a single-item batch, batch and single-run results must be identical.

---

## Procedure

1. **Fixed input:** e.g. `text = "justice lie fairness truth good order harm freedom"`.

2. **Single run:**  
   `single_out = run_structural_analysis(text, assets_root=assets, stages="full")`

3. **Batch run (single element):**  
   `batch_out_list = run_structural_analysis_batch([text], assets_root=assets)`  
   `batch_out = batch_out_list[0]`

4. **Compare:**  
   - `single_out` and `batch_out` must be **identical** (deep equality, or with allowed float tolerance).
   - Keys, structure, and values (including metric vectors, evidence, usf if present) must match.

---

## Expected result

- **Identical outputs:** `single_out == batch_out` (or equivalent under chosen tolerance).

---

## Failure interpretation

| Symptom | Likely cause |
|--------|---------------|
| Structures differ | Batch path uses different pipeline config or projection. |
| Values differ | document_id or per-item state leaking (e.g. index-dependent behavior). |
| Keys missing in one | Different code paths building the result. |

---

## How to run (example)

```python
from pathlib import Path
from core.services.analysis_service import run_structural_analysis, run_structural_analysis_batch

ROOT = Path(__file__).resolve().parents[2]
assets = ROOT / "lexicon" / "curated"
text = "justice lie fairness truth good order harm freedom"

single_out = run_structural_analysis(text, assets_root=assets, stages="full")
batch_out = run_structural_analysis_batch([text], assets_root=assets)[0]

assert single_out == batch_out, "A4: single vs batch[0] differ"
```

---

## Pass criterion

`run_structural_analysis_batch([text])[0]` equals `run_structural_analysis(text)` for the same options. No remediation required.
