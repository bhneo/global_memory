# ADR 0031: Read-only provider-neutral MCP boundary

- Status: accepted
- Date: 2026-07-17

## Decision

Global Memory exposes a provider-neutral MCP server over stdio and Streamable HTTP. The first version contains only five bounded read tools: `memory_context`, `memory_search`, `memory_show`, `memory_source`, and `memory_status`.

No MCP tool may capture content, create or approve proposals, compile knowledge, rebuild derived state, delete raw data, or modify canonical Markdown. Tool definitions declare read-only, non-destructive, idempotent annotations. Results preserve path, status, source IDs, evidence boundaries, and truncation.

Local stdio is the default integration for Cursor, Claude Code, Codex-compatible clients, and other desktop assistants. HTTP binds to `127.0.0.1` by default, validates Origin when supplied, caps request bodies, and requires a bearer token whenever bound to a non-loopback address. Public deployment additionally requires TLS and an authentication/tunnel layer appropriate to the client.

## Consequences

Multiple assistants can query one durable memory without receiving canonical write authority. Web ChatGPT still requires a reachable remote MCP endpoint or Secure MCP Tunnel; starting the local HTTP server alone does not expose it to the internet.
