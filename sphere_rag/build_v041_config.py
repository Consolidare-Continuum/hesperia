# HESPERIA v0.4.1 Dict B build — config (normative defaults per 29_SPEC)
from __future__ import annotations

TOTAL_FAMILIES = 288
MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"

# §5 Classification variables
TAU = 0.35
DELTA_MIN_PRIMARY = 0.05
TAU_RELAXED = 0.30
DELTA_MAX_SECONDARY = 0.12
FAMILY_OVERLAP_CAP = 0.80
FCS_MIN = 0.40
MAX_SECONDARY_RATIO_GLOBAL = 0.40
SECONDARY_PER_FAMILY_RATIO = 0.5  # secondary_count_F ≤ 0.5 × primary_count_F
KAPPA_MAX_SHARE = 0.06
LEXICAL_SLOTS_PER_FAMILY = 600

# §9 Failure conditions
AMBIGUOUS_PCT_MAX = 0.20  # build aborts if > 20% tokens ambiguous
WEAK_ANCHOR_PCT_MAX = 0.10  # build aborts if > 10% assigned via weak anchors (OSS < threshold)
OSS_THRESHOLD = 0.07  # weak anchor if OSS < this (from §8A)
