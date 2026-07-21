# M9.1 Cognitive Consolidation

M9.1 adds a cognitive interpretation layer without turning Global Memory into
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
  -> Weekly Cognitive Synthesis (not fact)
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
.\scripts\gm.ps1 idea capture --text "机器人技能下移可能类似编译器优化"
.\scripts\gm.ps1 conversation import .\chat.md --participant user --participant assistant --topic embodied-agent
.\scripts\gm.ps1 session import --from-file .\session.json --agent codex
.\scripts\gm.ps1 inputs
```

Existing Sources are not silently migrated. Recent or selected historical
material can enter the new layer through a bounded, explicit transition:

```powershell
.\scripts\gm.ps1 inputs --backfill --limit 5
.\scripts\gm.ps1 inputs --backfill --source-id source_<id>
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
.\scripts\gm.ps1 reflection queue --limit 5 --max-chars 6000
.\scripts\gm.ps1 reflection create <input-id> --from-file .\reflection.json
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

Daily Dream is a low-cost, bounded external-Agent workflow. The CLI does not
invoke a model. A Terra-Light-class Agent reads at most five queue items and
writes one local JSON bundle:

```json
{
  "provider_name": "gpt-5.6-terra-light",
  "reflections": [
    {
      "input_id": "input_...",
      "reflection": {"why_important": "...", "open_questions": ["..."]},
      "semantic_items": [{"object_type": "concept", "title": "...", "body": "..."}]
    }
  ]
}
```

Run:

```powershell
.\scripts\gm.ps1 recover
.\scripts\gm.ps1 reflection queue --limit 5 --max-chars 6000
.\scripts\gm.ps1 dream daily --bundle-file .\daily-dream.json --limit 5
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

## Weekly Dream and Synthesis schema

Weekly Dream consumes multiple Reflections plus explicit existing Concepts. Its
Synthesis objects live in `vault/synthesis/` and use
`truth_layer: cognitive_synthesis` with no Memory Tier.

```yaml
id: synthesis_<stable-id>
type: synthesis
status: active
period: 2026-W29
input_reflections: [reflection_<id>]
input_concepts: [concept_<id>]
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
unresolved_tensions: []
candidate_hypotheses: []
possible_experiments: []
confidence: medium
truth_layer: cognitive_synthesis
execution_safe: false
```

Weekly requires at least two Reflections and at least one pattern, qualified
connection, or unresolved tension. A hypothesis candidate must include a
statement, supporting patterns, supporting Reflection IDs, supporting Source
IDs, counterarguments, falsifier, and possible experiment. It is always labeled
`epistemic_status: hypothetical` and is never promoted to Trusted.

```powershell
.\scripts\gm.ps1 dream weekly --bundle-file .\weekly-dream.json
```

Optional `knowledge_bundles` in the JSON use explicit Source IDs, an exact
non-empty subset of this Synthesis's `reflection_ids`, and the normal Semantic
Bundle compiler. The declared Source must be covered by those Reflections. The
validated subset—not every weekly Reflection—is attached as
`reflection_context`. These bundles can create or update Working only.

The Synthesis content identity includes its provider, title, confidence,
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
