# Memory consolidation and promotion governance

## Normal flow

```text
capture -> immutable source -> compile -> Working
Working -> daily/weekly consolidation -> Trusted
Trusted -> promotion card -> explicit user approval -> Canonical
```

Working is intentionally cheap: it is searchable, readable in Obsidian and available to research/exploration Context Packs, but its status and provenance remain visible. Trusted means the object passed a type-specific policy; it does not mean universal truth. Canonical means the user chose to keep it as a scarce stable commitment.

## Commands

```powershell
.\scripts\gm.ps1 consolidate daily --limit 25
.\scripts\gm.ps1 consolidate weekly
.\scripts\gm.ps1 audit drift
.\scripts\gm.ps1 exceptions
.\scripts\gm.ps1 trust explain <object-id>
.\scripts\gm.ps1 promote <object-id> --to trusted --reason "manual judgement"
.\scripts\gm.ps1 promote <object-id> --to canonical --reason "high-impact durable memory"
.\scripts\gm.ps1 promotions
.\scripts\gm.ps1 promotion approve <promotion-id> --lock
```

`promote --to canonical` only creates a review card. The final command is the sole normal CLI path into Canonical.

## Legacy migration

```powershell
.\scripts\gm.ps1 migrate proposal-gate-to-promotion --dry-run
.\scripts\gm.ps1 migrate proposal-gate-to-promotion
.\scripts\gm.ps1 migrate proposal-gate-to-promotion --verify
```

Apply creates `data/backups/promotion-migration-*` before changing proposal decisions. Rejected, approved and superseded records remain intact. Invalid candidates enter the exception queue; existing Canonical files are untouched.

## Context Pack profiles

- `research`: may include Working, but ranks Trusted and Canonical higher.
- `exploration`: broad access to Working/Trusted/Canonical.
- `execution`: defaults to stable tiers; Working is limited to questions and tensions.
- Explicit `--statuses` is an expert override and never hides the returned status.

## Obsidian

`gm obsidian build`, capture commands, consolidation and derived maintenance rebuild the human views. `记忆层级`, `例外队列`, `晋升队列` and `每周整合` are generated views, not additional truth stores.
