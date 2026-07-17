---
id: "consolidation_74c4db8e9360bd99f00e4abd"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 具身 Agent 学习闭环（候选项目上下文）"
created_at: "2026-07-17T18:36:06+08:00"
updated_at: "2026-07-17T18:36:06+08:00"
consolidation_id: "consolidation_74c4db8e9360bd99f00e4abd"
object_id: "project_embodied_agent_learning_candidate"
object_version_before: 1
object_sha256_before: "d5c778e0959a906f109ff3a89c0de4c03c97d5ce568c5220ef0aa4ac4fc28987"
object_sha256_after: "0dc26413673b143075d93e7863af4f451c63ca1f433becfc14bf0f23a8e8ec91"
source_ids: ["source_0a113baae7ce4d1ab78da1a3"]
source_sha256s: ["5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c"]
source_records: [{"source_id": "source_0a113baae7ce4d1ab78da1a3", "source_record_sha256": "7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd", "raw_content_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-17T18:36:06+08:00"
completed_at: "2026-07-17T18:36:06+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/project/project_embodied_agent_learning_candidate.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_0a113baae7ce4d1ab78da1a3 raw_sha256:5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_0a113baae7ce4d1ab78da1a3 record_sha256:7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:project_embodied_agent_learning_candidate"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 4 related objects found", "related:project_embodied_agent_learning_candidate", "related:project_embodied_agent_learning_candidate", "related:project_embodied_agent_learning_candidate", "related:source_0a113baae7ce4d1ab78da1a3"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:24:09+08:00", "source:source_0a113baae7ce4d1ab78da1a3 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "0dc26413673b143075d93e7863af4f451c63ca1f433becfc14bf0f23a8e8ec91", "source_state_sha256": "9a9db415e0172b5d9e8b0e9727336410f88eb74b633ebef709efbb6f21843fb7", "source_record_sha256s": {"source_0a113baae7ce4d1ab78da1a3": "7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd"}, "raw_state_sha256": "9fc318700787b6bcd6acd0cf3beea04c899fd4beff3cc6d9a3de12d8611d8d81", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "4b82369c9494b4cb5ada2a9277370d2e49e09d0cc8b0feb617c9faed9258688a", "relation_neighborhood_sha256": "1b3ae87303bfe662b4c0953eba08f4f0c819f59e80523040634165c4c1e925d2", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
      "findings": [
        "contradiction relations inspected; 0 found"
      ],
      "status": "passed",
      "warnings": []
    },
    "drift_checked": {
      "findings": [
        "drift_reports:0"
      ],
      "status": "passed",
      "warnings": []
    },
    "duplicate_search_completed": {
      "findings": [
        "searched title; 1 candidates inspected",
        "candidate:project_embodied_agent_learning_candidate"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "findings": [
        "not applicable for non-claim object"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_revalidated": {
      "findings": [
        "not applicable for non-claim object"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:24:09+08:00",
        "source:source_0a113baae7ce4d1ab78da1a3 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_0a113baae7ce4d1ab78da1a3 record_sha256:7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_0a113baae7ce4d1ab78da1a3 raw_sha256:5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 4 related objects found",
        "related:project_embodied_agent_learning_candidate",
        "related:project_embodied_agent_learning_candidate",
        "related:project_embodied_agent_learning_candidate",
        "related:source_0a113baae7ce4d1ab78da1a3"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/project/project_embodied_agent_learning_candidate.md"
      ],
      "status": "passed",
      "warnings": []
    },
    "source_independence_checked": {
      "findings": [
        "distinct_source_ids:1",
        "distinct_work_ids:0"
      ],
      "status": "passed",
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
  "completed_at": "2026-07-17T18:36:06+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "0dc26413673b143075d93e7863af4f451c63ca1f433becfc14bf0f23a8e8ec91",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "9fc318700787b6bcd6acd0cf3beea04c899fd4beff3cc6d9a3de12d8611d8d81",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "1b3ae87303bfe662b4c0953eba08f4f0c819f59e80523040634165c4c1e925d2",
    "source_record_sha256s": {
      "source_0a113baae7ce4d1ab78da1a3": "7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd"
    },
    "source_state_sha256": "9a9db415e0172b5d9e8b0e9727336410f88eb74b633ebef709efbb6f21843fb7",
    "work_identity_sha256": "4b82369c9494b4cb5ada2a9277370d2e49e09d0cc8b0feb617c9faed9258688a"
  },
  "consolidation_id": "consolidation_74c4db8e9360bd99f00e4abd",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:36:06+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_74c4db8e9360bd99f00e4abd",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "project_embodied_agent_learning_candidate",
  "object_sha256_after": "0dc26413673b143075d93e7863af4f451c63ca1f433becfc14bf0f23a8e8ec91",
  "object_sha256_before": "d5c778e0959a906f109ff3a89c0de4c03c97d5ce568c5220ef0aa4ac4fc28987",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_0a113baae7ce4d1ab78da1a3"
  ],
  "source_records": [
    {
      "raw_content_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c",
      "source_id": "source_0a113baae7ce4d1ab78da1a3",
      "source_record_sha256": "7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c"
  ],
  "started_at": "2026-07-17T18:36:06+08:00",
  "status": "complete",
  "title": "Consolidation: 具身 Agent 学习闭环（候选项目上下文）",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:36:06+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
