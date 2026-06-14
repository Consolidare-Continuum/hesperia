# HESPERIA_CONTROL_MERGED_v1 — frozen appendix (Ethan HC-ETHAN-01)

**Date:** 2026-03-27  
**Role:** Ethan (architect)  
**Status:** **FROZEN** for HC program execution (cursor `active.md` HC-*).  
**Refs:** [ETHAN-HESPERIA-CONTROL-LAYER-V1-TASKING-2026-03-27.md](ETHAN-HESPERIA-CONTROL-LAYER-V1-TASKING-2026-03-27.md); Hesperia `docs/governance/cd_v1/MODEL_CARD_CD_PIPELINE.md`; operator HESPERIA CONTROL SPEC v1.0 (chat).

---

## 1. Authoritative layer chain (unchanged)

`A` → `B` → **`CD`** → **`C_agg`** (families / areas / hex) → **Topology**

Source of truth for **CD hook**: Hesperia repo `MODEL_CARD_CD_PIPELINE.md`.

---

## 2. Runtime hook order (vs `pipeline.py`)

**Shipped insertion point (CD):** `hesperia/engine/lexical_concept/pipeline.py` — **after** `_stabilize_concept_weights`, **before** `_post_hex_concept_feedback` / hex aggregation (`aggregate_hex_state`).

**New control slices — allowed insertion bands (no prod bypass):**

| Control | Band | Rule |
|--------|------|------|
| **B↔A validation / provenance (HC-01)** | After B/resolver outputs exist; **before** `apply_cd_phase1` | Trace-only or filter flags on concept activations; must map fields to existing resolver/DLCR schemas. |
| **Modifier MVP — negation + one damping (HC-03)** | **Between** `_stabilize_concept_weights` **and** `apply_cd_phase1` | **Frozen:** lexical-proximity modifiers adjust the **concept weight vector** consumed by CD; **no second modifier pass** after CD for MVP. |
| **Competition / co_occurs (HC-02)** | **Inside** CD Phase 2 executor math | **No** standalone `concept_competition.py` without ADR that retires overlap with CD. |
| **Strict dominance (HC-05)** | **After** segment-level `C_agg` / area (or **declared public projection**) | **Must not** rewrite hex field **H** in a way that violates sealed product-signal causality (signals stay functions of **H** per sealed stack). Dominance is **readout/policy**, not a second causal input to product formulas. |
| **Unmapped diagnostics (HC-08)** | Side channel / post-linking | **Non-blocking**; no dictionary mutation. |
| **Cross-plane agreement (HC-09)** | Release gate / audit | **Not** required inline per segment until plane schemas are comparable. |

**Env / flags:** Continue `HESPERIA_CD_ENABLED`, `HESPERIA_CD_DISABLE`, `HESPERIA_CD_JSONL`, `HESPERIA_CD_PHASE` per MODEL_CARD. Additional gates get **new versioned keys** (e.g. `hesperia_control_calibration_v0`) — no silent defaults.

---

## 3. Modifier placement (single ruling)

- **MVP modifiers (HC-03)** = **pre-CD** adjustment of stabilized concept weights (see §2 table).  
- **CD `type: modifier` and CD `effects` (amplify/inhibit)** = **CD-internal** per CD v1 execution doc.  
- **Precedence:** If a concept’s CD row defines an effect that **conflicts** with pre-CD lexical modifier for the same concept in the same segment, **CD wins** for that concept; log **both** contributions in trace for audit.

Full modifier taxonomy (temporal, scope limiter, …) **blocked** until **entity = span | turn | clause** is frozen (CD-T19 lineage).

---

## 4. Anti-duplication matrix (operator spec → owner)

| Operator CONTROL SPEC block | Disposition | Owner / artifact |
|----------------------------|-------------|-------------------|
| §1 B↔A validation | **HC-01** — trace + rules; align resolver | Noah |
| §2 Concept competition | **CD Phase 2** unified math | Marcus HC-02 + Gena executor when enabled |
| §3 Modifier propagation | **HC-03** pre-CD MVP + CD effects | Gena |
| §4 Unmapped token engine | **HC-08** diagnostics only | Gena |
| §5 Concept normalization | **Deferred** — offline calibration / `cd_calibration_vN`; no hot-path corpus prevalence | Grace/Ethan reopen |
| §6 Interaction compilation | **CD Phase 3** single compiler track | Gena + Liam; no parallel compiler package |
| §7 Strict dominance | **HC-05** post-C_agg policy | Gena |
| §8 Cross-plane agreement | **HC-09** gate schema | Olivia |
| §9 Length invariance | Segment normalization + tests; tie to metric registry | Noah HC-06 + Daniel HC-07 (slices) |
| §10 Test invariants | Extend existing double-run / gold | Daniel HC-07, Noah HC-06 |

---

## 5. Execution order vs operator §11

Operator list is **reordered** to match §2 table and MODEL_CARD. **Unmapped** may run **parallel** (diagnostic). **Cross-plane** default **post-run**.

---

`SIGNED: Architect (Ethan) | HESPERIA_CONTROL_MERGED_v1 appendix | 2026-03-27 | HC-ETHAN-01`
