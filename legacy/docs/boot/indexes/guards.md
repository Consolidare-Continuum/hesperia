# Historical reference (pre-refactor)

# Hesperia Guard Wiring (v0.2.0.1)

Execution order is mandatory and non-bypassable for runtime traversal:

1. **Σ (scripts/sigma_guard.py)** preflight at startup.
2. **Γ (scripts/gamma_guard.py)** on each traversal step.
3. **Θ (scripts/theta_gate.py)** once at the end, over the full run result.

Precedence rule with script-level `TraversalSafeguard`:

- In `sphere_rag` phase traversal, Σ/Γ/Θ is authoritative.
- `TraversalSafeguard` in `scripts/hesperia_logic.py` remains a separate script-level safety mechanism for that script's own loop flow.
- If both are used in one runtime, Γ stop reason must be treated as primary stop authority and surfaced in output.
