---
id: "consolidation_03e529746c906aaa48f0f585"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: an edit is accepted only when it strictly improves a held-out validation score."
created_at: "2026-07-19T03:05:42+08:00"
updated_at: "2026-07-19T03:05:42+08:00"
consolidation_id: "consolidation_03e529746c906aaa48f0f585"
object_id: "claim_bddbfc583594cb06ab113d17"
object_version_before: 1
object_sha256_before: "628023e1f7785c2283e7c1453e5293ce487703b1a28247be0623498712a8cb36"
object_sha256_after: "c2bc08892885665ec5dc838d8ac27773eb27e5e9474720b095b8cd6bc1d9a7a8"
source_ids: ["source_54c9a7922f348a245d17efaf"]
source_sha256s: ["87f7f0f323b1671e9202b3ebb1596e909e507c71ecd1b360b0075a5ee1727fe3"]
source_records: [{"source_id": "source_54c9a7922f348a245d17efaf", "source_record_sha256": "f6bfc5e50a544268665e30403002502b6a2c6a8cfe777ce7493d01a67df5b7af", "raw_content_sha256": "87f7f0f323b1671e9202b3ebb1596e909e507c71ecd1b360b0075a5ee1727fe3", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["evidence_2641831bfdc5d23523c7"]
started_at: "2026-07-19T03:05:42+08:00"
completed_at: "2026-07-19T03:05:42+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/claim/claim_bddbfc583594cb06ab113d17.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_54c9a7922f348a245d17efaf raw_sha256:87f7f0f323b1671e9202b3ebb1596e909e507c71ecd1b360b0075a5ee1727fe3"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_54c9a7922f348a245d17efaf record_sha256:f6bfc5e50a544268665e30403002502b6a2c6a8cfe777ce7493d01a67df5b7af"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["evidence:evidence_2641831bfdc5d23523c7"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "needs_review", "method": "declared-metadata-inspection", "semantic_recheck_performed": false, "declared_value": "full", "findings": ["evidence_entailment:full"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:claim_bddbfc583594cb06ab113d17"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:question_skill_compilation_boundary", "related:source_54c9a7922f348a245d17efaf"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T02:52:10+08:00", "source:source_54c9a7922f348a245d17efaf work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "c2bc08892885665ec5dc838d8ac27773eb27e5e9474720b095b8cd6bc1d9a7a8", "source_state_sha256": "8524af323d1b64ab161540192272e75f2f6f20475d36b90badfac6544a476c57", "source_record_sha256s": {"source_54c9a7922f348a245d17efaf": "f6bfc5e50a544268665e30403002502b6a2c6a8cfe777ce7493d01a67df5b7af"}, "raw_state_sha256": "537e24658d6016e07a171096577d4af3f02b5646d0590f550631e659022bbcef", "evidence_sha256": "b984fbb82825483c66420344521dea25adade3c1aa193a96497ff14534a2e340", "extraction_state_sha256": "e02c94fefb78fcdb2b38c80a1a738bb039688f564d114b9f960946389db34511", "work_identity_sha256": "bbb63dbc02d2623c807d6e6235c869fd1dcb7dc61d0c202059df64d3f210d663", "relation_fingerprint": {"outgoing_relations_sha256": "e8a164c2f3f3584124c319d1e46a5b3f51d4eb46a4b152363f41f51f2ca5a462", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "e8a164c2f3f3584124c319d1e46a5b3f51d4eb46a4b152363f41f51f2ca5a462"}, "relation_neighborhood_sha256": "e8a164c2f3f3584124c319d1e46a5b3f51d4eb46a4b152363f41f51f2ca5a462", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_bddbfc583594cb06ab113d17"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "check_name": "evidence_entailment_rechecked",
      "declared_value": "full",
      "execution_status": "completed",
      "findings": [
        "evidence_entailment:full"
      ],
      "method": "declared-metadata-inspection",
      "semantic_recheck_performed": false,
      "validation_outcome": "needs_review",
      "warnings": []
    },
    "evidence_revalidated": {
      "check_name": "evidence_revalidated",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "evidence:evidence_2641831bfdc5d23523c7"
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
        "object_updated_at:2026-07-19T02:52:10+08:00",
        "source:source_54c9a7922f348a245d17efaf work_sha256:none"
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
        "source:source_54c9a7922f348a245d17efaf record_sha256:f6bfc5e50a544268665e30403002502b6a2c6a8cfe777ce7493d01a67df5b7af"
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
        "source:source_54c9a7922f348a245d17efaf raw_sha256:87f7f0f323b1671e9202b3ebb1596e909e507c71ecd1b360b0075a5ee1727fe3"
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
        "related:question_skill_compilation_boundary",
        "related:source_54c9a7922f348a245d17efaf"
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
        "validated:vault/memory/claim/claim_bddbfc583594cb06ab113d17.md"
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
  "completed_at": "2026-07-19T03:05:42+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "b984fbb82825483c66420344521dea25adade3c1aa193a96497ff14534a2e340",
    "extraction_state_sha256": "e02c94fefb78fcdb2b38c80a1a738bb039688f564d114b9f960946389db34511",
    "memory_schema_version": 2,
    "object_sha256": "c2bc08892885665ec5dc838d8ac27773eb27e5e9474720b095b8cd6bc1d9a7a8",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "537e24658d6016e07a171096577d4af3f02b5646d0590f550631e659022bbcef",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "e8a164c2f3f3584124c319d1e46a5b3f51d4eb46a4b152363f41f51f2ca5a462",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "e8a164c2f3f3584124c319d1e46a5b3f51d4eb46a4b152363f41f51f2ca5a462"
    },
    "relation_neighborhood_sha256": "e8a164c2f3f3584124c319d1e46a5b3f51d4eb46a4b152363f41f51f2ca5a462",
    "source_record_sha256s": {
      "source_54c9a7922f348a245d17efaf": "f6bfc5e50a544268665e30403002502b6a2c6a8cfe777ce7493d01a67df5b7af"
    },
    "source_state_sha256": "8524af323d1b64ab161540192272e75f2f6f20475d36b90badfac6544a476c57",
    "work_identity_sha256": "bbb63dbc02d2623c807d6e6235c869fd1dcb7dc61d0c202059df64d3f210d663"
  },
  "consolidation_id": "consolidation_03e529746c906aaa48f0f585",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T03:05:42+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "evidence_2641831bfdc5d23523c7"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_03e529746c906aaa48f0f585",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_bddbfc583594cb06ab113d17",
  "object_sha256_after": "c2bc08892885665ec5dc838d8ac27773eb27e5e9474720b095b8cd6bc1d9a7a8",
  "object_sha256_before": "628023e1f7785c2283e7c1453e5293ce487703b1a28247be0623498712a8cb36",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_54c9a7922f348a245d17efaf"
  ],
  "source_records": [
    {
      "raw_content_sha256": "87f7f0f323b1671e9202b3ebb1596e909e507c71ecd1b360b0075a5ee1727fe3",
      "source_id": "source_54c9a7922f348a245d17efaf",
      "source_record_sha256": "f6bfc5e50a544268665e30403002502b6a2c6a8cfe777ce7493d01a67df5b7af",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "87f7f0f323b1671e9202b3ebb1596e909e507c71ecd1b360b0075a5ee1727fe3"
  ],
  "started_at": "2026-07-19T03:05:42+08:00",
  "status": "complete",
  "title": "Consolidation: an edit is accepted only when it strictly improves a held-out validation score.",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T03:05:42+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
