---
id: "consolidation_e13d2e635e0a7fba7ce66948"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 保留视觉语言先验的块内反应式力注入"
created_at: "2026-07-26T12:33:29+08:00"
updated_at: "2026-07-26T12:33:29+08:00"
consolidation_id: "consolidation_e13d2e635e0a7fba7ce66948"
object_id: "concept_2ce226e08d585158c1dfbb18"
object_version_before: 1
object_sha256_before: "0822cb1150229d79d139290fbd8aab8811d9cfe399a3a353def4f79102a204dd"
object_sha256_after: "1ea0dae94b6cad5dee3b4989ee0180d9faeb10d6162a062b5aeb51af06a08ab4"
source_ids: ["source_4e06d1b1cdcd0d07eff47909"]
source_sha256s: ["ebbe3a63017280d609e1822b31af341c505ea3aee643726c542d201df6fcdf4e"]
source_records: [{"source_id": "source_4e06d1b1cdcd0d07eff47909", "source_record_sha256": "b374bac455e32c834d10ee963468201032b77876a3822be5db85779e0f1ffb22", "raw_content_sha256": "ebbe3a63017280d609e1822b31af341c505ea3aee643726c542d201df6fcdf4e", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:28+08:00"
completed_at: "2026-07-26T12:33:29+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_2ce226e08d585158c1dfbb18.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_4e06d1b1cdcd0d07eff47909 raw_sha256:ebbe3a63017280d609e1822b31af341c505ea3aee643726c542d201df6fcdf4e"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_4e06d1b1cdcd0d07eff47909 record_sha256:b374bac455e32c834d10ee963468201032b77876a3822be5db85779e0f1ffb22"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_2ce226e08d585158c1dfbb18"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 4 related objects found", "related:source_4e06d1b1cdcd0d07eff47909", "related:concept_637cf7264723c03955c719e2", "related:concept_2ce226e08d585158c1dfbb18", "related:concept_2ce226e08d585158c1dfbb18"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-24T18:06:13+08:00", "source:source_4e06d1b1cdcd0d07eff47909 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "1ea0dae94b6cad5dee3b4989ee0180d9faeb10d6162a062b5aeb51af06a08ab4", "source_state_sha256": "427a03708d60267d6715c2980763e6c2f2764f043eb5e5912535aee78755840a", "source_record_sha256s": {"source_4e06d1b1cdcd0d07eff47909": "b374bac455e32c834d10ee963468201032b77876a3822be5db85779e0f1ffb22"}, "raw_state_sha256": "9e8015bdf377840f38096cfaa429e91490d1ed5a711fa14cfba849b50390f0a6", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "2403752d8bcfbcff9e1f1e99b0a895ea5bbee7d2aa64b783324f377a6f8d2aa2", "relation_fingerprint": {"outgoing_relations_sha256": "fed51768b65e236b1fa9a01da3f08f877da0533709efbec2dc58f1dfb410a3c3", "incoming_relations_sha256": "c70f247eab484b32b37233617b08749d3e97ef54606ac1b0092b9f521e71aef0", "full_neighborhood_sha256": "aff51fea1c3444a530c09ad6ec5de94b7eab1a6a1b4602835f81799cdecffe53"}, "relation_neighborhood_sha256": "aff51fea1c3444a530c09ad6ec5de94b7eab1a6a1b4602835f81799cdecffe53", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_2ce226e08d585158c1dfbb18"
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
        "object_updated_at:2026-07-24T18:06:13+08:00",
        "source:source_4e06d1b1cdcd0d07eff47909 work_sha256:none"
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
        "source:source_4e06d1b1cdcd0d07eff47909 record_sha256:b374bac455e32c834d10ee963468201032b77876a3822be5db85779e0f1ffb22"
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
        "source:source_4e06d1b1cdcd0d07eff47909 raw_sha256:ebbe3a63017280d609e1822b31af341c505ea3aee643726c542d201df6fcdf4e"
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
        "relation index inspected; 4 related objects found",
        "related:source_4e06d1b1cdcd0d07eff47909",
        "related:concept_637cf7264723c03955c719e2",
        "related:concept_2ce226e08d585158c1dfbb18",
        "related:concept_2ce226e08d585158c1dfbb18"
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
        "validated:vault/memory/concept/concept_2ce226e08d585158c1dfbb18.md"
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
  "completed_at": "2026-07-26T12:33:29+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "1ea0dae94b6cad5dee3b4989ee0180d9faeb10d6162a062b5aeb51af06a08ab4",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "9e8015bdf377840f38096cfaa429e91490d1ed5a711fa14cfba849b50390f0a6",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "aff51fea1c3444a530c09ad6ec5de94b7eab1a6a1b4602835f81799cdecffe53",
      "incoming_relations_sha256": "c70f247eab484b32b37233617b08749d3e97ef54606ac1b0092b9f521e71aef0",
      "outgoing_relations_sha256": "fed51768b65e236b1fa9a01da3f08f877da0533709efbec2dc58f1dfb410a3c3"
    },
    "relation_neighborhood_sha256": "aff51fea1c3444a530c09ad6ec5de94b7eab1a6a1b4602835f81799cdecffe53",
    "source_record_sha256s": {
      "source_4e06d1b1cdcd0d07eff47909": "b374bac455e32c834d10ee963468201032b77876a3822be5db85779e0f1ffb22"
    },
    "source_state_sha256": "427a03708d60267d6715c2980763e6c2f2764f043eb5e5912535aee78755840a",
    "work_identity_sha256": "2403752d8bcfbcff9e1f1e99b0a895ea5bbee7d2aa64b783324f377a6f8d2aa2"
  },
  "consolidation_id": "consolidation_e13d2e635e0a7fba7ce66948",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:29+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_e13d2e635e0a7fba7ce66948",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_2ce226e08d585158c1dfbb18",
  "object_sha256_after": "1ea0dae94b6cad5dee3b4989ee0180d9faeb10d6162a062b5aeb51af06a08ab4",
  "object_sha256_before": "0822cb1150229d79d139290fbd8aab8811d9cfe399a3a353def4f79102a204dd",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_4e06d1b1cdcd0d07eff47909"
  ],
  "source_records": [
    {
      "raw_content_sha256": "ebbe3a63017280d609e1822b31af341c505ea3aee643726c542d201df6fcdf4e",
      "source_id": "source_4e06d1b1cdcd0d07eff47909",
      "source_record_sha256": "b374bac455e32c834d10ee963468201032b77876a3822be5db85779e0f1ffb22",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "ebbe3a63017280d609e1822b31af341c505ea3aee643726c542d201df6fcdf4e"
  ],
  "started_at": "2026-07-26T12:33:28+08:00",
  "status": "complete",
  "title": "Consolidation: 保留视觉语言先验的块内反应式力注入",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:29+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
