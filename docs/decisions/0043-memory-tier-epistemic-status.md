# ADR 0043: Separate Memory Tier from Epistemic Status

- Status: Accepted
- Date: 2026-07-17

## Context

`trusted` previously mixed retention value with factual confidence and could not represent a durable unanswered Question or exploratory Analogy safely.

## Decision

Use orthogonal `memory_tier` (`working|trusted|canonical|historical`) and `epistemic_status` (established, supported, provisional, contested, hypothetical, open_question, partially_answered, exploratory_analogy, observed_anomaly, user_intuition, superseded, unknown).

## Consequences

Trusted no longer means factual truth. Legacy `status` becomes a compatibility mirror; unknown legacy values migrate conservatively.
