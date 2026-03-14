# SHIPPING SURFACE POLICY v1

**Status:** Active  
**Purpose:** Define exactly what the shipped runtime may do. Two deliverables: Linux CLI binary (Nuitka) and Linux API container (Docker multi-stage). Both built from the same sealed runtime core.

---

## 1. Public commands only

The shipped runtime exposes **exactly four** public commands. No other entry points may be advertised or default in the shipped product.

| Command | Purpose | Allowed behavior |
|---------|---------|------------------|
| **analyze** | Single-text structural analysis | Ingest one text; run structural analysis via service façade; return projected output only (macro-domain vector, policy family counts, evidence summary, trust/confidence). No layer views, no raw traces. |
| **compare** | Two-text comparison | Ingest two texts; run structural analysis on each via service; return projected comparison (divergence, similarity, difference profile). No internal coordinates or layer dumps. |
| **batch-analyze** | Batch structural analysis | Ingest a list of texts; run structural analysis per item via service; return list of projected outputs. No intermediate layer state. |
| **serve** | API server | Expose HTTP (or defined protocol) API that accepts text(s), calibration profile id, and report profile; returns projected analysis or comparison results only. No debug endpoints, no layer views, no raw traces. |

---

## 2. What the shipped runtime may do

- **Accept input:** Text (or corpus slice), calibration profile id, report profile id, domain/use-case preset.
- **Call sealed core:** Only via `core.services` (e.g. `run_structural_analysis`, `run_structural_analysis_batch`). No direct orchestration of internal layers.
- **Emit output:** Only projected, public-safe artifacts (per PUBLIC_OUTPUT_POLICY, public_output_schema). Evidence as matched span and concept label; no side_id, no topology, no internal coordinates.
- **Write artifacts:** Only via central artifact writer; public writes only; projection applied before any write.
- **Log:** Product-shaped messages only; no internal layer names, formula ids, or topology in log text.

---

## 3. What the shipped runtime must never do

- **Debug:** No debug mode, no layer dumps, no raw traces, no internal state export.
- **Layer views:** No endpoint or command that returns L1–L9 (or equivalent) as inspectable internal structures; only projected, high-level metrics and evidence.
- **Raw traces:** No propagation path, no bridge nodes, no adjacency, no internal graph exposure.
- **Internal entry points:** No access to run_l1_l2, run_l1_l2_l3, run_sphere_math_values, run_e2e_all, or any internal-review/internal-debug entry point from the shipped surface. Those exist for development only and are not part of the shipping boundary.
- **Bypass projection:** Every response and written artifact must pass through the public projection layer.

---

## 4. Mapping to current implementation

| Shipped command | Implementation mapping |
|-----------------|-------------------------|
| **analyze** | `core.services.analysis_service.run_structural_analysis(text, ...)`; CLI wrapper invokes this and prints/writes projected JSON only. |
| **compare** | Two calls to `run_structural_analysis`; diff/similarity over projected outputs; no internal state. |
| **batch-analyze** | `core.services.analysis_service.run_structural_analysis_batch(texts, ...)`; output list of projected results. |
| **serve** | API server that accepts requests and calls analysis_service (and optionally report_service); returns only projected responses. |

Existing runners (run_l1_through_l9, run_reference_pipeline, run_l1_l2, run_l1_l2_l3, run_sphere_math_values, run_sphere_math_100_sentences) may remain in the source tree for development and testing but **must not** be the primary advertised commands in the shipped CLI. The shipped CLI binary exposes **analyze**, **compare**, **batch-analyze**, and **serve** (or equivalent names) as the only user-facing commands.

---

## 5. Build context

- **Linux CLI binary:** Built with Nuitka from the sealed runtime core; standalone mode tested before onefile. No plain Python wheels as the main protection; Nuitka aligns with code protection.
- **Linux API container:** Docker multi-stage build; minimal final image; only runtime, core/services, core/projection, assets/public, and the four-command surface. No internal docs, no debug tooling, no topology helpers in the image.

---

## 6. Done condition

The shipped runtime may do only what is defined above (four public commands, projected output only, no debug/layer/raw traces). Any other behavior is out of scope for the shipping boundary.
