# Coverage Ledger

[← wiki home](index.md)

This wiki covers **137 items** verified on `/data/hesperia/hesperia` (113 live/beyond, 7 partial, 17 dead/rejected, 0 unverified). It is **not** a full census of every variable in the codebase — bounded to inspected research passes plus HWIKI expansion waves.

**Expansion waves:** all-encompassing `HWIKI-*` — [GRACE-TRIAGE-HESPERIA-WIKI-ALL-ENCOMPASSING-2026-07-19.md](../../../operational/assignments/GRACE-TRIAGE-HESPERIA-WIKI-ALL-ENCOMPASSING-2026-07-19.md). **Theory-depth 30** (`HWIKI-DOC-01..30`) — [GRACE-TRIAGE-HESPERIA-WIKI-DOC-THEORY-DEPTH-30-2026-07-19.md](../../../operational/assignments/GRACE-TRIAGE-HESPERIA-WIKI-DOC-THEORY-DEPTH-30-2026-07-19.md). Gaps below are backlog, not permanent silence.

## Explicitly NOT yet covered (real gaps in this wiki, not silently omitted)

- **L1–L11 pipeline layer variables** (`34_SPEC`…`42_SPEC`, ~25 named variables per layer × 9 layers) — **L6 first slice started** (7 pages: Lyapunov cluster + neighbors). Remaining L6 variables (gradients/curvature/depth-growth/…) and other layers still open.
- **KME derived metrics** — **35 stubs + hub now wikified** (35 derived pages + [KME Primitives and Derived Metrics](pages/KME-Primitives-and-Derived-Metrics.md)). Theory/plain-lang expansion still open.
- **TRIZ extension internals** (`hesperia/extensions/triz/`, 30+ modules) beyond Louvain and the contradiction-pressure mapping already pulled in.
- **Full `parameter_catalog.md` sweep** — delta list of still-unwikified catalog symbols: [COLOMBO-HWIKI-CAT-01-PARAMETER-CATALOG-DELTA-2026-07-23.md](../../../operational/assignments/COLOMBO-HWIKI-CAT-01-PARAMETER-CATALOG-DELTA-2026-07-23.md).

## Theory-depth wave (HWIKI-DOC-02..29) — refreshed 2026-07-23 (DOC-30)

- **Explainer blocks landed** on OPEN DOC targets this pass: PageRank structural analogy, PHI/icosahedron, DFT REJECTED, Gini, BM25, Jaccard, cosine, Louvain, clustering (PARTIAL+`layer_2` pin), circuit rank, contradiction→tension, penalty suite hub, propagation YAML ladder, fusion α/E_cap/η, FGR + share/freshness, Concept Dictionary status/extent terms, Geometry/Core Math/Propagation hub preambles.
- **Remaining theory gaps (next batch candidates):** deeper TRIZ inventives beyond Louvain/contradiction map; L7/L8 consumers of GLOBAL_STABILITY_SCORE; KME derived plain-lang names beyond stubs; CAT-01 leftover symbols; turn-boundary Mixing (dead [[cumulativeDrift / turnCoherence]] revival decision).

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
