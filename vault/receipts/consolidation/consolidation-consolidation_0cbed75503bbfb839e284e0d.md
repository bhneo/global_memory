---
id: "consolidation_0cbed75503bbfb839e284e0d"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 触觉对齐的人到机器人接触迁移"
created_at: "2026-07-20T13:37:29+08:00"
updated_at: "2026-07-20T13:37:29+08:00"
consolidation_id: "consolidation_0cbed75503bbfb839e284e0d"
object_id: "concept_5b49f7afd60ba18d35ca58e8"
object_version_before: 1
object_sha256_before: "a65d54474232e2027bea0ab4c1e69aa240ab1b17125482f1ea558f849a7ca484"
object_sha256_after: "9f301ce46f2650c29c7a8c4a52cd57b8019aa91bd7ca9c2865657b5781853f6f"
source_ids: ["source_37fe3c1f9d9fb7daa262fa91"]
source_sha256s: ["5655f303c17cd3486b6f71691dc332a3456cd7d3ac61c05fc1b44c73d391854a"]
source_records: [{"source_id": "source_37fe3c1f9d9fb7daa262fa91", "source_record_sha256": "ce6650953aaf0d216b205b64349c689eac34e1c071c28eb38c167003e2011924", "raw_content_sha256": "5655f303c17cd3486b6f71691dc332a3456cd7d3ac61c05fc1b44c73d391854a", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-20T13:37:28+08:00"
completed_at: "2026-07-20T13:37:29+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_5b49f7afd60ba18d35ca58e8.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_37fe3c1f9d9fb7daa262fa91 raw_sha256:5655f303c17cd3486b6f71691dc332a3456cd7d3ac61c05fc1b44c73d391854a"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_37fe3c1f9d9fb7daa262fa91 record_sha256:ce6650953aaf0d216b205b64349c689eac34e1c071c28eb38c167003e2011924"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_5b49f7afd60ba18d35ca58e8"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 3 related objects found", "related:source_37fe3c1f9d9fb7daa262fa91", "related:concept_multitimescale_tactile_world_model", "related:concept_5b49f7afd60ba18d35ca58e8"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-20T12:39:32+08:00", "source:source_37fe3c1f9d9fb7daa262fa91 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "9f301ce46f2650c29c7a8c4a52cd57b8019aa91bd7ca9c2865657b5781853f6f", "source_state_sha256": "60d5835075e5cb0045aed7d1805b7cd44710b2b2937aea487a710b2dbc32388a", "source_record_sha256s": {"source_37fe3c1f9d9fb7daa262fa91": "ce6650953aaf0d216b205b64349c689eac34e1c071c28eb38c167003e2011924"}, "raw_state_sha256": "baa4735e9370e39382703b9892dc650b1e051123ba09d7de2f788d4e55caf901", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "0faebd2ff14c43c2d701f3895f9611b59cfb2714eaf217dad5b7e23bf0fed36d", "relation_fingerprint": {"outgoing_relations_sha256": "565cbb008ffb147a78e0ccb5a7758102df2f2d3de601a7813a0e98b6919b73f7", "incoming_relations_sha256": "0a5ba1b0c29d0e563912d153be4cc471d231e68f9992a515a8a5e2af423262e2", "full_neighborhood_sha256": "885e92cdf98f08977e84d2156057a4d2a7bff1a16e87d01e6f4917692ca2f66f"}, "relation_neighborhood_sha256": "885e92cdf98f08977e84d2156057a4d2a7bff1a16e87d01e6f4917692ca2f66f", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_5b49f7afd60ba18d35ca58e8"
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
        "object_updated_at:2026-07-20T12:39:32+08:00",
        "source:source_37fe3c1f9d9fb7daa262fa91 work_sha256:none"
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
        "source:source_37fe3c1f9d9fb7daa262fa91 record_sha256:ce6650953aaf0d216b205b64349c689eac34e1c071c28eb38c167003e2011924"
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
        "source:source_37fe3c1f9d9fb7daa262fa91 raw_sha256:5655f303c17cd3486b6f71691dc332a3456cd7d3ac61c05fc1b44c73d391854a"
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
        "related:source_37fe3c1f9d9fb7daa262fa91",
        "related:concept_multitimescale_tactile_world_model",
        "related:concept_5b49f7afd60ba18d35ca58e8"
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
        "validated:vault/memory/concept/concept_5b49f7afd60ba18d35ca58e8.md"
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
  "completed_at": "2026-07-20T13:37:29+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "9f301ce46f2650c29c7a8c4a52cd57b8019aa91bd7ca9c2865657b5781853f6f",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "baa4735e9370e39382703b9892dc650b1e051123ba09d7de2f788d4e55caf901",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "885e92cdf98f08977e84d2156057a4d2a7bff1a16e87d01e6f4917692ca2f66f",
      "incoming_relations_sha256": "0a5ba1b0c29d0e563912d153be4cc471d231e68f9992a515a8a5e2af423262e2",
      "outgoing_relations_sha256": "565cbb008ffb147a78e0ccb5a7758102df2f2d3de601a7813a0e98b6919b73f7"
    },
    "relation_neighborhood_sha256": "885e92cdf98f08977e84d2156057a4d2a7bff1a16e87d01e6f4917692ca2f66f",
    "source_record_sha256s": {
      "source_37fe3c1f9d9fb7daa262fa91": "ce6650953aaf0d216b205b64349c689eac34e1c071c28eb38c167003e2011924"
    },
    "source_state_sha256": "60d5835075e5cb0045aed7d1805b7cd44710b2b2937aea487a710b2dbc32388a",
    "work_identity_sha256": "0faebd2ff14c43c2d701f3895f9611b59cfb2714eaf217dad5b7e23bf0fed36d"
  },
  "consolidation_id": "consolidation_0cbed75503bbfb839e284e0d",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-20T13:37:29+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_0cbed75503bbfb839e284e0d",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_5b49f7afd60ba18d35ca58e8",
  "object_sha256_after": "9f301ce46f2650c29c7a8c4a52cd57b8019aa91bd7ca9c2865657b5781853f6f",
  "object_sha256_before": "a65d54474232e2027bea0ab4c1e69aa240ab1b17125482f1ea558f849a7ca484",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_37fe3c1f9d9fb7daa262fa91"
  ],
  "source_records": [
    {
      "raw_content_sha256": "5655f303c17cd3486b6f71691dc332a3456cd7d3ac61c05fc1b44c73d391854a",
      "source_id": "source_37fe3c1f9d9fb7daa262fa91",
      "source_record_sha256": "ce6650953aaf0d216b205b64349c689eac34e1c071c28eb38c167003e2011924",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "5655f303c17cd3486b6f71691dc332a3456cd7d3ac61c05fc1b44c73d391854a"
  ],
  "started_at": "2026-07-20T13:37:28+08:00",
  "status": "complete",
  "title": "Consolidation: 触觉对齐的人到机器人接触迁移",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-20T13:37:29+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
