---
id: "consolidation_53fc27b7fc1b679960a2f34d"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 示范先验条件化的 VLA 结构化探索"
created_at: "2026-07-20T13:34:14+08:00"
updated_at: "2026-07-20T13:34:14+08:00"
consolidation_id: "consolidation_53fc27b7fc1b679960a2f34d"
object_id: "concept_9443d1789c9a179bd1611be3"
object_version_before: 1
object_sha256_before: "1d1c4af0c104ac6a1d1c2fb7d37f41e7bf24126adfbfb63dcbc4d660f0eb9cc2"
object_sha256_after: "ce78d94897279bae602fb320a65fef8f6bcf49f2b6a3d775949129c74bf97d58"
source_ids: ["source_5b8c57a9bef3348109f3b7bb"]
source_sha256s: ["76b101eb5c360c5dc9778e69b3a9a847c1be59566365ba1a143ff0685ac1faef"]
source_records: [{"source_id": "source_5b8c57a9bef3348109f3b7bb", "source_record_sha256": "b2f29eb1d616b99217418b8226152cc13a5f839aca89a829f989f3fde1a33e1e", "raw_content_sha256": "76b101eb5c360c5dc9778e69b3a9a847c1be59566365ba1a143ff0685ac1faef", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-20T13:34:13+08:00"
completed_at: "2026-07-20T13:34:14+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_9443d1789c9a179bd1611be3.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_5b8c57a9bef3348109f3b7bb raw_sha256:76b101eb5c360c5dc9778e69b3a9a847c1be59566365ba1a143ff0685ac1faef"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_5b8c57a9bef3348109f3b7bb record_sha256:b2f29eb1d616b99217418b8226152cc13a5f839aca89a829f989f3fde1a33e1e"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_9443d1789c9a179bd1611be3"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 3 related objects found", "related:source_5b8c57a9bef3348109f3b7bb", "related:concept_f67f822ee20789d74d7b75e3", "related:concept_f9a9f1d1818632c0380b7942"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-20T13:34:04+08:00", "source:source_5b8c57a9bef3348109f3b7bb work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "ce78d94897279bae602fb320a65fef8f6bcf49f2b6a3d775949129c74bf97d58", "source_state_sha256": "bba83606ee4c9717d72e3f300fd97154476741665e2151996836f56e673e461a", "source_record_sha256s": {"source_5b8c57a9bef3348109f3b7bb": "b2f29eb1d616b99217418b8226152cc13a5f839aca89a829f989f3fde1a33e1e"}, "raw_state_sha256": "230c1626ab47b1dddfa7a415e034f402490540b4dcc6ec947ed40a90fbd5e0c0", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "7c06531733170b08bbbd35587eb1a35d918ec69a38721e7fc9bebd5af953683d", "relation_fingerprint": {"outgoing_relations_sha256": "641e96238b13d846e2544949ff2850c610b80fccdcc749da8f1ac8ace1955e08", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "641e96238b13d846e2544949ff2850c610b80fccdcc749da8f1ac8ace1955e08"}, "relation_neighborhood_sha256": "641e96238b13d846e2544949ff2850c610b80fccdcc749da8f1ac8ace1955e08", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "refined"
changes: [{"change_type": "refine", "previous_statement": "# 示范先验条件化的 VLA 结构化探索\n\n从离线示范中提取离散行为模式，并以模式 token 条件化 VLA 的在线 rollout，使有限交互预算覆盖不同可行行为；部署时再用状态条件选择器收束为确定性模式选择。该接口提升的是探索分布结构，不等同于价值表示或全模型强化学习。", "new_statement": "# 示范先验条件化的 VLA 结构化探索\n\n从离线示范中提取离散行为模式，并以模式 token 条件化 VLA 的在线 rollout，使有限交互预算覆盖不同可行行为；部署时再用状态条件选择器收束为确定性模式选择。该接口提升的是探索分布结构，不等同于价值表示或全模型强化学习。", "changed_fields": [], "reason": "compile bundle from source_5b8c57a9bef3348109f3b7bb", "trigger_source": "source_5b8c57a9bef3348109f3b7bb", "evidence_added": []}]
change_summary: "compile bundle from source_5b8c57a9bef3348109f3b7bb"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "compile bundle from source_5b8c57a9bef3348109f3b7bb",
  "changes": [
    {
      "change_type": "refine",
      "changed_fields": [],
      "evidence_added": [],
      "new_statement": "# 示范先验条件化的 VLA 结构化探索\n\n从离线示范中提取离散行为模式，并以模式 token 条件化 VLA 的在线 rollout，使有限交互预算覆盖不同可行行为；部署时再用状态条件选择器收束为确定性模式选择。该接口提升的是探索分布结构，不等同于价值表示或全模型强化学习。",
      "previous_statement": "# 示范先验条件化的 VLA 结构化探索\n\n从离线示范中提取离散行为模式，并以模式 token 条件化 VLA 的在线 rollout，使有限交互预算覆盖不同可行行为；部署时再用状态条件选择器收束为确定性模式选择。该接口提升的是探索分布结构，不等同于价值表示或全模型强化学习。",
      "reason": "compile bundle from source_5b8c57a9bef3348109f3b7bb",
      "trigger_source": "source_5b8c57a9bef3348109f3b7bb"
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
        "candidate:concept_9443d1789c9a179bd1611be3"
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
        "object_updated_at:2026-07-20T13:34:04+08:00",
        "source:source_5b8c57a9bef3348109f3b7bb work_sha256:none"
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
        "source:source_5b8c57a9bef3348109f3b7bb record_sha256:b2f29eb1d616b99217418b8226152cc13a5f839aca89a829f989f3fde1a33e1e"
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
        "source:source_5b8c57a9bef3348109f3b7bb raw_sha256:76b101eb5c360c5dc9778e69b3a9a847c1be59566365ba1a143ff0685ac1faef"
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
        "related:source_5b8c57a9bef3348109f3b7bb",
        "related:concept_f67f822ee20789d74d7b75e3",
        "related:concept_f9a9f1d1818632c0380b7942"
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
        "validated:vault/memory/concept/concept_9443d1789c9a179bd1611be3.md"
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
  "completed_at": "2026-07-20T13:34:14+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "ce78d94897279bae602fb320a65fef8f6bcf49f2b6a3d775949129c74bf97d58",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "230c1626ab47b1dddfa7a415e034f402490540b4dcc6ec947ed40a90fbd5e0c0",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "641e96238b13d846e2544949ff2850c610b80fccdcc749da8f1ac8ace1955e08",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "641e96238b13d846e2544949ff2850c610b80fccdcc749da8f1ac8ace1955e08"
    },
    "relation_neighborhood_sha256": "641e96238b13d846e2544949ff2850c610b80fccdcc749da8f1ac8ace1955e08",
    "source_record_sha256s": {
      "source_5b8c57a9bef3348109f3b7bb": "b2f29eb1d616b99217418b8226152cc13a5f839aca89a829f989f3fde1a33e1e"
    },
    "source_state_sha256": "bba83606ee4c9717d72e3f300fd97154476741665e2151996836f56e673e461a",
    "work_identity_sha256": "7c06531733170b08bbbd35587eb1a35d918ec69a38721e7fc9bebd5af953683d"
  },
  "consolidation_id": "consolidation_53fc27b7fc1b679960a2f34d",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-20T13:34:14+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_53fc27b7fc1b679960a2f34d",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_9443d1789c9a179bd1611be3",
  "object_sha256_after": "ce78d94897279bae602fb320a65fef8f6bcf49f2b6a3d775949129c74bf97d58",
  "object_sha256_before": "1d1c4af0c104ac6a1d1c2fb7d37f41e7bf24126adfbfb63dcbc4d660f0eb9cc2",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "refined",
  "source_ids": [
    "source_5b8c57a9bef3348109f3b7bb"
  ],
  "source_records": [
    {
      "raw_content_sha256": "76b101eb5c360c5dc9778e69b3a9a847c1be59566365ba1a143ff0685ac1faef",
      "source_id": "source_5b8c57a9bef3348109f3b7bb",
      "source_record_sha256": "b2f29eb1d616b99217418b8226152cc13a5f839aca89a829f989f3fde1a33e1e",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "76b101eb5c360c5dc9778e69b3a9a847c1be59566365ba1a143ff0685ac1faef"
  ],
  "started_at": "2026-07-20T13:34:13+08:00",
  "status": "complete",
  "title": "Consolidation: 示范先验条件化的 VLA 结构化探索",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-20T13:34:14+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
