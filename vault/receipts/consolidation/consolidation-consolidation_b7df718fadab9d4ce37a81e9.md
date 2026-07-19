---
id: "consolidation_b7df718fadab9d4ce37a81e9"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: real-world environments demonstrate that ActionCache maintains high task success rates in a low-latency regime, achieving inference acceleration of up to 11.75×"
created_at: "2026-07-19T03:05:34+08:00"
updated_at: "2026-07-19T03:05:34+08:00"
consolidation_id: "consolidation_b7df718fadab9d4ce37a81e9"
object_id: "claim_6ed5013981fdc75c87eb19c9"
object_version_before: 1
object_sha256_before: "b440115784c7d11a6ad6787bd873db771d041c07f5f45101908fb94b7c480b48"
object_sha256_after: "a553fba356fd2b924c6acd3af6721d584f8ba0c7883c4b9f3e07a7bdb5483330"
source_ids: ["source_291d6174cf92660287138f47"]
source_sha256s: ["c3b99399eef2fc7b323dcb9e453ef2996d2fe76b48e18627b45b7cb301b515b7"]
source_records: [{"source_id": "source_291d6174cf92660287138f47", "source_record_sha256": "6bdc3cb2e29e35d86c9ca47c8c2ec19dfa104b47ea82dbd1ee99e4c6685b2df1", "raw_content_sha256": "c3b99399eef2fc7b323dcb9e453ef2996d2fe76b48e18627b45b7cb301b515b7", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["evidence_f6d09379560910ca9664"]
started_at: "2026-07-19T03:05:33+08:00"
completed_at: "2026-07-19T03:05:34+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/claim/claim_6ed5013981fdc75c87eb19c9.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_291d6174cf92660287138f47 raw_sha256:c3b99399eef2fc7b323dcb9e453ef2996d2fe76b48e18627b45b7cb301b515b7"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_291d6174cf92660287138f47 record_sha256:6bdc3cb2e29e35d86c9ca47c8c2ec19dfa104b47ea82dbd1ee99e4c6685b2df1"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["evidence:evidence_f6d09379560910ca9664"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "passed", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": "full", "findings": ["evidence_entailment:full"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 2 candidates inspected", "candidate:claim_6ed5013981fdc75c87eb19c9", "candidate:source_291d6174cf92660287138f47"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_291d6174cf92660287138f47", "related:concept_vla_action_cache_refinement"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T03:02:12+08:00", "source:source_291d6174cf92660287138f47 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "a553fba356fd2b924c6acd3af6721d584f8ba0c7883c4b9f3e07a7bdb5483330", "source_state_sha256": "537df76e2f43971316645bfbd61da00ae3bda41a7c198fe00d7ee58e882772e2", "source_record_sha256s": {"source_291d6174cf92660287138f47": "6bdc3cb2e29e35d86c9ca47c8c2ec19dfa104b47ea82dbd1ee99e4c6685b2df1"}, "raw_state_sha256": "3e468de79984505b87d3029df705d9eb362ae560939a7c7edb1f931955cbd6bd", "evidence_sha256": "bf785c406a463b84c5dcb129012df532e3e380476866f688e082f7f773a774a9", "extraction_state_sha256": "32e325aca5447b5c6094cfd19eba1665a1048f9c80fad5424da8d9e456111180", "work_identity_sha256": "bdeef10e8c35ded8f94f2652e95152bc2dbad40ef0feed8fb260d69886db6c8d", "relation_fingerprint": {"outgoing_relations_sha256": "097f9385506fcd13509c6923e441f766b7ceebd266c48159b8b0ef7586ad070e", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "097f9385506fcd13509c6923e441f766b7ceebd266c48159b8b0ef7586ad070e"}, "relation_neighborhood_sha256": "097f9385506fcd13509c6923e441f766b7ceebd266c48159b8b0ef7586ad070e", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "searched title; 2 candidates inspected",
        "candidate:claim_6ed5013981fdc75c87eb19c9",
        "candidate:source_291d6174cf92660287138f47"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "check_name": "evidence_entailment_rechecked",
      "declared_value": "full",
      "execution_status": "completed",
      "findings": [
        "evidence_entailment:full"
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
        "evidence:evidence_f6d09379560910ca9664"
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
        "object_updated_at:2026-07-19T03:02:12+08:00",
        "source:source_291d6174cf92660287138f47 work_sha256:none"
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
        "source:source_291d6174cf92660287138f47 record_sha256:6bdc3cb2e29e35d86c9ca47c8c2ec19dfa104b47ea82dbd1ee99e4c6685b2df1"
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
        "source:source_291d6174cf92660287138f47 raw_sha256:c3b99399eef2fc7b323dcb9e453ef2996d2fe76b48e18627b45b7cb301b515b7"
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
        "relation index inspected; 2 related objects found",
        "related:source_291d6174cf92660287138f47",
        "related:concept_vla_action_cache_refinement"
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
        "validated:vault/memory/claim/claim_6ed5013981fdc75c87eb19c9.md"
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
  "completed_at": "2026-07-19T03:05:34+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "bf785c406a463b84c5dcb129012df532e3e380476866f688e082f7f773a774a9",
    "extraction_state_sha256": "32e325aca5447b5c6094cfd19eba1665a1048f9c80fad5424da8d9e456111180",
    "memory_schema_version": 2,
    "object_sha256": "a553fba356fd2b924c6acd3af6721d584f8ba0c7883c4b9f3e07a7bdb5483330",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "3e468de79984505b87d3029df705d9eb362ae560939a7c7edb1f931955cbd6bd",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "097f9385506fcd13509c6923e441f766b7ceebd266c48159b8b0ef7586ad070e",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "097f9385506fcd13509c6923e441f766b7ceebd266c48159b8b0ef7586ad070e"
    },
    "relation_neighborhood_sha256": "097f9385506fcd13509c6923e441f766b7ceebd266c48159b8b0ef7586ad070e",
    "source_record_sha256s": {
      "source_291d6174cf92660287138f47": "6bdc3cb2e29e35d86c9ca47c8c2ec19dfa104b47ea82dbd1ee99e4c6685b2df1"
    },
    "source_state_sha256": "537df76e2f43971316645bfbd61da00ae3bda41a7c198fe00d7ee58e882772e2",
    "work_identity_sha256": "bdeef10e8c35ded8f94f2652e95152bc2dbad40ef0feed8fb260d69886db6c8d"
  },
  "consolidation_id": "consolidation_b7df718fadab9d4ce37a81e9",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T03:05:34+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "evidence_f6d09379560910ca9664"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_b7df718fadab9d4ce37a81e9",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_6ed5013981fdc75c87eb19c9",
  "object_sha256_after": "a553fba356fd2b924c6acd3af6721d584f8ba0c7883c4b9f3e07a7bdb5483330",
  "object_sha256_before": "b440115784c7d11a6ad6787bd873db771d041c07f5f45101908fb94b7c480b48",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_291d6174cf92660287138f47"
  ],
  "source_records": [
    {
      "raw_content_sha256": "c3b99399eef2fc7b323dcb9e453ef2996d2fe76b48e18627b45b7cb301b515b7",
      "source_id": "source_291d6174cf92660287138f47",
      "source_record_sha256": "6bdc3cb2e29e35d86c9ca47c8c2ec19dfa104b47ea82dbd1ee99e4c6685b2df1",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "c3b99399eef2fc7b323dcb9e453ef2996d2fe76b48e18627b45b7cb301b515b7"
  ],
  "started_at": "2026-07-19T03:05:33+08:00",
  "status": "complete",
  "title": "Consolidation: real-world environments demonstrate that ActionCache maintains high task success rates in a low-latency regime, achieving inference acceleration of up to 11.75×",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T03:05:34+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
