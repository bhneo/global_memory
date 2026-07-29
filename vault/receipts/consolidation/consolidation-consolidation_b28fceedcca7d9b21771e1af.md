---
id: "consolidation_b28fceedcca7d9b21771e1af"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 形态可重构机器人的跨本体控制边界"
created_at: "2026-07-26T12:33:36+08:00"
updated_at: "2026-07-26T12:33:36+08:00"
consolidation_id: "consolidation_b28fceedcca7d9b21771e1af"
object_id: "concept_705dff5d5d3ebdcb87f1564f"
object_version_before: 1
object_sha256_before: "3fd365e13037184dab839a86073da0b74bfb566f53ed10a30c2a2030a593cec8"
object_sha256_after: "810adc7b1d0bba0042432f1b7e57629c49672c3273d5856cdc11c6ed89ee437d"
source_ids: ["source_adcddc61e96d32f765d29c90"]
source_sha256s: ["6af1ed342a930840af3eb6a2e9ab44ee0718c8f2cb53c65373c23c279b262b75"]
source_records: [{"source_id": "source_adcddc61e96d32f765d29c90", "source_record_sha256": "fb6e1865b77807a0dc26c3081a64177c816d3637f8df6488dddb7fa326c94391", "raw_content_sha256": "6af1ed342a930840af3eb6a2e9ab44ee0718c8f2cb53c65373c23c279b262b75", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:36+08:00"
completed_at: "2026-07-26T12:33:36+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_705dff5d5d3ebdcb87f1564f.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_adcddc61e96d32f765d29c90 raw_sha256:6af1ed342a930840af3eb6a2e9ab44ee0718c8f2cb53c65373c23c279b262b75"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_adcddc61e96d32f765d29c90 record_sha256:fb6e1865b77807a0dc26c3081a64177c816d3637f8df6488dddb7fa326c94391"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_705dff5d5d3ebdcb87f1564f"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_adcddc61e96d32f765d29c90", "related:concept_end_to_end_embodied_reproducibility"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-21T18:08:44+08:00", "source:source_adcddc61e96d32f765d29c90 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "810adc7b1d0bba0042432f1b7e57629c49672c3273d5856cdc11c6ed89ee437d", "source_state_sha256": "61995c6155f7c07e927e3f121c10d1859d230cb30e144e39b3e791a76b5c5d8e", "source_record_sha256s": {"source_adcddc61e96d32f765d29c90": "fb6e1865b77807a0dc26c3081a64177c816d3637f8df6488dddb7fa326c94391"}, "raw_state_sha256": "df0ae6fcf9c92d07f5b4fb7c949219557448cb0010993156a090a835f91faba8", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "c7f6fee5582bd42603445953c3142c2d7fb32486bc6e1e54d203e843d5e00f9a", "relation_fingerprint": {"outgoing_relations_sha256": "c87f96b0228695a31e2e7912aeae37ea4771e81f0ad01eb75b3f842c87db42c9", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "c87f96b0228695a31e2e7912aeae37ea4771e81f0ad01eb75b3f842c87db42c9"}, "relation_neighborhood_sha256": "c87f96b0228695a31e2e7912aeae37ea4771e81f0ad01eb75b3f842c87db42c9", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_705dff5d5d3ebdcb87f1564f"
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
        "object_updated_at:2026-07-21T18:08:44+08:00",
        "source:source_adcddc61e96d32f765d29c90 work_sha256:none"
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
        "source:source_adcddc61e96d32f765d29c90 record_sha256:fb6e1865b77807a0dc26c3081a64177c816d3637f8df6488dddb7fa326c94391"
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
        "source:source_adcddc61e96d32f765d29c90 raw_sha256:6af1ed342a930840af3eb6a2e9ab44ee0718c8f2cb53c65373c23c279b262b75"
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
        "related:source_adcddc61e96d32f765d29c90",
        "related:concept_end_to_end_embodied_reproducibility"
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
        "validated:vault/memory/concept/concept_705dff5d5d3ebdcb87f1564f.md"
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
  "completed_at": "2026-07-26T12:33:36+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "810adc7b1d0bba0042432f1b7e57629c49672c3273d5856cdc11c6ed89ee437d",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "df0ae6fcf9c92d07f5b4fb7c949219557448cb0010993156a090a835f91faba8",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "c87f96b0228695a31e2e7912aeae37ea4771e81f0ad01eb75b3f842c87db42c9",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "c87f96b0228695a31e2e7912aeae37ea4771e81f0ad01eb75b3f842c87db42c9"
    },
    "relation_neighborhood_sha256": "c87f96b0228695a31e2e7912aeae37ea4771e81f0ad01eb75b3f842c87db42c9",
    "source_record_sha256s": {
      "source_adcddc61e96d32f765d29c90": "fb6e1865b77807a0dc26c3081a64177c816d3637f8df6488dddb7fa326c94391"
    },
    "source_state_sha256": "61995c6155f7c07e927e3f121c10d1859d230cb30e144e39b3e791a76b5c5d8e",
    "work_identity_sha256": "c7f6fee5582bd42603445953c3142c2d7fb32486bc6e1e54d203e843d5e00f9a"
  },
  "consolidation_id": "consolidation_b28fceedcca7d9b21771e1af",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:36+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_b28fceedcca7d9b21771e1af",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_705dff5d5d3ebdcb87f1564f",
  "object_sha256_after": "810adc7b1d0bba0042432f1b7e57629c49672c3273d5856cdc11c6ed89ee437d",
  "object_sha256_before": "3fd365e13037184dab839a86073da0b74bfb566f53ed10a30c2a2030a593cec8",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_adcddc61e96d32f765d29c90"
  ],
  "source_records": [
    {
      "raw_content_sha256": "6af1ed342a930840af3eb6a2e9ab44ee0718c8f2cb53c65373c23c279b262b75",
      "source_id": "source_adcddc61e96d32f765d29c90",
      "source_record_sha256": "fb6e1865b77807a0dc26c3081a64177c816d3637f8df6488dddb7fa326c94391",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "6af1ed342a930840af3eb6a2e9ab44ee0718c8f2cb53c65373c23c279b262b75"
  ],
  "started_at": "2026-07-26T12:33:36+08:00",
  "status": "complete",
  "title": "Consolidation: 形态可重构机器人的跨本体控制边界",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:36+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
