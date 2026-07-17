# ADR 0036: Canonical requires human confirmation

- Status: accepted
- Date: 2026-07-17

## Decision

No automatic task may write Canonical. A Trusted object first produces a promotion card explaining importance, evidence and uncertainty. Only `gm promotion approve` moves it into a canonical directory; `--lock` prevents later automatic changes.

Rejection and deferral preserve the card and reason. Weekly consolidation may recommend cards but always reports `canonical_writes: 0`.
