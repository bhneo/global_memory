# ADR 0040: Proposal-gate migration

- Status: accepted
- Date: 2026-07-17

## Decision

Pending and deferred proposal candidates migrate to Working after schema validation. Compound or unsupported candidates become exceptions. Approved, rejected and superseded proposals remain unchanged as audit history; existing Canonical files are never rewritten.

The migration supports dry-run, creates a complete proposal backup before applying, and becomes a no-op after completion.
