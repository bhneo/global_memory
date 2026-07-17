---
id: "consolidation_0992b387cb3eded6d770149a"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 该文称不均匀「磁瓶/磁镜」磁场可通过磁矩近似守恒约束带电粒子纵向与横向运动"
created_at: "2026-07-17T18:35:48+08:00"
updated_at: "2026-07-17T18:35:48+08:00"
consolidation_id: "consolidation_0992b387cb3eded6d770149a"
object_id: "claim_wechat_magnetic_bottle_constraint_20260715"
object_version_before: 1
object_sha256_before: "1d9f40d0b85f4b12a5796b63db1c9f502f7fa376ef0426d928dfc20f82ee662a"
object_sha256_after: "4f3c9c8513c09e40d8893f003f876f8b49ba3c576b597208ca56d76bc159fd6a"
source_ids: ["source_9bd3bdfb9a5b1a728c3adf25"]
source_sha256s: ["acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669"]
source_records: [{"source_id": "source_9bd3bdfb9a5b1a728c3adf25", "source_record_sha256": "550eb0e2721e216ab01f3547f7b15ac0d7004a01e770c54161c5cb83c0ebcf13", "raw_content_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_1184", "ev_1609", "ev_1733"]
started_at: "2026-07-17T18:35:48+08:00"
completed_at: "2026-07-17T18:35:48+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_wechat_magnetic_bottle_constraint_20260715.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_9bd3bdfb9a5b1a728c3adf25 raw_sha256:acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_9bd3bdfb9a5b1a728c3adf25 record_sha256:550eb0e2721e216ab01f3547f7b15ac0d7004a01e770c54161c5cb83c0ebcf13"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:ev_1184", "evidence:ev_1609", "evidence:ev_1733"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:partial"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_wechat_magnetic_bottle_constraint_20260715"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_9bd3bdfb9a5b1a728c3adf25"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:55+08:00", "source:source_9bd3bdfb9a5b1a728c3adf25 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "4f3c9c8513c09e40d8893f003f876f8b49ba3c576b597208ca56d76bc159fd6a", "source_state_sha256": "437c404268131e64236095ad976ec868226f163d71020e3d3f99f59a01d7165f", "source_record_sha256s": {"source_9bd3bdfb9a5b1a728c3adf25": "550eb0e2721e216ab01f3547f7b15ac0d7004a01e770c54161c5cb83c0ebcf13"}, "raw_state_sha256": "9a3064c3209719c29bd3453dda7129469cbe9feb901beca52cb65ba5320f419f", "evidence_sha256": "326d2c21241328882c503ba4e31b2bcdbbf7ee251a70ba329b5891581892d60d", "extraction_state_sha256": "0197025dad89717c61236f5f688fea2a3176c5213730b44e0296a9da6bbadbd7", "work_identity_sha256": "3c27990019c25f55b500af76b34a18cd74b585afd49d77eac7a4ca6db253cf15", "relation_neighborhood_sha256": "d72c379c5f75566e278c7c220003b30aa377a9a9e642c7221436dbe35a11c104", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_wechat_magnetic_bottle_constraint_20260715"
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
        "evidence:ev_1184",
        "evidence:ev_1609",
        "evidence:ev_1733"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:55+08:00",
        "source:source_9bd3bdfb9a5b1a728c3adf25 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_9bd3bdfb9a5b1a728c3adf25 record_sha256:550eb0e2721e216ab01f3547f7b15ac0d7004a01e770c54161c5cb83c0ebcf13"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_9bd3bdfb9a5b1a728c3adf25 raw_sha256:acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_9bd3bdfb9a5b1a728c3adf25"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_wechat_magnetic_bottle_constraint_20260715.md"
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
  "completed_at": "2026-07-17T18:35:48+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "326d2c21241328882c503ba4e31b2bcdbbf7ee251a70ba329b5891581892d60d",
    "extraction_state_sha256": "0197025dad89717c61236f5f688fea2a3176c5213730b44e0296a9da6bbadbd7",
    "memory_schema_version": 2,
    "object_sha256": "4f3c9c8513c09e40d8893f003f876f8b49ba3c576b597208ca56d76bc159fd6a",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "9a3064c3209719c29bd3453dda7129469cbe9feb901beca52cb65ba5320f419f",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "d72c379c5f75566e278c7c220003b30aa377a9a9e642c7221436dbe35a11c104",
    "source_record_sha256s": {
      "source_9bd3bdfb9a5b1a728c3adf25": "550eb0e2721e216ab01f3547f7b15ac0d7004a01e770c54161c5cb83c0ebcf13"
    },
    "source_state_sha256": "437c404268131e64236095ad976ec868226f163d71020e3d3f99f59a01d7165f",
    "work_identity_sha256": "3c27990019c25f55b500af76b34a18cd74b585afd49d77eac7a4ca6db253cf15"
  },
  "consolidation_id": "consolidation_0992b387cb3eded6d770149a",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:48+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_1184",
    "ev_1609",
    "ev_1733"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_0992b387cb3eded6d770149a",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_wechat_magnetic_bottle_constraint_20260715",
  "object_sha256_after": "4f3c9c8513c09e40d8893f003f876f8b49ba3c576b597208ca56d76bc159fd6a",
  "object_sha256_before": "1d9f40d0b85f4b12a5796b63db1c9f502f7fa376ef0426d928dfc20f82ee662a",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_9bd3bdfb9a5b1a728c3adf25"
  ],
  "source_records": [
    {
      "raw_content_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669",
      "source_id": "source_9bd3bdfb9a5b1a728c3adf25",
      "source_record_sha256": "550eb0e2721e216ab01f3547f7b15ac0d7004a01e770c54161c5cb83c0ebcf13",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669"
  ],
  "started_at": "2026-07-17T18:35:48+08:00",
  "status": "complete",
  "title": "Consolidation: 该文称不均匀「磁瓶/磁镜」磁场可通过磁矩近似守恒约束带电粒子纵向与横向运动",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:48+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
