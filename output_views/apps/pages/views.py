from __future__ import annotations

import json
from pathlib import Path

from django.conf import settings
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.views.decorators.http import require_GET

from . import inspector as insp
from segment.constants import DISCLAIMER_FOOTER_EN


@require_GET
def health(_request: HttpRequest) -> JsonResponse:
    return JsonResponse({"status": "ok", "surface": "hesperia_output_views"})


@require_GET
def operator_home(request: HttpRequest) -> HttpResponse:
    """Operator landing: links to preview surfaces and health."""
    return render(
        request,
        "pages/operator_home.html",
        {
            "title": "Hesperia output views",
            "hesperia_root": settings.HESPERIA_ROOT,
        },
    )


@require_GET
def client_preview(request: HttpRequest) -> HttpResponse:
    """Client-centric placeholder page — static shell for future report builder."""
    return render(
        request,
        "pages/client_preview.html",
        {"title": "Client preview", "subtitle": "Hesperia structured outputs (HTML)"},
    )


@require_GET
@require_GET
def session_inspector(request: HttpRequest, session_id: str) -> HttpResponse:
    """T13–T21 — Session Inspector MVP (fixture-backed). Deep links: ?iteration=&sentence="""
    bundle = insp.load_inspector_fixture(session_id)
    meta = bundle.get("meta") or {}
    order_q = request.GET.get("iteration")
    current, all_iter = insp.resolve_iteration(bundle, order_q)
    sentences = insp.sourced_text_lines(current)
    sentence_q = request.GET.get("sentence")
    if sentence_q:
        active_sid = sentence_q.strip()
    elif sentences:
        active_sid = str(sentences[0].get("id", ""))
    else:
        active_sid = ""

    iter_options: list[dict[str, str | int]] = []
    for it in all_iter:
        iter_options.append(
            {
                "order": int(it.get("order", 0)),
                "iteration_id": str(it.get("iteration_id", "")),
                "label": insp.iteration_label(it),
            }
        )

    params = current.get("parameters") or {}
    areas = params.get("areas") if isinstance(params.get("areas"), dict) else {}
    families = params.get("families") if isinstance(params.get("families"), dict) else {}
    metrics = params.get("metrics") if isinstance(params.get("metrics"), dict) else {}
    modules = params.get("modules") if isinstance(params.get("modules"), dict) else {}
    modules_json = mark_safe(json.dumps(modules, indent=2, ensure_ascii=False)) if modules else ""

    return render(
        request,
        "pages/session_inspector.html",
        {
            "title": "Session Inspector",
            "session_id": session_id,
            "meta": meta,
            "bundle": bundle,
            "iterations": iter_options,
            "current": current,
            "current_order": int(current.get("order", 0)),
            "sentences": sentences,
            "active_sentence_id": active_sid,
            "parameters": params,
            "parameters_json": mark_safe(json.dumps(params, indent=2, ensure_ascii=False)),
            "areas": areas,
            "families": families,
            "metrics": metrics,
            "modules": modules,
            "modules_json": modules_json,
            "audit": current.get("audit") or {},
            "disclaimer": meta.get("disclaimer_footer") or DISCLAIMER_FOOTER_EN,
        },
    )


@require_GET
def artifact_sample(request: HttpRequest) -> HttpResponse:
    """Read-only sample: list e2e artifact filenames (no path injection)."""
    root = Path(settings.HESPERIA_ROOT) / "assets" / "artifacts" / "e2e"
    names: list[str] = []
    if root.is_dir():
        names = sorted(p.name for p in root.iterdir() if p.is_file() and p.suffix == ".json")[:50]
    return render(
        request,
        "pages/artifact_list.html",
        {"title": "E2E artifacts (sample)", "artifacts": names, "root_display": str(root)},
    )
