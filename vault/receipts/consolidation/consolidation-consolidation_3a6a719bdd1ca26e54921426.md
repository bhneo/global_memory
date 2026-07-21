---
id: "consolidation_3a6a719bdd1ca26e54921426"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: Simulator-validated single-view demonstration transfer"
created_at: "2026-07-20T13:10:27+08:00"
updated_at: "2026-07-20T13:10:27+08:00"
consolidation_id: "consolidation_3a6a719bdd1ca26e54921426"
object_id: "concept_b1b62d103e0a768399664d9d"
object_version_before: 1
object_sha256_before: "3d7fd814b390096585191d5fc4dec2bb0c8ee75a06bddd72601d2bbf1bef4b75"
object_sha256_after: "f03ba30323072e645e33487723b4cba5c478e11b512530f4b6b8cd68cec76d79"
source_ids: ["source_513a527cb4d410e4f94a9bb5"]
source_sha256s: ["2c02222b536db0cc6c26fed247aaf5c792768c1a1ece4c3c650cae03fbbcf331"]
source_records: [{"source_id": "source_513a527cb4d410e4f94a9bb5", "source_record_sha256": "19b9742706b85ee487bfa40e1f1eeba7b0cfeb01412ba1ab2b9c04578888499d", "raw_content_sha256": "2c02222b536db0cc6c26fed247aaf5c792768c1a1ece4c3c650cae03fbbcf331", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-20T13:10:26+08:00"
completed_at: "2026-07-20T13:10:27+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_b1b62d103e0a768399664d9d.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_513a527cb4d410e4f94a9bb5 raw_sha256:2c02222b536db0cc6c26fed247aaf5c792768c1a1ece4c3c650cae03fbbcf331"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_513a527cb4d410e4f94a9bb5 record_sha256:19b9742706b85ee487bfa40e1f1eeba7b0cfeb01412ba1ab2b9c04578888499d"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_b1b62d103e0a768399664d9d"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_513a527cb4d410e4f94a9bb5"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-20T13:10:18+08:00", "source:source_513a527cb4d410e4f94a9bb5 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "f03ba30323072e645e33487723b4cba5c478e11b512530f4b6b8cd68cec76d79", "source_state_sha256": "d7273b545880e45f15582424399b419d81812615c5e486d2ac9c049041d65a9b", "source_record_sha256s": {"source_513a527cb4d410e4f94a9bb5": "19b9742706b85ee487bfa40e1f1eeba7b0cfeb01412ba1ab2b9c04578888499d"}, "raw_state_sha256": "3147c06622c5a4ca391a47c87298fe7ddf0dc1e937ce7426128910783dddd4ca", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "0e6e8594fecdd02688462ab43ae97293a258fc325e40c524ab09873671092176", "relation_fingerprint": {"outgoing_relations_sha256": "150e8c02f2f1bd294422d1d996e97bc7e4a8d316eb80ba97fd406a8dd885eebb", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "150e8c02f2f1bd294422d1d996e97bc7e4a8d316eb80ba97fd406a8dd885eebb"}, "relation_neighborhood_sha256": "150e8c02f2f1bd294422d1d996e97bc7e4a8d316eb80ba97fd406a8dd885eebb", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "refined"
changes: [{"change_type": "refine", "previous_statement": "# Simulator-validated single-view demonstration transfer\n\nConvert a single-view human demonstration into a robot plan through stereo reconstruction, object tracking, collision-aware whole-arm planning, and simulator phase validation with backtracking. The simulator is a feasibility filter, not proof that the reconstructed plan will execute reliably in reality.", "new_statement": "# Simulator-validated single-view demonstration transfer\n\nConvert a single-view human demonstration into a robot plan through stereo reconstruction, object tracking, collision-aware whole-arm planning, and simulator phase validation with backtracking. The simulator is a feasibility filter, not proof that the reconstructed plan will execute reliably in reality.", "changed_fields": [], "reason": "compile bundle from source_513a527cb4d410e4f94a9bb5", "trigger_source": "source_513a527cb4d410e4f94a9bb5", "evidence_added": []}]
change_summary: "compile bundle from source_513a527cb4d410e4f94a9bb5"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "compile bundle from source_513a527cb4d410e4f94a9bb5",
  "changes": [
    {
      "change_type": "refine",
      "changed_fields": [],
      "evidence_added": [],
      "new_statement": "# Simulator-validated single-view demonstration transfer\n\nConvert a single-view human demonstration into a robot plan through stereo reconstruction, object tracking, collision-aware whole-arm planning, and simulator phase validation with backtracking. The simulator is a feasibility filter, not proof that the reconstructed plan will execute reliably in reality.",
      "previous_statement": "# Simulator-validated single-view demonstration transfer\n\nConvert a single-view human demonstration into a robot plan through stereo reconstruction, object tracking, collision-aware whole-arm planning, and simulator phase validation with backtracking. The simulator is a feasibility filter, not proof that the reconstructed plan will execute reliably in reality.",
      "reason": "compile bundle from source_513a527cb4d410e4f94a9bb5",
      "trigger_source": "source_513a527cb4d410e4f94a9bb5"
    }
  ],
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
        "candidate:concept_b1b62d103e0a768399664d9d"
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
        "object_updated_at:2026-07-20T13:10:18+08:00",
        "source:source_513a527cb4d410e4f94a9bb5 work_sha256:none"
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
        "source:source_513a527cb4d410e4f94a9bb5 record_sha256:19b9742706b85ee487bfa40e1f1eeba7b0cfeb01412ba1ab2b9c04578888499d"
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
        "source:source_513a527cb4d410e4f94a9bb5 raw_sha256:2c02222b536db0cc6c26fed247aaf5c792768c1a1ece4c3c650cae03fbbcf331"
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
        "relation index inspected; 1 related objects found",
        "related:source_513a527cb4d410e4f94a9bb5"
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
        "validated:vault/memory/concept/concept_b1b62d103e0a768399664d9d.md"
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
  "completed_at": "2026-07-20T13:10:27+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "f03ba30323072e645e33487723b4cba5c478e11b512530f4b6b8cd68cec76d79",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "3147c06622c5a4ca391a47c87298fe7ddf0dc1e937ce7426128910783dddd4ca",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "150e8c02f2f1bd294422d1d996e97bc7e4a8d316eb80ba97fd406a8dd885eebb",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "150e8c02f2f1bd294422d1d996e97bc7e4a8d316eb80ba97fd406a8dd885eebb"
    },
    "relation_neighborhood_sha256": "150e8c02f2f1bd294422d1d996e97bc7e4a8d316eb80ba97fd406a8dd885eebb",
    "source_record_sha256s": {
      "source_513a527cb4d410e4f94a9bb5": "19b9742706b85ee487bfa40e1f1eeba7b0cfeb01412ba1ab2b9c04578888499d"
    },
    "source_state_sha256": "d7273b545880e45f15582424399b419d81812615c5e486d2ac9c049041d65a9b",
    "work_identity_sha256": "0e6e8594fecdd02688462ab43ae97293a258fc325e40c524ab09873671092176"
  },
  "consolidation_id": "consolidation_3a6a719bdd1ca26e54921426",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-20T13:10:27+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_3a6a719bdd1ca26e54921426",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_b1b62d103e0a768399664d9d",
  "object_sha256_after": "f03ba30323072e645e33487723b4cba5c478e11b512530f4b6b8cd68cec76d79",
  "object_sha256_before": "3d7fd814b390096585191d5fc4dec2bb0c8ee75a06bddd72601d2bbf1bef4b75",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "refined",
  "source_ids": [
    "source_513a527cb4d410e4f94a9bb5"
  ],
  "source_records": [
    {
      "raw_content_sha256": "2c02222b536db0cc6c26fed247aaf5c792768c1a1ece4c3c650cae03fbbcf331",
      "source_id": "source_513a527cb4d410e4f94a9bb5",
      "source_record_sha256": "19b9742706b85ee487bfa40e1f1eeba7b0cfeb01412ba1ab2b9c04578888499d",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "2c02222b536db0cc6c26fed247aaf5c792768c1a1ece4c3c650cae03fbbcf331"
  ],
  "started_at": "2026-07-20T13:10:26+08:00",
  "status": "complete",
  "title": "Consolidation: Simulator-validated single-view demonstration transfer",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-20T13:10:27+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
