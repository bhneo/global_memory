---
id: "consolidation_36eef696391a51a2e3d66531"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 从第一视角采集到跨本体训练的具身数据工具链"
created_at: "2026-07-26T12:33:41+08:00"
updated_at: "2026-07-26T12:33:41+08:00"
consolidation_id: "consolidation_36eef696391a51a2e3d66531"
object_id: "concept_9d0aea7bfb560c703b51d683"
object_version_before: 1
object_sha256_before: "7ac7ba1e0bf6d181dac68c0d858138e1ef553049704848ad9e0378b03b2f1c76"
object_sha256_after: "c42c6af32bbfd6246b9a79ad089ea264268e0571276f1af8ec071481cd842c3b"
source_ids: ["source_1f84f8abfca8810ebd19d85b"]
source_sha256s: ["44f0fa8dbb55fc4c0513f5374c1bc3683e6865e8592a1267340f84b80d547794"]
source_records: [{"source_id": "source_1f84f8abfca8810ebd19d85b", "source_record_sha256": "a64b42b1c61f6d063d6921a4273ad0aea1f267de490b22d5a013dd83f0a0cfaf", "raw_content_sha256": "44f0fa8dbb55fc4c0513f5374c1bc3683e6865e8592a1267340f84b80d547794", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:41+08:00"
completed_at: "2026-07-26T12:33:41+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_9d0aea7bfb560c703b51d683.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_1f84f8abfca8810ebd19d85b raw_sha256:44f0fa8dbb55fc4c0513f5374c1bc3683e6865e8592a1267340f84b80d547794"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_1f84f8abfca8810ebd19d85b record_sha256:a64b42b1c61f6d063d6921a4273ad0aea1f267de490b22d5a013dd83f0a0cfaf"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_9d0aea7bfb560c703b51d683"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_1f84f8abfca8810ebd19d85b", "related:concept_embodied_data_loop"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-23T18:06:57+08:00", "source:source_1f84f8abfca8810ebd19d85b work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "c42c6af32bbfd6246b9a79ad089ea264268e0571276f1af8ec071481cd842c3b", "source_state_sha256": "ffacd01567e74acb9c90cfe911bc0228b255eb0bd75b3cf2a008cf670c267ced", "source_record_sha256s": {"source_1f84f8abfca8810ebd19d85b": "a64b42b1c61f6d063d6921a4273ad0aea1f267de490b22d5a013dd83f0a0cfaf"}, "raw_state_sha256": "22554ed7ae5296921bd86d5acb55e86912f4f349d558235e1ac38ca562ac09f3", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "9557d23eb94a3c8cbee1745af5e381e513c7eec107a97760840f35801cca836c", "relation_fingerprint": {"outgoing_relations_sha256": "db63e7b3bc7a2f5ef224d144acd23d732f550e8428ff95ea7489183b25037785", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "db63e7b3bc7a2f5ef224d144acd23d732f550e8428ff95ea7489183b25037785"}, "relation_neighborhood_sha256": "db63e7b3bc7a2f5ef224d144acd23d732f550e8428ff95ea7489183b25037785", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_9d0aea7bfb560c703b51d683"
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
        "object_updated_at:2026-07-23T18:06:57+08:00",
        "source:source_1f84f8abfca8810ebd19d85b work_sha256:none"
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
        "source:source_1f84f8abfca8810ebd19d85b record_sha256:a64b42b1c61f6d063d6921a4273ad0aea1f267de490b22d5a013dd83f0a0cfaf"
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
        "source:source_1f84f8abfca8810ebd19d85b raw_sha256:44f0fa8dbb55fc4c0513f5374c1bc3683e6865e8592a1267340f84b80d547794"
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
        "related:source_1f84f8abfca8810ebd19d85b",
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
        "validated:vault/memory/concept/concept_9d0aea7bfb560c703b51d683.md"
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
  "completed_at": "2026-07-26T12:33:41+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "c42c6af32bbfd6246b9a79ad089ea264268e0571276f1af8ec071481cd842c3b",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "22554ed7ae5296921bd86d5acb55e86912f4f349d558235e1ac38ca562ac09f3",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "db63e7b3bc7a2f5ef224d144acd23d732f550e8428ff95ea7489183b25037785",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "db63e7b3bc7a2f5ef224d144acd23d732f550e8428ff95ea7489183b25037785"
    },
    "relation_neighborhood_sha256": "db63e7b3bc7a2f5ef224d144acd23d732f550e8428ff95ea7489183b25037785",
    "source_record_sha256s": {
      "source_1f84f8abfca8810ebd19d85b": "a64b42b1c61f6d063d6921a4273ad0aea1f267de490b22d5a013dd83f0a0cfaf"
    },
    "source_state_sha256": "ffacd01567e74acb9c90cfe911bc0228b255eb0bd75b3cf2a008cf670c267ced",
    "work_identity_sha256": "9557d23eb94a3c8cbee1745af5e381e513c7eec107a97760840f35801cca836c"
  },
  "consolidation_id": "consolidation_36eef696391a51a2e3d66531",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:41+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_36eef696391a51a2e3d66531",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_9d0aea7bfb560c703b51d683",
  "object_sha256_after": "c42c6af32bbfd6246b9a79ad089ea264268e0571276f1af8ec071481cd842c3b",
  "object_sha256_before": "7ac7ba1e0bf6d181dac68c0d858138e1ef553049704848ad9e0378b03b2f1c76",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_1f84f8abfca8810ebd19d85b"
  ],
  "source_records": [
    {
      "raw_content_sha256": "44f0fa8dbb55fc4c0513f5374c1bc3683e6865e8592a1267340f84b80d547794",
      "source_id": "source_1f84f8abfca8810ebd19d85b",
      "source_record_sha256": "a64b42b1c61f6d063d6921a4273ad0aea1f267de490b22d5a013dd83f0a0cfaf",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "44f0fa8dbb55fc4c0513f5374c1bc3683e6865e8592a1267340f84b80d547794"
  ],
  "started_at": "2026-07-26T12:33:41+08:00",
  "status": "complete",
  "title": "Consolidation: 从第一视角采集到跨本体训练的具身数据工具链",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:41+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
