---
id: "consolidation_d7cd7d382e58bbb22f7f07a4"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: Φ-SO 在生成过程中施加物理单位约束以排除不一致表达式并缩小搜索空间"
created_at: "2026-07-17T22:39:59+08:00"
updated_at: "2026-07-17T22:39:59+08:00"
consolidation_id: "consolidation_d7cd7d382e58bbb22f7f07a4"
object_id: "claim_physo_units_constraints_reduce_search_20260716"
object_version_before: 1
object_sha256_before: "d8b64159dd0dfb69c6c5756352962d0cc8f4935b129fce85e4d8b63599cfec75"
object_sha256_after: "cd96fdc6933400df363a3457037384a6205aa655bbb543fdf46d09e934028ed7"
source_ids: ["source_ef99e322cc662cffb7eb5c8f", "source_b85c7e35189fedbd359efa94"]
source_sha256s: ["fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf"]
source_records: [{"source_id": "source_ef99e322cc662cffb7eb5c8f", "source_record_sha256": "3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05", "raw_content_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "work_id": null, "work_document_sha256": null}, {"source_id": "source_b85c7e35189fedbd359efa94", "source_record_sha256": "b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b", "raw_content_sha256": "895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_388", "ev_primary_67f24f6c168a", "ev_primary_d79ac7b3a44d"]
started_at: "2026-07-17T22:39:58+08:00"
completed_at: "2026-07-17T22:39:59+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/claim/claim_physo_units_constraints_reduce_search_20260716.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_ef99e322cc662cffb7eb5c8f raw_sha256:fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "source:source_b85c7e35189fedbd359efa94 raw_sha256:895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_ef99e322cc662cffb7eb5c8f record_sha256:3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05", "source:source_b85c7e35189fedbd359efa94 record_sha256:b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["evidence:ev_388", "evidence:ev_primary_67f24f6c168a", "evidence:ev_primary_d79ac7b3a44d"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "passed", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": "full", "findings": ["evidence_entailment:full"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:claim_physo_units_constraints_reduce_search_20260716"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_b85c7e35189fedbd359efa94", "related:source_ef99e322cc662cffb7eb5c8f"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T18:38:06+08:00", "source:source_ef99e322cc662cffb7eb5c8f work_sha256:none", "source:source_b85c7e35189fedbd359efa94 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "cd96fdc6933400df363a3457037384a6205aa655bbb543fdf46d09e934028ed7", "source_state_sha256": "58cd4bbb021cff14051147305b4495e9201ff2bf277cdba72b4c99c5d695f7d0", "source_record_sha256s": {"source_ef99e322cc662cffb7eb5c8f": "3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05", "source_b85c7e35189fedbd359efa94": "b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b"}, "raw_state_sha256": "20a45392bf199765af1f1d6d217a9df88ca64ae57974050913c556c03db386ba", "evidence_sha256": "5573d5c3a3348b162133dcf3420bee47e397c5b706a9aad4688af63a644ad522", "extraction_state_sha256": "92edf289a11d1b6edc212db420455b7f0623d25a8d8158ae2c8ed967d4b3dacf", "work_identity_sha256": "96f9440db83dafd9d2330658730c5fec3c0becd6344a433be8de7eb71954976c", "relation_fingerprint": {"outgoing_relations_sha256": "821a92680c07888258dad8a20c3bf9888f5d7ad697ccaa7ad5a6a0226f6a0729", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "821a92680c07888258dad8a20c3bf9888f5d7ad697ccaa7ad5a6a0226f6a0729"}, "relation_neighborhood_sha256": "821a92680c07888258dad8a20c3bf9888f5d7ad697ccaa7ad5a6a0226f6a0729", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "requalification_candidate"
changes: []
change_summary: "Receipt v2 revalidated under incoming and outgoing relation fingerprint boundary"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "Receipt v2 revalidated under incoming and outgoing relation fingerprint boundary",
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
        "candidate:claim_physo_units_constraints_reduce_search_20260716"
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
        "evidence:ev_388",
        "evidence:ev_primary_67f24f6c168a",
        "evidence:ev_primary_d79ac7b3a44d"
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
        "object_updated_at:2026-07-17T18:38:06+08:00",
        "source:source_ef99e322cc662cffb7eb5c8f work_sha256:none",
        "source:source_b85c7e35189fedbd359efa94 work_sha256:none"
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
        "source:source_ef99e322cc662cffb7eb5c8f record_sha256:3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05",
        "source:source_b85c7e35189fedbd359efa94 record_sha256:b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b"
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
        "source:source_ef99e322cc662cffb7eb5c8f raw_sha256:fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58",
        "source:source_b85c7e35189fedbd359efa94 raw_sha256:895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf"
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
        "related:source_b85c7e35189fedbd359efa94",
        "related:source_ef99e322cc662cffb7eb5c8f"
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
        "validated:vault/memory/claim/claim_physo_units_constraints_reduce_search_20260716.md"
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
        "distinct_source_ids:2",
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
  "completed_at": "2026-07-17T22:39:59+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "5573d5c3a3348b162133dcf3420bee47e397c5b706a9aad4688af63a644ad522",
    "extraction_state_sha256": "92edf289a11d1b6edc212db420455b7f0623d25a8d8158ae2c8ed967d4b3dacf",
    "memory_schema_version": 2,
    "object_sha256": "cd96fdc6933400df363a3457037384a6205aa655bbb543fdf46d09e934028ed7",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "20a45392bf199765af1f1d6d217a9df88ca64ae57974050913c556c03db386ba",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "821a92680c07888258dad8a20c3bf9888f5d7ad697ccaa7ad5a6a0226f6a0729",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "821a92680c07888258dad8a20c3bf9888f5d7ad697ccaa7ad5a6a0226f6a0729"
    },
    "relation_neighborhood_sha256": "821a92680c07888258dad8a20c3bf9888f5d7ad697ccaa7ad5a6a0226f6a0729",
    "source_record_sha256s": {
      "source_b85c7e35189fedbd359efa94": "b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b",
      "source_ef99e322cc662cffb7eb5c8f": "3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05"
    },
    "source_state_sha256": "58cd4bbb021cff14051147305b4495e9201ff2bf277cdba72b4c99c5d695f7d0",
    "work_identity_sha256": "96f9440db83dafd9d2330658730c5fec3c0becd6344a433be8de7eb71954976c"
  },
  "consolidation_id": "consolidation_d7cd7d382e58bbb22f7f07a4",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-17T22:39:59+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_388",
    "ev_primary_67f24f6c168a",
    "ev_primary_d79ac7b3a44d"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_d7cd7d382e58bbb22f7f07a4",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_physo_units_constraints_reduce_search_20260716",
  "object_sha256_after": "cd96fdc6933400df363a3457037384a6205aa655bbb543fdf46d09e934028ed7",
  "object_sha256_before": "d8b64159dd0dfb69c6c5756352962d0cc8f4935b129fce85e4d8b63599cfec75",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "requalification_candidate",
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
  "started_at": "2026-07-17T22:39:58+08:00",
  "status": "complete",
  "title": "Consolidation: Φ-SO 在生成过程中施加物理单位约束以排除不一致表达式并缩小搜索空间",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T22:39:59+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
