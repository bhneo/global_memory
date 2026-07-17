---
id: "consolidation_58eedcd85602f4b90b73f635"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: “How would j’s action change if I had acted"
created_at: "2026-07-17T18:36:07+08:00"
updated_at: "2026-07-17T18:36:07+08:00"
consolidation_id: "consolidation_58eedcd85602f4b90b73f635"
object_id: "question_1e0121d4bdc2f58cea1ca426"
object_version_before: 1
object_sha256_before: "e7f461925a10156fd2217f0824e1d771bc4de36fdc0a02145dacc721d55a3c91"
object_sha256_after: "361fb80a686470c37eded79fd58e72d5be90ed85f15020b52b5a5699c8484cb9"
source_ids: ["source_c019c0a492cc659d7858134d"]
source_sha256s: ["4192bb78cef1c95a6013d7727d4ff6ced136f66b3ef0ff1870df7054ba6cc92b"]
source_records: [{"source_id": "source_c019c0a492cc659d7858134d", "source_record_sha256": "7064f0be479be1b51928ced60c254ea5396d58da4449dcac25575ae5f38b7283", "raw_content_sha256": "4192bb78cef1c95a6013d7727d4ff6ced136f66b3ef0ff1870df7054ba6cc92b", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-17T18:36:07+08:00"
completed_at: "2026-07-17T18:36:07+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/question/question_1e0121d4bdc2f58cea1ca426.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_c019c0a492cc659d7858134d raw_sha256:4192bb78cef1c95a6013d7727d4ff6ced136f66b3ef0ff1870df7054ba6cc92b"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_c019c0a492cc659d7858134d record_sha256:7064f0be479be1b51928ced60c254ea5396d58da4449dcac25575ae5f38b7283"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:question_1e0121d4bdc2f58cea1ca426"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_c019c0a492cc659d7858134d"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:24:09+08:00", "source:source_c019c0a492cc659d7858134d work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "361fb80a686470c37eded79fd58e72d5be90ed85f15020b52b5a5699c8484cb9", "source_state_sha256": "8a762cbb8c694bfee0d7fd9132ddc79678919843f75b96965842d58e7c2c1d09", "source_record_sha256s": {"source_c019c0a492cc659d7858134d": "7064f0be479be1b51928ced60c254ea5396d58da4449dcac25575ae5f38b7283"}, "raw_state_sha256": "5373f73398109d6084c2cd04097e7da48201bf0d728f17ad923595c6bd6ffa8c", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "8eafd78340cd90be6446049d7e3f8b987ab7a732563865aa09be8a7f8531376f", "relation_neighborhood_sha256": "05a30db249fd335f4f074b25a9a87af9a64e6a22eb35fea7c2d1d1575888052e", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:question_1e0121d4bdc2f58cea1ca426"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "findings": [
        "not applicable for non-claim object"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_revalidated": {
      "findings": [
        "not applicable for non-claim object"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:24:09+08:00",
        "source:source_c019c0a492cc659d7858134d work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_c019c0a492cc659d7858134d record_sha256:7064f0be479be1b51928ced60c254ea5396d58da4449dcac25575ae5f38b7283"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_c019c0a492cc659d7858134d raw_sha256:4192bb78cef1c95a6013d7727d4ff6ced136f66b3ef0ff1870df7054ba6cc92b"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_c019c0a492cc659d7858134d"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/question/question_1e0121d4bdc2f58cea1ca426.md"
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
  "completed_at": "2026-07-17T18:36:07+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "361fb80a686470c37eded79fd58e72d5be90ed85f15020b52b5a5699c8484cb9",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "5373f73398109d6084c2cd04097e7da48201bf0d728f17ad923595c6bd6ffa8c",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "05a30db249fd335f4f074b25a9a87af9a64e6a22eb35fea7c2d1d1575888052e",
    "source_record_sha256s": {
      "source_c019c0a492cc659d7858134d": "7064f0be479be1b51928ced60c254ea5396d58da4449dcac25575ae5f38b7283"
    },
    "source_state_sha256": "8a762cbb8c694bfee0d7fd9132ddc79678919843f75b96965842d58e7c2c1d09",
    "work_identity_sha256": "8eafd78340cd90be6446049d7e3f8b987ab7a732563865aa09be8a7f8531376f"
  },
  "consolidation_id": "consolidation_58eedcd85602f4b90b73f635",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:36:07+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_58eedcd85602f4b90b73f635",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "question_1e0121d4bdc2f58cea1ca426",
  "object_sha256_after": "361fb80a686470c37eded79fd58e72d5be90ed85f15020b52b5a5699c8484cb9",
  "object_sha256_before": "e7f461925a10156fd2217f0824e1d771bc4de36fdc0a02145dacc721d55a3c91",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_c019c0a492cc659d7858134d"
  ],
  "source_records": [
    {
      "raw_content_sha256": "4192bb78cef1c95a6013d7727d4ff6ced136f66b3ef0ff1870df7054ba6cc92b",
      "source_id": "source_c019c0a492cc659d7858134d",
      "source_record_sha256": "7064f0be479be1b51928ced60c254ea5396d58da4449dcac25575ae5f38b7283",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "4192bb78cef1c95a6013d7727d4ff6ced136f66b3ef0ff1870df7054ba6cc92b"
  ],
  "started_at": "2026-07-17T18:36:07+08:00",
  "status": "complete",
  "title": "Consolidation: “How would j’s action change if I had acted",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:36:07+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
