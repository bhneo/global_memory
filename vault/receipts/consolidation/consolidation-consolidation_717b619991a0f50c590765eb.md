---
id: "consolidation_717b619991a0f50c590765eb"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 感知预测偏差"
created_at: "2026-07-17T18:35:57+08:00"
updated_at: "2026-07-17T18:35:57+08:00"
consolidation_id: "consolidation_717b619991a0f50c590765eb"
object_id: "concept_perceptual_prediction_bias"
object_version_before: 1
object_sha256_before: "1556efe7186a1e76ff84ee0eca0a5d227afc807ebd8a74eb9091f92f51df5c10"
object_sha256_after: "bdaa4ab517bd28b92f1f90a20d9075e91c9263ad29f1dca0526c0184f13dbabd"
source_ids: ["source_38756ea977001ddb8594f144", "source_12432807660136b2471717f1"]
source_sha256s: ["fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b"]
source_records: [{"source_id": "source_38756ea977001ddb8594f144", "source_record_sha256": "a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1", "raw_content_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "work_id": null, "work_document_sha256": null}, {"source_id": "source_12432807660136b2471717f1", "source_record_sha256": "350cc93b3cca23675d3111d94fa1a131c0bf76a1eda69c7f253024724ab919e7", "raw_content_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-17T18:35:57+08:00"
completed_at: "2026-07-17T18:35:57+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/concept/concept_perceptual_prediction_bias.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_38756ea977001ddb8594f144 raw_sha256:fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "source:source_12432807660136b2471717f1 raw_sha256:05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_38756ea977001ddb8594f144 record_sha256:a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1", "source:source_12432807660136b2471717f1 record_sha256:350cc93b3cca23675d3111d94fa1a131c0bf76a1eda69c7f253024724ab919e7"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:concept_perceptual_prediction_bias"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 3 related objects found", "related:source_12432807660136b2471717f1", "related:source_38756ea977001ddb8594f144", "related:concept_perceptual_prediction_bias"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T18:17:30+08:00", "source:source_38756ea977001ddb8594f144 work_sha256:none", "source:source_12432807660136b2471717f1 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "bdaa4ab517bd28b92f1f90a20d9075e91c9263ad29f1dca0526c0184f13dbabd", "source_state_sha256": "1263578de38b68fd1ad47d31c4a37137cc7d98a16843db5a87e22d67a7986a84", "source_record_sha256s": {"source_38756ea977001ddb8594f144": "a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1", "source_12432807660136b2471717f1": "350cc93b3cca23675d3111d94fa1a131c0bf76a1eda69c7f253024724ab919e7"}, "raw_state_sha256": "d7d0f9019a24983ec43fd4de98f9746e05ca5265d3cb80f4339a4ef0140acd64", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "98ed46d181c674dbbeb2da0d8d053dda95e6e35320e0f40fa15e70259d9eaaf1", "relation_neighborhood_sha256": "c9b3ca731d960b575426e31f6149d0424915888182dc9a7bc2c62e4478ef76e9", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_perceptual_prediction_bias"
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
        "object_updated_at:2026-07-17T18:17:30+08:00",
        "source:source_38756ea977001ddb8594f144 work_sha256:none",
        "source:source_12432807660136b2471717f1 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_38756ea977001ddb8594f144 record_sha256:a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1",
        "source:source_12432807660136b2471717f1 record_sha256:350cc93b3cca23675d3111d94fa1a131c0bf76a1eda69c7f253024724ab919e7"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_38756ea977001ddb8594f144 raw_sha256:fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86",
        "source:source_12432807660136b2471717f1 raw_sha256:05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 3 related objects found",
        "related:source_12432807660136b2471717f1",
        "related:source_38756ea977001ddb8594f144",
        "related:concept_perceptual_prediction_bias"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/concept/concept_perceptual_prediction_bias.md"
      ],
      "status": "passed",
      "warnings": []
    },
    "source_independence_checked": {
      "findings": [
        "distinct_source_ids:2",
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
  "completed_at": "2026-07-17T18:35:57+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "bdaa4ab517bd28b92f1f90a20d9075e91c9263ad29f1dca0526c0184f13dbabd",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "d7d0f9019a24983ec43fd4de98f9746e05ca5265d3cb80f4339a4ef0140acd64",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "c9b3ca731d960b575426e31f6149d0424915888182dc9a7bc2c62e4478ef76e9",
    "source_record_sha256s": {
      "source_12432807660136b2471717f1": "350cc93b3cca23675d3111d94fa1a131c0bf76a1eda69c7f253024724ab919e7",
      "source_38756ea977001ddb8594f144": "a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1"
    },
    "source_state_sha256": "1263578de38b68fd1ad47d31c4a37137cc7d98a16843db5a87e22d67a7986a84",
    "work_identity_sha256": "98ed46d181c674dbbeb2da0d8d053dda95e6e35320e0f40fa15e70259d9eaaf1"
  },
  "consolidation_id": "consolidation_717b619991a0f50c590765eb",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:57+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_717b619991a0f50c590765eb",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_perceptual_prediction_bias",
  "object_sha256_after": "bdaa4ab517bd28b92f1f90a20d9075e91c9263ad29f1dca0526c0184f13dbabd",
  "object_sha256_before": "1556efe7186a1e76ff84ee0eca0a5d227afc807ebd8a74eb9091f92f51df5c10",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_38756ea977001ddb8594f144",
    "source_12432807660136b2471717f1"
  ],
  "source_records": [
    {
      "raw_content_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86",
      "source_id": "source_38756ea977001ddb8594f144",
      "source_record_sha256": "a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1",
      "work_document_sha256": null,
      "work_id": null
    },
    {
      "raw_content_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b",
      "source_id": "source_12432807660136b2471717f1",
      "source_record_sha256": "350cc93b3cca23675d3111d94fa1a131c0bf76a1eda69c7f253024724ab919e7",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86",
    "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b"
  ],
  "started_at": "2026-07-17T18:35:57+08:00",
  "status": "complete",
  "title": "Consolidation: 感知预测偏差",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:57+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
