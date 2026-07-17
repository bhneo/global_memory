---
id: "consolidation_a7ae4bfca4d642594d755333"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 李群与不变量 ↔ 技能组合和形态迁移"
created_at: "2026-07-17T22:39:54+08:00"
updated_at: "2026-07-17T22:39:54+08:00"
consolidation_id: "consolidation_a7ae4bfca4d642594d755333"
object_id: "analogy_lie_group_skill_transfer"
object_version_before: 1
object_sha256_before: "bc07af620f7326e5adea2ae51e6a8d6ad2dbb677e3a17a226bf83b08befdefd9"
object_sha256_after: "d2dd1f0b81686debb2e5f9e4209e8c6119437fbe767d13dc1310864b2c6b2c4c"
source_ids: ["source_941321d95232028c233c9433"]
source_sha256s: ["8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11"]
source_records: [{"source_id": "source_941321d95232028c233c9433", "source_record_sha256": "4235eb18ab1344c8420e011b715135652f70af5e3bf5b383c55f13c1f6ec3047", "raw_content_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-17T22:39:54+08:00"
completed_at: "2026-07-17T22:39:54+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/analogy/analogy_lie_group_skill_transfer.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_941321d95232028c233c9433 raw_sha256:8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_941321d95232028c233c9433 record_sha256:4235eb18ab1344c8420e011b715135652f70af5e3bf5b383c55f13c1f6ec3047"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:analogy_lie_group_skill_transfer"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 3 related objects found", "related:concept_lie_group", "related:concept_skill_evolution", "related:source_941321d95232028c233c9433"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T18:36:43+08:00", "source:source_941321d95232028c233c9433 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "d2dd1f0b81686debb2e5f9e4209e8c6119437fbe767d13dc1310864b2c6b2c4c", "source_state_sha256": "7f51d24958aa924cea63d040d5557fd0880382af4654afae991c487c7b162589", "source_record_sha256s": {"source_941321d95232028c233c9433": "4235eb18ab1344c8420e011b715135652f70af5e3bf5b383c55f13c1f6ec3047"}, "raw_state_sha256": "39c4d0b4266a2cc3df4c4344b8434aaa6a165805b1c2d72c342cfdf09f6703eb", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "4b365a8eb957ec37c58710a68910b973b403b05ec87eae5a39ac9f24e3e13898", "relation_fingerprint": {"outgoing_relations_sha256": "dae70e2e427c6b3945ff81e9b70ddb1dce206587adb316a84ec47649fee0c51f", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "dae70e2e427c6b3945ff81e9b70ddb1dce206587adb316a84ec47649fee0c51f"}, "relation_neighborhood_sha256": "dae70e2e427c6b3945ff81e9b70ddb1dce206587adb316a84ec47649fee0c51f", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "requalification_candidate"
changes: []
change_summary: "Receipt v2 revalidated under incoming and outgoing relation fingerprint boundary"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "Receipt v2 revalidated under incoming and outgoing relation fingerprint boundary",
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
        "candidate:analogy_lie_group_skill_transfer"
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
        "object_updated_at:2026-07-17T18:36:43+08:00",
        "source:source_941321d95232028c233c9433 work_sha256:none"
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
        "source:source_941321d95232028c233c9433 record_sha256:4235eb18ab1344c8420e011b715135652f70af5e3bf5b383c55f13c1f6ec3047"
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
        "source:source_941321d95232028c233c9433 raw_sha256:8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11"
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
        "relation index inspected; 3 related objects found",
        "related:concept_lie_group",
        "related:concept_skill_evolution",
        "related:source_941321d95232028c233c9433"
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
        "validated:vault/memory/analogy/analogy_lie_group_skill_transfer.md"
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
  "completed_at": "2026-07-17T22:39:54+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "d2dd1f0b81686debb2e5f9e4209e8c6119437fbe767d13dc1310864b2c6b2c4c",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "39c4d0b4266a2cc3df4c4344b8434aaa6a165805b1c2d72c342cfdf09f6703eb",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "dae70e2e427c6b3945ff81e9b70ddb1dce206587adb316a84ec47649fee0c51f",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "dae70e2e427c6b3945ff81e9b70ddb1dce206587adb316a84ec47649fee0c51f"
    },
    "relation_neighborhood_sha256": "dae70e2e427c6b3945ff81e9b70ddb1dce206587adb316a84ec47649fee0c51f",
    "source_record_sha256s": {
      "source_941321d95232028c233c9433": "4235eb18ab1344c8420e011b715135652f70af5e3bf5b383c55f13c1f6ec3047"
    },
    "source_state_sha256": "7f51d24958aa924cea63d040d5557fd0880382af4654afae991c487c7b162589",
    "work_identity_sha256": "4b365a8eb957ec37c58710a68910b973b403b05ec87eae5a39ac9f24e3e13898"
  },
  "consolidation_id": "consolidation_a7ae4bfca4d642594d755333",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-17T22:39:54+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_a7ae4bfca4d642594d755333",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "analogy_lie_group_skill_transfer",
  "object_sha256_after": "d2dd1f0b81686debb2e5f9e4209e8c6119437fbe767d13dc1310864b2c6b2c4c",
  "object_sha256_before": "bc07af620f7326e5adea2ae51e6a8d6ad2dbb677e3a17a226bf83b08befdefd9",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "requalification_candidate",
  "source_ids": [
    "source_941321d95232028c233c9433"
  ],
  "source_records": [
    {
      "raw_content_sha256": "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11",
      "source_id": "source_941321d95232028c233c9433",
      "source_record_sha256": "4235eb18ab1344c8420e011b715135652f70af5e3bf5b383c55f13c1f6ec3047",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "8ca515527b4c45ba7d9cbf931b4ab5dabc90b09436d73da21ad290ce9ea15d11"
  ],
  "started_at": "2026-07-17T22:39:54+08:00",
  "status": "complete",
  "title": "Consolidation: 李群与不变量 ↔ 技能组合和形态迁移",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T22:39:54+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
