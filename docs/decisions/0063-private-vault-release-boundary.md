# ADR 0063: Formal Releases Exclude User Knowledge Vaults

- Status: accepted
- Date: 2026-08-02

## Context

Galois is a long-term memory engine. Its value comes from knowledge accumulated
and cognitively consolidated by each user, but that knowledge is not part of
the product source code and must not become a shared project asset.

The current evaluation repository temporarily includes a live multi-domain
vault so web-based models can inspect and assess the complete system. Removing
or relocating it now would interfere with that evaluation. This temporary
state must not be mistaken for the formal distribution boundary.

## Decision

A formal open-source release includes the engine, protocols, adapters, tests,
documentation and optional synthetic fixtures. It excludes the project's live
research vault and every user's Sources, Inputs, Reflections, Syntheses,
knowledge objects, derived indexes and local credentials.

Release preparation will use a non-destructive allowlisted export into a clean
release history. It will verify both the exported tree and its Git history
before publication. It will not delete, rewrite or migrate the working vault in
place, and it will not change runtime paths merely to manufacture a clean
archive. Any optional demonstration vault must contain synthetic or separately
licensed material only.

This ADR records the future release boundary. It does not authorize repository
cleanup or vault migration during the current evaluation phase.

## Consequences

Each user creates and owns an independent vault through Galois capture and
governed consolidation. Public examples cannot depend on the author's private
knowledge. Release tooling must make accidental inclusion fail closed, while
the current working repository remains intact until the user explicitly starts
the release-isolation phase.
