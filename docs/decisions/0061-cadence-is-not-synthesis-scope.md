# ADR 0061: Cadence Is Not a Cognitive Synthesis Scope

- Status: accepted
- Date: 2026-07-28

## Decision

Weekly remains a scheduling and governance cadence, but a natural week is not a
semantic aggregation boundary. The date range selects newly eligible or
unresolved material for audit. Cognitive Synthesis is scoped by a research
direction or an explicit cross-direction comparison defined in
`docs/RESEARCH_DIRECTIONS.md`.

Synthesis protocol v2 records `scope_kind`, `scope_ids`, `candidate_window`,
`delta_kind`, exact direction assignments, and optional input Syntheses. A
direction Synthesis has one scope; a cross-direction Synthesis has at least two
scopes and cites at least two active direction Syntheses. Legacy `period`
artifacts remain readable and replayable but are audit history rather than the
default production format.

Every v2 cross-direction connection retains supporting Reflection/Source IDs,
shared mechanism, boundary, difference, research value, counterarguments,
evidence gaps, verification path, and confidence. Cross-direction output is
optional: keyword overlap, co-occurrence, or calendar proximity cannot force a
connection. Direction-local connections retain the existing qualified
shared-mechanism/boundary/difference contract and their Synthesis-level source
chain.

Reflection and Cognitive Synthesis remain non-factual, non-Evidence, without a
Memory Tier, and never execution-safe. Optional semantic bundles still enter
Working only; Trusted and Canonical policy is unchanged.

## Consequences

The recurring job can audit on a calendar while evolving durable research lines
incrementally. Unchanged directions produce a no-op/reuse report instead of a
new weekly summary. Cross-disciplinary discovery gains explicit provenance and
falsification boundaries without being laundered into confirmed knowledge.
