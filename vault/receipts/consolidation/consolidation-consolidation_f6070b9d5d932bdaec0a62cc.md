---
id: "consolidation_f6070b9d5d932bdaec0a62cc"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 接触中心的混合预测控制"
created_at: "2026-07-20T13:37:26+08:00"
updated_at: "2026-07-20T13:37:26+08:00"
consolidation_id: "consolidation_f6070b9d5d932bdaec0a62cc"
object_id: "concept_2d8e08b8d8ace05431e064a0"
object_version_before: 1
object_sha256_before: "e330ab9e18f5d56e5a5a21fa6608371af80479e5606c2eeb034012da4707a420"
object_sha256_after: "c57aa8e6cca263a716862159cc3cbacb3e6f9c5a2d2be66972f4d55fc63f5e6b"
source_ids: ["source_e8cc1290fdb80e80f77ba2c2"]
source_sha256s: ["419b068dd6bf2204b30ab14f94a29393d116037198cc3347cf158a17bcc5dc18"]
source_records: [{"source_id": "source_e8cc1290fdb80e80f77ba2c2", "source_record_sha256": "f2c834be935d1e8793b38e0faee60849d7bda86ae67b666b3e29520a5eceb448", "raw_content_sha256": "419b068dd6bf2204b30ab14f94a29393d116037198cc3347cf158a17bcc5dc18", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-20T13:37:25+08:00"
completed_at: "2026-07-20T13:37:26+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_2d8e08b8d8ace05431e064a0.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_e8cc1290fdb80e80f77ba2c2 raw_sha256:419b068dd6bf2204b30ab14f94a29393d116037198cc3347cf158a17bcc5dc18"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_e8cc1290fdb80e80f77ba2c2 record_sha256:f2c834be935d1e8793b38e0faee60849d7bda86ae67b666b3e29520a5eceb448"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_2d8e08b8d8ace05431e064a0"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_e8cc1290fdb80e80f77ba2c2", "related:concept_multitimescale_tactile_world_model"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-20T12:39:23+08:00", "source:source_e8cc1290fdb80e80f77ba2c2 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "c57aa8e6cca263a716862159cc3cbacb3e6f9c5a2d2be66972f4d55fc63f5e6b", "source_state_sha256": "006058400f36540cb9a45c2f4861e36274c744a09b703f25502c9b0a9b9d7728", "source_record_sha256s": {"source_e8cc1290fdb80e80f77ba2c2": "f2c834be935d1e8793b38e0faee60849d7bda86ae67b666b3e29520a5eceb448"}, "raw_state_sha256": "f74bc37d85fd786f94a834eee84e3e1b51f5c257a6d89d2d1f82a66629c8ec61", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "cee4fdee7b90c0497f4cd619f3db611fb25edd09bce54a85f107cd88fc5918fe", "relation_fingerprint": {"outgoing_relations_sha256": "2a65c6e025d9d823258dabf500b89585bcebddbebef07aabe323b445bc38c2e6", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "2a65c6e025d9d823258dabf500b89585bcebddbebef07aabe323b445bc38c2e6"}, "relation_neighborhood_sha256": "2a65c6e025d9d823258dabf500b89585bcebddbebef07aabe323b445bc38c2e6", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_2d8e08b8d8ace05431e064a0"
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
        "object_updated_at:2026-07-20T12:39:23+08:00",
        "source:source_e8cc1290fdb80e80f77ba2c2 work_sha256:none"
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
        "source:source_e8cc1290fdb80e80f77ba2c2 record_sha256:f2c834be935d1e8793b38e0faee60849d7bda86ae67b666b3e29520a5eceb448"
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
        "source:source_e8cc1290fdb80e80f77ba2c2 raw_sha256:419b068dd6bf2204b30ab14f94a29393d116037198cc3347cf158a17bcc5dc18"
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
        "related:source_e8cc1290fdb80e80f77ba2c2",
        "related:concept_multitimescale_tactile_world_model"
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
        "validated:vault/memory/concept/concept_2d8e08b8d8ace05431e064a0.md"
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
  "completed_at": "2026-07-20T13:37:26+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "c57aa8e6cca263a716862159cc3cbacb3e6f9c5a2d2be66972f4d55fc63f5e6b",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "f74bc37d85fd786f94a834eee84e3e1b51f5c257a6d89d2d1f82a66629c8ec61",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "2a65c6e025d9d823258dabf500b89585bcebddbebef07aabe323b445bc38c2e6",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "2a65c6e025d9d823258dabf500b89585bcebddbebef07aabe323b445bc38c2e6"
    },
    "relation_neighborhood_sha256": "2a65c6e025d9d823258dabf500b89585bcebddbebef07aabe323b445bc38c2e6",
    "source_record_sha256s": {
      "source_e8cc1290fdb80e80f77ba2c2": "f2c834be935d1e8793b38e0faee60849d7bda86ae67b666b3e29520a5eceb448"
    },
    "source_state_sha256": "006058400f36540cb9a45c2f4861e36274c744a09b703f25502c9b0a9b9d7728",
    "work_identity_sha256": "cee4fdee7b90c0497f4cd619f3db611fb25edd09bce54a85f107cd88fc5918fe"
  },
  "consolidation_id": "consolidation_f6070b9d5d932bdaec0a62cc",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-20T13:37:26+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_f6070b9d5d932bdaec0a62cc",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_2d8e08b8d8ace05431e064a0",
  "object_sha256_after": "c57aa8e6cca263a716862159cc3cbacb3e6f9c5a2d2be66972f4d55fc63f5e6b",
  "object_sha256_before": "e330ab9e18f5d56e5a5a21fa6608371af80479e5606c2eeb034012da4707a420",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_e8cc1290fdb80e80f77ba2c2"
  ],
  "source_records": [
    {
      "raw_content_sha256": "419b068dd6bf2204b30ab14f94a29393d116037198cc3347cf158a17bcc5dc18",
      "source_id": "source_e8cc1290fdb80e80f77ba2c2",
      "source_record_sha256": "f2c834be935d1e8793b38e0faee60849d7bda86ae67b666b3e29520a5eceb448",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "419b068dd6bf2204b30ab14f94a29393d116037198cc3347cf158a17bcc5dc18"
  ],
  "started_at": "2026-07-20T13:37:25+08:00",
  "status": "complete",
  "title": "Consolidation: 接触中心的混合预测控制",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-20T13:37:26+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
