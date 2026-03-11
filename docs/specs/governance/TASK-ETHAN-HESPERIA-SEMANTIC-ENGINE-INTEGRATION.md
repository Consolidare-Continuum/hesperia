# Task: Ethan — Semantic engine integration in Hesperia

**Owner**: Ethan
**Project**: hesperia
**Triage**: Grace
**Status**: DONE
**Report**: [ETHAN-HESPERIA-SEMANTIC-ENGINE-REPORT.md](ETHAN-HESPERIA-SEMANTIC-ENGINE-REPORT.md) — 2026-02-18

## Objective

Ethan: semantic engine integration in Hesperia — spec, scope, and/or design per project foundations (CONTEXT-PACKET, SCOPE-AND-SYNC, ARCH-DECISION). Align with current cursor-repo use (matrix, context RAG, Chroma) and with Hesperia product semantic layer when in scope.

## Refs

- [projects/hesperia/CONTEXT-PACKET.md](../projects/hesperia/CONTEXT-PACKET.md) — semantic layer "not in scope yet"; agents use = cursor-repo.
- [projects/hesperia/SCOPE-AND-SYNC.md](../projects/hesperia/SCOPE-AND-SYNC.md)
- [governance/HESPERIA-MULTIPLE-LOOP-BOUNDARIES.md](HESPERIA-MULTIPLE-LOOP-BOUNDARIES.md) — product semantic layer out of scope until Phase D.
- [governance/HESPERIA-RAG-DAEMON-MVP-PROPOSAL-ETHAN.md](HESPERIA-RAG-DAEMON-MVP-PROPOSAL-ETHAN.md) — context RAG (cursor-repo); full product semantic layer separate.

## Deliverable

Ethan: proposal or report (scope, boundaries, integration points for semantic engine in Hesperia). Gate: Grace triage; execution/division after Ethan output.

**Outcome (2026-02-18)**: Report delivered. **Recommendation: use Chroma** as semantic engine for Hesperia (cursor-repo and product when in scope). No separate tech investigation for an alternative engine unless Phase D requires it or we hit Chroma limits.
