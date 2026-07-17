---
id: "consolidation_120ba4dd41d78d862e43ea4b"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 该文称文本模型与视觉模型随能力增强也呈现更强表征一致性，并以颜色表征与人类感知一致为例"
created_at: "2026-07-17T18:35:40+08:00"
updated_at: "2026-07-17T18:35:40+08:00"
consolidation_id: "consolidation_120ba4dd41d78d862e43ea4b"
object_id: "claim_wechat_cross_modal_representation_alignment_20260716"
object_version_before: 1
object_sha256_before: "443bca677b9a13845ea0edb6d411011568332b12b06b116005a29d4d6e893b5d"
object_sha256_after: "433a20c6fecbae8345e3029eea62acdf59891ab916779f46d0abe92d9dd854af"
source_ids: ["source_f35b44d4bd383fb26ca49165"]
source_sha256s: ["0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0"]
source_records: [{"source_id": "source_f35b44d4bd383fb26ca49165", "source_record_sha256": "2777c09c1825f34dedeccec2459b0dde1dadcb4438f4c616db757bbe4915690b", "raw_content_sha256": "0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_993", "ev_1113"]
started_at: "2026-07-17T18:35:40+08:00"
completed_at: "2026-07-17T18:35:40+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_wechat_cross_modal_representation_alignment_20260716.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_f35b44d4bd383fb26ca49165 raw_sha256:0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_f35b44d4bd383fb26ca49165 record_sha256:2777c09c1825f34dedeccec2459b0dde1dadcb4438f4c616db757bbe4915690b"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:ev_993", "evidence:ev_1113"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:partial"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_wechat_cross_modal_representation_alignment_20260716"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_f35b44d4bd383fb26ca49165"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:48+08:00", "source:source_f35b44d4bd383fb26ca49165 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "433a20c6fecbae8345e3029eea62acdf59891ab916779f46d0abe92d9dd854af", "source_state_sha256": "5bd84ead68360b1c3db470f886b74d62b7aa48115bf0e1721fbb9b4c22d7c45d", "source_record_sha256s": {"source_f35b44d4bd383fb26ca49165": "2777c09c1825f34dedeccec2459b0dde1dadcb4438f4c616db757bbe4915690b"}, "raw_state_sha256": "f51b1090920416fef5b2129c0162814d2e1372539459f733f55527fb2825eeed", "evidence_sha256": "57f74d0ab4ea799162045b0f2bde11412a0b3b7b003eefd5f168fe00bcb55b93", "extraction_state_sha256": "3f77d4f1fe268d88a32e91ccae21286e67f851aee652c899591104ddb79721a2", "work_identity_sha256": "4f6c49f512ab1e26e2274fb0f71d62715a420267809b61d67ce9a65347c7944a", "relation_neighborhood_sha256": "d05116bd282b0a1825fd363bbba7ab79b2028a121a103eeecb6d4bf1d3f7290c", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_wechat_cross_modal_representation_alignment_20260716"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "findings": [
        "evidence_entailment:partial"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_revalidated": {
      "findings": [
        "evidence:ev_993",
        "evidence:ev_1113"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:48+08:00",
        "source:source_f35b44d4bd383fb26ca49165 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_f35b44d4bd383fb26ca49165 record_sha256:2777c09c1825f34dedeccec2459b0dde1dadcb4438f4c616db757bbe4915690b"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_f35b44d4bd383fb26ca49165 raw_sha256:0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_f35b44d4bd383fb26ca49165"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_wechat_cross_modal_representation_alignment_20260716.md"
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
  "completed_at": "2026-07-17T18:35:40+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "57f74d0ab4ea799162045b0f2bde11412a0b3b7b003eefd5f168fe00bcb55b93",
    "extraction_state_sha256": "3f77d4f1fe268d88a32e91ccae21286e67f851aee652c899591104ddb79721a2",
    "memory_schema_version": 2,
    "object_sha256": "433a20c6fecbae8345e3029eea62acdf59891ab916779f46d0abe92d9dd854af",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "f51b1090920416fef5b2129c0162814d2e1372539459f733f55527fb2825eeed",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "d05116bd282b0a1825fd363bbba7ab79b2028a121a103eeecb6d4bf1d3f7290c",
    "source_record_sha256s": {
      "source_f35b44d4bd383fb26ca49165": "2777c09c1825f34dedeccec2459b0dde1dadcb4438f4c616db757bbe4915690b"
    },
    "source_state_sha256": "5bd84ead68360b1c3db470f886b74d62b7aa48115bf0e1721fbb9b4c22d7c45d",
    "work_identity_sha256": "4f6c49f512ab1e26e2274fb0f71d62715a420267809b61d67ce9a65347c7944a"
  },
  "consolidation_id": "consolidation_120ba4dd41d78d862e43ea4b",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:40+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_993",
    "ev_1113"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_120ba4dd41d78d862e43ea4b",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_wechat_cross_modal_representation_alignment_20260716",
  "object_sha256_after": "433a20c6fecbae8345e3029eea62acdf59891ab916779f46d0abe92d9dd854af",
  "object_sha256_before": "443bca677b9a13845ea0edb6d411011568332b12b06b116005a29d4d6e893b5d",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_f35b44d4bd383fb26ca49165"
  ],
  "source_records": [
    {
      "raw_content_sha256": "0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0",
      "source_id": "source_f35b44d4bd383fb26ca49165",
      "source_record_sha256": "2777c09c1825f34dedeccec2459b0dde1dadcb4438f4c616db757bbe4915690b",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0"
  ],
  "started_at": "2026-07-17T18:35:40+08:00",
  "status": "complete",
  "title": "Consolidation: 该文称文本模型与视觉模型随能力增强也呈现更强表征一致性，并以颜色表征与人类感知一致为例",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:40+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
