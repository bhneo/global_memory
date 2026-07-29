---
id: "consolidation_5ade1001b519b74eb8edc9cc"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: Block-causal dense patch policy / 区块因果的密集视觉策略"
created_at: "2026-07-27T19:06:45+08:00"
updated_at: "2026-07-27T19:06:45+08:00"
consolidation_id: "consolidation_5ade1001b519b74eb8edc9cc"
object_id: "concept_97fc87cffe27a2fc9d741e78"
object_version_before: 1
object_sha256_before: "e377859a5357835a65ab088438138fd47c5b98316b5796f1d613494fd67c264e"
object_sha256_after: "73b139602879251d96c366daef6a8fb9e5eef5035029322c20934f15b76d0646"
source_ids: ["source_e8651a193623cbe2b86becb0"]
source_sha256s: ["aa755019b83403534f8e418ed52407197770b9eeeca2d46b581b31a01790b3fd"]
source_records: [{"source_id": "source_e8651a193623cbe2b86becb0", "source_record_sha256": "ebbb571e04a8ba0ba39406c91d4f66adcdb2e0dfca25c1d56c541a90420c2fd8", "raw_content_sha256": "aa755019b83403534f8e418ed52407197770b9eeeca2d46b581b31a01790b3fd", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-27T19:06:44+08:00"
completed_at: "2026-07-27T19:06:45+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_97fc87cffe27a2fc9d741e78.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_e8651a193623cbe2b86becb0 raw_sha256:aa755019b83403534f8e418ed52407197770b9eeeca2d46b581b31a01790b3fd"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_e8651a193623cbe2b86becb0 record_sha256:ebbb571e04a8ba0ba39406c91d4f66adcdb2e0dfca25c1d56c541a90420c2fd8"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_97fc87cffe27a2fc9d741e78"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_e8651a193623cbe2b86becb0"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-27T18:14:48+08:00", "source:source_e8651a193623cbe2b86becb0 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "73b139602879251d96c366daef6a8fb9e5eef5035029322c20934f15b76d0646", "source_state_sha256": "e6b00ef360c4ffddec66654b4b221703b2ed5a5d177ba484aa86f20b712ec598", "source_record_sha256s": {"source_e8651a193623cbe2b86becb0": "ebbb571e04a8ba0ba39406c91d4f66adcdb2e0dfca25c1d56c541a90420c2fd8"}, "raw_state_sha256": "fed3638089c7308bfa374533e98caae8b5c9a50f32ad12cb1154a82ff99aa07d", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "f228035f0f68cff91d104c58c6e2de4904f96051d67ec56bcabaec6913a6d86a", "relation_fingerprint": {"outgoing_relations_sha256": "094164cecba215fed449a965339634a83fc02eea80ba59a81679ad0a4ca1530b", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "094164cecba215fed449a965339634a83fc02eea80ba59a81679ad0a4ca1530b"}, "relation_neighborhood_sha256": "094164cecba215fed449a965339634a83fc02eea80ba59a81679ad0a4ca1530b", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_97fc87cffe27a2fc9d741e78"
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
        "object_updated_at:2026-07-27T18:14:48+08:00",
        "source:source_e8651a193623cbe2b86becb0 work_sha256:none"
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
        "source:source_e8651a193623cbe2b86becb0 record_sha256:ebbb571e04a8ba0ba39406c91d4f66adcdb2e0dfca25c1d56c541a90420c2fd8"
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
        "source:source_e8651a193623cbe2b86becb0 raw_sha256:aa755019b83403534f8e418ed52407197770b9eeeca2d46b581b31a01790b3fd"
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
        "relation index inspected; 1 related objects found",
        "related:source_e8651a193623cbe2b86becb0"
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
        "validated:vault/memory/concept/concept_97fc87cffe27a2fc9d741e78.md"
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
  "completed_at": "2026-07-27T19:06:45+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "73b139602879251d96c366daef6a8fb9e5eef5035029322c20934f15b76d0646",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "fed3638089c7308bfa374533e98caae8b5c9a50f32ad12cb1154a82ff99aa07d",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "094164cecba215fed449a965339634a83fc02eea80ba59a81679ad0a4ca1530b",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "094164cecba215fed449a965339634a83fc02eea80ba59a81679ad0a4ca1530b"
    },
    "relation_neighborhood_sha256": "094164cecba215fed449a965339634a83fc02eea80ba59a81679ad0a4ca1530b",
    "source_record_sha256s": {
      "source_e8651a193623cbe2b86becb0": "ebbb571e04a8ba0ba39406c91d4f66adcdb2e0dfca25c1d56c541a90420c2fd8"
    },
    "source_state_sha256": "e6b00ef360c4ffddec66654b4b221703b2ed5a5d177ba484aa86f20b712ec598",
    "work_identity_sha256": "f228035f0f68cff91d104c58c6e2de4904f96051d67ec56bcabaec6913a6d86a"
  },
  "consolidation_id": "consolidation_5ade1001b519b74eb8edc9cc",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-27T19:06:45+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_5ade1001b519b74eb8edc9cc",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_97fc87cffe27a2fc9d741e78",
  "object_sha256_after": "73b139602879251d96c366daef6a8fb9e5eef5035029322c20934f15b76d0646",
  "object_sha256_before": "e377859a5357835a65ab088438138fd47c5b98316b5796f1d613494fd67c264e",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_e8651a193623cbe2b86becb0"
  ],
  "source_records": [
    {
      "raw_content_sha256": "aa755019b83403534f8e418ed52407197770b9eeeca2d46b581b31a01790b3fd",
      "source_id": "source_e8651a193623cbe2b86becb0",
      "source_record_sha256": "ebbb571e04a8ba0ba39406c91d4f66adcdb2e0dfca25c1d56c541a90420c2fd8",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "aa755019b83403534f8e418ed52407197770b9eeeca2d46b581b31a01790b3fd"
  ],
  "started_at": "2026-07-27T19:06:44+08:00",
  "status": "complete",
  "title": "Consolidation: Block-causal dense patch policy / 区块因果的密集视觉策略",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-27T19:06:45+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
