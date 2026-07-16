# Agent and Obsidian integration

## Goal

Codex, Cursor, and Claude share one Global Memory without copying the vault into tool-specific memory stores. Each tool gets a thin filesystem entry; the knowledge and governance model remain provider-neutral.

## Read path

```text
AGENTS.md / CLAUDE.md / .cursor rule
  -> vault/INDEX.md
  -> gm context <question> --format markdown
  -> selected canonical/source pages
  -> evidence and immutable raw when verification is needed
```

The Context Pack is a temporary, versioned read-only contract. It is bounded by query, profiles, filters, relation expansion, and token budget. It must preserve truth layer, status, file path, source IDs, evidence/verification fields, selection reason, and truncation information. It never promotes a retrieved statement into fact.

## Write-back path

```text
agent session
  -> concise receipt in vault/receipts/
  -> immutable raw/source capture
  -> normal compile proposal
  -> inspect/diff/review
  -> canonical only after the existing gate
```

Use:

```text
gm receipt create --agent codex|cursor|claude --project <name> --task <name> --from-file <receipt.md>
gm receipt propose <receipt-id>
```

A receipt is not memory merely because an agent wrote it. It records a candidate handoff and cannot bypass evidence checks or approval. Keep durable decisions, validated observations, changed assumptions, unresolved questions, and source references; omit conversation filler and secrets.

## Obsidian

Open the repository's `vault/` directory as an Obsidian vault. Run `gm obsidian build` to generate:

- `vault/INDEX.md`: stable home and protocol;
- `vault/views/Knowledge Catalog.md`: links grouped by knowledge-object type;
- `vault/views/Review Queues.md`: proposals, weak evidence, and stale/historical items.

These files use ordinary Markdown, YAML frontmatter, and path-based wikilinks. They are generated navigation views, not a second database or a truth layer. Rebuild them whenever canonical/proposal state changes. Personal Obsidian workspace state and plugins are intentionally not required or committed.

## Maintenance

Run `gm maintain` for the normal read-only health and backlog report. It also reports whether generated Obsidian views are missing or stale. Run `gm maintain --rebuild-derived` only when an explicit refresh is wanted; it rebuilds SQLite and the three Obsidian notes, but never raw, proposal, receipt, or canonical content.

On Windows PowerShell, invoke the same commands through `.\\scripts\\gm.ps1` when the bare `gm` name resolves to the built-in `Get-Member` alias.
