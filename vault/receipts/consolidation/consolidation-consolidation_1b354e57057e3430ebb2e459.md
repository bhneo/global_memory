---
id: "consolidation_1b354e57057e3430ebb2e459"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 该文称具身 VLA 迭代速度常被真机评估流程而非训练本身卡住"
created_at: "2026-07-17T18:35:42+08:00"
updated_at: "2026-07-17T18:35:42+08:00"
consolidation_id: "consolidation_1b354e57057e3430ebb2e459"
object_id: "claim_wechat_embodied_eval_bottleneck_20260715"
object_version_before: 1
object_sha256_before: "e0093a83d4246fb4432cac040fdc2456918dc21506e9023e3d9da7fa533ba2ec"
object_sha256_after: "88038c120451d5a9ef9efed1f080f4d8dd46b6fb3e5c89063996ed6edd4227b5"
source_ids: ["source_2d4f3a7d3525782c8ff503ee"]
source_sha256s: ["2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e"]
source_records: [{"source_id": "source_2d4f3a7d3525782c8ff503ee", "source_record_sha256": "ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd", "raw_content_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_597", "ev_692"]
started_at: "2026-07-17T18:35:42+08:00"
completed_at: "2026-07-17T18:35:42+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_wechat_embodied_eval_bottleneck_20260715.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_2d4f3a7d3525782c8ff503ee raw_sha256:2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_2d4f3a7d3525782c8ff503ee record_sha256:ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:ev_597", "evidence:ev_692"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:partial"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_wechat_embodied_eval_bottleneck_20260715"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_2d4f3a7d3525782c8ff503ee"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:50+08:00", "source:source_2d4f3a7d3525782c8ff503ee work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "88038c120451d5a9ef9efed1f080f4d8dd46b6fb3e5c89063996ed6edd4227b5", "source_state_sha256": "ba7943f3a2a360a280c111d5d4fa02e900c28fd1d0743ff6e719806a54d51020", "source_record_sha256s": {"source_2d4f3a7d3525782c8ff503ee": "ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd"}, "raw_state_sha256": "367cb9dd55af5cae56b160a95e942a29555b8063320a400d4c76c919a838be93", "evidence_sha256": "2024bf2b575343bdff3d852dbf8673dbf5ec5a17c8f25f1a84380896a9e27911", "extraction_state_sha256": "be6ca894ad2baea92ca4faae3ba64b9d7f339f7ab06cb852d0843880f0d722fb", "work_identity_sha256": "2b60f17ed42989e9c34ce5083be81e0c2273482b4dfd868f634d47466fc7e723", "relation_neighborhood_sha256": "c78a485403d3a7e80fac6001b55cd4712fa67cad3bfcae9f38cabb4f98958a34", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_wechat_embodied_eval_bottleneck_20260715"
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
        "evidence:ev_597",
        "evidence:ev_692"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:50+08:00",
        "source:source_2d4f3a7d3525782c8ff503ee work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_2d4f3a7d3525782c8ff503ee record_sha256:ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_2d4f3a7d3525782c8ff503ee raw_sha256:2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_2d4f3a7d3525782c8ff503ee"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_wechat_embodied_eval_bottleneck_20260715.md"
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
  "completed_at": "2026-07-17T18:35:42+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "2024bf2b575343bdff3d852dbf8673dbf5ec5a17c8f25f1a84380896a9e27911",
    "extraction_state_sha256": "be6ca894ad2baea92ca4faae3ba64b9d7f339f7ab06cb852d0843880f0d722fb",
    "memory_schema_version": 2,
    "object_sha256": "88038c120451d5a9ef9efed1f080f4d8dd46b6fb3e5c89063996ed6edd4227b5",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "367cb9dd55af5cae56b160a95e942a29555b8063320a400d4c76c919a838be93",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "c78a485403d3a7e80fac6001b55cd4712fa67cad3bfcae9f38cabb4f98958a34",
    "source_record_sha256s": {
      "source_2d4f3a7d3525782c8ff503ee": "ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd"
    },
    "source_state_sha256": "ba7943f3a2a360a280c111d5d4fa02e900c28fd1d0743ff6e719806a54d51020",
    "work_identity_sha256": "2b60f17ed42989e9c34ce5083be81e0c2273482b4dfd868f634d47466fc7e723"
  },
  "consolidation_id": "consolidation_1b354e57057e3430ebb2e459",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:42+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_597",
    "ev_692"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_1b354e57057e3430ebb2e459",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_wechat_embodied_eval_bottleneck_20260715",
  "object_sha256_after": "88038c120451d5a9ef9efed1f080f4d8dd46b6fb3e5c89063996ed6edd4227b5",
  "object_sha256_before": "e0093a83d4246fb4432cac040fdc2456918dc21506e9023e3d9da7fa533ba2ec",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_2d4f3a7d3525782c8ff503ee"
  ],
  "source_records": [
    {
      "raw_content_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e",
      "source_id": "source_2d4f3a7d3525782c8ff503ee",
      "source_record_sha256": "ec1d99aaeb116a409621222a7c17c310a52c111c436cffec3680aa5721d1b2fd",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e"
  ],
  "started_at": "2026-07-17T18:35:42+08:00",
  "status": "complete",
  "title": "Consolidation: 该文称具身 VLA 迭代速度常被真机评估流程而非训练本身卡住",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:42+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
