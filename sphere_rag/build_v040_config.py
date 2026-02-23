# HESPERIA v0.4.0 build — config (normative defaults per 28_SPEC)
from __future__ import annotations

TOTAL_FAMILIES = 288
SIDES_PER_FAMILY = 1500
HEXES_PER_FAMILY = 250
SIDES_PER_HEX = 6
TOTAL_SIDES = 432_000

# §8 Anchor
A_MIN = 12

# §9 Similarity
TAU_DEFAULT = 0.35
DELTA_DEFAULT = 0.05
MU_DEFAULT = "flag_and_assign"  # flag_and_assign | flag_and_reject
K_TOP = 5

# §10 Anti-collapse
KAPPA_MAX_SHARE = 0.06
F_MIN_COVERED = 240

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
