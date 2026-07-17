---
id: "consolidation_940694467e0fde479e7eaf00"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 具身数据规模 vs 数据结构与闭环"
created_at: "2026-07-17T22:40:12+08:00"
updated_at: "2026-07-17T22:40:12+08:00"
consolidation_id: "consolidation_940694467e0fde479e7eaf00"
object_id: "tension_embodied_data_scale_structure"
object_version_before: 1
object_sha256_before: "076ddc829cf5d1bb6a1272d8394648aed10f26f257e7ce5063a486d7a9ca532e"
object_sha256_after: "07786358fd01054a851c7a59e8da05c96ca8b53d710f7ec93254d09da1995e6a"
source_ids: ["source_cda5a1b9e036598aff53e5be", "source_0a113baae7ce4d1ab78da1a3"]
source_sha256s: ["4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c"]
source_records: [{"source_id": "source_cda5a1b9e036598aff53e5be", "source_record_sha256": "ae7789297d3d482969f1988999060be39b44f0947bd267ff87ab0e69b8f791f1", "raw_content_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "work_id": null, "work_document_sha256": null}, {"source_id": "source_0a113baae7ce4d1ab78da1a3", "source_record_sha256": "7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd", "raw_content_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-17T22:40:11+08:00"
completed_at: "2026-07-17T22:40:12+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/tension/tension_embodied_data_scale_structure.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_cda5a1b9e036598aff53e5be raw_sha256:4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "source:source_0a113baae7ce4d1ab78da1a3 raw_sha256:5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_cda5a1b9e036598aff53e5be record_sha256:ae7789297d3d482969f1988999060be39b44f0947bd267ff87ab0e69b8f791f1", "source:source_0a113baae7ce4d1ab78da1a3 record_sha256:7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:tension_embodied_data_scale_structure"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 4 related objects found", "related:source_0a113baae7ce4d1ab78da1a3", "related:source_cda5a1b9e036598aff53e5be", "related:concept_embodied_data_loop", "related:tension_embodied_data_scale_structure"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T18:39:38+08:00", "source:source_cda5a1b9e036598aff53e5be work_sha256:none", "source:source_0a113baae7ce4d1ab78da1a3 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "07786358fd01054a851c7a59e8da05c96ca8b53d710f7ec93254d09da1995e6a", "source_state_sha256": "b4712198865afd6c60d9bdd36a9dfdc24a5f3087261404c74cf67e2c932544cf", "source_record_sha256s": {"source_cda5a1b9e036598aff53e5be": "ae7789297d3d482969f1988999060be39b44f0947bd267ff87ab0e69b8f791f1", "source_0a113baae7ce4d1ab78da1a3": "7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd"}, "raw_state_sha256": "f7a280a20080f2958f072fc6e6b0a713b3e5d277058274ab7411a828bf70b1a5", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "ce49f66b091acded703d1d47f7d4b45297834f474fe691319c6d54f33d87f18b", "relation_fingerprint": {"outgoing_relations_sha256": "c3c466c7cd9cad2b115feab9374394c94c315ba2aee4c50c86fdd6707ee09921", "incoming_relations_sha256": "ab69564d83475a386e41fa3e4dd96817935914174d4d10046631deffc045616e", "full_neighborhood_sha256": "8dcc5610f49b24cdb5b061090b15120dbf21b29e72ac72ce65ddb8997985e8ad"}, "relation_neighborhood_sha256": "8dcc5610f49b24cdb5b061090b15120dbf21b29e72ac72ce65ddb8997985e8ad", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "requalification_candidate"
changes: []
change_summary: "Receipt v2 revalidated under incoming and outgoing relation fingerprint boundary"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "Receipt v2 revalidated under incoming and outgoing relation fingerprint boundary",
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
        "candidate:tension_embodied_data_scale_structure"
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
        "object_updated_at:2026-07-17T18:39:38+08:00",
        "source:source_cda5a1b9e036598aff53e5be work_sha256:none",
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
        "source:source_cda5a1b9e036598aff53e5be record_sha256:ae7789297d3d482969f1988999060be39b44f0947bd267ff87ab0e69b8f791f1",
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
        "source:source_cda5a1b9e036598aff53e5be raw_sha256:4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5",
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
        "related:source_cda5a1b9e036598aff53e5be",
        "related:concept_embodied_data_loop",
        "related:tension_embodied_data_scale_structure"
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
        "validated:vault/memory/tension/tension_embodied_data_scale_structure.md"
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
  "completed_at": "2026-07-17T22:40:12+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "07786358fd01054a851c7a59e8da05c96ca8b53d710f7ec93254d09da1995e6a",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "f7a280a20080f2958f072fc6e6b0a713b3e5d277058274ab7411a828bf70b1a5",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "8dcc5610f49b24cdb5b061090b15120dbf21b29e72ac72ce65ddb8997985e8ad",
      "incoming_relations_sha256": "ab69564d83475a386e41fa3e4dd96817935914174d4d10046631deffc045616e",
      "outgoing_relations_sha256": "c3c466c7cd9cad2b115feab9374394c94c315ba2aee4c50c86fdd6707ee09921"
    },
    "relation_neighborhood_sha256": "8dcc5610f49b24cdb5b061090b15120dbf21b29e72ac72ce65ddb8997985e8ad",
    "source_record_sha256s": {
      "source_0a113baae7ce4d1ab78da1a3": "7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd",
      "source_cda5a1b9e036598aff53e5be": "ae7789297d3d482969f1988999060be39b44f0947bd267ff87ab0e69b8f791f1"
    },
    "source_state_sha256": "b4712198865afd6c60d9bdd36a9dfdc24a5f3087261404c74cf67e2c932544cf",
    "work_identity_sha256": "ce49f66b091acded703d1d47f7d4b45297834f474fe691319c6d54f33d87f18b"
  },
  "consolidation_id": "consolidation_940694467e0fde479e7eaf00",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-17T22:40:12+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_940694467e0fde479e7eaf00",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "tension_embodied_data_scale_structure",
  "object_sha256_after": "07786358fd01054a851c7a59e8da05c96ca8b53d710f7ec93254d09da1995e6a",
  "object_sha256_before": "076ddc829cf5d1bb6a1272d8394648aed10f26f257e7ce5063a486d7a9ca532e",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "requalification_candidate",
  "source_ids": [
    "source_cda5a1b9e036598aff53e5be",
    "source_0a113baae7ce4d1ab78da1a3"
  ],
  "source_records": [
    {
      "raw_content_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5",
      "source_id": "source_cda5a1b9e036598aff53e5be",
      "source_record_sha256": "ae7789297d3d482969f1988999060be39b44f0947bd267ff87ab0e69b8f791f1",
      "work_document_sha256": null,
      "work_id": null
    },
    {
      "raw_content_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c",
      "source_id": "source_0a113baae7ce4d1ab78da1a3",
      "source_record_sha256": "7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5",
    "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c"
  ],
  "started_at": "2026-07-17T22:40:11+08:00",
  "status": "complete",
  "title": "Consolidation: 具身数据规模 vs 数据结构与闭环",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T22:40:12+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
