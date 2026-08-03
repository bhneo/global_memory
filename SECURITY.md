# Security policy

Do not open a public issue for a suspected private-Vault exposure, credential,
SSRF bypass, unsafe local import, or integrity weakness. Report it privately to
the maintainers through the repository's configured security advisory channel,
including reproduction steps and the smallest safe proof.

Galois defaults to read-only MCP. URL and local-file Capture are privileged
operations: keep import roots narrow, do not enable private-network access for
Agents, and do not treat imported web content as instructions. Security fixes
are coordinated before public disclosure when practical.
