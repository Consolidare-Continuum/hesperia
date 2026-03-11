# Historical reference (pre-refactor)

# Core consolidation

**Date**: 2026-02-24
**Status**: Canonical

Single definition of the Hesperia core: what it is, what it uses, where it lives. One narrative; no duplicate authority.

---

## 1. What the core is

**Core** = one spec set + one default set + one code path. **Core math = L1–L9 only.**

| Component | Artifacts |
|-----------|------------|
| Resolution & pipeline contract | 22_SPEC__V0_3_Core_Math_Contract_v1_0.md |
| Instrumentation & gates (L1–L9) | 34_SPEC … 42_SPEC |
| Predefined defaults (thresholds, topology) | LAYER_1_9_PREDEFINED_DEFAULTS_v1_0.txt, layer_1_9_predefined_defaults_v1_0.json |
| Frozen state | Dict A, Dict B (and surface map if built); see §5 |
| Runtime config | guard_config_v1.json (22_SPEC pipeline) |

To run or evaluate the core you need: **22_SPEC + 34–42 + LAYER_1_9_PREDEFINED_DEFAULTS + frozen Dict A/B**; **guard_config_v1** for the pipeline. No other config for thresholds.

---

## 2. 22_SPEC vs 34–42

| Role | Spec(s) | Purpose |
|------|---------|---------|
| **What runs and decides** | 22_SPEC | Fusion, centroid, base + shadow traversal, aggregation → dominant family/area, penalties, metrics. Books non-voting. I-R2, I-R3, failure classes. |
| **What we measure and gate on** | 34_SPEC … 42_SPEC | Observability over attribution/traversal/evidence/stability. L1–L9 variables and gates; L7 DECISION_STATUS_CODE, OUTPUT_TRUST_TAG. |

22 = resolution and pipeline. 34–42 = observation and gates. Neither replaces the other.

---

## 3. Two config surfaces

| Config | Used by | Contents |
|--------|---------|----------|
| **guard_config_v1.json** | 22_SPEC | Fusion (alpha), traversal (lambda, decay, steps), shadow (max_hops, penalty), centroid (K_max, eta), penalties, books policy, failure policy. |
| **LAYER_1_9_PREDEFINED_DEFAULTS** (txt + json) | 34–42_SPEC | Topology F, A, FPA; eps/EPS/EPS_INT; L2 MAX_ALLOWED_DEPTH; L3 shadow caps; L4 TOP_K, MAX_SHORTFALL, MIN_SUPPORT, MAX_DUP_BOOK_CONC; L5 MAX_CONTRADICTION; L7 MIN_COVERAGE_RATIO, MAX_CROSS_AREA_RATIO, MAX_LYAPUNOV, HIGH_CONF, MED_CONF. |

Do not duplicate threshold names between the two without an explicit “same as” note. No asking for thresholds when computing L1–L9: use predefined defaults.

---

## 4. Single source for topology

**Topology constants** for the layer stack: **LAYER_1_9_PREDEFINED_DEFAULTS** (F=288, A=12, FAMILIES_PER_AREA=24, FPA=24). 13_SPEC (indexing) and 34_SPEC reference the same geometry; the canonical numeric source for L1–L9 is the predefined defaults file. Other specs refer to that or to 13_SPEC for indexing conventions, not the other way around.

---

## 5. Frozen state manifest

Canonical artifacts the core runs on (build outputs or curated):

| Artifact | Location / note |
|----------|------------------|
| Dict A (core star map) | hesperia_lex/curated/ (e.g. A_CORE_STAR_MAP_v0_4_1_3.json) |
| Dict B (runtime) | Build output (e.g. assets/v041) or curated; runtime dict for attribution |
| Surface map (if built) | v0.4.0 build output; hybrid terrain L/T/S/R |
| LAYER_1_9_PREDEFINED_DEFAULTS | LAYER_1_9_PREDEFINED_DEFAULTS_v1_0.txt, layer_1_9_predefined_defaults_v1_0.json |
| guard_config | guard_config_v1.json |

One place to check “what is the actual state the core runs on”: this manifest + RUNNABLE.md for build order.

---

## 6. Code path (single entry)

| Purpose | Command / path |
|---------|-----------------|
| Pre-test (build + core_math + pytest) | `python scripts/run_hesperia_pre_test.py` or `python sphere_rag/run_simulation.py pretest` |
| Full run | `python sphere_rag/run_simulation.py full` |
| Chroma run | `python sphere_rag/run_simulation.py chroma` |
| Core math (v0.3) | `python sphere_rag/hesperia_v03_core_math.py` / `... test` |
| Build v0.4.0 / v0.4.1 | See RUNNABLE.md |

Core = one spec set + one default set + this code path. Full list: RUNNABLE.md.

---

## 7. References

- DOC_INDEX.md — full doc map
- README.md — entry points table (includes Core pointer)
- LAYER_1_9_PREDEFINED_DEFAULTS_v1_0.txt — default values
- 22_SPEC §17 — ref to 34–42
