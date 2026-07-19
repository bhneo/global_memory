---
id: "consolidation_a0fbc27122ba271bbc34fdd5"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: predictive capability."
created_at: "2026-07-19T03:05:37+08:00"
updated_at: "2026-07-19T03:05:37+08:00"
consolidation_id: "consolidation_a0fbc27122ba271bbc34fdd5"
object_id: "claim_9af622d7162156b1ad40f640"
object_version_before: 1
object_sha256_before: "6acbecbdb636385c87ccf42134491485e6d34bdbeda40868f1cec0d45fc3d3c2"
object_sha256_after: "86a49f97aa4daa8fdb24c6369b40b6ac2b6bc71bdd92a16c13fc9150016ff1aa"
source_ids: ["source_233c4bef3a727389ddf81ae2"]
source_sha256s: ["4d15ccc778af7ce315a1efe81a403a7611b5e659f0ddec5570f7b7973302dda1"]
source_records: [{"source_id": "source_233c4bef3a727389ddf81ae2", "source_record_sha256": "7ba69ce30c98fe6a38dee087e03e25f1147010f743f248d4679d357b9dbd83b0", "raw_content_sha256": "4d15ccc778af7ce315a1efe81a403a7611b5e659f0ddec5570f7b7973302dda1", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["evidence_4fdfea63214cb20a192f"]
started_at: "2026-07-19T03:05:36+08:00"
completed_at: "2026-07-19T03:05:37+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/claim/claim_9af622d7162156b1ad40f640.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_233c4bef3a727389ddf81ae2 raw_sha256:4d15ccc778af7ce315a1efe81a403a7611b5e659f0ddec5570f7b7973302dda1"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_233c4bef3a727389ddf81ae2 record_sha256:7ba69ce30c98fe6a38dee087e03e25f1147010f743f248d4679d357b9dbd83b0"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["evidence:evidence_4fdfea63214cb20a192f"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "needs_review", "method": "declared-metadata-inspection", "semantic_recheck_performed": false, "declared_value": "full", "findings": ["evidence_entailment:full"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 2 candidates inspected", "candidate:claim_9af622d7162156b1ad40f640", "candidate:source_91072aa553af99e6ab97c6cd"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 3 related objects found", "related:source_233c4bef3a727389ddf81ae2", "related:tension_world_model_eval_action", "related:concept_embodied_data_loop"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T02:52:30+08:00", "source:source_233c4bef3a727389ddf81ae2 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "86a49f97aa4daa8fdb24c6369b40b6ac2b6bc71bdd92a16c13fc9150016ff1aa", "source_state_sha256": "579a9628228cffa8b0defab560c510353f11f61acf4c0fc9fed6a612c360319f", "source_record_sha256s": {"source_233c4bef3a727389ddf81ae2": "7ba69ce30c98fe6a38dee087e03e25f1147010f743f248d4679d357b9dbd83b0"}, "raw_state_sha256": "2bbdb0315d58f23a0ade7c09bce3631e68901f8bce04b34959ed4b232529ed4a", "evidence_sha256": "48bbef8f0229bc3207aafe59f1adc17203bece549d5afb6a27af82542cf0eaf3", "extraction_state_sha256": "5536044867526c3deb4c1c65e4f436cdc88f2c3efb15b3957386bbfd1a1255dc", "work_identity_sha256": "dd116ba5151dab929ad1633c4eed5454bb7868a427d5fd4c0423bf799c5a7cac", "relation_fingerprint": {"outgoing_relations_sha256": "3797058f45b4d73ba713cf289ab49398c80fac223f662fca0db5ab99dca33ae1", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "3797058f45b4d73ba713cf289ab49398c80fac223f662fca0db5ab99dca33ae1"}, "relation_neighborhood_sha256": "3797058f45b4d73ba713cf289ab49398c80fac223f662fca0db5ab99dca33ae1", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "unchanged"
changes: []
change_summary: "No semantic change."
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "No semantic change.",
  "changes": [],
  "check_details": {
    "contradiction_search_completed": {
      "check_name": "contradiction_search_completed",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "contradiction relations inspected; 0 found"
      ],
      "method": "relation-index-query",
      "semantic_recheck_performed": null,
      "validation_outcome": "clear",
      "warnings": []
    },
    "drift_checked": {
      "check_name": "drift_checked",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "drift_reports:0"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "duplicate_search_completed": {
      "check_name": "duplicate_search_completed",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "searched title; 2 candidates inspected",
        "candidate:claim_9af622d7162156b1ad40f640",
        "candidate:source_91072aa553af99e6ab97c6cd"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "check_name": "evidence_entailment_rechecked",
      "declared_value": "full",
      "execution_status": "completed",
      "findings": [
        "evidence_entailment:full"
      ],
      "method": "declared-metadata-inspection",
      "semantic_recheck_performed": false,
      "validation_outcome": "needs_review",
      "warnings": []
    },
    "evidence_revalidated": {
      "check_name": "evidence_revalidated",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "evidence:evidence_4fdfea63214cb20a192f"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "check_name": "freshness_checked",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "object_updated_at:2026-07-19T02:52:30+08:00",
        "source:source_233c4bef3a727389ddf81ae2 work_sha256:none"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "check_name": "provenance_revalidated",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "source:source_233c4bef3a727389ddf81ae2 record_sha256:7ba69ce30c98fe6a38dee087e03e25f1147010f743f248d4679d357b9dbd83b0"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "raw_available": {
      "check_name": "raw_available",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "source:source_233c4bef3a727389ddf81ae2 raw_sha256:4d15ccc778af7ce315a1efe81a403a7611b5e659f0ddec5570f7b7973302dda1"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "check_name": "related_object_search_completed",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "relation index inspected; 3 related objects found",
        "related:source_233c4bef3a727389ddf81ae2",
        "related:tension_world_model_eval_action",
        "related:concept_embodied_data_loop"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "schema_validated": {
      "check_name": "schema_validated",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "validated:vault/memory/claim/claim_9af622d7162156b1ad40f640.md"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "source_independence_checked": {
      "check_name": "source_independence_checked",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "distinct_source_ids:1",
        "distinct_work_ids:0"
      ],
      "method": "logical-work-identity-count",
      "semantic_recheck_performed": null,
      "validation_outcome": "not_applicable",
      "warnings": []
    }
  },
  "checks": {
    "contradiction_search_completed": true,
    "drift_checked": true,
    "duplicate_search_completed": true,
    "evidence_entailment_rechecked": true,
    "evidence_revalidated": true,
    "freshness_checked": true,
    "provenance_revalidated": true,
    "raw_available": true,
    "related_object_search_completed": true,
    "schema_validated": true,
    "source_independence_checked": true
  },
  "completed_at": "2026-07-19T03:05:37+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "48bbef8f0229bc3207aafe59f1adc17203bece549d5afb6a27af82542cf0eaf3",
    "extraction_state_sha256": "5536044867526c3deb4c1c65e4f436cdc88f2c3efb15b3957386bbfd1a1255dc",
    "memory_schema_version": 2,
    "object_sha256": "86a49f97aa4daa8fdb24c6369b40b6ac2b6bc71bdd92a16c13fc9150016ff1aa",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "2bbdb0315d58f23a0ade7c09bce3631e68901f8bce04b34959ed4b232529ed4a",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "3797058f45b4d73ba713cf289ab49398c80fac223f662fca0db5ab99dca33ae1",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "3797058f45b4d73ba713cf289ab49398c80fac223f662fca0db5ab99dca33ae1"
    },
    "relation_neighborhood_sha256": "3797058f45b4d73ba713cf289ab49398c80fac223f662fca0db5ab99dca33ae1",
    "source_record_sha256s": {
      "source_233c4bef3a727389ddf81ae2": "7ba69ce30c98fe6a38dee087e03e25f1147010f743f248d4679d357b9dbd83b0"
    },
    "source_state_sha256": "579a9628228cffa8b0defab560c510353f11f61acf4c0fc9fed6a612c360319f",
    "work_identity_sha256": "dd116ba5151dab929ad1633c4eed5454bb7868a427d5fd4c0423bf799c5a7cac"
  },
  "consolidation_id": "consolidation_a0fbc27122ba271bbc34fdd5",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T03:05:37+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "evidence_4fdfea63214cb20a192f"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_a0fbc27122ba271bbc34fdd5",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_9af622d7162156b1ad40f640",
  "object_sha256_after": "86a49f97aa4daa8fdb24c6369b40b6ac2b6bc71bdd92a16c13fc9150016ff1aa",
  "object_sha256_before": "6acbecbdb636385c87ccf42134491485e6d34bdbeda40868f1cec0d45fc3d3c2",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_233c4bef3a727389ddf81ae2"
  ],
  "source_records": [
    {
      "raw_content_sha256": "4d15ccc778af7ce315a1efe81a403a7611b5e659f0ddec5570f7b7973302dda1",
      "source_id": "source_233c4bef3a727389ddf81ae2",
      "source_record_sha256": "7ba69ce30c98fe6a38dee087e03e25f1147010f743f248d4679d357b9dbd83b0",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "4d15ccc778af7ce315a1efe81a403a7611b5e659f0ddec5570f7b7973302dda1"
  ],
  "started_at": "2026-07-19T03:05:36+08:00",
  "status": "complete",
  "title": "Consolidation: predictive capability.",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T03:05:37+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
