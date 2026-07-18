---
id: "consolidation_ec6cea055b1ec016767e3caa"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 该文称边界 double trace deformation 可引入负能量流，使原本不可穿越的 ER 桥变为可穿越"
created_at: "2026-07-18T16:02:59+08:00"
updated_at: "2026-07-18T16:02:59+08:00"
consolidation_id: "consolidation_ec6cea055b1ec016767e3caa"
object_id: "claim_wechat_double_trace_traversable_20260715"
object_version_before: 1
object_sha256_before: "27ae7a4efeccaee9c485a6df55bb8d273b7754d31d2ccdc171bff8f037cacd4c"
object_sha256_after: "cc3138280923a59b7733785fddca7995aa0cbd7702a4c3ebff0208d20ba04fc1"
source_ids: ["source_647ffb9287507f806c354670"]
source_sha256s: ["ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0"]
source_records: [{"source_id": "source_647ffb9287507f806c354670", "source_record_sha256": "7c8c3d3a8fc4e730929d2b87cec14c4637e43b064c18737693b751932b033232", "raw_content_sha256": "ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_2945", "ev_3121"]
started_at: "2026-07-18T16:02:58+08:00"
completed_at: "2026-07-18T16:02:59+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/claim/claim_wechat_double_trace_traversable_20260715.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_647ffb9287507f806c354670 raw_sha256:ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_647ffb9287507f806c354670 record_sha256:7c8c3d3a8fc4e730929d2b87cec14c4637e43b064c18737693b751932b033232"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["evidence:ev_2945", "evidence:ev_3121"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "passed", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": "partial", "findings": ["evidence_entailment:partial"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:claim_wechat_double_trace_traversable_20260715"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_647ffb9287507f806c354670"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T18:35:41+08:00", "source:source_647ffb9287507f806c354670 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "cc3138280923a59b7733785fddca7995aa0cbd7702a4c3ebff0208d20ba04fc1", "source_state_sha256": "c5899ad32de2f2f055a14d2af8d67c94c77cdaf0e23c5f25f37fe7c872523659", "source_record_sha256s": {"source_647ffb9287507f806c354670": "7c8c3d3a8fc4e730929d2b87cec14c4637e43b064c18737693b751932b033232"}, "raw_state_sha256": "0b1b2aca9a2c2a1aa9f523b8d0a499e15cd9ce37bec4d791c93ee6203e292e7d", "evidence_sha256": "0b3373f8c1c9d4fb6e809bc7d2065a616e3c17c0b804343944ed52941c95b984", "extraction_state_sha256": "7b3ef76d5b13e896c1224044fb5d78c7475b45abc0c3fad56817b80c80eb5dc9", "work_identity_sha256": "835742514231fb97b6c04de1ebecfed6ae9010d4fc6804050d810a4cdc6145aa", "relation_fingerprint": {"outgoing_relations_sha256": "72ce2b47affc606dba97fa07f9984627902c9e8d1ea6ae5b1f19fabbdb146a35", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "72ce2b47affc606dba97fa07f9984627902c9e8d1ea6ae5b1f19fabbdb146a35"}, "relation_neighborhood_sha256": "72ce2b47affc606dba97fa07f9984627902c9e8d1ea6ae5b1f19fabbdb146a35", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_wechat_double_trace_traversable_20260715"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "check_name": "evidence_entailment_rechecked",
      "declared_value": "partial",
      "execution_status": "completed",
      "findings": [
        "evidence_entailment:partial"
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
        "evidence:ev_2945",
        "evidence:ev_3121"
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
        "object_updated_at:2026-07-17T18:35:41+08:00",
        "source:source_647ffb9287507f806c354670 work_sha256:none"
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
        "source:source_647ffb9287507f806c354670 record_sha256:7c8c3d3a8fc4e730929d2b87cec14c4637e43b064c18737693b751932b033232"
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
        "source:source_647ffb9287507f806c354670 raw_sha256:ae36edff481f91a4e7698232656f71484625ab9e8f3415a95f9f1c65da358ab0"
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
        "relation index inspected; 1 related objects found",
        "related:source_647ffb9287507f806c354670"
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
        "validated:vault/memory/claim/claim_wechat_double_trace_traversable_20260715.md"
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
        "distinct_source_ids:1",
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
  "completed_at": "2026-07-18T16:02:59+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "0b3373f8c1c9d4fb6e809bc7d2065a616e3c17c0b804343944ed52941c95b984",
    "extraction_state_sha256": "7b3ef76d5b13e896c1224044fb5d78c7475b45abc0c3fad56817b80c80eb5dc9",
    "memory_schema_version": 2,
    "object_sha256": "cc3138280923a59b7733785fddca7995aa0cbd7702a4c3ebff0208d20ba04fc1",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "0b1b2aca9a2c2a1aa9f523b8d0a499e15cd9ce37bec4d791c93ee6203e292e7d",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "72ce2b47affc606dba97fa07f9984627902c9e8d1ea6ae5b1f19fabbdb146a35",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "72ce2b47affc606dba97fa07f9984627902c9e8d1ea6ae5b1f19fabbdb146a35"
    },
    "relation_neighborhood_sha256": "72ce2b47affc606dba97fa07f9984627902c9e8d1ea6ae5b1f19fabbdb146a35",
    "source_record_sha256s": {
      "source_647ffb9287507f806c354670": "7c8c3d3a8fc4e730929d2b87cec14c4637e43b064c18737693b751932b033232"
    },
    "source_state_sha256": "c5899ad32de2f2f055a14d2af8d67c94c77cdaf0e23c5f25f37fe7c872523659",
    "work_identity_sha256": "835742514231fb97b6c04de1ebecfed6ae9010d4fc6804050d810a4cdc6145aa"
  },
  "consolidation_id": "consolidation_ec6cea055b1ec016767e3caa",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-18T16:02:59+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_2945",
    "ev_3121"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_ec6cea055b1ec016767e3caa",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_wechat_double_trace_traversable_20260715",
  "object_sha256_after": "cc3138280923a59b7733785fddca7995aa0cbd7702a4c3ebff0208d20ba04fc1",
  "object_sha256_before": "27ae7a4efeccaee9c485a6df55bb8d273b7754d31d2ccdc171bff8f037cacd4c",
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
  "started_at": "2026-07-18T16:02:58+08:00",
  "status": "complete",
  "title": "Consolidation: 该文称边界 double trace deformation 可引入负能量流，使原本不可穿越的 ER 桥变为可穿越",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-18T16:02:59+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
