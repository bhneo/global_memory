---
id: "consolidation_b8640e036010ed17330d53e8"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 全身冗余的部分运动学嵌入"
created_at: "2026-07-20T13:37:44+08:00"
updated_at: "2026-07-20T13:37:44+08:00"
consolidation_id: "consolidation_b8640e036010ed17330d53e8"
object_id: "concept_fc70bfc09ac7d9473592f09c"
object_version_before: 1
object_sha256_before: "342e7edb8d1762a9ca23c40a717fd482490707cdaa818ac3e2fb5ed90d84de61"
object_sha256_after: "42fe8954775e73ba976b1c6205d1cf6c3e1934a5b5e91f97b805d6dbc3b1f6be"
source_ids: ["source_951559714c0383331b1b30ac"]
source_sha256s: ["5f3262a8de3930186c5a13936da869ece75ab770c3d08abcd36f9e0f77a721bf"]
source_records: [{"source_id": "source_951559714c0383331b1b30ac", "source_record_sha256": "26df6c0053fced942aa611bd090f38425602cdf04ef01c8cd5e92b4d9faa6521", "raw_content_sha256": "5f3262a8de3930186c5a13936da869ece75ab770c3d08abcd36f9e0f77a721bf", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-20T13:37:44+08:00"
completed_at: "2026-07-20T13:37:44+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_fc70bfc09ac7d9473592f09c.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_951559714c0383331b1b30ac raw_sha256:5f3262a8de3930186c5a13936da869ece75ab770c3d08abcd36f9e0f77a721bf"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_951559714c0383331b1b30ac record_sha256:26df6c0053fced942aa611bd090f38425602cdf04ef01c8cd5e92b4d9faa6521"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_fc70bfc09ac7d9473592f09c"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_951559714c0383331b1b30ac", "related:concept_fc70bfc09ac7d9473592f09c"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-20T12:39:41+08:00", "source:source_951559714c0383331b1b30ac work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "42fe8954775e73ba976b1c6205d1cf6c3e1934a5b5e91f97b805d6dbc3b1f6be", "source_state_sha256": "da4fabad7242e1e00bb07f828f218987662d9cf79b55b6b1719c531acc983370", "source_record_sha256s": {"source_951559714c0383331b1b30ac": "26df6c0053fced942aa611bd090f38425602cdf04ef01c8cd5e92b4d9faa6521"}, "raw_state_sha256": "acb7731168edb0c12d39e86496a1e8d6fedd5d22b264b7bf5bba2b8de27c10a7", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "104f76067c57a0a7a2a68bd6fbdea1c106b417c40b3872e8a0aae46ebe529ff5", "relation_fingerprint": {"outgoing_relations_sha256": "02bdee715a5410f988117ac1918ff8abe8a7716e834af86ee311999852715543", "incoming_relations_sha256": "819af852d565acfbbc3c8c291a9275d48015d5597134ba141bd6072a880efd41", "full_neighborhood_sha256": "5eb3937d7e23e511d64b2a9daf5354bab357e110688be251d1d71bafc697181b"}, "relation_neighborhood_sha256": "5eb3937d7e23e511d64b2a9daf5354bab357e110688be251d1d71bafc697181b", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_fc70bfc09ac7d9473592f09c"
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
        "object_updated_at:2026-07-20T12:39:41+08:00",
        "source:source_951559714c0383331b1b30ac work_sha256:none"
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
        "source:source_951559714c0383331b1b30ac record_sha256:26df6c0053fced942aa611bd090f38425602cdf04ef01c8cd5e92b4d9faa6521"
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
        "source:source_951559714c0383331b1b30ac raw_sha256:5f3262a8de3930186c5a13936da869ece75ab770c3d08abcd36f9e0f77a721bf"
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
        "related:source_951559714c0383331b1b30ac",
        "related:concept_fc70bfc09ac7d9473592f09c"
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
        "validated:vault/memory/concept/concept_fc70bfc09ac7d9473592f09c.md"
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
  "completed_at": "2026-07-20T13:37:44+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "42fe8954775e73ba976b1c6205d1cf6c3e1934a5b5e91f97b805d6dbc3b1f6be",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "acb7731168edb0c12d39e86496a1e8d6fedd5d22b264b7bf5bba2b8de27c10a7",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "5eb3937d7e23e511d64b2a9daf5354bab357e110688be251d1d71bafc697181b",
      "incoming_relations_sha256": "819af852d565acfbbc3c8c291a9275d48015d5597134ba141bd6072a880efd41",
      "outgoing_relations_sha256": "02bdee715a5410f988117ac1918ff8abe8a7716e834af86ee311999852715543"
    },
    "relation_neighborhood_sha256": "5eb3937d7e23e511d64b2a9daf5354bab357e110688be251d1d71bafc697181b",
    "source_record_sha256s": {
      "source_951559714c0383331b1b30ac": "26df6c0053fced942aa611bd090f38425602cdf04ef01c8cd5e92b4d9faa6521"
    },
    "source_state_sha256": "da4fabad7242e1e00bb07f828f218987662d9cf79b55b6b1719c531acc983370",
    "work_identity_sha256": "104f76067c57a0a7a2a68bd6fbdea1c106b417c40b3872e8a0aae46ebe529ff5"
  },
  "consolidation_id": "consolidation_b8640e036010ed17330d53e8",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-20T13:37:44+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_b8640e036010ed17330d53e8",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_fc70bfc09ac7d9473592f09c",
  "object_sha256_after": "42fe8954775e73ba976b1c6205d1cf6c3e1934a5b5e91f97b805d6dbc3b1f6be",
  "object_sha256_before": "342e7edb8d1762a9ca23c40a717fd482490707cdaa818ac3e2fb5ed90d84de61",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_951559714c0383331b1b30ac"
  ],
  "source_records": [
    {
      "raw_content_sha256": "5f3262a8de3930186c5a13936da869ece75ab770c3d08abcd36f9e0f77a721bf",
      "source_id": "source_951559714c0383331b1b30ac",
      "source_record_sha256": "26df6c0053fced942aa611bd090f38425602cdf04ef01c8cd5e92b4d9faa6521",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "5f3262a8de3930186c5a13936da869ece75ab770c3d08abcd36f9e0f77a721bf"
  ],
  "started_at": "2026-07-20T13:37:44+08:00",
  "status": "complete",
  "title": "Consolidation: 全身冗余的部分运动学嵌入",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-20T13:37:44+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
