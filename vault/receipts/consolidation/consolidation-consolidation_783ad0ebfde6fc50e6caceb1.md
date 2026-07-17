---
id: "consolidation_783ad0ebfde6fc50e6caceb1"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: Φ-SO 在生成过程中施加物理单位约束以排除不一致表达式并缩小搜索空间"
created_at: "2026-07-17T18:35:37+08:00"
updated_at: "2026-07-17T18:35:37+08:00"
consolidation_id: "consolidation_783ad0ebfde6fc50e6caceb1"
object_id: "claim_physo_units_constraints_reduce_search_20260716"
object_version_before: 1
object_sha256_before: "14e09d6aac3a1064daeeb5cbfc31c301347d7cc85dc3cbaf7eb7da614221243b"
object_sha256_after: "95c2c91972e4339acd15c336c6063a342afb20d7cebe841442bfa1731f8fcf4d"
source_ids: ["source_ef99e322cc662cffb7eb5c8f", "source_b85c7e35189fedbd359efa94"]
source_sha256s: ["fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf"]
source_records: [{"source_id": "source_ef99e322cc662cffb7eb5c8f", "source_record_sha256": "3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05", "raw_content_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "work_id": null, "work_document_sha256": null}, {"source_id": "source_b85c7e35189fedbd359efa94", "source_record_sha256": "b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b", "raw_content_sha256": "895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_388", "ev_primary_67f24f6c168a", "ev_primary_d79ac7b3a44d"]
started_at: "2026-07-17T18:35:36+08:00"
completed_at: "2026-07-17T18:35:37+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_physo_units_constraints_reduce_search_20260716.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_ef99e322cc662cffb7eb5c8f raw_sha256:fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "source:source_b85c7e35189fedbd359efa94 raw_sha256:895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_ef99e322cc662cffb7eb5c8f record_sha256:3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05", "source:source_b85c7e35189fedbd359efa94 record_sha256:b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:ev_388", "evidence:ev_primary_67f24f6c168a", "evidence:ev_primary_d79ac7b3a44d"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:full"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_physo_units_constraints_reduce_search_20260716"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 2 related objects found", "related:source_b85c7e35189fedbd359efa94", "related:source_ef99e322cc662cffb7eb5c8f"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T18:17:30+08:00", "source:source_ef99e322cc662cffb7eb5c8f work_sha256:none", "source:source_b85c7e35189fedbd359efa94 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "95c2c91972e4339acd15c336c6063a342afb20d7cebe841442bfa1731f8fcf4d", "source_state_sha256": "58cd4bbb021cff14051147305b4495e9201ff2bf277cdba72b4c99c5d695f7d0", "source_record_sha256s": {"source_ef99e322cc662cffb7eb5c8f": "3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05", "source_b85c7e35189fedbd359efa94": "b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b"}, "raw_state_sha256": "20a45392bf199765af1f1d6d217a9df88ca64ae57974050913c556c03db386ba", "evidence_sha256": "5573d5c3a3348b162133dcf3420bee47e397c5b706a9aad4688af63a644ad522", "extraction_state_sha256": "92edf289a11d1b6edc212db420455b7f0623d25a8d8158ae2c8ed967d4b3dacf", "work_identity_sha256": "96f9440db83dafd9d2330658730c5fec3c0becd6344a433be8de7eb71954976c", "relation_neighborhood_sha256": "a5713cf3c17da178e61eefc65eaeb599e2c694157ab598e89f9cabbf7497cf09", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_physo_units_constraints_reduce_search_20260716"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "findings": [
        "evidence_entailment:full"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_revalidated": {
      "findings": [
        "evidence:ev_388",
        "evidence:ev_primary_67f24f6c168a",
        "evidence:ev_primary_d79ac7b3a44d"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T18:17:30+08:00",
        "source:source_ef99e322cc662cffb7eb5c8f work_sha256:none",
        "source:source_b85c7e35189fedbd359efa94 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_ef99e322cc662cffb7eb5c8f record_sha256:3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05",
        "source:source_b85c7e35189fedbd359efa94 record_sha256:b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_ef99e322cc662cffb7eb5c8f raw_sha256:fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58",
        "source:source_b85c7e35189fedbd359efa94 raw_sha256:895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 2 related objects found",
        "related:source_b85c7e35189fedbd359efa94",
        "related:source_ef99e322cc662cffb7eb5c8f"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_physo_units_constraints_reduce_search_20260716.md"
      ],
      "status": "passed",
      "warnings": []
    },
    "source_independence_checked": {
      "findings": [
        "distinct_source_ids:2",
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
  "completed_at": "2026-07-17T18:35:37+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "5573d5c3a3348b162133dcf3420bee47e397c5b706a9aad4688af63a644ad522",
    "extraction_state_sha256": "92edf289a11d1b6edc212db420455b7f0623d25a8d8158ae2c8ed967d4b3dacf",
    "memory_schema_version": 2,
    "object_sha256": "95c2c91972e4339acd15c336c6063a342afb20d7cebe841442bfa1731f8fcf4d",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "20a45392bf199765af1f1d6d217a9df88ca64ae57974050913c556c03db386ba",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "a5713cf3c17da178e61eefc65eaeb599e2c694157ab598e89f9cabbf7497cf09",
    "source_record_sha256s": {
      "source_b85c7e35189fedbd359efa94": "b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b",
      "source_ef99e322cc662cffb7eb5c8f": "3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05"
    },
    "source_state_sha256": "58cd4bbb021cff14051147305b4495e9201ff2bf277cdba72b4c99c5d695f7d0",
    "work_identity_sha256": "96f9440db83dafd9d2330658730c5fec3c0becd6344a433be8de7eb71954976c"
  },
  "consolidation_id": "consolidation_783ad0ebfde6fc50e6caceb1",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:37+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_388",
    "ev_primary_67f24f6c168a",
    "ev_primary_d79ac7b3a44d"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_783ad0ebfde6fc50e6caceb1",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_physo_units_constraints_reduce_search_20260716",
  "object_sha256_after": "95c2c91972e4339acd15c336c6063a342afb20d7cebe841442bfa1731f8fcf4d",
  "object_sha256_before": "14e09d6aac3a1064daeeb5cbfc31c301347d7cc85dc3cbaf7eb7da614221243b",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_ef99e322cc662cffb7eb5c8f",
    "source_b85c7e35189fedbd359efa94"
  ],
  "source_records": [
    {
      "raw_content_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58",
      "source_id": "source_ef99e322cc662cffb7eb5c8f",
      "source_record_sha256": "3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05",
      "work_document_sha256": null,
      "work_id": null
    },
    {
      "raw_content_sha256": "895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf",
      "source_id": "source_b85c7e35189fedbd359efa94",
      "source_record_sha256": "b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58",
    "895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf"
  ],
  "started_at": "2026-07-17T18:35:36+08:00",
  "status": "complete",
  "title": "Consolidation: Φ-SO 在生成过程中施加物理单位约束以排除不一致表达式并缩小搜索空间",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:37+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
