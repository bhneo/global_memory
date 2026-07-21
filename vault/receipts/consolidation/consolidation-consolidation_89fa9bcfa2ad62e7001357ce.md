---
id: "consolidation_89fa9bcfa2ad62e7001357ce"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 多坐标系同步动作去噪"
created_at: "2026-07-20T13:35:13+08:00"
updated_at: "2026-07-20T13:35:13+08:00"
consolidation_id: "consolidation_89fa9bcfa2ad62e7001357ce"
object_id: "concept_3d739e54fe54c8a5205d2301"
object_version_before: 1
object_sha256_before: "6e24229241b1b19ee8405cadd642f5a0c04c056b7ed1a2069ddf8b6ed960b86e"
object_sha256_after: "bde79b863504f1949e55a8c00b921e8385b36ebbd5ec3ebc64ead62a6e39dd98"
source_ids: ["source_4df1017326dd7cc4786f4218"]
source_sha256s: ["34cb5cd186fc09ae78cf74eb89501f1e26c0b2e4508d8e6e2f3e95e1ba8719cc"]
source_records: [{"source_id": "source_4df1017326dd7cc4786f4218", "source_record_sha256": "87a6662e7454f67a4221b230f903d1a96897ea4a52aecd35b24d4e769fb11bce", "raw_content_sha256": "34cb5cd186fc09ae78cf74eb89501f1e26c0b2e4508d8e6e2f3e95e1ba8719cc", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-20T13:35:13+08:00"
completed_at: "2026-07-20T13:35:13+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_3d739e54fe54c8a5205d2301.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_4df1017326dd7cc4786f4218 raw_sha256:34cb5cd186fc09ae78cf74eb89501f1e26c0b2e4508d8e6e2f3e95e1ba8719cc"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_4df1017326dd7cc4786f4218 record_sha256:87a6662e7454f67a4221b230f903d1a96897ea4a52aecd35b24d4e769fb11bce"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_3d739e54fe54c8a5205d2301"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 3 related objects found", "related:source_4df1017326dd7cc4786f4218", "related:concept_21a37fbe65868f6e97a68a20", "related:concept_generalist_cross_embodiment_vla"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-20T13:35:04+08:00", "source:source_4df1017326dd7cc4786f4218 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "bde79b863504f1949e55a8c00b921e8385b36ebbd5ec3ebc64ead62a6e39dd98", "source_state_sha256": "f9201ece2be7cb021347909004272c0760ba7416c945719aafcc216caf501bad", "source_record_sha256s": {"source_4df1017326dd7cc4786f4218": "87a6662e7454f67a4221b230f903d1a96897ea4a52aecd35b24d4e769fb11bce"}, "raw_state_sha256": "a877cd9606d8075e57c0a31b933bfc8729a3f277e29f7c5cf529d63e1e709aa0", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "673425812d446e08214349b51c931d807c96af22a6151b8eb881f1670c8e9a8e", "relation_fingerprint": {"outgoing_relations_sha256": "43deef313b36f79c8d9cbc6b2642b0851e8e1346682f33a12eac0f27ccd5f68c", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "43deef313b36f79c8d9cbc6b2642b0851e8e1346682f33a12eac0f27ccd5f68c"}, "relation_neighborhood_sha256": "43deef313b36f79c8d9cbc6b2642b0851e8e1346682f33a12eac0f27ccd5f68c", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "refined"
changes: [{"change_type": "refine", "previous_statement": "# 多坐标系同步动作去噪\n\n在一个 canonical diffusion state 上，把同一噪声动作转换到多个任务相关坐标系，由 frame-specialized denoisers 分别预测，再变换回统一坐标系融合。它利用不同任务阶段在夹爪、基座或相对轨迹 frame 中更紧凑的动作分布，但依赖候选 frame 与可靠变换。", "new_statement": "# 多坐标系同步动作去噪\n\n在一个 canonical diffusion state 上，把同一噪声动作转换到多个任务相关坐标系，由 frame-specialized denoisers 分别预测，再变换回统一坐标系融合。它利用不同任务阶段在夹爪、基座或相对轨迹 frame 中更紧凑的动作分布，但依赖候选 frame 与可靠变换。", "changed_fields": [], "reason": "compile bundle from source_4df1017326dd7cc4786f4218", "trigger_source": "source_4df1017326dd7cc4786f4218", "evidence_added": []}]
change_summary: "compile bundle from source_4df1017326dd7cc4786f4218"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "compile bundle from source_4df1017326dd7cc4786f4218",
  "changes": [
    {
      "change_type": "refine",
      "changed_fields": [],
      "evidence_added": [],
      "new_statement": "# 多坐标系同步动作去噪\n\n在一个 canonical diffusion state 上，把同一噪声动作转换到多个任务相关坐标系，由 frame-specialized denoisers 分别预测，再变换回统一坐标系融合。它利用不同任务阶段在夹爪、基座或相对轨迹 frame 中更紧凑的动作分布，但依赖候选 frame 与可靠变换。",
      "previous_statement": "# 多坐标系同步动作去噪\n\n在一个 canonical diffusion state 上，把同一噪声动作转换到多个任务相关坐标系，由 frame-specialized denoisers 分别预测，再变换回统一坐标系融合。它利用不同任务阶段在夹爪、基座或相对轨迹 frame 中更紧凑的动作分布，但依赖候选 frame 与可靠变换。",
      "reason": "compile bundle from source_4df1017326dd7cc4786f4218",
      "trigger_source": "source_4df1017326dd7cc4786f4218"
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
        "candidate:concept_3d739e54fe54c8a5205d2301"
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
        "object_updated_at:2026-07-20T13:35:04+08:00",
        "source:source_4df1017326dd7cc4786f4218 work_sha256:none"
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
        "source:source_4df1017326dd7cc4786f4218 record_sha256:87a6662e7454f67a4221b230f903d1a96897ea4a52aecd35b24d4e769fb11bce"
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
        "source:source_4df1017326dd7cc4786f4218 raw_sha256:34cb5cd186fc09ae78cf74eb89501f1e26c0b2e4508d8e6e2f3e95e1ba8719cc"
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
        "related:source_4df1017326dd7cc4786f4218",
        "related:concept_21a37fbe65868f6e97a68a20",
        "related:concept_generalist_cross_embodiment_vla"
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
        "validated:vault/memory/concept/concept_3d739e54fe54c8a5205d2301.md"
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
  "completed_at": "2026-07-20T13:35:13+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "bde79b863504f1949e55a8c00b921e8385b36ebbd5ec3ebc64ead62a6e39dd98",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "a877cd9606d8075e57c0a31b933bfc8729a3f277e29f7c5cf529d63e1e709aa0",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "43deef313b36f79c8d9cbc6b2642b0851e8e1346682f33a12eac0f27ccd5f68c",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "43deef313b36f79c8d9cbc6b2642b0851e8e1346682f33a12eac0f27ccd5f68c"
    },
    "relation_neighborhood_sha256": "43deef313b36f79c8d9cbc6b2642b0851e8e1346682f33a12eac0f27ccd5f68c",
    "source_record_sha256s": {
      "source_4df1017326dd7cc4786f4218": "87a6662e7454f67a4221b230f903d1a96897ea4a52aecd35b24d4e769fb11bce"
    },
    "source_state_sha256": "f9201ece2be7cb021347909004272c0760ba7416c945719aafcc216caf501bad",
    "work_identity_sha256": "673425812d446e08214349b51c931d807c96af22a6151b8eb881f1670c8e9a8e"
  },
  "consolidation_id": "consolidation_89fa9bcfa2ad62e7001357ce",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-20T13:35:13+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_89fa9bcfa2ad62e7001357ce",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_3d739e54fe54c8a5205d2301",
  "object_sha256_after": "bde79b863504f1949e55a8c00b921e8385b36ebbd5ec3ebc64ead62a6e39dd98",
  "object_sha256_before": "6e24229241b1b19ee8405cadd642f5a0c04c056b7ed1a2069ddf8b6ed960b86e",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "refined",
  "source_ids": [
    "source_4df1017326dd7cc4786f4218"
  ],
  "source_records": [
    {
      "raw_content_sha256": "34cb5cd186fc09ae78cf74eb89501f1e26c0b2e4508d8e6e2f3e95e1ba8719cc",
      "source_id": "source_4df1017326dd7cc4786f4218",
      "source_record_sha256": "87a6662e7454f67a4221b230f903d1a96897ea4a52aecd35b24d4e769fb11bce",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "34cb5cd186fc09ae78cf74eb89501f1e26c0b2e4508d8e6e2f3e95e1ba8719cc"
  ],
  "started_at": "2026-07-20T13:35:13+08:00",
  "status": "complete",
  "title": "Consolidation: 多坐标系同步动作去噪",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-20T13:35:13+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
