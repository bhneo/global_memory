---
id: "consolidation_413fb58ed6d3a652c28fb7b6"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: Consecutive hand-object subgoal teleoperation"
created_at: "2026-07-20T13:09:59+08:00"
updated_at: "2026-07-20T13:09:59+08:00"
consolidation_id: "consolidation_413fb58ed6d3a652c28fb7b6"
object_id: "concept_64c23c660c9017a5bf73d012"
object_version_before: 1
object_sha256_before: "f750fece038b18651bb907f71c35a9003f15ad2d81be0772e983bedb15afe4c7"
object_sha256_after: "4945fffd0efb3b6a99e3ce091b7f55642598fb0595c65561568888d4c89a00d4"
source_ids: ["source_570c26541066c02080dd8de5"]
source_sha256s: ["ee5ffe42b301b501a652f72e57d6b0cf62126ee1c93fb5579d7e5951e556ee79"]
source_records: [{"source_id": "source_570c26541066c02080dd8de5", "source_record_sha256": "4465e0679cf2aba77ca16f891f14d1c95d156d5b6b50b1b77c756179d5dc5ec8", "raw_content_sha256": "ee5ffe42b301b501a652f72e57d6b0cf62126ee1c93fb5579d7e5951e556ee79", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-20T13:09:58+08:00"
completed_at: "2026-07-20T13:09:59+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_64c23c660c9017a5bf73d012.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_570c26541066c02080dd8de5 raw_sha256:ee5ffe42b301b501a652f72e57d6b0cf62126ee1c93fb5579d7e5951e556ee79"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_570c26541066c02080dd8de5 record_sha256:4465e0679cf2aba77ca16f891f14d1c95d156d5b6b50b1b77c756179d5dc5ec8"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 2 candidates inspected", "candidate:concept_64c23c660c9017a5bf73d012", "candidate:reflection_631ecd2479bd127e62730569"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_570c26541066c02080dd8de5"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-20T13:09:50+08:00", "source:source_570c26541066c02080dd8de5 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "4945fffd0efb3b6a99e3ce091b7f55642598fb0595c65561568888d4c89a00d4", "source_state_sha256": "99eb9a98009c42620c0131e3701ba7f43dd6b3a1d5017192375ab367b4ed8063", "source_record_sha256s": {"source_570c26541066c02080dd8de5": "4465e0679cf2aba77ca16f891f14d1c95d156d5b6b50b1b77c756179d5dc5ec8"}, "raw_state_sha256": "a1d784bc5c62b95e6dbb3c0b78d981a09792c1025328c778a7eca830d8987ac0", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "a2fb140aea02773ac53db0402a082d27eeb25b6f7884fb7d9afdfd2b03e0e2a7", "relation_fingerprint": {"outgoing_relations_sha256": "fa4d152ff14db53032856ba461747d1a10a2971cf9298786d3f6860a7da6dab2", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "fa4d152ff14db53032856ba461747d1a10a2971cf9298786d3f6860a7da6dab2"}, "relation_neighborhood_sha256": "fa4d152ff14db53032856ba461747d1a10a2971cf9298786d3f6860a7da6dab2", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "refined"
changes: [{"change_type": "refine", "previous_statement": "# Consecutive hand-object subgoal teleoperation\n\nTranslate live human intent into consecutive hand-object co-tracking subgoals, then let a simulation-trained low-level policy choose feasible contact sequences rather than copying every hand joint. The interface supports reorientation, finger gaiting, and tool use but currently depends on reliable hand and object pose tracking.", "new_statement": "# Consecutive hand-object subgoal teleoperation\n\nTranslate live human intent into consecutive hand-object co-tracking subgoals, then let a simulation-trained low-level policy choose feasible contact sequences rather than copying every hand joint. The interface supports reorientation, finger gaiting, and tool use but currently depends on reliable hand and object pose tracking.", "changed_fields": [], "reason": "compile bundle from source_570c26541066c02080dd8de5", "trigger_source": "source_570c26541066c02080dd8de5", "evidence_added": []}]
change_summary: "compile bundle from source_570c26541066c02080dd8de5"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "compile bundle from source_570c26541066c02080dd8de5",
  "changes": [
    {
      "change_type": "refine",
      "changed_fields": [],
      "evidence_added": [],
      "new_statement": "# Consecutive hand-object subgoal teleoperation\n\nTranslate live human intent into consecutive hand-object co-tracking subgoals, then let a simulation-trained low-level policy choose feasible contact sequences rather than copying every hand joint. The interface supports reorientation, finger gaiting, and tool use but currently depends on reliable hand and object pose tracking.",
      "previous_statement": "# Consecutive hand-object subgoal teleoperation\n\nTranslate live human intent into consecutive hand-object co-tracking subgoals, then let a simulation-trained low-level policy choose feasible contact sequences rather than copying every hand joint. The interface supports reorientation, finger gaiting, and tool use but currently depends on reliable hand and object pose tracking.",
      "reason": "compile bundle from source_570c26541066c02080dd8de5",
      "trigger_source": "source_570c26541066c02080dd8de5"
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
        "searched title; 2 candidates inspected",
        "candidate:concept_64c23c660c9017a5bf73d012",
        "candidate:reflection_631ecd2479bd127e62730569"
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
        "object_updated_at:2026-07-20T13:09:50+08:00",
        "source:source_570c26541066c02080dd8de5 work_sha256:none"
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
        "source:source_570c26541066c02080dd8de5 record_sha256:4465e0679cf2aba77ca16f891f14d1c95d156d5b6b50b1b77c756179d5dc5ec8"
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
        "source:source_570c26541066c02080dd8de5 raw_sha256:ee5ffe42b301b501a652f72e57d6b0cf62126ee1c93fb5579d7e5951e556ee79"
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
        "related:source_570c26541066c02080dd8de5"
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
        "validated:vault/memory/concept/concept_64c23c660c9017a5bf73d012.md"
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
  "completed_at": "2026-07-20T13:09:59+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "4945fffd0efb3b6a99e3ce091b7f55642598fb0595c65561568888d4c89a00d4",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "a1d784bc5c62b95e6dbb3c0b78d981a09792c1025328c778a7eca830d8987ac0",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "fa4d152ff14db53032856ba461747d1a10a2971cf9298786d3f6860a7da6dab2",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "fa4d152ff14db53032856ba461747d1a10a2971cf9298786d3f6860a7da6dab2"
    },
    "relation_neighborhood_sha256": "fa4d152ff14db53032856ba461747d1a10a2971cf9298786d3f6860a7da6dab2",
    "source_record_sha256s": {
      "source_570c26541066c02080dd8de5": "4465e0679cf2aba77ca16f891f14d1c95d156d5b6b50b1b77c756179d5dc5ec8"
    },
    "source_state_sha256": "99eb9a98009c42620c0131e3701ba7f43dd6b3a1d5017192375ab367b4ed8063",
    "work_identity_sha256": "a2fb140aea02773ac53db0402a082d27eeb25b6f7884fb7d9afdfd2b03e0e2a7"
  },
  "consolidation_id": "consolidation_413fb58ed6d3a652c28fb7b6",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-20T13:09:59+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_413fb58ed6d3a652c28fb7b6",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_64c23c660c9017a5bf73d012",
  "object_sha256_after": "4945fffd0efb3b6a99e3ce091b7f55642598fb0595c65561568888d4c89a00d4",
  "object_sha256_before": "f750fece038b18651bb907f71c35a9003f15ad2d81be0772e983bedb15afe4c7",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "refined",
  "source_ids": [
    "source_570c26541066c02080dd8de5"
  ],
  "source_records": [
    {
      "raw_content_sha256": "ee5ffe42b301b501a652f72e57d6b0cf62126ee1c93fb5579d7e5951e556ee79",
      "source_id": "source_570c26541066c02080dd8de5",
      "source_record_sha256": "4465e0679cf2aba77ca16f891f14d1c95d156d5b6b50b1b77c756179d5dc5ec8",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "ee5ffe42b301b501a652f72e57d6b0cf62126ee1c93fb5579d7e5951e556ee79"
  ],
  "started_at": "2026-07-20T13:09:58+08:00",
  "status": "complete",
  "title": "Consolidation: Consecutive hand-object subgoal teleoperation",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-20T13:09:59+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
