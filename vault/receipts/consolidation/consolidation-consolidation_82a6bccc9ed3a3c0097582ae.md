---
id: "consolidation_82a6bccc9ed3a3c0097582ae"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: Technology 3 University of Science"
created_at: "2026-07-17T18:35:21+08:00"
updated_at: "2026-07-17T18:35:21+08:00"
consolidation_id: "consolidation_82a6bccc9ed3a3c0097582ae"
object_id: "claim_0b690c465600b65a6f2a3652"
object_version_before: 1
object_sha256_before: "0f595381ab055ea18055fb6a80f9dbe006a8746fe9cfd1c1bebae085a2f5d817"
object_sha256_after: "20eda0d3fbfdd32d95ec08b28e33906c8da7a30455968af4801491016b4afdb8"
source_ids: ["source_30d6af4423a7ecb5e51c4a08"]
source_sha256s: ["0e115846512fe0242569c86bef41cb1d7c28064d769f0194cafe7b524bbf4fbe"]
source_records: [{"source_id": "source_30d6af4423a7ecb5e51c4a08", "source_record_sha256": "b808925258cf54f09f3f8b7b689241d0c996c0fb022386592de8dcc809a719a9", "raw_content_sha256": "0e115846512fe0242569c86bef41cb1d7c28064d769f0194cafe7b524bbf4fbe", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["evidence_8bf6abb3b14efa201760"]
started_at: "2026-07-17T18:35:20+08:00"
completed_at: "2026-07-17T18:35:21+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_0b690c465600b65a6f2a3652.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_30d6af4423a7ecb5e51c4a08 raw_sha256:0e115846512fe0242569c86bef41cb1d7c28064d769f0194cafe7b524bbf4fbe"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_30d6af4423a7ecb5e51c4a08 record_sha256:b808925258cf54f09f3f8b7b689241d0c996c0fb022386592de8dcc809a719a9"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:evidence_8bf6abb3b14efa201760"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:none"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_0b690c465600b65a6f2a3652"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_30d6af4423a7ecb5e51c4a08"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:34+08:00", "source:source_30d6af4423a7ecb5e51c4a08 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "20eda0d3fbfdd32d95ec08b28e33906c8da7a30455968af4801491016b4afdb8", "source_state_sha256": "624aa857c463f2c81e9687651c77b21cacc2457f4e1b38b2c8d1ff767ddd68af", "source_record_sha256s": {"source_30d6af4423a7ecb5e51c4a08": "b808925258cf54f09f3f8b7b689241d0c996c0fb022386592de8dcc809a719a9"}, "raw_state_sha256": "ee11d970f3d02bd9b3d10bf67157daf457ec644becb07d7fe3d9fd71caaa3f3a", "evidence_sha256": "19097ce6a09c4f20a851c1f1b73706e12f17b576b44f13137025ec2c38c9711d", "extraction_state_sha256": "12bc5cec98a29c1f7b55af3abbdd9c04b8911461795fd9a61c2b75359f0bd9c8", "work_identity_sha256": "0ea67f87bec951c5becd629a56b3281fbca4c5d7cee676b2649d9edb2a306ab6", "relation_neighborhood_sha256": "4349152256f443b9c0b85e53ad6549c7f5fb2fe3298b476e051a01d2fd5c1563", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_0b690c465600b65a6f2a3652"
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
        "evidence:evidence_8bf6abb3b14efa201760"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:34+08:00",
        "source:source_30d6af4423a7ecb5e51c4a08 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_30d6af4423a7ecb5e51c4a08 record_sha256:b808925258cf54f09f3f8b7b689241d0c996c0fb022386592de8dcc809a719a9"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_30d6af4423a7ecb5e51c4a08 raw_sha256:0e115846512fe0242569c86bef41cb1d7c28064d769f0194cafe7b524bbf4fbe"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_30d6af4423a7ecb5e51c4a08"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_0b690c465600b65a6f2a3652.md"
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
  "completed_at": "2026-07-17T18:35:21+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "19097ce6a09c4f20a851c1f1b73706e12f17b576b44f13137025ec2c38c9711d",
    "extraction_state_sha256": "12bc5cec98a29c1f7b55af3abbdd9c04b8911461795fd9a61c2b75359f0bd9c8",
    "memory_schema_version": 2,
    "object_sha256": "20eda0d3fbfdd32d95ec08b28e33906c8da7a30455968af4801491016b4afdb8",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "ee11d970f3d02bd9b3d10bf67157daf457ec644becb07d7fe3d9fd71caaa3f3a",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "4349152256f443b9c0b85e53ad6549c7f5fb2fe3298b476e051a01d2fd5c1563",
    "source_record_sha256s": {
      "source_30d6af4423a7ecb5e51c4a08": "b808925258cf54f09f3f8b7b689241d0c996c0fb022386592de8dcc809a719a9"
    },
    "source_state_sha256": "624aa857c463f2c81e9687651c77b21cacc2457f4e1b38b2c8d1ff767ddd68af",
    "work_identity_sha256": "0ea67f87bec951c5becd629a56b3281fbca4c5d7cee676b2649d9edb2a306ab6"
  },
  "consolidation_id": "consolidation_82a6bccc9ed3a3c0097582ae",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:21+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "evidence_8bf6abb3b14efa201760"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_82a6bccc9ed3a3c0097582ae",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_0b690c465600b65a6f2a3652",
  "object_sha256_after": "20eda0d3fbfdd32d95ec08b28e33906c8da7a30455968af4801491016b4afdb8",
  "object_sha256_before": "0f595381ab055ea18055fb6a80f9dbe006a8746fe9cfd1c1bebae085a2f5d817",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_30d6af4423a7ecb5e51c4a08"
  ],
  "source_records": [
    {
      "raw_content_sha256": "0e115846512fe0242569c86bef41cb1d7c28064d769f0194cafe7b524bbf4fbe",
      "source_id": "source_30d6af4423a7ecb5e51c4a08",
      "source_record_sha256": "b808925258cf54f09f3f8b7b689241d0c996c0fb022386592de8dcc809a719a9",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "0e115846512fe0242569c86bef41cb1d7c28064d769f0194cafe7b524bbf4fbe"
  ],
  "started_at": "2026-07-17T18:35:20+08:00",
  "status": "complete",
  "title": "Consolidation: Technology 3 University of Science",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:21+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
