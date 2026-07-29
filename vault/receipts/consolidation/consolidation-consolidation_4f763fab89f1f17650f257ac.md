---
id: "consolidation_4f763fab89f1f17650f257ac"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 带本体掩码的语义分组跨本体动作空间"
created_at: "2026-07-26T12:33:40+08:00"
updated_at: "2026-07-26T12:33:40+08:00"
consolidation_id: "consolidation_4f763fab89f1f17650f257ac"
object_id: "concept_98b7ebb5d2382b61dd11bab3"
object_version_before: 1
object_sha256_before: "f4ba8778993be050edcc5d7aac760366ebefbb4adaeb0a0b8dc5830421192699"
object_sha256_after: "08adbf0ec16c9364ae525e78e221f8b4a31195a6bc86662dab3587db56eef90c"
source_ids: ["source_5c29f310c66b0fb5c6cb2758"]
source_sha256s: ["70b79eb901833c62330c057a78046266f611ea3142896036f378caf5cc1200aa"]
source_records: [{"source_id": "source_5c29f310c66b0fb5c6cb2758", "source_record_sha256": "0c11cc8d4cdb4b954ab019c3b889d830097202eae8ba0622a90a8afa60df2554", "raw_content_sha256": "70b79eb901833c62330c057a78046266f611ea3142896036f378caf5cc1200aa", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:40+08:00"
completed_at: "2026-07-26T12:33:40+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_98b7ebb5d2382b61dd11bab3.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_5c29f310c66b0fb5c6cb2758 raw_sha256:70b79eb901833c62330c057a78046266f611ea3142896036f378caf5cc1200aa"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_5c29f310c66b0fb5c6cb2758 record_sha256:0c11cc8d4cdb4b954ab019c3b889d830097202eae8ba0622a90a8afa60df2554"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_98b7ebb5d2382b61dd11bab3"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_5c29f310c66b0fb5c6cb2758", "related:concept_staged_cross_embodiment_alignment"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-23T18:07:18+08:00", "source:source_5c29f310c66b0fb5c6cb2758 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "08adbf0ec16c9364ae525e78e221f8b4a31195a6bc86662dab3587db56eef90c", "source_state_sha256": "aaa2b9ec6d21be9c09bbcfc3f6d346245953980d0709e0a19092cd347345e348", "source_record_sha256s": {"source_5c29f310c66b0fb5c6cb2758": "0c11cc8d4cdb4b954ab019c3b889d830097202eae8ba0622a90a8afa60df2554"}, "raw_state_sha256": "71a4d898c81b74b921a6a4862ada6d7613cf242e24ffc0ca2e6877b9638d820b", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "7e0cfae2e44d1a4c158cb252cf70b0f690ea7626f3bc4cb8694e46bd80f5481b", "relation_fingerprint": {"outgoing_relations_sha256": "40ae322c5721f158fd3952ad23a38bb20e385ffb8d4539bcb1b5660a9154d8af", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "40ae322c5721f158fd3952ad23a38bb20e385ffb8d4539bcb1b5660a9154d8af"}, "relation_neighborhood_sha256": "40ae322c5721f158fd3952ad23a38bb20e385ffb8d4539bcb1b5660a9154d8af", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_98b7ebb5d2382b61dd11bab3"
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
        "object_updated_at:2026-07-23T18:07:18+08:00",
        "source:source_5c29f310c66b0fb5c6cb2758 work_sha256:none"
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
        "source:source_5c29f310c66b0fb5c6cb2758 record_sha256:0c11cc8d4cdb4b954ab019c3b889d830097202eae8ba0622a90a8afa60df2554"
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
        "source:source_5c29f310c66b0fb5c6cb2758 raw_sha256:70b79eb901833c62330c057a78046266f611ea3142896036f378caf5cc1200aa"
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
        "related:source_5c29f310c66b0fb5c6cb2758",
        "related:concept_staged_cross_embodiment_alignment"
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
        "validated:vault/memory/concept/concept_98b7ebb5d2382b61dd11bab3.md"
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
  "completed_at": "2026-07-26T12:33:40+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "08adbf0ec16c9364ae525e78e221f8b4a31195a6bc86662dab3587db56eef90c",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "71a4d898c81b74b921a6a4862ada6d7613cf242e24ffc0ca2e6877b9638d820b",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "40ae322c5721f158fd3952ad23a38bb20e385ffb8d4539bcb1b5660a9154d8af",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "40ae322c5721f158fd3952ad23a38bb20e385ffb8d4539bcb1b5660a9154d8af"
    },
    "relation_neighborhood_sha256": "40ae322c5721f158fd3952ad23a38bb20e385ffb8d4539bcb1b5660a9154d8af",
    "source_record_sha256s": {
      "source_5c29f310c66b0fb5c6cb2758": "0c11cc8d4cdb4b954ab019c3b889d830097202eae8ba0622a90a8afa60df2554"
    },
    "source_state_sha256": "aaa2b9ec6d21be9c09bbcfc3f6d346245953980d0709e0a19092cd347345e348",
    "work_identity_sha256": "7e0cfae2e44d1a4c158cb252cf70b0f690ea7626f3bc4cb8694e46bd80f5481b"
  },
  "consolidation_id": "consolidation_4f763fab89f1f17650f257ac",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:40+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_4f763fab89f1f17650f257ac",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_98b7ebb5d2382b61dd11bab3",
  "object_sha256_after": "08adbf0ec16c9364ae525e78e221f8b4a31195a6bc86662dab3587db56eef90c",
  "object_sha256_before": "f4ba8778993be050edcc5d7aac760366ebefbb4adaeb0a0b8dc5830421192699",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_5c29f310c66b0fb5c6cb2758"
  ],
  "source_records": [
    {
      "raw_content_sha256": "70b79eb901833c62330c057a78046266f611ea3142896036f378caf5cc1200aa",
      "source_id": "source_5c29f310c66b0fb5c6cb2758",
      "source_record_sha256": "0c11cc8d4cdb4b954ab019c3b889d830097202eae8ba0622a90a8afa60df2554",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "70b79eb901833c62330c057a78046266f611ea3142896036f378caf5cc1200aa"
  ],
  "started_at": "2026-07-26T12:33:40+08:00",
  "status": "complete",
  "title": "Consolidation: 带本体掩码的语义分组跨本体动作空间",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:40+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
