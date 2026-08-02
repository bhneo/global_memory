---
id: "consolidation_4fb05846d1d0f10269564fc4"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 行为对齐中间表征桥接跨本体数据 / Behavior-aligned intermediate representations for cross-embodiment transfer"
created_at: "2026-08-02T19:55:27+08:00"
updated_at: "2026-08-02T19:55:27+08:00"
consolidation_id: "consolidation_4fb05846d1d0f10269564fc4"
object_id: "concept_e0ed53e4ea7c1e1fa032f1d3"
object_version_before: 1
object_sha256_before: "eb363492e2f921d63f394a0639d4ba6a8842566dbc2f6c441eef7bb915b6636e"
object_sha256_after: "f9c6731d1b6cb06aacba7d660c7f693a8cb81aa5658de83207e2117cf171c59a"
source_ids: ["source_b8c45bfccc9646f938cb564c"]
source_sha256s: ["19291aa379ce61983b744901097acef15fd36407d5f6f4c9f0067b79acfdcdb5"]
source_records: [{"source_id": "source_b8c45bfccc9646f938cb564c", "source_record_sha256": "983f1671ed231849f73e7bdc9b0127111b7853088727aed884eaa4459a0ad41b", "raw_content_sha256": "19291aa379ce61983b744901097acef15fd36407d5f6f4c9f0067b79acfdcdb5", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-08-02T19:55:26+08:00"
completed_at: "2026-08-02T19:55:27+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_e0ed53e4ea7c1e1fa032f1d3.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_b8c45bfccc9646f938cb564c raw_sha256:19291aa379ce61983b744901097acef15fd36407d5f6f4c9f0067b79acfdcdb5"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_b8c45bfccc9646f938cb564c record_sha256:983f1671ed231849f73e7bdc9b0127111b7853088727aed884eaa4459a0ad41b"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_e0ed53e4ea7c1e1fa032f1d3"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 3 related objects found", "related:source_b8c45bfccc9646f938cb564c", "related:concept_ab253cb9064bc1b550d5e973", "related:concept_generalist_cross_embodiment_vla"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-08-02T18:22:23+08:00", "source:source_b8c45bfccc9646f938cb564c work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "f9c6731d1b6cb06aacba7d660c7f693a8cb81aa5658de83207e2117cf171c59a", "source_state_sha256": "1ea45fadf7362bc7a36541ab60dd78042f6a8cf41181d01fc547351e3a641976", "source_record_sha256s": {"source_b8c45bfccc9646f938cb564c": "983f1671ed231849f73e7bdc9b0127111b7853088727aed884eaa4459a0ad41b"}, "raw_state_sha256": "dac054e578a53d289e1e123f4bb1695b8642fe67ec7ad077454d36d73b0f1076", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "2fb46fcd199e7f7dec71361a6a1d9be42f0f65fd6812b7b10e5bd3dd1ebe897d", "relation_fingerprint": {"outgoing_relations_sha256": "2539f5197e32ce852b30183cb18a64041cddd5a5dbb316db922d16bd7d99255c", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "2539f5197e32ce852b30183cb18a64041cddd5a5dbb316db922d16bd7d99255c"}, "relation_neighborhood_sha256": "2539f5197e32ce852b30183cb18a64041cddd5a5dbb316db922d16bd7d99255c", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_e0ed53e4ea7c1e1fa032f1d3"
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
        "object_updated_at:2026-08-02T18:22:23+08:00",
        "source:source_b8c45bfccc9646f938cb564c work_sha256:none"
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
        "source:source_b8c45bfccc9646f938cb564c record_sha256:983f1671ed231849f73e7bdc9b0127111b7853088727aed884eaa4459a0ad41b"
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
        "source:source_b8c45bfccc9646f938cb564c raw_sha256:19291aa379ce61983b744901097acef15fd36407d5f6f4c9f0067b79acfdcdb5"
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
        "related:source_b8c45bfccc9646f938cb564c",
        "related:concept_ab253cb9064bc1b550d5e973",
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
        "validated:vault/memory/concept/concept_e0ed53e4ea7c1e1fa032f1d3.md"
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
  "completed_at": "2026-08-02T19:55:27+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "f9c6731d1b6cb06aacba7d660c7f693a8cb81aa5658de83207e2117cf171c59a",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "dac054e578a53d289e1e123f4bb1695b8642fe67ec7ad077454d36d73b0f1076",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "2539f5197e32ce852b30183cb18a64041cddd5a5dbb316db922d16bd7d99255c",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "2539f5197e32ce852b30183cb18a64041cddd5a5dbb316db922d16bd7d99255c"
    },
    "relation_neighborhood_sha256": "2539f5197e32ce852b30183cb18a64041cddd5a5dbb316db922d16bd7d99255c",
    "source_record_sha256s": {
      "source_b8c45bfccc9646f938cb564c": "983f1671ed231849f73e7bdc9b0127111b7853088727aed884eaa4459a0ad41b"
    },
    "source_state_sha256": "1ea45fadf7362bc7a36541ab60dd78042f6a8cf41181d01fc547351e3a641976",
    "work_identity_sha256": "2fb46fcd199e7f7dec71361a6a1d9be42f0f65fd6812b7b10e5bd3dd1ebe897d"
  },
  "consolidation_id": "consolidation_4fb05846d1d0f10269564fc4",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-08-02T19:55:27+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_4fb05846d1d0f10269564fc4",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_e0ed53e4ea7c1e1fa032f1d3",
  "object_sha256_after": "f9c6731d1b6cb06aacba7d660c7f693a8cb81aa5658de83207e2117cf171c59a",
  "object_sha256_before": "eb363492e2f921d63f394a0639d4ba6a8842566dbc2f6c441eef7bb915b6636e",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_b8c45bfccc9646f938cb564c"
  ],
  "source_records": [
    {
      "raw_content_sha256": "19291aa379ce61983b744901097acef15fd36407d5f6f4c9f0067b79acfdcdb5",
      "source_id": "source_b8c45bfccc9646f938cb564c",
      "source_record_sha256": "983f1671ed231849f73e7bdc9b0127111b7853088727aed884eaa4459a0ad41b",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "19291aa379ce61983b744901097acef15fd36407d5f6f4c9f0067b79acfdcdb5"
  ],
  "started_at": "2026-08-02T19:55:26+08:00",
  "status": "complete",
  "title": "Consolidation: 行为对齐中间表征桥接跨本体数据 / Behavior-aligned intermediate representations for cross-embodiment transfer",
  "type": "consolidation_receipt",
  "updated_at": "2026-08-02T19:55:27+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
