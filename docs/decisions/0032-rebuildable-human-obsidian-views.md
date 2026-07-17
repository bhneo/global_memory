# ADR 0032: Rebuildable human-facing Obsidian views

- Status: accepted
- Date: 2026-07-17

## Context

The first Obsidian adapter exposed the audit-oriented vault directly. Raw sources, proposals, receipts, technical identifiers, and orphan nodes made the default graph and file browser correct but difficult for a person to use as a second brain.

## Decision

Generate a human-facing layer under `vault/views/` containing a home page, recent imports, source library, topic navigation, canonical knowledge catalog, deep-review queue, and one readable page per source. Reader pages reuse existing extraction text and provenance; they do not summarize, classify, or promote source material.

The view layer remains disposable. Raw source records and canonical knowledge remain the truth layers. CLI capture, WeChat capture, text capture, daily triage, weekly maintenance, and explicit derived rebuilds refresh these views. The default Obsidian graph hides audit and reader-detail paths and orphan nodes; users may remove the filter when auditing.

## Consequences

- New captures appear immediately in recent imports and the source library.
- Daily and weekly runs deterministically refresh human navigation.
- Canonical and relation changes become visible after the next rebuild without changing their governance.
- Topic navigation uses only explicit tags and domains; it does not invent semantic labels.
- Human readability improves without creating a second truth store or requiring an Obsidian plugin.
