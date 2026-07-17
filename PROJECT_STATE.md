# Current State

## Current milestone

M8 — Trustworthy Consolidation and Incremental Knowledge Evolution is implemented and locally accepted. Working may evolve automatically; Trusted changes are versioned and receipt-backed; Canonical remains an explicit user decision.

## Current architecture

`capture → immutable Raw/Source → bounded triage → Working → real consolidation + hash-bound receipt → narrowly eligible Trusted → promotion card → explicit Canonical approval`.

Memory Tier (`working`, `trusted`, `canonical`, `historical`) is independent from Epistemic Status. Trusted semantic edits create Working Revisions; contradictions retain both evidence sides, mark the object contested and create an Exception; demotions create immutable version and event records.

## Current metrics

Generated from the real vault on 2026-07-17:

- 53 sources and 114 governed knowledge objects.
- 83 Working, 30 Trusted and 1 Canonical.
- 113 consolidation receipts: 105 complete and 8 explicitly failed.
- 0 promotion candidates, 0 Working Revisions and 0 contested objects at this snapshot.
- 2 open Exceptions and 2 medium semantic-drift warnings; 0 high-severity drift.
- Latest weekly considered 113 objects, produced 0 Trusted promotions, 0 demotions and 0 Canonical writes.

Run `.\scripts\gm.ps1 metrics` or `.\scripts\gm.ps1 status --machine-readable` for current counts; these numbers are a dated acceptance snapshot, not a hand-maintained source of truth.

## CI status

GitHub Actions CI #7 for M8 commit `928404f` passed all six jobs: Ubuntu/Windows × Python 3.11/3.12/3.13. Each job ran pytest, doctor, schema/state/raw checks, migrations, historical/current/M8 governance acceptance, promotion, weekly, A→B→C evolution, drift and three-profile Context validation.

## What is working

- M8.1 Trust Hardening（本地待推送）：Receipt v2 fingerprint、weekly high-drift exception、显式增量 change classification、provider-driven A→B→C、strict execution context、Trusted promotion recovery journal。

- Immutable raw capture, source/extraction validation and rebuildable SQLite/Obsidian views.
- Real Consolidation Receipts bound to the current object and source hashes.
- Explicit support/refine/limit/contradict/supersede/metadata-only evolution semantics.
- Narrow Claim/Concept Trusted promotion; exploratory types are paused by default.
- Safe Trusted revisions, conflict Exceptions, explicit demotion records and Canonical protection.
- Execution/Research/Exploration Context profiles with tier, epistemic and evidence boundaries.
- Idempotent epistemic migration with backup, verification and `legacy_status` preservation.
- Daily/weekly maintenance, semantic drift audit and generated project metrics.

## Known defects

- Eight legacy Agentic-VLA claims lack an explicit `evidence_entailment` value. Their receipts correctly fail and promotion remains blocked until the evidence is rechecked.
- Two M6 synthesis objects do not yet carry source-level evidence links in the expected structure. Drift audit reports them as medium-severity human-review items and does not rewrite them.
- PowerShell may resolve bare `gm` as `Get-Member`; use `.\scripts\gm.ps1`.
- `ci_status` is unavailable from an offline local metrics run; GitHub Actions is the authoritative portable CI result.

## Active exceptions

Two open synthesis-drift Exceptions from the real weekly pass. Estimated review time is six minutes. There are no Canonical exceptions and no high-severity drift findings.

## Next concrete task

Review the eight failed legacy receipts as evidence is actually reused, then resolve the two synthesis evidence-link warnings. Do not bulk-upgrade them merely to improve metrics.

## Do not do yet

Do not add embeddings, a vector/graph database, a new MCP write surface, browser ingestion, a Web UI, multi-Agent orchestration or automatic Canonical writes. M8 should first accumulate real usage evidence and threshold calibration.
