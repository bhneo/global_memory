# ADR 0060: Daily Semantic Admission Requires Explicit Coverage

- Status: accepted
- Date: 2026-07-28

## Decision

New Daily Dream artifacts use protocol v2. Before Working admission, the model
records source readability/role and an explicit semantic inventory. Every
candidate receives exactly one create, update, reuse, source-only,
review-required or deferred decision. Create/update decisions map exactly to
the at-most-three semantic items; reuse/update name active stable targets.

High-importance readable Inputs cannot have an empty inventory. High-value,
readable, source-grounded candidates cannot disappear behind a generic
Source-only outcome. Source-only, review and deferral use bounded reason codes,
and a read-only date-range audit exposes unresolved high-value, review and
deferred candidates before Weekly integration. Legacy v1 artifacts remain
accepted only to preserve safe immutable replay after interruption.

Within an audit range, the latest artifact for each stable `input_id` is the
current admission state. A later v2 re-admission can resolve an earlier legacy
gap, while the audit still reports the earlier unresolved event and the number
of repaired Inputs. Weekly ranges extend from the target week's start through
the current date so remediation is not hidden by an artificial week boundary.

Daily stays bounded and Working-only. Cognitive value, semantic value and
evidence strength remain separate; neither high value nor admission changes
Trust. Reflection remains non-factual, and no Daily or audit path writes
Trusted or Canonical.

Weekly completion additionally requires an explicit Obsidian expected/actual
freshness check. Doctor, lint, Raw verification and status do not prove that a
disposable graph projection is current.

## Consequences

The system favors precise knowledge without silently losing readable,
high-value mechanisms or boundaries. Duplicate and low-value material can still
remain Source-only, but every semantic candidate has an auditable outcome.
Graph density is not an acceptance metric, and Canonical writes remain zero.
