# ADR 0038: Memory exception queue

- Status: accepted
- Date: 2026-07-17

## Decision

Only compound claims, missing evidence, contradictions, drift and attempted Canonical changes require exception records. Exceptions live under `vault/exceptions/` with deterministic IDs, severity, reasons, context and resolution history.

Routine low-confidence material stays Working; uncertainty alone is not an exception.
