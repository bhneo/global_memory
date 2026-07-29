---
id: "consolidation_4b2042d2af21561ce9201a77"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 多线性 restriction 与 Kakeya 中的横截性控制"
created_at: "2026-07-27T19:06:49+08:00"
updated_at: "2026-07-27T19:06:49+08:00"
consolidation_id: "consolidation_4b2042d2af21561ce9201a77"
object_id: "concept_c0e590dd716efa867bc34cbd"
object_version_before: 1
object_sha256_before: "93862e88e6b9cf20cc5a1cf5e53432bf8a983754cca983b10893d43c75dab578"
object_sha256_after: "91259a82e1c9b463ffbc1b5f0673093b5d21d3c93c05f9a1b56dd97c6488f2db"
source_ids: ["source_84c8c0edd41364ae0542b7ca"]
source_sha256s: ["5777b4572393d0bdf5ad933027232d4302a1cbf8e4253565f36f4617984ae107"]
source_records: [{"source_id": "source_84c8c0edd41364ae0542b7ca", "source_record_sha256": "7a4912edfe68702973479229ebe765f76441089c29abf2d34c495dbdcd3546bb", "raw_content_sha256": "5777b4572393d0bdf5ad933027232d4302a1cbf8e4253565f36f4617984ae107", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-27T19:06:49+08:00"
completed_at: "2026-07-27T19:06:49+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_c0e590dd716efa867bc34cbd.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_84c8c0edd41364ae0542b7ca raw_sha256:5777b4572393d0bdf5ad933027232d4302a1cbf8e4253565f36f4617984ae107"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_84c8c0edd41364ae0542b7ca record_sha256:7a4912edfe68702973479229ebe765f76441089c29abf2d34c495dbdcd3546bb"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_c0e590dd716efa867bc34cbd"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 3 related objects found", "related:source_84c8c0edd41364ae0542b7ca", "related:concept_2baeb2cc7c9fb6cc84e1614f", "related:concept_c0e590dd716efa867bc34cbd"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-27T09:54:58+08:00", "source:source_84c8c0edd41364ae0542b7ca work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "91259a82e1c9b463ffbc1b5f0673093b5d21d3c93c05f9a1b56dd97c6488f2db", "source_state_sha256": "51929f557a6f510d91281a91b0269acdc6dc7c88e0f20619dd3ce5c7866f663e", "source_record_sha256s": {"source_84c8c0edd41364ae0542b7ca": "7a4912edfe68702973479229ebe765f76441089c29abf2d34c495dbdcd3546bb"}, "raw_state_sha256": "b9a0ab2ce3b4c60751dc6cbb2da39ed4818a3ff0ea26902fc7a2145739d71914", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "d9625cdf927b2b550ab3494b50c0c16a16c18dd63e15685016214b4466db294f", "relation_fingerprint": {"outgoing_relations_sha256": "85757b89b48c613b87ccbf61ef7d76b0e7f8b5fa66c2f102c95b6fc884f3d441", "incoming_relations_sha256": "1301a0e2de5970b6b01ae28c73e695c573cde4df129543b13229ad87bde90a14", "full_neighborhood_sha256": "2fbaa5863296c460be7e860ba28a1c22f9eaf35a97cd3ec72194a5874b843805"}, "relation_neighborhood_sha256": "2fbaa5863296c460be7e860ba28a1c22f9eaf35a97cd3ec72194a5874b843805", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_c0e590dd716efa867bc34cbd"
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
        "object_updated_at:2026-07-27T09:54:58+08:00",
        "source:source_84c8c0edd41364ae0542b7ca work_sha256:none"
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
        "source:source_84c8c0edd41364ae0542b7ca record_sha256:7a4912edfe68702973479229ebe765f76441089c29abf2d34c495dbdcd3546bb"
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
        "source:source_84c8c0edd41364ae0542b7ca raw_sha256:5777b4572393d0bdf5ad933027232d4302a1cbf8e4253565f36f4617984ae107"
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
        "related:source_84c8c0edd41364ae0542b7ca",
        "related:concept_2baeb2cc7c9fb6cc84e1614f",
        "related:concept_c0e590dd716efa867bc34cbd"
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
        "validated:vault/memory/concept/concept_c0e590dd716efa867bc34cbd.md"
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
  "completed_at": "2026-07-27T19:06:49+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "91259a82e1c9b463ffbc1b5f0673093b5d21d3c93c05f9a1b56dd97c6488f2db",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "b9a0ab2ce3b4c60751dc6cbb2da39ed4818a3ff0ea26902fc7a2145739d71914",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "2fbaa5863296c460be7e860ba28a1c22f9eaf35a97cd3ec72194a5874b843805",
      "incoming_relations_sha256": "1301a0e2de5970b6b01ae28c73e695c573cde4df129543b13229ad87bde90a14",
      "outgoing_relations_sha256": "85757b89b48c613b87ccbf61ef7d76b0e7f8b5fa66c2f102c95b6fc884f3d441"
    },
    "relation_neighborhood_sha256": "2fbaa5863296c460be7e860ba28a1c22f9eaf35a97cd3ec72194a5874b843805",
    "source_record_sha256s": {
      "source_84c8c0edd41364ae0542b7ca": "7a4912edfe68702973479229ebe765f76441089c29abf2d34c495dbdcd3546bb"
    },
    "source_state_sha256": "51929f557a6f510d91281a91b0269acdc6dc7c88e0f20619dd3ce5c7866f663e",
    "work_identity_sha256": "d9625cdf927b2b550ab3494b50c0c16a16c18dd63e15685016214b4466db294f"
  },
  "consolidation_id": "consolidation_4b2042d2af21561ce9201a77",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-27T19:06:49+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_4b2042d2af21561ce9201a77",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_c0e590dd716efa867bc34cbd",
  "object_sha256_after": "91259a82e1c9b463ffbc1b5f0673093b5d21d3c93c05f9a1b56dd97c6488f2db",
  "object_sha256_before": "93862e88e6b9cf20cc5a1cf5e53432bf8a983754cca983b10893d43c75dab578",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_84c8c0edd41364ae0542b7ca"
  ],
  "source_records": [
    {
      "raw_content_sha256": "5777b4572393d0bdf5ad933027232d4302a1cbf8e4253565f36f4617984ae107",
      "source_id": "source_84c8c0edd41364ae0542b7ca",
      "source_record_sha256": "7a4912edfe68702973479229ebe765f76441089c29abf2d34c495dbdcd3546bb",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "5777b4572393d0bdf5ad933027232d4302a1cbf8e4253565f36f4617984ae107"
  ],
  "started_at": "2026-07-27T19:06:49+08:00",
  "status": "complete",
  "title": "Consolidation: 多线性 restriction 与 Kakeya 中的横截性控制",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-27T19:06:49+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
