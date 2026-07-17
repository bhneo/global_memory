---
id: "consolidation_fd52dccd39789892fba3bb50"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: In small two-layer networks, conserved quantities were observed to correlate with convergence and minima sharpness"
created_at: "2026-07-17T22:39:55+08:00"
updated_at: "2026-07-17T22:39:55+08:00"
consolidation_id: "consolidation_fd52dccd39789892fba3bb50"
object_id: "claim_conserved_quantity_small_network_correlations_20260716"
object_version_before: 1
object_sha256_before: "5e0e45f7a99ad8d322f954231f55ad812cbb144bbf475c0d8f363d8fb6c5b35f"
object_sha256_after: "ef3f17966323b861406d70837aea6d9a8bb58198321f4aaf09a9cacb8f1ca302"
source_ids: ["source_6ae6c4bef52010f96ddb3dbf", "source_dbfef5ee180346812d6d9a99"]
source_sha256s: ["1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "8bd7c3fb4b6c8d6acf6c23a0911cd40c21102c66ebb3e096bc265265d10fb681"]
source_records: [{"source_id": "source_6ae6c4bef52010f96ddb3dbf", "source_record_sha256": "3f51d3e4a3dacc311d2fb7612cd12bbb67bdb9e3b3bd0d4ae351773751fcce83", "raw_content_sha256": "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "work_id": null, "work_document_sha256": null}, {"source_id": "source_dbfef5ee180346812d6d9a99", "source_record_sha256": "8787f67fb3a4837d4490d8b5007c6fc91486108cb14e9fa3527ca6ae8e9a4191", "raw_content_sha256": "8bd7c3fb4b6c8d6acf6c23a0911cd40c21102c66ebb3e096bc265265d10fb681", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_primary_d321a733ab22"]
started_at: "2026-07-17T22:39:54+08:00"
completed_at: "2026-07-17T22:39:55+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/claim/claim_conserved_quantity_small_network_correlations_20260716.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_6ae6c4bef52010f96ddb3dbf raw_sha256:1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "source:source_dbfef5ee180346812d6d9a99 raw_sha256:8bd7c3fb4b6c8d6acf6c23a0911cd40c21102c66ebb3e096bc265265d10fb681"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_6ae6c4bef52010f96ddb3dbf record_sha256:3f51d3e4a3dacc311d2fb7612cd12bbb67bdb9e3b3bd0d4ae351773751fcce83", "source:source_dbfef5ee180346812d6d9a99 record_sha256:8787f67fb3a4837d4490d8b5007c6fc91486108cb14e9fa3527ca6ae8e9a4191"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["evidence:ev_primary_d321a733ab22"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "needs_review", "method": "declared-metadata-inspection", "semantic_recheck_performed": false, "declared_value": "full", "findings": ["evidence_entailment:full"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:claim_conserved_quantity_small_network_correlations_20260716"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_dbfef5ee180346812d6d9a99"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T18:36:49+08:00", "source:source_6ae6c4bef52010f96ddb3dbf work_sha256:none", "source:source_dbfef5ee180346812d6d9a99 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "ef3f17966323b861406d70837aea6d9a8bb58198321f4aaf09a9cacb8f1ca302", "source_state_sha256": "b6df925574113667c7b98aa7d31a0d93ce42be3dd5d7b25790ac1f023a036122", "source_record_sha256s": {"source_6ae6c4bef52010f96ddb3dbf": "3f51d3e4a3dacc311d2fb7612cd12bbb67bdb9e3b3bd0d4ae351773751fcce83", "source_dbfef5ee180346812d6d9a99": "8787f67fb3a4837d4490d8b5007c6fc91486108cb14e9fa3527ca6ae8e9a4191"}, "raw_state_sha256": "f6d58052bd17d9cb95e877e5e6c686de2640216a452440f6a8dec8478336e585", "evidence_sha256": "bcdbbbe06c50702fcfee2231873932909ab2cb3538da8b84d3dcb81cbd877394", "extraction_state_sha256": "d86681e0a62b4a7a3e3053f4e249d4385cd6912b9893986851c37b769de1fa7a", "work_identity_sha256": "842d370c2707a4081a19af512a48fb7c5ec2b4cffff90456a28428db6629887b", "relation_fingerprint": {"outgoing_relations_sha256": "42145061e06adc9a530a7bdb248215c49846b05f7045e5dc0489b3340f21d4a8", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "42145061e06adc9a530a7bdb248215c49846b05f7045e5dc0489b3340f21d4a8"}, "relation_neighborhood_sha256": "42145061e06adc9a530a7bdb248215c49846b05f7045e5dc0489b3340f21d4a8", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_conserved_quantity_small_network_correlations_20260716"
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
        "evidence:ev_primary_d321a733ab22"
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
        "object_updated_at:2026-07-17T18:36:49+08:00",
        "source:source_6ae6c4bef52010f96ddb3dbf work_sha256:none",
        "source:source_dbfef5ee180346812d6d9a99 work_sha256:none"
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
        "source:source_6ae6c4bef52010f96ddb3dbf record_sha256:3f51d3e4a3dacc311d2fb7612cd12bbb67bdb9e3b3bd0d4ae351773751fcce83",
        "source:source_dbfef5ee180346812d6d9a99 record_sha256:8787f67fb3a4837d4490d8b5007c6fc91486108cb14e9fa3527ca6ae8e9a4191"
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
        "source:source_6ae6c4bef52010f96ddb3dbf raw_sha256:1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e",
        "source:source_dbfef5ee180346812d6d9a99 raw_sha256:8bd7c3fb4b6c8d6acf6c23a0911cd40c21102c66ebb3e096bc265265d10fb681"
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
        "related:source_dbfef5ee180346812d6d9a99"
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
        "validated:vault/memory/claim/claim_conserved_quantity_small_network_correlations_20260716.md"
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
  "completed_at": "2026-07-17T22:39:55+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "bcdbbbe06c50702fcfee2231873932909ab2cb3538da8b84d3dcb81cbd877394",
    "extraction_state_sha256": "d86681e0a62b4a7a3e3053f4e249d4385cd6912b9893986851c37b769de1fa7a",
    "memory_schema_version": 2,
    "object_sha256": "ef3f17966323b861406d70837aea6d9a8bb58198321f4aaf09a9cacb8f1ca302",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "f6d58052bd17d9cb95e877e5e6c686de2640216a452440f6a8dec8478336e585",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "42145061e06adc9a530a7bdb248215c49846b05f7045e5dc0489b3340f21d4a8",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "42145061e06adc9a530a7bdb248215c49846b05f7045e5dc0489b3340f21d4a8"
    },
    "relation_neighborhood_sha256": "42145061e06adc9a530a7bdb248215c49846b05f7045e5dc0489b3340f21d4a8",
    "source_record_sha256s": {
      "source_6ae6c4bef52010f96ddb3dbf": "3f51d3e4a3dacc311d2fb7612cd12bbb67bdb9e3b3bd0d4ae351773751fcce83",
      "source_dbfef5ee180346812d6d9a99": "8787f67fb3a4837d4490d8b5007c6fc91486108cb14e9fa3527ca6ae8e9a4191"
    },
    "source_state_sha256": "b6df925574113667c7b98aa7d31a0d93ce42be3dd5d7b25790ac1f023a036122",
    "work_identity_sha256": "842d370c2707a4081a19af512a48fb7c5ec2b4cffff90456a28428db6629887b"
  },
  "consolidation_id": "consolidation_fd52dccd39789892fba3bb50",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-17T22:39:55+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_primary_d321a733ab22"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_fd52dccd39789892fba3bb50",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_conserved_quantity_small_network_correlations_20260716",
  "object_sha256_after": "ef3f17966323b861406d70837aea6d9a8bb58198321f4aaf09a9cacb8f1ca302",
  "object_sha256_before": "5e0e45f7a99ad8d322f954231f55ad812cbb144bbf475c0d8f363d8fb6c5b35f",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "requalification_candidate",
  "source_ids": [
    "source_6ae6c4bef52010f96ddb3dbf",
    "source_dbfef5ee180346812d6d9a99"
  ],
  "source_records": [
    {
      "raw_content_sha256": "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e",
      "source_id": "source_6ae6c4bef52010f96ddb3dbf",
      "source_record_sha256": "3f51d3e4a3dacc311d2fb7612cd12bbb67bdb9e3b3bd0d4ae351773751fcce83",
      "work_document_sha256": null,
      "work_id": null
    },
    {
      "raw_content_sha256": "8bd7c3fb4b6c8d6acf6c23a0911cd40c21102c66ebb3e096bc265265d10fb681",
      "source_id": "source_dbfef5ee180346812d6d9a99",
      "source_record_sha256": "8787f67fb3a4837d4490d8b5007c6fc91486108cb14e9fa3527ca6ae8e9a4191",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e",
    "8bd7c3fb4b6c8d6acf6c23a0911cd40c21102c66ebb3e096bc265265d10fb681"
  ],
  "started_at": "2026-07-17T22:39:54+08:00",
  "status": "complete",
  "title": "Consolidation: In small two-layer networks, conserved quantities were observed to correlate with convergence and minima sharpness",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T22:39:55+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
