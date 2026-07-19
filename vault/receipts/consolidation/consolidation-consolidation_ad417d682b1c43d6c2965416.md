---
id: "consolidation_ad417d682b1c43d6c2965416"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 53.7% success under human perturbations, outperforming the strongest baseline by 15.7"
created_at: "2026-07-19T03:05:33+08:00"
updated_at: "2026-07-19T03:05:33+08:00"
consolidation_id: "consolidation_ad417d682b1c43d6c2965416"
object_id: "claim_6c93f48395d9852588c5c00f"
object_version_before: 1
object_sha256_before: "f80bc81007e12a52a35929c2f3318602269c4eae041364bb63e92901be2cb3c4"
object_sha256_after: "2bb323893a766cf97f398cfac6e44295f84b750aecd757d920681c718f37acf4"
source_ids: ["source_283911da72edc403d1b823fb"]
source_sha256s: ["1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558"]
source_records: [{"source_id": "source_283911da72edc403d1b823fb", "source_record_sha256": "79a6150e5aae2900abec238d83123f02e13565489e12f09da8d943dfc7d76ccb", "raw_content_sha256": "1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["evidence_67d442e885727dfc34e0"]
started_at: "2026-07-19T03:05:33+08:00"
completed_at: "2026-07-19T03:05:33+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/claim/claim_6c93f48395d9852588c5c00f.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_283911da72edc403d1b823fb raw_sha256:1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_283911da72edc403d1b823fb record_sha256:79a6150e5aae2900abec238d83123f02e13565489e12f09da8d943dfc7d76ccb"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["evidence:evidence_67d442e885727dfc34e0"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "passed", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": "full", "findings": ["evidence_entailment:full"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 2 candidates inspected", "candidate:claim_6c93f48395d9852588c5c00f", "candidate:source_283911da72edc403d1b823fb"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_283911da72edc403d1b823fb", "related:concept_multitimescale_tactile_world_model"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T03:02:54+08:00", "source:source_283911da72edc403d1b823fb work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "2bb323893a766cf97f398cfac6e44295f84b750aecd757d920681c718f37acf4", "source_state_sha256": "4dbb0f31188632b482a49f0b2254809aa63afd45e38404f36bc26f821179d0d2", "source_record_sha256s": {"source_283911da72edc403d1b823fb": "79a6150e5aae2900abec238d83123f02e13565489e12f09da8d943dfc7d76ccb"}, "raw_state_sha256": "04dbb68aac96d64ef750860f54351fb7940eef8bb62011e80d1a616c5a673e8c", "evidence_sha256": "4520be67a15b17850d89e36a28e0d963a428aee9abe4cd3433512139c7970e81", "extraction_state_sha256": "908b5289e59684538bcd9261d6a33134cfeb4c729240c408d9a112b02a3c60ea", "work_identity_sha256": "4986cf0e83301d59bc286fab46a32e681d6aff92877af88913cfd0fbd8f82d8b", "relation_fingerprint": {"outgoing_relations_sha256": "7a3b01790a8188fa8265f1852f4fd6159838727940866f8df89ecff5b77a6a33", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "7a3b01790a8188fa8265f1852f4fd6159838727940866f8df89ecff5b77a6a33"}, "relation_neighborhood_sha256": "7a3b01790a8188fa8265f1852f4fd6159838727940866f8df89ecff5b77a6a33", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_6c93f48395d9852588c5c00f",
        "candidate:source_283911da72edc403d1b823fb"
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
        "evidence:evidence_67d442e885727dfc34e0"
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
        "object_updated_at:2026-07-19T03:02:54+08:00",
        "source:source_283911da72edc403d1b823fb work_sha256:none"
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
        "source:source_283911da72edc403d1b823fb record_sha256:79a6150e5aae2900abec238d83123f02e13565489e12f09da8d943dfc7d76ccb"
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
        "source:source_283911da72edc403d1b823fb raw_sha256:1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558"
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
        "related:source_283911da72edc403d1b823fb",
        "related:concept_multitimescale_tactile_world_model"
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
        "validated:vault/memory/claim/claim_6c93f48395d9852588c5c00f.md"
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
  "completed_at": "2026-07-19T03:05:33+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4520be67a15b17850d89e36a28e0d963a428aee9abe4cd3433512139c7970e81",
    "extraction_state_sha256": "908b5289e59684538bcd9261d6a33134cfeb4c729240c408d9a112b02a3c60ea",
    "memory_schema_version": 2,
    "object_sha256": "2bb323893a766cf97f398cfac6e44295f84b750aecd757d920681c718f37acf4",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "04dbb68aac96d64ef750860f54351fb7940eef8bb62011e80d1a616c5a673e8c",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "7a3b01790a8188fa8265f1852f4fd6159838727940866f8df89ecff5b77a6a33",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "7a3b01790a8188fa8265f1852f4fd6159838727940866f8df89ecff5b77a6a33"
    },
    "relation_neighborhood_sha256": "7a3b01790a8188fa8265f1852f4fd6159838727940866f8df89ecff5b77a6a33",
    "source_record_sha256s": {
      "source_283911da72edc403d1b823fb": "79a6150e5aae2900abec238d83123f02e13565489e12f09da8d943dfc7d76ccb"
    },
    "source_state_sha256": "4dbb0f31188632b482a49f0b2254809aa63afd45e38404f36bc26f821179d0d2",
    "work_identity_sha256": "4986cf0e83301d59bc286fab46a32e681d6aff92877af88913cfd0fbd8f82d8b"
  },
  "consolidation_id": "consolidation_ad417d682b1c43d6c2965416",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T03:05:33+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "evidence_67d442e885727dfc34e0"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_ad417d682b1c43d6c2965416",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_6c93f48395d9852588c5c00f",
  "object_sha256_after": "2bb323893a766cf97f398cfac6e44295f84b750aecd757d920681c718f37acf4",
  "object_sha256_before": "f80bc81007e12a52a35929c2f3318602269c4eae041364bb63e92901be2cb3c4",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_283911da72edc403d1b823fb"
  ],
  "source_records": [
    {
      "raw_content_sha256": "1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558",
      "source_id": "source_283911da72edc403d1b823fb",
      "source_record_sha256": "79a6150e5aae2900abec238d83123f02e13565489e12f09da8d943dfc7d76ccb",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "1f8857d23479821799d71caf28a316b400fa73de4bc04f484ff508bc51ef0558"
  ],
  "started_at": "2026-07-19T03:05:33+08:00",
  "status": "complete",
  "title": "Consolidation: 53.7% success under human perturbations, outperforming the strongest baseline by 15.7",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T03:05:33+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
