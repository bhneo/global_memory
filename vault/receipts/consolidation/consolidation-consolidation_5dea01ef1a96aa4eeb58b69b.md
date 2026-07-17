---
id: "consolidation_5dea01ef1a96aa4eeb58b69b"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "failed"
execution_status: "complete"
validation_outcome: "failed"
title: "Consolidation: VIA 表明通用视觉 Agent 可在限定仿真任务中通过工具界面零样本闭环控制机器人"
created_at: "2026-07-17T22:40:15+08:00"
updated_at: "2026-07-17T22:40:15+08:00"
consolidation_id: "consolidation_5dea01ef1a96aa4eeb58b69b"
object_id: "claim_via_interface_first_robot_control_20260715"
object_version_before: 1
object_sha256_before: "1611382d982c34ef44cef8f51990e8986efaaad97106ef10675607dd656b65fa"
object_sha256_after: "1611382d982c34ef44cef8f51990e8986efaaad97106ef10675607dd656b65fa"
source_ids: ["source_86bad679192d3c34f728058b"]
source_sha256s: ["2261759e82c3f512a15fb870e5264fae5883efaff11c9917424894998be7cde3"]
source_records: [{"source_id": "source_86bad679192d3c34f728058b", "source_record_sha256": "36216fd9dd8b16625d880d5691bfba8e6b077716deb3f9d7acf2da32e0073d72", "raw_content_sha256": "2261759e82c3f512a15fb870e5264fae5883efaff11c9917424894998be7cde3", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-17T22:40:14+08:00"
completed_at: "2026-07-17T22:40:15+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": false, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/knowledge/claims/claim_via_interface_first_robot_control_20260715-via-表明稳定的视觉工具界面可让通用-agent-在限定仿真任务中零样本闭环控制机器人.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_86bad679192d3c34f728058b raw_sha256:2261759e82c3f512a15fb870e5264fae5883efaff11c9917424894998be7cde3"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_86bad679192d3c34f728058b record_sha256:36216fd9dd8b16625d880d5691bfba8e6b077716deb3f9d7acf2da32e0073d72"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["evidence:source_86bad679192d3c34f728058b", "evidence:source_86bad679192d3c34f728058b", "evidence:source_86bad679192d3c34f728058b"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "failed", "validation_outcome": "blocked", "method": "declared-metadata-inspection", "semantic_recheck_performed": false, "declared_value": null, "findings": ["evidence_entailment:None"], "warnings": ["claim evidence entailment not checked"]}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:claim_via_interface_first_robot_control_20260715"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_86bad679192d3c34f728058b"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-15T11:48:55+08:00", "source:source_86bad679192d3c34f728058b work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "1611382d982c34ef44cef8f51990e8986efaaad97106ef10675607dd656b65fa", "source_state_sha256": "89843104a57dc51ae5a323c01c8c3bdf994eb06e1d12ce43698f5ba4ecda7edc", "source_record_sha256s": {"source_86bad679192d3c34f728058b": "36216fd9dd8b16625d880d5691bfba8e6b077716deb3f9d7acf2da32e0073d72"}, "raw_state_sha256": "23e2d1deb36c6ce25d353243e4277e10343f1173d417c56b426476a797982ed9", "evidence_sha256": "1761543a0f1f371f8c01ad6f3bf0040e3d472430164d8012605a8ccfaf94f41e", "extraction_state_sha256": "bb3c87144222d7c8dbbaaf8d80c24b5ea824941c9f5de00189a04405ba193283", "work_identity_sha256": "63a242c0c6fd285b0e61dfb29fc19851a2a30b9a41257983e15db3fdd198ca5f", "relation_fingerprint": {"outgoing_relations_sha256": "189db1fa9302fae03b34c892e3884f00d034f8d2b893d48dff4f58f3fca88d3b", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "189db1fa9302fae03b34c892e3884f00d034f8d2b893d48dff4f58f3fca88d3b"}, "relation_neighborhood_sha256": "189db1fa9302fae03b34c892e3884f00d034f8d2b893d48dff4f58f3fca88d3b", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "canonical_approved"
changes: []
change_summary: "Receipt v2 revalidated under incoming and outgoing relation fingerprint boundary"
warnings: ["claim evidence entailment not checked"]
exceptions_created: []
promotion_recommendation: "blocked"
---

# Consolidation Receipt

```json
{
  "change_summary": "Receipt v2 revalidated under incoming and outgoing relation fingerprint boundary",
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
        "candidate:claim_via_interface_first_robot_control_20260715"
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
        "evidence:source_86bad679192d3c34f728058b",
        "evidence:source_86bad679192d3c34f728058b",
        "evidence:source_86bad679192d3c34f728058b"
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
        "object_updated_at:2026-07-15T11:48:55+08:00",
        "source:source_86bad679192d3c34f728058b work_sha256:none"
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
        "source:source_86bad679192d3c34f728058b record_sha256:36216fd9dd8b16625d880d5691bfba8e6b077716deb3f9d7acf2da32e0073d72"
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
        "source:source_86bad679192d3c34f728058b raw_sha256:2261759e82c3f512a15fb870e5264fae5883efaff11c9917424894998be7cde3"
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
        "related:source_86bad679192d3c34f728058b"
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
        "validated:vault/knowledge/claims/claim_via_interface_first_robot_control_20260715-via-表明稳定的视觉工具界面可让通用-agent-在限定仿真任务中零样本闭环控制机器人.md"
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
  "completed_at": "2026-07-17T22:40:15+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "1761543a0f1f371f8c01ad6f3bf0040e3d472430164d8012605a8ccfaf94f41e",
    "extraction_state_sha256": "bb3c87144222d7c8dbbaaf8d80c24b5ea824941c9f5de00189a04405ba193283",
    "memory_schema_version": 2,
    "object_sha256": "1611382d982c34ef44cef8f51990e8986efaaad97106ef10675607dd656b65fa",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "23e2d1deb36c6ce25d353243e4277e10343f1173d417c56b426476a797982ed9",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "189db1fa9302fae03b34c892e3884f00d034f8d2b893d48dff4f58f3fca88d3b",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "189db1fa9302fae03b34c892e3884f00d034f8d2b893d48dff4f58f3fca88d3b"
    },
    "relation_neighborhood_sha256": "189db1fa9302fae03b34c892e3884f00d034f8d2b893d48dff4f58f3fca88d3b",
    "source_record_sha256s": {
      "source_86bad679192d3c34f728058b": "36216fd9dd8b16625d880d5691bfba8e6b077716deb3f9d7acf2da32e0073d72"
    },
    "source_state_sha256": "89843104a57dc51ae5a323c01c8c3bdf994eb06e1d12ce43698f5ba4ecda7edc",
    "work_identity_sha256": "63a242c0c6fd285b0e61dfb29fc19851a2a30b9a41257983e15db3fdd198ca5f"
  },
  "consolidation_id": "consolidation_5dea01ef1a96aa4eeb58b69b",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-17T22:40:15+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_5dea01ef1a96aa4eeb58b69b",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_via_interface_first_robot_control_20260715",
  "object_sha256_after": "1611382d982c34ef44cef8f51990e8986efaaad97106ef10675607dd656b65fa",
  "object_sha256_before": "1611382d982c34ef44cef8f51990e8986efaaad97106ef10675607dd656b65fa",
  "object_version_before": 1,
  "promotion_recommendation": "blocked",
  "receipt_schema_version": 2,
  "result": "canonical_approved",
  "source_ids": [
    "source_86bad679192d3c34f728058b"
  ],
  "source_records": [
    {
      "raw_content_sha256": "2261759e82c3f512a15fb870e5264fae5883efaff11c9917424894998be7cde3",
      "source_id": "source_86bad679192d3c34f728058b",
      "source_record_sha256": "36216fd9dd8b16625d880d5691bfba8e6b077716deb3f9d7acf2da32e0073d72",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "2261759e82c3f512a15fb870e5264fae5883efaff11c9917424894998be7cde3"
  ],
  "started_at": "2026-07-17T22:40:14+08:00",
  "status": "failed",
  "title": "Consolidation: VIA 表明通用视觉 Agent 可在限定仿真任务中通过工具界面零样本闭环控制机器人",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T22:40:15+08:00",
  "validation_outcome": "failed",
  "warnings": [
    "claim evidence entailment not checked"
  ]
}
```
