# HESPERIA — RAD. Unified analysis text preparation (Ethan PO-01, PO-14).
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

"""Single preprocessing contract before structural multiscale + DLCR paths."""

from __future__ import annotations

import hashlib
import os
from typing import Any


def _clinical_role_line_fold(canonical: str) -> str:
    """
    Optional transcript softening: fold speaker role tags into spaces (same tokens remain).
    Enabled when policy is clinical_speech AND HESPERIA_CLINICAL_STRIP_ROLES=1.
    """
    if os.environ.get("HESPERIA_CLINICAL_STRIP_ROLES", "").strip().lower() not in ("1", "true", "yes", "on"):
        return canonical
    from hesperia.nlp.transcript_speaker_labels import CLINICAL_ROLE_STRIP_PATTERN

    lines = canonical.split("\n")
    out: list[str] = []
    for line in lines:
        out.append(CLINICAL_ROLE_STRIP_PATTERN.sub(" ", line).strip())
    return "\n".join(s for s in out if s).strip() or canonical


def prepare_structural_analysis_text(
    text: str,
    *,
    policy_mode: str | None = None,
) -> tuple[str, dict[str, Any]]:
    """
    Return (canonical_text, preprocess_meta) for deterministic downstream use.

    PO-01: NFKC, casefold, whitespace normalization via ``normalize_text``.
    PO-14: optional clinical transcript folding when env + speech-like policy.
    """
    from core.lexical.normalization import normalize_text

    raw = (text or "").strip()
    if not raw:
        return "", {"empty": True, "analysis_text_fingerprint": ""}

    n = normalize_text(raw)
    canonical = n["canonical_text"]
    mode_l = (policy_mode or os.environ.get("HESPERIA_DLCR_POLICY_MODE", "") or "default").strip().lower()
    clinical_soften = False
    if mode_l in ("clinical_speech", "speech_clinical", "clinical"):
        folded = _clinical_role_line_fold(canonical)
        if folded != canonical:
            clinical_soften = True
            canonical = folded
            n = normalize_text(canonical)
            canonical = n["canonical_text"]

    fp = hashlib.sha256(canonical.encode("utf-8")).hexdigest()[:24]
    meta: dict[str, Any] = {
        "policy_mode": policy_mode or "default",
        "analysis_text_fingerprint": fp,
        "token_count": len(n["tokens"]),
        "phrase_span_count": len(n["phrase_spans"]),
        "clinical_role_fold_applied": clinical_soften,
        "preprocess_version": "hesperia_text_prep_v1",
    }
    return canonical, meta
