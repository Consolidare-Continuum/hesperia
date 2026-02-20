# Hesperia /hesperia/analyze — build response from context_rag + optional semantic seed
from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CURSOR_ROOT = Path("/data/workspaces/cursor")
CANONICAL_AREAS = [
    "GOOD", "HARM", "TRUTH", "DECEIT", "ORDER", "CHAOS",
    "FREEDOM", "CONTROL", "CARE", "INDIFFERENCE", "CREATION", "DESTRUCTION",
]
HESPERIA_VERSION = "0.2.0.1"


def _run_context_rag(text: str, chroma: bool = True) -> dict | None:
    """Run context_rag.py with --query text and --chroma. Needs PYTHONPATH including cursor for Chroma."""
    script = REPO_ROOT / "scripts" / "context_rag.py"
    if not script.is_file():
        return None
    env = os.environ.copy()
    env["PYTHONPATH"] = os.pathsep.join([
        str(CURSOR_ROOT),
        str(REPO_ROOT),
        env.get("PYTHONPATH", ""),
    ]).strip(os.pathsep)
    env.setdefault("CHROMA_SERVER_URL", "http://127.0.0.1:8002")
    env.setdefault("HESPERIA_DATA_DIR", str(REPO_ROOT))
    cmd = [
        sys.executable,
        str(script),
        "--start", "0",
        "--direction", "1",
        "--steps", "12",
        "--query", text[:2000] if text else "",
    ]
    if chroma:
        cmd.append("--chroma")
    try:
        out = subprocess.run(
            cmd,
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=45,
            env=env,
        )
        if out.returncode != 0:
            return None
        return json.loads(out.stdout)
    except (subprocess.TimeoutExpired, json.JSONDecodeError, FileNotFoundError):
        return None


def _semantic_seed_from_text(text: str) -> tuple[int, int, str, str]:
    """Use sphere_rag semantic_engine to get dominant area/family from text. Returns (area_id, family_global, area_name, family_name)."""
    try:
        sys.path.insert(0, str(REPO_ROOT))
        from sphere_rag.semantic_engine import keywords_to_seed, CANONICAL_AREAS
        from sphere_rag.geometry import FAMILIES_PER_AREA

        families_path = REPO_ROOT / "31_FAMILIES__area_family_table_full.txt"
        if not families_path.is_file():
            return 0, 0, CANONICAL_AREAS[0], ""
        # Use first few words as keywords for deterministic seed
        keywords = [w for w in text.split() if len(w) > 2][:10]
        if not keywords:
            keywords = ["truth"]
        seed = keywords_to_seed(keywords, families_table_path=str(families_path))
        area_id = seed.start_area_id
        family_global = seed.start_family_global
        area_name = CANONICAL_AREAS[area_id]
        family_name = ""
        with open(families_path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) >= 3:
                    try:
                        g = int(parts[0].strip()) - 1
                        if g == family_global:
                            family_name = parts[2].strip()
                            break
                    except ValueError:
                        continue
        return area_id, family_global, area_name, family_name
    except Exception:
        return 0, 0, CANONICAL_AREAS[0], ""


def _road_to_region_labels(road: list[dict], max_labels: int = 5) -> list[str]:
    """Convert road_coordinates to side labels A02-F01-H001-S0 format. Capped for MVP (small payload)."""
    from sphere_rag.geometry import SideCoord, FAMILIES_PER_AREA, HEXES_PER_FAMILY, SIDES_PER_HEX

    labels = []
    seen = set()
    for step in road[:max_labels]:
        area_id = step.get("area_id", 0)
        global_id = step.get("global_id", 0)
        family_local = global_id % FAMILIES_PER_AREA
        hex_index = 0
        side_index = 0
        coord = SideCoord(area=area_id, family_local=family_local, hex_index=hex_index, side_index=side_index)
        label = coord.label()
        if label not in seen:
            seen.add(label)
            labels.append(label)
    return labels


def build_analyze_response(
    text: str,
    *,
    include_supporting_statements: bool = True,
    max_supporting_statements: int = 10,
    return_region_coordinates: bool = True,
    return_metrics: bool = True,
) -> dict:
    """Build HesperiaAnalyzeResponse dict from text. Uses context_rag + semantic seed."""
    packet = _run_context_rag(text, chroma=True)
    area_id, family_global, area_name, family_name = _semantic_seed_from_text(text)

    if not family_name and packet:
        hints = packet.get("coherence_hints", {})
        area_name = hints.get("current_area_name") or area_name
        area_id = hints.get("current_area_id", area_id)
        road = packet.get("calculable", {}).get("road_coordinates", [])
        if road:
            last = road[-1]
            area_name = last.get("area_name", area_name)
            family_name = last.get("family_name", "")
            family_global = last.get("global_id", family_global)

    loopability_val = 0.5
    if packet:
        calc = packet.get("calculable", {})
        loopability_val = calc.get("loopability", {}).get("L_full")
        if loopability_val is None:
            loopability_val = 0.5
        loopability_val = max(0.0, min(1.0, float(loopability_val)))

    region_coordinates = None
    if return_region_coordinates and packet:
        road = packet.get("calculable", {}).get("road_coordinates", [])
        region_coordinates = _road_to_region_labels(road) or None

    metrics = None
    if return_metrics and packet:
        obs = packet.get("observability", {})
        entropy = obs.get("entropy_metric")
        metrics = {
            "T_norm": loopability_val,
            "areaEntropy": entropy,
            "evidenceQuality": 0.5,
            "causalCoherence": 0.0,
        }

    supporting_statements = None
    if include_supporting_statements and packet and packet.get("retrieval", {}).get("families"):
        families = packet["retrieval"]["families"][:max_supporting_statements]
        supporting_statements = [
            {
                "statement_id": f"fam-{i}",
                "text": (f.get("document") or f.get("concept") or "")[:120],
                "side_label": f"A{int(f.get('area_id', 0))+1:02d}-F{(int(f.get('global_id', 0)) % 24)+1:02d}-H001-S0",
                "tau": 0.8,
            }
            for i, f in enumerate(families)
        ]

    return {
        "dominant_area": area_name,
        "dominant_family": family_name or "Unknown",
        "area_index": area_id,
        "family_global_index": family_global,
        "loopability": round(loopability_val, 6),
        "tension_energy": 0.0,
        "obstacle_score": 0.0,
        "governance": "allow",
        "metrics": metrics,
        "region_coordinates": region_coordinates,
        "supporting_statements": supporting_statements,
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "version": HESPERIA_VERSION,
    }
