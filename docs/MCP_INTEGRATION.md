# Global Memory Agent Gateway

The gateway gives local Agents bounded memory without turning storage and
maintenance mechanics into user-facing report content. Reads return a sanitized
Evidence Packet; full Context Pack diagnostics remain an operator-only CLI
surface.

## Tools

| Tool | Purpose | Authority |
|---|---|---|
| `memory_context` | Retrieve bounded, connected evidence for a question | Read-only |
| `memory_search` | Find candidate evidence objects | Read-only |
| `memory_show` | Read one evidence object by lookup reference | Read-only |
| `memory_source` | Read source text and an existing extraction | Read-only |
| `memory_capture` | Save explicitly requested user text as Source + Input | Capture-only, opt-in |

The first four tools omit local paths, hashes, route traces, ranking diagnostics,
SQLite details and maintenance queues. They retain tier/status, epistemic status,
confidence, authority, evidence coverage/entailment, contradictions, execution
safety, bounded content and source provenance.

`memory_capture` is available only when the server starts with
`--allow-capture`. Its request must include `confirmed: true`, meaning the user
explicitly asked to remember/save the supplied text. It runs recovery first and
stops on a blocked journal. It accepts no URL or file path, performs no network
fetch, and always reports zero Working, Trusted and Canonical writes.

## Local clients

The repository `.mcp.json` and `.cursor/mcp.json` use the strictly read-only
launcher:

```powershell
.\scripts\gm-mcp-stdio.ps1
```

For an explicitly trusted non-Desktop client that needs Capture-only intake,
use:

```powershell
.\scripts\gm-mcp-agent-stdio.ps1
```

Restart the client after changing MCP configuration. The server writes only
JSON-RPC messages to stdout; diagnostics go to stderr.

## Codex Desktop explicit plugin

The personal `global-memory` plugin contains `global-memory-read` and
`global-memory-capture`. Both set `allow_implicit_invocation: false` and call a
local gateway script only after the user selects the plugin/skill. The plugin
does not bundle or register an MCP server, so unrelated Desktop tasks do not
receive an always-on memory tool surface.

## Delivery contract

Use retrieved knowledge silently as background. In ordinary answers, do not
mention Global Memory, MCP, storage/index implementation, paths, internal IDs,
recovery, receipts, route traces or tool calls. These details are appropriate
only when the user explicitly asks for an audit or diagnostic report.

## Local HTTP acceptance

```powershell
.\scripts\gm.ps1 mcp http --host 127.0.0.1 --port 18765 --allowed-origin https://chatgpt.com
```

Add `--allow-capture` only for an explicitly trusted client. The endpoint is
`http://127.0.0.1:18765/mcp`; local-only HTTP is not directly reachable by a web
client.

## Remote deployment boundary

Set a high-entropy secret in `GM_MCP_TOKEN`, terminate TLS in a trusted reverse
proxy or tunnel, bind only within the protected runtime, and configure exact
allowed origins. Non-loopback startup is rejected when the token is empty.
Capture should remain disabled for remote deployments unless authentication,
client identity and explicit-consent behavior have been reviewed.

This repository does not install a tunnel, issue OAuth credentials, or publish
a hosted app. Those are deployment operations, not local knowledge-store
behavior.
