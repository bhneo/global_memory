# ADR 0056: M9 Quality Closure

- Status: accepted
- Date: 2026-07-18

## Decision

Routine maintenance consumes only active Working and Trusted memory. Historical,
archived and superseded objects remain durable audit material but are excluded from
Weekly consolidation, automatic promotion and routine requalification.

`source_only` is a successful terminal compile disposition, not a failure. An
unmarked web, PDF, GitHub or automated capture remains source-only unless an
explicit typed marker or external structured provider supplies a governed candidate.
The deterministic paragraph fallback is limited to bounded, sentence-like personal
notes. Session receipts do not receive an implicit knowledge fallback.

Research annotations remain append-only. Consumers use only the active leaf of a
supersession chain; history remains available for audit. Annotation payloads in
Context remain user-authored intent/value signals and are never execution-safe.

Working-quality migrations retain exact backups and snapshots. Verify checks the
manifest, backup bytes, exact post-migration object bytes, current historical
state, snapshots, source/Raw availability, archive events and the Canonical hash
baseline. Restore is explicit, checks that the migrated target has not changed
and that no Working Revision or Canonical successor exists, and never touches
Raw or Canonical. Incomplete manifests resume under their original migration ID;
event replay is idempotent. Legacy manifests require an explicit safety-baseline
upgrade before they receive post-image restore protection.

## Consequences

Weekly counts represent active cognitive maintenance rather than historical noise.
Source-only material remains visible in metrics and Obsidian. No M9.0.1 behavior
promotes knowledge, changes Trust, or writes Canonical automatically.
