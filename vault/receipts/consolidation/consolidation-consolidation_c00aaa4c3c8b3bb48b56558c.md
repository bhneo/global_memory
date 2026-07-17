---
id: "consolidation_c00aaa4c3c8b3bb48b56558c"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 该文称瞳孔调节可能依据大脑对光的感知而非实际照度，主观扩张感与瞳孔幅度正相关"
created_at: "2026-07-17T18:35:44+08:00"
updated_at: "2026-07-17T18:35:44+08:00"
consolidation_id: "consolidation_c00aaa4c3c8b3bb48b56558c"
object_id: "claim_wechat_expanding_hole_pupil_perception_not_luminance_20260716"
object_version_before: 1
object_sha256_before: "745fd1b344f1f2b981435ea0dab504fa6340a914f9eaae44d5bd9ad158a4a8a6"
object_sha256_after: "ad3afaf58b1ef162962461aa2109b6511aeafe25550ae02d54db6feba79f73ec"
source_ids: ["source_38756ea977001ddb8594f144"]
source_sha256s: ["fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86"]
source_records: [{"source_id": "source_38756ea977001ddb8594f144", "source_record_sha256": "a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1", "raw_content_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_980", "ev_569"]
started_at: "2026-07-17T18:35:44+08:00"
completed_at: "2026-07-17T18:35:44+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_wechat_expanding_hole_pupil_perception_not_luminance_20260716.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_38756ea977001ddb8594f144 raw_sha256:fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_38756ea977001ddb8594f144 record_sha256:a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:ev_980", "evidence:ev_569"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:partial"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_wechat_expanding_hole_pupil_perception_not_luminance_20260716"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_38756ea977001ddb8594f144"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:51+08:00", "source:source_38756ea977001ddb8594f144 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "ad3afaf58b1ef162962461aa2109b6511aeafe25550ae02d54db6feba79f73ec", "source_state_sha256": "f20bc6cc3d7c2d066cabbbe69248e7ffa6bfb935f0a4aad66e98d46fce12fe50", "source_record_sha256s": {"source_38756ea977001ddb8594f144": "a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1"}, "raw_state_sha256": "635e5ccdf6f906628aee0fe580f30095af4bf33884edb4f17af05778bfb030c0", "evidence_sha256": "cd3bbcfcedfe47a8c9971a5b667bb85293c5d530f745f3d3ac90d3e3bcdbea93", "extraction_state_sha256": "7a926bfb8f96b17a0aee1ce6b27586ba5658975394308712ac0ce608b9fa36a5", "work_identity_sha256": "791c125c2340eb9c96ed549e7c555c0c295145c73665f1ad74e469c53cec348e", "relation_neighborhood_sha256": "68a9ab0ac189dacace41f9bf3c6b65684ec8ef5b58c9a3a3d08242d9fda9ccd5", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_wechat_expanding_hole_pupil_perception_not_luminance_20260716"
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
        "evidence:ev_980",
        "evidence:ev_569"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:51+08:00",
        "source:source_38756ea977001ddb8594f144 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_38756ea977001ddb8594f144 record_sha256:a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_38756ea977001ddb8594f144 raw_sha256:fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_38756ea977001ddb8594f144"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_wechat_expanding_hole_pupil_perception_not_luminance_20260716.md"
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
  "completed_at": "2026-07-17T18:35:44+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "cd3bbcfcedfe47a8c9971a5b667bb85293c5d530f745f3d3ac90d3e3bcdbea93",
    "extraction_state_sha256": "7a926bfb8f96b17a0aee1ce6b27586ba5658975394308712ac0ce608b9fa36a5",
    "memory_schema_version": 2,
    "object_sha256": "ad3afaf58b1ef162962461aa2109b6511aeafe25550ae02d54db6feba79f73ec",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "635e5ccdf6f906628aee0fe580f30095af4bf33884edb4f17af05778bfb030c0",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "68a9ab0ac189dacace41f9bf3c6b65684ec8ef5b58c9a3a3d08242d9fda9ccd5",
    "source_record_sha256s": {
      "source_38756ea977001ddb8594f144": "a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1"
    },
    "source_state_sha256": "f20bc6cc3d7c2d066cabbbe69248e7ffa6bfb935f0a4aad66e98d46fce12fe50",
    "work_identity_sha256": "791c125c2340eb9c96ed549e7c555c0c295145c73665f1ad74e469c53cec348e"
  },
  "consolidation_id": "consolidation_c00aaa4c3c8b3bb48b56558c",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:44+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_980",
    "ev_569"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_c00aaa4c3c8b3bb48b56558c",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_wechat_expanding_hole_pupil_perception_not_luminance_20260716",
  "object_sha256_after": "ad3afaf58b1ef162962461aa2109b6511aeafe25550ae02d54db6feba79f73ec",
  "object_sha256_before": "745fd1b344f1f2b981435ea0dab504fa6340a914f9eaae44d5bd9ad158a4a8a6",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_38756ea977001ddb8594f144"
  ],
  "source_records": [
    {
      "raw_content_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86",
      "source_id": "source_38756ea977001ddb8594f144",
      "source_record_sha256": "a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86"
  ],
  "started_at": "2026-07-17T18:35:44+08:00",
  "status": "complete",
  "title": "Consolidation: 该文称瞳孔调节可能依据大脑对光的感知而非实际照度，主观扩张感与瞳孔幅度正相关",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:44+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
