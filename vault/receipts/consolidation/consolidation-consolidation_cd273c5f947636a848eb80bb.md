---
id: "consolidation_cd273c5f947636a848eb80bb"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 表征收敛"
created_at: "2026-07-17T18:35:58+08:00"
updated_at: "2026-07-17T18:35:58+08:00"
consolidation_id: "consolidation_cd273c5f947636a848eb80bb"
object_id: "concept_representation_convergence"
object_version_before: 1
object_sha256_before: "3fbe67f37a7d1b5889318f11da9dad0ea1e5fafbef8d503ed10e5738e160b708"
object_sha256_after: "07c5c3b0d7c5b5493a783b685598b6dca018df95d0e41c065dd229818b5aa70c"
source_ids: ["source_f35b44d4bd383fb26ca49165"]
source_sha256s: ["0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0"]
source_records: [{"source_id": "source_f35b44d4bd383fb26ca49165", "source_record_sha256": "2777c09c1825f34dedeccec2459b0dde1dadcb4438f4c616db757bbe4915690b", "raw_content_sha256": "0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-17T18:35:57+08:00"
completed_at: "2026-07-17T18:35:58+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/concept/concept_representation_convergence.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_f35b44d4bd383fb26ca49165 raw_sha256:0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_f35b44d4bd383fb26ca49165 record_sha256:2777c09c1825f34dedeccec2459b0dde1dadcb4438f4c616db757bbe4915690b"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:concept_representation_convergence"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 2 related objects found", "related:source_f35b44d4bd383fb26ca49165", "related:concept_representation_convergence"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:24:02+08:00", "source:source_f35b44d4bd383fb26ca49165 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "07c5c3b0d7c5b5493a783b685598b6dca018df95d0e41c065dd229818b5aa70c", "source_state_sha256": "5bd84ead68360b1c3db470f886b74d62b7aa48115bf0e1721fbb9b4c22d7c45d", "source_record_sha256s": {"source_f35b44d4bd383fb26ca49165": "2777c09c1825f34dedeccec2459b0dde1dadcb4438f4c616db757bbe4915690b"}, "raw_state_sha256": "f51b1090920416fef5b2129c0162814d2e1372539459f733f55527fb2825eeed", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "4f6c49f512ab1e26e2274fb0f71d62715a420267809b61d67ce9a65347c7944a", "relation_neighborhood_sha256": "24943e9a77228c3436e80bcfe69018a0cfa830404f166d981cb867be514ba35a", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_representation_convergence"
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
        "object_updated_at:2026-07-17T15:24:02+08:00",
        "source:source_f35b44d4bd383fb26ca49165 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_f35b44d4bd383fb26ca49165 record_sha256:2777c09c1825f34dedeccec2459b0dde1dadcb4438f4c616db757bbe4915690b"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_f35b44d4bd383fb26ca49165 raw_sha256:0c7ad8b6aa226a022258100bc5d81f8d10bb3f87dc9d80b24e6736efb381f1d0"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 2 related objects found",
        "related:source_f35b44d4bd383fb26ca49165",
        "related:concept_representation_convergence"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/concept/concept_representation_convergence.md"
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
  "completed_at": "2026-07-17T18:35:58+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "07c5c3b0d7c5b5493a783b685598b6dca018df95d0e41c065dd229818b5aa70c",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "f51b1090920416fef5b2129c0162814d2e1372539459f733f55527fb2825eeed",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "24943e9a77228c3436e80bcfe69018a0cfa830404f166d981cb867be514ba35a",
    "source_record_sha256s": {
      "source_f35b44d4bd383fb26ca49165": "2777c09c1825f34dedeccec2459b0dde1dadcb4438f4c616db757bbe4915690b"
    },
    "source_state_sha256": "5bd84ead68360b1c3db470f886b74d62b7aa48115bf0e1721fbb9b4c22d7c45d",
    "work_identity_sha256": "4f6c49f512ab1e26e2274fb0f71d62715a420267809b61d67ce9a65347c7944a"
  },
  "consolidation_id": "consolidation_cd273c5f947636a848eb80bb",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:58+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_cd273c5f947636a848eb80bb",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_representation_convergence",
  "object_sha256_after": "07c5c3b0d7c5b5493a783b685598b6dca018df95d0e41c065dd229818b5aa70c",
  "object_sha256_before": "3fbe67f37a7d1b5889318f11da9dad0ea1e5fafbef8d503ed10e5738e160b708",
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
  "started_at": "2026-07-17T18:35:57+08:00",
  "status": "complete",
  "title": "Consolidation: 表征收敛",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:58+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
