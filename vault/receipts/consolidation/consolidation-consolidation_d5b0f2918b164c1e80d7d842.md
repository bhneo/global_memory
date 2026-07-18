---
id: "consolidation_d5b0f2918b164c1e80d7d842"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 具身 Agent 学习闭环（候选项目上下文）"
created_at: "2026-07-18T16:03:22+08:00"
updated_at: "2026-07-18T16:03:22+08:00"
consolidation_id: "consolidation_d5b0f2918b164c1e80d7d842"
object_id: "project_embodied_agent_learning_candidate"
object_version_before: 1
object_sha256_before: "0dc26413673b143075d93e7863af4f451c63ca1f433becfc14bf0f23a8e8ec91"
object_sha256_after: "3d0a05ddd3e6a124683ca3715ff4cf14642b22ae8727c6356e092176328bd0f4"
source_ids: ["source_0a113baae7ce4d1ab78da1a3"]
source_sha256s: ["5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c"]
source_records: [{"source_id": "source_0a113baae7ce4d1ab78da1a3", "source_record_sha256": "7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd", "raw_content_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-18T16:03:22+08:00"
completed_at: "2026-07-18T16:03:22+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/project/project_embodied_agent_learning_candidate.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_0a113baae7ce4d1ab78da1a3 raw_sha256:5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_0a113baae7ce4d1ab78da1a3 record_sha256:7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:project_embodied_agent_learning_candidate"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 4 related objects found", "related:source_0a113baae7ce4d1ab78da1a3", "related:project_embodied_agent_learning_candidate", "related:project_embodied_agent_learning_candidate", "related:project_embodied_agent_learning_candidate"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T18:36:06+08:00", "source:source_0a113baae7ce4d1ab78da1a3 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "3d0a05ddd3e6a124683ca3715ff4cf14642b22ae8727c6356e092176328bd0f4", "source_state_sha256": "9a9db415e0172b5d9e8b0e9727336410f88eb74b633ebef709efbb6f21843fb7", "source_record_sha256s": {"source_0a113baae7ce4d1ab78da1a3": "7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd"}, "raw_state_sha256": "9fc318700787b6bcd6acd0cf3beea04c899fd4beff3cc6d9a3de12d8611d8d81", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "4b82369c9494b4cb5ada2a9277370d2e49e09d0cc8b0feb617c9faed9258688a", "relation_fingerprint": {"outgoing_relations_sha256": "4cc28750c05cb58f851e5fff2319e284a49c1c88f1684d2c67b9b7d0bccc2a7c", "incoming_relations_sha256": "90a0751e0f648d90977e7b4ca86a65de09ef44e12f78538d5ede284b97cc83bd", "full_neighborhood_sha256": "2e27e0e7e8dbe3c03ab25cb4825e6a0c21aed031348542800a9f21e92784ab7d"}, "relation_neighborhood_sha256": "2e27e0e7e8dbe3c03ab25cb4825e6a0c21aed031348542800a9f21e92784ab7d", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:project_embodied_agent_learning_candidate"
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
        "object_updated_at:2026-07-17T18:36:06+08:00",
        "source:source_0a113baae7ce4d1ab78da1a3 work_sha256:none"
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
        "source:source_0a113baae7ce4d1ab78da1a3 record_sha256:7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd"
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
        "source:source_0a113baae7ce4d1ab78da1a3 raw_sha256:5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c"
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
        "relation index inspected; 4 related objects found",
        "related:source_0a113baae7ce4d1ab78da1a3",
        "related:project_embodied_agent_learning_candidate",
        "related:project_embodied_agent_learning_candidate",
        "related:project_embodied_agent_learning_candidate"
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
        "validated:vault/memory/project/project_embodied_agent_learning_candidate.md"
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
  "completed_at": "2026-07-18T16:03:22+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "3d0a05ddd3e6a124683ca3715ff4cf14642b22ae8727c6356e092176328bd0f4",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "9fc318700787b6bcd6acd0cf3beea04c899fd4beff3cc6d9a3de12d8611d8d81",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "2e27e0e7e8dbe3c03ab25cb4825e6a0c21aed031348542800a9f21e92784ab7d",
      "incoming_relations_sha256": "90a0751e0f648d90977e7b4ca86a65de09ef44e12f78538d5ede284b97cc83bd",
      "outgoing_relations_sha256": "4cc28750c05cb58f851e5fff2319e284a49c1c88f1684d2c67b9b7d0bccc2a7c"
    },
    "relation_neighborhood_sha256": "2e27e0e7e8dbe3c03ab25cb4825e6a0c21aed031348542800a9f21e92784ab7d",
    "source_record_sha256s": {
      "source_0a113baae7ce4d1ab78da1a3": "7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd"
    },
    "source_state_sha256": "9a9db415e0172b5d9e8b0e9727336410f88eb74b633ebef709efbb6f21843fb7",
    "work_identity_sha256": "4b82369c9494b4cb5ada2a9277370d2e49e09d0cc8b0feb617c9faed9258688a"
  },
  "consolidation_id": "consolidation_d5b0f2918b164c1e80d7d842",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-18T16:03:22+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_d5b0f2918b164c1e80d7d842",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "project_embodied_agent_learning_candidate",
  "object_sha256_after": "3d0a05ddd3e6a124683ca3715ff4cf14642b22ae8727c6356e092176328bd0f4",
  "object_sha256_before": "0dc26413673b143075d93e7863af4f451c63ca1f433becfc14bf0f23a8e8ec91",
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
  "started_at": "2026-07-18T16:03:22+08:00",
  "status": "complete",
  "title": "Consolidation: 具身 Agent 学习闭环（候选项目上下文）",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-18T16:03:22+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
