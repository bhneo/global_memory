# Galois Agent Gateway

The gateway gives local Agents bounded memory without turning storage and
maintenance mechanics into user-facing report content. Reads return a sanitized
Evidence Packet; full Context Pack diagnostics remain an operator-only CLI
surface.

## Tools

| Tool | Purpose | Authority |
|---|---|---|
| `memory_capabilities` | Negotiate contract versions and exact write scopes | Read-only |
| `memory_context` | Retrieve bounded, connected evidence for a question | Read-only |
| `memory_search` | Find candidate evidence objects | Read-only |
| `memory_show` | Read one evidence object by lookup reference | Read-only |
| `memory_source` | Read source text and an existing extraction | Read-only |
| `memory_capture` | Save explicitly requested user text as Source + Input | Capture-only, opt-in |
| `memory_session_record` | Save bounded goal/result/lesson as Source + Input | Session scope, opt-in |
| `memory_use_record` | Append actual-use Activation (never retrieval) | Use scope, opt-in |
| `memory_feedback_record` | Save explicit connection-value feedback | user_annotation, opt-in |

The five read tools omit local paths, hashes, route traces, ranking diagnostics,
SQLite details and maintenance queues. They retain tier/status, epistemic status,
confidence, authority, evidence coverage/entailment, contradictions, execution
safety, bounded content and source provenance.

Gateway contract v1 uses one `EvidenceItem` shape across context, search, show
and source reads. Receipt state/currentness, policy qualification, qualification
scope/failures, last consolidation, contradiction blockers and execution safety
remain machine-readable. Evidence Packet v2 reports
`ready|partial|insufficient_evidence|blocked`. For an execution decision, call
`memory_context` with `profile=execution` and `strict_execution=true`; excluded
high-relevance objects become structured blockers instead of disappearing.

`memory_capture` is available only when the server starts with the `capture`
write scope (`--allow-capture` remains a compatibility alias). Its request must include `confirmed: true`, meaning the user
explicitly asked to remember/save the supplied text. It runs recovery first and
stops on a blocked journal. It accepts no URL or file path, performs no network
fetch, and always reports zero Working, Trusted and Canonical writes.

Session/use/feedback tools appear only under their corresponding server-side
write scopes. Every call requires an explicit authorization envelope, a
provider-neutral actor, a session reference and an idempotency key. Session
records stop at Source/Input, use records are trust-orthogonal Activation, and
feedback is `truth_layer=user_annotation` with `execution_safe=false`. None can
write Trusted or Canonical.

## Local clients

The repository `.mcp.json` and `.cursor/mcp.json` use the strictly read-only
launcher:

```powershell
.\scripts\galois-mcp-stdio.ps1
```

For an explicitly trusted single-user client that can preserve consent and
session identity, use:

```powershell
.\scripts\galois-mcp-agent-stdio.ps1
```

It enables only `capture`, `session`, `use`, and `feedback`. It does not enable
Receipt compilation, Working writes, Trusted writes or Canonical writes. Host
configuration fragments for Codex, Claude Desktop, Hermes, OpenClaw and
OpenHuman live in `adapters/hosts/`; they all default to the read-only launcher.

Restart the client after changing MCP configuration. The server writes only
JSON-RPC messages to stdout; diagnostics go to stderr.

## Host integration contract

Read `adapters/hosts/galois.mcp-manifest.json` before editing any assistant
configuration. Host fragments are machine-path-neutral Windows templates; an
assistant must discover and replace the runtime variables, preserve unrelated
configuration, restart the host when required, then validate the live server
with `memory_capabilities` and a Chinese Context query. The server-level
`tools/list` result must contain exactly the five read tools. A host may prefix
or wrap those names only through a one-to-one mapping that adds no write tools.
Static configuration is not acceptance evidence. OpenHuman may use either its
static TOML bridge or a dynamic MCP Registry, so the installed build's actual
surface must be verified live.

## Delivery contract

Use retrieved knowledge silently as background. In ordinary answers, do not
mention Galois, MCP, storage/index implementation, paths, internal IDs,
recovery, receipts, route traces or tool calls. These details are appropriate
only when the user explicitly asks for an audit or diagnostic report.

## Local HTTP acceptance

```powershell
.\scripts\galois.ps1 mcp http --host 127.0.0.1 --port 18765 --allowed-origin https://chatgpt.com
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
