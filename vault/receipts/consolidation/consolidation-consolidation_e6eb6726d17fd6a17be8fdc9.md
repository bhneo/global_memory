---
id: "consolidation_e6eb6726d17fd6a17be8fdc9"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 世界动作模型的激活空间鲁棒性 steering"
created_at: "2026-07-26T12:33:23+08:00"
updated_at: "2026-07-26T12:33:23+08:00"
consolidation_id: "consolidation_e6eb6726d17fd6a17be8fdc9"
object_id: "concept_09dc6e910b167ba474c89c38"
object_version_before: 1
object_sha256_before: "3c1890dbb92719a70f82a1677cd238b0391000d4d4d7f386c2a4b233ad898b12"
object_sha256_after: "ac41b269bcc646f96fdeff66ab221e7fbf5d22a8bc6a52d065f77dbfe74c1083"
source_ids: ["source_38cba686373b003398483ab2"]
source_sha256s: ["e11eb6aacf2a81fe62488337d3e1b0ee926b325ed36b634b5713b2a772e36965"]
source_records: [{"source_id": "source_38cba686373b003398483ab2", "source_record_sha256": "a4e431a376e55ef5187e50298954aaaa3bcc021ca6c293b67fb5cf154417c9c2", "raw_content_sha256": "e11eb6aacf2a81fe62488337d3e1b0ee926b325ed36b634b5713b2a772e36965", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:22+08:00"
completed_at: "2026-07-26T12:33:23+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_09dc6e910b167ba474c89c38.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_38cba686373b003398483ab2 raw_sha256:e11eb6aacf2a81fe62488337d3e1b0ee926b325ed36b634b5713b2a772e36965"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_38cba686373b003398483ab2 record_sha256:a4e431a376e55ef5187e50298954aaaa3bcc021ca6c293b67fb5cf154417c9c2"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_09dc6e910b167ba474c89c38"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_38cba686373b003398483ab2", "related:concept_latent_space_intervention_adaptation"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-20T18:05:49+08:00", "source:source_38cba686373b003398483ab2 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "ac41b269bcc646f96fdeff66ab221e7fbf5d22a8bc6a52d065f77dbfe74c1083", "source_state_sha256": "d0cdfc9561706d66e0f8d7139f95e44d566e64ab0820df16ee740d58361e7d66", "source_record_sha256s": {"source_38cba686373b003398483ab2": "a4e431a376e55ef5187e50298954aaaa3bcc021ca6c293b67fb5cf154417c9c2"}, "raw_state_sha256": "fe82f8b85fe2a278b1671924f98a67d7899daab7a4cec0ea269a42d4eecfc009", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "00d603c25b081e7db56ebb5b82ef38cda85d8639840d5d3c7475996066499913", "relation_fingerprint": {"outgoing_relations_sha256": "c1bffa215214275b5f099b9a77eaf84a91fd08f0747b9b387acf2d24a1a244bb", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "c1bffa215214275b5f099b9a77eaf84a91fd08f0747b9b387acf2d24a1a244bb"}, "relation_neighborhood_sha256": "c1bffa215214275b5f099b9a77eaf84a91fd08f0747b9b387acf2d24a1a244bb", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_09dc6e910b167ba474c89c38"
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
        "object_updated_at:2026-07-20T18:05:49+08:00",
        "source:source_38cba686373b003398483ab2 work_sha256:none"
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
        "source:source_38cba686373b003398483ab2 record_sha256:a4e431a376e55ef5187e50298954aaaa3bcc021ca6c293b67fb5cf154417c9c2"
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
        "source:source_38cba686373b003398483ab2 raw_sha256:e11eb6aacf2a81fe62488337d3e1b0ee926b325ed36b634b5713b2a772e36965"
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
        "related:source_38cba686373b003398483ab2",
        "related:concept_latent_space_intervention_adaptation"
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
        "validated:vault/memory/concept/concept_09dc6e910b167ba474c89c38.md"
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
  "completed_at": "2026-07-26T12:33:23+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "ac41b269bcc646f96fdeff66ab221e7fbf5d22a8bc6a52d065f77dbfe74c1083",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "fe82f8b85fe2a278b1671924f98a67d7899daab7a4cec0ea269a42d4eecfc009",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "c1bffa215214275b5f099b9a77eaf84a91fd08f0747b9b387acf2d24a1a244bb",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "c1bffa215214275b5f099b9a77eaf84a91fd08f0747b9b387acf2d24a1a244bb"
    },
    "relation_neighborhood_sha256": "c1bffa215214275b5f099b9a77eaf84a91fd08f0747b9b387acf2d24a1a244bb",
    "source_record_sha256s": {
      "source_38cba686373b003398483ab2": "a4e431a376e55ef5187e50298954aaaa3bcc021ca6c293b67fb5cf154417c9c2"
    },
    "source_state_sha256": "d0cdfc9561706d66e0f8d7139f95e44d566e64ab0820df16ee740d58361e7d66",
    "work_identity_sha256": "00d603c25b081e7db56ebb5b82ef38cda85d8639840d5d3c7475996066499913"
  },
  "consolidation_id": "consolidation_e6eb6726d17fd6a17be8fdc9",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:23+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_e6eb6726d17fd6a17be8fdc9",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_09dc6e910b167ba474c89c38",
  "object_sha256_after": "ac41b269bcc646f96fdeff66ab221e7fbf5d22a8bc6a52d065f77dbfe74c1083",
  "object_sha256_before": "3c1890dbb92719a70f82a1677cd238b0391000d4d4d7f386c2a4b233ad898b12",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_38cba686373b003398483ab2"
  ],
  "source_records": [
    {
      "raw_content_sha256": "e11eb6aacf2a81fe62488337d3e1b0ee926b325ed36b634b5713b2a772e36965",
      "source_id": "source_38cba686373b003398483ab2",
      "source_record_sha256": "a4e431a376e55ef5187e50298954aaaa3bcc021ca6c293b67fb5cf154417c9c2",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "e11eb6aacf2a81fe62488337d3e1b0ee926b325ed36b634b5713b2a772e36965"
  ],
  "started_at": "2026-07-26T12:33:22+08:00",
  "status": "complete",
  "title": "Consolidation: 世界动作模型的激活空间鲁棒性 steering",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:23+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
