# Public engine and private Vault boundary

The formal public Galois distribution is built only from the explicit
allowlist in `release/release-manifest.json`. `.gitignore` is not a release or
privacy boundary. The builder rejects Vault, Raw, system, data, artifacts, and
unknown top-level content; it writes only a new release directory.

`release/synthetic_vault.yaml` is intentionally synthetic and supports public
demos without exporting a user's research corpus. Run
`python scripts/audit_release_boundary.py --history` before a public release.
It reports only: it never deletes data or rewrites Git history. A separate,
owner-approved cleanup is required for any historical exposure.
