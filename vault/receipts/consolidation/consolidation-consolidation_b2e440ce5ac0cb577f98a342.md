---
id: "consolidation_b2e440ce5ac0cb577f98a342"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: Cursor M7 真实读取与 receipt 回写验收"
created_at: "2026-07-18T16:03:18+08:00"
updated_at: "2026-07-18T16:03:18+08:00"
consolidation_id: "consolidation_b2e440ce5ac0cb577f98a342"
object_id: "experiment_7101e03fb065226e65f388a5"
object_version_before: 1
object_sha256_before: "bdcc51efeee93e82754424f4f76d9cb27cd85912d777dab3e1c40bae9d32eb0b"
object_sha256_after: "33eb7e3bbb9a97f54496ad8bae6258b46dad323663cb9110f324a6ce5ccb3fc6"
source_ids: ["source_113d589e6dadf14b5fa8edea"]
source_sha256s: ["394593d72af8067a8b05675fa643d682f03c6ea11956027ce8c0492f91201ace"]
source_records: [{"source_id": "source_113d589e6dadf14b5fa8edea", "source_record_sha256": "a8d60f5e31e8887c7597dd303fc8a9903245d0b7db96249c307f65aff120067c", "raw_content_sha256": "394593d72af8067a8b05675fa643d682f03c6ea11956027ce8c0492f91201ace", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-18T16:03:18+08:00"
completed_at: "2026-07-18T16:03:18+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/experiment/experiment_7101e03fb065226e65f388a5.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_113d589e6dadf14b5fa8edea raw_sha256:394593d72af8067a8b05675fa643d682f03c6ea11956027ce8c0492f91201ace"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_113d589e6dadf14b5fa8edea record_sha256:a8d60f5e31e8887c7597dd303fc8a9903245d0b7db96249c307f65aff120067c"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 2 candidates inspected", "candidate:experiment_7101e03fb065226e65f388a5", "candidate:experiment_b6f1e1956690ac08fd56a5da"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_113d589e6dadf14b5fa8edea"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T18:36:01+08:00", "source:source_113d589e6dadf14b5fa8edea work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "33eb7e3bbb9a97f54496ad8bae6258b46dad323663cb9110f324a6ce5ccb3fc6", "source_state_sha256": "3acb638976c918dd75df4d74a2e875ac393b81e8012425c09f795d393a583590", "source_record_sha256s": {"source_113d589e6dadf14b5fa8edea": "a8d60f5e31e8887c7597dd303fc8a9903245d0b7db96249c307f65aff120067c"}, "raw_state_sha256": "c924a8e103d198e8ee429dc5e83ffd1f537bf0ee4a672c81ee1a5fd083d15cb2", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "7512cd3c657c2442a8ed812b5df9c440a67e372771b1dfc42c5f1509f4143b11", "relation_fingerprint": {"outgoing_relations_sha256": "be18a416cc8b912c363c40c66086295637b5fe17ba5abb74311ace2b17507dbe", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "be18a416cc8b912c363c40c66086295637b5fe17ba5abb74311ace2b17507dbe"}, "relation_neighborhood_sha256": "be18a416cc8b912c363c40c66086295637b5fe17ba5abb74311ace2b17507dbe", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "searched title; 2 candidates inspected",
        "candidate:experiment_7101e03fb065226e65f388a5",
        "candidate:experiment_b6f1e1956690ac08fd56a5da"
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
        "object_updated_at:2026-07-17T18:36:01+08:00",
        "source:source_113d589e6dadf14b5fa8edea work_sha256:none"
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
        "source:source_113d589e6dadf14b5fa8edea record_sha256:a8d60f5e31e8887c7597dd303fc8a9903245d0b7db96249c307f65aff120067c"
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
        "source:source_113d589e6dadf14b5fa8edea raw_sha256:394593d72af8067a8b05675fa643d682f03c6ea11956027ce8c0492f91201ace"
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
        "related:source_113d589e6dadf14b5fa8edea"
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
        "validated:vault/memory/experiment/experiment_7101e03fb065226e65f388a5.md"
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
  "completed_at": "2026-07-18T16:03:18+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "33eb7e3bbb9a97f54496ad8bae6258b46dad323663cb9110f324a6ce5ccb3fc6",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "c924a8e103d198e8ee429dc5e83ffd1f537bf0ee4a672c81ee1a5fd083d15cb2",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "be18a416cc8b912c363c40c66086295637b5fe17ba5abb74311ace2b17507dbe",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "be18a416cc8b912c363c40c66086295637b5fe17ba5abb74311ace2b17507dbe"
    },
    "relation_neighborhood_sha256": "be18a416cc8b912c363c40c66086295637b5fe17ba5abb74311ace2b17507dbe",
    "source_record_sha256s": {
      "source_113d589e6dadf14b5fa8edea": "a8d60f5e31e8887c7597dd303fc8a9903245d0b7db96249c307f65aff120067c"
    },
    "source_state_sha256": "3acb638976c918dd75df4d74a2e875ac393b81e8012425c09f795d393a583590",
    "work_identity_sha256": "7512cd3c657c2442a8ed812b5df9c440a67e372771b1dfc42c5f1509f4143b11"
  },
  "consolidation_id": "consolidation_b2e440ce5ac0cb577f98a342",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-18T16:03:18+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_b2e440ce5ac0cb577f98a342",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "experiment_7101e03fb065226e65f388a5",
  "object_sha256_after": "33eb7e3bbb9a97f54496ad8bae6258b46dad323663cb9110f324a6ce5ccb3fc6",
  "object_sha256_before": "bdcc51efeee93e82754424f4f76d9cb27cd85912d777dab3e1c40bae9d32eb0b",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_113d589e6dadf14b5fa8edea"
  ],
  "source_records": [
    {
      "raw_content_sha256": "394593d72af8067a8b05675fa643d682f03c6ea11956027ce8c0492f91201ace",
      "source_id": "source_113d589e6dadf14b5fa8edea",
      "source_record_sha256": "a8d60f5e31e8887c7597dd303fc8a9903245d0b7db96249c307f65aff120067c",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "394593d72af8067a8b05675fa643d682f03c6ea11956027ce8c0492f91201ace"
  ],
  "started_at": "2026-07-18T16:03:18+08:00",
  "status": "complete",
  "title": "Consolidation: Cursor M7 真实读取与 receipt 回写验收",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-18T16:03:18+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
