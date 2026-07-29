---
id: "consolidation_4f6077319a591cce126f80a5"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 单次前向动作条件世界模型的 rollout 吞吐量接口"
created_at: "2026-07-26T12:33:26+08:00"
updated_at: "2026-07-26T12:33:26+08:00"
consolidation_id: "consolidation_4f6077319a591cce126f80a5"
object_id: "concept_1bc84fc99981d367b712d161"
object_version_before: 1
object_sha256_before: "33309496f8a5405b2cfbe36d8ff2bffc272a315870f3235ca16942fda7965e35"
object_sha256_after: "98ea9ac83966a97993df41c2f522a9929158a31859203afc49eb9b8ff46d8f71"
source_ids: ["source_ce00fba8d7127c890fdcc46e"]
source_sha256s: ["37192629768a504aa3aeae95344073e4bf2bafa3323c6117c00a681cf2dcae63"]
source_records: [{"source_id": "source_ce00fba8d7127c890fdcc46e", "source_record_sha256": "dfa0d21dc6f955f024229722667329149086704fbe305ca7faa745e689b0b7cb", "raw_content_sha256": "37192629768a504aa3aeae95344073e4bf2bafa3323c6117c00a681cf2dcae63", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:26+08:00"
completed_at: "2026-07-26T12:33:26+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_1bc84fc99981d367b712d161.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_ce00fba8d7127c890fdcc46e raw_sha256:37192629768a504aa3aeae95344073e4bf2bafa3323c6117c00a681cf2dcae63"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_ce00fba8d7127c890fdcc46e record_sha256:dfa0d21dc6f955f024229722667329149086704fbe305ca7faa745e689b0b7cb"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_1bc84fc99981d367b712d161"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_ce00fba8d7127c890fdcc46e", "related:concept_dual_system_world_action_model"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-24T18:06:01+08:00", "source:source_ce00fba8d7127c890fdcc46e work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "98ea9ac83966a97993df41c2f522a9929158a31859203afc49eb9b8ff46d8f71", "source_state_sha256": "747cfd00b59d7818d5200780329395df5d1374fcc7faf0877b0cb7f7432c65ae", "source_record_sha256s": {"source_ce00fba8d7127c890fdcc46e": "dfa0d21dc6f955f024229722667329149086704fbe305ca7faa745e689b0b7cb"}, "raw_state_sha256": "4a8373052a1605665d7f12229e165b59a1ef7f7ccba37a9bce027dee5a31459e", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "1ddfd94c9693823d9cbdab7fe12d40db8e3c50fd10f9daf4013d279950b025a8", "relation_fingerprint": {"outgoing_relations_sha256": "761fc215a28f091202a3e5ce8a82faf168d0bbe25af58b96e8f67bf3d7bc992c", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "761fc215a28f091202a3e5ce8a82faf168d0bbe25af58b96e8f67bf3d7bc992c"}, "relation_neighborhood_sha256": "761fc215a28f091202a3e5ce8a82faf168d0bbe25af58b96e8f67bf3d7bc992c", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_1bc84fc99981d367b712d161"
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
        "object_updated_at:2026-07-24T18:06:01+08:00",
        "source:source_ce00fba8d7127c890fdcc46e work_sha256:none"
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
        "source:source_ce00fba8d7127c890fdcc46e record_sha256:dfa0d21dc6f955f024229722667329149086704fbe305ca7faa745e689b0b7cb"
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
        "source:source_ce00fba8d7127c890fdcc46e raw_sha256:37192629768a504aa3aeae95344073e4bf2bafa3323c6117c00a681cf2dcae63"
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
        "related:source_ce00fba8d7127c890fdcc46e",
        "related:concept_dual_system_world_action_model"
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
        "validated:vault/memory/concept/concept_1bc84fc99981d367b712d161.md"
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
  "completed_at": "2026-07-26T12:33:26+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "98ea9ac83966a97993df41c2f522a9929158a31859203afc49eb9b8ff46d8f71",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "4a8373052a1605665d7f12229e165b59a1ef7f7ccba37a9bce027dee5a31459e",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "761fc215a28f091202a3e5ce8a82faf168d0bbe25af58b96e8f67bf3d7bc992c",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "761fc215a28f091202a3e5ce8a82faf168d0bbe25af58b96e8f67bf3d7bc992c"
    },
    "relation_neighborhood_sha256": "761fc215a28f091202a3e5ce8a82faf168d0bbe25af58b96e8f67bf3d7bc992c",
    "source_record_sha256s": {
      "source_ce00fba8d7127c890fdcc46e": "dfa0d21dc6f955f024229722667329149086704fbe305ca7faa745e689b0b7cb"
    },
    "source_state_sha256": "747cfd00b59d7818d5200780329395df5d1374fcc7faf0877b0cb7f7432c65ae",
    "work_identity_sha256": "1ddfd94c9693823d9cbdab7fe12d40db8e3c50fd10f9daf4013d279950b025a8"
  },
  "consolidation_id": "consolidation_4f6077319a591cce126f80a5",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:26+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_4f6077319a591cce126f80a5",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_1bc84fc99981d367b712d161",
  "object_sha256_after": "98ea9ac83966a97993df41c2f522a9929158a31859203afc49eb9b8ff46d8f71",
  "object_sha256_before": "33309496f8a5405b2cfbe36d8ff2bffc272a315870f3235ca16942fda7965e35",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_ce00fba8d7127c890fdcc46e"
  ],
  "source_records": [
    {
      "raw_content_sha256": "37192629768a504aa3aeae95344073e4bf2bafa3323c6117c00a681cf2dcae63",
      "source_id": "source_ce00fba8d7127c890fdcc46e",
      "source_record_sha256": "dfa0d21dc6f955f024229722667329149086704fbe305ca7faa745e689b0b7cb",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "37192629768a504aa3aeae95344073e4bf2bafa3323c6117c00a681cf2dcae63"
  ],
  "started_at": "2026-07-26T12:33:26+08:00",
  "status": "complete",
  "title": "Consolidation: 单次前向动作条件世界模型的 rollout 吞吐量接口",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:26+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
