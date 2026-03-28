# HESPERIA — TFP-REL-01..04: real lexical unmapped, pipeline CD delta, competition stability.
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
from __future__ import annotations

import os
from pathlib import Path

import pytest

from hesperia.engine.lexical_concept.pipeline import (
    compute_lexical_unmapped_token_rate,
    run_dlcr_pipeline,
)

REPO = Path(__file__).resolve().parents[1]
CORPUS = REPO / "tests" / "fixtures" / "tfp_rel_real_corpus.txt"


def _dominant_area(area_activation: dict) -> str | None:
    if not area_activation:
        return None
    return max(area_activation, key=lambda k: float(area_activation[k]))


def _l1_area(a: dict, b: dict) -> float:
    keys = set(a) | set(b)
    return sum(abs(float(a.get(k, 0.0)) - float(b.get(k, 0.0))) for k in keys)


@pytest.fixture
def _restore_cd_env() -> None:
    saved = {
        "HESPERIA_CD_ENABLED": os.environ.get("HESPERIA_CD_ENABLED"),
        "HESPERIA_CD_DISABLE": os.environ.get("HESPERIA_CD_DISABLE"),
        "HESPERIA_CD_PHASE": os.environ.get("HESPERIA_CD_PHASE"),
    }
    yield
    for k, v in saved.items():
        if v is None:
            os.environ.pop(k, None)
        else:
            os.environ[k] = v


def test_unmapped_rate_real_sample() -> None:
    """TFP-REL-01: checked-in corpus; real matcher + dict merge (not JSON fixture formula only)."""
    text = CORPUS.read_text(encoding="utf-8")
    lines = [ln for ln in text.splitlines() if ln.strip() and not ln.strip().startswith("#")]
    blob = "\n".join(lines)
    rate = compute_lexical_unmapped_token_rate(blob, mode="clinical_speech")
    cap = float(os.environ.get("HESPERIA_REL_REAL_UNMAPPED_RATE_MAX", "0.95"))
    assert rate <= cap, f"lexical_unmapped_token_rate={rate} > cap={cap}"


def test_pipeline_cd_delta_final_areas(_restore_cd_env) -> None:
    """TFP-REL-02: CD on vs off must change final area_activation within bounds."""
    text = "примитивное расщепление в терапии тревога структура"
    os.environ["HESPERIA_CD_ENABLED"] = "1"
    os.environ.pop("HESPERIA_CD_DISABLE", None)
    os.environ["HESPERIA_CD_PHASE"] = "2"
    on = run_dlcr_pipeline(text, mode="clinical_speech")
    os.environ["HESPERIA_CD_ENABLED"] = "0"
    os.environ["HESPERIA_CD_DISABLE"] = "1"
    off = run_dlcr_pipeline(text, mode="clinical_speech")
    delta = _l1_area(on.get("area_activation") or {}, off.get("area_activation") or {})
    assert delta > 1e-9, "CD had no effect on final areas (useless CD)"
    assert delta < 1e6, "CD delta implausible (instability guard)"


def test_competition_stability_double_run_and_trim() -> None:
    """TFP-REL-04: same dominant area after duplicate run and whitespace-normalized variant."""
    base = "примитивное расщепление в терапии"
    a1 = _dominant_area(run_dlcr_pipeline(base, mode="clinical_speech")["area_activation"])
    a2 = _dominant_area(run_dlcr_pipeline(base, mode="clinical_speech")["area_activation"])
    assert a1 == a2
    padded = f"  \n{base}  \n"
    a3 = _dominant_area(run_dlcr_pipeline(padded, mode="clinical_speech")["area_activation"])
    assert a3 == a1
