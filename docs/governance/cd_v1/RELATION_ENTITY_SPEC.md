# CD `type: relation` — operational entity (v1.0)

**Entity** for Hesperia text pipeline (DLCR / session):

1. **Primary**: **resolved span** — one `resolve_hit` outcome (same `source_text_span` + `winning_concept_id` as one atomic unit).
2. **Secondary (speaker-aware paths)**: **speaker-attributed span** — same as (1) plus `speaker_id` when session parser provides it.

A concept row with `type: relation` **must not** receive full weight unless **at least two distinct entities** (by the definition above) are present in the active evidence set for the current segment. Enforcement is **Phase 2+** (engine branch); Phase 1 records type only.

SIGNED: Architect (Ethan) | relation entity | 2026-03-27
