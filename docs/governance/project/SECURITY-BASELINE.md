<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Security baseline — hesperia

Ref: [LEAN-GOVERNANCE.md](../../LEAN-GOVERNANCE.md), [governance/SECURITY-PROCEDURE.md](../../governance/SECURITY-PROCEDURE.md). **Critical** = release blocked until resolved (Daniel veto).

## Critical definition (Daniel)

- Data exposure (PII, credentials in logs or client).
- Auth bypass; remote execution; privilege escalation.

Any of the above → Daniel **blocks** release until mitigated or accepted by You.

## Minimum bar (release)

| Check | Owner | Requirement |
|-------|--------|-------------|
| Dependency scan | Daniel | No critical/high unmitigated. |
| Authentication / authorization | Daniel | Enforced on protected endpoints. |
| Secrets | Daniel | Not in code/config in repo; use secret store. (.env in workspace per [cluster/GITHUB-REPOS.md](../../cluster/GITHUB-REPOS.md).) |
| Infra hardening | Daniel | Per env. |

Project-specific additions (if any) to be added here. Otherwise standard baseline applies.
