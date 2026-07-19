---
id: "consolidation_6b1c5931d11667960b0e6c86"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: Experimental results show consistent improvements in task success rate"
created_at: "2026-07-19T03:05:43+08:00"
updated_at: "2026-07-19T03:05:43+08:00"
consolidation_id: "consolidation_6b1c5931d11667960b0e6c86"
object_id: "claim_db4c678a437a315763b8b434"
object_version_before: 1
object_sha256_before: "b852fb491d2b1eaed4ec3d5c6d0dee94138563db1e3e919358f4a5eeced173eb"
object_sha256_after: "dd08dd310dbef565c8605d70103fb6e5bdb118960dcbb05b044cea04be6da65d"
source_ids: ["source_91072aa553af99e6ab97c6cd"]
source_sha256s: ["435f588538e3bf95c4bdd51e4e7acea6fe2486b6dda7108c64048d6e8b3f9876"]
source_records: [{"source_id": "source_91072aa553af99e6ab97c6cd", "source_record_sha256": "404fcff2f6a367630951f50fa7217da05ac0e501b971d2b6f32e00f013728bb7", "raw_content_sha256": "435f588538e3bf95c4bdd51e4e7acea6fe2486b6dda7108c64048d6e8b3f9876", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["evidence_42308c25592c4fa888b5"]
started_at: "2026-07-19T03:05:43+08:00"
completed_at: "2026-07-19T03:05:43+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/claim/claim_db4c678a437a315763b8b434.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_91072aa553af99e6ab97c6cd raw_sha256:435f588538e3bf95c4bdd51e4e7acea6fe2486b6dda7108c64048d6e8b3f9876"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_91072aa553af99e6ab97c6cd record_sha256:404fcff2f6a367630951f50fa7217da05ac0e501b971d2b6f32e00f013728bb7"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["evidence:evidence_42308c25592c4fa888b5"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "passed", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": "full", "findings": ["evidence_entailment:full"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 3 candidates inspected", "candidate:claim_db4c678a437a315763b8b434", "candidate:source_91072aa553af99e6ab97c6cd", "candidate:source_291d6174cf92660287138f47"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_91072aa553af99e6ab97c6cd", "related:concept_embodied_data_loop"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T03:02:31+08:00", "source:source_91072aa553af99e6ab97c6cd work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "dd08dd310dbef565c8605d70103fb6e5bdb118960dcbb05b044cea04be6da65d", "source_state_sha256": "6d76f2670fd8262ff034d5a3224013f4d5303308ab44c125bfc5bd311d00a189", "source_record_sha256s": {"source_91072aa553af99e6ab97c6cd": "404fcff2f6a367630951f50fa7217da05ac0e501b971d2b6f32e00f013728bb7"}, "raw_state_sha256": "bdb2b46555aea300fd6da544086837210b97428188e908dd6a40de96a84c444f", "evidence_sha256": "88b73f444e90bfc01846daadc75ce5accf5476d1ea81ea6e0410fed2d0f6a0f5", "extraction_state_sha256": "47bedc55b7b5ca56905bd7ece093f8101ffd56641500ca932d7d62ec7fc4efe3", "work_identity_sha256": "789f987213421197c8da0ee072883e7262f4e4b3f0600dffd50e88254826d8a5", "relation_fingerprint": {"outgoing_relations_sha256": "bc686c365f923f2390d75e048b69fe49d3d8132608b0e68bb6bf8732258d17c4", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "bc686c365f923f2390d75e048b69fe49d3d8132608b0e68bb6bf8732258d17c4"}, "relation_neighborhood_sha256": "bc686c365f923f2390d75e048b69fe49d3d8132608b0e68bb6bf8732258d17c4", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "searched title; 3 candidates inspected",
        "candidate:claim_db4c678a437a315763b8b434",
        "candidate:source_91072aa553af99e6ab97c6cd",
        "candidate:source_291d6174cf92660287138f47"
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
      "semantic_recheck_performed": true,
      "validation_outcome": "passed",
      "warnings": []
    },
    "evidence_revalidated": {
      "check_name": "evidence_revalidated",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "evidence:evidence_42308c25592c4fa888b5"
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
        "object_updated_at:2026-07-19T03:02:31+08:00",
        "source:source_91072aa553af99e6ab97c6cd work_sha256:none"
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
        "source:source_91072aa553af99e6ab97c6cd record_sha256:404fcff2f6a367630951f50fa7217da05ac0e501b971d2b6f32e00f013728bb7"
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
        "source:source_91072aa553af99e6ab97c6cd raw_sha256:435f588538e3bf95c4bdd51e4e7acea6fe2486b6dda7108c64048d6e8b3f9876"
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
        "relation index inspected; 2 related objects found",
        "related:source_91072aa553af99e6ab97c6cd",
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
        "validated:vault/memory/claim/claim_db4c678a437a315763b8b434.md"
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
  "completed_at": "2026-07-19T03:05:43+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "88b73f444e90bfc01846daadc75ce5accf5476d1ea81ea6e0410fed2d0f6a0f5",
    "extraction_state_sha256": "47bedc55b7b5ca56905bd7ece093f8101ffd56641500ca932d7d62ec7fc4efe3",
    "memory_schema_version": 2,
    "object_sha256": "dd08dd310dbef565c8605d70103fb6e5bdb118960dcbb05b044cea04be6da65d",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "bdb2b46555aea300fd6da544086837210b97428188e908dd6a40de96a84c444f",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "bc686c365f923f2390d75e048b69fe49d3d8132608b0e68bb6bf8732258d17c4",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "bc686c365f923f2390d75e048b69fe49d3d8132608b0e68bb6bf8732258d17c4"
    },
    "relation_neighborhood_sha256": "bc686c365f923f2390d75e048b69fe49d3d8132608b0e68bb6bf8732258d17c4",
    "source_record_sha256s": {
      "source_91072aa553af99e6ab97c6cd": "404fcff2f6a367630951f50fa7217da05ac0e501b971d2b6f32e00f013728bb7"
    },
    "source_state_sha256": "6d76f2670fd8262ff034d5a3224013f4d5303308ab44c125bfc5bd311d00a189",
    "work_identity_sha256": "789f987213421197c8da0ee072883e7262f4e4b3f0600dffd50e88254826d8a5"
  },
  "consolidation_id": "consolidation_6b1c5931d11667960b0e6c86",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T03:05:43+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "evidence_42308c25592c4fa888b5"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_6b1c5931d11667960b0e6c86",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_db4c678a437a315763b8b434",
  "object_sha256_after": "dd08dd310dbef565c8605d70103fb6e5bdb118960dcbb05b044cea04be6da65d",
  "object_sha256_before": "b852fb491d2b1eaed4ec3d5c6d0dee94138563db1e3e919358f4a5eeced173eb",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_91072aa553af99e6ab97c6cd"
  ],
  "source_records": [
    {
      "raw_content_sha256": "435f588538e3bf95c4bdd51e4e7acea6fe2486b6dda7108c64048d6e8b3f9876",
      "source_id": "source_91072aa553af99e6ab97c6cd",
      "source_record_sha256": "404fcff2f6a367630951f50fa7217da05ac0e501b971d2b6f32e00f013728bb7",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "435f588538e3bf95c4bdd51e4e7acea6fe2486b6dda7108c64048d6e8b3f9876"
  ],
  "started_at": "2026-07-19T03:05:43+08:00",
  "status": "complete",
  "title": "Consolidation: Experimental results show consistent improvements in task success rate",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T03:05:43+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
