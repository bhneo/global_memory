---
id: "consolidation_a40bad0b9df74250a25c9be3"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 异构具身数据的分阶段对齐"
created_at: "2026-07-19T03:06:08+08:00"
updated_at: "2026-07-19T03:06:08+08:00"
consolidation_id: "consolidation_a40bad0b9df74250a25c9be3"
object_id: "concept_staged_cross_embodiment_alignment"
object_version_before: 1
object_sha256_before: "6a5316694622b753b03980f9fcfd8b591ea6a8f5805f09a2ff0817e1ead92458"
object_sha256_after: "1ca75f5b9366cc9ec292b1fb484a3c73769875e97457bc087924ff4f704d7564"
source_ids: ["source_691f3acc1fe3382639690f59"]
source_sha256s: ["445b6356f2ef5224951315cd2f3d3707b07fb225423f7f5d14f5673eaa1049fb"]
source_records: [{"source_id": "source_691f3acc1fe3382639690f59", "source_record_sha256": "6245ecacf1f4a94aff9ee571056f3d7a18926b9f40e47a2ee4a801d72a577f4f", "raw_content_sha256": "445b6356f2ef5224951315cd2f3d3707b07fb225423f7f5d14f5673eaa1049fb", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-19T03:06:08+08:00"
completed_at: "2026-07-19T03:06:08+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_staged_cross_embodiment_alignment.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_691f3acc1fe3382639690f59 raw_sha256:445b6356f2ef5224951315cd2f3d3707b07fb225423f7f5d14f5673eaa1049fb"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_691f3acc1fe3382639690f59 record_sha256:6245ecacf1f4a94aff9ee571056f3d7a18926b9f40e47a2ee4a801d72a577f4f"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_staged_cross_embodiment_alignment"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 4 related objects found", "related:source_691f3acc1fe3382639690f59", "related:concept_embodied_data_loop", "related:concept_staged_cross_embodiment_alignment", "related:concept_staged_cross_embodiment_alignment"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T02:51:01+08:00", "source:source_691f3acc1fe3382639690f59 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "1ca75f5b9366cc9ec292b1fb484a3c73769875e97457bc087924ff4f704d7564", "source_state_sha256": "6ed5431b669d6027e7493aece3bb89c32b7dea24085be52e95636ec1771d5f54", "source_record_sha256s": {"source_691f3acc1fe3382639690f59": "6245ecacf1f4a94aff9ee571056f3d7a18926b9f40e47a2ee4a801d72a577f4f"}, "raw_state_sha256": "f00337de8284804369d3149668c0af210123da800be843ed927647f617c1b952", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "f74c033c2ba7896b56c5eaffc3555201bdd4f68b379468a93b3335b3e31e2856", "relation_fingerprint": {"outgoing_relations_sha256": "c34be11bf7e53b56ccc1221be13f5c0e3617dca13259031956141c79e367ea5b", "incoming_relations_sha256": "f592cbbd2355a0ef5b731658b6194c0d302d5039d873cf3312d18ccc75d386be", "full_neighborhood_sha256": "73136846d9fae1030f47db1783c22602372fc681d9ec80ef4b67509d42f79813"}, "relation_neighborhood_sha256": "73136846d9fae1030f47db1783c22602372fc681d9ec80ef4b67509d42f79813", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_staged_cross_embodiment_alignment"
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
        "object_updated_at:2026-07-19T02:51:01+08:00",
        "source:source_691f3acc1fe3382639690f59 work_sha256:none"
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
        "source:source_691f3acc1fe3382639690f59 record_sha256:6245ecacf1f4a94aff9ee571056f3d7a18926b9f40e47a2ee4a801d72a577f4f"
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
        "source:source_691f3acc1fe3382639690f59 raw_sha256:445b6356f2ef5224951315cd2f3d3707b07fb225423f7f5d14f5673eaa1049fb"
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
        "relation index inspected; 4 related objects found",
        "related:source_691f3acc1fe3382639690f59",
        "related:concept_embodied_data_loop",
        "related:concept_staged_cross_embodiment_alignment",
        "related:concept_staged_cross_embodiment_alignment"
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
        "validated:vault/memory/concept/concept_staged_cross_embodiment_alignment.md"
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
  "completed_at": "2026-07-19T03:06:08+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "1ca75f5b9366cc9ec292b1fb484a3c73769875e97457bc087924ff4f704d7564",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "f00337de8284804369d3149668c0af210123da800be843ed927647f617c1b952",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "73136846d9fae1030f47db1783c22602372fc681d9ec80ef4b67509d42f79813",
      "incoming_relations_sha256": "f592cbbd2355a0ef5b731658b6194c0d302d5039d873cf3312d18ccc75d386be",
      "outgoing_relations_sha256": "c34be11bf7e53b56ccc1221be13f5c0e3617dca13259031956141c79e367ea5b"
    },
    "relation_neighborhood_sha256": "73136846d9fae1030f47db1783c22602372fc681d9ec80ef4b67509d42f79813",
    "source_record_sha256s": {
      "source_691f3acc1fe3382639690f59": "6245ecacf1f4a94aff9ee571056f3d7a18926b9f40e47a2ee4a801d72a577f4f"
    },
    "source_state_sha256": "6ed5431b669d6027e7493aece3bb89c32b7dea24085be52e95636ec1771d5f54",
    "work_identity_sha256": "f74c033c2ba7896b56c5eaffc3555201bdd4f68b379468a93b3335b3e31e2856"
  },
  "consolidation_id": "consolidation_a40bad0b9df74250a25c9be3",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T03:06:08+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_a40bad0b9df74250a25c9be3",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_staged_cross_embodiment_alignment",
  "object_sha256_after": "1ca75f5b9366cc9ec292b1fb484a3c73769875e97457bc087924ff4f704d7564",
  "object_sha256_before": "6a5316694622b753b03980f9fcfd8b591ea6a8f5805f09a2ff0817e1ead92458",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_691f3acc1fe3382639690f59"
  ],
  "source_records": [
    {
      "raw_content_sha256": "445b6356f2ef5224951315cd2f3d3707b07fb225423f7f5d14f5673eaa1049fb",
      "source_id": "source_691f3acc1fe3382639690f59",
      "source_record_sha256": "6245ecacf1f4a94aff9ee571056f3d7a18926b9f40e47a2ee4a801d72a577f4f",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "445b6356f2ef5224951315cd2f3d3707b07fb225423f7f5d14f5673eaa1049fb"
  ],
  "started_at": "2026-07-19T03:06:08+08:00",
  "status": "complete",
  "title": "Consolidation: 异构具身数据的分阶段对齐",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T03:06:08+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
