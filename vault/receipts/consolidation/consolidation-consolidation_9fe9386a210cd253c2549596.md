---
id: "consolidation_9fe9386a210cd253c2549596"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: Φ-SO 使用深度强化学习训练 RNN 生成符号表达式"
created_at: "2026-07-17T18:37:21+08:00"
updated_at: "2026-07-17T18:37:21+08:00"
consolidation_id: "consolidation_9fe9386a210cd253c2549596"
object_id: "claim_physo_rnn_reinforcement_learning_method_20260716"
object_version_before: 1
object_sha256_before: "3487b6dcfc19cf9d63e38a7f29fe83b0bdcbfb7f022a332a8421ef9c620e63a3"
object_sha256_after: "94aaa9385b3cd8ca78c9e16cb3a07e4dc61e8aaf2106af3393ce3ac73680029a"
source_ids: ["source_ef99e322cc662cffb7eb5c8f", "source_b85c7e35189fedbd359efa94"]
source_sha256s: ["fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf"]
source_records: [{"source_id": "source_ef99e322cc662cffb7eb5c8f", "source_record_sha256": "3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05", "raw_content_sha256": "fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "work_id": null, "work_document_sha256": null}, {"source_id": "source_b85c7e35189fedbd359efa94", "source_record_sha256": "b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b", "raw_content_sha256": "895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_290", "ev_primary_2e7e308b02a1"]
started_at: "2026-07-17T18:37:20+08:00"
completed_at: "2026-07-17T18:37:21+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_physo_rnn_reinforcement_learning_method_20260716.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_ef99e322cc662cffb7eb5c8f raw_sha256:fb4eb39bc16a2dd15c6be6bb31fd72c68e487060c4ac35e0af4ff8fab180fc58", "source:source_b85c7e35189fedbd359efa94 raw_sha256:895c64ddb9204adf2853a7feb87d4315de7bdc656230361c5dc5ee249d4481bf"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_ef99e322cc662cffb7eb5c8f record_sha256:3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05", "source:source_b85c7e35189fedbd359efa94 record_sha256:b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:ev_290", "evidence:ev_primary_2e7e308b02a1"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:full"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_physo_rnn_reinforcement_learning_method_20260716"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 2 related objects found", "related:source_b85c7e35189fedbd359efa94", "related:source_ef99e322cc662cffb7eb5c8f"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T18:37:14+08:00", "source:source_ef99e322cc662cffb7eb5c8f work_sha256:none", "source:source_b85c7e35189fedbd359efa94 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "94aaa9385b3cd8ca78c9e16cb3a07e4dc61e8aaf2106af3393ce3ac73680029a", "source_state_sha256": "58cd4bbb021cff14051147305b4495e9201ff2bf277cdba72b4c99c5d695f7d0", "source_record_sha256s": {"source_ef99e322cc662cffb7eb5c8f": "3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05", "source_b85c7e35189fedbd359efa94": "b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b"}, "raw_state_sha256": "20a45392bf199765af1f1d6d217a9df88ca64ae57974050913c556c03db386ba", "evidence_sha256": "42b7334878c0b581d95008b77e2e9768ebc5f634db268d198357456019c95e2f", "extraction_state_sha256": "88e04fc412525dc81f57a25fce058da1823b7866436f079f8a7b328522e4a025", "work_identity_sha256": "96f9440db83dafd9d2330658730c5fec3c0becd6344a433be8de7eb71954976c", "relation_neighborhood_sha256": "4c3814f436d9300315d69241102f94de1aeefddd4d4ec416116aa099ded6295c", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "requalified"
changes: []
change_summary: "Trusted memory qualified under trusted-promotion-v3-receipt-v2"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "Trusted memory qualified under trusted-promotion-v3-receipt-v2",
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
        "candidate:claim_physo_rnn_reinforcement_learning_method_20260716"
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
        "evidence:ev_290",
        "evidence:ev_primary_2e7e308b02a1"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T18:37:14+08:00",
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
        "validated:vault/memory/claim/claim_physo_rnn_reinforcement_learning_method_20260716.md"
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
  "completed_at": "2026-07-17T18:37:21+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "42b7334878c0b581d95008b77e2e9768ebc5f634db268d198357456019c95e2f",
    "extraction_state_sha256": "88e04fc412525dc81f57a25fce058da1823b7866436f079f8a7b328522e4a025",
    "memory_schema_version": 2,
    "object_sha256": "94aaa9385b3cd8ca78c9e16cb3a07e4dc61e8aaf2106af3393ce3ac73680029a",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "20a45392bf199765af1f1d6d217a9df88ca64ae57974050913c556c03db386ba",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "4c3814f436d9300315d69241102f94de1aeefddd4d4ec416116aa099ded6295c",
    "source_record_sha256s": {
      "source_b85c7e35189fedbd359efa94": "b8b0af2b68621857fea9a501d7608d269d759bf3d523039b4fdd62a9fd92bf4b",
      "source_ef99e322cc662cffb7eb5c8f": "3d4180a2498fc9e5d66b6bc15fcfe0b6787571c8cc22b765d04d09e4a89b3f05"
    },
    "source_state_sha256": "58cd4bbb021cff14051147305b4495e9201ff2bf277cdba72b4c99c5d695f7d0",
    "work_identity_sha256": "96f9440db83dafd9d2330658730c5fec3c0becd6344a433be8de7eb71954976c"
  },
  "consolidation_id": "consolidation_9fe9386a210cd253c2549596",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:37:21+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_290",
    "ev_primary_2e7e308b02a1"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_9fe9386a210cd253c2549596",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_physo_rnn_reinforcement_learning_method_20260716",
  "object_sha256_after": "94aaa9385b3cd8ca78c9e16cb3a07e4dc61e8aaf2106af3393ce3ac73680029a",
  "object_sha256_before": "3487b6dcfc19cf9d63e38a7f29fe83b0bdcbfb7f022a332a8421ef9c620e63a3",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "requalified",
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
  "started_at": "2026-07-17T18:37:20+08:00",
  "status": "complete",
  "title": "Consolidation: Φ-SO 使用深度强化学习训练 RNN 生成符号表达式",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:37:21+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
