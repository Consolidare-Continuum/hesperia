# Hesperia Guard Wiring (v0.2.0.1)

Execution order is mandatory and non-bypassable for runtime traversal:

1. **Σ (sigma_guard_v3.py)** preflight at startup.
2. **Γ (gamma_guard_v1.py)** on each traversal step.
3. **Θ (theta_gate_v1.py)** once at the end, over the full run result.

Precedence rule with script-level `TraversalSafeguard`:

- In `sphere_rag` phase traversal, Σ/Γ/Θ is authoritative.
- `TraversalSafeguard` in `scripts/hesperia_logic.py` remains a separate script-level safety mechanism for that script's own loop flow.
- If both are used in one runtime, Γ stop reason must be treated as primary stop authority and surfaced in output.
