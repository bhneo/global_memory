# Current State

## Daily/Weekly timeout hardening (2026-08-02)

- An empty Daily consolidation is now a true bounded no-op: it reports
  `derived_rebuild_required: false` and skips both SQLite FTS and Obsidian
  regeneration. Daily runs that create an Extraction, quality assessment,
  source-only record, Working object or Exception still rebuild derived state.
- Index rebuilds use the latest ready Extraction only when its `input_sha256`
  matches the current Source. Raw remains the immutable provenance boundary and
  the fallback when no current Extraction exists, but routine rebuilds no
  longer decode and insert large Raw captures redundantly.
- Weekly consolidation now performs drift checks against the already-loaded
  object, reuses batch document/Receipt/Source/Promotion lookup state, preserves
  live Source-record fingerprint invalidation, and coalesces normal index work
  into one final rebuild. Trusted promotion/requalification remains atomic and
  Receipt v2-gated; Canonical writes remain impossible in this path.
- Obsidian source-only rendering uses the loaded Source inventory instead of a
  full repository lookup per row. Governed ID lookup caches paths but rereads
  current bytes, while typed-evidence validation caches immutable, derived
  Extraction reads with directory-change invalidation.

## README visual architecture (2026-08-02)

- The README now presents Claude, Codex, Hermes, OpenClaw and OpenHuman as host
  assistants, with MCP explicitly shown as their open connection protocol to
  Galois rather than as another assistant.
- The two Mermaid diagrams have been replaced by branded, labeled SVG
  architecture diagrams. Exact pipeline semantics are visible inside each
  diagram and remain available in adjacent text legends and image alt text.

## README truth boundary and private-vault release contract (2026-08-02)

- The public README now leads with Galois's actual cognitive loop—fragments,
  directions, bounded connections and verification—without claiming automatic
  discovery or undocumented scale. It distinguishes factual memory from
  Reflection/Synthesis and states that the current vault has no accepted active
  cross-direction Synthesis.
- Host acceptance now distinguishes the exact server-level five-tool surface
  from host-visible prefixes or wrappers. Windows is the live-validated path;
  OpenHuman may use either its static MCP bridge or dynamic Registry, and
  OpenClaw setup prefers its managed MCP CLI or Control UI.
- ADR 0063 fixes the formal release boundary: engine and protocols may be
  released with synthetic fixtures, but no live or user knowledge vault is
  included. The current full-vault evaluation repository remains unchanged
  until a separately authorized, non-destructive allowlisted export.

## Galois public interface and assistant bootstrap (2026-08-01)

- Current user and AI-assistant instructions expose one public name: `galois`.
  The installed console command, PowerShell launchers, host registration key and
  negotiated MCP server name now follow that identity. Deprecated launchers
  remain compatibility-only and are absent from current instructions.
- Host templates are machine-path-neutral Windows templates governed by a
  machine-readable manifest.
  Integration acceptance requires a live capabilities call, exactly five
  read-only tools and a bounded Chinese Context query; static config is not
  counted as success. Host prefixes/wrappers may map one-to-one to that server
  surface; OpenHuman remains conditional on live static-bridge or dynamic-
  Registry verification.
- The Claude Desktop installer now discovers the repository and Python runtime,
  backs up and merges the actual config, preserves unrelated servers and
  migrates the old server key. The internal Python package and persisted legacy
  identifiers remain unchanged pending a separately governed migration.

## MCP Unicode boundary hardening (2026-08-01)

- The stdio gateway now explicitly reconfigures its Python stdin/stdout text
  wrappers to UTF-8 before the first MCP read. This prevents a UTF-8 MCP client
  such as Hermes from being decoded through the zh-CN Windows GBK code page.
- The stdio gateway now normalizes UTF-16 surrogate pairs at both JSON input
  and output boundaries. This fixes Claude Desktop Chinese-query failures while
  preserving ordinary CJK text and replacing only isolated invalid halves.
- Regression coverage exercises both a valid non-BMP pair and an unpaired
  surrogate, plus explicit stdio UTF-8 configuration. A live subprocess check
  also preserved a Chinese query when its initial environment requested GBK.
  The gateway contract remains read-only and Trusted/Canonical policy is unchanged.
- System-design questions remain a separate retrieval-coverage issue: project
  protocol documents are not ordinary Memory evidence, and no active
  cross-direction Synthesis exists yet. A successful lexical search must not be
  presented as evidence of an implemented cross-direction result.

## Direction alias routing (2026-07-29)

- Context routing now reads machine-readable aliases from the direction
  registry. A matched alias selects a bounded set of active Syntheses by their
  declared `scope_ids`, records the match in Route Trace, and remains a
  navigation signal rather than Evidence. Execution Context still excludes
  every Reflection and Cognitive Synthesis.

## Direction-scoped cognitive synthesis (2026-07-28)

- Weekly remains the scheduling and governance cadence, but new Cognitive
  Synthesis is organized by registered research directions rather than natural
  weeks. Candidate date windows and semantic scope are separate fields.
