---
id: "consolidation_ebc28aee1676e85b8aab4eae"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: VLA 动作缓存与上下文复用"
created_at: "2026-07-19T03:28:18+08:00"
updated_at: "2026-07-19T03:28:18+08:00"
consolidation_id: "consolidation_ebc28aee1676e85b8aab4eae"
object_id: "concept_vla_action_cache_refinement"
object_version_before: 1
object_sha256_before: "232b0499f1a617eabe49ecf496781014835bf2b33acc75603b7635637e5988d7"
object_sha256_after: "c14fe37a90fb03ba86f7b64baa9f46eb4e2de5d5897e628b3e6441e62bdac8c6"
source_ids: ["source_291d6174cf92660287138f47"]
source_sha256s: ["c3b99399eef2fc7b323dcb9e453ef2996d2fe76b48e18627b45b7cb301b515b7"]
source_records: [{"source_id": "source_291d6174cf92660287138f47", "source_record_sha256": "6bdc3cb2e29e35d86c9ca47c8c2ec19dfa104b47ea82dbd1ee99e4c6685b2df1", "raw_content_sha256": "c3b99399eef2fc7b323dcb9e453ef2996d2fe76b48e18627b45b7cb301b515b7", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-19T03:28:18+08:00"
completed_at: "2026-07-19T03:28:18+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_vla_action_cache_refinement.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_291d6174cf92660287138f47 raw_sha256:c3b99399eef2fc7b323dcb9e453ef2996d2fe76b48e18627b45b7cb301b515b7"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_291d6174cf92660287138f47 record_sha256:6bdc3cb2e29e35d86c9ca47c8c2ec19dfa104b47ea82dbd1ee99e4c6685b2df1"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_vla_action_cache_refinement"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 7 related objects found", "related:source_291d6174cf92660287138f47", "related:concept_generalist_cross_embodiment_vla", "related:concept_predictive_vla_deployment", "related:concept_vla_action_cache_refinement", "related:concept_vla_action_cache_refinement"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T03:28:10+08:00", "source:source_291d6174cf92660287138f47 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "c14fe37a90fb03ba86f7b64baa9f46eb4e2de5d5897e628b3e6441e62bdac8c6", "source_state_sha256": "537df76e2f43971316645bfbd61da00ae3bda41a7c198fe00d7ee58e882772e2", "source_record_sha256s": {"source_291d6174cf92660287138f47": "6bdc3cb2e29e35d86c9ca47c8c2ec19dfa104b47ea82dbd1ee99e4c6685b2df1"}, "raw_state_sha256": "3e468de79984505b87d3029df705d9eb362ae560939a7c7edb1f931955cbd6bd", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "bdeef10e8c35ded8f94f2652e95152bc2dbad40ef0feed8fb260d69886db6c8d", "relation_fingerprint": {"outgoing_relations_sha256": "08b86bb5d650c57a7a36fa1a9e57e6ef23b40e3b3950c93915bd3aec68def376", "incoming_relations_sha256": "80bfcb1761cf5d2c36f60ad78ac25682fe29d5b74491063d0e26e910b72d4d73", "full_neighborhood_sha256": "57495f270e1ff375b78df1e0a93a86522930d0d64e721d87c11ad2b77d93d684"}, "relation_neighborhood_sha256": "57495f270e1ff375b78df1e0a93a86522930d0d64e721d87c11ad2b77d93d684", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "unchanged"
changes: [{"change_type": "metadata_only", "previous_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。", "new_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_291d6174cf92660287138f47", "trigger_source": "source_291d6174cf92660287138f47", "evidence_added": []}]
change_summary: "compile bundle from source_291d6174cf92660287138f47"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "compile bundle from source_291d6174cf92660287138f47",
  "changes": [
    {
      "change_type": "metadata_only",
      "changed_fields": [
        "source_ids",
        "evidence",
        "last_verified_at"
      ],
      "evidence_added": [],
      "new_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。",
      "previous_statement": "# VLA 动作缓存与上下文复用\n\n为扩散或流匹配 VLA 保存带多模态上下文键的中间动作，在相似状态下检索并作为新一轮动作生成的暖启动，再通过后续生成步骤修正。",
      "reason": "compile bundle from source_291d6174cf92660287138f47",
      "trigger_source": "source_291d6174cf92660287138f47"
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
        "candidate:concept_vla_action_cache_refinement"
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
        "object_updated_at:2026-07-19T03:28:10+08:00",
        "source:source_291d6174cf92660287138f47 work_sha256:none"
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
        "source:source_291d6174cf92660287138f47 record_sha256:6bdc3cb2e29e35d86c9ca47c8c2ec19dfa104b47ea82dbd1ee99e4c6685b2df1"
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
        "source:source_291d6174cf92660287138f47 raw_sha256:c3b99399eef2fc7b323dcb9e453ef2996d2fe76b48e18627b45b7cb301b515b7"
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
        "relation index inspected; 7 related objects found",
        "related:source_291d6174cf92660287138f47",
        "related:concept_generalist_cross_embodiment_vla",
        "related:concept_predictive_vla_deployment",
        "related:concept_vla_action_cache_refinement",
        "related:concept_vla_action_cache_refinement"
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
        "validated:vault/memory/concept/concept_vla_action_cache_refinement.md"
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
  "completed_at": "2026-07-19T03:28:18+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "c14fe37a90fb03ba86f7b64baa9f46eb4e2de5d5897e628b3e6441e62bdac8c6",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "3e468de79984505b87d3029df705d9eb362ae560939a7c7edb1f931955cbd6bd",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "57495f270e1ff375b78df1e0a93a86522930d0d64e721d87c11ad2b77d93d684",
      "incoming_relations_sha256": "80bfcb1761cf5d2c36f60ad78ac25682fe29d5b74491063d0e26e910b72d4d73",
      "outgoing_relations_sha256": "08b86bb5d650c57a7a36fa1a9e57e6ef23b40e3b3950c93915bd3aec68def376"
    },
    "relation_neighborhood_sha256": "57495f270e1ff375b78df1e0a93a86522930d0d64e721d87c11ad2b77d93d684",
    "source_record_sha256s": {
      "source_291d6174cf92660287138f47": "6bdc3cb2e29e35d86c9ca47c8c2ec19dfa104b47ea82dbd1ee99e4c6685b2df1"
    },
    "source_state_sha256": "537df76e2f43971316645bfbd61da00ae3bda41a7c198fe00d7ee58e882772e2",
    "work_identity_sha256": "bdeef10e8c35ded8f94f2652e95152bc2dbad40ef0feed8fb260d69886db6c8d"
  },
  "consolidation_id": "consolidation_ebc28aee1676e85b8aab4eae",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T03:28:18+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_ebc28aee1676e85b8aab4eae",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_vla_action_cache_refinement",
  "object_sha256_after": "c14fe37a90fb03ba86f7b64baa9f46eb4e2de5d5897e628b3e6441e62bdac8c6",
  "object_sha256_before": "232b0499f1a617eabe49ecf496781014835bf2b33acc75603b7635637e5988d7",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_291d6174cf92660287138f47"
  ],
  "source_records": [
    {
      "raw_content_sha256": "c3b99399eef2fc7b323dcb9e453ef2996d2fe76b48e18627b45b7cb301b515b7",
      "source_id": "source_291d6174cf92660287138f47",
      "source_record_sha256": "6bdc3cb2e29e35d86c9ca47c8c2ec19dfa104b47ea82dbd1ee99e4c6685b2df1",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "c3b99399eef2fc7b323dcb9e453ef2996d2fe76b48e18627b45b7cb301b515b7"
  ],
  "started_at": "2026-07-19T03:28:18+08:00",
  "status": "complete",
  "title": "Consolidation: VLA 动作缓存与上下文复用",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T03:28:18+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
