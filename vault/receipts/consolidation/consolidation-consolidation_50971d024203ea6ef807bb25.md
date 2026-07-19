---
id: "consolidation_50971d024203ea6ef807bb25"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: The neural network architecture of GR00T N1.7 is a combination of vision-language foundation model"
created_at: "2026-07-19T03:05:27+08:00"
updated_at: "2026-07-19T03:05:27+08:00"
consolidation_id: "consolidation_50971d024203ea6ef807bb25"
object_id: "claim_251ad28e5021bb5fb97a0f2b"
object_version_before: 1
object_sha256_before: "e3949d66a544cd402963efeb6bcd46885283ffb75c043cff8c1357444814b807"
object_sha256_after: "a499823e26130c4b60cb3ca3ba7b8c3bf652d000eb5932a6a026f86f22b4afe4"
source_ids: ["source_34d6513b0522739d0b25e303"]
source_sha256s: ["033e4db94452ac25a2bef6e5602333badc523745bb3b99f4d52888abb41ff393"]
source_records: [{"source_id": "source_34d6513b0522739d0b25e303", "source_record_sha256": "66934a4775cde9b449ccfaede3175151f55b64dbd8e54e44e5ce0fbb5d757b21", "raw_content_sha256": "033e4db94452ac25a2bef6e5602333badc523745bb3b99f4d52888abb41ff393", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["evidence_9d814f3351cd8e54a857"]
started_at: "2026-07-19T03:05:27+08:00"
completed_at: "2026-07-19T03:05:27+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/claim/claim_251ad28e5021bb5fb97a0f2b.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_34d6513b0522739d0b25e303 raw_sha256:033e4db94452ac25a2bef6e5602333badc523745bb3b99f4d52888abb41ff393"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_34d6513b0522739d0b25e303 record_sha256:66934a4775cde9b449ccfaede3175151f55b64dbd8e54e44e5ce0fbb5d757b21"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["evidence:evidence_9d814f3351cd8e54a857"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "passed", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": "full", "findings": ["evidence_entailment:full"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 2 candidates inspected", "candidate:claim_251ad28e5021bb5fb97a0f2b", "candidate:source_34d6513b0522739d0b25e303"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_34d6513b0522739d0b25e303", "related:concept_generalist_cross_embodiment_vla"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T03:01:53+08:00", "source:source_34d6513b0522739d0b25e303 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "a499823e26130c4b60cb3ca3ba7b8c3bf652d000eb5932a6a026f86f22b4afe4", "source_state_sha256": "10e992a09b7d823660b891c05d59b0c3fc22bb300e2143bed4c89ab918b889a2", "source_record_sha256s": {"source_34d6513b0522739d0b25e303": "66934a4775cde9b449ccfaede3175151f55b64dbd8e54e44e5ce0fbb5d757b21"}, "raw_state_sha256": "454943d8f5cffd016f8d2aa892c4c744975e711c15bd8810b3e4378e1787492b", "evidence_sha256": "a94764940eb2873324c6add93f46310d597c68f6c5a7fdab4f4be047aeb065f0", "extraction_state_sha256": "0c03eb79e11c3e289157ff7ed2ebe237cdd7a61066bd74186e04e879977167ca", "work_identity_sha256": "af0ee3378ce29c18eb07048d9b5008e8bbe6e8899e16c91f47eddd5e4a7f7c61", "relation_fingerprint": {"outgoing_relations_sha256": "9c2fba4204ad8fff7610c6a8d61f46520b4d60b87c290c2d8194ce61576c8312", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "9c2fba4204ad8fff7610c6a8d61f46520b4d60b87c290c2d8194ce61576c8312"}, "relation_neighborhood_sha256": "9c2fba4204ad8fff7610c6a8d61f46520b4d60b87c290c2d8194ce61576c8312", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_251ad28e5021bb5fb97a0f2b",
        "candidate:source_34d6513b0522739d0b25e303"
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
      "semantic_recheck_performed": true,
      "validation_outcome": "passed",
      "warnings": []
    },
    "evidence_revalidated": {
      "check_name": "evidence_revalidated",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "evidence:evidence_9d814f3351cd8e54a857"
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
        "object_updated_at:2026-07-19T03:01:53+08:00",
        "source:source_34d6513b0522739d0b25e303 work_sha256:none"
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
        "source:source_34d6513b0522739d0b25e303 record_sha256:66934a4775cde9b449ccfaede3175151f55b64dbd8e54e44e5ce0fbb5d757b21"
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
        "source:source_34d6513b0522739d0b25e303 raw_sha256:033e4db94452ac25a2bef6e5602333badc523745bb3b99f4d52888abb41ff393"
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
        "related:source_34d6513b0522739d0b25e303",
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
        "validated:vault/memory/claim/claim_251ad28e5021bb5fb97a0f2b.md"
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
  "completed_at": "2026-07-19T03:05:27+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "a94764940eb2873324c6add93f46310d597c68f6c5a7fdab4f4be047aeb065f0",
    "extraction_state_sha256": "0c03eb79e11c3e289157ff7ed2ebe237cdd7a61066bd74186e04e879977167ca",
    "memory_schema_version": 2,
    "object_sha256": "a499823e26130c4b60cb3ca3ba7b8c3bf652d000eb5932a6a026f86f22b4afe4",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "454943d8f5cffd016f8d2aa892c4c744975e711c15bd8810b3e4378e1787492b",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "9c2fba4204ad8fff7610c6a8d61f46520b4d60b87c290c2d8194ce61576c8312",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "9c2fba4204ad8fff7610c6a8d61f46520b4d60b87c290c2d8194ce61576c8312"
    },
    "relation_neighborhood_sha256": "9c2fba4204ad8fff7610c6a8d61f46520b4d60b87c290c2d8194ce61576c8312",
    "source_record_sha256s": {
      "source_34d6513b0522739d0b25e303": "66934a4775cde9b449ccfaede3175151f55b64dbd8e54e44e5ce0fbb5d757b21"
    },
    "source_state_sha256": "10e992a09b7d823660b891c05d59b0c3fc22bb300e2143bed4c89ab918b889a2",
    "work_identity_sha256": "af0ee3378ce29c18eb07048d9b5008e8bbe6e8899e16c91f47eddd5e4a7f7c61"
  },
  "consolidation_id": "consolidation_50971d024203ea6ef807bb25",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T03:05:27+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "evidence_9d814f3351cd8e54a857"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_50971d024203ea6ef807bb25",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_251ad28e5021bb5fb97a0f2b",
  "object_sha256_after": "a499823e26130c4b60cb3ca3ba7b8c3bf652d000eb5932a6a026f86f22b4afe4",
  "object_sha256_before": "e3949d66a544cd402963efeb6bcd46885283ffb75c043cff8c1357444814b807",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_34d6513b0522739d0b25e303"
  ],
  "source_records": [
    {
      "raw_content_sha256": "033e4db94452ac25a2bef6e5602333badc523745bb3b99f4d52888abb41ff393",
      "source_id": "source_34d6513b0522739d0b25e303",
      "source_record_sha256": "66934a4775cde9b449ccfaede3175151f55b64dbd8e54e44e5ce0fbb5d757b21",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "033e4db94452ac25a2bef6e5602333badc523745bb3b99f4d52888abb41ff393"
  ],
  "started_at": "2026-07-19T03:05:27+08:00",
  "status": "complete",
  "title": "Consolidation: The neural network architecture of GR00T N1.7 is a combination of vision-language foundation model",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T03:05:27+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
