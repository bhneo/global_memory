---
id: "consolidation_2fd19d87e433d955dc98986a"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: the policy attends to memory through its existing token-processing pipeline."
created_at: "2026-07-19T01:46:40+08:00"
updated_at: "2026-07-19T01:46:40+08:00"
consolidation_id: "consolidation_2fd19d87e433d955dc98986a"
object_id: "architecture_929a68a1fd830b00f780f138"
object_version_before: 1
object_sha256_before: "4b52040d97154dba2b8c430408d094bd06beabe32bae81e4034de924377740e6"
object_sha256_after: "af6a08624d4b82ed4a4b873d9fb492c504b768c5c095c0a1b4a738939d9f06df"
source_ids: ["source_748cef2215ddc958568e6368"]
source_sha256s: ["ea6151a38b853ec9c204bc3c600b6c9e14e1bed2a36954299297cb470a5ba86c"]
source_records: [{"source_id": "source_748cef2215ddc958568e6368", "source_record_sha256": "af9c06fac15dfefbecea20cc28f8e6a0b032d2fdb3f98664e23b740071f1a235", "raw_content_sha256": "ea6151a38b853ec9c204bc3c600b6c9e14e1bed2a36954299297cb470a5ba86c", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-19T01:46:39+08:00"
completed_at: "2026-07-19T01:46:40+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/architecture/architecture_929a68a1fd830b00f780f138.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_748cef2215ddc958568e6368 raw_sha256:ea6151a38b853ec9c204bc3c600b6c9e14e1bed2a36954299297cb470a5ba86c"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_748cef2215ddc958568e6368 record_sha256:af9c06fac15dfefbecea20cc28f8e6a0b032d2fdb3f98664e23b740071f1a235"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:architecture_929a68a1fd830b00f780f138"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_748cef2215ddc958568e6368"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T01:30:42+08:00", "source:source_748cef2215ddc958568e6368 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "af6a08624d4b82ed4a4b873d9fb492c504b768c5c095c0a1b4a738939d9f06df", "source_state_sha256": "191bd232a81a7c3515d2743a3737663e9247038cd3bb4116145ca33be829f901", "source_record_sha256s": {"source_748cef2215ddc958568e6368": "af9c06fac15dfefbecea20cc28f8e6a0b032d2fdb3f98664e23b740071f1a235"}, "raw_state_sha256": "26f018d084e5836beffb81658f945b3b5f9f11bc5115e8289eda22dd9039c643", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "e0622b6a12da2580ead7ce12c10c121bfc67bec1f13537ce074d80ae7278b3f1", "relation_fingerprint": {"outgoing_relations_sha256": "2ef43e66b5804a8cd61250216764d8be4f87a11bf6bcc1c2995a943bc656f2bd", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "2ef43e66b5804a8cd61250216764d8be4f87a11bf6bcc1c2995a943bc656f2bd"}, "relation_neighborhood_sha256": "2ef43e66b5804a8cd61250216764d8be4f87a11bf6bcc1c2995a943bc656f2bd", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:architecture_929a68a1fd830b00f780f138"
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
        "object_updated_at:2026-07-19T01:30:42+08:00",
        "source:source_748cef2215ddc958568e6368 work_sha256:none"
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
        "source:source_748cef2215ddc958568e6368 record_sha256:af9c06fac15dfefbecea20cc28f8e6a0b032d2fdb3f98664e23b740071f1a235"
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
        "source:source_748cef2215ddc958568e6368 raw_sha256:ea6151a38b853ec9c204bc3c600b6c9e14e1bed2a36954299297cb470a5ba86c"
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
        "related:source_748cef2215ddc958568e6368"
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
        "validated:vault/memory/architecture/architecture_929a68a1fd830b00f780f138.md"
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
  "completed_at": "2026-07-19T01:46:40+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "af6a08624d4b82ed4a4b873d9fb492c504b768c5c095c0a1b4a738939d9f06df",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "26f018d084e5836beffb81658f945b3b5f9f11bc5115e8289eda22dd9039c643",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "2ef43e66b5804a8cd61250216764d8be4f87a11bf6bcc1c2995a943bc656f2bd",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "2ef43e66b5804a8cd61250216764d8be4f87a11bf6bcc1c2995a943bc656f2bd"
    },
    "relation_neighborhood_sha256": "2ef43e66b5804a8cd61250216764d8be4f87a11bf6bcc1c2995a943bc656f2bd",
    "source_record_sha256s": {
      "source_748cef2215ddc958568e6368": "af9c06fac15dfefbecea20cc28f8e6a0b032d2fdb3f98664e23b740071f1a235"
    },
    "source_state_sha256": "191bd232a81a7c3515d2743a3737663e9247038cd3bb4116145ca33be829f901",
    "work_identity_sha256": "e0622b6a12da2580ead7ce12c10c121bfc67bec1f13537ce074d80ae7278b3f1"
  },
  "consolidation_id": "consolidation_2fd19d87e433d955dc98986a",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T01:46:40+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_2fd19d87e433d955dc98986a",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "architecture_929a68a1fd830b00f780f138",
  "object_sha256_after": "af6a08624d4b82ed4a4b873d9fb492c504b768c5c095c0a1b4a738939d9f06df",
  "object_sha256_before": "4b52040d97154dba2b8c430408d094bd06beabe32bae81e4034de924377740e6",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_748cef2215ddc958568e6368"
  ],
  "source_records": [
    {
      "raw_content_sha256": "ea6151a38b853ec9c204bc3c600b6c9e14e1bed2a36954299297cb470a5ba86c",
      "source_id": "source_748cef2215ddc958568e6368",
      "source_record_sha256": "af9c06fac15dfefbecea20cc28f8e6a0b032d2fdb3f98664e23b740071f1a235",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "ea6151a38b853ec9c204bc3c600b6c9e14e1bed2a36954299297cb470a5ba86c"
  ],
  "started_at": "2026-07-19T01:46:39+08:00",
  "status": "complete",
  "title": "Consolidation: the policy attends to memory through its existing token-processing pipeline.",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T01:46:40+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
