---
id: "consolidation_46f2f8916b1062c280eedeb5"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 感知预测偏差"
created_at: "2026-07-20T13:37:52+08:00"
updated_at: "2026-07-20T13:37:52+08:00"
consolidation_id: "consolidation_46f2f8916b1062c280eedeb5"
object_id: "concept_perceptual_prediction_bias"
object_version_before: 1
object_sha256_before: "f338f67a9167760aba4582999076e80b0d74183b9e994f8fe1e27661c55fee1e"
object_sha256_after: "7728f3f4c6607f09eb6cb3daaa53b8a1eea56b1bfbb2e6dc1ef9f46f79bed23a"
source_ids: ["source_38756ea977001ddb8594f144", "source_12432807660136b2471717f1"]
source_sha256s: ["fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b"]
source_records: [{"source_id": "source_38756ea977001ddb8594f144", "source_record_sha256": "a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1", "raw_content_sha256": "fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "work_id": null, "work_document_sha256": null}, {"source_id": "source_12432807660136b2471717f1", "source_record_sha256": "350cc93b3cca23675d3111d94fa1a131c0bf76a1eda69c7f253024724ab919e7", "raw_content_sha256": "05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-20T13:37:52+08:00"
completed_at: "2026-07-20T13:37:52+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_perceptual_prediction_bias.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_38756ea977001ddb8594f144 raw_sha256:fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86", "source:source_12432807660136b2471717f1 raw_sha256:05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_38756ea977001ddb8594f144 record_sha256:a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1", "source:source_12432807660136b2471717f1 record_sha256:350cc93b3cca23675d3111d94fa1a131c0bf76a1eda69c7f253024724ab919e7"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_perceptual_prediction_bias"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 3 related objects found", "related:source_12432807660136b2471717f1", "related:source_38756ea977001ddb8594f144", "related:concept_perceptual_prediction_bias"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-20T12:09:55+08:00", "source:source_38756ea977001ddb8594f144 work_sha256:none", "source:source_12432807660136b2471717f1 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "7728f3f4c6607f09eb6cb3daaa53b8a1eea56b1bfbb2e6dc1ef9f46f79bed23a", "source_state_sha256": "1263578de38b68fd1ad47d31c4a37137cc7d98a16843db5a87e22d67a7986a84", "source_record_sha256s": {"source_38756ea977001ddb8594f144": "a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1", "source_12432807660136b2471717f1": "350cc93b3cca23675d3111d94fa1a131c0bf76a1eda69c7f253024724ab919e7"}, "raw_state_sha256": "d7d0f9019a24983ec43fd4de98f9746e05ca5265d3cb80f4339a4ef0140acd64", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "98ed46d181c674dbbeb2da0d8d053dda95e6e35320e0f40fa15e70259d9eaaf1", "relation_fingerprint": {"outgoing_relations_sha256": "d7136a04f2c797402389375dce90750dc10754cd27bf64e56454334b7be02e75", "incoming_relations_sha256": "3baf6762c165c7817845f6763c70c0baf70ac1bf6b9391d1a19f8ce02d1c18f8", "full_neighborhood_sha256": "6a641d4f1db8d4072f8c8ac38299041524a1e831a6099928970e7e41bec6d141"}, "relation_neighborhood_sha256": "6a641d4f1db8d4072f8c8ac38299041524a1e831a6099928970e7e41bec6d141", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_perceptual_prediction_bias"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "check_name": "evidence_entailment_rechecked",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "not applicable for non-claim object"
      ],
      "method": "declared-metadata-inspection",
      "semantic_recheck_performed": true,
      "validation_outcome": "not_applicable",
      "warnings": []
    },
    "evidence_revalidated": {
      "check_name": "evidence_revalidated",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "not applicable for non-claim object"
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
        "object_updated_at:2026-07-20T12:09:55+08:00",
        "source:source_38756ea977001ddb8594f144 work_sha256:none",
        "source:source_12432807660136b2471717f1 work_sha256:none"
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
        "source:source_38756ea977001ddb8594f144 record_sha256:a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1",
        "source:source_12432807660136b2471717f1 record_sha256:350cc93b3cca23675d3111d94fa1a131c0bf76a1eda69c7f253024724ab919e7"
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
        "source:source_38756ea977001ddb8594f144 raw_sha256:fc2140ce2cdf4019533f67bd6801061bc341a47afcaddc77797e79535e96cb86",
        "source:source_12432807660136b2471717f1 raw_sha256:05d0d9d390f1e06b5e61c33375a572d5f6117c540f719604d3c2980bb31e443b"
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
        "relation index inspected; 3 related objects found",
        "related:source_12432807660136b2471717f1",
        "related:source_38756ea977001ddb8594f144",
        "related:concept_perceptual_prediction_bias"
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
        "validated:vault/memory/concept/concept_perceptual_prediction_bias.md"
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
        "distinct_source_ids:2",
        "distinct_work_ids:0"
      ],
      "method": "logical-work-identity-count",
      "semantic_recheck_performed": null,
      "validation_outcome": "not_established",
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
  "completed_at": "2026-07-20T13:37:52+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "7728f3f4c6607f09eb6cb3daaa53b8a1eea56b1bfbb2e6dc1ef9f46f79bed23a",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "d7d0f9019a24983ec43fd4de98f9746e05ca5265d3cb80f4339a4ef0140acd64",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "6a641d4f1db8d4072f8c8ac38299041524a1e831a6099928970e7e41bec6d141",
      "incoming_relations_sha256": "3baf6762c165c7817845f6763c70c0baf70ac1bf6b9391d1a19f8ce02d1c18f8",
      "outgoing_relations_sha256": "d7136a04f2c797402389375dce90750dc10754cd27bf64e56454334b7be02e75"
    },
    "relation_neighborhood_sha256": "6a641d4f1db8d4072f8c8ac38299041524a1e831a6099928970e7e41bec6d141",
    "source_record_sha256s": {
      "source_12432807660136b2471717f1": "350cc93b3cca23675d3111d94fa1a131c0bf76a1eda69c7f253024724ab919e7",
      "source_38756ea977001ddb8594f144": "a54e976bcfdf35301a313ba98277731e8c4c878d1fbff2bc0f914ca5ea47e7c1"
    },
    "source_state_sha256": "1263578de38b68fd1ad47d31c4a37137cc7d98a16843db5a87e22d67a7986a84",
    "work_identity_sha256": "98ed46d181c674dbbeb2da0d8d053dda95e6e35320e0f40fa15e70259d9eaaf1"
  },
  "consolidation_id": "consolidation_46f2f8916b1062c280eedeb5",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-20T13:37:52+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_46f2f8916b1062c280eedeb5",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_perceptual_prediction_bias",
  "object_sha256_after": "7728f3f4c6607f09eb6cb3daaa53b8a1eea56b1bfbb2e6dc1ef9f46f79bed23a",
  "object_sha256_before": "f338f67a9167760aba4582999076e80b0d74183b9e994f8fe1e27661c55fee1e",
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
  "started_at": "2026-07-20T13:37:52+08:00",
  "status": "complete",
  "title": "Consolidation: 感知预测偏差",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-20T13:37:52+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
