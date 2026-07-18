# Current State

## M9.0 update (2026-07-18)

M9.0 — Research Signals and Progressive Routing is implemented locally on top of the frozen M8.1.2 trust boundary.

- Append-only Capture Intent, Research Note and Connection Feedback live under `vault/annotations/research/` and are independently indexed.
- Context Pack includes a bounded Route Trace; explicit Project/Domain wins and uncertain matching retains Global fallback.
- Activation events are explicit and local, with rebuildable SQLite aggregates. Default Context and read-only MCP do not write.
- Research Digest and Research Map are deterministic local outputs; research-use metrics remain separate from Trust metrics.
- `consolidate weekly` now admits up to 25 capture-only sources through the
  normal Daily Working gate before Weekly review; `--skip-daily-admission`
  preserves an explicit review-only mode.
- Deterministic compilation now keeps long unstructured articles source-only
  unless they contain explicit typed markers. Weekly surfaces legacy low-quality
  fallback objects as `recompile_or_source_only` findings without silently
  deleting or rewriting them.
- The first real Working-quality migration archived 37 confirmed legacy
  first-paragraph fallback Claims with exact backups and version snapshots;
  three explicit-marker objects were retained and Canonical writes remained 0.
- Seven M9-specific CI acceptance steps were added to the Ubuntu/Windows × Python 3.11–3.13 matrix.
- M8 governance, Canonical gate, Receipt v2 and recovery state machines were not changed.

## Current milestone

M9.0 — Research Signals and Progressive Routing is implemented and locally accepted. M8.1.2 remains the frozen trust foundation: Receipt v2 is bound to the complete current environment, governed writes remain recoverable, and Canonical remains an explicit proposal/approval decision.

## M8.1.2 update (2026-07-17)

- Receipt v2 now fingerprints incoming and outgoing relation state. Earlier receipts remain preserved but are safely stale until an explicit re-consolidation; no real knowledge object was bulk-rewritten to improve metrics.
- Canonical approval is a recoverable multi-file transaction: it keeps exact Trusted/Card pre-images and rolls forward only with a complete `canonical_approved` Receipt v2 bound to final Canonical bytes.
- Receipt check details distinguish execution from validation outcome; only typed evidence may automatically contest a Trusted object. Exploratory qualifications are governance scope, not factual reliability.
- 30 Trusted objects were re-consolidated without modifying their knowledge bodies. The sole Canonical VIA claim remains intentionally receipt-stale because its source-linked evidence entailment is not yet recheckable.
- Promotion consumes semantic Receipt details; `evolve --force-contest` is an explicit, source-bound escalation that creates a must-confirm Exception rather than claiming verification.

## Current architecture

`capture → immutable Raw/Source → bounded triage → Working → real consolidation + hash-bound receipt → narrowly eligible Trusted → promotion card → explicit Canonical approval`.

Memory Tier (`working`, `trusted`, `canonical`, `historical`) is independent from Epistemic Status. Trusted semantic edits create Working Revisions; contradictions retain both evidence sides, mark the object contested and create an Exception; demotions create immutable version and event records.

## Current metrics

Generated from the real vault after the M8.1.1 recovery pass on 2026-07-17:

- 53 sources and 114 governed knowledge objects.
- 83 Working, 30 Trusted and 1 Canonical.
- 28 Trusted are Policy v3-qualified; 2 remain Trusted while awaiting requalification because they do not yet have two independent `work_id` values.
- 302 historical consolidation receipts: 113 v1 and 189 v2; 105 governed objects have a current valid v2, while 24 historical attempts are explicitly failed (including repeated recovery-pass evidence rather than overwritten files).
- 0 promotion candidates, 0 Working Revisions and 0 contested objects at this snapshot.
- 10 open Exceptions: 2 pre-existing synthesis drift reviews and 8 explicit legacy consolidation failures; 2 medium semantic-drift warnings and 0 high-severity drift.
- 0 pending recovery journals after `gm recover`.
- Latest weekly considered 113 objects, produced 0 Trusted promotions, 0 demotions and 0 Canonical writes.

Run `.\scripts\gm.ps1 metrics` or `.\scripts\gm.ps1 status --machine-readable` for current counts; these numbers are a dated acceptance snapshot, not a hand-maintained source of truth.

## CI status

GitHub Actions CI #7 for the prior M8 commit `928404f` passed all six jobs: Ubuntu/Windows × Python 3.11/3.12/3.13. M8.1.1 is fully green locally; its six-job remote matrix remains unverified until the user performs the planned unified push.

## What is working

- M8.1.1 correctness recovery: test-boundary repair, exact Trusted restoration, v1→v2 receipt regeneration, explicit Trusted requalification, five-phase recovery, transactional Trusted support, Canonical evolution gate, real Receipt findings and provider `target_id` updates.

- Immutable raw capture, source/extraction validation and rebuildable SQLite/Obsidian views.
- Real Consolidation Receipts bound to object/source/raw/extraction/work/relation/policy state, with non-empty per-check Findings.
- Explicit support/refine/limit/contradict/supersede/metadata-only evolution semantics.
- Narrow Claim/Concept Trusted promotion; exploratory types are paused by default.
- Safe Trusted revisions, conflict Exceptions, explicit demotion records and Canonical protection.
- Execution/Research/Exploration Context profiles with tier, epistemic and evidence boundaries.
- Idempotent epistemic migration with backup, verification and `legacy_status` preservation.
- Daily/weekly maintenance, semantic drift audit and generated project metrics.

## Known defects

- Eight legacy Agentic-VLA/Play2Perfect claims lack an explicit `evidence_entailment` value. Their v2 attempts and Exceptions correctly remain failed until evidence is rechecked.
- Two restored Concepts remain Trusted but awaiting Policy v3 requalification because their captures have not yet been linked to two independent logical works. They are excluded from strict execution and Canonical promotion.
- Two M6 synthesis objects do not yet carry source-level evidence links in the expected structure. Drift audit reports them as medium-severity human-review items and does not rewrite them.
- PowerShell may resolve bare `gm` as `Get-Member`; use `.\scripts\gm.ps1`.
- `ci_status` is unavailable from an offline local metrics run; GitHub Actions is the authoritative portable CI result.

## Active exceptions

Two open synthesis-drift Exceptions from the real weekly pass. Estimated review time is six minutes. There are no Canonical exceptions and no high-severity drift findings.

## Next concrete task

Link the two awaiting Concepts to genuinely independent logical works only when evidence supports that identity, then re-run `gm trust requalify <id>`. Review the eight failed legacy receipts and two synthesis evidence-link warnings without bulk-upgrading them merely to improve metrics.

## Do not do yet

Do not add embeddings, a vector/graph database, a new MCP write surface, browser ingestion, a Web UI, multi-Agent orchestration or automatic Canonical writes. M8 should first accumulate real usage evidence and threshold calibration.
