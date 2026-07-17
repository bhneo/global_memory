# ADR 0033: Proposal gate becomes a promotion gate

- Status: accepted
- Date: 2026-07-17

## Decision

Validated compiler output is written automatically to `vault/memory/` as `working`. Proposals and immutable candidates remain audit material, but routine per-item approval is no longer required for usable memory. Human confirmation moves to the rare `trusted -> canonical` transition.

## Consequences

Ingestion is cheap and useful immediately. Canonical remains scarce and user-controlled. Legacy library approval APIs remain for recovery compatibility, but the CLI routes compile/review through Working memory.
