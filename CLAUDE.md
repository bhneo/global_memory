# Claude entry for Global Memory

This repository is the shared, local-first Global Memory. Before working here:

For routine article import, default to cheap capture and triage, then let `.\\scripts\\gm.ps1 consolidate daily` create Working memory without per-article approval. Deep verification belongs at use, conflict, or promotion time.

Use `.\\scripts\\gm.ps1 consolidate weekly` for Working review, Trusted policy, drift/exceptions and promotion recommendations. It never writes Canonical automatically.

The repository `.mcp.json` configures the provider-neutral read-only Agent Memory Gateway. Prefer its bounded context/search/show/source tools for retrieval; it grants no capture, compile, proposal, approval, Trusted, or Canonical authority. Use retrieved memory silently and omit MCP/storage/route details from ordinary answers.

1. Read `AGENTS.md`, `vault/INDEX.md`, and the architecture documents it names.
2. Retrieve a bounded task view with `gm context "<question>" --format markdown --token-budget 1200`.
3. Open only the selected pages and their relevant evidence/source links. Do not scan the whole vault by default.
4. Treat `vault/raw/` and canonical Markdown as the truth layers. SQLite indexes, Context Packs, and `vault/views/` are rebuildable derived data.
5. Never write canonical knowledge directly. End a memory-worthy session by writing a UTF-8 Markdown receipt and running:

   `gm receipt create --agent claude --project "<project>" --task "<task>" --from-file <receipt.md>`

   Then compile the receipt into auditable Working memory. Only an explicitly approved Trusted promotion card may enter Canonical.

Receipts should contain only durable decisions, verified facts, unresolved questions, changed assumptions, and source references. Exclude chat transcript filler and secrets.

Use `gm maintain` to inspect maintenance state without writes. `gm maintain --rebuild-derived` may refresh SQLite and Obsidian views only; it never authorizes canonical changes.

On Windows PowerShell prefer `.\\scripts\\gm.ps1`; `gm` may resolve to the built-in `Get-Member` alias.
