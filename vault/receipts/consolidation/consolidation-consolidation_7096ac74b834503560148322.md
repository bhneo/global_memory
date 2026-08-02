---
id: "consolidation_7096ac74b834503560148322"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 延迟自适应的三段 flow 动作调度 / Latency-adaptive three-region flow action schedule"
created_at: "2026-08-02T12:30:31+08:00"
updated_at: "2026-08-02T12:30:31+08:00"
consolidation_id: "consolidation_7096ac74b834503560148322"
object_id: "concept_2c69b09323afa79344401cd8"
object_version_before: 1
object_sha256_before: "c682ad920ac3617408da7ea1952e4a67bcd54b4a569e78809ef9868ab4066b3a"
object_sha256_after: "5ffa5130a93236c01d5dded2e4ebd8f2218e3802186200b68f8bba524d92693f"
source_ids: ["source_9ddfb0f3d50b606bd13e17e2"]
source_sha256s: ["cad352444bb5990cac9f8ccd05c5582189745448a987ed41a518e5ca1deebf4c"]
source_records: [{"source_id": "source_9ddfb0f3d50b606bd13e17e2", "source_record_sha256": "63ee8f8873a2fa3dc329786c62c99dcdc50943fbb3a1adb7245bbc72a7265253", "raw_content_sha256": "cad352444bb5990cac9f8ccd05c5582189745448a987ed41a518e5ca1deebf4c", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-08-02T12:30:31+08:00"
completed_at: "2026-08-02T12:30:31+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_2c69b09323afa79344401cd8.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_9ddfb0f3d50b606bd13e17e2 raw_sha256:cad352444bb5990cac9f8ccd05c5582189745448a987ed41a518e5ca1deebf4c"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_9ddfb0f3d50b606bd13e17e2 record_sha256:63ee8f8873a2fa3dc329786c62c99dcdc50943fbb3a1adb7245bbc72a7265253"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_2c69b09323afa79344401cd8"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 3 related objects found", "related:source_9ddfb0f3d50b606bd13e17e2", "related:concept_a858f8d191d3afdd69418471", "related:concept_dynamic_execution_horizon"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-08-01T18:23:05+08:00", "source:source_9ddfb0f3d50b606bd13e17e2 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "5ffa5130a93236c01d5dded2e4ebd8f2218e3802186200b68f8bba524d92693f", "source_state_sha256": "b3c8c816314433b9808ef6af0ad04ab7e9e3b8ead4cea41e254eca43cef86ace", "source_record_sha256s": {"source_9ddfb0f3d50b606bd13e17e2": "63ee8f8873a2fa3dc329786c62c99dcdc50943fbb3a1adb7245bbc72a7265253"}, "raw_state_sha256": "e9cff5eadea001bd39c8bef4bbfd8c49feccd0e73511b7b5e17a53af48dcefa8", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "7f0df9504f3decc4e26d7f51f5366afb3e2a1ddad6216fc7a18ae1711f366c75", "relation_fingerprint": {"outgoing_relations_sha256": "d2ec5edf847912fd9d38d187b3f7b22745b25dd3378f89be4c68a173c008bded", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "d2ec5edf847912fd9d38d187b3f7b22745b25dd3378f89be4c68a173c008bded"}, "relation_neighborhood_sha256": "d2ec5edf847912fd9d38d187b3f7b22745b25dd3378f89be4c68a173c008bded", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_2c69b09323afa79344401cd8"
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
        "object_updated_at:2026-08-01T18:23:05+08:00",
        "source:source_9ddfb0f3d50b606bd13e17e2 work_sha256:none"
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
        "source:source_9ddfb0f3d50b606bd13e17e2 record_sha256:63ee8f8873a2fa3dc329786c62c99dcdc50943fbb3a1adb7245bbc72a7265253"
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
        "source:source_9ddfb0f3d50b606bd13e17e2 raw_sha256:cad352444bb5990cac9f8ccd05c5582189745448a987ed41a518e5ca1deebf4c"
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
        "related:source_9ddfb0f3d50b606bd13e17e2",
        "related:concept_a858f8d191d3afdd69418471",
        "related:concept_dynamic_execution_horizon"
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
        "validated:vault/memory/concept/concept_2c69b09323afa79344401cd8.md"
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
  "completed_at": "2026-08-02T12:30:31+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "5ffa5130a93236c01d5dded2e4ebd8f2218e3802186200b68f8bba524d92693f",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "e9cff5eadea001bd39c8bef4bbfd8c49feccd0e73511b7b5e17a53af48dcefa8",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "d2ec5edf847912fd9d38d187b3f7b22745b25dd3378f89be4c68a173c008bded",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "d2ec5edf847912fd9d38d187b3f7b22745b25dd3378f89be4c68a173c008bded"
    },
    "relation_neighborhood_sha256": "d2ec5edf847912fd9d38d187b3f7b22745b25dd3378f89be4c68a173c008bded",
    "source_record_sha256s": {
      "source_9ddfb0f3d50b606bd13e17e2": "63ee8f8873a2fa3dc329786c62c99dcdc50943fbb3a1adb7245bbc72a7265253"
    },
    "source_state_sha256": "b3c8c816314433b9808ef6af0ad04ab7e9e3b8ead4cea41e254eca43cef86ace",
    "work_identity_sha256": "7f0df9504f3decc4e26d7f51f5366afb3e2a1ddad6216fc7a18ae1711f366c75"
  },
  "consolidation_id": "consolidation_7096ac74b834503560148322",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-08-02T12:30:31+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_7096ac74b834503560148322",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_2c69b09323afa79344401cd8",
  "object_sha256_after": "5ffa5130a93236c01d5dded2e4ebd8f2218e3802186200b68f8bba524d92693f",
  "object_sha256_before": "c682ad920ac3617408da7ea1952e4a67bcd54b4a569e78809ef9868ab4066b3a",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_9ddfb0f3d50b606bd13e17e2"
  ],
  "source_records": [
    {
      "raw_content_sha256": "cad352444bb5990cac9f8ccd05c5582189745448a987ed41a518e5ca1deebf4c",
      "source_id": "source_9ddfb0f3d50b606bd13e17e2",
      "source_record_sha256": "63ee8f8873a2fa3dc329786c62c99dcdc50943fbb3a1adb7245bbc72a7265253",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "cad352444bb5990cac9f8ccd05c5582189745448a987ed41a518e5ca1deebf4c"
  ],
  "started_at": "2026-08-02T12:30:31+08:00",
  "status": "complete",
  "title": "Consolidation: 延迟自适应的三段 flow 动作调度 / Latency-adaptive three-region flow action schedule",
  "type": "consolidation_receipt",
  "updated_at": "2026-08-02T12:30:31+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
