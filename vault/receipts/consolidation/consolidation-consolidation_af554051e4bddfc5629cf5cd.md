---
id: "consolidation_af554051e4bddfc5629cf5cd"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 面向策略学习的可运行交互孪生"
created_at: "2026-07-26T12:33:33+08:00"
updated_at: "2026-07-26T12:33:33+08:00"
consolidation_id: "consolidation_af554051e4bddfc5629cf5cd"
object_id: "concept_4b29abb8c07d6365b04b97c3"
object_version_before: 1
object_sha256_before: "66d58696c036827afe19ec23183e8e47da22b1eb13b83612975b938121558677"
object_sha256_after: "6dea85679d77decca36a1c793bf2ef0114566cd01941fa02caf13615a48836df"
source_ids: ["source_4ceaa5243dd0d99116547dda"]
source_sha256s: ["9568e2787c1248710b06a78658e796ef4132352ac066844078fc007380d13f5b"]
source_records: [{"source_id": "source_4ceaa5243dd0d99116547dda", "source_record_sha256": "6971a09ed3e7e96878280dafcf490bd8d4cc0b17ba5a4bf8dcadb432a0f20481", "raw_content_sha256": "9568e2787c1248710b06a78658e796ef4132352ac066844078fc007380d13f5b", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:32+08:00"
completed_at: "2026-07-26T12:33:33+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_4b29abb8c07d6365b04b97c3.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_4ceaa5243dd0d99116547dda raw_sha256:9568e2787c1248710b06a78658e796ef4132352ac066844078fc007380d13f5b"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_4ceaa5243dd0d99116547dda record_sha256:6971a09ed3e7e96878280dafcf490bd8d4cc0b17ba5a4bf8dcadb432a0f20481"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_4b29abb8c07d6365b04b97c3"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_4ceaa5243dd0d99116547dda"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-23T18:06:36+08:00", "source:source_4ceaa5243dd0d99116547dda work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "6dea85679d77decca36a1c793bf2ef0114566cd01941fa02caf13615a48836df", "source_state_sha256": "42f7a0bac5142fb0ba7908444970ea5458f41ba94c8929d987cf0373bf0f07f2", "source_record_sha256s": {"source_4ceaa5243dd0d99116547dda": "6971a09ed3e7e96878280dafcf490bd8d4cc0b17ba5a4bf8dcadb432a0f20481"}, "raw_state_sha256": "cf1c3f30ac8ccd19c6e2dbae68a6919fd6cbff275fdbc21f6b8a4aefa8e176d5", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "fee2d8b1d16e921cca6029ea1c10cb290197baa688ff0eaf1eebb04264f048e5", "relation_fingerprint": {"outgoing_relations_sha256": "cb586d231f92ea9eeb666cff44eb73e240b3a1e1f55bc7dc3673b4001e699262", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "cb586d231f92ea9eeb666cff44eb73e240b3a1e1f55bc7dc3673b4001e699262"}, "relation_neighborhood_sha256": "cb586d231f92ea9eeb666cff44eb73e240b3a1e1f55bc7dc3673b4001e699262", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "searched title; 1 candidates inspected",
        "candidate:concept_4b29abb8c07d6365b04b97c3"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "check_name": "evidence_entailment_rechecked",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "not applicable for non-claim object"
      ],
      "method": "declared-metadata-inspection",
      "semantic_recheck_performed": true,
      "validation_outcome": "not_applicable",
      "warnings": []
    },
    "evidence_revalidated": {
      "check_name": "evidence_revalidated",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "not applicable for non-claim object"
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
        "object_updated_at:2026-07-23T18:06:36+08:00",
        "source:source_4ceaa5243dd0d99116547dda work_sha256:none"
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
        "source:source_4ceaa5243dd0d99116547dda record_sha256:6971a09ed3e7e96878280dafcf490bd8d4cc0b17ba5a4bf8dcadb432a0f20481"
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
        "source:source_4ceaa5243dd0d99116547dda raw_sha256:9568e2787c1248710b06a78658e796ef4132352ac066844078fc007380d13f5b"
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
        "relation index inspected; 1 related objects found",
        "related:source_4ceaa5243dd0d99116547dda"
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
        "validated:vault/memory/concept/concept_4b29abb8c07d6365b04b97c3.md"
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
      "validation_outcome": "not_established",
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
  "completed_at": "2026-07-26T12:33:33+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "6dea85679d77decca36a1c793bf2ef0114566cd01941fa02caf13615a48836df",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "cf1c3f30ac8ccd19c6e2dbae68a6919fd6cbff275fdbc21f6b8a4aefa8e176d5",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "cb586d231f92ea9eeb666cff44eb73e240b3a1e1f55bc7dc3673b4001e699262",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "cb586d231f92ea9eeb666cff44eb73e240b3a1e1f55bc7dc3673b4001e699262"
    },
    "relation_neighborhood_sha256": "cb586d231f92ea9eeb666cff44eb73e240b3a1e1f55bc7dc3673b4001e699262",
    "source_record_sha256s": {
      "source_4ceaa5243dd0d99116547dda": "6971a09ed3e7e96878280dafcf490bd8d4cc0b17ba5a4bf8dcadb432a0f20481"
    },
    "source_state_sha256": "42f7a0bac5142fb0ba7908444970ea5458f41ba94c8929d987cf0373bf0f07f2",
    "work_identity_sha256": "fee2d8b1d16e921cca6029ea1c10cb290197baa688ff0eaf1eebb04264f048e5"
  },
  "consolidation_id": "consolidation_af554051e4bddfc5629cf5cd",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:33+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_af554051e4bddfc5629cf5cd",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_4b29abb8c07d6365b04b97c3",
  "object_sha256_after": "6dea85679d77decca36a1c793bf2ef0114566cd01941fa02caf13615a48836df",
  "object_sha256_before": "66d58696c036827afe19ec23183e8e47da22b1eb13b83612975b938121558677",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_4ceaa5243dd0d99116547dda"
  ],
  "source_records": [
    {
      "raw_content_sha256": "9568e2787c1248710b06a78658e796ef4132352ac066844078fc007380d13f5b",
      "source_id": "source_4ceaa5243dd0d99116547dda",
      "source_record_sha256": "6971a09ed3e7e96878280dafcf490bd8d4cc0b17ba5a4bf8dcadb432a0f20481",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "9568e2787c1248710b06a78658e796ef4132352ac066844078fc007380d13f5b"
  ],
  "started_at": "2026-07-26T12:33:32+08:00",
  "status": "complete",
  "title": "Consolidation: 面向策略学习的可运行交互孪生",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:33+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
