# Galois host adapters

This directory is an AI-executable integration kit for connecting an existing
assistant to Galois. The JSON/TOML/YAML files are templates, not machine-specific
drop-ins: the assistant must replace `{{GALOIS_PYTHON}}` and `{{GALOIS_ROOT}}`
with absolute paths discovered on the user's machine.

Read [`galois.mcp-manifest.json`](galois.mcp-manifest.json) first. It is the
machine-readable contract for the server identity, transport, exact server-level
read-only tool set, profiles, host status and acceptance checks.

These are machine-path-neutral **Windows** templates. Windows is the currently
live-validated onboarding path; macOS and Linux clients may use the same stdio
contract, but their setup is not yet claimed as validated here.

## Required assistant workflow

1. Resolve the repository root from this README; do not guess or create an
   ASCII junction.
2. Resolve a Python 3.11-3.13 executable that imports the checked-out package.
   Prefer `GALOIS_PYTHON`, then the active environment's `python`.
3. Detect the operating system, assistant name, version and actual MCP
   configuration surface. Do not assume the sample path or schema matches the
   installed build. Stop with a concrete compatibility gap on an unvalidated OS.
4. Prefer the host's managed MCP command or Registry. Otherwise back up and
   merge the corresponding template. Preserve unrelated servers, tools,
   credentials and settings. Register the server as `galois`.
5. Keep the default connection read-only. Do not add write scopes merely to
   make a smoke test pass.
6. Fully restart the host when its MCP registry is process-scoped.
7. Prove the live connection with `memory_capabilities`, then confirm that the
   server-level `tools/list` result is exactly the five tools below. Finally run
   one bounded Chinese `memory_context` probe. A host may prefix or wrap those
   names, but its mapping must remain one-to-one and expose no write tools.

Static config, a healthy registry, or a successful subprocess launch is not
proof that the assistant can call the live server.

## Read-only server surface

- `memory_capabilities`
- `memory_context`
- `memory_search`
- `memory_show`
- `memory_source`

For execution decisions, use `profile=execution` with
`strict_execution=true`. A blocked or insufficient packet is a valid governed
result. Raw Source, Input, Annotation, Reflection and Cognitive Synthesis are
never execution-safe.

Hermes commonly prefixes the names with its MCP server identifier. OpenHuman's
static bridge can expose the server through `mcp_list_tools` and
`mcp_call_tool`. Those host-visible names do not change the server contract.

The opt-in launcher `galois-mcp-agent-stdio.ps1` additionally exposes explicit,
idempotent Capture, session, use and feedback signals. Never register it as a
global/default server. It is only for a single-user host that can preserve
explicit consent, stable session identity and project isolation.

## Host mapping

| Host | Template / installer | Acceptance boundary |
|---|---|---|
| Codex Desktop/CLI | `codex.config.toml` | Merge under `mcp_servers.galois`; restart and call capabilities. |
| Claude Desktop | `claude-desktop.mcp.json` or `..\..\scripts\install-galois-claude-desktop.ps1` | Fully quit and reopen Claude, then call capabilities. |
| Hermes | `hermes.config.yaml` | Preserve the five-tool allowlist; validate Chinese queries. |
| OpenClaw | `openclaw.mcp-server.json` | Prefer `openclaw mcp add`, `set` or `configure` (or the Control UI); use the JSON as the reviewed server fragment, then run `status`/`probe`. |
| OpenHuman | `openhuman.config.toml` | Conditional dual path: some builds use the static TOML bridge, others a dynamic SQLite-backed Registry. Verify whichever surface the installed build actually exposes. |

Host hooks decide when to retrieve and how to map project/session identity.
Galois decides truth layer, trust tier, Receipt qualification, contradictions
and execution safety. A read never records Activation.

## Claude Desktop installer

The Windows installer is self-locating, resolves Python dynamically, preserves
the full existing JSON, removes the deprecated server key, and creates a
timestamped backup before writing:

```powershell
.\scripts\install-galois-claude-desktop.ps1
```

It never stops or restarts Claude. Fully quit and reopen Claude after the merge.

## Bounded retrieval behavior

`budget_exhausted=true` means the requested Context Pack reached its explicit
budget. It is not a server failure and does not authorize unbounded follow-up
queries. Narrow the question or ask the user before materially expanding the
retrieval scope. Do not fall back to another assistant's native memory tools
when the `galois` server is missing; report the missing integration instead.
