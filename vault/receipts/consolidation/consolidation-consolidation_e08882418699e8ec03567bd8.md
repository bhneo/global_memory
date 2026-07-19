---
id: "consolidation_e08882418699e8ec03567bd8"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 该文称具身 VLA 迭代速度常被真机评估流程而非训练本身卡住"
created_at: "2026-07-19T12:19:58+08:00"
updated_at: "2026-07-19T12:19:58+08:00"
consolidation_id: "consolidation_e08882418699e8ec03567bd8"
object_id: "claim_wechat_embodied_eval_bottleneck_20260715"
object_version_before: 1
object_sha256_before: "8d6f37011560bfe1fbdca540d33dacb073469c9836f2b54cc17020510a55c028"
object_sha256_after: "2ed645dc767bb40b0adb8fc52a1f32e172f8848fdfccf69f25feb7b1b0c42663"
source_ids: ["source_2d4f3a7d3525782c8ff503ee"]
source_sha256s: ["2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e"]
source_records: [{"source_id": "source_2d4f3a7d3525782c8ff503ee", "source_record_sha256": "ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd", "raw_content_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_597", "ev_692"]
started_at: "2026-07-19T12:19:57+08:00"
completed_at: "2026-07-19T12:19:58+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/claim/claim_wechat_embodied_eval_bottleneck_20260715.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_2d4f3a7d3525782c8ff503ee raw_sha256:2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_2d4f3a7d3525782c8ff503ee record_sha256:ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["evidence:ev_597", "evidence:ev_692"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "passed", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": "partial", "findings": ["evidence_entailment:partial"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:claim_wechat_embodied_eval_bottleneck_20260715"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_2d4f3a7d3525782c8ff503ee", "related:claim_wechat_embodied_eval_bottleneck_20260715"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-18T16:03:01+08:00", "source:source_2d4f3a7d3525782c8ff503ee work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "2ed645dc767bb40b0adb8fc52a1f32e172f8848fdfccf69f25feb7b1b0c42663", "source_state_sha256": "ba7943f3a2a360a280c111d5d4fa02e900c28fd1d0743ff6e719806a54d51020", "source_record_sha256s": {"source_2d4f3a7d3525782c8ff503ee": "ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd"}, "raw_state_sha256": "367cb9dd55af5cae56b160a95e942a29555b8063320a400d4c76c919a838be93", "evidence_sha256": "2024bf2b575343bdff3d852dbf8673dbf5ec5a17c8f25f1a84380896a9e27911", "extraction_state_sha256": "be6ca894ad2baea92ca4faae3ba64b9d7f339f7ab06cb852d0843880f0d722fb", "work_identity_sha256": "2b60f17ed42989e9c34ce5083be81e0c2273482b4dfd868f634d47466fc7e723", "relation_fingerprint": {"outgoing_relations_sha256": "ba709688339a20492c0a45b805b2989f84763f5e6e6c95d1fbe4e91e71394508", "incoming_relations_sha256": "f3eb4a5a513bf16b4ebce665cc33b0f7ff0f53f424b25869f92ac031f53758fa", "full_neighborhood_sha256": "6c6cb1a4de0b9155af3b13af3da2b2c5807f797657a3efab7504ba90e7b76488"}, "relation_neighborhood_sha256": "6c6cb1a4de0b9155af3b13af3da2b2c5807f797657a3efab7504ba90e7b76488", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_wechat_embodied_eval_bottleneck_20260715"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "check_name": "evidence_entailment_rechecked",
      "declared_value": "partial",
      "execution_status": "completed",
      "findings": [
        "evidence_entailment:partial"
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
        "evidence:ev_597",
        "evidence:ev_692"
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
        "object_updated_at:2026-07-18T16:03:01+08:00",
        "source:source_2d4f3a7d3525782c8ff503ee work_sha256:none"
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
        "source:source_2d4f3a7d3525782c8ff503ee record_sha256:ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd"
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
        "source:source_2d4f3a7d3525782c8ff503ee raw_sha256:2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e"
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
        "related:source_2d4f3a7d3525782c8ff503ee",
        "related:claim_wechat_embodied_eval_bottleneck_20260715"
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
        "validated:vault/memory/claim/claim_wechat_embodied_eval_bottleneck_20260715.md"
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
  "completed_at": "2026-07-19T12:19:58+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "2024bf2b575343bdff3d852dbf8673dbf5ec5a17c8f25f1a84380896a9e27911",
    "extraction_state_sha256": "be6ca894ad2baea92ca4faae3ba64b9d7f339f7ab06cb852d0843880f0d722fb",
    "memory_schema_version": 2,
    "object_sha256": "2ed645dc767bb40b0adb8fc52a1f32e172f8848fdfccf69f25feb7b1b0c42663",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "367cb9dd55af5cae56b160a95e942a29555b8063320a400d4c76c919a838be93",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "6c6cb1a4de0b9155af3b13af3da2b2c5807f797657a3efab7504ba90e7b76488",
      "incoming_relations_sha256": "f3eb4a5a513bf16b4ebce665cc33b0f7ff0f53f424b25869f92ac031f53758fa",
      "outgoing_relations_sha256": "ba709688339a20492c0a45b805b2989f84763f5e6e6c95d1fbe4e91e71394508"
    },
    "relation_neighborhood_sha256": "6c6cb1a4de0b9155af3b13af3da2b2c5807f797657a3efab7504ba90e7b76488",
    "source_record_sha256s": {
      "source_2d4f3a7d3525782c8ff503ee": "ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd"
    },
    "source_state_sha256": "ba7943f3a2a360a280c111d5d4fa02e900c28fd1d0743ff6e719806a54d51020",
    "work_identity_sha256": "2b60f17ed42989e9c34ce5083be81e0c2273482b4dfd868f634d47466fc7e723"
  },
  "consolidation_id": "consolidation_e08882418699e8ec03567bd8",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T12:19:58+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_597",
    "ev_692"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_e08882418699e8ec03567bd8",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_wechat_embodied_eval_bottleneck_20260715",
  "object_sha256_after": "2ed645dc767bb40b0adb8fc52a1f32e172f8848fdfccf69f25feb7b1b0c42663",
  "object_sha256_before": "8d6f37011560bfe1fbdca540d33dacb073469c9836f2b54cc17020510a55c028",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_2d4f3a7d3525782c8ff503ee"
  ],
  "source_records": [
    {
      "raw_content_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e",
      "source_id": "source_2d4f3a7d3525782c8ff503ee",
      "source_record_sha256": "ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e"
  ],
  "started_at": "2026-07-19T12:19:57+08:00",
  "status": "complete",
  "title": "Consolidation: 该文称具身 VLA 迭代速度常被真机评估流程而非训练本身卡住",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T12:19:58+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
