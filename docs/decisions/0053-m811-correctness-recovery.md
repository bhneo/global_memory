# ADR 0053: M8.1.1 Correctness Recovery

- Status: accepted
- Date: 2026-07-17

## Decision

Policy upgrades do not erase previously accepted Trusted state. Legacy Trusted objects remain Trusted with `needs_policy_requalification=true` until the current policy succeeds. Requalification clears that marker without adding a second promotion or a false demotion.

Receipt v1 is immutable history and cannot satisfy current trust gates. Receipt v2 reuse requires an exact current object hash and a fingerprint covering source records, Raw bytes, Evidence/extraction identity, logical works, relations, contradictions, schema and policy versions. Failed attempts are independent immutable records with real Findings.

All governed Trusted mutations use the recoverable sequence `prepared -> staged -> receipt_completed -> event_logged -> finalized`. Recovery rolls back pre-Receipt state and safely finishes post-Receipt state with an idempotent audit event. Canonical evolution always becomes an update Proposal and optional Exception; it never mutates Canonical directly.

External providers identify updates using `action=update` and stable `target_id`. Titles are presentation metadata, not identity.

## Consequences

Trusted totals no longer conceal qualification state. Metrics separately expose Policy v3-qualified, awaiting-requalification and contested Trusted objects, Receipt schema versions, failed attempts and pending recovery journals. Strict execution and Canonical gates reject awaiting objects while research remains able to inspect them with their boundary visible.
