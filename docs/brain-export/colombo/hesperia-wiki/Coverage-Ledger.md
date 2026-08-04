# Coverage Ledger

[← wiki home](index.md)

This wiki covers **401 items** verified on `/data/hesperia/hesperia` (347 live/beyond, 33 partial, 21 dead/rejected, 0 unverified). It is **not** a full census of every variable in the codebase — bounded to inspected research passes plus HWIKI expansion waves.

**Expansion waves:** all-encompassing `HWIKI-*` — [GRACE-TRIAGE-HESPERIA-WIKI-ALL-ENCOMPASSING-2026-07-19.md](../../../operational/assignments/GRACE-TRIAGE-HESPERIA-WIKI-ALL-ENCOMPASSING-2026-07-19.md). **Theory-depth 30** (`HWIKI-DOC-01..30`) — [GRACE-TRIAGE-HESPERIA-WIKI-DOC-THEORY-DEPTH-30-2026-07-19.md](../../../operational/assignments/GRACE-TRIAGE-HESPERIA-WIKI-DOC-THEORY-DEPTH-30-2026-07-19.md). **Structure / how-it-works (post 0.7.0)** (`HWIKI-STRUCT-*`) — [GRACE-TRIAGE-HESPERIA-WIKI-STRUCT-070-2026-07-26.md](../../../operational/assignments/GRACE-TRIAGE-HESPERIA-WIKI-STRUCT-070-2026-07-26.md). Gaps below are backlog, not permanent silence.

## Explicitly NOT yet covered (real gaps in this wiki, not silently omitted)

- **L1–L9 pipeline layer variables** (`34_SPEC`…`42_SPEC`) — **HWIKI-CATALOG wave, 2026-08-04: full census landed, including L6.** L1 through L9 all wikified (L1 hub [L1 — Structural Activation Census](pages/L1-Structural-Activation-Census.md), L2–L9 hubs alongside), and L6's Group-IV stubs (HIT_VECTOR_RANK, PRINCIPAL_COMPONENT_ENERGY_RATIO, ESCAPE_ENERGY_THRESHOLD, FORCE_ANALOG_MAGNITUDE, MONOTONICITY_CHECK, FIXED_POINT_DETECTION, CYCLE_DETECTION_FUNCTIONAL) closed the same day — all 25 L6 keys now wikified, 24 L6-related pages total. **Correction:** the pipeline terminates at L9 (`docs/foundations/output_catalog.md` calls it "the terminus" explicitly) — there is no L10/L11; the old "L1–L11" phrasing in this ledger was stale/aspirational, not a real gap. See [GRACE-TRIAGE-HESPERIA-WIKI-CATALOG-ABSORB-2026-08-04.md](../../../operational/assignments/GRACE-TRIAGE-HESPERIA-WIKI-CATALOG-ABSORB-2026-08-04.md) for the closure record.
- **KME derived metrics** — **35 derived + hub wikified** (35 derived pages + [KME Primitives and Derived Metrics](pages/KME-Primitives-and-Derived-Metrics.md)). **HWIKI-KME-03:** plain-lang Theory Explainer notes on each derived page.
- **TRIZ extension internals** (`hesperia/extensions/triz/`, 30+ modules) — **contradiction core hub landed** (HWIKI-TRIZ-02); **the three named export products landed 2026-08-04** (HWIKI-CATALOG-BRIDGE: [Policy Contradiction Detector](pages/Policy-Contradiction-Detector-TRIZ-export.md), [Innovation Radar](pages/Innovation-Radar-TRIZ-export.md), [Narrative Propagation Monitor](pages/Narrative-Propagation-Monitor-TRIZ-export.md)). Remaining: the internal implementation modules beneath these exports (30+ files) are not individually wikified — only their shaped output products are.
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

## Plain-language definition wave (HWIKI-PLAIN) — opened 2026-08-04

**Mandate:** every parameter/term page answers **Receives / Does / Outputs / Exists for** in ordinary words **and** keeps the formula. Template: [TEMPLATES-PLAIN-DEFINITION.md](TEMPLATES-PLAIN-DEFINITION.md). Live: [http://wiki.hesperia.local/](http://wiki.hesperia.local/). Prod-of-record mirror: `Consolidare-Continuum/hesperia` → `docs/brain-export/colombo/hesperia-wiki/`.

- **Batch A landed:** page renderer always emits **In plain words** + **Definition**; L1–L9 catalog + L9 terminus + fpf_bridge states promote `_meaning` → Theory Explainer `plain_lang`.
- **Batch B landed (2026-08-04):** `backfill_plain_lang()` fills remaining LIVE/PARTIAL/BEYOND/DEAD rows from existing formula+notes (no invented science).
- **Batch C landed (2026-08-04):** hand-polish for algebra-shaped rows (KME derived sentences + curated core/L6/SI/ontology plains). Coverage **401/401** with `plain_lang`.
- **HWIKI-WIRE landed (2026-08-04):** bidirectional hub↔member edges, orphan→category anchors, DEAD→LIVE successors, autolink of known names, **See also** on every page, [Wiki Wire Map](pages/Wiki-Wire-Map.md). Orphans remaining: **0**.
- **Still open:** Felix export/promote to `Consolidare-Continuum/hesperia`; Abelard CHROMA-1 `hesperia_wiki` re-ingest.


## Cheap, concrete next-wave candidates

- **Still open:** Add `compute_dominant_family_share` as a real page once/if built (mirrors [dominant_area_share_threshold](pages/dominant-area-share-threshold.md)) — see [X_A / X_F alignment (Java)](pages/X-A-X-F-alignment-Java.md). Re-checked 2026-08-04: still doesn't exist in source.
- **DONE 2026-08-04:** ~~Finish remaining L6 variables~~ — all 25 L6 keys now wikified (Group-IV stubs HIT_VECTOR_RANK/PRINCIPAL_COMPONENT_ENERGY_RATIO/ESCAPE_ENERGY_THRESHOLD/FORCE_ANALOG_MAGNITUDE/MONOTONICITY_CHECK/FIXED_POINT_DETECTION/CYCLE_DETECTION_FUNCTIONAL landed HWIKI-CATALOG-L6-GROUP-IV). ~~then L7/L8 consumers of GLOBAL_STABILITY_SCORE~~ — subsumed by the full L7/L8/L9 HWIKI-CATALOG batches.
- **DONE 2026-08-04, re-verified not just assumed:** ~~Wikify CAT-01 delta list~~ — the CAT-01 delta doc itself (`COLOMBO-HWIKI-CAT-01-PARAMETER-CATALOG-DELTA-2026-07-23.md`, linked above) doesn't exist on disk, so checked source directly: diagnostic `ultra_sparse_coverage_threshold` already has its own page, all 4 FGR numeric-table constants (`DOMINANT_SHARE_HIGH`, `ENTROPY_DROP_SIGNIFICANT`, `STABILITY_CURRENT_THRESHOLD`, `STABILITY_STALE_THRESHOLD`) already wikified. Field Dynamics extension constants remain a deliberate scope exclusion (no consumer path — `EXTENSION_STATUS.yaml` classifies it `internal`), not an oversight.
