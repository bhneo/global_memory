---
id: "consolidation_c78a4dc2236b4fee70bf276d"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 该文称边界 double trace deformation 可引入负能量流，使原本不可穿越的 ER 桥变为可穿越"
created_at: "2026-07-17T18:35:41+08:00"
updated_at: "2026-07-17T18:35:41+08:00"
consolidation_id: "consolidation_c78a4dc2236b4fee70bf276d"
object_id: "claim_wechat_double_trace_traversable_20260715"
object_version_before: 1
object_sha256_before: "72e0e81f2412308a26ddb54ae32ff6dc80a59683d2fb4c5f985e4867a18f7494"
object_sha256_after: "27ae7a4efeccaee9c485a6df55bb8d273b7754d31d2ccdc171bff8f037cacd4c"
source_ids: ["source_647ffb9287507f806c354670"]
source_sha256s: ["ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0"]
source_records: [{"source_id": "source_647ffb9287507f806c354670", "source_record_sha256": "7c8c3d3a8fc4e730929d2b87cec14c4637e43b064c18737693b751932b033232", "raw_content_sha256": "ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_2945", "ev_3121"]
started_at: "2026-07-17T18:35:40+08:00"
completed_at: "2026-07-17T18:35:41+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_wechat_double_trace_traversable_20260715.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_647ffb9287507f806c354670 raw_sha256:ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_647ffb9287507f806c354670 record_sha256:7c8c3d3a8fc4e730929d2b87cec14c4637e43b064c18737693b751932b033232"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:ev_2945", "evidence:ev_3121"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:partial"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_wechat_double_trace_traversable_20260715"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_647ffb9287507f806c354670"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:48+08:00", "source:source_647ffb9287507f806c354670 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "27ae7a4efeccaee9c485a6df55bb8d273b7754d31d2ccdc171bff8f037cacd4c", "source_state_sha256": "c5899ad32de2f2f055a14d2af8d67c94c77cdaf0e23c5f25f37fe7c872523659", "source_record_sha256s": {"source_647ffb9287507f806c354670": "7c8c3d3a8fc4e730929d2b87cec14c4637e43b064c18737693b751932b033232"}, "raw_state_sha256": "0b1b2aca9a2c2a1aa9f523b8d0a499e15cd9ce37bec4d791c93ee6203e292e7d", "evidence_sha256": "0b3373f8c1c9d4fb6e809bc7d2065a616e3c17c0b804343944ed52941c95b984", "extraction_state_sha256": "7b3ef76d5b13e896c1224044fb5d78c7475b45abc0c3fad56817b80c80eb5dc9", "work_identity_sha256": "835742514231fb97b6c04de1ebecfed6ae9010d4fc6804050d810a4cdc6145aa", "relation_neighborhood_sha256": "13e7a522505f3c9e4d6b00e5fd355978eda35a51677e8e8ec4b2c65d0a8102f9", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_wechat_double_trace_traversable_20260715"
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
        "evidence:ev_2945",
        "evidence:ev_3121"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:48+08:00",
        "source:source_647ffb9287507f806c354670 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_647ffb9287507f806c354670 record_sha256:7c8c3d3a8fc4e730929d2b87cec14c4637e43b064c18737693b751932b033232"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_647ffb9287507f806c354670 raw_sha256:ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_647ffb9287507f806c354670"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_wechat_double_trace_traversable_20260715.md"
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
  "completed_at": "2026-07-17T18:35:41+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "0b3373f8c1c9d4fb6e809bc7d2065a616e3c17c0b804343944ed52941c95b984",
    "extraction_state_sha256": "7b3ef76d5b13e896c1224044fb5d78c7475b45abc0c3fad56817b80c80eb5dc9",
    "memory_schema_version": 2,
    "object_sha256": "27ae7a4efeccaee9c485a6df55bb8d273b7754d31d2ccdc171bff8f037cacd4c",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "0b1b2aca9a2c2a1aa9f523b8d0a499e15cd9ce37bec4d791c93ee6203e292e7d",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "13e7a522505f3c9e4d6b00e5fd355978eda35a51677e8e8ec4b2c65d0a8102f9",
    "source_record_sha256s": {
      "source_647ffb9287507f806c354670": "7c8c3d3a8fc4e730929d2b87cec14c4637e43b064c18737693b751932b033232"
    },
    "source_state_sha256": "c5899ad32de2f2f055a14d2af8d67c94c77cdaf0e23c5f25f37fe7c872523659",
    "work_identity_sha256": "835742514231fb97b6c04de1ebecfed6ae9010d4fc6804050d810a4cdc6145aa"
  },
  "consolidation_id": "consolidation_c78a4dc2236b4fee70bf276d",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:41+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_2945",
    "ev_3121"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_c78a4dc2236b4fee70bf276d",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_wechat_double_trace_traversable_20260715",
  "object_sha256_after": "27ae7a4efeccaee9c485a6df55bb8d273b7754d31d2ccdc171bff8f037cacd4c",
  "object_sha256_before": "72e0e81f2412308a26ddb54ae32ff6dc80a59683d2fb4c5f985e4867a18f7494",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_647ffb9287507f806c354670"
  ],
  "source_records": [
    {
      "raw_content_sha256": "ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0",
      "source_id": "source_647ffb9287507f806c354670",
      "source_record_sha256": "7c8c3d3a8fc4e730929d2b87cec14c4637e43b064c18737693b751932b033232",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0"
  ],
  "started_at": "2026-07-17T18:35:40+08:00",
  "status": "complete",
  "title": "Consolidation: 该文称边界 double trace deformation 可引入负能量流，使原本不可穿越的 ER 桥变为可穿越",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:41+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
