# ADR 0059: Agent Memory Gateway Uses Evidence Packets and Capture-only Intake

- Status: accepted
- Date: 2026-07-20
- Supersedes: ADR 0031 only for the explicitly enabled Capture-only tool and
  the agent-facing response shape

## Decision

Global Memory exposes an Agent Memory Gateway over the existing MCP transports.
The default server remains read-only. When startup explicitly includes
`--allow-capture`, one additional tool, `memory_capture`, may accept bounded
user-supplied text only after the calling Agent affirms that the user explicitly
asked to remember or save it.

Capture-only intake runs repository recovery first and stops if recovery is
blocked. It writes immutable Raw/Source plus one typed Input Episode queued for
Reflection. It cannot compile, create or update Working, promote Trusted,
approve Canonical, rebuild human views, restore Historical, or execute an
external fetch. Repeated identical text is idempotent.

Agent-facing reads return a sanitized Evidence Packet. The packet retains title,
type, tier/status, epistemic status, confidence, source authority,
evidence coverage/entailment, contradictions, execution safety, bounded content
and public source references. It excludes filesystem paths, object hashes,
route traces, selection diagnostics, SQLite details, maintenance inventories,
recovery state and administrative commands. Full Context Pack diagnostics remain
available to operators through the local CLI, not through the Agent Gateway.

The MCP initialization contract instructs Agents to use memory silently as
background context. Ordinary user-facing answers must not narrate the memory
system, MCP calls, internal IDs or operational details unless the user asks for
an audit or diagnostic report.

## Consequences

Ordinary chat windows can retrieve consistent local context without leaking
storage mechanics into deliverables. Users can explicitly save text from those
windows without granting semantic or trust authority. Capture is still not
knowledge: later Reflection, semantic distillation, consolidation and promotion
retain their existing boundaries. Repository MCP configurations use the
read-only launcher. Codex Desktop uses a personal plugin whose read and capture
skills both prohibit implicit invocation; the plugin registers no always-on MCP
server. The Capture-only launcher remains available only for explicitly trusted
non-Desktop clients.
