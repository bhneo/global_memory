# ADR 0049: Separate Historical and Current Acceptance Fixtures

- Status: Accepted
- Date: 2026-07-17

## Decision

CI separates historical fixture compatibility, current architecture acceptance and migration acceptance. Historical M6 fixtures may validate old Proposal states but cannot require the live M8 Vault to remain Proposal-only.

## Consequences

The six-platform matrix tests real current invariants without deleting or weakening historical checks.
