# ADR 0062: Galois Is the Only Public Command and Host Identity

- Status: accepted
- Date: 2026-08-01

## Decision

All current user instructions, AI-assistant bootstrap instructions, examples,
host registrations and generated user-facing command recipes use `galois`.
Windows users use `.\scripts\galois.ps1`; MCP hosts register the server as
`galois`, whose negotiated server name is `galois-agent-gateway`.

The previous short CLI and launcher names remain only as deprecated migration
shims so existing local automation does not fail abruptly. They are excluded
from current documentation and new configurations. Historical ADRs, immutable
artifacts, storage identifiers and the Python import package remain unchanged
where renaming would damage auditability or compatibility. The internal module
and environment names used by stdio transport are not public commands.

Assistant integration is governed by the machine-readable
`adapters/hosts/galois.mcp-manifest.json`. An assistant must discover the real
repository, Python runtime, host version and configuration path; back up and
merge rather than replace configuration; keep the default gateway read-only;
restart the host when required; and validate the live server through
capabilities, the exact five-tool read surface and a bounded Chinese Context
query. Static configuration or subprocess startup alone is not acceptance.

The exact-five rule applies to the server-level MCP `tools/list` surface.
Host-visible names may be prefixed or wrapped when the host architecture
requires it, but the mapping must be one-to-one and must not expose a write
tool. The reviewed templates are machine-path-neutral Windows templates;
Windows is the live-validated onboarding platform, not an implicit claim of
completed cross-platform support.

OpenHuman is conditional because releases may expose MCP through either a
static TOML bridge or a dynamic MCP Registry. Its integration is complete only
when the surface used by the installed build can reach the `galois` server and
maps to the five required tools.

## Consequences

Users can hand the README to an assistant without translating product names,
machine paths or acceptance criteria. New installations have one stable public
vocabulary. Existing local scripts continue to run during migration, while
future documentation cannot silently regress to the deprecated command.

The compatibility boundary is explicit: a later release may rename the Python
package or persisted identifiers only through a separate migration with tests,
rollback and audit-preservation rules.
