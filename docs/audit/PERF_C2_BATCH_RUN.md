# Performance C2 — Batch scaling

**Block:** C — Performance sanity  
**Goal:** Run `run_structural_analysis_batch` with a moderate batch size (e.g. 100 texts). Check linear scaling, no memory leak, and that artifact writer is not the bottleneck.

---

## Procedure

1. **Batch size:** e.g. 100 texts. Use a fixed list of texts (same length/content profile if possible).

2. **Run:**  
   `run_structural_analysis_batch(texts, assets_root=assets)`  
   with `len(texts) == 100` (or chosen N).

3. **Scaling:** Optionally run with N = 10, 50, 100 and record total runtime.  
   **Check:** Runtime grows roughly linearly with N (no N² or worse). Approximate: `T(100) ≈ 10 × T(10)` (allowing for startup and variance).

4. **Memory:** Monitor memory during the batch run (e.g. tracemalloc or process RSS).  
   **Check:** No unbounded growth (memory leak). Peak memory should be reasonable (e.g. not 10× single-run memory for 100 items if each summary is bounded).

5. **Artifact writer:** If batch run also writes artifacts (e.g. one file per summary or one combined file), ensure write time is not dominant.  
   **Check:** Artifact writer is not the bottleneck (e.g. compute time >> write time, or writes are batched/efficient).

---

## Expected summary

- **Linear scaling:** Total time scales approximately linearly with batch size.
- **No memory leak:** Peak memory bounded; no continuous growth across batch.
- **Writer not bottleneck:** I/O does not dominate total runtime.

---

## Failure interpretation

| Symptom | Action |
|--------|--------|
| Super-linear scaling | Identify hot loop or redundant work; consider batching or caching where appropriate. |
| Memory growth with N | Fix references or caches that retain per-item state; stream or discard intermediates. |
| Writer bottleneck | Batch writes; or ensure write_public_json is not called in a tight loop with small payloads in a way that dominates. |

---

## Deliverable

Document in this audit (or in the consistency report):

- **Batch size:** e.g. 100.
- **Total runtime (s):** and optionally runtime for N=10, 50, 100.
- **Scaling:** Linear / sub-linear / super-linear.
- **Memory:** Peak during batch; any leak observed (yes/no).
- **Pass/fail:** Pass if scaling is linear and no leak; fail if otherwise.

---

## Pass criterion

Batch run scales roughly linearly; no memory leak; artifact writer not bottleneck. Performance remains within expected bounds.
