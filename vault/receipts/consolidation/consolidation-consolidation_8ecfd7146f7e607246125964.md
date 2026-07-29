---
id: "consolidation_8ecfd7146f7e607246125964"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 状态转换语言驱动的跨本体 VLA 两阶段训练"
created_at: "2026-07-26T12:33:31+08:00"
updated_at: "2026-07-26T12:33:31+08:00"
consolidation_id: "consolidation_8ecfd7146f7e607246125964"
object_id: "concept_39512575bdcd8ac68d340b03"
object_version_before: 1
object_sha256_before: "87d5b72209c98f8047a06395b2e50d4a3fac365b9ed4af96a3ec614d5862d80c"
object_sha256_after: "95c59a9cc51381995610c08ed94dcd8595fac55506199c00ac080dd438ee134c"
source_ids: ["source_5df8ebbcd9bd1afec33d46cc"]
source_sha256s: ["fb589afdf0299c47cf4db2a80d29005bbfbef2cee60c97f8dd36d51ef993b8fb"]
source_records: [{"source_id": "source_5df8ebbcd9bd1afec33d46cc", "source_record_sha256": "441bf073f1036ac000c0705c3988997321f9452d5b4f7e51c464b3d9e7a2869b", "raw_content_sha256": "fb589afdf0299c47cf4db2a80d29005bbfbef2cee60c97f8dd36d51ef993b8fb", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:31+08:00"
completed_at: "2026-07-26T12:33:31+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_39512575bdcd8ac68d340b03.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_5df8ebbcd9bd1afec33d46cc raw_sha256:fb589afdf0299c47cf4db2a80d29005bbfbef2cee60c97f8dd36d51ef993b8fb"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_5df8ebbcd9bd1afec33d46cc record_sha256:441bf073f1036ac000c0705c3988997321f9452d5b4f7e51c464b3d9e7a2869b"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_39512575bdcd8ac68d340b03"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_5df8ebbcd9bd1afec33d46cc", "related:concept_real_robot_deployment_iteration_loop"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-21T18:08:35+08:00", "source:source_5df8ebbcd9bd1afec33d46cc work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "95c59a9cc51381995610c08ed94dcd8595fac55506199c00ac080dd438ee134c", "source_state_sha256": "2ad43e2d29cc120c470f9459414a8941d5e32cbf6ba9a24f6b737c2ca97711b3", "source_record_sha256s": {"source_5df8ebbcd9bd1afec33d46cc": "441bf073f1036ac000c0705c3988997321f9452d5b4f7e51c464b3d9e7a2869b"}, "raw_state_sha256": "90b1460bc0bcbd37bd11d45e008a8b7c3d2d670e57940b4130a1b36340630ab0", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "520c6b9ba01af8c27874b30a8c299e52491e1d09c46ba6c8ca2c720a44dfba8c", "relation_fingerprint": {"outgoing_relations_sha256": "b17244977d1a7ce65447c13ffe7d74ab8932411ffd0ee5dd8765515a9b660581", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "b17244977d1a7ce65447c13ffe7d74ab8932411ffd0ee5dd8765515a9b660581"}, "relation_neighborhood_sha256": "b17244977d1a7ce65447c13ffe7d74ab8932411ffd0ee5dd8765515a9b660581", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_39512575bdcd8ac68d340b03"
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
        "object_updated_at:2026-07-21T18:08:35+08:00",
        "source:source_5df8ebbcd9bd1afec33d46cc work_sha256:none"
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
        "source:source_5df8ebbcd9bd1afec33d46cc record_sha256:441bf073f1036ac000c0705c3988997321f9452d5b4f7e51c464b3d9e7a2869b"
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
        "source:source_5df8ebbcd9bd1afec33d46cc raw_sha256:fb589afdf0299c47cf4db2a80d29005bbfbef2cee60c97f8dd36d51ef993b8fb"
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
        "related:source_5df8ebbcd9bd1afec33d46cc",
        "related:concept_real_robot_deployment_iteration_loop"
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
        "validated:vault/memory/concept/concept_39512575bdcd8ac68d340b03.md"
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
  "completed_at": "2026-07-26T12:33:31+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "95c59a9cc51381995610c08ed94dcd8595fac55506199c00ac080dd438ee134c",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "90b1460bc0bcbd37bd11d45e008a8b7c3d2d670e57940b4130a1b36340630ab0",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "b17244977d1a7ce65447c13ffe7d74ab8932411ffd0ee5dd8765515a9b660581",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "b17244977d1a7ce65447c13ffe7d74ab8932411ffd0ee5dd8765515a9b660581"
    },
    "relation_neighborhood_sha256": "b17244977d1a7ce65447c13ffe7d74ab8932411ffd0ee5dd8765515a9b660581",
    "source_record_sha256s": {
      "source_5df8ebbcd9bd1afec33d46cc": "441bf073f1036ac000c0705c3988997321f9452d5b4f7e51c464b3d9e7a2869b"
    },
    "source_state_sha256": "2ad43e2d29cc120c470f9459414a8941d5e32cbf6ba9a24f6b737c2ca97711b3",
    "work_identity_sha256": "520c6b9ba01af8c27874b30a8c299e52491e1d09c46ba6c8ca2c720a44dfba8c"
  },
  "consolidation_id": "consolidation_8ecfd7146f7e607246125964",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:31+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_8ecfd7146f7e607246125964",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_39512575bdcd8ac68d340b03",
  "object_sha256_after": "95c59a9cc51381995610c08ed94dcd8595fac55506199c00ac080dd438ee134c",
  "object_sha256_before": "87d5b72209c98f8047a06395b2e50d4a3fac365b9ed4af96a3ec614d5862d80c",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_5df8ebbcd9bd1afec33d46cc"
  ],
  "source_records": [
    {
      "raw_content_sha256": "fb589afdf0299c47cf4db2a80d29005bbfbef2cee60c97f8dd36d51ef993b8fb",
      "source_id": "source_5df8ebbcd9bd1afec33d46cc",
      "source_record_sha256": "441bf073f1036ac000c0705c3988997321f9452d5b4f7e51c464b3d9e7a2869b",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "fb589afdf0299c47cf4db2a80d29005bbfbef2cee60c97f8dd36d51ef993b8fb"
  ],
  "started_at": "2026-07-26T12:33:31+08:00",
  "status": "complete",
  "title": "Consolidation: 状态转换语言驱动的跨本体 VLA 两阶段训练",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:31+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
