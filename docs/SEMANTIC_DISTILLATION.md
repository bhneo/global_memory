# Agent Semantic Distillation

M9.1 inserts Reflection before semantic compilation. Daily Agents consume the
bounded `reflection queue`, create quality-gated Reflection objects, and attach
`reflection_context` to explicit Semantic Bundle items. Weekly Agents compare
multiple Reflections with active Concepts and emit a separate Cognitive
Synthesis before proposing any Working knowledge update. The CLI validates
artifacts; it does not invoke the model. See `COGNITIVE_CONSOLIDATION.md`.

Daily and Weekly are Agent workflows, not aliases for deterministic CLI calls.
The CLI enforces provenance, schemas and trust boundaries; the Agent model must
perform the semantic reading that the deterministic core intentionally cannot.

## Daily: cheap semantic admission

1. Run `galois recover`, then `galois consolidate daily --limit 25` for extraction and
   the safe deterministic boundary. Source-only is acceptable staging, not the
   end of semantic maintenance.
2. Run `galois reflection queue --limit 5 --max-chars 6000`. Use the bounded
   `galois semantic queue` only as a source/extraction supplement for those selected
   Input Episodes; do not process a separate unrelated batch.
3. For every selected Input, read the bounded excerpt and its Source reader. Use
   Context Pack/search to find existing Concepts, Claims, Questions and
   Tensions before creating anything.
4. The Daily model first records source readability/role and a semantic
   inventory covering the research question, central mechanism/contribution,
   bounded result, assumptions and limitation when present. It then assigns
   every candidate an explicit create/update/reuse/source_only/review/deferred
   decision and emits at most three source-grounded `semantic_items` per Input.
   Daily semantic items are limited to Concept, Claim, Question, Tension and
   Work; Hypothesis, Analogy and Synthesis are rejected by the core.
5. Apply the artifact with `galois dream daily --bundle-file <json> --limit 5`.
   The command validates the entire batch before cognitive writes, reuses an
   identical immutable Reflection after interruption, and writes Working only.
6. Run `galois dream audit-daily` for the batch date. High-value readable empty
   outcomes, review-required candidates and deferred candidates remain visible
   and cannot be reported as silently complete. For Weekly or remediation,
   extend the range through the current date; the audit uses the latest state
   per `input_id` while retaining historical unresolved-event counts.
7. Rebuild disposable views once with `galois maintain --rebuild-derived`.

Daily should normally extract the source's research question, central mechanism
or contribution, one bounded result/limitation when evidence is available, and
the minimum useful relations. It should not summarize every section or create
generic nodes merely to improve graph density.

Source-only is a semantic decision, not a default. It needs one of the bounded
reason codes documented in `COGNITIVE_CONSOLIDATION.md`; duplicate/reuse claims
must name the active target compared. A tagged Reflection alone is insufficient
Context acceptance for a readable high-value primary source unless its Working
admission, reuse target, review state or explicit deferral is also visible.

Claims must be complete, bounded propositions written by the model. The core
does not split compound prose at commas or conjunctions: such material remains
`compound` and must be replaced by explicit semantic items. Headings, trailing
clauses and fragments such as “respectively” tails fail semantic completeness
and cannot be approved into Working.

## Weekly cadence: governance plus direction-scoped integration

Weekly uses the stronger Agent model, but the date window only identifies new or
unresolved candidates. It does not define a cognitive topic.

1. Run `galois recover`, then audit Daily artifacts since the previous successful
   run. Finish any bounded
   Reflection backlog and resolve or explicitly defer high-value Daily admission
   findings before Weekly integration; do not silently synthesize unreflected
   raw captures.
2. Route each eligible Reflection through `docs/RESEARCH_DIRECTIONS.md`: exactly
   one primary direction, optional secondary directions, subdirections and
   crosscuts. Feedback and Activation may prioritize work but are not evidence.
3. For each direction with a real semantic delta, read its Sources, Reflections
   and active Concepts. Reuse stable nodes and propose typed `support`, `refine`, `limit`,
   `contradict`, `related_to`, `depends_on`, `tested_by`, `applied_in` or
   `part_of` relationships. A shared keyword alone is not a relation.
4. Produce one protocol-v2 JSON artifact per coherent direction, not one
   calendar-week aggregate. More than eight Reflections should normally split
   by subdirection or mechanism. Every `knowledge_update` names an
   active input Concept, typed change, previous/proposed view, reason and its
   supporting Reflection/Source IDs. Every `knowledge_bundle` declares the
   exact Reflection IDs that support its Source and semantic items.
5. Apply each artifact with `galois dream weekly --bundle-file <json>`. Cognitive Synthesis is
   non-factual; optional semantic bundles enter Working only.
6. Optionally create a separate cross-direction artifact after its direction
   Syntheses exist. It must cite at least two direction Syntheses and retain
   qualified connection provenance; zero cross-direction output is valid.
7. Run `galois consolidate weekly --skip-daily-admission` only after the Dream
   artifact has entered Working, so Receipt/trust review operates on actual
   knowledge rather than raw articles.
8. Rebuild derived views and test one direction query plus one cross-direction
   query when a cross-direction candidate was created.
   Weekly completion also requires Obsidian expected/actual freshness with zero
   missing and stale nodes. A maintenance timeout is `indeterminate`; it cannot
   be promoted to complete from partial timestamps or doctor/lint/raw/status.
   Use `galois obsidian status --graph-profile knowledge`; if it is not current,
   run only `galois obsidian build --graph-profile knowledge` and check status again.

Weekly must report semantic yield separately from governance yield:

- sources read by the model;
- Working objects created/updated;
- existing nodes reused;
- typed relations added;
- duplicate/no-value sources left Source-only;
- support/refine/limit/contradict outcomes;
- Trusted/Canonical changes (Canonical must remain zero without approval).

## Bundle contract

The model writes local JSON only; it does not edit governed objects directly.

```json
{
  "items": [
    {
      "object_type": "concept",
      "title": "Human-readable stable concept",
      "body": "Concise source-grounded definition.",
      "relations": [
        {
          "type": "related_to",
          "target_id": "concept_existing",
          "reason": "Specific semantic reason, not keyword overlap.",
          "confidence": "medium"
        }
      ],
      "metadata": {
        "aliases": ["common English term", "standard acronym"],
        "domains": ["embodied-ai", "vla"],
        "confidence": "medium"
      }
    }
  ]
}
```

Model output is always Working. Trusted still requires current evidence-bound
Receipts and policy qualification. Canonical still requires explicit human
approval.

When the human-readable title and the source use different languages, the model
must include standard bilingual aliases and acronyms. Aliases improve retrieval;
they do not change the statement or its epistemic status.
