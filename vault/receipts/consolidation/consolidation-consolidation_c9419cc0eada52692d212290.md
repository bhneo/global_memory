---
id: "consolidation_c9419cc0eada52692d212290"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 比较数据集覆盖与真实部署轨迹覆盖"
created_at: "2026-07-17T18:36:02+08:00"
updated_at: "2026-07-17T18:36:02+08:00"
consolidation_id: "consolidation_c9419cc0eada52692d212290"
object_id: "experiment_dataset_trajectory_coverage"
object_version_before: 1
object_sha256_before: "fd8e742e515f785fbae2716fc238380531ff48e8b438270d01b47b65f9029bf4"
object_sha256_after: "00e05f6fb779127a492942ecd841ff16dc08832706d984b69515ea6cee8074fd"
source_ids: ["source_9d39636775b188c87d6a001f", "source_0a113baae7ce4d1ab78da1a3"]
source_sha256s: ["0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c"]
source_records: [{"source_id": "source_9d39636775b188c87d6a001f", "source_record_sha256": "8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78", "raw_content_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "work_id": null, "work_document_sha256": null}, {"source_id": "source_0a113baae7ce4d1ab78da1a3", "source_record_sha256": "7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd", "raw_content_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-17T18:36:01+08:00"
completed_at: "2026-07-17T18:36:02+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/experiment/experiment_dataset_trajectory_coverage.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_9d39636775b188c87d6a001f raw_sha256:0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "source:source_0a113baae7ce4d1ab78da1a3 raw_sha256:5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_9d39636775b188c87d6a001f record_sha256:8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78", "source:source_0a113baae7ce4d1ab78da1a3 record_sha256:7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:experiment_dataset_trajectory_coverage"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 4 related objects found", "related:project_embodied_agent_learning_candidate", "related:source_0a113baae7ce4d1ab78da1a3", "related:source_9d39636775b188c87d6a001f", "related:hypothesis_ergodicity_offline_coverage"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:24:05+08:00", "source:source_9d39636775b188c87d6a001f work_sha256:none", "source:source_0a113baae7ce4d1ab78da1a3 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "00e05f6fb779127a492942ecd841ff16dc08832706d984b69515ea6cee8074fd", "source_state_sha256": "bf695fc3cf604df0be285e92c6693cf87e8265f5b8f65ca84ee5673204b549d9", "source_record_sha256s": {"source_9d39636775b188c87d6a001f": "8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78", "source_0a113baae7ce4d1ab78da1a3": "7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd"}, "raw_state_sha256": "76bc42f1311235b79be0e6599977b78d1f1e3f8ddae6be52f21c4703bde66726", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "f203408792291316dee3a419c0cc80199534aa90a061bd57d8629d0cf111b083", "relation_neighborhood_sha256": "be37475ee4fc2b71335884e0dfefc8537458cc4b860b002d2cb275c6f5cbc346", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:experiment_dataset_trajectory_coverage"
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
        "object_updated_at:2026-07-17T15:24:05+08:00",
        "source:source_9d39636775b188c87d6a001f work_sha256:none",
        "source:source_0a113baae7ce4d1ab78da1a3 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_9d39636775b188c87d6a001f record_sha256:8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78",
        "source:source_0a113baae7ce4d1ab78da1a3 record_sha256:7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_9d39636775b188c87d6a001f raw_sha256:0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33",
        "source:source_0a113baae7ce4d1ab78da1a3 raw_sha256:5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 4 related objects found",
        "related:project_embodied_agent_learning_candidate",
        "related:source_0a113baae7ce4d1ab78da1a3",
        "related:source_9d39636775b188c87d6a001f",
        "related:hypothesis_ergodicity_offline_coverage"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/experiment/experiment_dataset_trajectory_coverage.md"
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
  "completed_at": "2026-07-17T18:36:02+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "00e05f6fb779127a492942ecd841ff16dc08832706d984b69515ea6cee8074fd",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "76bc42f1311235b79be0e6599977b78d1f1e3f8ddae6be52f21c4703bde66726",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "be37475ee4fc2b71335884e0dfefc8537458cc4b860b002d2cb275c6f5cbc346",
    "source_record_sha256s": {
      "source_0a113baae7ce4d1ab78da1a3": "7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd",
      "source_9d39636775b188c87d6a001f": "8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78"
    },
    "source_state_sha256": "bf695fc3cf604df0be285e92c6693cf87e8265f5b8f65ca84ee5673204b549d9",
    "work_identity_sha256": "f203408792291316dee3a419c0cc80199534aa90a061bd57d8629d0cf111b083"
  },
  "consolidation_id": "consolidation_c9419cc0eada52692d212290",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:36:02+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_c9419cc0eada52692d212290",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "experiment_dataset_trajectory_coverage",
  "object_sha256_after": "00e05f6fb779127a492942ecd841ff16dc08832706d984b69515ea6cee8074fd",
  "object_sha256_before": "fd8e742e515f785fbae2716fc238380531ff48e8b438270d01b47b65f9029bf4",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_9d39636775b188c87d6a001f",
    "source_0a113baae7ce4d1ab78da1a3"
  ],
  "source_records": [
    {
      "raw_content_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33",
      "source_id": "source_9d39636775b188c87d6a001f",
      "source_record_sha256": "8e6bd3e8415516df1001862b99f779cb3fb641232ffa75638c9a47b825da3b78",
      "work_document_sha256": null,
      "work_id": null
    },
    {
      "raw_content_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c",
      "source_id": "source_0a113baae7ce4d1ab78da1a3",
      "source_record_sha256": "7e61c0b7be59b525845c74e604165f57ff3c90c5b84777a438c34dbcc6edf1cd",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33",
    "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c"
  ],
  "started_at": "2026-07-17T18:36:01+08:00",
  "status": "complete",
  "title": "Consolidation: 比较数据集覆盖与真实部署轨迹覆盖",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:36:02+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
