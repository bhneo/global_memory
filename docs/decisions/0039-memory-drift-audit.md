# ADR 0039: Read-only memory drift audit

- Status: accepted
- Date: 2026-07-17

## Decision

`gm audit drift` detects translations presented as exact quotes, claims losing source/evidence, unsupported synthesis, analogies losing their boundary, and high-confidence claims whose entailment is incomplete. The audit is read-only; Weekly may turn findings into exception records without changing the affected memory.
