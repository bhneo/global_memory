# ADR 0044: Trusted Revision and Demotion Governance

- Status: Accepted
- Date: 2026-07-17

## Decision

Supporting evidence may update Trusted while preserving tier and trust. Semantic changes create a separate Working Revision and immutable prior-version snapshot. Conflict marks epistemic status contested and creates an Exception. Every Trusted demotion creates a Demotion Event; Canonical never auto-demotes.

## Consequences

Trusted history is explainable and rollbackable; ingestion cannot silently reset trust or overwrite a stable statement.
