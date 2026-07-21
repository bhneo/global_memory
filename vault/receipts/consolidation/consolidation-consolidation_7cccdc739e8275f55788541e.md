---
id: "consolidation_7cccdc739e8275f55788541e"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 连续曲线动作接口与执行重定时"
created_at: "2026-07-20T13:34:43+08:00"
updated_at: "2026-07-20T13:34:43+08:00"
consolidation_id: "consolidation_7cccdc739e8275f55788541e"
object_id: "concept_17750931a381f8453b27ccba"
object_version_before: 1
object_sha256_before: "43993bdb4af08256faf3f74bc3d79143a4b537d1e3e52739825e3caa4da87975"
object_sha256_after: "069887173e9fff554c40d32317520e31e05ec1dbb6a28b86f636e438e5edf646"
source_ids: ["source_4b25f596c34869693b9b8151"]
source_sha256s: ["95a283c498946d7e5f99ce2721d85b2c9543d84e77d848407cd61f6b6eb251d6"]
source_records: [{"source_id": "source_4b25f596c34869693b9b8151", "source_record_sha256": "7aabf7b7e1b8cdc47fc2f05799dabf8a177c03420d83f83e869d2894a232bd4e", "raw_content_sha256": "95a283c498946d7e5f99ce2721d85b2c9543d84e77d848407cd61f6b6eb251d6", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-20T13:34:42+08:00"
completed_at: "2026-07-20T13:34:43+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_17750931a381f8453b27ccba.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_4b25f596c34869693b9b8151 raw_sha256:95a283c498946d7e5f99ce2721d85b2c9543d84e77d848407cd61f6b6eb251d6"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_4b25f596c34869693b9b8151 record_sha256:7aabf7b7e1b8cdc47fc2f05799dabf8a177c03420d83f83e869d2894a232bd4e"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_17750931a381f8453b27ccba"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 3 related objects found", "related:source_4b25f596c34869693b9b8151", "related:concept_d01c4f0b61292d29f0a7ffe2", "related:concept_dynamic_execution_horizon"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-20T13:34:34+08:00", "source:source_4b25f596c34869693b9b8151 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "069887173e9fff554c40d32317520e31e05ec1dbb6a28b86f636e438e5edf646", "source_state_sha256": "d861e73d6632f0037f21153c5a947eb16ea293ec4eacda8e30a3ca76a73dde38", "source_record_sha256s": {"source_4b25f596c34869693b9b8151": "7aabf7b7e1b8cdc47fc2f05799dabf8a177c03420d83f83e869d2894a232bd4e"}, "raw_state_sha256": "942269036c67b602112a68bb6ffb4c98f99a72e0e4c379d6da9ad97c38ee48f0", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "29ce6d34ea30a05d2e54c028152fb8eb5d36aa08f41279fe1402d7b352faf239", "relation_fingerprint": {"outgoing_relations_sha256": "30b256762ce0fd6f12dafbbaef417d0a45aca601ff375e3fdd0a9520339fbc33", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "30b256762ce0fd6f12dafbbaef417d0a45aca601ff375e3fdd0a9520339fbc33"}, "relation_neighborhood_sha256": "30b256762ce0fd6f12dafbbaef417d0a45aca601ff375e3fdd0a9520339fbc33", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "refined"
changes: [{"change_type": "refine", "previous_statement": "# 连续曲线动作接口与执行重定时\n\n策略输出参数化连续动作曲线而非固定采样的离散动作块，使轨迹几何能够被高频采样、按时间缩放并在相邻预测段之间对齐。该接口把动作表示与执行时标解耦，但可用倍速仍受接触动力学、低层控制器和执行器裕度限制。", "new_statement": "# 连续曲线动作接口与执行重定时\n\n策略输出参数化连续动作曲线而非固定采样的离散动作块，使轨迹几何能够被高频采样、按时间缩放并在相邻预测段之间对齐。该接口把动作表示与执行时标解耦，但可用倍速仍受接触动力学、低层控制器和执行器裕度限制。", "changed_fields": [], "reason": "compile bundle from source_4b25f596c34869693b9b8151", "trigger_source": "source_4b25f596c34869693b9b8151", "evidence_added": []}]
change_summary: "compile bundle from source_4b25f596c34869693b9b8151"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "compile bundle from source_4b25f596c34869693b9b8151",
  "changes": [
    {
      "change_type": "refine",
      "changed_fields": [],
      "evidence_added": [],
      "new_statement": "# 连续曲线动作接口与执行重定时\n\n策略输出参数化连续动作曲线而非固定采样的离散动作块，使轨迹几何能够被高频采样、按时间缩放并在相邻预测段之间对齐。该接口把动作表示与执行时标解耦，但可用倍速仍受接触动力学、低层控制器和执行器裕度限制。",
      "previous_statement": "# 连续曲线动作接口与执行重定时\n\n策略输出参数化连续动作曲线而非固定采样的离散动作块，使轨迹几何能够被高频采样、按时间缩放并在相邻预测段之间对齐。该接口把动作表示与执行时标解耦，但可用倍速仍受接触动力学、低层控制器和执行器裕度限制。",
      "reason": "compile bundle from source_4b25f596c34869693b9b8151",
      "trigger_source": "source_4b25f596c34869693b9b8151"
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
        "candidate:concept_17750931a381f8453b27ccba"
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
        "object_updated_at:2026-07-20T13:34:34+08:00",
        "source:source_4b25f596c34869693b9b8151 work_sha256:none"
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
        "source:source_4b25f596c34869693b9b8151 record_sha256:7aabf7b7e1b8cdc47fc2f05799dabf8a177c03420d83f83e869d2894a232bd4e"
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
        "source:source_4b25f596c34869693b9b8151 raw_sha256:95a283c498946d7e5f99ce2721d85b2c9543d84e77d848407cd61f6b6eb251d6"
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
        "relation index inspected; 3 related objects found",
        "related:source_4b25f596c34869693b9b8151",
        "related:concept_d01c4f0b61292d29f0a7ffe2",
        "related:concept_dynamic_execution_horizon"
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
        "validated:vault/memory/concept/concept_17750931a381f8453b27ccba.md"
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
  "completed_at": "2026-07-20T13:34:43+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "069887173e9fff554c40d32317520e31e05ec1dbb6a28b86f636e438e5edf646",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "942269036c67b602112a68bb6ffb4c98f99a72e0e4c379d6da9ad97c38ee48f0",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "30b256762ce0fd6f12dafbbaef417d0a45aca601ff375e3fdd0a9520339fbc33",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "30b256762ce0fd6f12dafbbaef417d0a45aca601ff375e3fdd0a9520339fbc33"
    },
    "relation_neighborhood_sha256": "30b256762ce0fd6f12dafbbaef417d0a45aca601ff375e3fdd0a9520339fbc33",
    "source_record_sha256s": {
      "source_4b25f596c34869693b9b8151": "7aabf7b7e1b8cdc47fc2f05799dabf8a177c03420d83f83e869d2894a232bd4e"
    },
    "source_state_sha256": "d861e73d6632f0037f21153c5a947eb16ea293ec4eacda8e30a3ca76a73dde38",
    "work_identity_sha256": "29ce6d34ea30a05d2e54c028152fb8eb5d36aa08f41279fe1402d7b352faf239"
  },
  "consolidation_id": "consolidation_7cccdc739e8275f55788541e",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-20T13:34:43+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_7cccdc739e8275f55788541e",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_17750931a381f8453b27ccba",
  "object_sha256_after": "069887173e9fff554c40d32317520e31e05ec1dbb6a28b86f636e438e5edf646",
  "object_sha256_before": "43993bdb4af08256faf3f74bc3d79143a4b537d1e3e52739825e3caa4da87975",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "refined",
  "source_ids": [
    "source_4b25f596c34869693b9b8151"
  ],
  "source_records": [
    {
      "raw_content_sha256": "95a283c498946d7e5f99ce2721d85b2c9543d84e77d848407cd61f6b6eb251d6",
      "source_id": "source_4b25f596c34869693b9b8151",
      "source_record_sha256": "7aabf7b7e1b8cdc47fc2f05799dabf8a177c03420d83f83e869d2894a232bd4e",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "95a283c498946d7e5f99ce2721d85b2c9543d84e77d848407cd61f6b6eb251d6"
  ],
  "started_at": "2026-07-20T13:34:42+08:00",
  "status": "complete",
  "title": "Consolidation: 连续曲线动作接口与执行重定时",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-20T13:34:43+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
