HESPERIA cryptographic copyright / proof-of-work chain
Source: igareosh/hesperia git commit b1e0feac (2026-03-12)
Removed from tip by 3b31604 (docs/ prod strip) — recoverable from git history.

Files:
- ARCHITECTURE_FINGERPRINT.txt — SHA256 + commit c6bcf14 + tag HESPERIA_RAD_FREEZE evidence chain
- HESPERIA_SYSTEM_SPEC_v1.md — RAD architecture document (fingerprinted content)
- HESPERIA_SYSTEM_SPEC_v1.md.ots — OpenTimestamps proof (Bitcoin blockchain anchor)

Verify:
  sha256sum HESPERIA_SYSTEM_SPEC_v1.md
  ots verify HESPERIA_SYSTEM_SPEC_v1.md HESPERIA_SYSTEM_SPEC_v1.md.ots
  git rev-parse HESPERIA_RAD_FREEZE   (in full clone with tag)
