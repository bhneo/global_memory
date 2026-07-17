# ADR 0050: Generated Project Metrics

- Status: Accepted
- Date: 2026-07-17

## Decision

`gm metrics`, `gm metrics --write-project-state` and `gm status --machine-readable` compute tier, epistemic, Revision, Exception, Promotion, Receipt, Drift and corpus counts from the real Vault. README contains no hand-maintained active counts.

## Consequences

PROJECT_STATE holds one current snapshot; historical results move to reports, changelog and Git history.