- Synthesis protocol v2 records direction assignments, subdirections,
  crosscuts, semantic delta and optional parent Syntheses. Cross-direction
  connections require explicit provenance, counterarguments, evidence gaps and
  a verification path; zero candidates is valid.
- `docs/RESEARCH_DIRECTIONS.md` initializes the user-approved embodied-AI,
  mathematics and physics directions with domain-specific subdirections and
  crosscuts. The registry is navigation policy, not Evidence or truth.
- Legacy period-based Synthesis remains replayable for audit. Reflection and
  Synthesis stay non-factual and non-execution-safe; Trusted/Canonical policy is
  unchanged.

## Daily semantic admission coverage and graph closure (2026-07-28)

- Daily Dream protocol v2 now separates source assessment, semantic inventory
  and admission decisions before Working compilation. Every candidate is
  explicitly created, updated, reused, left Source-only, sent to review or
  deferred; high-value readable candidates cannot silently disappear.
- The provider-neutral core reports candidate/admission coverage, high-value
  Reflection-only outcomes, review/deferred counts, reuse targets and
  Source-only reasons. Legacy v1 artifacts remain replayable for recovery.
- `dream audit-daily --from-date ... --to-date ...` provides a read-only Weekly
  preflight over persisted Daily artifacts. It reports unresolved legacy/high-
  value/review/deferred items and never writes knowledge. The current gate uses
  the latest state per Input: later v2 remediation closes an earlier gap while
  historical event counts and `resolved_prior_unresolved` preserve the audit
  trail.
- The knowledge Obsidian projection was rebuilt and independently verified with
  zero missing and zero stale expected nodes. Weekly policy now treats derived
  projection freshness as a separate completion gate.
- Daily/Weekly model output remains Working-only; Trusted and Canonical policy
  is unchanged and Canonical writes remain zero.

## Daily Dream recovery hardening (2026-07-24)

- Daily and Weekly cognitive writes now share an OS-backed process lock. If a
  command wrapper times out while its child is still running, a replay must
  wait and then reuse the same immutable artifact instead of racing writes.
- Semantically identical candidate replays are no-ops even when regenerated
  timestamps or proposal metadata differ. Four false Daily
  `unclassified-change` Exceptions were dismissed with audit resolutions; no
  Working semantics changed.
- The corrupted arXiv Source was preserved and recaptured as immutable version
  `source_4f709a2f26b6_v0002_cb9f3e56f3e6`. Its extraction is ready, the failed
  predecessor is `superseded`, and Daily consolidation safely staged the new
  version as Source-only.
- Source refresh approval now uses the Source-refresh governance path. A failed
  extraction no longer aborts the rest of a triage batch.
- Lifecycle and Receipt lookups use operation-local indexes. Machine-readable
  status now completes in about 3.3 seconds locally while retaining current
  Receipt fingerprint validation. Trusted and Canonical were not changed.

## Legacy semantic re-admission update (2026-07-21)

- Sources whose only deterministic Working output was later quality-retired to
  Historical/source-only are again visible to the bounded model semantic
  queue. This is derived queue state: it neither restores Historical objects
  nor mutates terminal legacy proposals.
- arXiv:2603.20396 was re-read from its 28-page extraction and admitted through
  Input Episode and Reflection into two bounded Working objects covering the
  hierarchical compression model and its compression-bias validation question.
  Trusted and Canonical remained unchanged.
- The remaining 13 quality-retired legacy Sources were reviewed in bounded
  batches. Eight primary papers yielded one reusable Working Concept each;
  five paired, secondary, directory or already-covered implementation Sources
  were deliberately left without new governed knowledge. Agent-authored active
  Reflections now count as completed model review for semantic queue state, so
  intentional Source-only outcomes do not loop back into the queue.

## M9.2 Agent Memory Gateway update (2026-07-20)

- Agent-facing MCP reads now return sanitized Evidence Packets rather than raw
  Context Pack diagnostics. Epistemic and provenance boundaries remain visible;
  filesystem paths, hashes, route traces, SQLite/maintenance state and admin
  commands are excluded.
- MCP initialization establishes a silent-background delivery contract so
  ordinary reports do not narrate the memory system or tool operations.
- Default MCP remains read-only. The explicitly enabled Capture-only tool
  requires confirmed user intent, runs recovery first, and writes immutable
  Source plus typed Input Episode only. Working, Trusted and Canonical writes
  are structurally absent and reported as zero.
- Repository MCP configurations remain strictly read-only. Codex Desktop uses
  a personal plugin with two explicit-only skills for bounded retrieval and
  Capture-only intake; the plugin registers no always-on MCP server.

## M9.2.1 Gateway and cognitive-debt closure (2026-07-29)

- Agent-facing reads now share one versioned `EvidenceItem` / Evidence Packet
  contract across Context, Search, Show and Source. `memory_capabilities`
  negotiates contract versions and exact server-side write scopes.
