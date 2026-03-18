#!/usr/bin/env python3

# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
E2E: single session run — runtime sphere stack + Hesperia engine (KME, TRIZ, clinical session).

Writes planned outputs under assets/artifacts/e2e/. Order is documented in docs/E2E_RUN_ORDER.md.
No calibration of results; existence of output only (large payloads truncated where noted).
Usage: python3 -m runtime.pipeline.run_e2e_all [--out-dir path]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

_HERE = Path(__file__).resolve().parent
_HESPERIA = _HERE.parents[1]
if str(_HESPERIA) not in sys.path:
    sys.path.insert(0, str(_HESPERIA))

# Canonical e2e artifact directory
DEFAULT_E2E_DIR = _HESPERIA / "assets" / "artifacts" / "e2e"

# Planned output basenames (all under out_dir)
# Order matches run_all() — see docs/E2E_RUN_ORDER.md
E2E_OUTPUTS = (
    "run_output_e2e_sentence.json",
    "run_output_e2e_l1_l9.json",
    "run_output_e2e_r1_r4.json",
    "run_output_e2e_sphere_math_values.json",
    "run_output_e2e_sphere_math_100.json",
    "run_output_e2e_domain_metrics.json",
    "run_output_e2e_session_kme.json",
    "run_output_e2e_triz_complete.json",
    "run_output_e2e_session_topology.json",
)


def _round_floats(obj, ndigits=6):
    if isinstance(obj, float):
        return round(obj, ndigits)
    if isinstance(obj, dict):
        return {k: _round_floats(v, ndigits) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_round_floats(x, ndigits) for x in obj]
    return obj


