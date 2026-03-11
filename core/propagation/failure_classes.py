"""
HESPERIA v0.3 / v0.3.1 — failure classification.
19_SPEC Release v0.3 Structural Enforcement; 20_SPEC Runtime Guards and Failure Classes.
No free-form error logic; use only these classes.
"""

from enum import Enum, auto


class FailureClass(Enum):
    HARD_STOP = auto()
    DATA_REJECT = auto()
    DEGRADED_STATE = auto()
    WARN = auto()
