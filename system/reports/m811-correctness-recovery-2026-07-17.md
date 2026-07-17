# M8.1.1 Correctness Recovery Acceptance

## Outcome

- Wrong requalification migration: corrected from the immutable pre-migration backup.
- Original affected Trusted objects: 30.
- Restored as Trusted: 30.
- Restore conflicts / forced restores: 0 / 0.
- False Demotion Events: 0.
- Current Trusted: 30 total; 28 Policy v3-qualified; 2 awaiting requalification; 0 contested.
- Current tiers: 83 Working / 30 Trusted / 1 Canonical.
- Canonical content writes during correction: 0.

The two awaiting objects are `concept_embodied_data_loop` and `concept_perceptual_prediction_bias`. They remain Trusted because the migration may not erase prior acceptance, but Policy v3 qualification is blocked until two genuinely independent logical `work_id` values exist.

## Receipt recovery

- Receipt history: 113 v1 and 189 v2 (302 immutable records).
- Objects with a current valid v2: 105.
- Historical failed attempts: 24. Repeated failures are retained as separate attempt records rather than overwritten.
- Eight current legacy claim objects remain invalid because evidence entailment is missing; each has an explicit failed v2 attempt and Exception.

Receipt reuse now requires schema v2, complete status, current object SHA-256 and the full current fingerprint. The fingerprint covers source-record and Raw hashes, Evidence/extraction identity, logical works, relations, contradictions, memory/receipt schema, consolidator, drift policy and Trusted policy versions.

Real Findings examples:

- Claim: `vault/receipts/consolidation/consolidation-consolidation_109c7958cf4cb5c5fbc2661f.md` records two source-record hashes, two Raw hashes, two Evidence IDs, title-search candidates, related objects, zero contradiction relations, independence counts and zero drift reports.
- Concept: `vault/receipts/consolidation/consolidation-consolidation_fb8da51efa12a2eff4def831.md` records its source/Raw hashes, non-claim Evidence/entailment applicability, 11 duplicate-search candidates, four relation results, independence counts and zero drift reports.

## Governed transaction and gates

Trusted promotion, requalification and support/conflict writes use:

`prepared -> staged -> receipt_completed -> event_logged -> finalized`

Recovery rolls back exact pre-write bytes before Receipt completion. After Receipt completion it retains the new bytes and idempotently finishes the audit event. Final pending recovery journals: 0.

All Canonical evolution types (`support`, `metadata_only`, `refine`, `limit`, `contradict`, `supersede`) leave Canonical bytes unchanged and create an update Proposal; contradictions also create an Exception. Canonical promotion additionally requires Policy v3 qualification, a current v2 Receipt and no unresolved contradiction/high-risk drift.

## Provider target identity

The external provider contract supports `action=create|update`. Updates require stable `target_id` and explicit `change_type`; title similarity is not identity. The portable A -> B -> C fixture used deliberately different B/C titles and the same target ID:

- Support updates: 1.
- Contradiction updates: 1.
- Duplicate claim count: 1.
- Silent Trusted demotions: 0.
- Canonical writes: 0.

Artifact: `artifacts/incremental-evolution.json`.

## Verification

- Full pytest: 170 collected, all passed locally.
- `gm doctor --check-state`: ok; 167 indexed documents; 0 recovery journals.
- `gm lint`: ok; 659 checked documents; 0 errors/warnings.
- `gm raw verify`: ok; 53 sources / 52 unique objects / 0 errors.
- Trust requalification verify: ok; 0 Canonical writes.
- Obsidian/SQLite derived views: rebuilt from current Markdown truth.
- Remote six-job CI: not yet run for M8.1.1; the user plans one unified push. The previous M8 baseline remains green on Ubuntu/Windows x Python 3.11/3.12/3.13.

## Remaining evidence work

- Link the two awaiting Concepts to independent logical works only when the real provenance supports it, then run `gm trust requalify <id>`.
- Recheck evidence entailment for eight failed legacy claims.
- Review the two pre-existing synthesis evidence-link drift warnings.
