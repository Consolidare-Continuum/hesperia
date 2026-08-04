# Coverage Ledger

[← wiki home](index.md)

This wiki covers **163 items** verified on `/data/hesperia/hesperia` (131 live/beyond, 15 partial, 17 dead/rejected, 0 unverified). It is **not** a full census of every variable in the codebase — bounded to inspected research passes plus HWIKI expansion waves.

**Expansion waves:** all-encompassing `HWIKI-*` — [GRACE-TRIAGE-HESPERIA-WIKI-ALL-ENCOMPASSING-2026-07-19.md](../../../operational/assignments/GRACE-TRIAGE-HESPERIA-WIKI-ALL-ENCOMPASSING-2026-07-19.md). **Theory-depth 30** (`HWIKI-DOC-01..30`) — [GRACE-TRIAGE-HESPERIA-WIKI-DOC-THEORY-DEPTH-30-2026-07-19.md](../../../operational/assignments/GRACE-TRIAGE-HESPERIA-WIKI-DOC-THEORY-DEPTH-30-2026-07-19.md). **Structure / how-it-works (post 0.7.0)** (`HWIKI-STRUCT-*`) — [GRACE-TRIAGE-HESPERIA-WIKI-STRUCT-070-2026-07-26.md](../../../operational/assignments/GRACE-TRIAGE-HESPERIA-WIKI-STRUCT-070-2026-07-26.md). Gaps below are backlog, not permanent silence.

## Explicitly NOT yet covered (real gaps in this wiki, not silently omitted)

- **L1–L11 pipeline layer variables** (`34_SPEC`…`42_SPEC`, ~25 named variables per layer × 9 layers) — **L6 Lyapunov + curvature/gradient/depth-growth block wikified** (17 L6-related pages). Remaining L6 Group-IV stubs (HIT_VECTOR_RANK, ESCAPE_ENERGY, …) and **L1–L5 / L9–L11** full census still open. L7/L8 stability consumers of GLOBAL_STABILITY_SCORE landed (HWIKI-L7-01 / L8-01).
- **KME derived metrics** — **35 derived + hub wikified** (35 derived pages + [KME Primitives and Derived Metrics](pages/KME-Primitives-and-Derived-Metrics.md)). **HWIKI-KME-03:** plain-lang Theory Explainer notes on each derived page.
- **TRIZ extension internals** (`hesperia/extensions/triz/`, 30+ modules) — **contradiction core hub landed** (HWIKI-TRIZ-02); remaining novelty/topology/commercial modules still open beyond Louvain.
- **Full `parameter_catalog.md` sweep** — CAT-02 landed top diagnostic + FGR freshness pair; field-dynamics env knobs and remaining CAT-01 leftovers still open: [COLOMBO-HWIKI-CAT-01-PARAMETER-CATALOG-DELTA-2026-07-23.md](../../../operational/assignments/COLOMBO-HWIKI-CAT-01-PARAMETER-CATALOG-DELTA-2026-07-23.md).
- **Post-0.7.0 structure depth:** hubs under [structure/](structure/README.md) — SYSTEM-STRUCTURE, HOW-IT-WORKS, HAND-FACES, APPLY-ALLOWLIST, COBALT-REAL-DATA-GATES. Felix STRUCT-05 code-anchor PASS; Cursor STRUCT-06 ingest DONE.

## Theory-depth wave (HWIKI-DOC-02..29) — refreshed 2026-07-23 (DOC-30)

- **Explainer blocks landed** on OPEN DOC targets this pass: PageRank structural analogy, PHI/icosahedron, DFT REJECTED, Gini, BM25, Jaccard, cosine, Louvain, clustering (PARTIAL+`layer_2` pin), circuit rank, contradiction→tension, penalty suite hub, propagation YAML ladder, fusion α/E_cap/η, FGR + share/freshness, Concept Dictionary status/extent terms, Geometry/Core Math/Propagation hub preambles.
- **Remaining theory gaps (next batch candidates):** deeper TRIZ inventives beyond Louvain/contradiction map; L7/L8 consumers of GLOBAL_STABILITY_SCORE; KME derived plain-lang names beyond stubs; CAT-01 leftover symbols; turn-boundary Mixing (dead [[cumulativeDrift / turnCoherence]] revival decision).

## Structure / how-it-works wave (HWIKI-STRUCT) — opened 2026-07-26

- **Landed:** [System structure](structure/SYSTEM-STRUCTURE-0.7.0.md) · [How it works](structure/HOW-IT-WORKS-0.7.0.md) · [HAND faces](structure/HAND-FACES-0.7.0.md) · [Apply allowlist](structure/APPLY-ALLOWLIST-0.7.0.md) · [COBALT/REAL_DATA gates](structure/COBALT-REAL-DATA-GATES-0.7.0.md).
- **Verify:** [FELIX-HWIKI-STRUCT-05](../../../operational/assignments/FELIX-HWIKI-STRUCT-05-CODE-ANCHOR-VERIFY-2026-07-26.md) PASS · ingest includes `structure/*.md`.

## Resolved questions (were open; evidence now on the page)

- **[compute_tension](pages/compute-tension.md)** (HWIKI-OPEN-01): `(i,i+6)` is **not** geometrically antipodal after `get_aligned_area_coordinates` — combinatorial [[OPPOSITE_OFFSET]], not sphere antipodes.
- **[Wiener feedback on alpha (k_s / k_j)](pages/Wiener-feedback-on-alpha-k-s-k-j.md)** (HWIKI-OPEN-02): relocated LIVE_SUCCESSOR → `sphere/propagation/weighting.py` as `k_stability`/`k_jump` (diffusion α, not fusion α).
- **[Mixing Diagnostics](pages/Mixing-Diagnostics.md)** (HWIKI-OPEN-03): line-by-line confirmed as `propagation_depth_metric` (`consecutive_l1` + `entropy_sequence` via canonical `compute_normalized_entropy`).

## Open / unresolved questions carried into this wiki (do not treat as settled)

- *(none from the original three Coverage-Ledger open Qs — all resolved 2026-07-23.)*

## Cheap, concrete next-wave candidates

- Add `compute_dominant_family_share` as a real page once/if built (mirrors [dominant_area_share_threshold](pages/dominant-area-share-threshold.md)) — see [X_A / X_F alignment (Java)](pages/X-A-X-F-alignment-Java.md).
- Finish remaining L6 variables (curvature/gradient/depth-growth block) then L7/L8 consumers of GLOBAL_STABILITY_SCORE.
- Wikify CAT-01 delta list (diagnostic ultra_sparse / field-dynamics / FGR numeric table leftovers).
