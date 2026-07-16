# ADR 0029: Thin agent entries and rebuildable Obsidian views

- Status: accepted
- Date: 2026-07-16

## Context

Global Memory needs to be usable from Codex, Cursor, Claude, and Obsidian without turning any assistant, editor, plugin, index, or chat history into a competing source of truth. Loading the whole vault wastes context and weakens provenance. Direct agent write-back would bypass the proposal gate.

## Decision

Provide small tool-native instruction files that all point to the same repository protocol and a versioned, bounded Context Pack. Generate Obsidian navigation notes from canonical/proposal state using standard Markdown, YAML frontmatter, and wikilinks. Treat these views as disposable.

Agents write session receipts, not canonical knowledge. A receipt is immutable, is captured as a normal source, and is compiled into the existing proposal/review path. Supported adapters in this milestone are Codex, Cursor, and Claude only.

## Consequences

- There is one shared memory and governance model, with no synchronization between assistant-specific databases.
- Context selection remains inspectable and budgeted.
- Obsidian can browse and link the vault without owning truth or requiring plugins.
- Agent-generated conclusions remain candidates until reviewed.
- Hermes, OpenHuman, MCP, embeddings, automatic background maintenance, and bidirectional Obsidian automation remain out of scope.
