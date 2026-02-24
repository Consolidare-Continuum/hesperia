# HESPERIA v0.4.0 / v0.4.1 — Coverage Report

**Artifact**: Single deliverable coverage report.  
**Source**: `assets/v040` build outputs (full build, no `--allow-small-build`).  
**Date**: 2026-02-23.

---

## 1. Covered families (by Dict A anchors)

**288/288 covered.** Dict A v0.4.1 complete: 12 anchors per family, 3456 total. Deterministic keying (`lemma_normalized_familyNumber_slot`); no key collisions.

**Count**: 288 families with ≥1 anchor.

---

## 2. Missing families (no Dict A anchors)

**0 families.**

**Count**: 0 families.

---

## 3. Per-family anchor counts (Dict A)

- **288 families**: 12 anchors each.
- **0 families**: 0 anchors.
- **Total anchors**: 3456.
- **Distribution**: min=12, max=12, std dev=0 (audit PASS).

**Config**: `A_MIN` = 12, `MIN_ANCHORS_PER_FAMILY` = 12, `MAX_ANCHORS_PER_FAMILY` = 18 (build_v040_config.py §8, §8b).

---

## 4. Metric that triggered κ (and exact thresholds)

**κ result**: **PASS** (full build 2026-02-23).

- **Rule**: Build fails if any single family’s share of **Dict B** tokens exceeds KAPPA_MAX_SHARE.
- **Check**: For each family, `(token_count_in_family / total_dict_b_tokens) ≤ KAPPA_MAX_SHARE`.
- **This run**: Dict B total = 3456; per-family share &lt; 6%.

### Thresholds in effect (build_v040_config.py)

| Parameter                    | Value | Meaning |
|-----------------------------|-------|--------|
| **KAPPA_MAX_SHARE**         | 0.06  | No family may have more than 6% of Dict B tokens. |
| **F_MIN_COVERED**           | 240   | At least 240 families must have ≥1 Dict B token. |
| **MIN_DICT_B_TOKENS**       | 240   | Precheck: fail before κ if Dict B total &lt; 240 (unless allow_small_build). |
| **MIN_DICT_A_COVERED_FAMILIES** | 240 | Precheck: fail if Dict A anchors cover &lt; 240 families (unless allow_small_build). |
| **TOTAL_FAMILIES**          | 288   | Total number of families. Build fails if covered &lt; 288 (key collision). |
| **A_MIN**                   | 12    | Minimum anchors per family (diagnostic). |
| **MIN_ANCHORS_PER_FAMILY**  | 12    | Fail if any family &lt; 12 anchors (v0.4.1). |
| **MAX_ANCHORS_PER_FAMILY**  | 18    | Fail if any family &gt; 18 anchors (skew). |
| **MAX_ANCHOR_STD_DEV**      | 2.5   | Fail if std dev of per-family count &gt; 2.5. |
| **MIN_TOTAL_ANCHORS**       | 3456  | Fail if total anchors &lt; 3456. |

**Build manifest** (`assets/v040/build_manifest_v040.json`): `kappa_max_share: 0.06`, `tau: 0.35`, `delta: 0.05`.

---

**Source files**: `assets/v040/report_dictA_coverage_v040.txt`, `assets/v040/report_dictB_stats_v040.txt`, `assets/v040/build_manifest_v040.json`, `sphere_rag/build_v040_config.py`.  
**Freeze**: [DICT-A-FREEZE-v0_4_1.md](DICT-A-FREEZE-v0_4_1.md).
