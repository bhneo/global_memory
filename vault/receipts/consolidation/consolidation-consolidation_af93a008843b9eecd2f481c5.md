---
id: "consolidation_af93a008843b9eecd2f481c5"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 上下文匹配的失败动作有界重定向 / Context-matched bounded redirection of failure actions"
created_at: "2026-08-02T19:54:58+08:00"
updated_at: "2026-08-02T19:54:58+08:00"
consolidation_id: "consolidation_af93a008843b9eecd2f481c5"
object_id: "concept_61c0ffd089f650a51ec3f00d"
object_version_before: 1
object_sha256_before: "0a9c66a5a6a32d9615b8f4b942101f3777b43b1c1c11c466ffdfb47ea08914a9"
object_sha256_after: "3b30a69d6eee28d0953e5fb79ea383c6d88c2d3e9291524be1f53f11ee01afc4"
source_ids: ["source_9f9972326eb118a8e4bb5623"]
source_sha256s: ["b4ca82a153732c8fdae606f271f37ecceb2d091c19e221cd1d3c6e21f73311ea"]
source_records: [{"source_id": "source_9f9972326eb118a8e4bb5623", "source_record_sha256": "0adbdcabf38d2a0e7fb4a29a8c5a22243474ebc3697cd3076d29d0c2ca32ab2c", "raw_content_sha256": "b4ca82a153732c8fdae606f271f37ecceb2d091c19e221cd1d3c6e21f73311ea", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-08-02T19:54:58+08:00"
completed_at: "2026-08-02T19:54:58+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_61c0ffd089f650a51ec3f00d.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_9f9972326eb118a8e4bb5623 raw_sha256:b4ca82a153732c8fdae606f271f37ecceb2d091c19e221cd1d3c6e21f73311ea"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_9f9972326eb118a8e4bb5623 record_sha256:0adbdcabf38d2a0e7fb4a29a8c5a22243474ebc3697cd3076d29d0c2ca32ab2c"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_61c0ffd089f650a51ec3f00d"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_9f9972326eb118a8e4bb5623", "related:concept_6a559a41722de87986c350e7"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-08-02T18:21:45+08:00", "source:source_9f9972326eb118a8e4bb5623 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "3b30a69d6eee28d0953e5fb79ea383c6d88c2d3e9291524be1f53f11ee01afc4", "source_state_sha256": "223a8309e5aae06a41df10e3cbc4bb6b12bf4ef5080e991ab71685964c8bc4a0", "source_record_sha256s": {"source_9f9972326eb118a8e4bb5623": "0adbdcabf38d2a0e7fb4a29a8c5a22243474ebc3697cd3076d29d0c2ca32ab2c"}, "raw_state_sha256": "aa31c55877e493edfe1a80da9185d105341292b7d71e19e8a847659dcf15f33b", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "88914158547ab8087fe262c74fedd446ce37e76effcc4dde0fcacdef86f92c28", "relation_fingerprint": {"outgoing_relations_sha256": "38a1c69db6c941f957f2551160f4317e808294d58cb94153514d9be47ba7d914", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "38a1c69db6c941f957f2551160f4317e808294d58cb94153514d9be47ba7d914"}, "relation_neighborhood_sha256": "38a1c69db6c941f957f2551160f4317e808294d58cb94153514d9be47ba7d914", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_61c0ffd089f650a51ec3f00d"
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
        "object_updated_at:2026-08-02T18:21:45+08:00",
        "source:source_9f9972326eb118a8e4bb5623 work_sha256:none"
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
        "source:source_9f9972326eb118a8e4bb5623 record_sha256:0adbdcabf38d2a0e7fb4a29a8c5a22243474ebc3697cd3076d29d0c2ca32ab2c"
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
        "source:source_9f9972326eb118a8e4bb5623 raw_sha256:b4ca82a153732c8fdae606f271f37ecceb2d091c19e221cd1d3c6e21f73311ea"
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
        "related:source_9f9972326eb118a8e4bb5623",
        "related:concept_6a559a41722de87986c350e7"
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
        "validated:vault/memory/concept/concept_61c0ffd089f650a51ec3f00d.md"
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
  "completed_at": "2026-08-02T19:54:58+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "3b30a69d6eee28d0953e5fb79ea383c6d88c2d3e9291524be1f53f11ee01afc4",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "aa31c55877e493edfe1a80da9185d105341292b7d71e19e8a847659dcf15f33b",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "38a1c69db6c941f957f2551160f4317e808294d58cb94153514d9be47ba7d914",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "38a1c69db6c941f957f2551160f4317e808294d58cb94153514d9be47ba7d914"
    },
    "relation_neighborhood_sha256": "38a1c69db6c941f957f2551160f4317e808294d58cb94153514d9be47ba7d914",
    "source_record_sha256s": {
      "source_9f9972326eb118a8e4bb5623": "0adbdcabf38d2a0e7fb4a29a8c5a22243474ebc3697cd3076d29d0c2ca32ab2c"
    },
    "source_state_sha256": "223a8309e5aae06a41df10e3cbc4bb6b12bf4ef5080e991ab71685964c8bc4a0",
    "work_identity_sha256": "88914158547ab8087fe262c74fedd446ce37e76effcc4dde0fcacdef86f92c28"
  },
  "consolidation_id": "consolidation_af93a008843b9eecd2f481c5",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-08-02T19:54:58+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_af93a008843b9eecd2f481c5",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_61c0ffd089f650a51ec3f00d",
  "object_sha256_after": "3b30a69d6eee28d0953e5fb79ea383c6d88c2d3e9291524be1f53f11ee01afc4",
  "object_sha256_before": "0a9c66a5a6a32d9615b8f4b942101f3777b43b1c1c11c466ffdfb47ea08914a9",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_9f9972326eb118a8e4bb5623"
  ],
  "source_records": [
    {
      "raw_content_sha256": "b4ca82a153732c8fdae606f271f37ecceb2d091c19e221cd1d3c6e21f73311ea",
      "source_id": "source_9f9972326eb118a8e4bb5623",
      "source_record_sha256": "0adbdcabf38d2a0e7fb4a29a8c5a22243474ebc3697cd3076d29d0c2ca32ab2c",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "b4ca82a153732c8fdae606f271f37ecceb2d091c19e221cd1d3c6e21f73311ea"
  ],
  "started_at": "2026-08-02T19:54:58+08:00",
  "status": "complete",
  "title": "Consolidation: 上下文匹配的失败动作有界重定向 / Context-matched bounded redirection of failure actions",
  "type": "consolidation_receipt",
  "updated_at": "2026-08-02T19:54:58+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
