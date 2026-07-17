# Claude entry for Global Memory

This repository is the shared, local-first Global Memory. Before working here:

For routine article import, default to cheap capture followed by `.\\scripts\\gm.ps1 triage <source-id>`. Triage only extracts and quality-checks. Do not compile every article or request per-article approval. Use `--compile-selected` only for important, decision-critical, repeatedly retrieved, or conflicting material; deep verification belongs at use/promotion time.

Use `.\\scripts\\gm.ps1 weekly` for the bounded weekly maintenance loop. It may rebuild derived views and report synthesis eligibility, but it never creates synthesis proposals or canonical writes automatically.

The repository `.mcp.json` configures the provider-neutral `global-memory` read-only MCP server. Prefer its bounded context/search/show/source/status tools for retrieval; it grants no capture, proposal, approval, or canonical-write authority.

1. Read `AGENTS.md`, `vault/INDEX.md`, and the architecture documents it names.
2. Retrieve a bounded task view with `gm context "<question>" --format markdown --token-budget 1200`.
3. Open only the selected pages and their relevant evidence/source links. Do not scan the whole vault by default.
4. Treat `vault/raw/` and canonical Markdown as the truth layers. SQLite indexes, Context Packs, and `vault/views/` are rebuildable derived data.
5. Never write canonical knowledge directly. End a memory-worthy session by writing a UTF-8 Markdown receipt and running:

   `gm receipt create --agent claude --project "<project>" --task "<task>" --from-file <receipt.md>`

   Then route it to review with `gm receipt propose <receipt-id>`. This creates a normal proposal; it does not approve it.

Receipts should contain only durable decisions, verified facts, unresolved questions, changed assumptions, and source references. Exclude chat transcript filler and secrets.

Use `gm maintain` to inspect maintenance state without writes. `gm maintain --rebuild-derived` may refresh SQLite and Obsidian views only; it never authorizes canonical changes.

On Windows PowerShell prefer `.\\scripts\\gm.ps1`; `gm` may resolve to the built-in `Get-Member` alias.
