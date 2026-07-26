from __future__ import annotations

from core.lexical.matcher import LexicalHit
from core.resolver.resolver import resolve_hit


def test_resolver_picks_top_specificity() -> None:
    hit = LexicalHit(
        entry_id="A-1",
        matched_text="identity diffusion",
        span_start=0,
        span_end=18,
        match_type="phrase",
        candidate_concept_ids=["C-LOW", "C-HIGH"],
        priority=10
    )
    concept_index = {
        "C-LOW": {"specificity_rank": 2, "preferred_label": "low"},
        "C-HIGH": {"specificity_rank": 7, "preferred_label": "high"},
    }
    out = resolve_hit(hit, concept_index, mode="clinical_speech")
    assert out["winning_concept_id"] == "C-HIGH"
    assert out["candidate_scores"]["C-HIGH"] > out["candidate_scores"]["C-LOW"]


def test_resolver_is_schema_compatible() -> None:
    hit = LexicalHit(
        entry_id="A-2",
        matched_text="split",
        span_start=3,
        span_end=8,
        match_type="exact",
        candidate_concept_ids=["C-A"],
        priority=1
    )
    out = resolve_hit(hit, {"C-A": {"specificity_rank": 1, "preferred_label": "a"}})
    assert "rule_trace" in out
    assert "winning_reason_codes" in out
    assert "rejected_reason_codes" in out
    assert "audit" in out


def test_tiebreak_lexical_id_when_scores_and_specificity_equal() -> None:
    hit = LexicalHit(
        entry_id="x",
        matched_text="tie",
        span_start=0,
        span_end=3,
        match_type="exact",
        candidate_concept_ids=["Z-WING", "A-WING"],
        priority=0,
    )
    concepts = {
        "Z-WING": {"specificity_rank": 3, "preferred_label": "zztop"},
        "A-WING": {"specificity_rank": 3, "preferred_label": "aaalpha"},
    }
    out = resolve_hit(hit, concepts, canonical_text="tie blob")
    assert out["winning_concept_id"] == "A-WING"
    assert any("tiebreak" in x for x in out.get("winning_reason_codes", []))

