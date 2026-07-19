---
id: "consolidation_568c97c25c770825fd0ea416"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 传感器条件化专家路由"
created_at: "2026-07-19T03:25:13+08:00"
updated_at: "2026-07-19T03:25:13+08:00"
consolidation_id: "consolidation_568c97c25c770825fd0ea416"
object_id: "concept_sensor_conditional_expert_routing"
object_version_before: 1
object_sha256_before: "13d56fa218033b436a703850b943ab3843faf5b968d4991299365274f897b0e3"
object_sha256_after: "9d590e86cab0fa32c6d6c8e11f8930150acd2fae5c690b7b767d7b6cce4dcd75"
source_ids: ["source_5d8306b5caf7371feeacbc09"]
source_sha256s: ["4793c2e64e6d67a02a4f3e62b2d6376eb1ea7493edc6706c70f3fc79e735b3ca"]
source_records: [{"source_id": "source_5d8306b5caf7371feeacbc09", "source_record_sha256": "b2b030ac7177a5df21066addfe586d4feeb1378acc2535c4efabb0f0b5d798cb", "raw_content_sha256": "4793c2e64e6d67a02a4f3e62b2d6376eb1ea7493edc6706c70f3fc79e735b3ca", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-19T03:25:13+08:00"
completed_at: "2026-07-19T03:25:13+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_sensor_conditional_expert_routing.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_5d8306b5caf7371feeacbc09 raw_sha256:4793c2e64e6d67a02a4f3e62b2d6376eb1ea7493edc6706c70f3fc79e735b3ca"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_5d8306b5caf7371feeacbc09 record_sha256:b2b030ac7177a5df21066addfe586d4feeb1378acc2535c4efabb0f0b5d798cb"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_sensor_conditional_expert_routing"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_5d8306b5caf7371feeacbc09", "related:concept_generalist_cross_embodiment_vla"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T03:25:05+08:00", "source:source_5d8306b5caf7371feeacbc09 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "9d590e86cab0fa32c6d6c8e11f8930150acd2fae5c690b7b767d7b6cce4dcd75", "source_state_sha256": "533ebfde183d1498b67ffbc519ecb2bdd07d106f8adbfdef5633c3d4f26f73f4", "source_record_sha256s": {"source_5d8306b5caf7371feeacbc09": "b2b030ac7177a5df21066addfe586d4feeb1378acc2535c4efabb0f0b5d798cb"}, "raw_state_sha256": "238eb7277c16d38c93e095c2d05daa28480c297ae458d68a686d3d5dde01b306", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "8302a385fee79642d901c801373d630922f01dff1fbdf8a8f509d53274713d6c", "relation_fingerprint": {"outgoing_relations_sha256": "a74094847ba07287ec90f49b49f56c0ad88626bd8b3a045b713e838441a27992", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "a74094847ba07287ec90f49b49f56c0ad88626bd8b3a045b713e838441a27992"}, "relation_neighborhood_sha256": "a74094847ba07287ec90f49b49f56c0ad88626bd8b3a045b713e838441a27992", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "unchanged"
changes: [{"change_type": "metadata_only", "previous_statement": "# 传感器条件化专家路由\n\n根据传感器是否可用选择模态专用稀疏专家，并根据任务意图路由动作侧表示，使 VLA 能利用辅助传感器，同时在传感器缺失时退化而非整体失效。", "new_statement": "# 传感器条件化专家路由\n\n根据传感器是否可用选择模态专用稀疏专家，并根据任务意图路由动作侧表示，使 VLA 能利用辅助传感器，同时在传感器缺失时退化而非整体失效。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_5d8306b5caf7371feeacbc09", "trigger_source": "source_5d8306b5caf7371feeacbc09", "evidence_added": []}]
change_summary: "compile bundle from source_5d8306b5caf7371feeacbc09"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "compile bundle from source_5d8306b5caf7371feeacbc09",
  "changes": [
    {
      "change_type": "metadata_only",
      "changed_fields": [
        "source_ids",
        "evidence",
        "last_verified_at"
      ],
      "evidence_added": [],
      "new_statement": "# 传感器条件化专家路由\n\n根据传感器是否可用选择模态专用稀疏专家，并根据任务意图路由动作侧表示，使 VLA 能利用辅助传感器，同时在传感器缺失时退化而非整体失效。",
      "previous_statement": "# 传感器条件化专家路由\n\n根据传感器是否可用选择模态专用稀疏专家，并根据任务意图路由动作侧表示，使 VLA 能利用辅助传感器，同时在传感器缺失时退化而非整体失效。",
      "reason": "compile bundle from source_5d8306b5caf7371feeacbc09",
      "trigger_source": "source_5d8306b5caf7371feeacbc09"
    }
  ],
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
        "candidate:concept_sensor_conditional_expert_routing"
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
        "object_updated_at:2026-07-19T03:25:05+08:00",
        "source:source_5d8306b5caf7371feeacbc09 work_sha256:none"
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
        "source:source_5d8306b5caf7371feeacbc09 record_sha256:b2b030ac7177a5df21066addfe586d4feeb1378acc2535c4efabb0f0b5d798cb"
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
        "source:source_5d8306b5caf7371feeacbc09 raw_sha256:4793c2e64e6d67a02a4f3e62b2d6376eb1ea7493edc6706c70f3fc79e735b3ca"
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
        "related:source_5d8306b5caf7371feeacbc09",
        "related:concept_generalist_cross_embodiment_vla"
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
        "validated:vault/memory/concept/concept_sensor_conditional_expert_routing.md"
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
  "completed_at": "2026-07-19T03:25:13+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "9d590e86cab0fa32c6d6c8e11f8930150acd2fae5c690b7b767d7b6cce4dcd75",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "238eb7277c16d38c93e095c2d05daa28480c297ae458d68a686d3d5dde01b306",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "a74094847ba07287ec90f49b49f56c0ad88626bd8b3a045b713e838441a27992",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "a74094847ba07287ec90f49b49f56c0ad88626bd8b3a045b713e838441a27992"
    },
    "relation_neighborhood_sha256": "a74094847ba07287ec90f49b49f56c0ad88626bd8b3a045b713e838441a27992",
    "source_record_sha256s": {
      "source_5d8306b5caf7371feeacbc09": "b2b030ac7177a5df21066addfe586d4feeb1378acc2535c4efabb0f0b5d798cb"
    },
    "source_state_sha256": "533ebfde183d1498b67ffbc519ecb2bdd07d106f8adbfdef5633c3d4f26f73f4",
    "work_identity_sha256": "8302a385fee79642d901c801373d630922f01dff1fbdf8a8f509d53274713d6c"
  },
  "consolidation_id": "consolidation_568c97c25c770825fd0ea416",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T03:25:13+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_568c97c25c770825fd0ea416",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_sensor_conditional_expert_routing",
  "object_sha256_after": "9d590e86cab0fa32c6d6c8e11f8930150acd2fae5c690b7b767d7b6cce4dcd75",
  "object_sha256_before": "13d56fa218033b436a703850b943ab3843faf5b968d4991299365274f897b0e3",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_5d8306b5caf7371feeacbc09"
  ],
  "source_records": [
    {
      "raw_content_sha256": "4793c2e64e6d67a02a4f3e62b2d6376eb1ea7493edc6706c70f3fc79e735b3ca",
      "source_id": "source_5d8306b5caf7371feeacbc09",
      "source_record_sha256": "b2b030ac7177a5df21066addfe586d4feeb1378acc2535c4efabb0f0b5d798cb",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "4793c2e64e6d67a02a4f3e62b2d6376eb1ea7493edc6706c70f3fc79e735b3ca"
  ],
  "started_at": "2026-07-19T03:25:13+08:00",
  "status": "complete",
  "title": "Consolidation: 传感器条件化专家路由",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T03:25:13+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
