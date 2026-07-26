# HESPERIA — RAD. Ethan PO-03 / PO-04 matcher behavior.
from __future__ import annotations

from core.lexical.matcher import match_dict_a


def test_longest_span_wins_at_same_start() -> None:
    text = "object relations theory"
    entries = [
        {
            "entry_id": "e1",
            "normalized_form": "object",
            "match_type": "phrase",
            "candidate_concept_ids": ["C1"],
            "priority": 0,
        },
        {
            "entry_id": "e2",
            "normalized_form": "object relations",
            "match_type": "phrase",
            "candidate_concept_ids": ["C2"],
            "priority": 0,
        },
    ]
    acc, rej = match_dict_a(text, entries)
    assert len(acc) == 1
    assert acc[0].matched_text == "object relations"
    assert acc[0].entry_id == "e2"


def test_max_accepted_caps_deterministically() -> None:
    text = "a b c d e"
    entries = [
        {
            "entry_id": f"e{i}",
            "normalized_form": tok,
            "match_type": "exact",
            "candidate_concept_ids": [f"C{i}"],
            "priority": 0,
        }
        for i, tok in enumerate(text.split(), start=1)
    ]
    acc, rej = match_dict_a(text, entries, max_accepted=2)
    assert len(acc) == 2
    assert len(rej) >= 1
