# Public engine and private Vault boundary

The formal public Galois distribution is built only from the explicit
allowlist in `release/release-manifest.json`. `.gitignore` is not a release or
privacy boundary. The builder rejects Vault, Raw, system, data, artifacts, and
unknown top-level content; it writes only a new release directory.

## What ships

- Engine, protocols, adapters, tests, schemas and host templates
- Human-facing documentation that describes the **current** system
  (`README`, `docs/ARCHITECTURE`, `VISION`, `PRINCIPLES`, integration guides, …)
- Optional synthetic fixtures for demos
  (`release/synthetic_vault.yaml` and related)

## What does not ship

- Any user's live vault (Sources, Inputs, Reflections, Syntheses, knowledge,
  derived indexes, local credentials)
- This project's research directions file and other private operating state
  (`docs/RESEARCH_DIRECTIONS.md`, `PROJECT_STATE.md`, agent entry stubs, …)
- **Historical decision records** under `docs/decisions/` (ADRs). They remain
  useful inside the evaluation / development repository as an audit trail of
  internal iteration; they are not part of the public product surface.

`release/synthetic_vault.yaml` is intentionally synthetic and supports public
demos without exporting a user's research corpus. Run
`python scripts/audit_release_boundary.py --history` before a public release.
It reports only: it never deletes data or rewrites Git history. A separate,
owner-approved cleanup is required for any historical exposure.
