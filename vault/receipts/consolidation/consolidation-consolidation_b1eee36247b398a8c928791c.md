---
id: "consolidation_b1eee36247b398a8c928791c"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: Accepted October 06, 2023) S"
created_at: "2026-07-17T18:35:23+08:00"
updated_at: "2026-07-17T18:35:23+08:00"
consolidation_id: "consolidation_b1eee36247b398a8c928791c"
object_id: "claim_54cac5c21565eb6d274a5383"
object_version_before: 1
object_sha256_before: "8cbbe9c144e144da80aa2c17159c024ec3ba1cf9e2f9083b101013687322e21a"
object_sha256_after: "17552c690278871fd04a944a54c666aa590096e4a756212b25fe5e5c83a2c831"
source_ids: ["source_b85c7e35189fedbd359efa94"]
source_sha256s: ["895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf"]
source_records: [{"source_id": "source_b85c7e35189fedbd359efa94", "source_record_sha256": "b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b", "raw_content_sha256": "895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["evidence_887c253c384e4923c392"]
started_at: "2026-07-17T18:35:23+08:00"
completed_at: "2026-07-17T18:35:23+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_54cac5c21565eb6d274a5383.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_b85c7e35189fedbd359efa94 raw_sha256:895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_b85c7e35189fedbd359efa94 record_sha256:b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:evidence_887c253c384e4923c392"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:none"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_54cac5c21565eb6d274a5383"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_b85c7e35189fedbd359efa94"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:35+08:00", "source:source_b85c7e35189fedbd359efa94 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "17552c690278871fd04a944a54c666aa590096e4a756212b25fe5e5c83a2c831", "source_state_sha256": "26f648c5cc89ca1090db155c5f971c83d5b21756ee0a5dd2cc41627341899013", "source_record_sha256s": {"source_b85c7e35189fedbd359efa94": "b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b"}, "raw_state_sha256": "346713fc2ca01f343247b028b680d3b2faabb0f8d0f164597c7bf14da5801107", "evidence_sha256": "4bd7f9e779ba11616d25fab53c7dccb9117e58c4471095775bd07e6eb79b4d44", "extraction_state_sha256": "d9caaadd6d49bcd8eebaea5588b9164898d265864892880435101d3511fd9d94", "work_identity_sha256": "8460237ad44ecfa2265eaba6409adc7de2728e0538c70ddf769369aa066d3d2a", "relation_neighborhood_sha256": "325ddba7d02ccf73e28dc3d422875501f95a7a6e49e1b08402c14f54db6eb50d", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
      "findings": [
        "contradiction relations inspected; 0 found"
      ],
      "status": "passed",
      "warnings": []
    },
    "drift_checked": {
      "findings": [
        "drift_reports:0"
      ],
      "status": "passed",
      "warnings": []
    },
    "duplicate_search_completed": {
      "findings": [
        "searched title; 1 candidates inspected",
        "candidate:claim_54cac5c21565eb6d274a5383"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "findings": [
        "evidence_entailment:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_revalidated": {
      "findings": [
        "evidence:evidence_887c253c384e4923c392"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:35+08:00",
        "source:source_b85c7e35189fedbd359efa94 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_b85c7e35189fedbd359efa94 record_sha256:b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_b85c7e35189fedbd359efa94 raw_sha256:895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_b85c7e35189fedbd359efa94"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_54cac5c21565eb6d274a5383.md"
      ],
      "status": "passed",
      "warnings": []
    },
    "source_independence_checked": {
      "findings": [
        "distinct_source_ids:1",
        "distinct_work_ids:0"
      ],
      "status": "passed",
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
  "completed_at": "2026-07-17T18:35:23+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4bd7f9e779ba11616d25fab53c7dccb9117e58c4471095775bd07e6eb79b4d44",
    "extraction_state_sha256": "d9caaadd6d49bcd8eebaea5588b9164898d265864892880435101d3511fd9d94",
    "memory_schema_version": 2,
    "object_sha256": "17552c690278871fd04a944a54c666aa590096e4a756212b25fe5e5c83a2c831",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "346713fc2ca01f343247b028b680d3b2faabb0f8d0f164597c7bf14da5801107",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "325ddba7d02ccf73e28dc3d422875501f95a7a6e49e1b08402c14f54db6eb50d",
    "source_record_sha256s": {
      "source_b85c7e35189fedbd359efa94": "b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b"
    },
    "source_state_sha256": "26f648c5cc89ca1090db155c5f971c83d5b21756ee0a5dd2cc41627341899013",
    "work_identity_sha256": "8460237ad44ecfa2265eaba6409adc7de2728e0538c70ddf769369aa066d3d2a"
  },
  "consolidation_id": "consolidation_b1eee36247b398a8c928791c",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:23+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "evidence_887c253c384e4923c392"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_b1eee36247b398a8c928791c",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_54cac5c21565eb6d274a5383",
  "object_sha256_after": "17552c690278871fd04a944a54c666aa590096e4a756212b25fe5e5c83a2c831",
  "object_sha256_before": "8cbbe9c144e144da80aa2c17159c024ec3ba1cf9e2f9083b101013687322e21a",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_b85c7e35189fedbd359efa94"
  ],
  "source_records": [
    {
      "raw_content_sha256": "895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf",
      "source_id": "source_b85c7e35189fedbd359efa94",
      "source_record_sha256": "b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf"
  ],
  "started_at": "2026-07-17T18:35:23+08:00",
  "status": "complete",
  "title": "Consolidation: Accepted October 06, 2023) S",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:23+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
