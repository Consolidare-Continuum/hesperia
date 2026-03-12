"""
Layer-9 Structural diagnostics: transform triggered rules into canonical diagnostic objects.
Deterministic, traceable to facts; machine-clean, no interpretation prose.
"""

from __future__ import annotations

from typing import Any


def build_diagnostic(triggered_rule: dict[str, Any], facts: dict[str, Any]) -> dict[str, Any]:
    """
    Build one structural diagnostic from a triggered rule and current facts.
    Evidence is the subset of facts referenced by the rule (matched_facts if present, else key facts).
    """
    evidence = triggered_rule.get("matched_facts")
    if evidence is None:
        evidence = {}
    return {
        "rule_id": triggered_rule.get("rule_id", ""),
        "diagnostic_code": triggered_rule.get("diagnostic_code", ""),
        "severity": triggered_rule.get("severity", "medium"),
        "message": triggered_rule.get("diagnostic_message", ""),
        "evidence": dict(evidence),
    }


def build_structural_diagnostics(
    triggered_rules: list[dict[str, Any]],
    facts: dict[str, Any],
) -> list[dict[str, Any]]:
    """
    Build canonical structural diagnostics list from triggered rules, preserving order.
    Deterministic and traceable to triggering facts.
    """
    return [build_diagnostic(tr, facts) for tr in triggered_rules]
