#!/usr/bin/env python3
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
"""
Resumable dict calibration clearance (corpus → extract → normalize → propose → anchor → links → eval → errors).

Uses checkpoints under WORKDIR/.clearance/ so normalize/propose can stop and resume (OpenAI batches).

Examples:
  PYTHONPATH=. python3 tools/run_dict_calibration_clearance.py status --workdir outputs/dict_calibration/clr1
  PYTHONPATH=. python3 tools/run_dict_calibration_clearance.py extract --corpus hesperia/modules/tfp/data/tfp_v1/corpus/original/ru --workdir outputs/dict_calibration/clr1
  PYTHONPATH=. python3 tools/run_dict_calibration_clearance.py normalize --workdir outputs/dict_calibration/clr1
  PYTHONPATH=. python3 tools/run_dict_calibration_clearance.py propose --workdir outputs/dict_calibration/clr1
  PYTHONPATH=. python3 tools/run_dict_calibration_clearance.py post --workdir outputs/dict_calibration/clr1 --corpus hesperia/modules/tfp/data/tfp_v1/corpus/original/ru
  PYTHONPATH=. python3 tools/run_dict_calibration_clearance.py run --corpus hesperia/modules/tfp/data/tfp_v1/corpus/original/ru --workdir outputs/dict_calibration/clr1

Dry / partial:
  python3 ... normalize --workdir /tmp/x --max-rows 72 --dry-run
  python3 ... propose --workdir /tmp/x --max-phrases 80 --dry-run

Reset checkpoints:
  python3 ... reset-normalize --workdir DIR
  python3 ... reset-propose --workdir DIR
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))


def _maybe_load_env() -> None:
    if os.environ.get("OPENAI_API_KEY"):
        return
    for name in (".env.openai", ".env"):
        p = _ROOT / name
        if not p.is_file():
            continue
        for raw in p.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("export "):
                line = line[7:].strip()
            if "=" not in line:
                continue
            k, v = line.split("=", 1)
            k, v = k.strip(), v.strip().strip('"').strip("'")
            if k and k not in os.environ:
                os.environ[k] = v
        break


def main() -> int:
    _maybe_load_env()
    from tools.dict_calibration.env_defaults import apply_dict_calib_offline_bundle, dict_calib_worker_default

    apply_dict_calib_offline_bundle()
    dw = dict_calib_worker_default()
    ap = argparse.ArgumentParser(description="Resumable dict calibration clearance (A–D + checkpoints)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_ext = sub.add_parser("extract", help="Phase A: corpus → dict_a_candidates.jsonl")
    p_ext.add_argument("--corpus", type=Path, required=True)
    p_ext.add_argument("--workdir", type=Path, required=True)
    p_ext.add_argument("--min-freq", type=int, default=2)
    p_ext.set_defaults(_fn="extract")

    def add_norm_propose(p):
        p.add_argument("--workdir", type=Path, required=True)
        p.add_argument("--dry-run", action="store_true")
        p.add_argument("--log-every", type=int, default=25, help="Progress log every N API chunks (0=quiet)")
        p.add_argument("--max-rows", type=int, default=None, help="normalize: cap filtered rows (testing)")
        p.add_argument("--max-phrases", type=int, default=None, help="propose: cap phrase count (testing)")

    p_no = sub.add_parser("normalize", help="Phase B1: resumable LLM normalize → dict_a_normalized.jsonl")
    add_norm_propose(p_no)
    p_no.add_argument("--batch-size", type=int, default=24)
    p_no.set_defaults(_fn="normalize")

    p_pr = sub.add_parser("propose", help="Phase B2: resumable LLM propose → dict_b_draft.jsonl")
    add_norm_propose(p_pr)
    p_pr.add_argument("--batch-size", type=int, default=40)
    p_pr.add_argument("--max-concepts", type=int, default=80)
    p_pr.add_argument("--catalog-limit", type=int, default=400)
    p_pr.set_defaults(_fn="propose")

    p_po = sub.add_parser("post", help="Phase C+D: anchor, links, eval, errors (local)")
    p_po.add_argument("--workdir", type=Path, required=True)
    p_po.add_argument("--corpus", type=Path, required=True)
    p_po.add_argument("--min-score", type=float, default=0.52)
    p_po.add_argument(
        "--anchor-workers",
        type=int,
        default=dw,
        help="Parallel anchoring (default: $HESPERIA_DICT_CALIB_WORKERS or 4)",
    )
    p_po.add_argument(
        "--link-workers",
        type=int,
        default=dw,
        help="Parallel workers for linking (default: $HESPERIA_DICT_CALIB_WORKERS or 4)",
    )
    p_po.add_argument(
        "--link-fuzzy-mode",
        choices=["auto", "off", "full", "partial"],
        default="auto",
        help="links fuzzy policy",
    )
    p_po.add_argument("--partial-fuzzy-top-misses", type=int, default=0)
    p_po.add_argument("--fuzzy-top-k", type=int, default=3)
    p_po.add_argument("--fuzzy-candidate-cap", type=int, default=2048)
    p_po.add_argument(
        "--eval-workers",
        type=int,
        default=dw,
        help="Parallel workers for eval texts (default: $HESPERIA_DICT_CALIB_WORKERS or 4)",
    )
    p_po.add_argument(
        "--error-workers",
        type=int,
        default=dw,
        help="Parallel workers for errors extract (default: $HESPERIA_DICT_CALIB_WORKERS or 4)",
    )
    p_po.add_argument("--eval-max-files", type=int, default=0, help="<=0 = whole corpus tree")
    p_po.add_argument("--eval-max-chars", type=int, default=0, help="<=0 = full file text")
    p_po.set_defaults(_fn="post")

    p_run = sub.add_parser("run", help="extract (if needed) + normalize + propose + post")
    p_run.add_argument("--corpus", type=Path, required=True)
    p_run.add_argument("--workdir", type=Path, required=True)
    p_run.add_argument("--min-freq", type=int, default=2)
    p_run.add_argument("--dry-run", action="store_true")
    p_run.add_argument("--log-every", type=int, default=25)
    p_run.add_argument("--normalize-batch-size", type=int, default=24)
    p_run.add_argument("--propose-batch-size", type=int, default=40)
    p_run.add_argument("--max-concepts", type=int, default=80)
    p_run.add_argument("--catalog-limit", type=int, default=400)
    p_run.add_argument("--max-rows", type=int, default=None)
    p_run.add_argument("--max-phrases", type=int, default=None)
    p_run.add_argument("--eval-max-files", type=int, default=0)
    p_run.add_argument("--eval-max-chars", type=int, default=0)
    p_run.add_argument("--anchor-workers", type=int, default=dw)
    p_run.add_argument("--link-workers", type=int, default=dw)
    p_run.add_argument("--link-fuzzy-mode", choices=["auto", "off", "full", "partial"], default="auto")
    p_run.add_argument("--partial-fuzzy-top-misses", type=int, default=0)
    p_run.add_argument("--fuzzy-top-k", type=int, default=3)
    p_run.add_argument("--fuzzy-candidate-cap", type=int, default=2048)
    p_run.add_argument("--eval-workers", type=int, default=dw)
    p_run.add_argument("--error-workers", type=int, default=dw)
    p_run.set_defaults(_fn="run")

    p_st = sub.add_parser("status", help="Checkpoint + artifact summary")
    p_st.add_argument("--workdir", type=Path, required=True)
    p_st.add_argument("--json", action="store_true", help="Print JSON only (no stderr summary)")
    p_st.set_defaults(_fn="status")

    p_rn = sub.add_parser("reset-normalize", help="Remove normalize outputs + checkpoint (keep candidates)")
    p_rn.add_argument("--workdir", type=Path, required=True)
    p_rn.set_defaults(_fn="reset_norm")

    p_rp = sub.add_parser("reset-propose", help="Remove propose outputs + checkpoint (keep normalized)")
    p_rp.add_argument("--workdir", type=Path, required=True)
    p_rp.set_defaults(_fn="reset_prop")

    args = ap.parse_args()
    fn = args._fn

    if getattr(args, "corpus", None):
        from tools.dict_calibration.env_defaults import assert_corpus_not_legacy_research

        assert_corpus_not_legacy_research(args.corpus)

    from tools.dict_calibration import clearance_resume as cr

    def log_fn(msg: str) -> None:
        print(msg, file=sys.stderr)

    if fn == "extract":
        info = cr.run_extract(corpus=args.corpus, workdir=args.workdir, min_freq=args.min_freq)
        print(json.dumps(info, indent=2))
        return 0

    if fn == "normalize":
        cr.run_normalize_resume(
            args.workdir,
            batch_size=args.batch_size,
            dry_run=args.dry_run,
            max_rows=args.max_rows,
            log_every=args.log_every,
            log=log_fn,
        )
        return 0

    if fn == "propose":
        cr.run_propose_resume(
            args.workdir,
            dict_b_paths=None,
            max_concepts=args.max_concepts,
            batch_size=args.batch_size,
            catalog_limit=args.catalog_limit,
            dry_run=args.dry_run,
            max_phrases=args.max_phrases,
            log_every=args.log_every,
            log=log_fn,
        )
        return 0

    if fn == "post":
        cr.run_post(
            args.workdir,
            corpus=args.corpus,
            min_score=args.min_score,
            dict_b_paths=None,
            eval_max_files=args.eval_max_files,
            eval_max_chars=args.eval_max_chars,
            anchor_workers=getattr(args, "anchor_workers", dict_calib_worker_default()),
            link_workers=getattr(args, "link_workers", dict_calib_worker_default()),
            eval_workers=getattr(args, "eval_workers", dict_calib_worker_default()),
            error_workers=getattr(args, "error_workers", dict_calib_worker_default()),
            link_fuzzy_mode=getattr(args, "link_fuzzy_mode", "auto"),
            partial_fuzzy_top_misses=getattr(args, "partial_fuzzy_top_misses", 0),
            fuzzy_top_k=getattr(args, "fuzzy_top_k", 3),
            fuzzy_candidate_cap=getattr(args, "fuzzy_candidate_cap", 2048),
        )
        print("OK post (anchor, links, eval, errors)", file=sys.stderr)
        return 0

    if fn == "run":
        wd = args.workdir
        cand = wd / "dict_a_candidates.jsonl"
        if not cand.is_file():
            info = cr.run_extract(corpus=args.corpus, workdir=wd, min_freq=args.min_freq)
            print(json.dumps({"extract": info}, indent=2), file=sys.stderr)
        cr.run_normalize_resume(
            wd,
            batch_size=args.normalize_batch_size,
            dry_run=args.dry_run,
            max_rows=args.max_rows,
            log_every=args.log_every,
            log=log_fn,
        )
        cr.run_propose_resume(
            wd,
            dict_b_paths=None,
            max_concepts=args.max_concepts,
            batch_size=args.propose_batch_size,
            catalog_limit=args.catalog_limit,
            dry_run=args.dry_run,
            max_phrases=args.max_phrases,
            log_every=args.log_every,
            log=log_fn,
        )
        cr.run_post(
            wd,
            corpus=args.corpus,
            min_score=0.52,
            dict_b_paths=None,
            eval_max_files=args.eval_max_files,
            eval_max_chars=args.eval_max_chars,
            anchor_workers=getattr(args, "anchor_workers", dict_calib_worker_default()),
            link_workers=getattr(args, "link_workers", dict_calib_worker_default()),
            eval_workers=getattr(args, "eval_workers", dict_calib_worker_default()),
            error_workers=getattr(args, "error_workers", dict_calib_worker_default()),
            link_fuzzy_mode=getattr(args, "link_fuzzy_mode", "auto"),
            partial_fuzzy_top_misses=getattr(args, "partial_fuzzy_top_misses", 0),
            fuzzy_top_k=getattr(args, "fuzzy_top_k", 3),
            fuzzy_candidate_cap=getattr(args, "fuzzy_candidate_cap", 2048),
        )
        print("OK run complete", file=sys.stderr)
        st = cr.clearance_status(wd)
        print(json.dumps(st, indent=2))
        return 0

    if fn == "status":
        st = cr.clearance_status(args.workdir)
        print(json.dumps(st, indent=2))
        if args.json:
            return 0
        print("—", file=sys.stderr)
        n = st.get("normalize") or {}
        p = st.get("propose") or {}
        if isinstance(n, dict) and "filtered_total" in n:
            print(
                f"normalize: {n.get('next_row_index')}/{n.get('filtered_total')} "
                f"({n.get('progress_pct')}%) api_chunks≈{n.get('api_chunks_done_approx')}/"
                f"{n.get('api_chunks_total_approx')} complete={n.get('complete')}",
                file=sys.stderr,
            )
        if isinstance(p, dict) and "phrase_total" in p:
            print(
                f"propose:   {p.get('next_phrase_index')}/{p.get('phrase_total')} "
                f"({p.get('progress_pct')}%) api_chunks≈{p.get('api_chunks_done_approx')}/"
                f"{p.get('api_chunks_total_approx')} complete={p.get('complete')}",
                file=sys.stderr,
            )
        print("artifacts:", st.get("files"), file=sys.stderr)
        return 0

    if fn == "reset_norm":
        cr.reset_normalize(args.workdir)
        print("OK reset-normalize", file=sys.stderr)
        return 0

    if fn == "reset_prop":
        cr.reset_propose(args.workdir)
        print("OK reset-propose", file=sys.stderr)
        return 0

    raise SystemExit(2)


if __name__ == "__main__":
    raise SystemExit(main())
