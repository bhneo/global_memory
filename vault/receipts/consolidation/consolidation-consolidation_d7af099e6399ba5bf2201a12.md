---
id: "consolidation_d7af099e6399ba5bf2201a12"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: can the proxy labels themselves be corrected before"
created_at: "2026-07-19T01:47:08+08:00"
updated_at: "2026-07-19T01:47:08+08:00"
consolidation_id: "consolidation_d7af099e6399ba5bf2201a12"
object_id: "question_a6b5d595ace88e906de2e2f0"
object_version_before: 1
object_sha256_before: "59ff48fb18d227d65e286e31148aa11f0cb527215b45197b8fa41644fd098c4c"
object_sha256_after: "559814e04b07b9d167def1855146e398f8b676bbaa214cecd10baa1632599953"
source_ids: ["source_e326446389e083c6ba9c94c2"]
source_sha256s: ["a4b4478068c3f446e7c102b61dac030838357d1d190f678139674fd0cf4e9251"]
source_records: [{"source_id": "source_e326446389e083c6ba9c94c2", "source_record_sha256": "b09217e1b8adc7659af388b2015806395a8eadaf82ae9f532b647ee7f980c2f4", "raw_content_sha256": "a4b4478068c3f446e7c102b61dac030838357d1d190f678139674fd0cf4e9251", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-19T01:47:08+08:00"
completed_at: "2026-07-19T01:47:08+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/question/question_a6b5d595ace88e906de2e2f0.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_e326446389e083c6ba9c94c2 raw_sha256:a4b4478068c3f446e7c102b61dac030838357d1d190f678139674fd0cf4e9251"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_e326446389e083c6ba9c94c2 record_sha256:b09217e1b8adc7659af388b2015806395a8eadaf82ae9f532b647ee7f980c2f4"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:question_a6b5d595ace88e906de2e2f0"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_e326446389e083c6ba9c94c2"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T01:40:20+08:00", "source:source_e326446389e083c6ba9c94c2 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "559814e04b07b9d167def1855146e398f8b676bbaa214cecd10baa1632599953", "source_state_sha256": "175643c585ed9f9158433c119d8cd87528077b9488c19612c71f38f8ef022d4c", "source_record_sha256s": {"source_e326446389e083c6ba9c94c2": "b09217e1b8adc7659af388b2015806395a8eadaf82ae9f532b647ee7f980c2f4"}, "raw_state_sha256": "57e2cff3a667900f47e60aa767dc0ad89ed72e7de30a22a5294a7d352d7c7b99", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "ef58331347cebcea476e77235a11d963313cc4f5f41903decacca7833c249bc0", "relation_fingerprint": {"outgoing_relations_sha256": "2eb2ecd9128894d52ffe1aa67bd9202ebc056415b222c035fe695dea04aa674e", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "2eb2ecd9128894d52ffe1aa67bd9202ebc056415b222c035fe695dea04aa674e"}, "relation_neighborhood_sha256": "2eb2ecd9128894d52ffe1aa67bd9202ebc056415b222c035fe695dea04aa674e", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:question_a6b5d595ace88e906de2e2f0"
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
        "object_updated_at:2026-07-19T01:40:20+08:00",
        "source:source_e326446389e083c6ba9c94c2 work_sha256:none"
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
        "source:source_e326446389e083c6ba9c94c2 record_sha256:b09217e1b8adc7659af388b2015806395a8eadaf82ae9f532b647ee7f980c2f4"
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
        "source:source_e326446389e083c6ba9c94c2 raw_sha256:a4b4478068c3f446e7c102b61dac030838357d1d190f678139674fd0cf4e9251"
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
        "related:source_e326446389e083c6ba9c94c2"
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
        "validated:vault/memory/question/question_a6b5d595ace88e906de2e2f0.md"
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
  "completed_at": "2026-07-19T01:47:08+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "559814e04b07b9d167def1855146e398f8b676bbaa214cecd10baa1632599953",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "57e2cff3a667900f47e60aa767dc0ad89ed72e7de30a22a5294a7d352d7c7b99",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "2eb2ecd9128894d52ffe1aa67bd9202ebc056415b222c035fe695dea04aa674e",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "2eb2ecd9128894d52ffe1aa67bd9202ebc056415b222c035fe695dea04aa674e"
    },
    "relation_neighborhood_sha256": "2eb2ecd9128894d52ffe1aa67bd9202ebc056415b222c035fe695dea04aa674e",
    "source_record_sha256s": {
      "source_e326446389e083c6ba9c94c2": "b09217e1b8adc7659af388b2015806395a8eadaf82ae9f532b647ee7f980c2f4"
    },
    "source_state_sha256": "175643c585ed9f9158433c119d8cd87528077b9488c19612c71f38f8ef022d4c",
    "work_identity_sha256": "ef58331347cebcea476e77235a11d963313cc4f5f41903decacca7833c249bc0"
  },
  "consolidation_id": "consolidation_d7af099e6399ba5bf2201a12",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T01:47:08+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_d7af099e6399ba5bf2201a12",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "question_a6b5d595ace88e906de2e2f0",
  "object_sha256_after": "559814e04b07b9d167def1855146e398f8b676bbaa214cecd10baa1632599953",
  "object_sha256_before": "59ff48fb18d227d65e286e31148aa11f0cb527215b45197b8fa41644fd098c4c",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_e326446389e083c6ba9c94c2"
  ],
  "source_records": [
    {
      "raw_content_sha256": "a4b4478068c3f446e7c102b61dac030838357d1d190f678139674fd0cf4e9251",
      "source_id": "source_e326446389e083c6ba9c94c2",
      "source_record_sha256": "b09217e1b8adc7659af388b2015806395a8eadaf82ae9f532b647ee7f980c2f4",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "a4b4478068c3f446e7c102b61dac030838357d1d190f678139674fd0cf4e9251"
  ],
  "started_at": "2026-07-19T01:47:08+08:00",
  "status": "complete",
  "title": "Consolidation: can the proxy labels themselves be corrected before",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T01:47:08+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
