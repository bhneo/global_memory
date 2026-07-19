# Agent Semantic Distillation

Daily and Weekly are Agent workflows, not aliases for deterministic CLI calls.
The CLI enforces provenance, schemas and trust boundaries; the Agent model must
perform the semantic reading that the deterministic core intentionally cannot.

## Daily: cheap semantic admission

1. Run `gm consolidate daily --limit 25` for capture, extraction and the safe
   deterministic boundary. Source-only is an acceptable staging result, not the
   end of semantic maintenance.
2. Run `gm semantic queue --limit 5 --max-chars 6000`.
3. For every selected source, read the bounded excerpt and its reader page. Use
   Context Pack/search to find existing Concepts, Claims, Questions and
   Tensions before creating anything.
4. Produce a local JSON Bundle with at most three high-value items per source.
   Prefer reuse/update over duplication. Every update needs stable `target_id`
   and typed `change_type`; every proposed relation needs a real target and a
   reason.
5. Apply it with `gm compile <source-id> --bundle-file <json>
   --provider-name agent-semantic-daily-v1 --skip-obsidian`. The result enters
   Working only. Batch runs rebuild the disposable Obsidian projection once at
   the final `gm maintain --rebuild-derived`, rather than once per source.

Daily should normally extract the source's research question, central mechanism
or contribution, one bounded result/limitation when evidence is available, and
the minimum useful relations. It should not summarize every section or create
generic nodes merely to improve graph density.

## Weekly: cross-source integration

Weekly uses the stronger Agent model to compare the week's new Working objects
and still-pending semantic queue with existing memory.

1. Run a bounded semantic queue (`--limit 15 --max-chars 10000`) and process the
   highest-value material, prioritizing repeated domains, active projects,
   conflicts and frequently co-occurring concepts.
2. Reuse stable nodes and propose typed `support`, `refine`, `limit`,
   `contradict`, `related_to`, `depends_on`, `tested_by`, `applied_in` or
   `part_of` relationships. A shared keyword alone is not a relation.
3. Run `gm consolidate weekly --skip-daily-admission` only after semantic
   bundles have entered Working, so Weekly Receipt/trust review operates on
   actual knowledge rather than raw articles.
4. Rebuild derived views and test at least one cross-source Context Pack query.

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
