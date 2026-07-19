---
id: "consolidation_48dc5fcbe817827856b09cd1"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 可移植具身推理运行时"
created_at: "2026-07-19T12:20:19+08:00"
updated_at: "2026-07-19T12:20:19+08:00"
consolidation_id: "consolidation_48dc5fcbe817827856b09cd1"
object_id: "concept_portable_embodied_inference_runtime"
object_version_before: 1
object_sha256_before: "54fa90e03ba4fae54e15db712dd4e3c09eaf45da8d40cb76670d23f9d2c50c4b"
object_sha256_after: "3aeb9280869b7f1c8decb74ba3d02933dd8039a212974edc97d4be4a978e7def"
source_ids: ["source_c46b1e0305ec5c9adba634f1"]
source_sha256s: ["9c26795d85fc431283566eb343ffbd8c34d29c8df03e81c5419f17a7510a439c"]
source_records: [{"source_id": "source_c46b1e0305ec5c9adba634f1", "source_record_sha256": "59833a7ef056087a253b75f59f817a8d22452ff790e386e2c1ddfc3972c3d1af", "raw_content_sha256": "9c26795d85fc431283566eb343ffbd8c34d29c8df03e81c5419f17a7510a439c", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-19T12:20:19+08:00"
completed_at: "2026-07-19T12:20:19+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_portable_embodied_inference_runtime.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_c46b1e0305ec5c9adba634f1 raw_sha256:9c26795d85fc431283566eb343ffbd8c34d29c8df03e81c5419f17a7510a439c"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_c46b1e0305ec5c9adba634f1 record_sha256:59833a7ef056087a253b75f59f817a8d22452ff790e386e2c1ddfc3972c3d1af"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_portable_embodied_inference_runtime"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 4 related objects found", "related:source_c46b1e0305ec5c9adba634f1", "related:concept_end_to_end_embodied_reproducibility", "related:concept_dual_system_world_action_model", "related:concept_portable_embodied_inference_runtime"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T12:17:50+08:00", "source:source_c46b1e0305ec5c9adba634f1 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "3aeb9280869b7f1c8decb74ba3d02933dd8039a212974edc97d4be4a978e7def", "source_state_sha256": "db88a700199ed9de3ce87d9a44515b1c2101d0709065785c5164272fac164df3", "source_record_sha256s": {"source_c46b1e0305ec5c9adba634f1": "59833a7ef056087a253b75f59f817a8d22452ff790e386e2c1ddfc3972c3d1af"}, "raw_state_sha256": "d40dbb21dd3191259875804ea8b543f3ea5095e9fb138fb907091eadb79b9da1", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "acddd40a6235caf416432db66c3fb88004666e744ef86d8b26a027afbfc7d002", "relation_fingerprint": {"outgoing_relations_sha256": "eac2e4bf4c317db25b1fbe8ddad0e9a8f64c58a5b90f8ccf95f5f052b23123fa", "incoming_relations_sha256": "9f3ced585df50a64f814d34873eaaf8750f5b1cf682dbdb16c2b572c6a4eb87f", "full_neighborhood_sha256": "f3ae4b208d267087675fece4404b1ee61139ad638e11168e28b6811ce324b19f"}, "relation_neighborhood_sha256": "f3ae4b208d267087675fece4404b1ee61139ad638e11168e28b6811ce324b19f", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_portable_embodied_inference_runtime"
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
        "object_updated_at:2026-07-19T12:17:50+08:00",
        "source:source_c46b1e0305ec5c9adba634f1 work_sha256:none"
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
        "source:source_c46b1e0305ec5c9adba634f1 record_sha256:59833a7ef056087a253b75f59f817a8d22452ff790e386e2c1ddfc3972c3d1af"
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
        "source:source_c46b1e0305ec5c9adba634f1 raw_sha256:9c26795d85fc431283566eb343ffbd8c34d29c8df03e81c5419f17a7510a439c"
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
        "related:source_c46b1e0305ec5c9adba634f1",
        "related:concept_end_to_end_embodied_reproducibility",
        "related:concept_dual_system_world_action_model",
        "related:concept_portable_embodied_inference_runtime"
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
        "validated:vault/memory/concept/concept_portable_embodied_inference_runtime.md"
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
  "completed_at": "2026-07-19T12:20:19+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "3aeb9280869b7f1c8decb74ba3d02933dd8039a212974edc97d4be4a978e7def",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "d40dbb21dd3191259875804ea8b543f3ea5095e9fb138fb907091eadb79b9da1",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "f3ae4b208d267087675fece4404b1ee61139ad638e11168e28b6811ce324b19f",
      "incoming_relations_sha256": "9f3ced585df50a64f814d34873eaaf8750f5b1cf682dbdb16c2b572c6a4eb87f",
      "outgoing_relations_sha256": "eac2e4bf4c317db25b1fbe8ddad0e9a8f64c58a5b90f8ccf95f5f052b23123fa"
    },
    "relation_neighborhood_sha256": "f3ae4b208d267087675fece4404b1ee61139ad638e11168e28b6811ce324b19f",
    "source_record_sha256s": {
      "source_c46b1e0305ec5c9adba634f1": "59833a7ef056087a253b75f59f817a8d22452ff790e386e2c1ddfc3972c3d1af"
    },
    "source_state_sha256": "db88a700199ed9de3ce87d9a44515b1c2101d0709065785c5164272fac164df3",
    "work_identity_sha256": "acddd40a6235caf416432db66c3fb88004666e744ef86d8b26a027afbfc7d002"
  },
  "consolidation_id": "consolidation_48dc5fcbe817827856b09cd1",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T12:20:19+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_48dc5fcbe817827856b09cd1",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_portable_embodied_inference_runtime",
  "object_sha256_after": "3aeb9280869b7f1c8decb74ba3d02933dd8039a212974edc97d4be4a978e7def",
  "object_sha256_before": "54fa90e03ba4fae54e15db712dd4e3c09eaf45da8d40cb76670d23f9d2c50c4b",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_c46b1e0305ec5c9adba634f1"
  ],
  "source_records": [
    {
      "raw_content_sha256": "9c26795d85fc431283566eb343ffbd8c34d29c8df03e81c5419f17a7510a439c",
      "source_id": "source_c46b1e0305ec5c9adba634f1",
      "source_record_sha256": "59833a7ef056087a253b75f59f817a8d22452ff790e386e2c1ddfc3972c3d1af",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "9c26795d85fc431283566eb343ffbd8c34d29c8df03e81c5419f17a7510a439c"
  ],
  "started_at": "2026-07-19T12:20:19+08:00",
  "status": "complete",
  "title": "Consolidation: 可移植具身推理运行时",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T12:20:19+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
