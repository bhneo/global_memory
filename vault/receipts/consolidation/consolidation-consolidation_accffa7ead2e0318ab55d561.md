---
id: "consolidation_accffa7ead2e0318ab55d561"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: Epiplexity is the program length in the compute-bounded minimum two-part description of a random variable"
created_at: "2026-07-17T22:40:00+08:00"
updated_at: "2026-07-17T22:40:00+08:00"
consolidation_id: "consolidation_accffa7ead2e0318ab55d561"
object_id: "claim_wechat_epiplexity_definition_20260715"
object_version_before: 1
object_sha256_before: "9d9a2e0e21dc4d5b59363237cdf0c5ad25011f7cb75a95fa3e204f208395bf3b"
object_sha256_after: "c16591290d2e153b2bc68b087b8a1a64f33ca97b9fff4886c2eed331e0d49ebc"
source_ids: ["source_494ab02c17c5f495f1ed29d0", "source_1c0f944bf6b14cf9d1fff939"]
source_sha256s: ["40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c"]
source_records: [{"source_id": "source_494ab02c17c5f495f1ed29d0", "source_record_sha256": "c83384117be8883eece5b9a9da6bcaa1a577c8bb2f8555efa162bc42cf1cf8cb", "raw_content_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "work_id": null, "work_document_sha256": null}, {"source_id": "source_1c0f944bf6b14cf9d1fff939", "source_record_sha256": "0a2d70b38b3383e6aa78f3bbbba3f3602921cbf2890fbd2c497bd2921ef4ef6f", "raw_content_sha256": "8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_primary_f7df8420e167", "ev_primary_749ece9a1660"]
started_at: "2026-07-17T22:39:59+08:00"
completed_at: "2026-07-17T22:40:00+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/claim/claim_wechat_epiplexity_definition_20260715.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_494ab02c17c5f495f1ed29d0 raw_sha256:40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "source:source_1c0f944bf6b14cf9d1fff939 raw_sha256:8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_494ab02c17c5f495f1ed29d0 record_sha256:c83384117be8883eece5b9a9da6bcaa1a577c8bb2f8555efa162bc42cf1cf8cb", "source:source_1c0f944bf6b14cf9d1fff939 record_sha256:0a2d70b38b3383e6aa78f3bbbba3f3602921cbf2890fbd2c497bd2921ef4ef6f"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["evidence:ev_primary_f7df8420e167", "evidence:ev_primary_749ece9a1660"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "needs_review", "method": "declared-metadata-inspection", "semantic_recheck_performed": false, "declared_value": "full", "findings": ["evidence_entailment:full"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:claim_wechat_epiplexity_definition_20260715"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_1c0f944bf6b14cf9d1fff939", "related:source_494ab02c17c5f495f1ed29d0"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T18:38:14+08:00", "source:source_494ab02c17c5f495f1ed29d0 work_sha256:none", "source:source_1c0f944bf6b14cf9d1fff939 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "c16591290d2e153b2bc68b087b8a1a64f33ca97b9fff4886c2eed331e0d49ebc", "source_state_sha256": "6bfdca68392a93d0ac849d57a51be71d442d23cfc66fd13895ba425de9aed30f", "source_record_sha256s": {"source_494ab02c17c5f495f1ed29d0": "c83384117be8883eece5b9a9da6bcaa1a577c8bb2f8555efa162bc42cf1cf8cb", "source_1c0f944bf6b14cf9d1fff939": "0a2d70b38b3383e6aa78f3bbbba3f3602921cbf2890fbd2c497bd2921ef4ef6f"}, "raw_state_sha256": "5ddc55307a191af8a8549035fea61f5137f443afe0f6c32c1456f1a64fa00eaf", "evidence_sha256": "6f916ba7da4c7cf682a1317d80d19a985a30a21f11dca1d22b58eda387855627", "extraction_state_sha256": "2f49da3d12006455e949374aee9b319b55eba88c1619d6ea35746bd6599c3de1", "work_identity_sha256": "2afba82629235278445cf5206d683a77e404c58418dfbdec66192833989baa3d", "relation_fingerprint": {"outgoing_relations_sha256": "eae3025d0580792c5c73cc3e26aa717b6f5f52af958621b42cd4ebc75c0b8668", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "eae3025d0580792c5c73cc3e26aa717b6f5f52af958621b42cd4ebc75c0b8668"}, "relation_neighborhood_sha256": "eae3025d0580792c5c73cc3e26aa717b6f5f52af958621b42cd4ebc75c0b8668", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_wechat_epiplexity_definition_20260715"
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
      "semantic_recheck_performed": false,
      "validation_outcome": "needs_review",
      "warnings": []
    },
    "evidence_revalidated": {
      "check_name": "evidence_revalidated",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "evidence:ev_primary_f7df8420e167",
        "evidence:ev_primary_749ece9a1660"
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
        "object_updated_at:2026-07-17T18:38:14+08:00",
        "source:source_494ab02c17c5f495f1ed29d0 work_sha256:none",
        "source:source_1c0f944bf6b14cf9d1fff939 work_sha256:none"
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
        "source:source_494ab02c17c5f495f1ed29d0 record_sha256:c83384117be8883eece5b9a9da6bcaa1a577c8bb2f8555efa162bc42cf1cf8cb",
        "source:source_1c0f944bf6b14cf9d1fff939 record_sha256:0a2d70b38b3383e6aa78f3bbbba3f3602921cbf2890fbd2c497bd2921ef4ef6f"
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
        "source:source_494ab02c17c5f495f1ed29d0 raw_sha256:40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d",
        "source:source_1c0f944bf6b14cf9d1fff939 raw_sha256:8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c"
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
        "related:source_1c0f944bf6b14cf9d1fff939",
        "related:source_494ab02c17c5f495f1ed29d0"
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
        "validated:vault/memory/claim/claim_wechat_epiplexity_definition_20260715.md"
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
        "distinct_source_ids:2",
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
  "completed_at": "2026-07-17T22:40:00+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "6f916ba7da4c7cf682a1317d80d19a985a30a21f11dca1d22b58eda387855627",
    "extraction_state_sha256": "2f49da3d12006455e949374aee9b319b55eba88c1619d6ea35746bd6599c3de1",
    "memory_schema_version": 2,
    "object_sha256": "c16591290d2e153b2bc68b087b8a1a64f33ca97b9fff4886c2eed331e0d49ebc",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "5ddc55307a191af8a8549035fea61f5137f443afe0f6c32c1456f1a64fa00eaf",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "eae3025d0580792c5c73cc3e26aa717b6f5f52af958621b42cd4ebc75c0b8668",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "eae3025d0580792c5c73cc3e26aa717b6f5f52af958621b42cd4ebc75c0b8668"
    },
    "relation_neighborhood_sha256": "eae3025d0580792c5c73cc3e26aa717b6f5f52af958621b42cd4ebc75c0b8668",
    "source_record_sha256s": {
      "source_1c0f944bf6b14cf9d1fff939": "0a2d70b38b3383e6aa78f3bbbba3f3602921cbf2890fbd2c497bd2921ef4ef6f",
      "source_494ab02c17c5f495f1ed29d0": "c83384117be8883eece5b9a9da6bcaa1a577c8bb2f8555efa162bc42cf1cf8cb"
    },
    "source_state_sha256": "6bfdca68392a93d0ac849d57a51be71d442d23cfc66fd13895ba425de9aed30f",
    "work_identity_sha256": "2afba82629235278445cf5206d683a77e404c58418dfbdec66192833989baa3d"
  },
  "consolidation_id": "consolidation_accffa7ead2e0318ab55d561",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-17T22:40:00+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_primary_f7df8420e167",
    "ev_primary_749ece9a1660"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_accffa7ead2e0318ab55d561",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_wechat_epiplexity_definition_20260715",
  "object_sha256_after": "c16591290d2e153b2bc68b087b8a1a64f33ca97b9fff4886c2eed331e0d49ebc",
  "object_sha256_before": "9d9a2e0e21dc4d5b59363237cdf0c5ad25011f7cb75a95fa3e204f208395bf3b",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "requalification_candidate",
  "source_ids": [
    "source_494ab02c17c5f495f1ed29d0",
    "source_1c0f944bf6b14cf9d1fff939"
  ],
  "source_records": [
    {
      "raw_content_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d",
      "source_id": "source_494ab02c17c5f495f1ed29d0",
      "source_record_sha256": "c83384117be8883eece5b9a9da6bcaa1a577c8bb2f8555efa162bc42cf1cf8cb",
      "work_document_sha256": null,
      "work_id": null
    },
    {
      "raw_content_sha256": "8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c",
      "source_id": "source_1c0f944bf6b14cf9d1fff939",
      "source_record_sha256": "0a2d70b38b3383e6aa78f3bbbba3f3602921cbf2890fbd2c497bd2921ef4ef6f",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d",
    "8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c"
  ],
  "started_at": "2026-07-17T22:39:59+08:00",
  "status": "complete",
  "title": "Consolidation: Epiplexity is the program length in the compute-bounded minimum two-part description of a random variable",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T22:40:00+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
