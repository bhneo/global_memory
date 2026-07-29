---
id: "consolidation_706e5a41bcafbd013bca0544"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 陈旧性对齐的异步慢上下文—快控制接口"
created_at: "2026-07-26T12:33:42+08:00"
updated_at: "2026-07-26T12:33:42+08:00"
consolidation_id: "consolidation_706e5a41bcafbd013bca0544"
object_id: "concept_a858f8d191d3afdd69418471"
object_version_before: 1
object_sha256_before: "86a2644a858c463b4284a1b89784cf7b6fd538d88c16590b4eba5c4a0e5643e5"
object_sha256_after: "bde8f1c73d6783882225367e8b2fd4de43db7224ec3503f015848299f6267042"
source_ids: ["source_d4762e0cf2330ab6ea00a521"]
source_sha256s: ["f8d363f6a631f9a6f28ebfffeb5f9d1cd19b9f8bec643ecf54bcd8744deb0b35"]
source_records: [{"source_id": "source_d4762e0cf2330ab6ea00a521", "source_record_sha256": "b286871c8d1940a63a2092ab31eee35237324336a980824860aefd75aa69ce4a", "raw_content_sha256": "f8d363f6a631f9a6f28ebfffeb5f9d1cd19b9f8bec643ecf54bcd8744deb0b35", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:41+08:00"
completed_at: "2026-07-26T12:33:42+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_a858f8d191d3afdd69418471.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_d4762e0cf2330ab6ea00a521 raw_sha256:f8d363f6a631f9a6f28ebfffeb5f9d1cd19b9f8bec643ecf54bcd8744deb0b35"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_d4762e0cf2330ab6ea00a521 record_sha256:b286871c8d1940a63a2092ab31eee35237324336a980824860aefd75aa69ce4a"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_a858f8d191d3afdd69418471"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 3 related objects found", "related:source_d4762e0cf2330ab6ea00a521", "related:concept_2ce226e08d585158c1dfbb18", "related:concept_asymmetric_frozen_vla_harness"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-26T12:18:42+08:00", "source:source_d4762e0cf2330ab6ea00a521 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "bde8f1c73d6783882225367e8b2fd4de43db7224ec3503f015848299f6267042", "source_state_sha256": "97e61f9964fb989e9132fc68d2ce469cd6d9dc4f56ab9379aa7f17d2732d7700", "source_record_sha256s": {"source_d4762e0cf2330ab6ea00a521": "b286871c8d1940a63a2092ab31eee35237324336a980824860aefd75aa69ce4a"}, "raw_state_sha256": "bbe96c0a5c05b13f91915d45adcf1773bc881ce0204bb9ea5293860d809d5245", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "db949fd50cdb0884964c795446f72fc286aaf24987b73777ecf6fc9597879ef6", "relation_fingerprint": {"outgoing_relations_sha256": "5a298d543f3057e494082075d61fb8688839c069ce4436e6b274a035e1f2a922", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "5a298d543f3057e494082075d61fb8688839c069ce4436e6b274a035e1f2a922"}, "relation_neighborhood_sha256": "5a298d543f3057e494082075d61fb8688839c069ce4436e6b274a035e1f2a922", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_a858f8d191d3afdd69418471"
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
        "object_updated_at:2026-07-26T12:18:42+08:00",
        "source:source_d4762e0cf2330ab6ea00a521 work_sha256:none"
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
        "source:source_d4762e0cf2330ab6ea00a521 record_sha256:b286871c8d1940a63a2092ab31eee35237324336a980824860aefd75aa69ce4a"
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
        "source:source_d4762e0cf2330ab6ea00a521 raw_sha256:f8d363f6a631f9a6f28ebfffeb5f9d1cd19b9f8bec643ecf54bcd8744deb0b35"
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
        "related:source_d4762e0cf2330ab6ea00a521",
        "related:concept_2ce226e08d585158c1dfbb18",
        "related:concept_asymmetric_frozen_vla_harness"
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
        "validated:vault/memory/concept/concept_a858f8d191d3afdd69418471.md"
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
  "completed_at": "2026-07-26T12:33:42+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "bde8f1c73d6783882225367e8b2fd4de43db7224ec3503f015848299f6267042",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "bbe96c0a5c05b13f91915d45adcf1773bc881ce0204bb9ea5293860d809d5245",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "5a298d543f3057e494082075d61fb8688839c069ce4436e6b274a035e1f2a922",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "5a298d543f3057e494082075d61fb8688839c069ce4436e6b274a035e1f2a922"
    },
    "relation_neighborhood_sha256": "5a298d543f3057e494082075d61fb8688839c069ce4436e6b274a035e1f2a922",
    "source_record_sha256s": {
      "source_d4762e0cf2330ab6ea00a521": "b286871c8d1940a63a2092ab31eee35237324336a980824860aefd75aa69ce4a"
    },
    "source_state_sha256": "97e61f9964fb989e9132fc68d2ce469cd6d9dc4f56ab9379aa7f17d2732d7700",
    "work_identity_sha256": "db949fd50cdb0884964c795446f72fc286aaf24987b73777ecf6fc9597879ef6"
  },
  "consolidation_id": "consolidation_706e5a41bcafbd013bca0544",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:42+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_706e5a41bcafbd013bca0544",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_a858f8d191d3afdd69418471",
  "object_sha256_after": "bde8f1c73d6783882225367e8b2fd4de43db7224ec3503f015848299f6267042",
  "object_sha256_before": "86a2644a858c463b4284a1b89784cf7b6fd538d88c16590b4eba5c4a0e5643e5",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_d4762e0cf2330ab6ea00a521"
  ],
  "source_records": [
    {
      "raw_content_sha256": "f8d363f6a631f9a6f28ebfffeb5f9d1cd19b9f8bec643ecf54bcd8744deb0b35",
      "source_id": "source_d4762e0cf2330ab6ea00a521",
      "source_record_sha256": "b286871c8d1940a63a2092ab31eee35237324336a980824860aefd75aa69ce4a",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "f8d363f6a631f9a6f28ebfffeb5f9d1cd19b9f8bec643ecf54bcd8744deb0b35"
  ],
  "started_at": "2026-07-26T12:33:41+08:00",
  "status": "complete",
  "title": "Consolidation: 陈旧性对齐的异步慢上下文—快控制接口",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:42+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
