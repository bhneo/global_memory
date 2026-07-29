---
id: "consolidation_bec4e0095f884853daf6e939"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 查询介导的 VLA 动作表征塑形"
created_at: "2026-07-26T12:33:23+08:00"
updated_at: "2026-07-26T12:33:23+08:00"
consolidation_id: "consolidation_bec4e0095f884853daf6e939"
object_id: "concept_149582520594364a508516c6"
object_version_before: 1
object_sha256_before: "8b88bf9f11b701fc30b86a43bdd05a2b1376b87be541700e7ac323cb17dc1ff6"
object_sha256_after: "6e4a3884836a99dc2f90e9a39e4eac0489463121a9b2fb69cea16d3c8ce66a15"
source_ids: ["source_9b0d550203c4d7bd7acf8a36"]
source_sha256s: ["29fb80abd6ad13993c768785bf3cc8f639a5eed42b7606d495e74edcf2fdfa3f"]
source_records: [{"source_id": "source_9b0d550203c4d7bd7acf8a36", "source_record_sha256": "426f334157eacc62bf125bc87264453358e1e0bbe64a995c0d3cbd21c4a407ac", "raw_content_sha256": "29fb80abd6ad13993c768785bf3cc8f639a5eed42b7606d495e74edcf2fdfa3f", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:23+08:00"
completed_at: "2026-07-26T12:33:23+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_149582520594364a508516c6.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_9b0d550203c4d7bd7acf8a36 raw_sha256:29fb80abd6ad13993c768785bf3cc8f639a5eed42b7606d495e74edcf2fdfa3f"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_9b0d550203c4d7bd7acf8a36 record_sha256:426f334157eacc62bf125bc87264453358e1e0bbe64a995c0d3cbd21c4a407ac"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_149582520594364a508516c6"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_9b0d550203c4d7bd7acf8a36", "related:concept_action_centric_embodied_vlm_taxonomy"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-22T18:12:09+08:00", "source:source_9b0d550203c4d7bd7acf8a36 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "6e4a3884836a99dc2f90e9a39e4eac0489463121a9b2fb69cea16d3c8ce66a15", "source_state_sha256": "d36fc2e75d30572df972c746e1ad2b5b0b005d1b98337e4770696ca8d93b4b60", "source_record_sha256s": {"source_9b0d550203c4d7bd7acf8a36": "426f334157eacc62bf125bc87264453358e1e0bbe64a995c0d3cbd21c4a407ac"}, "raw_state_sha256": "225f30aa1189117c6a97ff8fe3208cd6566f73e1cb8f3a2b7cf878df95e80553", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "fb5b6e837814f99c6f983cbfee0962c3fb3c8e584b07866554cf422cb2cb380a", "relation_fingerprint": {"outgoing_relations_sha256": "b850732233ea0fbc6ab7b0515f60bc28e3c4d9f1e5d360020d286d138f454893", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "b850732233ea0fbc6ab7b0515f60bc28e3c4d9f1e5d360020d286d138f454893"}, "relation_neighborhood_sha256": "b850732233ea0fbc6ab7b0515f60bc28e3c4d9f1e5d360020d286d138f454893", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_149582520594364a508516c6"
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
        "object_updated_at:2026-07-22T18:12:09+08:00",
        "source:source_9b0d550203c4d7bd7acf8a36 work_sha256:none"
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
        "source:source_9b0d550203c4d7bd7acf8a36 record_sha256:426f334157eacc62bf125bc87264453358e1e0bbe64a995c0d3cbd21c4a407ac"
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
        "source:source_9b0d550203c4d7bd7acf8a36 raw_sha256:29fb80abd6ad13993c768785bf3cc8f639a5eed42b7606d495e74edcf2fdfa3f"
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
        "relation index inspected; 2 related objects found",
        "related:source_9b0d550203c4d7bd7acf8a36",
        "related:concept_action_centric_embodied_vlm_taxonomy"
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
        "validated:vault/memory/concept/concept_149582520594364a508516c6.md"
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
  "completed_at": "2026-07-26T12:33:23+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "6e4a3884836a99dc2f90e9a39e4eac0489463121a9b2fb69cea16d3c8ce66a15",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "225f30aa1189117c6a97ff8fe3208cd6566f73e1cb8f3a2b7cf878df95e80553",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "b850732233ea0fbc6ab7b0515f60bc28e3c4d9f1e5d360020d286d138f454893",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "b850732233ea0fbc6ab7b0515f60bc28e3c4d9f1e5d360020d286d138f454893"
    },
    "relation_neighborhood_sha256": "b850732233ea0fbc6ab7b0515f60bc28e3c4d9f1e5d360020d286d138f454893",
    "source_record_sha256s": {
      "source_9b0d550203c4d7bd7acf8a36": "426f334157eacc62bf125bc87264453358e1e0bbe64a995c0d3cbd21c4a407ac"
    },
    "source_state_sha256": "d36fc2e75d30572df972c746e1ad2b5b0b005d1b98337e4770696ca8d93b4b60",
    "work_identity_sha256": "fb5b6e837814f99c6f983cbfee0962c3fb3c8e584b07866554cf422cb2cb380a"
  },
  "consolidation_id": "consolidation_bec4e0095f884853daf6e939",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:23+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_bec4e0095f884853daf6e939",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_149582520594364a508516c6",
  "object_sha256_after": "6e4a3884836a99dc2f90e9a39e4eac0489463121a9b2fb69cea16d3c8ce66a15",
  "object_sha256_before": "8b88bf9f11b701fc30b86a43bdd05a2b1376b87be541700e7ac323cb17dc1ff6",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_9b0d550203c4d7bd7acf8a36"
  ],
  "source_records": [
    {
      "raw_content_sha256": "29fb80abd6ad13993c768785bf3cc8f639a5eed42b7606d495e74edcf2fdfa3f",
      "source_id": "source_9b0d550203c4d7bd7acf8a36",
      "source_record_sha256": "426f334157eacc62bf125bc87264453358e1e0bbe64a995c0d3cbd21c4a407ac",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "29fb80abd6ad13993c768785bf3cc8f639a5eed42b7606d495e74edcf2fdfa3f"
  ],
  "started_at": "2026-07-26T12:33:23+08:00",
  "status": "complete",
  "title": "Consolidation: 查询介导的 VLA 动作表征塑形",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:23+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
