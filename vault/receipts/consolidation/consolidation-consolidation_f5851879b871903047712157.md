---
id: "consolidation_f5851879b871903047712157"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 跨本体世界监督通道"
created_at: "2026-07-19T23:49:38+08:00"
updated_at: "2026-07-19T23:49:38+08:00"
consolidation_id: "consolidation_f5851879b871903047712157"
object_id: "concept_ab253cb9064bc1b550d5e973"
object_version_before: 1
object_sha256_before: "1891b768a336db1da9e10261ed20d4294b3746343b91d763d8920de0956aa100"
object_sha256_after: "3b834fcb4aeff5f1a9d4373030e8831abd420cf01394d09e7f7396c50cc62c83"
source_ids: ["source_61f3045b170e78e4adb2422c"]
source_sha256s: ["dcda12fc4e871509ff95847ed92e64cfc71aaf021c3bf17e14312259e2229443"]
source_records: [{"source_id": "source_61f3045b170e78e4adb2422c", "source_record_sha256": "5216a187c7cd52a66dae837c6e2949bdb9e863e37cda2d48c81cdf2d0cf105b6", "raw_content_sha256": "dcda12fc4e871509ff95847ed92e64cfc71aaf021c3bf17e14312259e2229443", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-19T23:49:37+08:00"
completed_at: "2026-07-19T23:49:38+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_ab253cb9064bc1b550d5e973.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_61f3045b170e78e4adb2422c raw_sha256:dcda12fc4e871509ff95847ed92e64cfc71aaf021c3bf17e14312259e2229443"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_61f3045b170e78e4adb2422c record_sha256:5216a187c7cd52a66dae837c6e2949bdb9e863e37cda2d48c81cdf2d0cf105b6"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_ab253cb9064bc1b550d5e973"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_61f3045b170e78e4adb2422c", "related:concept_generalist_cross_embodiment_vla"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T17:16:45+08:00", "source:source_61f3045b170e78e4adb2422c work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "3b834fcb4aeff5f1a9d4373030e8831abd420cf01394d09e7f7396c50cc62c83", "source_state_sha256": "310b59313a7957f80541d18f93257faaed8e26b033dcec47205899cca7d82be3", "source_record_sha256s": {"source_61f3045b170e78e4adb2422c": "5216a187c7cd52a66dae837c6e2949bdb9e863e37cda2d48c81cdf2d0cf105b6"}, "raw_state_sha256": "582e0c562c9f61f67bb20fef5c741cd7828d912daad8ef56f64d6279f90e5fee", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "4881e8cd5fe016ac3e1fd15d49ce2cc450350bcf581eb09ba309e1354c8014be", "relation_fingerprint": {"outgoing_relations_sha256": "ef9109c2c26b759183b6863d029d341a86070c43d1b30c7c14d6a56d60c9742e", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "ef9109c2c26b759183b6863d029d341a86070c43d1b30c7c14d6a56d60c9742e"}, "relation_neighborhood_sha256": "ef9109c2c26b759183b6863d029d341a86070c43d1b30c7c14d6a56d60c9742e", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_ab253cb9064bc1b550d5e973"
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
        "object_updated_at:2026-07-19T17:16:45+08:00",
        "source:source_61f3045b170e78e4adb2422c work_sha256:none"
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
        "source:source_61f3045b170e78e4adb2422c record_sha256:5216a187c7cd52a66dae837c6e2949bdb9e863e37cda2d48c81cdf2d0cf105b6"
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
        "source:source_61f3045b170e78e4adb2422c raw_sha256:dcda12fc4e871509ff95847ed92e64cfc71aaf021c3bf17e14312259e2229443"
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
        "related:source_61f3045b170e78e4adb2422c",
        "related:concept_generalist_cross_embodiment_vla"
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
        "validated:vault/memory/concept/concept_ab253cb9064bc1b550d5e973.md"
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
  "completed_at": "2026-07-19T23:49:38+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "3b834fcb4aeff5f1a9d4373030e8831abd420cf01394d09e7f7396c50cc62c83",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "582e0c562c9f61f67bb20fef5c741cd7828d912daad8ef56f64d6279f90e5fee",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "ef9109c2c26b759183b6863d029d341a86070c43d1b30c7c14d6a56d60c9742e",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "ef9109c2c26b759183b6863d029d341a86070c43d1b30c7c14d6a56d60c9742e"
    },
    "relation_neighborhood_sha256": "ef9109c2c26b759183b6863d029d341a86070c43d1b30c7c14d6a56d60c9742e",
    "source_record_sha256s": {
      "source_61f3045b170e78e4adb2422c": "5216a187c7cd52a66dae837c6e2949bdb9e863e37cda2d48c81cdf2d0cf105b6"
    },
    "source_state_sha256": "310b59313a7957f80541d18f93257faaed8e26b033dcec47205899cca7d82be3",
    "work_identity_sha256": "4881e8cd5fe016ac3e1fd15d49ce2cc450350bcf581eb09ba309e1354c8014be"
  },
  "consolidation_id": "consolidation_f5851879b871903047712157",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T23:49:38+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_f5851879b871903047712157",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_ab253cb9064bc1b550d5e973",
  "object_sha256_after": "3b834fcb4aeff5f1a9d4373030e8831abd420cf01394d09e7f7396c50cc62c83",
  "object_sha256_before": "1891b768a336db1da9e10261ed20d4294b3746343b91d763d8920de0956aa100",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_61f3045b170e78e4adb2422c"
  ],
  "source_records": [
    {
      "raw_content_sha256": "dcda12fc4e871509ff95847ed92e64cfc71aaf021c3bf17e14312259e2229443",
      "source_id": "source_61f3045b170e78e4adb2422c",
      "source_record_sha256": "5216a187c7cd52a66dae837c6e2949bdb9e863e37cda2d48c81cdf2d0cf105b6",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "dcda12fc4e871509ff95847ed92e64cfc71aaf021c3bf17e14312259e2229443"
  ],
  "started_at": "2026-07-19T23:49:37+08:00",
  "status": "complete",
  "title": "Consolidation: 跨本体世界监督通道",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T23:49:38+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
