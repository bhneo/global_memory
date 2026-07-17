---
id: "consolidation_71634498e11a46f804028359"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 来源原文：[2506.13018] Symmetry in Neural Network Parameter Spaces"
created_at: "2026-07-17T18:35:31+08:00"
updated_at: "2026-07-17T18:35:31+08:00"
consolidation_id: "consolidation_71634498e11a46f804028359"
object_id: "claim_e0bd63c968b13d31416f354b"
object_version_before: 1
object_sha256_before: "fad80df0065d60bfcc2030ef032b5180d538b43bd489b5d7ec94d31ad195c6a4"
object_sha256_after: "8e548f0b42cffe8762ae555fbe6ae51f45a120d230dd793249de77381d0193b0"
source_ids: ["source_6c2de78ee298e83335e3a291"]
source_sha256s: ["99dcc610ff083cc553efe6c61b4ec9492e9919e9cc6b528fc63afa33685a41c8"]
source_records: [{"source_id": "source_6c2de78ee298e83335e3a291", "source_record_sha256": "19b1b2d6b686a47ce80153656388c09f1adbc28a3933c72a22b3f4971747b605", "raw_content_sha256": "99dcc610ff083cc553efe6c61b4ec9492e9919e9cc6b528fc63afa33685a41c8", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["evidence_6d956dcc9a9851436138"]
started_at: "2026-07-17T18:35:30+08:00"
completed_at: "2026-07-17T18:35:31+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_e0bd63c968b13d31416f354b.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_6c2de78ee298e83335e3a291 raw_sha256:99dcc610ff083cc553efe6c61b4ec9492e9919e9cc6b528fc63afa33685a41c8"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_6c2de78ee298e83335e3a291 record_sha256:19b1b2d6b686a47ce80153656388c09f1adbc28a3933c72a22b3f4971747b605"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:evidence_6d956dcc9a9851436138"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:none"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_e0bd63c968b13d31416f354b"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_6c2de78ee298e83335e3a291"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:41+08:00", "source:source_6c2de78ee298e83335e3a291 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "8e548f0b42cffe8762ae555fbe6ae51f45a120d230dd793249de77381d0193b0", "source_state_sha256": "a406652fbda81dfdd03731fb9460f2950d82c29ae4465279ebe9b3fc35e3b9aa", "source_record_sha256s": {"source_6c2de78ee298e83335e3a291": "19b1b2d6b686a47ce80153656388c09f1adbc28a3933c72a22b3f4971747b605"}, "raw_state_sha256": "ee6bb1a5afae9d6b22eb22b4ad6ee0689f82d5ffe4ae3344136d3f51ec94d8c4", "evidence_sha256": "59b3d8c1ba0152dd7d4495d7b5c17728d6c0a532297045823681427cefb647de", "extraction_state_sha256": "dd52b4c3d5bab0ee98487879dca56a429839b38f70af293588641cfda1b435ef", "work_identity_sha256": "8426e890542813a78efd86a5dee0d2115b66e49f85681dd73cac5b2852b7efd4", "relation_neighborhood_sha256": "81ea4c08f9768978e3842f5e7293fed566b16afd73cf1d6be292db21557d1308", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_e0bd63c968b13d31416f354b"
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
        "evidence:evidence_6d956dcc9a9851436138"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:41+08:00",
        "source:source_6c2de78ee298e83335e3a291 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_6c2de78ee298e83335e3a291 record_sha256:19b1b2d6b686a47ce80153656388c09f1adbc28a3933c72a22b3f4971747b605"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_6c2de78ee298e83335e3a291 raw_sha256:99dcc610ff083cc553efe6c61b4ec9492e9919e9cc6b528fc63afa33685a41c8"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_6c2de78ee298e83335e3a291"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_e0bd63c968b13d31416f354b.md"
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
  "completed_at": "2026-07-17T18:35:31+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "59b3d8c1ba0152dd7d4495d7b5c17728d6c0a532297045823681427cefb647de",
    "extraction_state_sha256": "dd52b4c3d5bab0ee98487879dca56a429839b38f70af293588641cfda1b435ef",
    "memory_schema_version": 2,
    "object_sha256": "8e548f0b42cffe8762ae555fbe6ae51f45a120d230dd793249de77381d0193b0",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "ee6bb1a5afae9d6b22eb22b4ad6ee0689f82d5ffe4ae3344136d3f51ec94d8c4",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "81ea4c08f9768978e3842f5e7293fed566b16afd73cf1d6be292db21557d1308",
    "source_record_sha256s": {
      "source_6c2de78ee298e83335e3a291": "19b1b2d6b686a47ce80153656388c09f1adbc28a3933c72a22b3f4971747b605"
    },
    "source_state_sha256": "a406652fbda81dfdd03731fb9460f2950d82c29ae4465279ebe9b3fc35e3b9aa",
    "work_identity_sha256": "8426e890542813a78efd86a5dee0d2115b66e49f85681dd73cac5b2852b7efd4"
  },
  "consolidation_id": "consolidation_71634498e11a46f804028359",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:31+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "evidence_6d956dcc9a9851436138"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_71634498e11a46f804028359",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_e0bd63c968b13d31416f354b",
  "object_sha256_after": "8e548f0b42cffe8762ae555fbe6ae51f45a120d230dd793249de77381d0193b0",
  "object_sha256_before": "fad80df0065d60bfcc2030ef032b5180d538b43bd489b5d7ec94d31ad195c6a4",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_6c2de78ee298e83335e3a291"
  ],
  "source_records": [
    {
      "raw_content_sha256": "99dcc610ff083cc553efe6c61b4ec9492e9919e9cc6b528fc63afa33685a41c8",
      "source_id": "source_6c2de78ee298e83335e3a291",
      "source_record_sha256": "19b1b2d6b686a47ce80153656388c09f1adbc28a3933c72a22b3f4971747b605",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "99dcc610ff083cc553efe6c61b4ec9492e9919e9cc6b528fc63afa33685a41c8"
  ],
  "started_at": "2026-07-17T18:35:30+08:00",
  "status": "complete",
  "title": "Consolidation: 来源原文：[2506.13018] Symmetry in Neural Network Parameter Spaces",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:31+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
