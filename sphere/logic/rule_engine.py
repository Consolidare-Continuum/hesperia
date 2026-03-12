"""
Layer-9 Rule engine: evaluate rules against structural facts, return triggered rules and diagnostics.
Strictly downstream of measurement layers; strictly upstream of interpretation.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from . import diagnostics, rule_runtime, trigger_registry

_DEFAULT_SPEC = Path(__file__).resolve().parents[2] / "spec" / "logic_rules.yaml"


def _collect_matched_facts(rule: dict[str, Any], facts: dict[str, Any]) -> dict[str, Any]:
    """Extract fact names and values from rule conditions that are present in facts."""
    out: dict[str, Any] = {}
    conds = rule.get("conditions") or {}
    for key in ("all", "any"):
        if key not in conds:
            continue
        for c in conds[key]:
            name = c.get("fact")
            if name is not None and name in facts:
                out[name] = facts[name]
    return out


def _ordered_rules(rules: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Enabled rules only, sorted by priority descending, tie-break rule_id ascending."""
    enabled = [r for r in rules if r.get("enabled") is True]
    return sorted(enabled, key=lambda r: (-int(r.get("priority", 0)), r.get("rule_id", "")))


def evaluate_rules(
    facts: dict[str, Any],
    rules: list[dict[str, Any]] | None = None,
    rule_spec_path: str | Path | None = None,
) -> dict[str, Any]:
    """
    Layer-9 entrypoint: evaluate rules against facts, return deterministic diagnostics artifact.

    Rules: either pass `rules` list (already loaded/validated) or set `rule_spec_path`.
    If both omitted, uses spec/logic_rules.yaml. Validates rules once if loaded from path.

    Returns:
      triggered_rules: list of triggered rule objects with matched_facts
      structural_diagnostics: list of diagnostic dicts (traceable, machine-clean)
      rule_trigger_registry: counts and ordering by severity/code
    """
    if rules is None:
        path = rule_spec_path if rule_spec_path is not None else _DEFAULT_SPEC
        rules = rule_runtime.load_rules(path)
        rule_runtime.validate_rule_spec(rules)
    else:
        rule_runtime.validate_rule_spec(rules)

    ordered = _ordered_rules(rules)
    triggered: list[dict[str, Any]] = []
    for r in ordered:
        if not rule_runtime.evaluate_condition_group(r.get("conditions") or {}, facts):
            continue
        matched = _collect_matched_facts(r, facts)
        triggered.append({
            "rule_id": r.get("rule_id", ""),
            "name": r.get("name", ""),
            "priority": r.get("priority", 0),
            "severity": r.get("severity", "medium"),
            "diagnostic_code": r.get("diagnostic_code", ""),
            "diagnostic_message": r.get("diagnostic_message", ""),
            "matched_facts": matched,
        })

    structural_diagnostics = diagnostics.build_structural_diagnostics(triggered, facts)
    rule_trigger_registry = trigger_registry.build_rule_trigger_registry(triggered, facts)

    return {
        "triggered_rules": triggered,
        "structural_diagnostics": structural_diagnostics,
        "rule_trigger_registry": rule_trigger_registry,
    }


