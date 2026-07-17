# Global Memory read-only MCP

## Tools

| Tool | Purpose |
|---|---|
| `memory_context` | Build a bounded, provenance-preserving Context Pack |
| `memory_search` | Search canonical knowledge and captured sources |
| `memory_show` | Read one object by stable ID |
| `memory_source` | Read a source record and an already-existing extraction |
| `memory_status` | Inspect capture-only, review, evidence, receipt, and follow-up inventory |

All tools are read-only. Retrieval never means approval.

## Local clients

Cursor uses `.cursor/mcp.json`; Claude Code and compatible clients can use `.mcp.json`. Both launch:

```powershell
.\scripts\gm-mcp-stdio.ps1
```

Restart the client after adding or changing MCP configuration. The server writes only JSON-RPC messages to stdout.

## Local HTTP acceptance

```powershell
.\scripts\gm.ps1 mcp http --host 127.0.0.1 --port 18765 --allowed-origin https://chatgpt.com
```

The endpoint is `http://127.0.0.1:18765/mcp`. This is local-only and is not directly reachable by ChatGPT web.

## Remote deployment boundary

Set a high-entropy secret in `GM_MCP_TOKEN`, terminate TLS in a trusted reverse proxy or tunnel, bind only within the protected runtime, and configure exact allowed origins. Non-loopback startup is rejected when the configured token environment variable is empty.

ChatGPT web requires a reachable remote MCP endpoint. For a private machine or private network, use Secure MCP Tunnel or an equivalent authenticated deployment; do not expose the local port directly. Workspace plan, developer-mode, authentication, and app approval requirements still apply.

This repository does not yet install or operate the tunnel, issue OAuth credentials, or publish a ChatGPT app. Those are deployment operations, not local knowledge-store behavior.
