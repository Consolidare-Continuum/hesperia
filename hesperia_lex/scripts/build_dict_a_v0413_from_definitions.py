#!/usr/bin/env python3
"""Build Dict A v0.4.1.3 from definitions/v0413/families.yaml."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DEFINITIONS_DIR = REPO_ROOT / "hesperia_lex" / "definitions" / "v0413"
FAMILIES_YAML = DEFINITIONS_DIR / "families.yaml"
TABLE_PATH = REPO_ROOT / "31_FAMILIES__area_family_table_full.txt"
OUT_PATH = REPO_ROOT / "hesperia_lex" / "curated" / "A_CORE_STAR_MAP_v0_4_1_3.json"

SIDES_PER_FAMILY = 1500


def _normalize(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", s.lower().strip()).strip("_") or "family"


def _load_yaml(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    try:
        return json.loads(raw)
    except Exception:
        try:
            import yaml
        except ImportError as exc:
            raise SystemExit("PyYAML required when families.yaml is not JSON-compatible.") from exc
        return yaml.safe_load(raw)


def main() -> None:
    if not FAMILIES_YAML.exists():
        print(f"Missing {FAMILIES_YAML}", file=sys.stderr)
        sys.exit(1)

    data = _load_yaml(FAMILIES_YAML)
    sys.path.insert(0, str(DEFINITIONS_DIR))
    import validate as vmod

    errors, warnings, _ = vmod.validate_families_yaml(data, table_path=TABLE_PATH)
    if errors:
        for e in errors:
            print("VALIDATE_ERR:", e, file=sys.stderr)
        sys.exit(1)
    for w in warnings:
        print("VALIDATE_WARN:", w)

    out: dict[str, list[dict]] = {
        "_comment": "Dict A v0.4.1.3 from semantic family definitions (8 real + 2 optional real + up to 2 structural).",
    }

    for f in data["families"]:
        family_id = int(f["family_id"])
        family_global = family_id - 1
        side_id = family_global * SIDES_PER_FAMILY
        central = [_normalize(x) for x in (f.get("central_examples") or []) if isinstance(x, str)]
        boundary = [_normalize(x) for x in (f.get("boundary_examples") or []) if isinstance(x, str)]
        structural = [_normalize(f.get("label_slug", ""))]
        if len(structural[0].split("_")) > 1:
            structural.append(structural[0].split("_")[0])
        else:
            structural.append(f"area{f['area_id']}")

        anchors: list[tuple[str, float, str]] = []
        for i, word in enumerate(central):
            if i < 2:
                w = 0.78
            elif i < 4:
                w = 0.62
            else:
                w = 0.52
            anchors.append((word, w, "definition_central_v0413"))
        for word in boundary:
            anchors.append((word, 0.35, "definition_boundary_v0413"))

        real_anchors = anchors[:10]
        if len(real_anchors) < 8:
            print(f"family {family_id} has fewer than 8 real anchors", file=sys.stderr)
            sys.exit(1)

        final_anchors = real_anchors[:12]
        while len(final_anchors) < 12 and len(real_anchors) > len(final_anchors):
            final_anchors.append(real_anchors[len(final_anchors)])
        for s in structural[:2]:
            if len(final_anchors) >= 12:
                break
            final_anchors.append((s, 0.40, "structural_label_slug_v0413"))

        while len(final_anchors) < 12:
            final_anchors.append((f"fallback_{family_id}_{len(final_anchors)}", 0.35, "fallback_v0413"))

        for slot, (word, weight, code) in enumerate(final_anchors[:12]):
            key = f"{word}_{family_id}_{slot}"
            out[key] = [{"side_id": side_id, "weight": round(weight, 2), "map_code": code}]

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, indent=2), encoding="utf-8")
    n = len([k for k in out if not k.startswith("_")])
    print(f"Wrote {OUT_PATH}: {n} entries")


if __name__ == "__main__":
    main()
