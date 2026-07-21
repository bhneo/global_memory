---
id: "consolidation_413ab9f4cd628d45bba41a04"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 具身数据闭环"
created_at: "2026-07-20T13:37:39+08:00"
updated_at: "2026-07-20T13:37:39+08:00"
consolidation_id: "consolidation_413ab9f4cd628d45bba41a04"
object_id: "concept_embodied_data_loop"
object_version_before: 1
object_sha256_before: "ebf968525ba4bcb9cb40379904f52d81ce42525a1d461c51623f4e01a0afc845"
object_sha256_after: "428cd18d1f98566ab33e90d35060b791e9389d84440a80553b23251887fa4666"
source_ids: ["source_0a113baae7ce4d1ab78da1a3", "source_cda5a1b9e036598aff53e5be"]
source_sha256s: ["5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5"]
source_records: [{"source_id": "source_0a113baae7ce4d1ab78da1a3", "source_record_sha256": "7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd", "raw_content_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "work_id": null, "work_document_sha256": null}, {"source_id": "source_cda5a1b9e036598aff53e5be", "source_record_sha256": "ae7789297d3d482969f1988999060be39b44f0947bd267ff87ab0e69b8f791f1", "raw_content_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-20T13:37:39+08:00"
completed_at: "2026-07-20T13:37:39+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_embodied_data_loop.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_0a113baae7ce4d1ab78da1a3 raw_sha256:5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "source:source_cda5a1b9e036598aff53e5be raw_sha256:4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_0a113baae7ce4d1ab78da1a3 record_sha256:7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd", "source:source_cda5a1b9e036598aff53e5be record_sha256:ae7789297d3d482969f1988999060be39b44f0947bd267ff87ab0e69b8f791f1"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_embodied_data_loop"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 16 related objects found", "related:source_0a113baae7ce4d1ab78da1a3", "related:source_cda5a1b9e036598aff53e5be", "related:concept_embodied_data_loop", "related:concept_embodied_data_loop", "related:concept_embodied_data_loop"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-20T12:09:47+08:00", "source:source_0a113baae7ce4d1ab78da1a3 work_sha256:none", "source:source_cda5a1b9e036598aff53e5be work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "428cd18d1f98566ab33e90d35060b791e9389d84440a80553b23251887fa4666", "source_state_sha256": "774c2c70337fd26e7afbdb9669f9a74aaef623dc3de9fe750d532872ecbaea63", "source_record_sha256s": {"source_0a113baae7ce4d1ab78da1a3": "7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd", "source_cda5a1b9e036598aff53e5be": "ae7789297d3d482969f1988999060be39b44f0947bd267ff87ab0e69b8f791f1"}, "raw_state_sha256": "e6a015b1429a8731928237ef48f2ce4dbd8d1925ebb2334053fa7326bcbd0c28", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "773bc3e8ce64867512d2e3818f4860feaf9565a47c8784c10b46b31819a4294f", "relation_fingerprint": {"outgoing_relations_sha256": "143a63707a1ebe7265f54581b5632c66cf1ed206679e5955f4a20f13fca0822f", "incoming_relations_sha256": "86c7c0e1868c0376ff16114ea34d88adfad679447045cee3787ab4ca69e32a01", "full_neighborhood_sha256": "29a488510eed1e4cf7cf35f6b0b51a52f312904239ff7172f8ece101e84ebc40"}, "relation_neighborhood_sha256": "29a488510eed1e4cf7cf35f6b0b51a52f312904239ff7172f8ece101e84ebc40", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_embodied_data_loop"
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
        "object_updated_at:2026-07-20T12:09:47+08:00",
        "source:source_0a113baae7ce4d1ab78da1a3 work_sha256:none",
        "source:source_cda5a1b9e036598aff53e5be work_sha256:none"
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
        "source:source_0a113baae7ce4d1ab78da1a3 record_sha256:7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd",
        "source:source_cda5a1b9e036598aff53e5be record_sha256:ae7789297d3d482969f1988999060be39b44f0947bd267ff87ab0e69b8f791f1"
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
        "source:source_0a113baae7ce4d1ab78da1a3 raw_sha256:5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c",
        "source:source_cda5a1b9e036598aff53e5be raw_sha256:4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5"
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
        "relation index inspected; 16 related objects found",
        "related:source_0a113baae7ce4d1ab78da1a3",
        "related:source_cda5a1b9e036598aff53e5be",
        "related:concept_embodied_data_loop",
        "related:concept_embodied_data_loop",
        "related:concept_embodied_data_loop"
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
        "validated:vault/memory/concept/concept_embodied_data_loop.md"
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
  "completed_at": "2026-07-20T13:37:39+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "428cd18d1f98566ab33e90d35060b791e9389d84440a80553b23251887fa4666",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "e6a015b1429a8731928237ef48f2ce4dbd8d1925ebb2334053fa7326bcbd0c28",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "29a488510eed1e4cf7cf35f6b0b51a52f312904239ff7172f8ece101e84ebc40",
      "incoming_relations_sha256": "86c7c0e1868c0376ff16114ea34d88adfad679447045cee3787ab4ca69e32a01",
      "outgoing_relations_sha256": "143a63707a1ebe7265f54581b5632c66cf1ed206679e5955f4a20f13fca0822f"
    },
    "relation_neighborhood_sha256": "29a488510eed1e4cf7cf35f6b0b51a52f312904239ff7172f8ece101e84ebc40",
    "source_record_sha256s": {
      "source_0a113baae7ce4d1ab78da1a3": "7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd",
      "source_cda5a1b9e036598aff53e5be": "ae7789297d3d482969f1988999060be39b44f0947bd267ff87ab0e69b8f791f1"
    },
    "source_state_sha256": "774c2c70337fd26e7afbdb9669f9a74aaef623dc3de9fe750d532872ecbaea63",
    "work_identity_sha256": "773bc3e8ce64867512d2e3818f4860feaf9565a47c8784c10b46b31819a4294f"
  },
  "consolidation_id": "consolidation_413ab9f4cd628d45bba41a04",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-20T13:37:39+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_413ab9f4cd628d45bba41a04",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_embodied_data_loop",
  "object_sha256_after": "428cd18d1f98566ab33e90d35060b791e9389d84440a80553b23251887fa4666",
  "object_sha256_before": "ebf968525ba4bcb9cb40379904f52d81ce42525a1d461c51623f4e01a0afc845",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_0a113baae7ce4d1ab78da1a3",
    "source_cda5a1b9e036598aff53e5be"
  ],
  "source_records": [
    {
      "raw_content_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c",
      "source_id": "source_0a113baae7ce4d1ab78da1a3",
      "source_record_sha256": "7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd",
      "work_document_sha256": null,
      "work_id": null
    },
    {
      "raw_content_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5",
      "source_id": "source_cda5a1b9e036598aff53e5be",
      "source_record_sha256": "ae7789297d3d482969f1988999060be39b44f0947bd267ff87ab0e69b8f791f1",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c",
    "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5"
  ],
  "started_at": "2026-07-20T13:37:39+08:00",
  "status": "complete",
  "title": "Consolidation: 具身数据闭环",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-20T13:37:39+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
