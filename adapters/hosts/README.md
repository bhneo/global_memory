# Global Memory host adapters

These fragments connect personal assistants to one shared, governed memory
backend.  Every default fragment starts the read-only launcher through the
ASCII runtime junction:

`C:\Users\bhneo\Desktop\project\global-memory-runtime\scripts\gm-mcp-stdio.ps1`

The read-only gateway exposes:

- `memory_capabilities`
- `memory_context`
- `memory_search`
- `memory_show`
- `memory_source`

`profile=execution` should be paired with `strict_execution=true`.  A blocked
packet is a normal result, not a tool failure.  Raw Source, Input, Annotation,
Reflection and Cognitive Synthesis are never execution-safe.

The trusted launcher `gm-mcp-agent-stdio.ps1` additionally exposes explicit,
idempotent Capture, session, use and feedback signals.  Do not register it as a
global/default server.  Enable it only for a single-user host that can preserve
user consent, stable session identity and user/project isolation.

## Host mapping

| Host | Fragment | Notes |
|---|---|---|
| Codex Desktop/CLI | `codex.config.toml` | Keep the existing explicit personal plugin; MCP is an optional read-only backend. |
| Claude Desktop | `claude-desktop.mcp.json` | Merge the `global-memory` entry into `mcpServers`, then fully restart Claude. |
| Hermes | `hermes.config.yaml` | Merge under `mcp_servers`; the allowlist keeps the server read-only. |
| OpenClaw | `openclaw.mcp-server.json` | Merge `global-memory` under `mcp.servers`; preserve per-peer session isolation. |
| OpenHuman | `openhuman.config.toml` | Merge into its TOML config; it is consumed through the generic MCP bridge. |

Host hooks decide when to retrieve and how to map project/session identity.
Global Memory alone decides truth layer, trust tier, Receipt qualification,
contradictions and execution safety.  Retrieval never records Activation.

For the installed Windows Claude Desktop app, the repository also provides an
idempotent merge installer that preserves the full existing JSON and creates a
timestamped backup before changing it:

```powershell
.\scripts\install-claude-desktop-mcp.ps1
```

The installer registers only the read-only launcher and never stops or restarts
Claude. Fully quit and reopen Claude after installation.
