---
id: "consolidation_cb307d1848b21177548390b2"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 该文称哥德尔第一不完全性定理表明：在《数学原理》体系中存在既不可证也不可否的佩亚诺算术命题"
created_at: "2026-07-17T18:35:45+08:00"
updated_at: "2026-07-17T18:35:45+08:00"
consolidation_id: "consolidation_cb307d1848b21177548390b2"
object_id: "claim_wechat_godel_first_incompleteness_20260716"
object_version_before: 1
object_sha256_before: "8f289d082110dd2ac784d2a1fce4cf0b8ccc0384f3b0d9debf1a551721087c05"
object_sha256_after: "5614e8da3b5ed660647ab70698110112d96f951c1e04458ff6612b8c22b0964b"
source_ids: ["source_aff280ea206f7233b98afc6a"]
source_sha256s: ["c4575ab201d9c39112ec6245ab3b56aaa66637b5c0ef3db241f7aaac816400f7"]
source_records: [{"source_id": "source_aff280ea206f7233b98afc6a", "source_record_sha256": "c993ca4786e90ae1258bfbcbe4cc50eb2cd8f8e43397fe687d26ad8ec5708956", "raw_content_sha256": "c4575ab201d9c39112ec6245ab3b56aaa66637b5c0ef3db241f7aaac816400f7", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_1527", "ev_1443"]
started_at: "2026-07-17T18:35:45+08:00"
completed_at: "2026-07-17T18:35:45+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_wechat_godel_first_incompleteness_20260716.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_aff280ea206f7233b98afc6a raw_sha256:c4575ab201d9c39112ec6245ab3b56aaa66637b5c0ef3db241f7aaac816400f7"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_aff280ea206f7233b98afc6a record_sha256:c993ca4786e90ae1258bfbcbe4cc50eb2cd8f8e43397fe687d26ad8ec5708956"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:ev_1527", "evidence:ev_1443"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:partial"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_wechat_godel_first_incompleteness_20260716"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_aff280ea206f7233b98afc6a"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:52+08:00", "source:source_aff280ea206f7233b98afc6a work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "5614e8da3b5ed660647ab70698110112d96f951c1e04458ff6612b8c22b0964b", "source_state_sha256": "e1bf9fe24447f9ad45fe56250440cfb055ec6753578c33f5b359944494802ecf", "source_record_sha256s": {"source_aff280ea206f7233b98afc6a": "c993ca4786e90ae1258bfbcbe4cc50eb2cd8f8e43397fe687d26ad8ec5708956"}, "raw_state_sha256": "1359e4777fc4461e462a581e81762f65b5f7611fded1ef0c1373a5a7db70f9f2", "evidence_sha256": "0f4a5796b5707e5d8a58c0c548288e5f51fae35e8decc7dad78f6770adac490f", "extraction_state_sha256": "ce64a7985d521e51915c156cbb7f512d627d6dc9b3299cb08501b2c8da7a967c", "work_identity_sha256": "bf7b401911650d0ef8f41fec35a29e443ae3a87e63fa6d51f74fefad46ca09bb", "relation_neighborhood_sha256": "f702b0c0713851001828ed1ca025981cf89cbbf36b605f3bfb003c9d7d361f5b", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_wechat_godel_first_incompleteness_20260716"
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
        "evidence:ev_1527",
        "evidence:ev_1443"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:52+08:00",
        "source:source_aff280ea206f7233b98afc6a work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_aff280ea206f7233b98afc6a record_sha256:c993ca4786e90ae1258bfbcbe4cc50eb2cd8f8e43397fe687d26ad8ec5708956"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_aff280ea206f7233b98afc6a raw_sha256:c4575ab201d9c39112ec6245ab3b56aaa66637b5c0ef3db241f7aaac816400f7"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_aff280ea206f7233b98afc6a"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_wechat_godel_first_incompleteness_20260716.md"
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
  "completed_at": "2026-07-17T18:35:45+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "0f4a5796b5707e5d8a58c0c548288e5f51fae35e8decc7dad78f6770adac490f",
    "extraction_state_sha256": "ce64a7985d521e51915c156cbb7f512d627d6dc9b3299cb08501b2c8da7a967c",
    "memory_schema_version": 2,
    "object_sha256": "5614e8da3b5ed660647ab70698110112d96f951c1e04458ff6612b8c22b0964b",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "1359e4777fc4461e462a581e81762f65b5f7611fded1ef0c1373a5a7db70f9f2",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "f702b0c0713851001828ed1ca025981cf89cbbf36b605f3bfb003c9d7d361f5b",
    "source_record_sha256s": {
      "source_aff280ea206f7233b98afc6a": "c993ca4786e90ae1258bfbcbe4cc50eb2cd8f8e43397fe687d26ad8ec5708956"
    },
    "source_state_sha256": "e1bf9fe24447f9ad45fe56250440cfb055ec6753578c33f5b359944494802ecf",
    "work_identity_sha256": "bf7b401911650d0ef8f41fec35a29e443ae3a87e63fa6d51f74fefad46ca09bb"
  },
  "consolidation_id": "consolidation_cb307d1848b21177548390b2",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:45+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_1527",
    "ev_1443"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_cb307d1848b21177548390b2",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_wechat_godel_first_incompleteness_20260716",
  "object_sha256_after": "5614e8da3b5ed660647ab70698110112d96f951c1e04458ff6612b8c22b0964b",
  "object_sha256_before": "8f289d082110dd2ac784d2a1fce4cf0b8ccc0384f3b0d9debf1a551721087c05",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_aff280ea206f7233b98afc6a"
  ],
  "source_records": [
    {
      "raw_content_sha256": "c4575ab201d9c39112ec6245ab3b56aaa66637b5c0ef3db241f7aaac816400f7",
      "source_id": "source_aff280ea206f7233b98afc6a",
      "source_record_sha256": "c993ca4786e90ae1258bfbcbe4cc50eb2cd8f8e43397fe687d26ad8ec5708956",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "c4575ab201d9c39112ec6245ab3b56aaa66637b5c0ef3db241f7aaac816400f7"
  ],
  "started_at": "2026-07-17T18:35:45+08:00",
  "status": "complete",
  "title": "Consolidation: 该文称哥德尔第一不完全性定理表明：在《数学原理》体系中存在既不可证也不可否的佩亚诺算术命题",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:45+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
