---
id: "consolidation_45f2ba28b17dca759f7ad566"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 冻结技能库与轻量路由适应"
created_at: "2026-07-19T23:49:40+08:00"
updated_at: "2026-07-19T23:49:40+08:00"
consolidation_id: "consolidation_45f2ba28b17dca759f7ad566"
object_id: "concept_d7111f304971448401a57f3b"
object_version_before: 1
object_sha256_before: "4663d2ac1fe4b559a27012ad7ff3b0a4c4685ac7cd21546de9c49f6ee407b017"
object_sha256_after: "7bf0f2f5bd18e86d693e430180486873e4f1ecc33877358908dc05b90b37050c"
source_ids: ["source_d83bb2c45bcaf70906e9ac96"]
source_sha256s: ["e5c283c6492a46b932c61a750972e97f3629b265e7748b2b68a9917081fecf8b"]
source_records: [{"source_id": "source_d83bb2c45bcaf70906e9ac96", "source_record_sha256": "03aea64aa036265b0910f4bbd58fd6849932d83f4811cec8f4587f84cf023646", "raw_content_sha256": "e5c283c6492a46b932c61a750972e97f3629b265e7748b2b68a9917081fecf8b", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-19T23:49:40+08:00"
completed_at: "2026-07-19T23:49:40+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_d7111f304971448401a57f3b.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_d83bb2c45bcaf70906e9ac96 raw_sha256:e5c283c6492a46b932c61a750972e97f3629b265e7748b2b68a9917081fecf8b"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_d83bb2c45bcaf70906e9ac96 record_sha256:03aea64aa036265b0910f4bbd58fd6849932d83f4811cec8f4587f84cf023646"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_d7111f304971448401a57f3b"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_d83bb2c45bcaf70906e9ac96", "related:concept_typed_verified_robot_skill_graph"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T17:16:36+08:00", "source:source_d83bb2c45bcaf70906e9ac96 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "7bf0f2f5bd18e86d693e430180486873e4f1ecc33877358908dc05b90b37050c", "source_state_sha256": "9b0895285cd54188e996949e0935548c326d35c860de47533778675e6274c379", "source_record_sha256s": {"source_d83bb2c45bcaf70906e9ac96": "03aea64aa036265b0910f4bbd58fd6849932d83f4811cec8f4587f84cf023646"}, "raw_state_sha256": "fd1a809957a43f18b5e95520537c2e0d0613f0b0bc66fc287b8ba5691a07699f", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "398f7f6e5fb30b84f1ab4e855c59bf75335ef0fb7c8a17965c594cf6b3356c7f", "relation_fingerprint": {"outgoing_relations_sha256": "e8e022168a5621c744391092dfd621c2b7a6352132c2726013153ec76a2be615", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "e8e022168a5621c744391092dfd621c2b7a6352132c2726013153ec76a2be615"}, "relation_neighborhood_sha256": "e8e022168a5621c744391092dfd621c2b7a6352132c2726013153ec76a2be615", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_d7111f304971448401a57f3b"
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
        "object_updated_at:2026-07-19T17:16:36+08:00",
        "source:source_d83bb2c45bcaf70906e9ac96 work_sha256:none"
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
        "source:source_d83bb2c45bcaf70906e9ac96 record_sha256:03aea64aa036265b0910f4bbd58fd6849932d83f4811cec8f4587f84cf023646"
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
        "source:source_d83bb2c45bcaf70906e9ac96 raw_sha256:e5c283c6492a46b932c61a750972e97f3629b265e7748b2b68a9917081fecf8b"
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
        "related:source_d83bb2c45bcaf70906e9ac96",
        "related:concept_typed_verified_robot_skill_graph"
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
        "validated:vault/memory/concept/concept_d7111f304971448401a57f3b.md"
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
  "completed_at": "2026-07-19T23:49:40+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "7bf0f2f5bd18e86d693e430180486873e4f1ecc33877358908dc05b90b37050c",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "fd1a809957a43f18b5e95520537c2e0d0613f0b0bc66fc287b8ba5691a07699f",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "e8e022168a5621c744391092dfd621c2b7a6352132c2726013153ec76a2be615",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "e8e022168a5621c744391092dfd621c2b7a6352132c2726013153ec76a2be615"
    },
    "relation_neighborhood_sha256": "e8e022168a5621c744391092dfd621c2b7a6352132c2726013153ec76a2be615",
    "source_record_sha256s": {
      "source_d83bb2c45bcaf70906e9ac96": "03aea64aa036265b0910f4bbd58fd6849932d83f4811cec8f4587f84cf023646"
    },
    "source_state_sha256": "9b0895285cd54188e996949e0935548c326d35c860de47533778675e6274c379",
    "work_identity_sha256": "398f7f6e5fb30b84f1ab4e855c59bf75335ef0fb7c8a17965c594cf6b3356c7f"
  },
  "consolidation_id": "consolidation_45f2ba28b17dca759f7ad566",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T23:49:40+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_45f2ba28b17dca759f7ad566",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_d7111f304971448401a57f3b",
  "object_sha256_after": "7bf0f2f5bd18e86d693e430180486873e4f1ecc33877358908dc05b90b37050c",
  "object_sha256_before": "4663d2ac1fe4b559a27012ad7ff3b0a4c4685ac7cd21546de9c49f6ee407b017",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_d83bb2c45bcaf70906e9ac96"
  ],
  "source_records": [
    {
      "raw_content_sha256": "e5c283c6492a46b932c61a750972e97f3629b265e7748b2b68a9917081fecf8b",
      "source_id": "source_d83bb2c45bcaf70906e9ac96",
      "source_record_sha256": "03aea64aa036265b0910f4bbd58fd6849932d83f4811cec8f4587f84cf023646",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "e5c283c6492a46b932c61a750972e97f3629b265e7748b2b68a9917081fecf8b"
  ],
  "started_at": "2026-07-19T23:49:40+08:00",
  "status": "complete",
  "title": "Consolidation: 冻结技能库与轻量路由适应",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T23:49:40+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
