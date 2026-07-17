# Agent and Obsidian integration

## M7 write-back contract

Agents may capture, compile and create Working memory without requesting per-item approval. They must preserve raw provenance, candidate hashes, tier, uncertainty and evidence boundaries. They may recommend Trusted/Canonical promotion, but only the user can approve a Canonical promotion card. Read-only MCP remains unchanged and exposes no write authority. Use `consolidate daily`, `consolidate weekly`, `exceptions`, `promotions`, and `trust explain` as described in `MEMORY_CONSOLIDATION.md`.

## Goal

Codex, Cursor, and Claude share one Global Memory without copying the vault into tool-specific memory stores. Each tool gets a thin filesystem entry; the knowledge and governance model remain provider-neutral.

## Read path

Local MCP-capable assistants may use the configured `global-memory` server instead of shelling out directly. Its five tools map to the same bounded read path and expose no write operation; see `docs/MCP_INTEGRATION.md` and ADR 0031.

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
  -> compile audit bundle + Working memory
  -> periodic consolidation -> Trusted
  -> promotion card -> explicit user approval -> Canonical
```

Use:

```text
gm receipt create --agent codex|cursor|claude --project <name> --task <name> --from-file <receipt.md>
gm receipt propose <receipt-id>
```

A receipt is not Trusted or Canonical merely because an agent wrote it. It records a candidate handoff and cannot bypass evidence or promotion checks. Keep durable decisions, validated observations, changed assumptions, unresolved questions, and source references; omit conversation filler and secrets.

Begin each candidate section with an explicit marker such as `Experiment:`, `Decision:`, `Failure:`, `Question:`, or `Claim:`. The deterministic compiler preserves the complete section until the next marker and creates one pending item per section. It does not infer a type from unmarked prose and never approves the result.

## Obsidian

Open the repository's `vault/` directory as an Obsidian vault. Run `gm obsidian build` to generate:

- `vault/INDEX.md`: human home and current overview;
- `vault/views/最近导入.md`, `资料库.md`, and `主题导航.md`: source-oriented browsing;
- `vault/views/知识目录.md` and `待深挖.md`: canonical knowledge and governed work queues;
- `vault/views/readers/`: one readable, provenance-linked page per source;
- `vault/views/Knowledge Catalog.md` and `Review Queues.md`: stable technical compatibility entries.

These files use ordinary Markdown and path-based wikilinks. They are generated views, not a second database or a truth layer. Reader pages reuse existing extraction text and never invent summaries or topics. CLI capture and daily/weekly maintenance refresh them automatically; `gm obsidian build` remains the manual repair command. The default graph hides audit paths and orphan nodes, but the filter can be cleared for an audit. No plugin is required.

## Maintenance

For routine article ingestion, `gm triage [source-id ...] --limit 25` remains the cheapest extraction/quality preparation step. `gm consolidate daily` then compiles prepared sources into Working without per-article approval; expensive verification is deferred until use, conflict or promotion.

Run `gm consolidate weekly` for Working review, Trusted policy, drift audit, exception routing, promotion recommendations and the review-compression digest. It never writes Canonical automatically.

Run `gm maintain` for the normal read-only health and backlog report. It also reports whether generated Obsidian views are missing or stale. Run `gm maintain --rebuild-derived` only when an explicit refresh is wanted; it rebuilds SQLite and all generated Obsidian views, but never raw, proposal, receipt, or canonical content.

On Windows PowerShell, invoke the same commands through `.\\scripts\\gm.ps1` when the bare `gm` name resolves to the built-in `Get-Member` alias.
