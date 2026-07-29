---
id: "consolidation_1d55cc9b273ff37b0682fb37"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 接触反馈应区分短时反应、事件记忆与概率后验"
created_at: "2026-07-27T19:04:24+08:00"
updated_at: "2026-07-27T19:04:24+08:00"
consolidation_id: "consolidation_1d55cc9b273ff37b0682fb37"
object_id: "concept_2ce226e08d585158c1dfbb18"
object_version_before: 1
object_sha256_before: "46f1bf9f341f15008eb85f167d5eb4fef0f27db27fba8ccc790c57fb36ebd93b"
object_sha256_after: "332a4372384bcd4064c30a50745356e0e651baff34d9be5465edac697bfcb972"
source_ids: ["source_4e06d1b1cdcd0d07eff47909", "source_1ee2c3fae53a9d05689cd143"]
source_sha256s: ["ebbe3a63017280d609e1822b31af341c505ea3aee643726c542d201df6fcdf4e", "705e82070aa5fe4f189d766855734afaa208a93245ab19cb1570d8b902a02691"]
source_records: [{"source_id": "source_4e06d1b1cdcd0d07eff47909", "source_record_sha256": "b374bac455e32c834d10ee963468201032b77876a3822be5db85779e0f1ffb22", "raw_content_sha256": "ebbe3a63017280d609e1822b31af341c505ea3aee643726c542d201df6fcdf4e", "work_id": null, "work_document_sha256": null}, {"source_id": "source_1ee2c3fae53a9d05689cd143", "source_record_sha256": "86e22ce7451f1b3d7b8603286ba6cd7fb2b98ee0e6901c58e46371314ba35a65", "raw_content_sha256": "705e82070aa5fe4f189d766855734afaa208a93245ab19cb1570d8b902a02691", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-27T19:04:24+08:00"
completed_at: "2026-07-27T19:04:24+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_2ce226e08d585158c1dfbb18.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_4e06d1b1cdcd0d07eff47909 raw_sha256:ebbe3a63017280d609e1822b31af341c505ea3aee643726c542d201df6fcdf4e", "source:source_1ee2c3fae53a9d05689cd143 raw_sha256:705e82070aa5fe4f189d766855734afaa208a93245ab19cb1570d8b902a02691"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_4e06d1b1cdcd0d07eff47909 record_sha256:b374bac455e32c834d10ee963468201032b77876a3822be5db85779e0f1ffb22", "source:source_1ee2c3fae53a9d05689cd143 record_sha256:86e22ce7451f1b3d7b8603286ba6cd7fb2b98ee0e6901c58e46371314ba35a65"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_2ce226e08d585158c1dfbb18"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 6 related objects found", "related:source_4e06d1b1cdcd0d07eff47909", "related:concept_637cf7264723c03955c719e2", "related:concept_bb69fa188e0417143c3277cf", "related:concept_c37ccf2640da63192432d5d5", "related:concept_2ce226e08d585158c1dfbb18"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-27T19:03:59+08:00", "source:source_4e06d1b1cdcd0d07eff47909 work_sha256:none", "source:source_1ee2c3fae53a9d05689cd143 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "332a4372384bcd4064c30a50745356e0e651baff34d9be5465edac697bfcb972", "source_state_sha256": "5506ffb1c1686f7a36164ca35c5322bc7b41f568985af3e3aa1b95b16629216a", "source_record_sha256s": {"source_4e06d1b1cdcd0d07eff47909": "b374bac455e32c834d10ee963468201032b77876a3822be5db85779e0f1ffb22", "source_1ee2c3fae53a9d05689cd143": "86e22ce7451f1b3d7b8603286ba6cd7fb2b98ee0e6901c58e46371314ba35a65"}, "raw_state_sha256": "e433d8792fa151f754280ad4360c31cfae611650e785f77da1a140774bcbfc8d", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "9691f46da6f261ee8042b4fff17fcf81e526ce77ac3d874d0468fee74ececc15", "relation_fingerprint": {"outgoing_relations_sha256": "cefa369d8a52c5893e566ae0a87fb5ebd4a5fcd814956705643c41553ae0fdec", "incoming_relations_sha256": "c70f247eab484b32b37233617b08749d3e97ef54606ac1b0092b9f521e71aef0", "full_neighborhood_sha256": "09bccee71bde764f86524bfabd2d1ee7e29a57ac05f2f12bbc9bec46648e6139"}, "relation_neighborhood_sha256": "09bccee71bde764f86524bfabd2d1ee7e29a57ac05f2f12bbc9bec46648e6139", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "refined"
changes: [{"change_type": "refine", "previous_statement": "# 保留视觉语言先验的块内反应式力注入\n\n对预训练视觉语言动作策略，可在保留慢速视觉语言前缀的同时，以因果近期六维末端力记忆驱动并行反应动作分支，并用零初始化残差使后训练前的输出与基线一致；在线纠正数据用于覆盖当前策略遇到的接触失败状态，但效果受传感延迟、任务接触动力学和在线数据质量限制。", "new_statement": "# 保留视觉语言先验的块内反应式力注入\n\n对预训练视觉语言动作策略，可在保留慢速视觉语言前缀的同时，以因果近期六维末端力记忆驱动并行反应动作分支，并用零初始化残差使后训练前的输出与基线一致；在线纠正数据用于覆盖当前策略遇到的接触失败状态，但效果受传感延迟、任务接触动力学和在线数据质量限制。\n\n## 新增来源材料\n\n- `source_1ee2c3fae53a9d05689cd143`：预训练 VLA 的接触反馈接口应区分短时反应、事件记忆与不确定性估计。LIFT 用近期六维力在动作块内做因果反应；FM-VLA 把更长的 wrench 历史压缩为 force-memory tokens，以保留视觉难以区分的接触事件和重复进度；BayesContact 则用深度与接触似然维护物体姿态粒子后验。三者共同弥补纯视觉在接触状态中的可观测性缺口，但短时残差修正、历史压缩和概率信念不能相互替代，且都受传感延迟、模型失配和任务分布限制。", "changed_fields": [], "reason": "compile bundle from source_1ee2c3fae53a9d05689cd143", "trigger_source": "source_1ee2c3fae53a9d05689cd143", "evidence_added": []}]
change_summary: "compile bundle from source_1ee2c3fae53a9d05689cd143"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "compile bundle from source_1ee2c3fae53a9d05689cd143",
  "changes": [
    {
      "change_type": "refine",
      "changed_fields": [],
      "evidence_added": [],
      "new_statement": "# 保留视觉语言先验的块内反应式力注入\n\n对预训练视觉语言动作策略，可在保留慢速视觉语言前缀的同时，以因果近期六维末端力记忆驱动并行反应动作分支，并用零初始化残差使后训练前的输出与基线一致；在线纠正数据用于覆盖当前策略遇到的接触失败状态，但效果受传感延迟、任务接触动力学和在线数据质量限制。\n\n## 新增来源材料\n\n- `source_1ee2c3fae53a9d05689cd143`：预训练 VLA 的接触反馈接口应区分短时反应、事件记忆与不确定性估计。LIFT 用近期六维力在动作块内做因果反应；FM-VLA 把更长的 wrench 历史压缩为 force-memory tokens，以保留视觉难以区分的接触事件和重复进度；BayesContact 则用深度与接触似然维护物体姿态粒子后验。三者共同弥补纯视觉在接触状态中的可观测性缺口，但短时残差修正、历史压缩和概率信念不能相互替代，且都受传感延迟、模型失配和任务分布限制。",
      "previous_statement": "# 保留视觉语言先验的块内反应式力注入\n\n对预训练视觉语言动作策略，可在保留慢速视觉语言前缀的同时，以因果近期六维末端力记忆驱动并行反应动作分支，并用零初始化残差使后训练前的输出与基线一致；在线纠正数据用于覆盖当前策略遇到的接触失败状态，但效果受传感延迟、任务接触动力学和在线数据质量限制。",
      "reason": "compile bundle from source_1ee2c3fae53a9d05689cd143",
      "trigger_source": "source_1ee2c3fae53a9d05689cd143"
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
        "candidate:concept_2ce226e08d585158c1dfbb18"
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
        "object_updated_at:2026-07-27T19:03:59+08:00",
        "source:source_4e06d1b1cdcd0d07eff47909 work_sha256:none",
        "source:source_1ee2c3fae53a9d05689cd143 work_sha256:none"
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
        "source:source_4e06d1b1cdcd0d07eff47909 record_sha256:b374bac455e32c834d10ee963468201032b77876a3822be5db85779e0f1ffb22",
        "source:source_1ee2c3fae53a9d05689cd143 record_sha256:86e22ce7451f1b3d7b8603286ba6cd7fb2b98ee0e6901c58e46371314ba35a65"
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
        "source:source_4e06d1b1cdcd0d07eff47909 raw_sha256:ebbe3a63017280d609e1822b31af341c505ea3aee643726c542d201df6fcdf4e",
        "source:source_1ee2c3fae53a9d05689cd143 raw_sha256:705e82070aa5fe4f189d766855734afaa208a93245ab19cb1570d8b902a02691"
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
        "relation index inspected; 6 related objects found",
        "related:source_4e06d1b1cdcd0d07eff47909",
        "related:concept_637cf7264723c03955c719e2",
        "related:concept_bb69fa188e0417143c3277cf",
        "related:concept_c37ccf2640da63192432d5d5",
        "related:concept_2ce226e08d585158c1dfbb18"
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
        "validated:vault/memory/concept/concept_2ce226e08d585158c1dfbb18.md"
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
  "completed_at": "2026-07-27T19:04:24+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "332a4372384bcd4064c30a50745356e0e651baff34d9be5465edac697bfcb972",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "e433d8792fa151f754280ad4360c31cfae611650e785f77da1a140774bcbfc8d",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "09bccee71bde764f86524bfabd2d1ee7e29a57ac05f2f12bbc9bec46648e6139",
      "incoming_relations_sha256": "c70f247eab484b32b37233617b08749d3e97ef54606ac1b0092b9f521e71aef0",
      "outgoing_relations_sha256": "cefa369d8a52c5893e566ae0a87fb5ebd4a5fcd814956705643c41553ae0fdec"
    },
    "relation_neighborhood_sha256": "09bccee71bde764f86524bfabd2d1ee7e29a57ac05f2f12bbc9bec46648e6139",
    "source_record_sha256s": {
      "source_1ee2c3fae53a9d05689cd143": "86e22ce7451f1b3d7b8603286ba6cd7fb2b98ee0e6901c58e46371314ba35a65",
      "source_4e06d1b1cdcd0d07eff47909": "b374bac455e32c834d10ee963468201032b77876a3822be5db85779e0f1ffb22"
    },
    "source_state_sha256": "5506ffb1c1686f7a36164ca35c5322bc7b41f568985af3e3aa1b95b16629216a",
    "work_identity_sha256": "9691f46da6f261ee8042b4fff17fcf81e526ce77ac3d874d0468fee74ececc15"
  },
  "consolidation_id": "consolidation_1d55cc9b273ff37b0682fb37",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-27T19:04:24+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_1d55cc9b273ff37b0682fb37",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_2ce226e08d585158c1dfbb18",
  "object_sha256_after": "332a4372384bcd4064c30a50745356e0e651baff34d9be5465edac697bfcb972",
  "object_sha256_before": "46f1bf9f341f15008eb85f167d5eb4fef0f27db27fba8ccc790c57fb36ebd93b",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "refined",
  "source_ids": [
    "source_4e06d1b1cdcd0d07eff47909",
    "source_1ee2c3fae53a9d05689cd143"
  ],
  "source_records": [
    {
      "raw_content_sha256": "ebbe3a63017280d609e1822b31af341c505ea3aee643726c542d201df6fcdf4e",
      "source_id": "source_4e06d1b1cdcd0d07eff47909",
      "source_record_sha256": "b374bac455e32c834d10ee963468201032b77876a3822be5db85779e0f1ffb22",
      "work_document_sha256": null,
      "work_id": null
    },
    {
      "raw_content_sha256": "705e82070aa5fe4f189d766855734afaa208a93245ab19cb1570d8b902a02691",
      "source_id": "source_1ee2c3fae53a9d05689cd143",
      "source_record_sha256": "86e22ce7451f1b3d7b8603286ba6cd7fb2b98ee0e6901c58e46371314ba35a65",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "ebbe3a63017280d609e1822b31af341c505ea3aee643726c542d201df6fcdf4e",
    "705e82070aa5fe4f189d766855734afaa208a93245ab19cb1570d8b902a02691"
  ],
  "started_at": "2026-07-27T19:04:24+08:00",
  "status": "complete",
  "title": "Consolidation: 接触反馈应区分短时反应、事件记忆与概率后验",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-27T19:04:24+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
