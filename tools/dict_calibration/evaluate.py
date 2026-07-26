# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
"""Task 6 — Run DLCR (Hesperia) evaluation over sample texts + calibration dicts."""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any

from hesperia.engine.lexical_concept.pipeline import run_dlcr_pipeline

from . import repo_root


def _shannon_entropy(weights: dict[str, float]) -> float:
    tot = sum(max(0.0, float(v)) for v in weights.values())
    if tot <= 0:
        return 0.0
    h = 0.0
    for v in weights.values():
        p = max(0.0, float(v)) / tot
        if p > 0:
            h -= p * math.log(p + 1e-15, 2)
    return h


def _coverage(canonical: str, span_outputs: list[dict[str, Any]]) -> float:
    if not canonical:
        return 1.0
    n = len(canonical)
    mask = [0] * n
    for s in span_outputs:
        ss = s.get("source_char_start")
        se = s.get("source_char_end")
        if isinstance(ss, int) and isinstance(se, int) and 0 <= ss < se <= n:
            for j in range(ss, se):
                mask[j] = 1
            continue
        mt = str(s.get("source_text_span") or "")
        if not mt:
            continue
        start = 0
        while True:
            idx = canonical.find(mt, start)
            if idx < 0:
                break
            for j in range(idx, min(n, idx + len(mt))):
                mask[j] = 1
            start = idx + 1
    covered = sum(mask)
    return covered / max(1, n)


def evaluate_on_texts(
    texts: list[str],
    *,
    dict_a_path: Path,
    dict_b_paths: list[Path],
    anchors_path: Path,
    repo_path: Path | None = None,
    mode: str = "clinical_speech",
) -> dict[str, Any]:
    repo = repo_path or repo_root()
    da = [dict_a_path]
    per_text: list[dict[str, Any]] = []
    agg_cw: dict[str, float] = {}
    agg_fam: dict[str, float] = {}
    total_accepted = 0
    total_rejected = 0
    unmapped_ratios: list[float] = []

    for t in texts:
        out = run_dlcr_pipeline(
            t,
            repo_root=repo,
            dict_a_paths=da,
            dict_b_paths=dict_b_paths,
            anchors_path=anchors_path,
            mode=mode,
        )
        cw = out.get("concept_weights") or {}
        for k, v in cw.items():
            agg_cw[k] = agg_cw.get(k, 0.0) + float(v)
        fam = out.get("family_activation") or {}
        for k, v in fam.items():
            agg_fam[k] = agg_fam.get(k, 0.0) + float(v)
        total_accepted += int(out.get("lexical_hits_accepted") or 0)
        total_rejected += int(out.get("lexical_hits_rejected") or 0)
        canon = str(out.get("canonical_text") or "")
        spans = list(out.get("span_resolutions") or [])
        cov = _coverage(canon, spans)
        unmapped_ratios.append(1.0 - cov)

        per_text.append(
            {
                "lexical_hits_accepted": out.get("lexical_hits_accepted"),
                "lexical_hits_rejected": out.get("lexical_hits_rejected"),
                "concept_weights": out.get("concept_weights"),
                "family_activation": out.get("family_activation"),
                "hex_concentration": out.get("hex_concentration"),
                "degradation_flags": out.get("degradation_flags"),
                "unmapped_lexical_ratio_est": round(1.0 - cov, 4),
            }
        )

    noise_denom = max(1, total_accepted + total_rejected)
    eval_out = {
        "run": "dict_calibration_eval_v1",
        "n_texts": len(texts),
        "per_text": per_text,
        "aggregate": {
            "concept_activation": {k: round(v, 6) for k, v in sorted(agg_cw.items())},
            "concept_entropy": round(_shannon_entropy(agg_cw), 6),
            "family_activation": {k: round(v, 6) for k, v in sorted(agg_fam.items())},
            "family_balance_gini_stub": round(
                1.0 - sum(1 for _ in agg_fam) / max(1, len(agg_fam)), 6
            ),
            "noise_ratio": round(total_rejected / noise_denom, 6),
            "unmapped_lexical_pct_mean": round(
                100.0 * (sum(unmapped_ratios) / max(1, len(unmapped_ratios))), 4
            ),
        },
    }
    return eval_out
