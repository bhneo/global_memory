# M9.1 Cognitive Consolidation

M9.1 adds a cognitive interpretation layer without turning Galois into
an Agent runtime. The core remains provider-neutral: it stores Input Episodes,
validates externally authored Reflections and Weekly Synthesis, compiles
explicit semantic items through the existing Working gate, and serves labeled
read-only Context Packs. It does not call models, tools, or experiments.

## Cognitive pipeline

```text
Experience / Source / Conversation / Idea
  -> Input Episode
  -> Reflection (not fact)
  -> Semantic Bundle + reflection_context
  -> Working Knowledge
  -> Direction Cognitive Synthesis (not fact)
  -> optional Cross-direction Synthesis (not fact)
  -> questions, tensions and falsifiable hypothesis candidates
```

Reflection and Cognitive Synthesis never enter Evidence, Trusted or Canonical.
Daily and Weekly Dream assert a zero-Canonical-write boundary. Knowledge items
still pass through the existing Bundle compiler and enter Working only.

## Input Episode schema

Input Episodes live in `vault/inputs/` and are indexed, local Markdown records.
The linked immutable Source remains authoritative.

```yaml
id: input_<stable-id>
type: input
status: active
input_type: article | paper | github | conversation | idea | experiment | meeting
source_id: source_<id>
participants: []
topic: null
user_authored: false
submitted_by: capture | user | <agent-name>
episode_kind: null | agent_session
truth_layer: input_episode
execution_safe: false
```

Every normal CLI capture now creates an Input Episode and queues it for
Reflection. Specialized entry points are:

```powershell
.\scripts\galois.ps1 idea capture --text "机器人技能下移可能类似编译器优化"
.\scripts\galois.ps1 conversation import .\chat.md --participant user --participant assistant --topic embodied-agent
.\scripts\galois.ps1 session import --from-file .\session.json --agent codex
.\scripts\galois.ps1 inputs
```

Existing Sources are not silently migrated. Recent or selected historical
material can enter the new layer through a bounded, explicit transition:

```powershell
.\scripts\galois.ps1 inputs --backfill --limit 5
.\scripts\galois.ps1 inputs --backfill --source-id source_<id>
```

Default backfill excludes personal notes/receipts, writes no governed Knowledge
and never runs automatically.

Reflection Queue prefers the Source's current hash-bound Derived Extraction for
its bounded excerpt and falls back to the Input body only when no ready
Extraction exists. This keeps PDF/HTML queues readable without copying derived
text into the immutable Input Episode.

Agent Session JSON requires `goal`, `result`, and `lesson`. Import creates an
Input Episode and a Reflection queue item; it writes no Knowledge directly.

## Reflection schema

Reflections live in `vault/reflections/`. They are append-only interpretations,
not factual claims or trust-bearing memory.

```yaml
id: reflection_<stable-id>
type: reflection
status: active
target_ids: [input_<id>, source_<id>]
created_by: agent | user
reflection_kind: article | conversation | idea | experiment | project
importance: high
why_important: <cognitive value, not a summary>
what_changed: <previous view and changed view>
surprising: <counter-intuitive result>
connections:
  - shared_mechanism: <specific common structure>
    boundary: <where the connection applies>
    difference: <how the domains differ>
conflicts: []
open_questions: []
possible_mechanisms: []
future_directions: []
confidence: medium
truth_layer: reflection
user_authored: false
execution_safe: false
```

Reflection objects cannot contain `memory_tier` or `epistemic_status`. They do
not participate in Receipt, Trust or Canonical policy.

```powershell
.\scripts\galois.ps1 reflection queue --limit 5 --max-chars 6000
.\scripts\galois.ps1 reflection create <input-id> --from-file .\reflection.json
```

## Reflection quality gate

The gate rejects generic summaries such as “这篇文章介绍了 XXX”. A Reflection
must explain why the input matters and include at least one of:

- a changed belief;
- a surprising observation;
- a qualified connection;
- an open question.

Every connection must state `shared_mechanism`, `boundary`, and `difference`.
Keyword overlap is not a cognitive connection.

## Daily Dream

