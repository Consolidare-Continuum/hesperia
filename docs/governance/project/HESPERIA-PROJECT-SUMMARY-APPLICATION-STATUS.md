<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Hesperia project — summary in relation to real application status

**Purpose**: Bullet-statement summary for manager/assistant use. Three sections: what it is, what it does, what it uses. **Status**: As of V1 fixed point 2026-02-18. **Format**: .md only.

---

## 1. What it is

- **Hesperia** is the prichindel.com semantic-substrate product (matrix, sphere, RAG, families); ownership and IP: prichindel.com / igareosh.
- **Technically**: A **geometry-safe semantic traversal kernel** — in product terms, a **deterministic semantic traversal and validation core**.
- **Structure-only**: Fixed geometry (12 areas × 24 families × 250 hexes per family; 72k hexes, 432k sides). No semantic reasoning, no value-evaluating, no content-level conflict detection in the kernel.
- **Canonical areas**: GOOD, HARM, TRUTH, DECEIT, ORDER, CHAOS, FREEDOM, CONTROL, CARE, INDIFFERENCE, CREATION, DESTRUCTION — in a ring. Each area has 24 families (288 families total).
- **Mid-stage engine**: Agents-oriented layer is live; product semantic layer (full RAG in product workspace) is out of scope until Phase D.
- **Cursor repo role**: Cursor (and Cursor main when invoked) is the **main invoker** of Hesperia in the cursor repo — context_rag.py for full packet, matrix_run for geometry/path, run_core_mode_invocation for core-mode calibration.
- **Fixed point**: Release V1 fixed point 2026-02-18 defines the baseline; all new Hesperia work starts from there. Backup: archive/hesperia-fixed-point-20260218/.
- **Direction locked**: A (harden structure). **Spec locked**: Safeguard State Machine Spec v0.1 (three consecutive logical failures → stop; valid_streak ≥ 2 to reset).
- **Do not touch** (until Phase D): ring ordering, area adjacency, family counts, hex geometry, safeguard threshold.
- **Not yet**: Semantic weight per area, content polarity mapping, family-level constraint logic, inter-family contradiction detection, multi-path interference, region/obstacle semantics beyond simple fail detection.

---

## 2. What it does

- **Deterministic ring traversal**: Given start area (0–11), direction (clockwise/counter-clockwise), and steps, produces one path: road_coordinates (step, area_id, global_id, area_name, family_name), border_passings (area and family crossings), traversal_length, is_loop.
- **Context packet**: Single entry point (context_rag.py) returns calculable block (geometry, path_params, road_coordinates, border_passings, traversal_length, is_loop, loopability) plus coherence_hints and **observability** (loopability_band, entropy_metric, border_passings_count, direction, ring_distance_from_start, safeguard_events_count). Optional retrieval (families, books chunks) when --query or --area_id or --family_name.
- **Context governor**: Forces current area, adjacent areas, border context, traversal history for AI/agents — prevents topic teleportation, axis skipping, semantic drift.
- **Logic layer**: Path-level validity check (Hex.evaluate); run_traversal_with_safeguard runs path step-by-step, records hop result (valid/invalid), triggers SAFEGUARD_STOP after three consecutive failures; stores fail_trace, marks obstacle region.
- **Coverage accounting (Apple)**: apple_path_imprint stores path from a run; apple_involvements reports which areas and families were touched — policy audit, balance audit, bias detection (e.g. “Did we skip HARM?”).
- **Path validation**: Arbitrary paths can be tested; jumps or polarity flips can be injected; safeguard triggers observed — calibration, stress-testing, QA.
- **Path comparison**: Clockwise vs counter-clockwise, partial arcs vs full ring, start shifts — experimental lab for traversal heuristics and structural bias.
- **Core-mode calibration**: run_core_mode_invocation runs matrix_run → context_rag (no retrieval) → hesperia_logic → apple_path_imprint → apple_involvements; logs all outputs to timestamped dir; internal use only, not product spec.
- **Loopability**: Formula reference in packet; L_full value when activation data provided (--activation PATH). No automated activation pipeline yet.
- **Real applications today**: Structured AI assistant context stabilizer; policy traversal audit tool; semantic bias detector (coverage); narrative flow analysis (path); controlled reasoning sandbox (logic + safeguard).

---

## 3. What it uses

- **Matrix source**: Canonical CSV (CLIENTS/hesperia/v0.1/hex_sphere_areas_families_ideal_proportions.csv) or Chroma layer=hesperia_families. Matrix is read-only in core mode; coordinates (area_id, area_name, family_name, global_id) and geometry constants only.
- **Chroma**: layer=hesperia_families for matrix when --chroma; optional retrieval (families, books chunks) via context_rag when query/area_id/family_name given. Chroma operational on prichindel; cursor repo uses it for context and optional retrieval.
- **Scripts (cluster/chroma-server)**: matrix_run.py (geometry, path, road_coordinates, border_passings); context_rag.py (calculable + coherence_hints + optional retrieval); hesperia_logic.py (Area, Family, Hex, Path, Hop, TraversalSafeguard, run_traversal_with_safeguard, VALIDATE/SATISFY/UNSAT/ENTAILS); run_core_mode_invocation.py (Plan 1 calibration); apple_path_imprint.py, apple_involvements.py; hesperia_safeguard_stress_test.py.
- **Rules**: .cursor/rules/cursor-main-awareness.mdc — Context RAG (full packet), Matrix-derived context (matrix_run or Chroma layer=hesperia_families). Packet schema: governance/CONTEXT-RAG-PACKET-SCHEMA.md.
- **Governance**: ETHAN-HESPERIA-STATE-NOW-ASSESSMENT (what it is/does, do not touch, fork); ETHAN-HESPERIA-CORE-MODE-MVP (core mode scope); ETHAN-HESPERIA-LOOP-SAFEGUARD; ETHAN-HESPERIA-OPERATOR-INTERFACE-SPEC; GRACE-HESPERIA-NEXT-DIRECTION (direction A, Safeguard Spec v0.1); CONTEXT-RAG-PACKET-SCHEMA; HESPERIA_OBSERVABILITY_EXTENSION_v0_1 (observability block); ETHAN-HESPERIA-POST-V01-FORMAL-DEFINITIONS (governance equation GO, risk analysis; B/C deferred); ETHAN-HESPERIA-WATERLINE-PRINCIPLE (capacity doctrine and waterLevel equation, definition only); HESPERIA-FAMILIES-CHROMA-SCHEMA; projects/hesperia/ (CONTEXT-PACKET, PROJECT-CHARTER, RELEASE-V1-FIXED-POINT-2026-02-18, mid-stage report).
- **Data dir**: HESPERIA_DATA_DIR or repo CLIENTS/hesperia for CSV and data paths.
- **Activation data**: Optional JSON file (--activation PATH) for L_full in calculable.loopability; no automated feed.
- **Deploy**: No separate service unit; scripts run on-demand from repo root (cursor repo or prichindel); Chroma assumed available (e.g. :8002) for retrieval and matrix when --chroma.
- **FPF/books**: When retrieval is used, books chunks can be scoped by bounding(concept, source, family, area). FPF layer in Chroma is separate; Hesperia uses hesperia_families and optionally books for retrieval. Structure is sovereign over content.

---

*End of summary. Ref: RELEASE-V1-FIXED-POINT-2026-02-18.md, ETHAN-HESPERIA-STATE-NOW-ASSESSMENT.md, HESPERIA-MID-STAGE-PRODUCT-REPORT.md.*
