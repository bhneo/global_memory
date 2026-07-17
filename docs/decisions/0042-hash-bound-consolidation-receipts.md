# ADR 0042: Hash-bound Consolidation Receipts

- Status: Accepted
- Date: 2026-07-17

## Context

`consolidation_count += 1` cannot prove that Raw, Evidence, provenance, conflicts or drift were rechecked.

## Decision

Every effective consolidation creates an immutable Receipt bound to object before/after hashes, source hashes, Evidence IDs, named checks, result, changes and exceptions. Promotion accepts only a complete Receipt matching the current object hash.

## Consequences

Object changes invalidate old Receipts automatically. Scans and failed checks remain reportable but cannot satisfy Promotion.