Daily Dream is a bounded external-Agent workflow. The CLI does not invoke a
model. New production artifacts use the v2 admission contract and a strong
reasoning model reads at most five queue items before writing one local JSON
bundle. Legacy v1 artifacts remain accepted only so an interrupted immutable
artifact can be replayed safely:

```json
{
  "daily_protocol_version": 2,
  "provider_name": "gpt-5.6-sol-high",
  "reflections": [
    {
      "input_id": "input_...",
      "reflection": {"why_important": "...", "open_questions": ["..."]},
      "source_assessment": {"readability": "readable", "source_role": "primary", "reason": ""},
      "semantic_inventory": [{
        "candidate_id": "mechanism",
        "candidate_type": "concept",
        "statement": "A complete, reusable semantic candidate.",
        "value": "high",
        "value_reason": "It changes or reuses durable knowledge.",
        "source_grounded": true
      }],
      "admission_decisions": [{
        "candidate_id": "mechanism",
        "decision": "create",
        "reason_code": "",
        "reason": "No active object fully covers it.",
        "target_ids": []
      }],
      "semantic_items": [{
        "candidate_id": "mechanism",
        "object_type": "concept",
        "title": "...",
        "body": "..."
      }]
    }
  ]
}
```

Run:

```powershell
.\scripts\galois.ps1 recover
.\scripts\galois.ps1 reflection queue --limit 5 --max-chars 6000
.\scripts\galois.ps1 dream daily --bundle-file .\daily-dream.json --limit 5
```

Daily permits at most three semantic items per input, creates Reflections,
compiles explicit items into Working, and reports `canonical_writes: 0`. It does
not perform cross-domain synthesis or generate hypotheses. The allowed Daily
semantic object types are Concept, Claim, Question, Tension and Work. The whole
artifact is structurally validated before the first Reflection write. If a run
is interrupted after an immutable Reflection is written, rerunning the same
artifact reuses that deterministic Reflection and resumes Working compilation.

Daily Claim items must each be a self-contained proposition. Connector-based
automatic splitting is forbidden because textual clauses are not reliable
semantic boundaries. Compound Claims stay in the proposal layer for explicit
model/human decomposition; fragments receive `semantic_completeness: fragment`
and incomplete evidence coverage, so they cannot enter Working.

Daily v2 separates cognitive value, semantic value and evidence strength. Each
Input first records source readability/role and an explicit semantic inventory,
then gives every candidate exactly one `create`, `update`, `reuse`,
`source_only`, `review_required`, or `deferred` decision. Create/update decisions
must map exactly to the at-most-three semantic items. Reuse/update name active
stable target IDs. Source-only uses a specific reason code: `unreadable`,
`duplicate`, `insufficient_evidence`, `too_broad`, `metadata_only`, or
`no_reusable_increment`. Review uses `needs_deep_review`, `dedup_uncertain`, or
`evidence_ambiguous`; deferred is reserved for `daily_item_limit`.

A high-importance readable Input cannot have an empty semantic inventory. A
high-value readable, source-grounded candidate must be admitted, reused,
deferred, or sent to review rather than silently disappearing. Run the read-only
coverage audit before Weekly integration:

```powershell
.\scripts\galois.ps1 dream audit-daily --from-date 2026-07-21 --to-date 2026-07-27
.\scripts\galois.ps1 obsidian status --graph-profile knowledge
```

The audit resolves admission state by stable `input_id`, using the latest
artifact in the selected range. A later v2 re-admission therefore closes an
earlier legacy high-value-empty event without erasing its historical event
count. The weekly cadence should audit from the previous successful run (or
another explicit bounded start) through the current date so later remediation
is included.
`inputs` counts artifact entries, `unique_inputs` counts logical Inputs, and
`resolved_prior_unresolved` makes repaired gaps explicit.

## Recurring Dream and Synthesis schema

The weekly scheduler consumes multiple Reflections plus explicit existing
Concepts, but the calendar is not the semantic grouping key. Synthesis objects
live in `vault/synthesis/` and use
`truth_layer: cognitive_synthesis` with no Memory Tier.