def run_e2e_sentence(out_path: Path, text: str) -> None:
    """Run analyze (6-key + attribution + dict_b + R1–R4); write JSON."""
    from runtime.pipeline.analyze import analyze

    minimal, extended = analyze(
        text,
        r1_r4=True,
        r1_r4_book_id="e2e",
        r1_r4_levels=["R1", "R2", "R3", "R4"],
    )
    out = {
        "input": {"text_preview": text[:200] + ("..." if len(text) > 200 else ""), "length": len(text)},
        "result": minimal,
        "extended": dict(extended),
    }
    if isinstance(out["extended"].get("family_vector"), list):
        out["extended"]["family_vector"] = {"length": len(out["extended"]["family_vector"]), "_truncated": True}
    if isinstance(out["extended"].get("family_vector_pre_sharpen"), list):
        out["extended"]["family_vector_pre_sharpen"] = {
            "length": len(out["extended"]["family_vector_pre_sharpen"]),
            "_truncated": True,
        }
    out = _round_floats(out)
    from core.projection import apply_public_projection
    out = apply_public_projection(out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")


def run_e2e_l1_l9(out_path: Path, text: str) -> None:
    """Run L1–L9 pipeline; write JSON."""
    from runtime.pipeline.run_l1_through_l9 import run_pipeline_for_text

    assets = _HESPERIA / "lexicon" / "curated"
    out = run_pipeline_for_text(text, assets_root=assets)
    from core.projection import apply_public_projection
    out = apply_public_projection(out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")


def run_e2e_r1_r4(out_path: Path, text: str) -> None:
    """Run R1–R4 pipeline; write single JSON with units + book_profile."""
    from runtime.pipeline.r1_r4_pipeline import run_full_pipeline_to_json

    result = run_full_pipeline_to_json(text, book_id="e2e", levels=["R1", "R2", "R3", "R4"])
    from core.projection import apply_public_projection
    result = apply_public_projection(result)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(result, indent=2), encoding="utf-8")


def run_e2e_sphere_math_values(out_path: Path, text: str) -> None:
    """Run sphere math values flow; write JSON (via main with patched argv)."""
    from runtime.pipeline import run_sphere_math_values

    old_argv = list(sys.argv)
    try:
        sys.argv = ["", "--out", str(out_path), "--text", text]
        run_sphere_math_values.main()
    finally:
        sys.argv = old_argv


def run_e2e_domain_metrics(out_path: Path, text: str) -> None:
    """Run structural analysis with domain metrics; write domain_metrics to JSON via service."""
    from runtime.services.analysis_service import run_structural_analysis
    from runtime.artifact_writer import write_public_json

    assets = _HESPERIA / "lexicon" / "curated"
    domain_constants_path = _HESPERIA / "assets" / "data" / "domain_constants.json"
    result = run_structural_analysis(
        text,
        assets_root=assets,
        stages="full",
        enable_domain_metrics=True,
        domain_constants_path=domain_constants_path if domain_constants_path.exists() else None,
    )
    out_data = result.get("domain_metrics")
    if not out_data:
        out_data = {"_error": "domain_metrics not in result", "sourceId": "e2e_domain_metrics"}
    write_public_json(out_path, out_data)


def run_e2e_sphere_math_100(out_path: Path, limit: int = 3) -> None:
    """Run sphere math on first N calibration sentences; write JSON."""
    from runtime.pipeline import run_sphere_math_100_sentences

    sentences_path = _HESPERIA / "tools" / "calibration" / "data" / "calibration_100_sentences.json"
    if not sentences_path.exists():
        import tempfile
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump([
                {"id": 1, "domain": "e2e", "text": "Justice and fairness support order."},
                {"id": 2, "domain": "e2e", "text": "Harm and conflict reduce trust."},
            ], f, indent=2)
            tmp_path = f.name
        use_path = tmp_path
        try:
            old_argv = list(sys.argv)
            sys.argv = ["", "--out", str(out_path), "--sentences", use_path, "--limit", str(limit)]
            run_sphere_math_100_sentences.main()
        finally:
            sys.argv = old_argv
            Path(tmp_path).unlink(missing_ok=True)
        return
    old_argv = list(sys.argv)
    try:
        sys.argv = ["", "--out", str(out_path), "--sentences", str(sentences_path), "--limit", str(limit)]
        run_sphere_math_100_sentences.main()
    finally:
        sys.argv = old_argv


def _text_preview(text: str, n: int = 200) -> dict[str, Any]:
    return {"text_preview": text[:n] + ("..." if len(text) > n else ""), "length": len(text)}


def _activation_topology_maps(
    activation: dict[str, Any], node_ids: set[str]
) -> dict[str, Any] | None:
    """Same binding as clinical KME TRIZ: concept_to_area + concept_to_family for active nodes."""
    c2a = activation.get("concept_to_area") or {}
    c2f = activation.get("concept_to_family") or {}

    def _ival(x: Any) -> int | None:
        try:
            return int(x)
        except (TypeError, ValueError):
            try:
                return int(float(x))
            except (TypeError, ValueError):
                return None

    ca = {str(k): v for k, v in c2a.items() if str(k) in node_ids and _ival(v) is not None}
    cf = {str(k): v for k, v in c2f.items() if str(k) in node_ids and _ival(v) is not None}
    ca = {k: _ival(v) for k, v in ca.items()}
    cf = {k: _ival(v) for k, v in cf.items()}
    if not ca and not cf:
        return None
    topo: dict[str, Any] = {}
    if ca:
        topo["concept_to_area"] = dict(sorted(ca.items()))
    if cf:
        topo["concept_to_family"] = dict(sorted(cf.items()))
    return topo or None


def _slim_csv_exports(obj: dict[str, Any]) -> None:
    ce = obj.get("csv_exports")
    if isinstance(ce, dict):
        obj["csv_exports"] = {
            k: {"byte_length": len(v) if isinstance(v, str) else 0} for k, v in sorted(ce.items())
        }


def run_e2e_session_kme(out_path: Path, text: str) -> None:
    """NLP session → clinical ActiveGraph → KME primitives/derived/fingerprint + TRIZ."""
    from hesperia.engine.kme.clinical_bridge import run_session_kme_pipeline
    from hesperia.engine.kme.pipeline import metric_report_to_dict

    try:
        report = run_session_kme_pipeline(text, source_id="e2e_session")
        body = {"report": metric_report_to_dict(report)}
    except Exception as e:
        body = {"_error": str(e), "sourceId": "e2e_session"}
    out = {"input": _text_preview(text), **body}
    out = _round_floats(out)
    from core.projection import apply_public_projection

    out = apply_public_projection(out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")


def run_e2e_triz_complete(out_path: Path, text: str) -> None:
    """Session activation → ActiveGraph → run_triz_analysis_complete (API /analysis/triz parity)."""
    from hesperia.engine.kme.clinical_bridge import build_clinical_active_graph
    from hesperia.engine.triz.pipeline import active_graph_from_payload, run_triz_analysis_complete
    from hesperia.nlp.session_parser import analyze_session

    try:
        try:
            from sphere.topology.family_embedding import load_family_embedding_tfp

            embedding = load_family_embedding_tfp()
        except Exception:
            embedding = {}
        activation = analyze_session(text, embedding=embedding)
        ag = build_clinical_active_graph(activation)
        payload = {
            "nodes": {cid: {"hitCount": n.hit_count} for cid, n in sorted(ag.nodes.items())},
            "edges": [
                {
                    "source": e.source_concept_id,
                    "target": e.target_concept_id,
                    "type": e.relation_type or "",
                }
                for e in sorted(
                    ag.edges,
                    key=lambda x: (x.source_concept_id, x.target_concept_id, x.relation_type or ""),
                )
            ],
        }
        topo = _activation_topology_maps(activation, set(ag.nodes.keys()))
        ag2 = active_graph_from_payload(payload)
        content = run_triz_analysis_complete(
            ag2,
            topo,
            narrative_id="e2e_narrative",
            run_id=None,
            topology_mode=True,
        )
        _slim_csv_exports(content)
        body = {"triz_complete": content}
    except Exception as e:
        body = {"_error": str(e)}
    out = {"input": _text_preview(text), **body}
    out = _round_floats(out)
    from core.projection import apply_public_projection

    out = apply_public_projection(out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")


def run_e2e_session_topology(out_path: Path, text: str) -> None:
    """Clinical session topology: segmented activation, transitions, aggression curve, defenses."""
    from hesperia.clinical.session_topology import run_session_topology

    max_segments = 12
    try:
        full = run_session_topology(text, window_size=80)
        segs = full.get("segments") or []
        if len(segs) > max_segments:
            full = {
                **full,
                "segments": segs[:max_segments],
                "_segments_truncated": True,
                "_segments_total": len(segs),
            }
        body = {"session_topology": full}
    except Exception as e:
        body = {"_error": str(e)}
    out = _round_floats({"input": _text_preview(text), **body})
    # Not apply_public_projection: clinical topology keys are not on the public allowlist.
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")


def run_all(out_dir: Path | None = None, text: str | None = None) -> dict[str, Path]:
    """Run all e2e flows; write to out_dir. Returns map output_basename -> path written."""
    out_dir = out_dir or DEFAULT_E2E_DIR
    out_dir = Path(out_dir)
    text = (text or "Justice and fairness support social order. Harm and conflict reduce trust.").strip()

    written: dict[str, Path] = {}

    # 1. Analyze sentence
    p = out_dir / "run_output_e2e_sentence.json"
    run_e2e_sentence(p, text)
    written["run_output_e2e_sentence.json"] = p

    # 2. L1–L9
    p = out_dir / "run_output_e2e_l1_l9.json"
    run_e2e_l1_l9(p, text)
    written["run_output_e2e_l1_l9.json"] = p

    # 3. R1–R4
    p = out_dir / "run_output_e2e_r1_r4.json"
    run_e2e_r1_r4(p, text)
    written["run_output_e2e_r1_r4.json"] = p

    # 4. Sphere math values
    p = out_dir / "run_output_e2e_sphere_math_values.json"
    run_e2e_sphere_math_values(p, text)
    written["run_output_e2e_sphere_math_values.json"] = p

    # 5. Sphere math 100 (limit 3)
    p = out_dir / "run_output_e2e_sphere_math_100.json"
    run_e2e_sphere_math_100(p, limit=3)
    written["run_output_e2e_sphere_math_100.json"] = p

    # 6. Domain metrics (41 signals, fingerprint, hash) — structural pipeline + KME bridge
    p = out_dir / "run_output_e2e_domain_metrics.json"
    run_e2e_domain_metrics(p, text)
    written["run_output_e2e_domain_metrics.json"] = p

    # 7. Session → KME + TRIZ (hesperia.engine.kme clinical path)
    p = out_dir / "run_output_e2e_session_kme.json"
    run_e2e_session_kme(p, text)
    written["run_output_e2e_session_kme.json"] = p

    # 8. TRIZ complete report (same session graph; API parity)
    p = out_dir / "run_output_e2e_triz_complete.json"
    run_e2e_triz_complete(p, text)
    written["run_output_e2e_triz_complete.json"] = p

    # 9. Clinical session topology (segmented windows)
    p = out_dir / "run_output_e2e_session_topology.json"
    run_e2e_session_topology(p, text)
    written["run_output_e2e_session_topology.json"] = p

    return written


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Run all e2e flows; write multiple outputs to assets/artifacts/e2e/.")
    ap.add_argument("--out-dir", type=Path, default=DEFAULT_E2E_DIR, help="Output directory for e2e artifacts")
    ap.add_argument("--text", default=None, help="Input text for sentence/L1–L9/R1–R4 flows")
    args = ap.parse_args()

    try:
        written = run_all(out_dir=args.out_dir, text=args.text)
    except Exception as e:
        print(f"E2E run failed: {e}", file=sys.stderr)
        return 1

    for name, path in written.items():
        print(path.resolve(), file=sys.stderr)
    print("e2e_run_ok", len(written), "outputs", file=sys.stderr)
    print("Order: docs/E2E_RUN_ORDER.md | outputs: assets/artifacts/e2e/E2E_OUTPUTS.md", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
