# ADR 0037: Weekly memory consolidation

- Status: accepted
- Date: 2026-07-17

## Decision

Weekly consolidation reviews Working objects, increments review provenance, applies Trusted policy, runs drift audit, creates exception records, and recommends high-impact Canonical candidates. It emits a digest with retention, promotions, exceptions, estimated review time and compression ratio.

The process is incremental and may not silently resolve contradictions or create Canonical content.
