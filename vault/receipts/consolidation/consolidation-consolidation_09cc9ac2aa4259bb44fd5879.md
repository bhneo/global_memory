---
id: "consolidation_09cc9ac2aa4259bb44fd5879"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: Cursor M7 真实读取与 receipt 回写验收"
created_at: "2026-07-17T18:36:01+08:00"
updated_at: "2026-07-17T18:36:01+08:00"
consolidation_id: "consolidation_09cc9ac2aa4259bb44fd5879"
object_id: "experiment_7101e03fb065226e65f388a5"
object_version_before: 1
object_sha256_before: "0d017bb14e69d0bdb63833eacd67b8d37b716f8a2355fbb09ade0a0b9ab4ca43"
object_sha256_after: "bdcc51efeee93e82754424f4f76d9cb27cd85912d777dab3e1c40bae9d32eb0b"
source_ids: ["source_113d589e6dadf14b5fa8edea"]
source_sha256s: ["394593d72af8067a8b05675fa643d682f03c6ea11956027ce8c0492f91201ace"]
source_records: [{"source_id": "source_113d589e6dadf14b5fa8edea", "source_record_sha256": "a8d60f5e31e8887c7597dd303fc8a9903245d0b7db96249c307f65aff120067c", "raw_content_sha256": "394593d72af8067a8b05675fa643d682f03c6ea11956027ce8c0492f91201ace", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-17T18:36:00+08:00"
completed_at: "2026-07-17T18:36:01+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/experiment/experiment_7101e03fb065226e65f388a5.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_113d589e6dadf14b5fa8edea raw_sha256:394593d72af8067a8b05675fa643d682f03c6ea11956027ce8c0492f91201ace"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_113d589e6dadf14b5fa8edea record_sha256:a8d60f5e31e8887c7597dd303fc8a9903245d0b7db96249c307f65aff120067c"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 2 candidates inspected", "candidate:experiment_7101e03fb065226e65f388a5", "candidate:experiment_b6f1e1956690ac08fd56a5da"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_113d589e6dadf14b5fa8edea"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:24:04+08:00", "source:source_113d589e6dadf14b5fa8edea work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "bdcc51efeee93e82754424f4f76d9cb27cd85912d777dab3e1c40bae9d32eb0b", "source_state_sha256": "3acb638976c918dd75df4d74a2e875ac393b81e8012425c09f795d393a583590", "source_record_sha256s": {"source_113d589e6dadf14b5fa8edea": "a8d60f5e31e8887c7597dd303fc8a9903245d0b7db96249c307f65aff120067c"}, "raw_state_sha256": "c924a8e103d198e8ee429dc5e83ffd1f537bf0ee4a672c81ee1a5fd083d15cb2", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "7512cd3c657c2442a8ed812b5df9c440a67e372771b1dfc42c5f1509f4143b11", "relation_neighborhood_sha256": "ec77f6f07ad99875bbdc841e55432aa8fec0b65155918abbe0c3a69fc2fdfa9b", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "searched title; 2 candidates inspected",
        "candidate:experiment_7101e03fb065226e65f388a5",
        "candidate:experiment_b6f1e1956690ac08fd56a5da"
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
        "object_updated_at:2026-07-17T15:24:04+08:00",
        "source:source_113d589e6dadf14b5fa8edea work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_113d589e6dadf14b5fa8edea record_sha256:a8d60f5e31e8887c7597dd303fc8a9903245d0b7db96249c307f65aff120067c"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_113d589e6dadf14b5fa8edea raw_sha256:394593d72af8067a8b05675fa643d682f03c6ea11956027ce8c0492f91201ace"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_113d589e6dadf14b5fa8edea"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/experiment/experiment_7101e03fb065226e65f388a5.md"
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
  "completed_at": "2026-07-17T18:36:01+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "bdcc51efeee93e82754424f4f76d9cb27cd85912d777dab3e1c40bae9d32eb0b",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "c924a8e103d198e8ee429dc5e83ffd1f537bf0ee4a672c81ee1a5fd083d15cb2",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "ec77f6f07ad99875bbdc841e55432aa8fec0b65155918abbe0c3a69fc2fdfa9b",
    "source_record_sha256s": {
      "source_113d589e6dadf14b5fa8edea": "a8d60f5e31e8887c7597dd303fc8a9903245d0b7db96249c307f65aff120067c"
    },
    "source_state_sha256": "3acb638976c918dd75df4d74a2e875ac393b81e8012425c09f795d393a583590",
    "work_identity_sha256": "7512cd3c657c2442a8ed812b5df9c440a67e372771b1dfc42c5f1509f4143b11"
  },
  "consolidation_id": "consolidation_09cc9ac2aa4259bb44fd5879",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:36:01+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_09cc9ac2aa4259bb44fd5879",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "experiment_7101e03fb065226e65f388a5",
  "object_sha256_after": "bdcc51efeee93e82754424f4f76d9cb27cd85912d777dab3e1c40bae9d32eb0b",
  "object_sha256_before": "0d017bb14e69d0bdb63833eacd67b8d37b716f8a2355fbb09ade0a0b9ab4ca43",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_113d589e6dadf14b5fa8edea"
  ],
  "source_records": [
    {
      "raw_content_sha256": "394593d72af8067a8b05675fa643d682f03c6ea11956027ce8c0492f91201ace",
      "source_id": "source_113d589e6dadf14b5fa8edea",
      "source_record_sha256": "a8d60f5e31e8887c7597dd303fc8a9903245d0b7db96249c307f65aff120067c",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "394593d72af8067a8b05675fa643d682f03c6ea11956027ce8c0492f91201ace"
  ],
  "started_at": "2026-07-17T18:36:00+08:00",
  "status": "complete",
  "title": "Consolidation: Cursor M7 真实读取与 receipt 回写验收",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:36:01+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
