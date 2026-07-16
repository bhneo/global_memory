# Claude entry for Global Memory

This repository is the shared, local-first Global Memory. Before working here:

1. Read `AGENTS.md`, `vault/INDEX.md`, and the architecture documents it names.
2. Retrieve a bounded task view with `gm context "<question>" --format markdown --token-budget 1200`.
3. Open only the selected pages and their relevant evidence/source links. Do not scan the whole vault by default.
4. Treat `vault/raw/` and canonical Markdown as the truth layers. SQLite indexes, Context Packs, and `vault/views/` are rebuildable derived data.
5. Never write canonical knowledge directly. End a memory-worthy session by writing a UTF-8 Markdown receipt and running:

   `gm receipt create --agent claude --project "<project>" --task "<task>" --from-file <receipt.md>`

   Then route it to review with `gm receipt propose <receipt-id>`. This creates a normal proposal; it does not approve it.

Receipts should contain only durable decisions, verified facts, unresolved questions, changed assumptions, and source references. Exclude chat transcript filler and secrets.