```yaml
id: synthesis_<stable-id>
type: synthesis
status: active
synthesis_protocol_version: 2
scope_kind: direction
scope_ids: [world-models-predictive-representations]
candidate_window: {from_date: 2026-07-21, to_date: 2026-07-28}
delta_kind: extend
direction_assignments:
  - reflection_id: reflection_<id>
    primary_direction: world-models-predictive-representations
    secondary_directions: []
    subdirections: [action-conditioned-prediction]
    crosscut_dimensions: [system-and-deployment]
    routing_confidence: high
    reason: <specific routing reason>
input_reflections: [reflection_<id>]
input_concepts: [concept_<id>]
input_syntheses: []
emerging_patterns: []
knowledge_updates:
  - target_id: concept_<id>
    previous: ...
    proposed: ...
    reason: ...
    change_type: refine
    supporting_reflections: [reflection_<id>]
    supporting_sources: [source_<id>]
new_connections:
  - shared_mechanism: ...
    boundary: ...
    difference: ...
    direction_ids: [world-models-predictive-representations]
    supporting_reflections: [reflection_<id>]
    supporting_sources: [source_<id>]
    why_potentially_useful: ...
    counter_arguments: [...]
    evidence_gap: ...
    verification_path: ...
    confidence: low
unresolved_tensions: []
candidate_hypotheses: []
possible_experiments: []
confidence: medium
truth_layer: cognitive_synthesis
execution_safe: false
```

Synthesis requires at least two Reflections and at least one pattern, qualified
connection, or unresolved tension. A hypothesis candidate must include a
statement, supporting patterns, supporting Reflection IDs, supporting Source
IDs, counterarguments, falsifier, and possible experiment. It is always labeled
`epistemic_status: hypothetical` and is never promoted to Trusted.

Protocol v2 has two scopes:

- `direction`: exactly one registered direction; it may cite at most one prior
  active Synthesis to express an incremental delta.
- `cross_direction`: at least two registered directions and at least two active
  direction Syntheses. Every connection names both directions and retains its
  Reflection/Source support, counterarguments, evidence gap and verification
  path.

Every input Reflection has exactly one primary direction. Secondary directions
are allowed only for a distinct mechanism or boundary. The registry is
`docs/RESEARCH_DIRECTIONS.md`. Unchanged directions reuse prior Synthesis and
produce a no-op report. Legacy `period` artifacts remain replayable as protocol
v1 audit history, but new production artifacts do not use a natural week as
their scope.

```powershell
.\scripts\galois.ps1 dream weekly --bundle-file .\weekly-dream.json
```

Optional `knowledge_bundles` in the JSON use explicit Source IDs, an exact
non-empty subset of this Synthesis's `reflection_ids`, and the normal Semantic
Bundle compiler. The declared Source must be covered by those Reflections. The
validated subset—not every weekly Reflection—is attached as
`reflection_context`. These bundles can create or update Working only.

The Synthesis content identity includes its provider, semantic scope, candidate
window, direction assignments, title, confidence,
patterns, tensions, connections, knowledge updates, hypothesis candidates and
possible experiments. Changing any cognitive content produces a new immutable
Synthesis rather than silently reusing an older object.

## Semantic Bundle reflection context

External JSON bundles may include:

```json
{
  "reflection_context": {
    "reflection_ids": ["reflection_..."],
    "importance": "high",
    "changed_belief": "...",
    "surprising": "...",
    "connections": [{"shared_mechanism": "...", "boundary": "...", "difference": "..."}],
    "open_questions": ["..."]
  },
  "items": []
}
```

The compiler preserves this context for audit and rejects unqualified
connections. Reflection context is interpretation metadata, never Evidence.

## Third-party Context API

The existing read-only Context API remains the integration surface for Codex,
Claude Code, OpenHuman, Hermes, and other Agents:

```json
{"query": "如何设计具身 Agent 大脑", "profile": "research"}
```

Research and Exploration may return Concepts, Claims, Reflections, Questions,
Tensions and recent Cognitive Synthesis with explicit truth labels. Execution
does not admit Reflection or Cognitive Synthesis and continues to require
validated knowledge plus project state. MCP remains read-only and delegates to
the same Context Pack policy.

## Explicit non-goals

M9.1 adds no Agent Runtime, Skill System, tool execution, automatic experiment,
automatic scientific discovery, graph/vector database, write MCP, or multi-Agent
orchestration.
