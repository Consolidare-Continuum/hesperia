#!/usr/bin/env python3
# HESPERIA — RAD. Gena: file-in → multi-artifact TFP + main engine paths (testing / research).
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
"""
Run TFP-oriented pipelines on one or more session texts from a file.

**Input**
  - ``.json`` — ``{"sessions": [{"session_id": "...", "text": "..."}, ...]}`` (same shape as Kernberg smoke).
  - Any other extension — whole file is one session (``session_id`` = stem of filename).

**Outputs** (under ``--out-dir``)
  - ``00_manifest.json`` — scope, flags, session ids, artifact list, **tfp_signal_calibration** (topology + Dict-A knobs), **operational_envelope** (Task 7).
  - ``01_structural_batch.json`` — frozen lexicon structural batch (plane A); per-row + file envelope.
  - ``02_session_tfp_stages.json`` — ``analyze_session`` + ``detect_tfp_stage`` per session (plane B).
  - ``03_hex_microstructure_tfp.json`` — hex microstructure + TFP provenance per session.
  - ``04_dlcr_full.json`` — full ``run_dlcr_pipeline`` payload per session.
  - ``05_sealed_multiscale.json`` — ``run_sealed_multiscale_stack`` per session.
  - ``06_product_analyze.json`` — ``runtime.pipeline.analyze.analyze`` minimal + extended per session.
  - Optional: ``07_session_kme.json``, ``08_triz_complete.json``, ``09_session_topology.json`` (flags).
  - With ``--with-topology``: flat ``12_<session_id>_<artifact>.json`` in ``--out-dir`` (coactivation, contradictions,
    metrics, sparse family weights, ``cross_plane_audit.json``; no subfolders) unless ``--skip-triz-activation``.
    Pipeline exits **3** on ``TRIZ_DEAD_LAYER`` / topology+activation write failure.
  - Post-run: ``python3 tools/tfp_calibration_audit.py`` → ``10_calibration_audit.json``; ``tools/calibration_release_gate.py`` → ``11_calibration_release_gate.json``.

Usage::

  python3 -m runtime.pipeline.run_tfp_file_pipeline --input path/to/note.md --out-dir outputs/my_tfp_run

**Gena all-in-one** (same pipeline + audit + schema validation + release gate): ``python3 tools/gena_tfp_bundle_run.py -i path/to/note.md``.

Forces ``HESPERIA_DLCR_DOMAIN_PACK=tfp`` unless ``--no-dlcr-domain-pack``. Optional: ``HESPERIA_ANALYZE_DLCR_EVIDENCE=1`` for DLCR evidence inside ``analyze()``.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import uuid
from pathlib import Path
from typing import Any

_REPO = Path(__file__).resolve().parents[2]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))


def _round_floats(obj: Any, ndigits: int = 6) -> Any:
    if isinstance(obj, float):
        return round(obj, ndigits)
    if isinstance(obj, dict):
        return {k: _round_floats(v, ndigits) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_round_floats(x, ndigits) for x in obj]
    return obj


def _text_preview(text: str, n: int = 200) -> dict[str, Any]:
    return {"text_preview": text[:n] + ("..." if len(text) > n else ""), "length": len(text)}


def _write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(_round_floats(data), indent=2, ensure_ascii=False), encoding="utf-8")


def _stable_contradiction_sort_key(row: dict[str, Any], idx: int) -> tuple[str, str, float, int]:
    pair = row.get("pair")
    concept_a = None
    concept_b = None
    if isinstance(pair, (list, tuple)) and len(pair) >= 2:
        concept_a = pair[0]
        concept_b = pair[1]
    else:
        concept_a = row.get("concept_a")
        concept_b = row.get("concept_b")
    a = "" if concept_a is None else str(concept_a)
    b = "" if concept_b is None else str(concept_b)
    left, right = (a, b) if a <= b else (b, a)
    score_raw = row.get("raw_contradiction_score", row.get("score", 0.0))
    try:
        score = float(score_raw)
    except (TypeError, ValueError):
        score = 0.0
    return (left, right, -score, idx)


def _normalize_contradictions(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    ordered = list(enumerate(rows))
    ordered.sort(key=lambda item: _stable_contradiction_sort_key(item[1], item[0]))
    return [dict(row) for _, row in ordered]


def _extract_contradictions_from_08(path_08: Path, session_id: str) -> list[dict[str, Any]]:
    if not path_08.is_file():
        return []
    try:
        data = json.loads(path_08.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    sessions = data.get("sessions") if isinstance(data, dict) else None
    if not isinstance(sessions, list):
        return []
    for row in sessions:
        if not isinstance(row, dict):
            continue
        if str(row.get("session_id") or "") != session_id:
            continue
        tc = row.get("triz_complete")
        if isinstance(tc, dict):
            nested = tc.get("triz_complete")
            if isinstance(nested, dict) and isinstance(nested.get("contradictions"), list):
                return _normalize_contradictions([x for x in nested["contradictions"] if isinstance(x, dict)])
            if isinstance(tc.get("contradictions"), list):
                return _normalize_contradictions([x for x in tc["contradictions"] if isinstance(x, dict)])
    return []


def _extract_contradictions_from_12(bundle_dir: Path, session_id: str) -> list[dict[str, Any]]:
    pattern = f"12_{session_id}_*contradictions*.json"
    files = sorted(bundle_dir.glob(pattern), key=lambda p: p.name)
    for file_path in files:
        try:
            data = json.loads(file_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(data, dict) and isinstance(data.get("contradictions"), list):
            rows = [x for x in data["contradictions"] if isinstance(x, dict)]
            return _normalize_contradictions(rows)
        if isinstance(data, list):
            rows = [x for x in data if isinstance(x, dict)]
            return _normalize_contradictions(rows)
    return []


def _load_contradictions(bundle_dir: Path, session_id: str) -> tuple[list[dict[str, Any]], str]:
    rows_08 = _extract_contradictions_from_08(bundle_dir / "08_triz_complete.json", session_id)
    if rows_08:
        return rows_08, "08_triz_complete.json"
    rows_12 = _extract_contradictions_from_12(bundle_dir, session_id)
    if rows_12:
        return rows_12, "12_*_contradictions*.json"
    return [], "none"


def _build_activation_with_bundle_contradictions(
    *,
    session_id: str,
    text: str,
    bundle_dir: Path,
    embedding: dict[str, Any] | None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    from hesperia.nlp.session_parser import analyze_session

    contradictions, source = _load_contradictions(bundle_dir, session_id)
    activation = analyze_session(
        text,
        embedding=embedding or None,
        contradictions=contradictions if contradictions else None,
    )
    used = int((activation.get("contradiction_count_used") or 0))
    coupling_active = bool(activation.get("contradiction_coupling_active"))
    row = {
        "session_id": session_id,
        "contradiction_pipeline": {
            "source": source,
            "count": len(contradictions),
            "used_in_activation": bool(coupling_active and used > 0),
        },
        "activation": activation,
    }
    trace = {
        "session_id": session_id,
        "source": source,
        "count": len(contradictions),
        "used_in_activation": bool(coupling_active and used > 0),
        "contradiction_count_used": used,
    }
    return row, trace


def load_sessions(path: Path) -> list[tuple[str, str]]:
    suf = path.suffix.lower()
    if suf == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        sessions = data.get("sessions")
        if not isinstance(sessions, list):
            raise ValueError("JSON must be an object with key 'sessions': [...]")
        out: list[tuple[str, str]] = []
        for i, s in enumerate(sessions):
            if not isinstance(s, dict):
                continue
            sid = str(s.get("session_id") or f"session_{i}")
            text = str(s.get("text") or "")
            out.append((sid, text))
        return out
    text = path.read_text(encoding="utf-8")
    sid = path.stem or "document"
    return [(sid, text)]


def _maybe_speaker_aware(text: str, embedding: dict[str, Any] | None) -> dict[str, Any] | None:
    from hesperia.nlp.transcript_speaker_labels import transcript_has_both_clinical_speakers

    if not transcript_has_both_clinical_speakers(text):
        return None
    try:
        from research.clinical_tfp.stage_detection import detect_tfp_stage
        from hesperia.nlp.session_parser import analyze_session_speaker_aware

        sa = analyze_session_speaker_aware(text, embedding=embedding or None)
        areas_sa = sa.get("areas") or {}
        return {
            "tfp_stage": detect_tfp_stage({k: float(v) for k, v in areas_sa.items() if v is not None}),
            "areas_top": dict(sorted(areas_sa.items(), key=lambda x: -float(x[1] or 0))[:8]),
            "has_speaker_activation": "speaker_activation" in sa,
            "activation_path_id": ((sa.get("invariant_activation") or {}).get("path_id")),
        }
    except Exception as e:  # noqa: BLE001
        return {"_error": str(e)}


def run_pipeline(
    *,
    sessions: list[tuple[str, str]],
    out_dir: Path,
    with_kme: bool,
    with_triz: bool,
    with_topology: bool,
    with_r1_r4: bool,
    skip_structural: bool,
    skip_stages: bool,
    skip_hex: bool,
    skip_dlcr: bool,
    skip_sealed: bool,
    skip_analyze: bool,
    dlcr_mode: str,
    skip_triz_activation: bool = False,
    topology_run_params: dict[str, Any] | None = None,
) -> dict[str, Any]:
    from hesperia.engine.lexical_concept.pipeline import run_dlcr_pipeline
    from hesperia.engine.hex_outputs.e2e_integration import hex_microstructure_bundle_for_text
    from hesperia.engine.sealed_multiscale_stack import run_sealed_multiscale_stack
    from hesperia.nlp.session_parser import analyze_session
    from research.clinical_tfp.stage_detection import TFP_STAGES, detect_tfp_stage
    from runtime.pipeline.analyze import analyze
    from runtime.services.analysis_service import run_structural_analysis_batch

    from hesperia.engine.output_anomalies import (
        aggregate_file_envelope,
        apply_envelopes_standalone_sealed_analyze,
        apply_session_envelopes,
        default_operational_envelope,
    )
    from hesperia.engine.tfp_signal_calibration import load_tfp_runtime_bundle
    from hesperia.extensions.triz.topology_activation_pipeline import triz_activation_bundle_filename
    from hesperia.ontology.dictA.loader import CONFIDENCE_TYPE_MULTIPLIER
    from research.clinical_tfp.session_topology import (
        AREA_CURVE_MAP,
        CURVE_CALIBRATION_REFERENCE,
        DEFAULT_SESSION_TOPOLOGY_RUN_PARAMS,
        run_session_topology,
    )

    tfp_runtime = load_tfp_runtime_bundle()
    tfp_calibration = dict(tfp_runtime["calibration"])
    tfp_inhibition = dict(tfp_runtime["inhibition_matrix"])
    topo_params: dict[str, Any] = dict(DEFAULT_SESSION_TOPOLOGY_RUN_PARAMS)
    if topology_run_params:
        topo_params.update(topology_run_params)

    assets = _REPO / "lexicon" / "curated"
    texts = [t for _, t in sessions]
    sids = [sid for sid, t in sessions]

    written: dict[str, str] = {}
    errors: list[str] = []
    triz_activation_paths: dict[str, dict[str, str]] = {}
    triz_activation_critical = False

    try:
        from sphere.topology.family_embedding import load_family_embedding_tfp

        embedding = load_family_embedding_tfp()
    except Exception:
        embedding = {}

    # 1 Structural batch (all sessions in one call)
    structural_batch: list[dict[str, Any]] = []
    if not skip_structural:
        try:
            batch = run_structural_analysis_batch(texts, assets_root=assets, attach_version=False)
            for i, row in enumerate(batch):
                sid = sids[i] if i < len(sids) else f"batch_{i}"
                one = dict(row)
                one["session_id"] = sid
                structural_batch.append(one)
        except Exception as e:  # noqa: BLE001
            structural_batch = [{"_error": str(e), "session_id": "_batch"}]
            errors.append(f"structural_batch: {e}")
        p = out_dir / "01_structural_batch.json"
        envs01 = [r.get("operational_envelope") or default_operational_envelope() for r in structural_batch]
        _write_json(
            p,
            {
                "run": "tfp_file_pipeline_structural",
                "session_count": len(sessions),
                "structural_batch": structural_batch,
                "operational_envelope": aggregate_file_envelope(envs01),
            },
        )
        written["01_structural_batch.json"] = str(p)

    # Per-session bundles
    session_tfp_stages: list[dict[str, Any]] = []
    session_hex: list[dict[str, Any]] = []
    session_dlcr: list[dict[str, Any]] = []
    session_sealed: list[dict[str, Any]] = []
    session_analyze: list[dict[str, Any]] = []
    session_speaker_aware: list[dict[str, Any]] = []
    session_kme: list[dict[str, Any]] = []
    session_triz: list[dict[str, Any]] = []
    session_topo: list[dict[str, Any]] = []
    session_main_engine_full_context: list[dict[str, Any]] = []
    contradiction_pipeline_rows: list[dict[str, Any]] = []

    for sid, t in zip(sids, texts):
        t = (t or "").strip()
        if not t:
            continue

        if not skip_stages:
            try:
                act = analyze_session(t, embedding=embedding or None)
                areas = act.get("areas") or {}
                stage = detect_tfp_stage({k: float(v) for k, v in areas.items() if v is not None})
                session_tfp_stages.append(
                    {
                        "session_id": sid,
                        "tfp_stage": stage,
                        "areas_top": dict(sorted(areas.items(), key=lambda x: -float(x[1] or 0))[:8]),
                        "areas_raw": act.get("areas_raw") or {},
                        "areas_inhibited": act.get("areas_inhibited") or {},
                        "areas_final": act.get("areas_final") or areas,
                        "activation_path_id": (act.get("invariant_activation") or {}).get("path_id"),
                        "config_version": (act.get("invariant_activation") or {}).get("config_version"),
                        "hex_feedback_active": (act.get("invariant_activation") or {}).get(
                            "hex_feedback_active"
                        ),
                    }
                )
            except Exception as ex:  # noqa: BLE001
                session_tfp_stages.append({"session_id": sid, "_error": str(ex)})

        saw = _maybe_speaker_aware(t, embedding)
        if saw is not None:
            session_speaker_aware.append({"session_id": sid, **saw})

        if not skip_hex:
            try:
                session_hex.append(
                    {"session_id": sid, **hex_microstructure_bundle_for_text(t, assets, list_cap=56)}
                )
            except Exception as ex:  # noqa: BLE001
                session_hex.append({"session_id": sid, "_error": str(ex)})

        if not skip_dlcr:
            try:
                body = run_dlcr_pipeline(t, repo_root=_REPO, mode=dlcr_mode)
                body = dict(body)
                body["run"] = "tfp_file_pipeline_dlcr"
                body["session_id"] = sid
                body["input"] = _text_preview(t)
                session_dlcr.append(body)
            except Exception as ex:  # noqa: BLE001
                session_dlcr.append({"session_id": sid, "_error": str(ex), "input": _text_preview(t)})

        if not skip_sealed:
            try:
                bundle = run_sealed_multiscale_stack(t, assets, use_triz_contradiction=False)
                session_sealed.append(
                    {"session_id": sid, "run": "tfp_file_pipeline_sealed", **_round_floats(dict(bundle))}
                )
            except Exception as ex:  # noqa: BLE001
                session_sealed.append({"session_id": sid, "_error": str(ex)})

        if not skip_analyze:
            try:
                minimal, extended = analyze(t, r1_r4=with_r1_r4)
                session_analyze.append(
                    {
                        "session_id": sid,
                        "input": _text_preview(t),
                        "result": minimal,
                        "extended": dict(extended),
                    }
                )
            except Exception as ex:  # noqa: BLE001
                session_analyze.append({"session_id": sid, "_error": str(ex), "input": _text_preview(t)})

        if with_kme:
            try:
                from hesperia.engine.kme.clinical_bridge import run_session_kme_pipeline
                from hesperia.engine.kme.pipeline import metric_report_to_dict
                from core.projection import apply_public_projection

                report = run_session_kme_pipeline(t, source_id=sid)
                body = apply_public_projection(
                    {"session_id": sid, "input": _text_preview(t), "report": metric_report_to_dict(report)}
                )
                session_kme.append(_round_floats(body))
            except Exception as ex:  # noqa: BLE001
                session_kme.append({"session_id": sid, "_error": str(ex)})

        if with_triz:
            try:
                from hesperia.engine.kme.clinical_bridge import build_clinical_active_graph
                from hesperia.extensions.triz.pipeline import active_graph_from_payload, run_triz_analysis_complete
                from runtime.pipeline.run_e2e_all import _activation_topology_maps, _slim_csv_exports

                act = analyze_session(t, embedding=embedding or None)
                ag = build_clinical_active_graph(act)
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
                topo = _activation_topology_maps(act, set(ag.nodes.keys()))
                ag2 = active_graph_from_payload(payload)
                content = run_triz_analysis_complete(
                    ag2,
                    topo,
                    narrative_id=sid,
                    run_id=None,
                    topology_mode=True,
                )
                _slim_csv_exports(content)
                from core.projection import apply_public_projection

                session_triz.append(
                    apply_public_projection(
                        _round_floats(
                            {"session_id": sid, "input": _text_preview(t), "triz_complete": content}
                        )
                    )
                )
            except Exception as ex:  # noqa: BLE001
                session_triz.append({"session_id": sid, "_error": str(ex)})

        if with_topology:
            try:
                full = run_session_topology(t, **topo_params)
                segs = full.get("segments") or []
                if len(segs) > 12:
                    full = {
                        **full,
                        "segments": segs[:12],
                        "_segments_truncated": True,
                        "_segments_total": len(segs),
                    }
                session_topo.append({"session_id": sid, "session_topology": full})
            except Exception as ex:  # noqa: BLE001
                session_topo.append({"session_id": sid, "_error": str(ex)})

    if with_topology and not skip_triz_activation:
        from hesperia.extensions.triz.topology_activation_pipeline import (
            run_topology_triz_activation,
            triz_activation_pipeline_fail,
        )

        for topo_row in session_topo:
            sid = str(topo_row.get("session_id") or "")
            if topo_row.get("_error"):
                triz_activation_critical = True
                errors.append(f"triz_activation_blocked_bad_topology:{sid}")
                continue
            st_full = topo_row.get("session_topology") or {}
            tc: dict[str, Any] | None = None
            for tr in session_triz:
                if str(tr.get("session_id")) == sid and tr.get("triz_complete") is not None:
                    tc = tr
                    break
            try:
                bundle = run_topology_triz_activation(st_full, triz_complete=tc)
                rel_files: dict[str, str] = {}
                for fn, data in bundle.items():
                    flat = triz_activation_bundle_filename(sid, fn)
                    p = out_dir / flat
                    _write_json(p, data)
                    rel_files[fn] = str(p)
                triz_activation_paths[sid] = rel_files
                audit = bundle["cross_plane_audit.json"]
                if triz_activation_pipeline_fail(audit):
                    triz_activation_critical = True
                    errors.append(f"TRIZ_DEAD_LAYER:{sid}")
            except Exception as ex:  # noqa: BLE001
                triz_activation_critical = True
                errors.append(f"triz_activation_write:{sid}:{ex}")

    if not skip_structural and structural_batch:
        if session_sealed or session_analyze:
            apply_session_envelopes(
                structural_batch=structural_batch,
                session_sealed=session_sealed,
                session_analyze=session_analyze,
            )
    elif session_sealed or session_analyze:
        apply_envelopes_standalone_sealed_analyze(session_sealed, session_analyze)

    if not skip_stages:
        p = out_dir / "02_session_tfp_stages.json"
        _write_json(
            p,
            {
                "run": "tfp_file_pipeline_stages",
                "tfp_stages_enum": list(TFP_STAGES),
                "session_tfp_stages": session_tfp_stages,
                "session_speaker_aware": session_speaker_aware,
                "operational_envelope": default_operational_envelope(),
            },
        )
        written["02_session_tfp_stages.json"] = str(p)

    if not skip_hex:
        p = out_dir / "03_hex_microstructure_tfp.json"
        for _hx in session_hex:
            _hx.setdefault("operational_envelope", default_operational_envelope())
        _write_json(
            p,
            {
                "run": "tfp_file_pipeline_hex",
                "sessions": session_hex,
                "operational_envelope": default_operational_envelope(),
            },
        )
        written["03_hex_microstructure_tfp.json"] = str(p)

    if not skip_dlcr:
        p = out_dir / "04_dlcr_full.json"
        for _dc in session_dlcr:
            _dc.setdefault("operational_envelope", default_operational_envelope())
        envs04 = [s.get("operational_envelope") or default_operational_envelope() for s in session_dlcr]
        _write_json(
            p,
            {
                "run": "tfp_file_pipeline_dlcr",
                "sessions": session_dlcr,
                "operational_envelope": aggregate_file_envelope(envs04) if envs04 else default_operational_envelope(),
            },
        )
        written["04_dlcr_full.json"] = str(p)

    if not skip_sealed:
        p = out_dir / "05_sealed_multiscale.json"
        envs05 = [s.get("operational_envelope") or default_operational_envelope() for s in session_sealed]
        _write_json(
            p,
            {
                "run": "tfp_file_pipeline_sealed",
                "sessions": session_sealed,
                "operational_envelope": aggregate_file_envelope(envs05) if envs05 else default_operational_envelope(),
            },
        )
        written["05_sealed_multiscale.json"] = str(p)

    if not skip_analyze:
        p = out_dir / "06_product_analyze.json"
        envs06 = [s.get("operational_envelope") or default_operational_envelope() for s in session_analyze]
        _write_json(
            p,
            {
                "run": "tfp_file_pipeline_analyze",
                "with_r1_r4": with_r1_r4,
                "sessions": session_analyze,
                "operational_envelope": aggregate_file_envelope(envs06) if envs06 else default_operational_envelope(),
            },
        )
        written["06_product_analyze.json"] = str(p)

    if with_kme and session_kme:
        p = out_dir / "07_session_kme.json"
        for _km in session_kme:
            _km.setdefault("operational_envelope", default_operational_envelope())
        envs07 = [s.get("operational_envelope") or default_operational_envelope() for s in session_kme]
        _write_json(
            p,
            {
                "run": "tfp_file_pipeline_kme",
                "sessions": session_kme,
                "operational_envelope": aggregate_file_envelope(envs07) if envs07 else default_operational_envelope(),
            },
        )
        written["07_session_kme.json"] = str(p)

    if with_triz and session_triz:
        p = out_dir / "08_triz_complete.json"
        for _tz in session_triz:
            _tz.setdefault("operational_envelope", default_operational_envelope())
        envs08 = [s.get("operational_envelope") or default_operational_envelope() for s in session_triz]
        _write_json(
            p,
            {
                "run": "tfp_file_pipeline_triz",
                "sessions": session_triz,
                "operational_envelope": aggregate_file_envelope(envs08) if envs08 else default_operational_envelope(),
            },
        )
        written["08_triz_complete.json"] = str(p)

    if with_topology and session_topo:
        p = out_dir / "09_session_topology.json"
        for _tp in session_topo:
            _tp.setdefault("operational_envelope", default_operational_envelope())
        envs09 = [s.get("operational_envelope") or default_operational_envelope() for s in session_topo]
        _write_json(
            p,
            {
                "run": "tfp_file_pipeline_topology",
                "topology_run_params": dict(topo_params),
                "tfp_signal_calibration_version": str(tfp_calibration.get("version") or "unknown"),
                "area_curve_map": dict(AREA_CURVE_MAP),
                "curve_calibration_reference": dict(CURVE_CALIBRATION_REFERENCE),
                "dict_a_confidence_multiplier": dict(CONFIDENCE_TYPE_MULTIPLIER),
                "sessions": session_topo,
                "operational_envelope": aggregate_file_envelope(envs09) if envs09 else default_operational_envelope(),
            },
        )
        written["09_session_topology.json"] = str(p)

    # Main-engine activation pass with contradiction injection from bundle artifacts.
    for sid, t in zip(sids, texts):
        t = (t or "").strip()
        if not t:
            continue
        try:
            row, trace = _build_activation_with_bundle_contradictions(
                session_id=sid,
                text=t,
                bundle_dir=out_dir,
                embedding=embedding or None,
            )
            session_main_engine_full_context.append(row)
            contradiction_pipeline_rows.append(trace)
        except Exception as exc:  # noqa: BLE001
            contradictions, source = _load_contradictions(out_dir, sid)
            session_main_engine_full_context.append(
                {
                    "session_id": sid,
                    "contradiction_pipeline": {
                        "source": source,
                        "count": len(contradictions),
                        "used_in_activation": False,
                    },
                    "_error": str(exc),
                }
            )
            contradiction_pipeline_rows.append(
                {
                    "session_id": sid,
                    "source": source,
                    "count": len(contradictions),
                    "used_in_activation": False,
                    "contradiction_count_used": 0,
                }
            )

    p = out_dir / "20_main_engine_full_context.json"
    _write_json(
        p,
        {
            "run": "tfp_file_pipeline_main_engine_full_context",
            "sessions": session_main_engine_full_context,
            "contradiction_pipeline": contradiction_pipeline_rows,
            "operational_envelope": default_operational_envelope(),
        },
    )
    written["20_main_engine_full_context.json"] = str(p)

    manifest_parts: list[dict[str, Any]] = []
    if not skip_structural and structural_batch:
        manifest_parts.extend(
            [r.get("operational_envelope") or default_operational_envelope() for r in structural_batch]
        )
    if session_sealed:
        manifest_parts.extend(
            [s.get("operational_envelope") or default_operational_envelope() for s in session_sealed]
        )
    if session_analyze:
        manifest_parts.extend(
            [s.get("operational_envelope") or default_operational_envelope() for s in session_analyze]
        )
    manifest_operational_envelope = (
        aggregate_file_envelope(manifest_parts) if manifest_parts else default_operational_envelope()
    )

    manifest = {
        "run": "tfp_file_pipeline_manifest",
        "run_id": os.environ.get("HESPERIA_TFP_PIPELINE_RUN_ID") or str(uuid.uuid4()),
        "repo_root": str(_REPO),
        "session_ids": sids,
        "non_empty_sessions": sum(1 for _, t in sessions if (t or "").strip()),
        "tfp_signal_calibration": {
            "config_version": str(tfp_calibration.get("version") or "unknown"),
            "invariant_path_id": str(tfp_calibration.get("invariant_path_id") or "unknown"),
            "session_topology_run_params": dict(topo_params),
            "loaded_config": tfp_calibration,
            "area_curve_map": dict(AREA_CURVE_MAP),
            "curve_calibration_reference": dict(CURVE_CALIBRATION_REFERENCE),
            "dict_a_confidence_multiplier": dict(CONFIDENCE_TYPE_MULTIPLIER),
            "inhibition_matrix": {
                "version": tfp_inhibition.get("version"),
                "date": tfp_inhibition.get("date"),
                "area_ids": tfp_inhibition.get("area_ids"),
                "intended_range": tfp_inhibition.get("intended_range"),
            },
            "notes": (
                "Invariant TFP path: stabilized concepts -> hex feedback -> area inhibition -> softmax. "
                "session_topology_run_params control segmentation and topology metadata only; "
                "per-session curve_projection_meta and stage rows expose authoritative diagnostic vectors."
            ),
        },
        "flags": {
            "with_kme": with_kme,
            "with_triz": with_triz,
            "with_topology": with_topology,
            "with_r1_r4": with_r1_r4,
            "skip_structural": skip_structural,
            "skip_stages": skip_stages,
            "skip_hex": skip_hex,
            "skip_dlcr": skip_dlcr,
            "skip_sealed": skip_sealed,
            "skip_analyze": skip_analyze,
            "skip_triz_activation": skip_triz_activation,
            "dlcr_mode": dlcr_mode,
            "HESPERIA_DLCR_DOMAIN_PACK": os.environ.get("HESPERIA_DLCR_DOMAIN_PACK"),
            "HESPERIA_ANALYZE_DLCR_EVIDENCE": os.environ.get("HESPERIA_ANALYZE_DLCR_EVIDENCE"),
        },
        "artifacts": written,
        "contradiction_pipeline": contradiction_pipeline_rows,
        "triz_activation": triz_activation_paths,
        "errors": errors,
        "operational_envelope": manifest_operational_envelope,
        "scope_note": (
            "TFP testing / research bundle — not the sealed v0.5.1 product proof. "
            "Planes: A=structural batch, B=session_parser+TFP stage, C=DLCR JSONL v0.6.0, "
            "plus sealed multiscale and analyze()."
        ),
    }
    mp = out_dir / "00_manifest.json"
    _write_json(mp, manifest)
    written_out = dict(written)
    written_out["00_manifest.json"] = str(mp)
    for _sid, sid_paths in triz_activation_paths.items():
        for _fn, pth in sid_paths.items():
            written_out[triz_activation_bundle_filename(_sid, _fn)] = pth
    return {
        "manifest": manifest,
        "paths": written_out,
        "triz_activation_critical": triz_activation_critical,
    }


def main() -> int:
    ap = argparse.ArgumentParser(
        description="TFP file pipeline: input .json sessions or plain text → multi-artifact output directory."
    )
    ap.add_argument("--input", "-i", type=Path, required=True, help="Input .json (sessions[]) or text/markdown file")
    ap.add_argument(
        "--out-dir",
        "-o",
        type=Path,
        default=None,
        help="Output directory (default: outputs/tfp_pipeline_run/<run_id>)",
    )
    ap.add_argument("--with-kme", action="store_true", help="Include KME clinical report per session (07_…)")
    ap.add_argument("--with-triz", action="store_true", help="Include TRIZ complete per session (08_…)")
    ap.add_argument(
        "--with-topology",
        action="store_true",
        help="Include clinical session topology (09_…) and flat 12_<session>_*.json triz_activation artifacts (unless --skip-triz-activation)",
    )
    ap.add_argument(
        "--skip-triz-activation",
        action="store_true",
        help="With --with-topology: do not write 12_* triz_activation files or enforce TRIZ-from-topology gate",
    )
    ap.add_argument("--with-r1-r4", action="store_true", help="Pass r1_r4=True into analyze()")
    ap.add_argument(
        "--dlcr-mode",
        default="clinical_speech",
        help="Mode for run_dlcr_pipeline (default: clinical_speech)",
    )
    ap.add_argument("--skip-structural", action="store_true")
    ap.add_argument("--skip-stages", action="store_true")
    ap.add_argument("--skip-hex", action="store_true")
    ap.add_argument("--skip-dlcr", action="store_true")
    ap.add_argument("--skip-sealed", action="store_true")
    ap.add_argument("--skip-analyze", action="store_true")
    ap.add_argument(
        "--no-dlcr-domain-pack",
        action="store_true",
        help="Do not force HESPERIA_DLCR_DOMAIN_PACK=tfp (leave env as-is)",
    )
    ap.add_argument(
        "--topology-params-json",
        type=Path,
        default=None,
        help="Optional JSON object merged over DEFAULT_SESSION_TOPOLOGY_RUN_PARAMS for run_session_topology",
    )
    args = ap.parse_args()

    inp = args.input.resolve()
    if not inp.is_file():
        print(f"ERROR: input not a file: {inp}", file=sys.stderr)
        return 2

    if not args.no_dlcr_domain_pack:
        os.environ["HESPERIA_DLCR_DOMAIN_PACK"] = "tfp"

    try:
        sessions = load_sessions(inp)
    except Exception as e:  # noqa: BLE001
        print(f"ERROR: load_sessions: {e}", file=sys.stderr)
        return 2

    if not sessions:
        print("ERROR: no sessions loaded", file=sys.stderr)
        return 2

    topology_run_params: dict[str, Any] | None = None
    if args.topology_params_json is not None:
        tp = args.topology_params_json.resolve()
        if not tp.is_file():
            print(f"ERROR: --topology-params-json not a file: {tp}", file=sys.stderr)
            return 2
        try:
            topology_run_params = json.loads(tp.read_text(encoding="utf-8"))
            if not isinstance(topology_run_params, dict):
                print("ERROR: topology JSON must be an object", file=sys.stderr)
                return 2
        except json.JSONDecodeError as e:
            print(f"ERROR: topology JSON: {e}", file=sys.stderr)
            return 2

    run_id = str(uuid.uuid4())
    os.environ["HESPERIA_TFP_PIPELINE_RUN_ID"] = run_id
    out_dir = args.out_dir
    if out_dir is None:
        out_dir = _REPO / "outputs" / "tfp_pipeline_run" / run_id
    out_dir = out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    summary = run_pipeline(
        sessions=sessions,
        out_dir=out_dir,
        with_kme=args.with_kme,
        with_triz=args.with_triz,
        with_topology=args.with_topology,
        with_r1_r4=args.with_r1_r4,
        skip_structural=args.skip_structural,
        skip_stages=args.skip_stages,
        skip_hex=args.skip_hex,
        skip_dlcr=args.skip_dlcr,
        skip_sealed=args.skip_sealed,
        skip_analyze=args.skip_analyze,
        dlcr_mode=args.dlcr_mode,
        skip_triz_activation=args.skip_triz_activation,
        topology_run_params=topology_run_params,
    )

    print(f"tfp_file_pipeline_ok wrote {len(summary['paths'])} files under {out_dir}", file=sys.stderr)
    for name in sorted(summary["paths"]):
        print(summary["paths"][name], file=sys.stderr)
    if summary.get("triz_activation_critical"):
        print("ERROR: triz_activation gate failed (see manifest errors)", file=sys.stderr)
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
