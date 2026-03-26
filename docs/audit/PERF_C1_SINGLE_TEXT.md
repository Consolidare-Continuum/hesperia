# Performance C1 — Single text latency

**Block:** C — Performance sanity  
**Goal:** Measure runtime and memory for a single `run_structural_analysis(text)` call. Compare with pre-seal baseline if available; ensure sealing did not introduce unacceptable overhead.

---

## Procedure

1. **Environment:** Use a representative environment (same Python version, no debug flags). Optional: set `HESPERIA_RUNTIME_MODE=public_runtime` to match production.

2. **Raw_text:** Fixed text, e.g.  
   `text = "justice lie fairness truth good order harm freedom"`  
   (or a longer paragraph if that is the typical unit).

3. **Runtime measurement:**
   - Call `run_structural_analysis(text, assets_root=assets, stages="full")` and measure wall-clock time (e.g. `time.perf_counter()` before/after). Optionally run multiple times (e.g. 5) and report mean/std or median.
   - Record **runtime** in seconds.

4. **Memory (optional):**
   - Use a memory profiler (e.g. `memory_profiler`, `tracemalloc`) to measure peak memory during the call, or run under a tool that reports RSS.
   - Record **peak memory** (MB or GB).

5. **Baseline comparison:** If a pre-seal baseline was recorded (same raw_text, same machine/profile), compare:
   - Runtime: within expected bounds (e.g. within 2× or within a stated SLA).
   - Memory: no large unexplained increase.

---

## Expected summary

- **Runtime:** Recorded and (if baseline exists) within acceptable range. No order-of-magnitude regression.
- **Memory:** Recorded; no obvious leak (single run). If baseline exists, within expected range.

---

## Failure interpretation

| Symptom | Action |
|--------|--------|
| Large runtime increase vs baseline | Profile hot paths; check for redundant projection or duplicate execution_flow runs. |
| High or growing memory | Check for unbounded caches, large intermediate structures, or references holding state. |

---

## Deliverable

Document in this audit (or in the consistency report):

- **Runtime (s):** e.g. mean ± std over N runs.
- **Memory:** e.g. peak RSS or profiler summary.
- **Baseline (if any):** pre-seal values and comparison.
- **Pass/fail:** Pass if within expected bounds; fail if regression exceeds policy threshold.

---

## Pass criterion

Single-text latency and memory are recorded and within expected bounds (or no baseline to compare). Performance remains acceptable for production use.
