---
id: "consolidation_647df8b5ad7de40dd4412179"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 几何落地的本体感觉视觉融合"
created_at: "2026-07-19T12:20:13+08:00"
updated_at: "2026-07-19T12:20:13+08:00"
consolidation_id: "consolidation_647df8b5ad7de40dd4412179"
object_id: "concept_geometry_grounded_proprioception"
object_version_before: 1
object_sha256_before: "45731a6cb9936d775c4f80ffd1f1e41f70612f97bfd4a9349b4e0e9fa5719509"
object_sha256_after: "3b010cbc99511ab53499c015c4eb521e9c06fad367f6d4a56aa89247674b5686"
source_ids: ["source_b1f4ea371eb10f3bc7a0f532"]
source_sha256s: ["69528ff2f3536ebfba6c82e2aa8063f26dc9eb79a5d47a72bd5084a2a6582731"]
source_records: [{"source_id": "source_b1f4ea371eb10f3bc7a0f532", "source_record_sha256": "07d6ca20e2145d10bcf4748f06daede9434eb9617a9d1242f10d5c26b0b9cd7e", "raw_content_sha256": "69528ff2f3536ebfba6c82e2aa8063f26dc9eb79a5d47a72bd5084a2a6582731", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-19T12:20:13+08:00"
completed_at: "2026-07-19T12:20:13+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_geometry_grounded_proprioception.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_b1f4ea371eb10f3bc7a0f532 raw_sha256:69528ff2f3536ebfba6c82e2aa8063f26dc9eb79a5d47a72bd5084a2a6582731"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_b1f4ea371eb10f3bc7a0f532 record_sha256:07d6ca20e2145d10bcf4748f06daede9434eb9617a9d1242f10d5c26b0b9cd7e"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_geometry_grounded_proprioception"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 4 related objects found", "related:source_b1f4ea371eb10f3bc7a0f532", "related:concept_generalist_cross_embodiment_vla", "related:concept_generalist_cross_embodiment_vla", "related:concept_predictive_vla_deployment"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T12:19:15+08:00", "source:source_b1f4ea371eb10f3bc7a0f532 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "3b010cbc99511ab53499c015c4eb521e9c06fad367f6d4a56aa89247674b5686", "source_state_sha256": "9aa84d628df61363fbff215a72a4e7d902f2fcfb18b30649edd8297e20325c3e", "source_record_sha256s": {"source_b1f4ea371eb10f3bc7a0f532": "07d6ca20e2145d10bcf4748f06daede9434eb9617a9d1242f10d5c26b0b9cd7e"}, "raw_state_sha256": "eb43cbd6de4dcae6a8092d5e6af1451e189aac2da369c78c83ec6df6e3f7abde", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "c1ab84726b08fb5f71c98f597cfb15aad3f93b850197d78c91caa3dcfc0ff27b", "relation_fingerprint": {"outgoing_relations_sha256": "79ecb2419df2fde2006b285672379ca515461e8494d6a640f41872e0af141153", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "79ecb2419df2fde2006b285672379ca515461e8494d6a640f41872e0af141153"}, "relation_neighborhood_sha256": "79ecb2419df2fde2006b285672379ca515461e8494d6a640f41872e0af141153", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_geometry_grounded_proprioception"
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
        "object_updated_at:2026-07-19T12:19:15+08:00",
        "source:source_b1f4ea371eb10f3bc7a0f532 work_sha256:none"
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
        "source:source_b1f4ea371eb10f3bc7a0f532 record_sha256:07d6ca20e2145d10bcf4748f06daede9434eb9617a9d1242f10d5c26b0b9cd7e"
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
        "source:source_b1f4ea371eb10f3bc7a0f532 raw_sha256:69528ff2f3536ebfba6c82e2aa8063f26dc9eb79a5d47a72bd5084a2a6582731"
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
        "related:source_b1f4ea371eb10f3bc7a0f532",
        "related:concept_generalist_cross_embodiment_vla",
        "related:concept_generalist_cross_embodiment_vla",
        "related:concept_predictive_vla_deployment"
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
        "validated:vault/memory/concept/concept_geometry_grounded_proprioception.md"
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
  "completed_at": "2026-07-19T12:20:13+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "3b010cbc99511ab53499c015c4eb521e9c06fad367f6d4a56aa89247674b5686",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "eb43cbd6de4dcae6a8092d5e6af1451e189aac2da369c78c83ec6df6e3f7abde",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "79ecb2419df2fde2006b285672379ca515461e8494d6a640f41872e0af141153",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "79ecb2419df2fde2006b285672379ca515461e8494d6a640f41872e0af141153"
    },
    "relation_neighborhood_sha256": "79ecb2419df2fde2006b285672379ca515461e8494d6a640f41872e0af141153",
    "source_record_sha256s": {
      "source_b1f4ea371eb10f3bc7a0f532": "07d6ca20e2145d10bcf4748f06daede9434eb9617a9d1242f10d5c26b0b9cd7e"
    },
    "source_state_sha256": "9aa84d628df61363fbff215a72a4e7d902f2fcfb18b30649edd8297e20325c3e",
    "work_identity_sha256": "c1ab84726b08fb5f71c98f597cfb15aad3f93b850197d78c91caa3dcfc0ff27b"
  },
  "consolidation_id": "consolidation_647df8b5ad7de40dd4412179",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T12:20:13+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_647df8b5ad7de40dd4412179",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_geometry_grounded_proprioception",
  "object_sha256_after": "3b010cbc99511ab53499c015c4eb521e9c06fad367f6d4a56aa89247674b5686",
  "object_sha256_before": "45731a6cb9936d775c4f80ffd1f1e41f70612f97bfd4a9349b4e0e9fa5719509",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_b1f4ea371eb10f3bc7a0f532"
  ],
  "source_records": [
    {
      "raw_content_sha256": "69528ff2f3536ebfba6c82e2aa8063f26dc9eb79a5d47a72bd5084a2a6582731",
      "source_id": "source_b1f4ea371eb10f3bc7a0f532",
      "source_record_sha256": "07d6ca20e2145d10bcf4748f06daede9434eb9617a9d1242f10d5c26b0b9cd7e",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "69528ff2f3536ebfba6c82e2aa8063f26dc9eb79a5d47a72bd5084a2a6582731"
  ],
  "started_at": "2026-07-19T12:20:13+08:00",
  "status": "complete",
  "title": "Consolidation: 几何落地的本体感觉视觉融合",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T12:20:13+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
