---
id: "consolidation_f33b7146f691ddb531b52d01"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 可靠价值驱动的离线到在线策略改进"
created_at: "2026-07-28T16:31:44+08:00"
updated_at: "2026-07-28T16:31:44+08:00"
consolidation_id: "consolidation_f33b7146f691ddb531b52d01"
object_id: "concept_4739daf4ef7eacc9153c535f"
object_version_before: 1
object_sha256_before: "3859dc3eec0946de2551efdddc6b622b92c40b17f7cd28a987e8b2cf5edee0e9"
object_sha256_after: "366339ab6ac7b8f7ddef0aef4f22e76064cf035a22e046ff340b2645ee5605a2"
source_ids: ["source_7b278ba348f2a8bb94cce1fc", "source_e326446389e083c6ba9c94c2"]
source_sha256s: ["1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "a4b4478068c3f446e7c102b61dac030838357d1d190f678139674fd0cf4e9251"]
source_records: [{"source_id": "source_7b278ba348f2a8bb94cce1fc", "source_record_sha256": "eb51e254e90199545afc7f545d222beb01e366afac889f6eb2b866ec4235e003", "raw_content_sha256": "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "work_id": null, "work_document_sha256": null}, {"source_id": "source_e326446389e083c6ba9c94c2", "source_record_sha256": "b09217e1b8adc7659af388b2015806395a8eadaf82ae9f532b647ee7f980c2f4", "raw_content_sha256": "a4b4478068c3f446e7c102b61dac030838357d1d190f678139674fd0cf4e9251", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-28T16:31:44+08:00"
completed_at: "2026-07-28T16:31:44+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_4739daf4ef7eacc9153c535f.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_7b278ba348f2a8bb94cce1fc raw_sha256:1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "source:source_e326446389e083c6ba9c94c2 raw_sha256:a4b4478068c3f446e7c102b61dac030838357d1d190f678139674fd0cf4e9251"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_7b278ba348f2a8bb94cce1fc record_sha256:eb51e254e90199545afc7f545d222beb01e366afac889f6eb2b866ec4235e003", "source:source_e326446389e083c6ba9c94c2 record_sha256:b09217e1b8adc7659af388b2015806395a8eadaf82ae9f532b647ee7f980c2f4"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 2 candidates inspected", "candidate:concept_4739daf4ef7eacc9153c535f", "candidate:synthesis_a4a2bd5ddcee562f2574676f"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:concept_abb38fe58cbeee09ce87a01d", "related:source_7b278ba348f2a8bb94cce1fc"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-28T16:31:28+08:00", "source:source_7b278ba348f2a8bb94cce1fc work_sha256:none", "source:source_e326446389e083c6ba9c94c2 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "366339ab6ac7b8f7ddef0aef4f22e76064cf035a22e046ff340b2645ee5605a2", "source_state_sha256": "64534e5e6ae0f8346e3326e6235775c07572fd0b62dc25279bdc3b22fb62fd4e", "source_record_sha256s": {"source_7b278ba348f2a8bb94cce1fc": "eb51e254e90199545afc7f545d222beb01e366afac889f6eb2b866ec4235e003", "source_e326446389e083c6ba9c94c2": "b09217e1b8adc7659af388b2015806395a8eadaf82ae9f532b647ee7f980c2f4"}, "raw_state_sha256": "53ec12b50a9bbbb09d174314da4ea5b30c3d40b5169524a0e146580be9793b4b", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "3004a54e631a216145b5b43a0509d97f5784f9f501a3c468ebb16c0f6a497103", "relation_fingerprint": {"outgoing_relations_sha256": "a6f2b8b7d8038e6a2c7ac63430dd02758855c904b230fbb5c1ee7b26c6e358ae", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "a6f2b8b7d8038e6a2c7ac63430dd02758855c904b230fbb5c1ee7b26c6e358ae"}, "relation_neighborhood_sha256": "a6f2b8b7d8038e6a2c7ac63430dd02758855c904b230fbb5c1ee7b26c6e358ae", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "refined"
changes: [{"change_type": "refine", "previous_statement": "# 可靠价值驱动的离线到在线策略改进\n\n可靠价值驱动的离线到在线策略改进，是先用历史条件价值估计减少阶段歧义，再把价值差分转为动作质量条件，并用同一信号过滤在线片段和门控轻量残差适配；其风险是价值偏差会通过数据选择被自我强化。", "new_statement": "# 可靠价值驱动的离线到在线策略改进\n\n可靠价值驱动的离线到在线策略改进，是先用历史条件价值估计减少阶段歧义，再把价值差分转为动作质量条件，并用同一信号过滤在线片段和门控轻量残差适配；其风险是价值偏差会通过数据选择被自我强化。\n\n## 新增来源材料\n\n- `source_e326446389e083c6ba9c94c2`：可靠价值驱动的离线到在线改进需要在价值学习之前增加代理校准门禁。若训练标签来自归一化时间，必须先检验停滞、倒退与非均匀进度，并用跨轨迹状态一致性或其他物理信号校正；历史条件价值随后才能用于质量条件、在线片段筛选和残差门控。跨轨迹视觉相似与价值估计都可能偏置，因此两级置信度必须分别评估，不能由下游策略收益反向证明上游代理正确。", "changed_fields": [], "reason": "compile bundle from source_e326446389e083c6ba9c94c2", "trigger_source": "source_e326446389e083c6ba9c94c2", "evidence_added": []}]
change_summary: "compile bundle from source_e326446389e083c6ba9c94c2"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "compile bundle from source_e326446389e083c6ba9c94c2",
  "changes": [
    {
      "change_type": "refine",
      "changed_fields": [],
      "evidence_added": [],
      "new_statement": "# 可靠价值驱动的离线到在线策略改进\n\n可靠价值驱动的离线到在线策略改进，是先用历史条件价值估计减少阶段歧义，再把价值差分转为动作质量条件，并用同一信号过滤在线片段和门控轻量残差适配；其风险是价值偏差会通过数据选择被自我强化。\n\n## 新增来源材料\n\n- `source_e326446389e083c6ba9c94c2`：可靠价值驱动的离线到在线改进需要在价值学习之前增加代理校准门禁。若训练标签来自归一化时间，必须先检验停滞、倒退与非均匀进度，并用跨轨迹状态一致性或其他物理信号校正；历史条件价值随后才能用于质量条件、在线片段筛选和残差门控。跨轨迹视觉相似与价值估计都可能偏置，因此两级置信度必须分别评估，不能由下游策略收益反向证明上游代理正确。",
      "previous_statement": "# 可靠价值驱动的离线到在线策略改进\n\n可靠价值驱动的离线到在线策略改进，是先用历史条件价值估计减少阶段歧义，再把价值差分转为动作质量条件，并用同一信号过滤在线片段和门控轻量残差适配；其风险是价值偏差会通过数据选择被自我强化。",
      "reason": "compile bundle from source_e326446389e083c6ba9c94c2",
      "trigger_source": "source_e326446389e083c6ba9c94c2"
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
        "searched title; 2 candidates inspected",
        "candidate:concept_4739daf4ef7eacc9153c535f",
        "candidate:synthesis_a4a2bd5ddcee562f2574676f"
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
        "object_updated_at:2026-07-28T16:31:28+08:00",
        "source:source_7b278ba348f2a8bb94cce1fc work_sha256:none",
        "source:source_e326446389e083c6ba9c94c2 work_sha256:none"
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
        "source:source_7b278ba348f2a8bb94cce1fc record_sha256:eb51e254e90199545afc7f545d222beb01e366afac889f6eb2b866ec4235e003",
        "source:source_e326446389e083c6ba9c94c2 record_sha256:b09217e1b8adc7659af388b2015806395a8eadaf82ae9f532b647ee7f980c2f4"
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
        "source:source_7b278ba348f2a8bb94cce1fc raw_sha256:1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9",
        "source:source_e326446389e083c6ba9c94c2 raw_sha256:a4b4478068c3f446e7c102b61dac030838357d1d190f678139674fd0cf4e9251"
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
        "related:concept_abb38fe58cbeee09ce87a01d",
        "related:source_7b278ba348f2a8bb94cce1fc"
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
        "validated:vault/memory/concept/concept_4739daf4ef7eacc9153c535f.md"
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
        "distinct_source_ids:2",
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
  "completed_at": "2026-07-28T16:31:44+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "366339ab6ac7b8f7ddef0aef4f22e76064cf035a22e046ff340b2645ee5605a2",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "53ec12b50a9bbbb09d174314da4ea5b30c3d40b5169524a0e146580be9793b4b",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "a6f2b8b7d8038e6a2c7ac63430dd02758855c904b230fbb5c1ee7b26c6e358ae",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "a6f2b8b7d8038e6a2c7ac63430dd02758855c904b230fbb5c1ee7b26c6e358ae"
    },
    "relation_neighborhood_sha256": "a6f2b8b7d8038e6a2c7ac63430dd02758855c904b230fbb5c1ee7b26c6e358ae",
    "source_record_sha256s": {
      "source_7b278ba348f2a8bb94cce1fc": "eb51e254e90199545afc7f545d222beb01e366afac889f6eb2b866ec4235e003",
      "source_e326446389e083c6ba9c94c2": "b09217e1b8adc7659af388b2015806395a8eadaf82ae9f532b647ee7f980c2f4"
    },
    "source_state_sha256": "64534e5e6ae0f8346e3326e6235775c07572fd0b62dc25279bdc3b22fb62fd4e",
    "work_identity_sha256": "3004a54e631a216145b5b43a0509d97f5784f9f501a3c468ebb16c0f6a497103"
  },
  "consolidation_id": "consolidation_f33b7146f691ddb531b52d01",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-28T16:31:44+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_f33b7146f691ddb531b52d01",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_4739daf4ef7eacc9153c535f",
  "object_sha256_after": "366339ab6ac7b8f7ddef0aef4f22e76064cf035a22e046ff340b2645ee5605a2",
  "object_sha256_before": "3859dc3eec0946de2551efdddc6b622b92c40b17f7cd28a987e8b2cf5edee0e9",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "refined",
  "source_ids": [
    "source_7b278ba348f2a8bb94cce1fc",
    "source_e326446389e083c6ba9c94c2"
  ],
  "source_records": [
    {
      "raw_content_sha256": "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9",
      "source_id": "source_7b278ba348f2a8bb94cce1fc",
      "source_record_sha256": "eb51e254e90199545afc7f545d222beb01e366afac889f6eb2b866ec4235e003",
      "work_document_sha256": null,
      "work_id": null
    },
    {
      "raw_content_sha256": "a4b4478068c3f446e7c102b61dac030838357d1d190f678139674fd0cf4e9251",
      "source_id": "source_e326446389e083c6ba9c94c2",
      "source_record_sha256": "b09217e1b8adc7659af388b2015806395a8eadaf82ae9f532b647ee7f980c2f4",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9",
    "a4b4478068c3f446e7c102b61dac030838357d1d190f678139674fd0cf4e9251"
  ],
  "started_at": "2026-07-28T16:31:44+08:00",
  "status": "complete",
  "title": "Consolidation: 可靠价值驱动的离线到在线策略改进",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-28T16:31:44+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
