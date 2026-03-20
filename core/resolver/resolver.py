"""Deterministic lexical-candidate to concept resolver."""

from __future__ import annotations

from typing import Any

from core.lexical.matcher import LexicalHit
from core.resolver.context import coherence_from_related, label_token_overlap
from core.resolver.score_rules import score_candidate
from core.resolver.tiebreaks import break_tie


def resolve_hit(
    hit: LexicalHit,
    concept_index: dict[str, dict],
    mode: str = "default",
    version: str = "v0.6.0",
    *,
    canonical_text: str | None = None,
    context_window: int = 48,
    association_boost: dict[str, float] | None = None,
) -> dict[str, Any]:
    """
    Resolve a single lexical hit to a winning concept (Ethan PO-05–PO-09).

    ``canonical_text`` enables deterministic context overlap (PO-07).
    ``association_boost`` adds bounded prior mass from co-occurrence layer (PO-23).
    """
    association_boost = association_boost or {}
    siblings = frozenset(str(x) for x in hit.candidate_concept_ids)
    candidate_scores: dict[str, float] = {}
    candidate_detail: list[dict[str, Any]] = []

    for concept_id in hit.candidate_concept_ids:
        concept = concept_index.get(concept_id, {})
        ctx_n = 0
        if canonical_text:
            label = str(concept.get("preferred_label") or "")
            ctx_n = label_token_overlap(
                canonical_text, hit.span_start, hit.span_end, label, window=context_window
            )
        coh = coherence_from_related(concept_id, concept_index, sibling_ids=siblings)
        boost = float(association_boost.get(concept_id, 0.0))
        sc = score_candidate(
            match_type=hit.match_type,
            priority=hit.priority,
            specificity_rank=int(concept.get("specificity_rank", 0)),
            context_overlap=ctx_n,
            coherence_boost=coh,
        ) + boost
        candidate_scores[concept_id] = sc
        candidate_detail.append(
            {
                "concept_id": concept_id,
                "score": round(sc, 6),
                "context_overlap": ctx_n,
                "coherence_boost": round(coh, 6),
                "association_boost": round(boost, 6),
            }
        )

    if not candidate_scores:
        winner = None
        reasons = ["no_candidates"]
        rejected = ["no_candidate_scores"]
    else:
        top_score = max(candidate_scores.values())
        top_candidates = [cid for cid, val in candidate_scores.items() if val == top_score]
        if len(top_candidates) == 1:
            winner = top_candidates[0]
            reasons = ["top_score_unique"]
        else:
            winner = break_tie(top_candidates, concept_index)
            reasons = ["top_score_tie", "tiebreak_specificity_then_lexical_id"]
        rejected = [f"candidate_rejected:{cid}" for cid in candidate_scores if cid != winner]

    return {
        "source_text_span": hit.matched_text,
        "source_char_start": hit.span_start,
        "source_char_end": hit.span_end,
        "normalized_span": hit.matched_text,
        "lexical_entry_ids": [hit.entry_id],
        "candidate_concepts": list(hit.candidate_concept_ids),
        "candidate_scores": {k: round(v, 6) for k, v in candidate_scores.items()},
        "winning_concept_id": winner,
        "winning_reason_codes": reasons,
        "rejected_reason_codes": rejected,
        "rule_trace": [
            "phrase-first",
            "match-strength",
            "context_overlap",
            "coherence_related",
            "association_boost_optional",
            "tiebreak_specificity_lexical",
        ],
        "audit": {
            "candidates_detail": candidate_detail,
            "tie_break_rule": "specificity_rank_desc_then_concept_id_lex",
        },
        "mode": mode,
        "version": version,
    }

