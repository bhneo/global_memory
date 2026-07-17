---
id: "consolidation_1a43d39c3e1d556e9076863b"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 该文定义李群为同时满足群公理、微分流形结构与运算相容性的集合"
created_at: "2026-07-17T18:35:48+08:00"
updated_at: "2026-07-17T18:35:48+08:00"
consolidation_id: "consolidation_1a43d39c3e1d556e9076863b"
object_id: "claim_wechat_lie_group_definition_20260715"
object_version_before: 1
object_sha256_before: "91e33b7e30dfb134d5264648c3085513eddc5cabdd9c5150750539655c60e997"
object_sha256_after: "7deeb6fb80f94049b8f2c64ac9833181f1bc6f8bc09cd5b1fe8debc8f01129c8"
source_ids: ["source_941321d95232028c233c9433"]
source_sha256s: ["8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11"]
source_records: [{"source_id": "source_941321d95232028c233c9433", "source_record_sha256": "4235eb18ab1344c8420e011b715135652f70af5e3bf5b383c55f13c1f6ec3047", "raw_content_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_1682", "ev_1843"]
started_at: "2026-07-17T18:35:47+08:00"
completed_at: "2026-07-17T18:35:48+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_wechat_lie_group_definition_20260715.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_941321d95232028c233c9433 raw_sha256:8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_941321d95232028c233c9433 record_sha256:4235eb18ab1344c8420e011b715135652f70af5e3bf5b383c55f13c1f6ec3047"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:ev_1682", "evidence:ev_1843"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:partial"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_wechat_lie_group_definition_20260715"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_941321d95232028c233c9433"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:55+08:00", "source:source_941321d95232028c233c9433 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "7deeb6fb80f94049b8f2c64ac9833181f1bc6f8bc09cd5b1fe8debc8f01129c8", "source_state_sha256": "7f51d24958aa924cea63d040d5557fd0880382af4654afae991c487c7b162589", "source_record_sha256s": {"source_941321d95232028c233c9433": "4235eb18ab1344c8420e011b715135652f70af5e3bf5b383c55f13c1f6ec3047"}, "raw_state_sha256": "39c4d0b4266a2cc3df4c4344b8434aaa6a165805b1c2d72c342cfdf09f6703eb", "evidence_sha256": "b15d0395a140038de6440c8f6a42875191172ccc2637ffc1b09dc1c7766fe994", "extraction_state_sha256": "5446ed97a9541a95e5e6e613237581ac5ff6ca648e33139354346d8b3444bc71", "work_identity_sha256": "4b365a8eb957ec37c58710a68910b973b403b05ec87eae5a39ac9f24e3e13898", "relation_neighborhood_sha256": "3a69733560e64664e4213eb5c06a3e2aa7d5a088dc613a0a0a5ac6b3074d895a", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_wechat_lie_group_definition_20260715"
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
        "evidence:ev_1682",
        "evidence:ev_1843"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:55+08:00",
        "source:source_941321d95232028c233c9433 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_941321d95232028c233c9433 record_sha256:4235eb18ab1344c8420e011b715135652f70af5e3bf5b383c55f13c1f6ec3047"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_941321d95232028c233c9433 raw_sha256:8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_941321d95232028c233c9433"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_wechat_lie_group_definition_20260715.md"
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
  "completed_at": "2026-07-17T18:35:48+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "b15d0395a140038de6440c8f6a42875191172ccc2637ffc1b09dc1c7766fe994",
    "extraction_state_sha256": "5446ed97a9541a95e5e6e613237581ac5ff6ca648e33139354346d8b3444bc71",
    "memory_schema_version": 2,
    "object_sha256": "7deeb6fb80f94049b8f2c64ac9833181f1bc6f8bc09cd5b1fe8debc8f01129c8",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "39c4d0b4266a2cc3df4c4344b8434aaa6a165805b1c2d72c342cfdf09f6703eb",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "3a69733560e64664e4213eb5c06a3e2aa7d5a088dc613a0a0a5ac6b3074d895a",
    "source_record_sha256s": {
      "source_941321d95232028c233c9433": "4235eb18ab1344c8420e011b715135652f70af5e3bf5b383c55f13c1f6ec3047"
    },
    "source_state_sha256": "7f51d24958aa924cea63d040d5557fd0880382af4654afae991c487c7b162589",
    "work_identity_sha256": "4b365a8eb957ec37c58710a68910b973b403b05ec87eae5a39ac9f24e3e13898"
  },
  "consolidation_id": "consolidation_1a43d39c3e1d556e9076863b",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:48+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_1682",
    "ev_1843"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_1a43d39c3e1d556e9076863b",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_wechat_lie_group_definition_20260715",
  "object_sha256_after": "7deeb6fb80f94049b8f2c64ac9833181f1bc6f8bc09cd5b1fe8debc8f01129c8",
  "object_sha256_before": "91e33b7e30dfb134d5264648c3085513eddc5cabdd9c5150750539655c60e997",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_941321d95232028c233c9433"
  ],
  "source_records": [
    {
      "raw_content_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11",
      "source_id": "source_941321d95232028c233c9433",
      "source_record_sha256": "4235eb18ab1344c8420e011b715135652f70af5e3bf5b383c55f13c1f6ec3047",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11"
  ],
  "started_at": "2026-07-17T18:35:47+08:00",
  "status": "complete",
  "title": "Consolidation: 该文定义李群为同时满足群公理、微分流形结构与运算相容性的集合",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:48+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
