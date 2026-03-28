# HESPERIA — TFP-GATE-INV: single entrypoint listing concept-level invariant coverage (dominance, length, competition).
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
#
# Heavy assertions live in focused modules; this file prevents "implied elsewhere" drift by importing them.

from __future__ import annotations


def test_concept_invariant_suite_importable() -> None:
    """Ensure invariant-related test modules remain importable (CD executor, env determinism)."""
    import tests.concept_dictionary.test_cd_executor  # noqa: F401 — CD / registry invariants
    import tests.test_env_determinism  # noqa: F401 — PYTHONHASHSEED / strict mode bar
