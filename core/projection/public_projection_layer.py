# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
Public projection layer — map full internal structure to safe public structure.
Exposes only public areas 0–9, public families 0–239; excludes reserved areas/families/side_ids.
All public reports, responses, exports, and traces must pass through this layer.
"""

from __future__ import annotations

from typing import Any

from core.topology import reserve_loader

# Public counts (internal has 12 areas, 288 families; 2 areas and 48 families are reserved)
PUBLIC_AREA_COUNT = 10
PUBLIC_FAMILY_COUNT = 240

# Public-safe key names (per PUBLIC_VOCABULARY_MAP)
KEY_MACRO_DOMAIN_VECTOR = "macro_domain_vector"
KEY_POLICY_FAMILY_COUNTS = "policy_family_counts"
KEY_DOMINANT_MACRO_DOMAIN = "dominant_macro_domain"
KEY_DOMINANT_POLICY_FAMILY = "dominant_policy_family"
KEY_PROPAGATED_MACRO_DOMAIN_VECTOR = "propagated_macro_domain_vector"
KEY_PROPAGATED_POLICY_FAMILY_COUNTS = "propagated_policy_family_counts"
KEY_CORRECTED_MACRO_DOMAIN_VECTOR = "corrected_macro_domain_vector"
KEY_CORRECTED_POLICY_FAMILY_COUNTS = "corrected_policy_family_counts"


def filter_reserved_structures(
    area_indices: list[int] | None = None,
    family_indices: list[int] | None = None,
    side_ids: list[int] | None = None,
) -> dict[str, Any]:
    """
    Filter out any reserved area, family, or side_id from the given lists.
    Returns a dict with keys 'area_indices', 'family_indices', 'side_ids' containing
    only non-reserved values. Inputs may be None (returned as empty list).
    """
    out: dict[str, Any] = {
        "area_indices": [],
        "family_indices": [],
        "side_ids": [],
    }
    if area_indices is not None:
        out["area_indices"] = [a for a in area_indices if not reserve_loader.is_reserved_area(a)]
    if family_indices is not None:
        out["family_indices"] = [f for f in family_indices if not reserve_loader.is_reserved_family(f)]
    if side_ids is not None:
        out["side_ids"] = [s for s in side_ids if not reserve_loader.is_reserved_side_id(s)]
    return out


def project_public_areas(
    internal_area_vector: list[float] | None = None,
    internal_area_indices: list[int] | None = None,
) -> dict[str, Any]:
    """
    Project internal 12-area data to public 10-area data.
    - internal_area_vector: length-12 list; indices 10, 11 are dropped.
    - internal_area_indices: list of area indices; reserved (10, 11) are dropped.
    Returns dict with public-safe keys and only indices 0–9.
    """
    result: dict[str, Any] = {}
    if internal_area_vector is not None and len(internal_area_vector) >= 10:
        public_vector = [
            internal_area_vector[i]
            for i in range(PUBLIC_AREA_COUNT)
            if not reserve_loader.is_reserved_area(i)
        ]
        result[KEY_MACRO_DOMAIN_VECTOR] = public_vector
    if internal_area_indices is not None:
        result["macro_domain_indices"] = [
            i for i in internal_area_indices
            if not reserve_loader.is_reserved_area(i) and i < PUBLIC_AREA_COUNT
        ]
    return result


def project_public_families(
    internal_family_counts: list[float] | list[int] | None = None,
    internal_family_indices: list[int] | None = None,
) -> dict[str, Any]:
    """
    Project internal 288-family data to public 240-family data.
    Reserved families 240–287 are excluded.
    Returns dict with public-safe keys and only indices 0–239.
    """
    result: dict[str, Any] = {}
    if internal_family_counts is not None and len(internal_family_counts) >= PUBLIC_FAMILY_COUNT:
        public_counts = [
            float(internal_family_counts[i])
            for i in range(PUBLIC_FAMILY_COUNT)
            if not reserve_loader.is_reserved_family(i)
        ]
        result[KEY_POLICY_FAMILY_COUNTS] = public_counts
    if internal_family_indices is not None:
        result["policy_family_indices"] = [
            i for i in internal_family_indices
            if not reserve_loader.is_reserved_family(i) and i < 288
        ]
    return result


def project_public_metrics(internal_metrics: dict[str, Any]) -> dict[str, Any]:
    """
    Take internal metrics dict (may contain area_vector, family_counts, dominant_area, etc.)
    and return a new dict with only public indices and public-safe key names.
    Reserved areas/families are excluded; raw internal keys are remapped to public vocabulary.
    """
    out: dict[str, Any] = {}
    # Map common internal keys to public keys and slice to public range
    if "area_vector" in internal_metrics:
        av = internal_metrics["area_vector"]
        if isinstance(av, (list, tuple)) and len(av) >= PUBLIC_AREA_COUNT:
            out[KEY_MACRO_DOMAIN_VECTOR] = [av[i] for i in range(PUBLIC_AREA_COUNT) if not reserve_loader.is_reserved_area(i)]
    if "propagated_area_vector" in internal_metrics:
        av = internal_metrics["propagated_area_vector"]
        if isinstance(av, (list, tuple)) and len(av) >= PUBLIC_AREA_COUNT:
            out[KEY_PROPAGATED_MACRO_DOMAIN_VECTOR] = [av[i] for i in range(PUBLIC_AREA_COUNT) if not reserve_loader.is_reserved_area(i)]
    if "corrected_area_vector" in internal_metrics:
        av = internal_metrics["corrected_area_vector"]
        if isinstance(av, (list, tuple)) and len(av) >= PUBLIC_AREA_COUNT:
            out[KEY_CORRECTED_MACRO_DOMAIN_VECTOR] = [av[i] for i in range(PUBLIC_AREA_COUNT) if not reserve_loader.is_reserved_area(i)]

    if "family_counts" in internal_metrics:
        fc = internal_metrics["family_counts"]
        if isinstance(fc, (list, tuple)) and len(fc) >= PUBLIC_FAMILY_COUNT:
            out[KEY_POLICY_FAMILY_COUNTS] = [float(fc[i]) for i in range(PUBLIC_FAMILY_COUNT) if not reserve_loader.is_reserved_family(i)]
    if "propagated_family_counts" in internal_metrics:
        fc = internal_metrics["propagated_family_counts"]
        if isinstance(fc, (list, tuple)) and len(fc) >= PUBLIC_FAMILY_COUNT:
            out[KEY_PROPAGATED_POLICY_FAMILY_COUNTS] = [float(fc[i]) for i in range(PUBLIC_FAMILY_COUNT) if not reserve_loader.is_reserved_family(i)]
    if "corrected_family_counts" in internal_metrics:
        fc = internal_metrics["corrected_family_counts"]
        if isinstance(fc, (list, tuple)) and len(fc) >= PUBLIC_FAMILY_COUNT:
            out[KEY_CORRECTED_POLICY_FAMILY_COUNTS] = [float(fc[i]) for i in range(PUBLIC_FAMILY_COUNT) if not reserve_loader.is_reserved_family(i)]

    dominant_area = internal_metrics.get("dominant_area") or internal_metrics.get("DOMINANT_AREA_ID")
    if dominant_area is not None:
        a = int(dominant_area)
        if not reserve_loader.is_reserved_area(a) and a < PUBLIC_AREA_COUNT:
            out[KEY_DOMINANT_MACRO_DOMAIN] = a
    dominant_family = internal_metrics.get("dominant_family") or internal_metrics.get("DOMINANT_FAMILY_ID")
    if dominant_family is not None:
        f = int(dominant_family)
        if not reserve_loader.is_reserved_family(f) and f < 288:
            out[KEY_DOMINANT_POLICY_FAMILY] = f

    # Copy over non-structural metrics that are already safe (scalars, non-revealing)
    safe_keys = {
        "entropy", "coverage", "tension", "loopability", "governance",
        "confidence", "trust_tier", "contradiction", "divergence",
        "structural_focus", "evidence_count", "run_version", "result_hash",
    }
    for k, v in internal_metrics.items():
        if k in safe_keys or (k not in out and not _is_internal_revealing_key(k)):
            if k not in (
                "area_vector", "family_counts", "propagated_area_vector", "propagated_family_counts",
                "corrected_area_vector", "corrected_family_counts",
                "dominant_area", "dominant_family", "DOMINANT_AREA_ID", "DOMINANT_FAMILY_ID",
            ):
                out[k] = v
    return out


def _is_internal_revealing_key(key: str) -> bool:
    """True if key name reveals internal geometry/topology. L1–L9 kept but their contents are sanitized recursively."""
    revealing = (
        "side_id", "hex", "hexagon", "sphere", "topology", "adjacency",
        "area_sequence", "family_sequence", "area_id", "family_id",
        "AREA_", "FAMILY_", "layer_", "bridge",
    )
    return any(r in key.lower() for r in revealing)


def sanitize_public_trace(trace: dict[str, Any] | list[Any]) -> dict[str, Any] | list[Any]:
    """
    Sanitize a trace object for public emission: remove reserved structures and
    internal-revealing keys/values. Evidence may remain; internal coordinates and
    propagation internals must not.
    """
    if isinstance(trace, list):
        return [sanitize_public_trace(item) for item in trace if _trace_item_safe(item)]
    if not isinstance(trace, dict):
        return trace
    out: dict[str, Any] = {}
    for k, v in trace.items():
        if _is_internal_revealing_key(k):
            continue
        if k in ("area_vector", "family_counts", "propagated_area_vector", "propagated_family_counts",
                 "corrected_area_vector", "corrected_family_counts") and isinstance(v, (list, tuple)):
            # Replace with projected public slice
            if "area" in k:
                out[KEY_MACRO_DOMAIN_VECTOR if k == "area_vector" else (
                    KEY_PROPAGATED_MACRO_DOMAIN_VECTOR if k == "propagated_area_vector" else KEY_CORRECTED_MACRO_DOMAIN_VECTOR
                )] = [v[i] for i in range(min(len(v), PUBLIC_AREA_COUNT)) if not reserve_loader.is_reserved_area(i)]
            else:
                out[KEY_POLICY_FAMILY_COUNTS if k == "family_counts" else (
                    KEY_PROPAGATED_POLICY_FAMILY_COUNTS if k == "propagated_family_counts" else KEY_CORRECTED_POLICY_FAMILY_COUNTS
                )] = [float(v[i]) for i in range(min(len(v), PUBLIC_FAMILY_COUNT)) if not reserve_loader.is_reserved_family(i)]
            continue
        if k in ("dominant_area", "dominant_family", "DOMINANT_AREA_ID", "DOMINANT_FAMILY_ID"):
            idx = int(v) if v is not None else None
            if idx is not None:
                if "area" in k and not reserve_loader.is_reserved_area(idx):
                    out[KEY_DOMINANT_MACRO_DOMAIN] = idx
                elif "family" in k and not reserve_loader.is_reserved_family(idx):
                    out[KEY_DOMINANT_POLICY_FAMILY] = idx
            continue
        out[k] = sanitize_public_trace(v) if isinstance(v, (dict, list)) else v
    return out


def apply_public_projection(payload: dict[str, Any]) -> dict[str, Any]:
    """
    Apply full public projection to a payload. Call before writing any public artifact
    (report, manifest, JSON export, evidence trace, dashboard payload).
    Removes reserved structures and internal-revealing keys; remaps to public vocabulary.
    """
    return sanitize_public_trace(payload)


def _trace_item_safe(item: Any) -> bool:
    """Filter trace list items that reference reserved structures (e.g. side_id in range)."""
    if isinstance(item, dict):
        sid = item.get("side_id")
        if sid is not None and reserve_loader.is_reserved_side_id(int(sid)):
            return False
        fid = item.get("family_id")
        if fid is not None and reserve_loader.is_reserved_family(int(fid)):
            return False
        aid = item.get("area_id")
        if aid is not None and reserve_loader.is_reserved_area(int(aid)):
            return False
    return True
