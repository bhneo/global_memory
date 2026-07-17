---
id: "consolidation_8d0e0b2ed0a07246fe8f2a9a"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 来源原文：[2303.03192] Deep symbolic regression for physics guided by units constraints: t"
created_at: "2026-07-17T18:35:33+08:00"
updated_at: "2026-07-17T18:35:33+08:00"
consolidation_id: "consolidation_8d0e0b2ed0a07246fe8f2a9a"
object_id: "claim_fdabd7e1d00b7d7dc9352297"
object_version_before: 1
object_sha256_before: "ad3ce0840c16fba2b719fa3dd3e05473a5313499100683de263ee86aed81d24b"
object_sha256_after: "864b57478dc6e1c87f79b1d67464b07d7492b445689e77765aacc6614fe87311"
source_ids: ["source_7800c747533d774786595ef7"]
source_sha256s: ["c762318b4677a679bc40c3a42bad294a779b99c1a0ca21fe5e09c29f6e823e0c"]
source_records: [{"source_id": "source_7800c747533d774786595ef7", "source_record_sha256": "7c6e0affeb53d8ff8b9568762a7001b2621c4098cef5d0283a4c1b6e03f4e737", "raw_content_sha256": "c762318b4677a679bc40c3a42bad294a779b99c1a0ca21fe5e09c29f6e823e0c", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["evidence_ba99c9b0a106cb0bf5cf"]
started_at: "2026-07-17T18:35:33+08:00"
completed_at: "2026-07-17T18:35:33+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_fdabd7e1d00b7d7dc9352297.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_7800c747533d774786595ef7 raw_sha256:c762318b4677a679bc40c3a42bad294a779b99c1a0ca21fe5e09c29f6e823e0c"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_7800c747533d774786595ef7 record_sha256:7c6e0affeb53d8ff8b9568762a7001b2621c4098cef5d0283a4c1b6e03f4e737"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:evidence_ba99c9b0a106cb0bf5cf"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:none"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_fdabd7e1d00b7d7dc9352297"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_7800c747533d774786595ef7"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:44+08:00", "source:source_7800c747533d774786595ef7 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "864b57478dc6e1c87f79b1d67464b07d7492b445689e77765aacc6614fe87311", "source_state_sha256": "968aac85a9620d63f538ba1fc91c8db18a4f5f595ab0a9706264d7e0107eb3a0", "source_record_sha256s": {"source_7800c747533d774786595ef7": "7c6e0affeb53d8ff8b9568762a7001b2621c4098cef5d0283a4c1b6e03f4e737"}, "raw_state_sha256": "023767a1ccdc82a76f968334770d18e6bc891ed81a53c3ca895adeaa11c235f1", "evidence_sha256": "794af27f7011e1e47f381c042889ac6d3135c9b181bf0a72d8838aa38b671f14", "extraction_state_sha256": "027d9fdfca86c8d89513d5211f507133c295063b0348bad08d04ef0f828f124a", "work_identity_sha256": "df70ceb78ffe8d3af4031e7f6af97dedd9ed141b701867e2e288bf547e806448", "relation_neighborhood_sha256": "d6d955a5466fd59b2590b72c1bdc1eb5cdbc5c5fa64d53bce7a5e071f6fe3625", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_fdabd7e1d00b7d7dc9352297"
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
        "evidence:evidence_ba99c9b0a106cb0bf5cf"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:44+08:00",
        "source:source_7800c747533d774786595ef7 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_7800c747533d774786595ef7 record_sha256:7c6e0affeb53d8ff8b9568762a7001b2621c4098cef5d0283a4c1b6e03f4e737"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_7800c747533d774786595ef7 raw_sha256:c762318b4677a679bc40c3a42bad294a779b99c1a0ca21fe5e09c29f6e823e0c"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_7800c747533d774786595ef7"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_fdabd7e1d00b7d7dc9352297.md"
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
  "completed_at": "2026-07-17T18:35:33+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "794af27f7011e1e47f381c042889ac6d3135c9b181bf0a72d8838aa38b671f14",
    "extraction_state_sha256": "027d9fdfca86c8d89513d5211f507133c295063b0348bad08d04ef0f828f124a",
    "memory_schema_version": 2,
    "object_sha256": "864b57478dc6e1c87f79b1d67464b07d7492b445689e77765aacc6614fe87311",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "023767a1ccdc82a76f968334770d18e6bc891ed81a53c3ca895adeaa11c235f1",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "d6d955a5466fd59b2590b72c1bdc1eb5cdbc5c5fa64d53bce7a5e071f6fe3625",
    "source_record_sha256s": {
      "source_7800c747533d774786595ef7": "7c6e0affeb53d8ff8b9568762a7001b2621c4098cef5d0283a4c1b6e03f4e737"
    },
    "source_state_sha256": "968aac85a9620d63f538ba1fc91c8db18a4f5f595ab0a9706264d7e0107eb3a0",
    "work_identity_sha256": "df70ceb78ffe8d3af4031e7f6af97dedd9ed141b701867e2e288bf547e806448"
  },
  "consolidation_id": "consolidation_8d0e0b2ed0a07246fe8f2a9a",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:33+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "evidence_ba99c9b0a106cb0bf5cf"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_8d0e0b2ed0a07246fe8f2a9a",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_fdabd7e1d00b7d7dc9352297",
  "object_sha256_after": "864b57478dc6e1c87f79b1d67464b07d7492b445689e77765aacc6614fe87311",
  "object_sha256_before": "ad3ce0840c16fba2b719fa3dd3e05473a5313499100683de263ee86aed81d24b",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_7800c747533d774786595ef7"
  ],
  "source_records": [
    {
      "raw_content_sha256": "c762318b4677a679bc40c3a42bad294a779b99c1a0ca21fe5e09c29f6e823e0c",
      "source_id": "source_7800c747533d774786595ef7",
      "source_record_sha256": "7c6e0affeb53d8ff8b9568762a7001b2621c4098cef5d0283a4c1b6e03f4e737",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "c762318b4677a679bc40c3a42bad294a779b99c1a0ca21fe5e09c29f6e823e0c"
  ],
  "started_at": "2026-07-17T18:35:33+08:00",
  "status": "complete",
  "title": "Consolidation: 来源原文：[2303.03192] Deep symbolic regression for physics guided by units constraints: t",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:33+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
