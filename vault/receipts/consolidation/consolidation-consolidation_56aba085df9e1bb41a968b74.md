---
id: "consolidation_56aba085df9e1bb41a968b74"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 面向组合式 OOD 操作的子任务监督与状态条件视觉遮蔽"
created_at: "2026-07-26T12:33:38+08:00"
updated_at: "2026-07-26T12:33:38+08:00"
consolidation_id: "consolidation_56aba085df9e1bb41a968b74"
object_id: "concept_88f87ddc5dcf77113c5154c4"
object_version_before: 1
object_sha256_before: "759571b3525d013a323ceed7fb4c048d84f82c271e57e57782155639c09945b8"
object_sha256_after: "eae2ebfc0b6b96cd6a74e82c26f5383e02a8c0884b6f96df4205b96a4094442e"
source_ids: ["source_0c017bf657a648ca70e9ae25"]
source_sha256s: ["fc5c0239b065a97d3cba7e441fd03cb6f4a100462da5a7959f37df6e383943fb"]
source_records: [{"source_id": "source_0c017bf657a648ca70e9ae25", "source_record_sha256": "92c53feba9a8f5dcddbcbcb47961497b686b7bbea9d27d670e2e4505604f170c", "raw_content_sha256": "fc5c0239b065a97d3cba7e441fd03cb6f4a100462da5a7959f37df6e383943fb", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:38+08:00"
completed_at: "2026-07-26T12:33:38+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_88f87ddc5dcf77113c5154c4.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_0c017bf657a648ca70e9ae25 raw_sha256:fc5c0239b065a97d3cba7e441fd03cb6f4a100462da5a7959f37df6e383943fb"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_0c017bf657a648ca70e9ae25 record_sha256:92c53feba9a8f5dcddbcbcb47961497b686b7bbea9d27d670e2e4505604f170c"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_88f87ddc5dcf77113c5154c4"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_0c017bf657a648ca70e9ae25", "related:concept_90d52ab5e62d9847f9529875"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-25T18:08:44+08:00", "source:source_0c017bf657a648ca70e9ae25 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "eae2ebfc0b6b96cd6a74e82c26f5383e02a8c0884b6f96df4205b96a4094442e", "source_state_sha256": "732eb5387dd667a249eba7ad4e9df8976dccfa22927a2b065af9cf8c24d43476", "source_record_sha256s": {"source_0c017bf657a648ca70e9ae25": "92c53feba9a8f5dcddbcbcb47961497b686b7bbea9d27d670e2e4505604f170c"}, "raw_state_sha256": "6846fa53f9206d6af699327d2b9f0237727a26bf9fb5f6820dbd5be03d58dc8d", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "1c79dab0494634f88fb61ffbbe059975fb64f3dde42588b8f17960ee06395d3d", "relation_fingerprint": {"outgoing_relations_sha256": "229c131e740aee776ab82c6c1fd0cd7af705154280b1ae56b6282962fd0dcb6f", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "229c131e740aee776ab82c6c1fd0cd7af705154280b1ae56b6282962fd0dcb6f"}, "relation_neighborhood_sha256": "229c131e740aee776ab82c6c1fd0cd7af705154280b1ae56b6282962fd0dcb6f", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_88f87ddc5dcf77113c5154c4"
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
        "object_updated_at:2026-07-25T18:08:44+08:00",
        "source:source_0c017bf657a648ca70e9ae25 work_sha256:none"
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
        "source:source_0c017bf657a648ca70e9ae25 record_sha256:92c53feba9a8f5dcddbcbcb47961497b686b7bbea9d27d670e2e4505604f170c"
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
        "source:source_0c017bf657a648ca70e9ae25 raw_sha256:fc5c0239b065a97d3cba7e441fd03cb6f4a100462da5a7959f37df6e383943fb"
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
        "related:source_0c017bf657a648ca70e9ae25",
        "related:concept_90d52ab5e62d9847f9529875"
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
        "validated:vault/memory/concept/concept_88f87ddc5dcf77113c5154c4.md"
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
  "completed_at": "2026-07-26T12:33:38+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "eae2ebfc0b6b96cd6a74e82c26f5383e02a8c0884b6f96df4205b96a4094442e",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "6846fa53f9206d6af699327d2b9f0237727a26bf9fb5f6820dbd5be03d58dc8d",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "229c131e740aee776ab82c6c1fd0cd7af705154280b1ae56b6282962fd0dcb6f",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "229c131e740aee776ab82c6c1fd0cd7af705154280b1ae56b6282962fd0dcb6f"
    },
    "relation_neighborhood_sha256": "229c131e740aee776ab82c6c1fd0cd7af705154280b1ae56b6282962fd0dcb6f",
    "source_record_sha256s": {
      "source_0c017bf657a648ca70e9ae25": "92c53feba9a8f5dcddbcbcb47961497b686b7bbea9d27d670e2e4505604f170c"
    },
    "source_state_sha256": "732eb5387dd667a249eba7ad4e9df8976dccfa22927a2b065af9cf8c24d43476",
    "work_identity_sha256": "1c79dab0494634f88fb61ffbbe059975fb64f3dde42588b8f17960ee06395d3d"
  },
  "consolidation_id": "consolidation_56aba085df9e1bb41a968b74",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:38+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_56aba085df9e1bb41a968b74",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_88f87ddc5dcf77113c5154c4",
  "object_sha256_after": "eae2ebfc0b6b96cd6a74e82c26f5383e02a8c0884b6f96df4205b96a4094442e",
  "object_sha256_before": "759571b3525d013a323ceed7fb4c048d84f82c271e57e57782155639c09945b8",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_0c017bf657a648ca70e9ae25"
  ],
  "source_records": [
    {
      "raw_content_sha256": "fc5c0239b065a97d3cba7e441fd03cb6f4a100462da5a7959f37df6e383943fb",
      "source_id": "source_0c017bf657a648ca70e9ae25",
      "source_record_sha256": "92c53feba9a8f5dcddbcbcb47961497b686b7bbea9d27d670e2e4505604f170c",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "fc5c0239b065a97d3cba7e441fd03cb6f4a100462da5a7959f37df6e383943fb"
  ],
  "started_at": "2026-07-26T12:33:38+08:00",
  "status": "complete",
  "title": "Consolidation: 面向组合式 OOD 操作的子任务监督与状态条件视觉遮蔽",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:38+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
