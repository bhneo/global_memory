---
id: "consolidation_ea7720175917694ce28a6207"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 表征收敛"
created_at: "2026-07-18T16:03:16+08:00"
updated_at: "2026-07-18T16:03:16+08:00"
consolidation_id: "consolidation_ea7720175917694ce28a6207"
object_id: "concept_representation_convergence"
object_version_before: 1
object_sha256_before: "07c5c3b0d7c5b5493a783b685598b6dca018df95d0e41c065dd229818b5aa70c"
object_sha256_after: "5f157b497a3ea5d9a219c3082a82c2e36f15408cc6e70583bfb76400e7bc619c"
source_ids: ["source_f35b44d4bd383fb26ca49165"]
source_sha256s: ["0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0"]
source_records: [{"source_id": "source_f35b44d4bd383fb26ca49165", "source_record_sha256": "2777c09c1825f34dedeccec2459b0dde1dadcb4438f4c616db757bbe4915690b", "raw_content_sha256": "0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-18T16:03:15+08:00"
completed_at: "2026-07-18T16:03:16+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_representation_convergence.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_f35b44d4bd383fb26ca49165 raw_sha256:0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_f35b44d4bd383fb26ca49165 record_sha256:2777c09c1825f34dedeccec2459b0dde1dadcb4438f4c616db757bbe4915690b"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_representation_convergence"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_f35b44d4bd383fb26ca49165", "related:concept_representation_convergence"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T18:35:58+08:00", "source:source_f35b44d4bd383fb26ca49165 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "5f157b497a3ea5d9a219c3082a82c2e36f15408cc6e70583bfb76400e7bc619c", "source_state_sha256": "5bd84ead68360b1c3db470f886b74d62b7aa48115bf0e1721fbb9b4c22d7c45d", "source_record_sha256s": {"source_f35b44d4bd383fb26ca49165": "2777c09c1825f34dedeccec2459b0dde1dadcb4438f4c616db757bbe4915690b"}, "raw_state_sha256": "f51b1090920416fef5b2129c0162814d2e1372539459f733f55527fb2825eeed", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "4f6c49f512ab1e26e2274fb0f71d62715a420267809b61d67ce9a65347c7944a", "relation_fingerprint": {"outgoing_relations_sha256": "0e0cf2dac4c7031db1d5dbeb5fa62684fb9e7334d58bd5a161eaa030c628c0c2", "incoming_relations_sha256": "a2c7ebd8e67674de9274717b087e5b202d71ddfaeb372f077f3997f23a3e03a8", "full_neighborhood_sha256": "c07261a84cee01b52023206ff4acb5852fd4e33d67cbddf218ea75579e5566ab"}, "relation_neighborhood_sha256": "c07261a84cee01b52023206ff4acb5852fd4e33d67cbddf218ea75579e5566ab", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_representation_convergence"
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
        "object_updated_at:2026-07-17T18:35:58+08:00",
        "source:source_f35b44d4bd383fb26ca49165 work_sha256:none"
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
        "source:source_f35b44d4bd383fb26ca49165 record_sha256:2777c09c1825f34dedeccec2459b0dde1dadcb4438f4c616db757bbe4915690b"
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
        "source:source_f35b44d4bd383fb26ca49165 raw_sha256:0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0"
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
        "related:source_f35b44d4bd383fb26ca49165",
        "related:concept_representation_convergence"
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
        "validated:vault/memory/concept/concept_representation_convergence.md"
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
  "completed_at": "2026-07-18T16:03:16+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "5f157b497a3ea5d9a219c3082a82c2e36f15408cc6e70583bfb76400e7bc619c",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "f51b1090920416fef5b2129c0162814d2e1372539459f733f55527fb2825eeed",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "c07261a84cee01b52023206ff4acb5852fd4e33d67cbddf218ea75579e5566ab",
      "incoming_relations_sha256": "a2c7ebd8e67674de9274717b087e5b202d71ddfaeb372f077f3997f23a3e03a8",
      "outgoing_relations_sha256": "0e0cf2dac4c7031db1d5dbeb5fa62684fb9e7334d58bd5a161eaa030c628c0c2"
    },
    "relation_neighborhood_sha256": "c07261a84cee01b52023206ff4acb5852fd4e33d67cbddf218ea75579e5566ab",
    "source_record_sha256s": {
      "source_f35b44d4bd383fb26ca49165": "2777c09c1825f34dedeccec2459b0dde1dadcb4438f4c616db757bbe4915690b"
    },
    "source_state_sha256": "5bd84ead68360b1c3db470f886b74d62b7aa48115bf0e1721fbb9b4c22d7c45d",
    "work_identity_sha256": "4f6c49f512ab1e26e2274fb0f71d62715a420267809b61d67ce9a65347c7944a"
  },
  "consolidation_id": "consolidation_ea7720175917694ce28a6207",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-18T16:03:16+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_ea7720175917694ce28a6207",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_representation_convergence",
  "object_sha256_after": "5f157b497a3ea5d9a219c3082a82c2e36f15408cc6e70583bfb76400e7bc619c",
  "object_sha256_before": "07c5c3b0d7c5b5493a783b685598b6dca018df95d0e41c065dd229818b5aa70c",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_f35b44d4bd383fb26ca49165"
  ],
  "source_records": [
    {
      "raw_content_sha256": "0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0",
      "source_id": "source_f35b44d4bd383fb26ca49165",
      "source_record_sha256": "2777c09c1825f34dedeccec2459b0dde1dadcb4438f4c616db757bbe4915690b",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0"
  ],
  "started_at": "2026-07-18T16:03:15+08:00",
  "status": "complete",
  "title": "Consolidation: 表征收敛",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-18T16:03:16+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
