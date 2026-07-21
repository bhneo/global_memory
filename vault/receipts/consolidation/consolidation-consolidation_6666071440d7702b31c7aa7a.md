---
id: "consolidation_6666071440d7702b31c7aa7a"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "failed"
execution_status: "complete"
validation_outcome: "failed"
title: "Consolidation: Agentic-VLA 在 LIBERO 上报告平均成功率 97.8%，Long 套件相对 SFT 基线提升 12.3 个百分点"
created_at: "2026-07-20T11:56:41+08:00"
updated_at: "2026-07-20T11:56:41+08:00"
consolidation_id: "consolidation_6666071440d7702b31c7aa7a"
object_id: "claim_agentic_vla_libero_main_20260715"
object_version_before: 1
object_sha256_before: "e1f9b7891b16e2b913c29ff9d74f018da8777c7ad32243e15e03d6e1c2194068"
object_sha256_after: "e1f9b7891b16e2b913c29ff9d74f018da8777c7ad32243e15e03d6e1c2194068"
source_ids: ["source_2c21320690e566fbbf80fd75"]
source_sha256s: ["8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43"]
source_records: [{"source_id": "source_2c21320690e566fbbf80fd75", "source_record_sha256": "f45509bd9142b118ffa0790c0c0f8cafc12a336c4817db27c3ea1634d0018513", "raw_content_sha256": "8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-20T11:56:41+08:00"
completed_at: "2026-07-20T11:56:41+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": false, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/claim/claim_agentic_vla_libero_main_20260715.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_2c21320690e566fbbf80fd75 raw_sha256:8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_2c21320690e566fbbf80fd75 record_sha256:f45509bd9142b118ffa0790c0c0f8cafc12a336c4817db27c3ea1634d0018513"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["evidence:source_2c21320690e566fbbf80fd75", "evidence:source_2c21320690e566fbbf80fd75", "evidence:source_2c21320690e566fbbf80fd75"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "failed", "validation_outcome": "blocked", "method": "declared-metadata-inspection", "semantic_recheck_performed": false, "declared_value": null, "findings": ["evidence_entailment:None"], "warnings": ["claim evidence entailment not checked"]}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:claim_agentic_vla_libero_main_20260715"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_2c21320690e566fbbf80fd75"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T15:23:38+08:00", "source:source_2c21320690e566fbbf80fd75 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "e1f9b7891b16e2b913c29ff9d74f018da8777c7ad32243e15e03d6e1c2194068", "source_state_sha256": "b183c849f4701693c7977f37650b2427587f12431d50db110182a346f4a1e459", "source_record_sha256s": {"source_2c21320690e566fbbf80fd75": "f45509bd9142b118ffa0790c0c0f8cafc12a336c4817db27c3ea1634d0018513"}, "raw_state_sha256": "66319a8bb37a86a1f09fd9d17bb01f137b5d583ba9e3e9780a968dad976028c8", "evidence_sha256": "872764e82f9c86e0d72c6cf2fde09008e59e64a1c5279f84ed07b118fbb9d5b6", "extraction_state_sha256": "bb3c87144222d7c8dbbaaf8d80c24b5ea824941c9f5de00189a04405ba193283", "work_identity_sha256": "a08f1abff1e75024db50cdcd272ee91bce2e46d9ce1813171e887755926028f0", "relation_fingerprint": {"outgoing_relations_sha256": "4d443c9afd6a1ef2f5ebb2d5063e77522d6031cd773cabcb494559b9bcbac89a", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "4d443c9afd6a1ef2f5ebb2d5063e77522d6031cd773cabcb494559b9bcbac89a"}, "relation_neighborhood_sha256": "4d443c9afd6a1ef2f5ebb2d5063e77522d6031cd773cabcb494559b9bcbac89a", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "failed"
changes: []
change_summary: "No semantic change."
warnings: ["claim evidence entailment not checked"]
exceptions_created: []
promotion_recommendation: "blocked"
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
        "candidate:claim_agentic_vla_libero_main_20260715"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "check_name": "evidence_entailment_rechecked",
      "declared_value": null,
      "execution_status": "failed",
      "findings": [
        "evidence_entailment:None"
      ],
      "method": "declared-metadata-inspection",
      "semantic_recheck_performed": false,
      "validation_outcome": "blocked",
      "warnings": [
        "claim evidence entailment not checked"
      ]
    },
    "evidence_revalidated": {
      "check_name": "evidence_revalidated",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "evidence:source_2c21320690e566fbbf80fd75",
        "evidence:source_2c21320690e566fbbf80fd75",
        "evidence:source_2c21320690e566fbbf80fd75"
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
        "object_updated_at:2026-07-17T15:23:38+08:00",
        "source:source_2c21320690e566fbbf80fd75 work_sha256:none"
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
        "source:source_2c21320690e566fbbf80fd75 record_sha256:f45509bd9142b118ffa0790c0c0f8cafc12a336c4817db27c3ea1634d0018513"
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
        "source:source_2c21320690e566fbbf80fd75 raw_sha256:8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43"
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
        "related:source_2c21320690e566fbbf80fd75"
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
        "validated:vault/memory/claim/claim_agentic_vla_libero_main_20260715.md"
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
    "evidence_entailment_rechecked": false,
    "evidence_revalidated": true,
    "freshness_checked": true,
    "provenance_revalidated": true,
    "raw_available": true,
    "related_object_search_completed": true,
    "schema_validated": true,
    "source_independence_checked": true
  },
  "completed_at": "2026-07-20T11:56:41+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "872764e82f9c86e0d72c6cf2fde09008e59e64a1c5279f84ed07b118fbb9d5b6",
    "extraction_state_sha256": "bb3c87144222d7c8dbbaaf8d80c24b5ea824941c9f5de00189a04405ba193283",
    "memory_schema_version": 2,
    "object_sha256": "e1f9b7891b16e2b913c29ff9d74f018da8777c7ad32243e15e03d6e1c2194068",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "66319a8bb37a86a1f09fd9d17bb01f137b5d583ba9e3e9780a968dad976028c8",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "4d443c9afd6a1ef2f5ebb2d5063e77522d6031cd773cabcb494559b9bcbac89a",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "4d443c9afd6a1ef2f5ebb2d5063e77522d6031cd773cabcb494559b9bcbac89a"
    },
    "relation_neighborhood_sha256": "4d443c9afd6a1ef2f5ebb2d5063e77522d6031cd773cabcb494559b9bcbac89a",
    "source_record_sha256s": {
      "source_2c21320690e566fbbf80fd75": "f45509bd9142b118ffa0790c0c0f8cafc12a336c4817db27c3ea1634d0018513"
    },
    "source_state_sha256": "b183c849f4701693c7977f37650b2427587f12431d50db110182a346f4a1e459",
    "work_identity_sha256": "a08f1abff1e75024db50cdcd272ee91bce2e46d9ce1813171e887755926028f0"
  },
  "consolidation_id": "consolidation_6666071440d7702b31c7aa7a",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-20T11:56:41+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_6666071440d7702b31c7aa7a",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_agentic_vla_libero_main_20260715",
  "object_sha256_after": "e1f9b7891b16e2b913c29ff9d74f018da8777c7ad32243e15e03d6e1c2194068",
  "object_sha256_before": "e1f9b7891b16e2b913c29ff9d74f018da8777c7ad32243e15e03d6e1c2194068",
  "object_version_before": 1,
  "promotion_recommendation": "blocked",
  "receipt_schema_version": 2,
  "result": "failed",
  "source_ids": [
    "source_2c21320690e566fbbf80fd75"
  ],
  "source_records": [
    {
      "raw_content_sha256": "8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43",
      "source_id": "source_2c21320690e566fbbf80fd75",
      "source_record_sha256": "f45509bd9142b118ffa0790c0c0f8cafc12a336c4817db27c3ea1634d0018513",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43"
  ],
  "started_at": "2026-07-20T11:56:41+08:00",
  "status": "failed",
  "title": "Consolidation: Agentic-VLA 在 LIBERO 上报告平均成功率 97.8%，Long 套件相对 SFT 基线提升 12.3 个百分点",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-20T11:56:41+08:00",
  "validation_outcome": "failed",
  "warnings": [
    "claim evidence entailment not checked"
  ]
}
```
