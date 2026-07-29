---
id: "consolidation_528a78a6745434329987870b"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 端到端具身系统可复现性"
created_at: "2026-07-26T12:33:50+08:00"
updated_at: "2026-07-26T12:33:50+08:00"
consolidation_id: "consolidation_528a78a6745434329987870b"
object_id: "concept_end_to_end_embodied_reproducibility"
object_version_before: 1
object_sha256_before: "61225502635067db1c607bf99879b377f0bb92d1f332f2070203dbb1603d0635"
object_sha256_after: "18c85b9834ebdf542e585d3707612a3cd110dd32e5c5c292e32f21a4311012bf"
source_ids: ["source_650f616f1e641912e73115b1"]
source_sha256s: ["3ef9cac2aa672c2b1cf2c06edb93ebb4df7cb504b17c99cb635d082e495009c8"]
source_records: [{"source_id": "source_650f616f1e641912e73115b1", "source_record_sha256": "beba7b69587253148d8c303b3c40f1fb875bd2bc1d3ed476ce0f3b0273616ac0", "raw_content_sha256": "3ef9cac2aa672c2b1cf2c06edb93ebb4df7cb504b17c99cb635d082e495009c8", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:50+08:00"
completed_at: "2026-07-26T12:33:50+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_end_to_end_embodied_reproducibility.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_650f616f1e641912e73115b1 raw_sha256:3ef9cac2aa672c2b1cf2c06edb93ebb4df7cb504b17c99cb635d082e495009c8"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_650f616f1e641912e73115b1 record_sha256:beba7b69587253148d8c303b3c40f1fb875bd2bc1d3ed476ce0f3b0273616ac0"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 2 candidates inspected", "candidate:concept_end_to_end_embodied_reproducibility", "candidate:reflection_b36ae3f4f0dfb6a2942e94ab"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 6 related objects found", "related:source_650f616f1e641912e73115b1", "related:concept_generalist_cross_embodiment_vla", "related:concept_embodied_data_loop", "related:concept_end_to_end_embodied_reproducibility", "related:concept_end_to_end_embodied_reproducibility"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T12:20:10+08:00", "source:source_650f616f1e641912e73115b1 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "18c85b9834ebdf542e585d3707612a3cd110dd32e5c5c292e32f21a4311012bf", "source_state_sha256": "85f5df9aa731b655efe25f07db9033471cf95966c1a280408a839b393ddbe60b", "source_record_sha256s": {"source_650f616f1e641912e73115b1": "beba7b69587253148d8c303b3c40f1fb875bd2bc1d3ed476ce0f3b0273616ac0"}, "raw_state_sha256": "ffd846b11c585a66bc11e37f64f2319e67298933db4878edce5c15ce07cc8c96", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "02a24aa07ce1ce1ce7a4f6b78257bbaf0d255ea5285846a0024dc5f307d04d7b", "relation_fingerprint": {"outgoing_relations_sha256": "cce0ecde4167821ade9797e141e9b93183267e0683dab7ea4aca5006ec725b5e", "incoming_relations_sha256": "dd1bbc53b79fe49e26a1bcc9017c3ecf4d70d5116acf2cc111649ff3c0ac23f6", "full_neighborhood_sha256": "30d452c604fa964a09ca54130a1e58c72919511e3cb435a1f6335c0bfa4fd6ed"}, "relation_neighborhood_sha256": "30d452c604fa964a09ca54130a1e58c72919511e3cb435a1f6335c0bfa4fd6ed", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_end_to_end_embodied_reproducibility",
        "candidate:reflection_b36ae3f4f0dfb6a2942e94ab"
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
        "object_updated_at:2026-07-19T12:20:10+08:00",
        "source:source_650f616f1e641912e73115b1 work_sha256:none"
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
        "source:source_650f616f1e641912e73115b1 record_sha256:beba7b69587253148d8c303b3c40f1fb875bd2bc1d3ed476ce0f3b0273616ac0"
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
        "source:source_650f616f1e641912e73115b1 raw_sha256:3ef9cac2aa672c2b1cf2c06edb93ebb4df7cb504b17c99cb635d082e495009c8"
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
        "relation index inspected; 6 related objects found",
        "related:source_650f616f1e641912e73115b1",
        "related:concept_generalist_cross_embodiment_vla",
        "related:concept_embodied_data_loop",
        "related:concept_end_to_end_embodied_reproducibility",
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
        "validated:vault/memory/concept/concept_end_to_end_embodied_reproducibility.md"
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
  "completed_at": "2026-07-26T12:33:50+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "18c85b9834ebdf542e585d3707612a3cd110dd32e5c5c292e32f21a4311012bf",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "ffd846b11c585a66bc11e37f64f2319e67298933db4878edce5c15ce07cc8c96",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "30d452c604fa964a09ca54130a1e58c72919511e3cb435a1f6335c0bfa4fd6ed",
      "incoming_relations_sha256": "dd1bbc53b79fe49e26a1bcc9017c3ecf4d70d5116acf2cc111649ff3c0ac23f6",
      "outgoing_relations_sha256": "cce0ecde4167821ade9797e141e9b93183267e0683dab7ea4aca5006ec725b5e"
    },
    "relation_neighborhood_sha256": "30d452c604fa964a09ca54130a1e58c72919511e3cb435a1f6335c0bfa4fd6ed",
    "source_record_sha256s": {
      "source_650f616f1e641912e73115b1": "beba7b69587253148d8c303b3c40f1fb875bd2bc1d3ed476ce0f3b0273616ac0"
    },
    "source_state_sha256": "85f5df9aa731b655efe25f07db9033471cf95966c1a280408a839b393ddbe60b",
    "work_identity_sha256": "02a24aa07ce1ce1ce7a4f6b78257bbaf0d255ea5285846a0024dc5f307d04d7b"
  },
  "consolidation_id": "consolidation_528a78a6745434329987870b",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:50+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_528a78a6745434329987870b",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_end_to_end_embodied_reproducibility",
  "object_sha256_after": "18c85b9834ebdf542e585d3707612a3cd110dd32e5c5c292e32f21a4311012bf",
  "object_sha256_before": "61225502635067db1c607bf99879b377f0bb92d1f332f2070203dbb1603d0635",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_650f616f1e641912e73115b1"
  ],
  "source_records": [
    {
      "raw_content_sha256": "3ef9cac2aa672c2b1cf2c06edb93ebb4df7cb504b17c99cb635d082e495009c8",
      "source_id": "source_650f616f1e641912e73115b1",
      "source_record_sha256": "beba7b69587253148d8c303b3c40f1fb875bd2bc1d3ed476ce0f3b0273616ac0",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "3ef9cac2aa672c2b1cf2c06edb93ebb4df7cb504b17c99cb635d082e495009c8"
  ],
  "started_at": "2026-07-26T12:33:50+08:00",
  "status": "complete",
  "title": "Consolidation: 端到端具身系统可复现性",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:50+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
