---
id: "consolidation_055cdd8b1d32c009b15c925d"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 前缀可解码的有序动作令牌 / Prefix-decodable ordered action tokens"
created_at: "2026-08-02T12:31:02+08:00"
updated_at: "2026-08-02T12:31:02+08:00"
consolidation_id: "consolidation_055cdd8b1d32c009b15c925d"
object_id: "concept_fdb5ce439cbb603e19af8653"
object_version_before: 1
object_sha256_before: "3a08daf7f647a4b0008f87d93cce0e6ad1fcd586378bae56111e05941ab699cf"
object_sha256_after: "47ef90ae920c348d356d90c3a75ea49997b7d34288dde1ba5a5be3014f31f3ab"
source_ids: ["source_ba71396b5fc37637b125a89f"]
source_sha256s: ["172ce81b6a922b1ad05f1c5c102e6aae06509a6a84b2d256ec033b275427d16c"]
source_records: [{"source_id": "source_ba71396b5fc37637b125a89f", "source_record_sha256": "3e8ce2f828dae6e66ddc8bcda16059ea251d432527166f3c25ae4de7cba321dc", "raw_content_sha256": "172ce81b6a922b1ad05f1c5c102e6aae06509a6a84b2d256ec033b275427d16c", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-08-02T12:31:01+08:00"
completed_at: "2026-08-02T12:31:02+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_fdb5ce439cbb603e19af8653.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_ba71396b5fc37637b125a89f raw_sha256:172ce81b6a922b1ad05f1c5c102e6aae06509a6a84b2d256ec033b275427d16c"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_ba71396b5fc37637b125a89f record_sha256:3e8ce2f828dae6e66ddc8bcda16059ea251d432527166f3c25ae4de7cba321dc"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_fdb5ce439cbb603e19af8653"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_ba71396b5fc37637b125a89f", "related:concept_dynamic_execution_horizon"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-28T18:37:22+08:00", "source:source_ba71396b5fc37637b125a89f work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "47ef90ae920c348d356d90c3a75ea49997b7d34288dde1ba5a5be3014f31f3ab", "source_state_sha256": "ab9bde0954da30e3049f4a130ea5c47835be278c2a9ceb613d485bb1892b1c14", "source_record_sha256s": {"source_ba71396b5fc37637b125a89f": "3e8ce2f828dae6e66ddc8bcda16059ea251d432527166f3c25ae4de7cba321dc"}, "raw_state_sha256": "abc28c94c01e3d575c23104d08fd952aa0a90b65323f38f32e46c5f4d5863678", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "cac3443e5640a819138fd82ef83decd2d6315aa42db9f5672abc6d44e01c1db5", "relation_fingerprint": {"outgoing_relations_sha256": "9a2b7612fd6db5e39d8fd87255103e088d6b2f0b292200d117d0cd593d61364d", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "9a2b7612fd6db5e39d8fd87255103e088d6b2f0b292200d117d0cd593d61364d"}, "relation_neighborhood_sha256": "9a2b7612fd6db5e39d8fd87255103e088d6b2f0b292200d117d0cd593d61364d", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_fdb5ce439cbb603e19af8653"
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
        "object_updated_at:2026-07-28T18:37:22+08:00",
        "source:source_ba71396b5fc37637b125a89f work_sha256:none"
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
        "source:source_ba71396b5fc37637b125a89f record_sha256:3e8ce2f828dae6e66ddc8bcda16059ea251d432527166f3c25ae4de7cba321dc"
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
        "source:source_ba71396b5fc37637b125a89f raw_sha256:172ce81b6a922b1ad05f1c5c102e6aae06509a6a84b2d256ec033b275427d16c"
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
        "related:source_ba71396b5fc37637b125a89f",
        "related:concept_dynamic_execution_horizon"
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
        "validated:vault/memory/concept/concept_fdb5ce439cbb603e19af8653.md"
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
  "completed_at": "2026-08-02T12:31:02+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "47ef90ae920c348d356d90c3a75ea49997b7d34288dde1ba5a5be3014f31f3ab",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "abc28c94c01e3d575c23104d08fd952aa0a90b65323f38f32e46c5f4d5863678",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "9a2b7612fd6db5e39d8fd87255103e088d6b2f0b292200d117d0cd593d61364d",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "9a2b7612fd6db5e39d8fd87255103e088d6b2f0b292200d117d0cd593d61364d"
    },
    "relation_neighborhood_sha256": "9a2b7612fd6db5e39d8fd87255103e088d6b2f0b292200d117d0cd593d61364d",
    "source_record_sha256s": {
      "source_ba71396b5fc37637b125a89f": "3e8ce2f828dae6e66ddc8bcda16059ea251d432527166f3c25ae4de7cba321dc"
    },
    "source_state_sha256": "ab9bde0954da30e3049f4a130ea5c47835be278c2a9ceb613d485bb1892b1c14",
    "work_identity_sha256": "cac3443e5640a819138fd82ef83decd2d6315aa42db9f5672abc6d44e01c1db5"
  },
  "consolidation_id": "consolidation_055cdd8b1d32c009b15c925d",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-08-02T12:31:02+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_055cdd8b1d32c009b15c925d",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_fdb5ce439cbb603e19af8653",
  "object_sha256_after": "47ef90ae920c348d356d90c3a75ea49997b7d34288dde1ba5a5be3014f31f3ab",
  "object_sha256_before": "3a08daf7f647a4b0008f87d93cce0e6ad1fcd586378bae56111e05941ab699cf",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_ba71396b5fc37637b125a89f"
  ],
  "source_records": [
    {
      "raw_content_sha256": "172ce81b6a922b1ad05f1c5c102e6aae06509a6a84b2d256ec033b275427d16c",
      "source_id": "source_ba71396b5fc37637b125a89f",
      "source_record_sha256": "3e8ce2f828dae6e66ddc8bcda16059ea251d432527166f3c25ae4de7cba321dc",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "172ce81b6a922b1ad05f1c5c102e6aae06509a6a84b2d256ec033b275427d16c"
  ],
  "started_at": "2026-08-02T12:31:01+08:00",
  "status": "complete",
  "title": "Consolidation: 前缀可解码的有序动作令牌 / Prefix-decodable ordered action tokens",
  "type": "consolidation_receipt",
  "updated_at": "2026-08-02T12:31:02+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
