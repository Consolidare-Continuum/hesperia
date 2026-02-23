# HESPERIA v0.4.0 build — config (normative defaults per 28_SPEC)
from __future__ import annotations

TOTAL_FAMILIES = 288
SIDES_PER_FAMILY = 1500
HEXES_PER_FAMILY = 250
SIDES_PER_HEX = 6
TOTAL_SIDES = 432_000

# §8 Anchor
A_MIN = 12

# §8b Dict A: default v0.4.1.1 (semantic, gates); v0.4.1 (12×288 complete) deprecated
MIN_ANCHORS_PER_FAMILY = 12   # fail if any family has fewer (unless allow_small_build)
MAX_ANCHORS_PER_FAMILY = 18   # fail if any family has more (excessive skew)
MAX_ANCHOR_STD_DEV = 2.5      # fail if std dev of per-family anchor count > this
MIN_TOTAL_ANCHORS = 3456      # 288 * 12 minimum (unless allow_small_build)

# §8c v0.4.1.1 semantic correction
MAX_LABEL_ANCHORS_PER_FAMILY = 4   # fail if ≥5 anchors match normalized family label
MIN_REAL_ANCHORS_PER_FAMILY = 8    # fail if real (non-label) anchors < 8 per family
MIN_WEIGHT_TIERS_PER_FAMILY = 3    # fail if unique weight tiers per family < 3

# §9 Similarity
TAU_DEFAULT = 0.35
DELTA_DEFAULT = 0.05
MU_DEFAULT = "flag_and_assign"  # flag_and_assign | flag_and_reject
K_TOP = 5

# §10 Anti-collapse
KAPPA_MAX_SHARE = 0.06
F_MIN_COVERED = 240

# §10a Build-time sanity prechecks (fail before κ on tiny builds)
MIN_DICT_B_TOKENS = 240  # hard fail if Dict B total tokens below this (unless allow_small_build)
MIN_DICT_A_COVERED_FAMILIES = 240  # hard fail if Dict A anchors cover fewer families (unless allow_small_build)

# §11 Build modes
MODE_STRICT = {"tau": 0.40, "delta": 0.06, "mu": "flag_and_reject"}
MODE_BALANCED = {"tau": 0.35, "delta": 0.05, "mu": "flag_and_assign"}
MODE_EXPLORATORY = {"tau": 0.30, "delta": 0.04, "mu": "flag_and_assign"}

# §13 Surface role quotas per family (1500 sides)
ROLE_L, ROLE_T, ROLE_S, ROLE_R = "L", "T", "S", "R"
QUOTA_L, QUOTA_T, QUOTA_S, QUOTA_R = 600, 450, 300, 150
L_MAX_PER_HEX = 3
T_MIN_PER_HEX = 1

MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"

# §8A Affinity diagnostics
OSS_THRESHOLD = 0.07  # flag lemma if OSS < this
OSS_AMBIGUOUS_PCT_MAX = 0.15  # warn/fail if % lemmas with OSS < OSS_THRESHOLD exceeds this
FCS_THRESHOLD = 0.45  # flag family if FCS < this
FCS_FAIL = 0.40  # hard fail if any family FCS < this
CFL_CROSS_SIM_MAX = 0.75  # warn if any two families mean cross-similarity > this
