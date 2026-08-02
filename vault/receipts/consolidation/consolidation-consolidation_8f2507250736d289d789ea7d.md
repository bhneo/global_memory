---
id: "consolidation_8f2507250736d289d789ea7d"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 多时间尺度触觉世界模型控制"
created_at: "2026-08-02T19:55:39+08:00"
updated_at: "2026-08-02T19:55:39+08:00"
consolidation_id: "consolidation_8f2507250736d289d789ea7d"
object_id: "concept_multitimescale_tactile_world_model"
object_version_before: 1
object_sha256_before: "cf3578da0ac2b34c7a4d86e0703dfc56d3711370beb7c923269ed5003c868d58"
object_sha256_after: "44f31102755642b2b4fbdae4f70e35213bb21c025849541be92605d060223314"
source_ids: ["source_283911da72edc403d1b823fb", "source_c79f943c818d06054ca5cf92"]
source_sha256s: ["1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558", "17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb"]
source_records: [{"source_id": "source_283911da72edc403d1b823fb", "source_record_sha256": "79a6150e5aae2900abec238d83123f02e13565489e12f09da8d943dfc7d76ccb", "raw_content_sha256": "1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558", "work_id": null, "work_document_sha256": null}, {"source_id": "source_c79f943c818d06054ca5cf92", "source_record_sha256": "986d4ba674af6cd7d3f115e76d98503b7e54f7701c55a2494d550f31f1158adc", "raw_content_sha256": "17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-08-02T19:55:38+08:00"
completed_at: "2026-08-02T19:55:39+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_multitimescale_tactile_world_model.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_283911da72edc403d1b823fb raw_sha256:1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558", "source:source_c79f943c818d06054ca5cf92 raw_sha256:17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_283911da72edc403d1b823fb record_sha256:79a6150e5aae2900abec238d83123f02e13565489e12f09da8d943dfc7d76ccb", "source:source_c79f943c818d06054ca5cf92 record_sha256:986d4ba674af6cd7d3f115e76d98503b7e54f7701c55a2494d550f31f1158adc"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 4 candidates inspected", "candidate:concept_multitimescale_tactile_world_model", "candidate:reflection_4b63a8834e11b28db3cf2fdc", "candidate:reflection_dc321adda5d26fa9e6f71d5a", "candidate:reflection_e8e62c04da8ad9f420c37be4"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 15 related objects found", "related:source_283911da72edc403d1b823fb", "related:concept_predictive_vla_deployment", "related:concept_d01c4f0b61292d29f0a7ffe2", "related:concept_vla_action_cache_refinement", "related:concept_world_model_evaluation"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-28T16:32:20+08:00", "source:source_283911da72edc403d1b823fb work_sha256:none", "source:source_c79f943c818d06054ca5cf92 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "44f31102755642b2b4fbdae4f70e35213bb21c025849541be92605d060223314", "source_state_sha256": "266616e2c158263659edfa5265a37f0d341ffbecea2f46efd4f755d9532b4d5b", "source_record_sha256s": {"source_283911da72edc403d1b823fb": "79a6150e5aae2900abec238d83123f02e13565489e12f09da8d943dfc7d76ccb", "source_c79f943c818d06054ca5cf92": "986d4ba674af6cd7d3f115e76d98503b7e54f7701c55a2494d550f31f1158adc"}, "raw_state_sha256": "a6d3c04f17215cd49c8e8477f8f087d15f2c2ffe1871d3e382acfc828af4cc65", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "53d5c6138d51df85b287e305967a17ff8fd1d14620b540bd584fd59971fa06e6", "relation_fingerprint": {"outgoing_relations_sha256": "5f654e392914acc5415e211245e3458fb9f35cc8f4db4122aaac24b313388fdf", "incoming_relations_sha256": "aa8e586d37ed9f43bb3766c47444fa431265007f4e773b2923558d15a21c0029", "full_neighborhood_sha256": "f380718857c9996e5454f3f12a5da8306c73e480e71be418d816500db37d8c94"}, "relation_neighborhood_sha256": "f380718857c9996e5454f3f12a5da8306c73e480e71be418d816500db37d8c94", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "searched title; 4 candidates inspected",
        "candidate:concept_multitimescale_tactile_world_model",
        "candidate:reflection_4b63a8834e11b28db3cf2fdc",
        "candidate:reflection_dc321adda5d26fa9e6f71d5a",
        "candidate:reflection_e8e62c04da8ad9f420c37be4"
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
        "object_updated_at:2026-07-28T16:32:20+08:00",
        "source:source_283911da72edc403d1b823fb work_sha256:none",
        "source:source_c79f943c818d06054ca5cf92 work_sha256:none"
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
        "source:source_283911da72edc403d1b823fb record_sha256:79a6150e5aae2900abec238d83123f02e13565489e12f09da8d943dfc7d76ccb",
        "source:source_c79f943c818d06054ca5cf92 record_sha256:986d4ba674af6cd7d3f115e76d98503b7e54f7701c55a2494d550f31f1158adc"
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
        "source:source_283911da72edc403d1b823fb raw_sha256:1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558",
        "source:source_c79f943c818d06054ca5cf92 raw_sha256:17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb"
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
        "relation index inspected; 15 related objects found",
        "related:source_283911da72edc403d1b823fb",
        "related:concept_predictive_vla_deployment",
        "related:concept_d01c4f0b61292d29f0a7ffe2",
        "related:concept_vla_action_cache_refinement",
        "related:concept_world_model_evaluation"
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
        "validated:vault/memory/concept/concept_multitimescale_tactile_world_model.md"
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
  "completed_at": "2026-08-02T19:55:39+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "44f31102755642b2b4fbdae4f70e35213bb21c025849541be92605d060223314",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "a6d3c04f17215cd49c8e8477f8f087d15f2c2ffe1871d3e382acfc828af4cc65",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "f380718857c9996e5454f3f12a5da8306c73e480e71be418d816500db37d8c94",
      "incoming_relations_sha256": "aa8e586d37ed9f43bb3766c47444fa431265007f4e773b2923558d15a21c0029",
      "outgoing_relations_sha256": "5f654e392914acc5415e211245e3458fb9f35cc8f4db4122aaac24b313388fdf"
    },
    "relation_neighborhood_sha256": "f380718857c9996e5454f3f12a5da8306c73e480e71be418d816500db37d8c94",
    "source_record_sha256s": {
      "source_283911da72edc403d1b823fb": "79a6150e5aae2900abec238d83123f02e13565489e12f09da8d943dfc7d76ccb",
      "source_c79f943c818d06054ca5cf92": "986d4ba674af6cd7d3f115e76d98503b7e54f7701c55a2494d550f31f1158adc"
    },
    "source_state_sha256": "266616e2c158263659edfa5265a37f0d341ffbecea2f46efd4f755d9532b4d5b",
    "work_identity_sha256": "53d5c6138d51df85b287e305967a17ff8fd1d14620b540bd584fd59971fa06e6"
  },
  "consolidation_id": "consolidation_8f2507250736d289d789ea7d",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-08-02T19:55:39+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_8f2507250736d289d789ea7d",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_multitimescale_tactile_world_model",
  "object_sha256_after": "44f31102755642b2b4fbdae4f70e35213bb21c025849541be92605d060223314",
  "object_sha256_before": "cf3578da0ac2b34c7a4d86e0703dfc56d3711370beb7c923269ed5003c868d58",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_283911da72edc403d1b823fb",
    "source_c79f943c818d06054ca5cf92"
  ],
  "source_records": [
    {
      "raw_content_sha256": "1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558",
      "source_id": "source_283911da72edc403d1b823fb",
      "source_record_sha256": "79a6150e5aae2900abec238d83123f02e13565489e12f09da8d943dfc7d76ccb",
      "work_document_sha256": null,
      "work_id": null
    },
    {
      "raw_content_sha256": "17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb",
      "source_id": "source_c79f943c818d06054ca5cf92",
      "source_record_sha256": "986d4ba674af6cd7d3f115e76d98503b7e54f7701c55a2494d550f31f1158adc",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558",
    "17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb"
  ],
  "started_at": "2026-08-02T19:55:38+08:00",
  "status": "complete",
  "title": "Consolidation: 多时间尺度触觉世界模型控制",
  "type": "consolidation_receipt",
  "updated_at": "2026-08-02T19:55:39+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
