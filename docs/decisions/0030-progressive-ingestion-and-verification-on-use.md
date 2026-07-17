# ADR 0030: Progressive ingestion and verification on use

- Status: accepted
- Date: 2026-07-16

## Decision

Routine ingestion is split from knowledge compilation. Capture remains append-only and cheap. `gm triage` incrementally creates or reuses derived extraction and quality assessment, with a bounded default batch size of 25, but does not create proposals or canonical knowledge by default.

Compilation is opt-in through `--compile-selected` or the existing explicit compile/model-propose commands. Deep primary-source verification is paid when a source is important, decision-critical, repeatedly retrieved, contradictory, or being promoted toward confirmed knowledge. A valid source may remain capture-only and searchable indefinitely.

Daily work uses inexpensive incremental triage. `gm weekly` composes bounded triage, integrity checks, explicit contradiction audit, backlog inventory, derived-view rebuild, and synthesis eligibility reporting. It never creates synthesis proposals or canonical writes automatically; scheduling and model invocation remain outside the core repository for now.

## Consequences

Per-article cost and review backlog no longer grow automatically with capture volume. Provenance and canonical approval gates remain unchanged, but their cost moves to knowledge use and promotion rather than initial collection.