- Strict execution retrieval exposes stable blocker codes for unresolved
  contradiction, Receipt/currentness, policy qualification and semantic
  entailment failures. Raw Source, Input, Annotation, Reflection and Cognitive
  Synthesis remain non-execution-safe.
- Provider-neutral, explicitly authorized and idempotent session/use/feedback
  signals are available only from the opt-in Agent launcher. Session records
  stop at Source/Input; Activation and research feedback cannot change trust.
- Codex retains its explicit-only personal plugin. Claude Desktop has a backed-up
  read-only MCP registration; reviewed templates cover Hermes, OpenClaw and
  OpenHuman without copying the Vault or replacing their native memory stores.
- Twenty low-authority single-WeChat Claims and two provenance-debt M6
  Syntheses were reversibly retired to Historical/source-only. Eight active
  cadence-scoped Syntheses were replaced by provenance-linked direction-scoped
  successors and moved to the synthesis archive through a verified migration.
- The duplicate REAL Concept was collapsed: the stable Working Concept now
  retains both the official repository and primary-paper sources; the duplicate
  is Historical/source-only. Trusted and Canonical were unchanged.

## M9.1 Cognitive Consolidation update (2026-07-19)

- A 2026-W30 cross-line Weekly integrated four VLA post-training interfaces
  with TouchWorld, TACTIC, TactiDex, REGRIND, TELEDEXTER and DemoBridge under
  precision/contact-rich manipulation. It used 10 existing Reflections,
  preserved the weaker Robo-ValueRL evidence boundary, created one non-factual
  Synthesis and wrote 0 Working, Trusted or Canonical objects.
- The default Obsidian projection now renders active Cognitive Synthesis as a
  distinct colored node class and links its declared Concept inputs with
  explicitly non-factual derived edges. Compact method aliases remain visible,
  so cross-paper research lines can be inspected without exposing hash IDs.
- The 2026-W29 real Weekly follow-up classified all 17 open Exceptions. Five
  duplicate no-op updates and two Historical drift false positives were
  dismissed; eight legacy Claim verification gaps and two M6 Synthesis
  provenance gaps were explicitly deferred. No knowledge tier changed and
  Canonical writes remained zero.
- Drift audit now excludes archived, superseded and Historical objects, in line
  with the routine-maintenance boundary. The two remaining active drift signals
  are medium-severity M6 Synthesis provenance gaps; high-severity drift is zero.
- M9.1 quality closure removed the unsafe regex Claim splitter. Compound
  statements remain proposal-gated until explicit semantic decomposition, and
  headings/sentence fragments fail semantic completeness instead of becoming
  Working nodes.
- Working-quality policy v2 inspects actual fallback markers rather than
  trusting `compiler_version`. It reversibly archived 21 Agent-labeled Claim
  fragments in migration `working_quality_93b259fa551083972ae7524e`; exact
  backups, version snapshots and events are retained, with 0 Trusted and 0
  Canonical writes.
- The default Obsidian knowledge graph excludes operational Global Memory
  acceptance experiments while retaining them in the audit corpus.

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
- Generated at: 2026-07-20T12:00:26+08:00
- Working / Trusted / Canonical / Historical: 89 / 30 / 1 / 64
- Source-only compile records / sources / historical objects: 42 / 42 / 64
- Trusted current policy / receipt / qualified: 28 / 30 / 23
- Trusted awaiting / stale receipt / contested / high-risk drift: 2 / 0 / 0 / 0
- Trusted factual / exploration; Canonical with current Receipt: 11 / 19 / 0
- Contested: 0
- Working revisions: 0
- Open exceptions: 11
- Promotion candidates: 0
- Consolidation receipts / failed: 592 / 82
- Receipt schema versions: {'v1': 113, 'v2': 479}
- Objects with current valid Receipt v2: 111
- Pending recovery journals: 0
- Drift warnings / high severity: 2 / 0
- Corpus sources / knowledge objects: 110 / 184
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

Eight legacy Claim evidence-verification gaps remain explicitly deferred. The
two M6 Synthesis provenance gaps were retired to Historical/source-only after
review and no longer participate in routine conclusions. The Canonical VIA
Claim remains an execution blocker until its semantic entailment evidence is
re-verifiable; Canonical status alone does not make it execution-safe.

## Next concrete task

Restart Claude Desktop and run a real read-only Context acceptance call. Bring
Hermes, OpenClaw and OpenHuman online one at a time, validate their native MCP
config parser and session isolation, then pilot explicit session/use/feedback
signals only after the host can preserve consent and stable idempotency keys.

## Do not do yet

Do not expose receipt compilation, Working mutation, promotion, maintenance or
admin operations through default MCP. Do not add URL/file ingestion,
embeddings, a vector/graph database, browser ingestion, automatic cross-domain
hypothesis generation, multi-Agent orchestration or automatic Canonical writes.
