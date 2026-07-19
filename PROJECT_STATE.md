# Current State

## M9.1 Cognitive Consolidation update (2026-07-19)

- Typed Input Episodes now unify article, paper, GitHub, conversation, idea,
  experiment, meeting and third-party Agent Session capture under
  `vault/inputs/`, while immutable Source remains authoritative.
- Quality-gated Reflection objects under `vault/reflections/` record cognitive
  value, changed beliefs, surprises, bounded structural connections, conflicts,
  questions and possible mechanisms. Reflection is explicitly non-factual,
  carries no Memory Tier/Epistemic Status, does not enter Evidence/Receipt, and
  is never execution-safe.
- Provider-neutral `dream daily` consumes at most five current queue items,
  prevalidates the complete artifact, rejects Daily Hypothesis/Analogy/Synthesis,
  resumes an identical immutable Reflection after interruption, attaches
  `reflection_context` to explicit semantic items, and compiles them into
  Working only.
- Provider-neutral `dream weekly` creates non-factual Cognitive Synthesis from
  multiple Reflections and existing Concepts. Connections require a shared
  mechanism, boundary and difference; hypothesis candidates require supporting
  Reflections/Sources, counterarguments, a falsifier and a possible experiment.
- Research/Exploration Context can return labeled Reflections and Cognitive
  Synthesis. Execution Context excludes both. The existing read-only MCP gains
  this behavior through the shared Context Pack without a new write surface.
- M8.1.2 governance is unchanged: model artifacts never write Trusted or
  Canonical, both Dream pipelines assert zero Canonical writes, and third-party
  Agents submit Experience rather than Knowledge.
- Local regression status: 230 tests pass. GitHub's Ubuntu/Windows x Python
  3.11-3.13 matrix has an explicit M9.1 acceptance step but is not yet verified
  remotely for this uncommitted change set.

## Operational status

The M9.1 code, synthetic end-to-end scenario and first bounded real-Vault pilot
are locally accepted. Five selected recent Sources were explicitly transitioned
into five Input Episodes, read from their hash-bound Extractions, distilled into
five quality-gated Reflections and five new Working Concepts, then integrated
into one non-factual Cognitive Synthesis with one falsifiable hypothesis. The
pilot wrote 0 Trusted and 0 Canonical objects. Historical Sources were not bulk
migrated; bounded `inputs --backfill` remains explicit. New CLI captures enter
the Input layer. The Codex Daily/Weekly tasks now explicitly produce and apply
Dream JSON artifacts; deterministic `consolidate daily/weekly` remains a
separate governance stage and does not invoke a model.

## Current milestone

M9.1 — Cognitive Consolidation is implemented and accepted through synthetic
and bounded real-Input pilots on the frozen M8.1.2 trust boundary. Remote matrix
CI remains pending the user's unified push.

## M9.0.1 Quality Closure update (2026-07-18)

- Daily/Weekly now have an explicit Agent semantic-distillation stage. The
  read-only `gm semantic queue` exposes bounded Source-only material; Agent
  JSON Bundles may add validated typed relations and still enter Working only.
  Automatic Web/PDF article text can no longer trigger deterministic knowledge
  creation merely because a paper contains `Question:` or similar headings.
- Semantic bundles can link explicitly named objects created in the same batch,
  add bilingual aliases through governed `metadata_only` updates, and defer
  Obsidian work with `compile --skip-obsidian` until one final rebuild.
- Context Pack broad-query expansion now evaluates active lexical knowledge
  independently from archived hits and route seeds, expands multiple bounded
  terms, and rewards multi-term governed matches over long raw-source bodies.

- Derived extraction now replaces unpaired Unicode surrogates with U+FFFD and
  records a warning, so malformed extractor output cannot block bounded Daily
  admission; immutable Raw remains unchanged.
- Working-quality migration Verify/Restore now compares exact post-migration
  bytes, binds snapshots/events/source Raw and Canonical hashes, blocks later
  Working/Canonical successors, and resumes incomplete manifests under the same
  migration ID. The original 37-object manifest was explicitly safety-baselined;
  this is a forward-looking protection, not a retrospective claim.
- Annotation consumers validate supersession over the complete graph before
  filtering by target, so multi-target corrections remain queryable.

- The default `knowledge` Obsidian Graph now exposes active Working, Trusted,
  and Canonical semantic objects and their validated typed relations. Raw Source
  nodes remain in library/reader views and the explicit `--graph-profile all`
  audit graph; `--graph-profile trusted` keeps the stricter trust-only view.
  This is a disposable projection and changes no trust tier.

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

## Previous milestone

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

<!-- GENERATED_METRICS_START -->
- Generated at: 2026-07-19T17:27:47+08:00
- Working / Trusted / Canonical / Historical: 106 / 30 / 1 / 43
- Source-only compile records / sources / historical objects: 42 / 42 / 43
- Trusted current policy / receipt / qualified: 28 / 30 / 23
- Trusted awaiting / stale receipt / contested / high-risk drift: 2 / 0 / 0 / 0
- Trusted factual / exploration; Canonical with current Receipt: 11 / 19 / 0
- Contested: 0
- Working revisions: 0
- Open exceptions: 12
- Promotion candidates: 0
- Consolidation receipts / failed: 557 / 66
- Receipt schema versions: {'v1': 113, 'v2': 444}
- Objects with current valid Receipt v2: 120
- Pending recovery journals: 0
- Drift warnings / high severity: 4 / 2
- Corpus sources / knowledge objects: 107 / 180
- Research annotations total / active / superseded: 0 / 0 / 0
<!-- GENERATED_METRICS_END -->

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
