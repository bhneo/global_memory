---
id: "consolidation_09e496a05140ffc289e0493f"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: VLA 的强化学习读出接口"
created_at: "2026-07-20T13:37:43+08:00"
updated_at: "2026-07-20T13:37:43+08:00"
consolidation_id: "consolidation_09e496a05140ffc289e0493f"
object_id: "concept_f9a9f1d1818632c0380b7942"
object_version_before: 1
object_sha256_before: "a7fe6c74cda182df7a3bb294d76004a930f214c9b46092b2b3b7c64a3fd05dfa"
object_sha256_after: "c2e6a2071aa69c57d46de187e4347c31830b1acfacdfd679d09c5ca11d095f95"
source_ids: ["source_40700e61702f4b5a5765e11d"]
source_sha256s: ["a64c94a365332756ee45c5762a630bae9bfa13fdba80bd626744883032ac4c8b"]
source_records: [{"source_id": "source_40700e61702f4b5a5765e11d", "source_record_sha256": "67cc8a512f4ba2af69ba83cc27215a0e87ffdc84dc12ef4ae43ea61e8bf634b9", "raw_content_sha256": "a64c94a365332756ee45c5762a630bae9bfa13fdba80bd626744883032ac4c8b", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-20T13:37:43+08:00"
completed_at: "2026-07-20T13:37:43+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_f9a9f1d1818632c0380b7942.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_40700e61702f4b5a5765e11d raw_sha256:a64c94a365332756ee45c5762a630bae9bfa13fdba80bd626744883032ac4c8b"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_40700e61702f4b5a5765e11d record_sha256:67cc8a512f4ba2af69ba83cc27215a0e87ffdc84dc12ef4ae43ea61e8bf634b9"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 2 candidates inspected", "candidate:concept_f9a9f1d1818632c0380b7942", "candidate:reflection_305130038ee9fd3cb9e18ec4"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_40700e61702f4b5a5765e11d", "related:concept_f9a9f1d1818632c0380b7942"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-20T11:57:07+08:00", "source:source_40700e61702f4b5a5765e11d work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "c2e6a2071aa69c57d46de187e4347c31830b1acfacdfd679d09c5ca11d095f95", "source_state_sha256": "dad0c826ba020e5eebc0a5b66696aec9fc90fa8d3327957856bb572bfe40f663", "source_record_sha256s": {"source_40700e61702f4b5a5765e11d": "67cc8a512f4ba2af69ba83cc27215a0e87ffdc84dc12ef4ae43ea61e8bf634b9"}, "raw_state_sha256": "0240b75e83e7d7ab397b71d560e7aba79584a35e2e156b73a7505ec4f19af4db", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "9b9dd9f0852276b9679d0d71220fffd951d3dc7327c982850a41ea7af4d69026", "relation_fingerprint": {"outgoing_relations_sha256": "55c7a2451213deea3c36b635187f624d8b6621e85923cfc19372af3c542f32e8", "incoming_relations_sha256": "fc1714b63a7a7702111d28c97dd97f5cc3d9bb616cf0b48565746f1bf7d03afc", "full_neighborhood_sha256": "069ad3486c606879a1a40f5f7e0e0a9e5c4650d0f3a3ec8852e228cf9953bc28"}, "relation_neighborhood_sha256": "069ad3486c606879a1a40f5f7e0e0a9e5c4650d0f3a3ec8852e228cf9953bc28", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_f9a9f1d1818632c0380b7942",
        "candidate:reflection_305130038ee9fd3cb9e18ec4"
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
        "object_updated_at:2026-07-20T11:57:07+08:00",
        "source:source_40700e61702f4b5a5765e11d work_sha256:none"
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
        "source:source_40700e61702f4b5a5765e11d record_sha256:67cc8a512f4ba2af69ba83cc27215a0e87ffdc84dc12ef4ae43ea61e8bf634b9"
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
        "source:source_40700e61702f4b5a5765e11d raw_sha256:a64c94a365332756ee45c5762a630bae9bfa13fdba80bd626744883032ac4c8b"
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
        "related:source_40700e61702f4b5a5765e11d",
        "related:concept_f9a9f1d1818632c0380b7942"
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
        "validated:vault/memory/concept/concept_f9a9f1d1818632c0380b7942.md"
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
  "completed_at": "2026-07-20T13:37:43+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "c2e6a2071aa69c57d46de187e4347c31830b1acfacdfd679d09c5ca11d095f95",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "0240b75e83e7d7ab397b71d560e7aba79584a35e2e156b73a7505ec4f19af4db",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "069ad3486c606879a1a40f5f7e0e0a9e5c4650d0f3a3ec8852e228cf9953bc28",
      "incoming_relations_sha256": "fc1714b63a7a7702111d28c97dd97f5cc3d9bb616cf0b48565746f1bf7d03afc",
      "outgoing_relations_sha256": "55c7a2451213deea3c36b635187f624d8b6621e85923cfc19372af3c542f32e8"
    },
    "relation_neighborhood_sha256": "069ad3486c606879a1a40f5f7e0e0a9e5c4650d0f3a3ec8852e228cf9953bc28",
    "source_record_sha256s": {
      "source_40700e61702f4b5a5765e11d": "67cc8a512f4ba2af69ba83cc27215a0e87ffdc84dc12ef4ae43ea61e8bf634b9"
    },
    "source_state_sha256": "dad0c826ba020e5eebc0a5b66696aec9fc90fa8d3327957856bb572bfe40f663",
    "work_identity_sha256": "9b9dd9f0852276b9679d0d71220fffd951d3dc7327c982850a41ea7af4d69026"
  },
  "consolidation_id": "consolidation_09e496a05140ffc289e0493f",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-20T13:37:43+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_09e496a05140ffc289e0493f",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_f9a9f1d1818632c0380b7942",
  "object_sha256_after": "c2e6a2071aa69c57d46de187e4347c31830b1acfacdfd679d09c5ca11d095f95",
  "object_sha256_before": "a7fe6c74cda182df7a3bb294d76004a930f214c9b46092b2b3b7c64a3fd05dfa",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_40700e61702f4b5a5765e11d"
  ],
  "source_records": [
    {
      "raw_content_sha256": "a64c94a365332756ee45c5762a630bae9bfa13fdba80bd626744883032ac4c8b",
      "source_id": "source_40700e61702f4b5a5765e11d",
      "source_record_sha256": "67cc8a512f4ba2af69ba83cc27215a0e87ffdc84dc12ef4ae43ea61e8bf634b9",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "a64c94a365332756ee45c5762a630bae9bfa13fdba80bd626744883032ac4c8b"
  ],
  "started_at": "2026-07-20T13:37:43+08:00",
  "status": "complete",
  "title": "Consolidation: VLA 的强化学习读出接口",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-20T13:37:43+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
