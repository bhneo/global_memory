---
id: "consolidation_f7ddddd96ffb0a36b40ef34f"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: the policy is initialized from the same ACT model"
created_at: "2026-07-19T01:47:03+08:00"
updated_at: "2026-07-19T01:47:03+08:00"
consolidation_id: "consolidation_f7ddddd96ffb0a36b40ef34f"
object_id: "experiment_305648b9377f92e9f4ef9a5f"
object_version_before: 1
object_sha256_before: "3569622c77695ffd151170192d15411eb51c81ea0987a2281e7519d3330aadd5"
object_sha256_after: "c54f2fb988173e8a398f5fd1db204bdd7f6f2f5a0724a0812a2cf8a921d3794d"
source_ids: ["source_c79f943c818d06054ca5cf92"]
source_sha256s: ["17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb"]
source_records: [{"source_id": "source_c79f943c818d06054ca5cf92", "source_record_sha256": "986d4ba674af6cd7d3f115e76d98503b7e54f7701c55a2494d550f31f1158adc", "raw_content_sha256": "17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-19T01:47:03+08:00"
completed_at: "2026-07-19T01:47:03+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/experiment/experiment_305648b9377f92e9f4ef9a5f.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_c79f943c818d06054ca5cf92 raw_sha256:17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_c79f943c818d06054ca5cf92 record_sha256:986d4ba674af6cd7d3f115e76d98503b7e54f7701c55a2494d550f31f1158adc"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:experiment_305648b9377f92e9f4ef9a5f"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_c79f943c818d06054ca5cf92"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T01:40:12+08:00", "source:source_c79f943c818d06054ca5cf92 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "c54f2fb988173e8a398f5fd1db204bdd7f6f2f5a0724a0812a2cf8a921d3794d", "source_state_sha256": "e25333c2e5da47f2727b029e5615bf0e1cd37dbec82f10e05460d1309886e15f", "source_record_sha256s": {"source_c79f943c818d06054ca5cf92": "986d4ba674af6cd7d3f115e76d98503b7e54f7701c55a2494d550f31f1158adc"}, "raw_state_sha256": "ee5d75dabb00dc903ea280412900dc43c7e99094849133cbd8c596340569b119", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "c0a678a8157a26af88488226bf145e84a32da51a3710b7a22094040b29f37cea", "relation_fingerprint": {"outgoing_relations_sha256": "a42c7e86b0341aefaa3aa06a67efcb1117ce7d9b9b76b52725cbffa3c20505f2", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "a42c7e86b0341aefaa3aa06a67efcb1117ce7d9b9b76b52725cbffa3c20505f2"}, "relation_neighborhood_sha256": "a42c7e86b0341aefaa3aa06a67efcb1117ce7d9b9b76b52725cbffa3c20505f2", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:experiment_305648b9377f92e9f4ef9a5f"
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
        "object_updated_at:2026-07-19T01:40:12+08:00",
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
        "relation index inspected; 1 related objects found",
        "related:source_c79f943c818d06054ca5cf92"
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
        "validated:vault/memory/experiment/experiment_305648b9377f92e9f4ef9a5f.md"
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
  "completed_at": "2026-07-19T01:47:03+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "c54f2fb988173e8a398f5fd1db204bdd7f6f2f5a0724a0812a2cf8a921d3794d",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "ee5d75dabb00dc903ea280412900dc43c7e99094849133cbd8c596340569b119",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "a42c7e86b0341aefaa3aa06a67efcb1117ce7d9b9b76b52725cbffa3c20505f2",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "a42c7e86b0341aefaa3aa06a67efcb1117ce7d9b9b76b52725cbffa3c20505f2"
    },
    "relation_neighborhood_sha256": "a42c7e86b0341aefaa3aa06a67efcb1117ce7d9b9b76b52725cbffa3c20505f2",
    "source_record_sha256s": {
      "source_c79f943c818d06054ca5cf92": "986d4ba674af6cd7d3f115e76d98503b7e54f7701c55a2494d550f31f1158adc"
    },
    "source_state_sha256": "e25333c2e5da47f2727b029e5615bf0e1cd37dbec82f10e05460d1309886e15f",
    "work_identity_sha256": "c0a678a8157a26af88488226bf145e84a32da51a3710b7a22094040b29f37cea"
  },
  "consolidation_id": "consolidation_f7ddddd96ffb0a36b40ef34f",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T01:47:03+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_f7ddddd96ffb0a36b40ef34f",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "experiment_305648b9377f92e9f4ef9a5f",
  "object_sha256_after": "c54f2fb988173e8a398f5fd1db204bdd7f6f2f5a0724a0812a2cf8a921d3794d",
  "object_sha256_before": "3569622c77695ffd151170192d15411eb51c81ea0987a2281e7519d3330aadd5",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_c79f943c818d06054ca5cf92"
  ],
  "source_records": [
    {
      "raw_content_sha256": "17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb",
      "source_id": "source_c79f943c818d06054ca5cf92",
      "source_record_sha256": "986d4ba674af6cd7d3f115e76d98503b7e54f7701c55a2494d550f31f1158adc",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "17d5408321d42ec512a8edb226b86ea72f40e42768d44db55335137ca6dcfdfb"
  ],
  "started_at": "2026-07-19T01:47:03+08:00",
  "status": "complete",
  "title": "Consolidation: the policy is initialized from the same ACT model",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T01:47:03+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
