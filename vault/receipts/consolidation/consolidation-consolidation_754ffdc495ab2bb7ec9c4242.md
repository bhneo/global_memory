---
id: "consolidation_754ffdc495ab2bb7ec9c4242"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: In small two-layer networks, conserved quantities were observed to correlate with convergence and minima sharpness"
created_at: "2026-07-17T18:35:29+08:00"
updated_at: "2026-07-17T18:35:29+08:00"
consolidation_id: "consolidation_754ffdc495ab2bb7ec9c4242"
object_id: "claim_conserved_quantity_small_network_correlations_20260716"
object_version_before: 1
object_sha256_before: "275ff69d839de24a176ca07d1583d125b056f8df8e46cd0fe6748448748bb0bc"
object_sha256_after: "b76bc5548f37547182ded0feb06a9fcea5fde6532644869b0905457e5572e05d"
source_ids: ["source_6ae6c4bef52010f96ddb3dbf", "source_dbfef5ee180346812d6d9a99"]
source_sha256s: ["1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "8bd7c3fb4b6c8d6acf6c23a0911cd40c21102c66ebb3e096bc265265d10fb681"]
source_records: [{"source_id": "source_6ae6c4bef52010f96ddb3dbf", "source_record_sha256": "3f51d3e4a3dacc311d2fb7612cd12bbb67bdb9e3b3bd0d4ae351773751fcce83", "raw_content_sha256": "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "work_id": null, "work_document_sha256": null}, {"source_id": "source_dbfef5ee180346812d6d9a99", "source_record_sha256": "8787f67fb3a4837d4490d8b5007c6fc91486108cb14e9fa3527ca6ae8e9a4191", "raw_content_sha256": "8bd7c3fb4b6c8d6acf6c23a0911cd40c21102c66ebb3e096bc265265d10fb681", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["ev_primary_d321a733ab22"]
started_at: "2026-07-17T18:35:29+08:00"
completed_at: "2026-07-17T18:35:29+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_conserved_quantity_small_network_correlations_20260716.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_6ae6c4bef52010f96ddb3dbf raw_sha256:1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "source:source_dbfef5ee180346812d6d9a99 raw_sha256:8bd7c3fb4b6c8d6acf6c23a0911cd40c21102c66ebb3e096bc265265d10fb681"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_6ae6c4bef52010f96ddb3dbf record_sha256:3f51d3e4a3dacc311d2fb7612cd12bbb67bdb9e3b3bd0d4ae351773751fcce83", "source:source_dbfef5ee180346812d6d9a99 record_sha256:8787f67fb3a4837d4490d8b5007c6fc91486108cb14e9fa3527ca6ae8e9a4191"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:ev_primary_d321a733ab22"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:full"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_conserved_quantity_small_network_correlations_20260716"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_dbfef5ee180346812d6d9a99"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T18:17:30+08:00", "source:source_6ae6c4bef52010f96ddb3dbf work_sha256:none", "source:source_dbfef5ee180346812d6d9a99 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "b76bc5548f37547182ded0feb06a9fcea5fde6532644869b0905457e5572e05d", "source_state_sha256": "b6df925574113667c7b98aa7d31a0d93ce42be3dd5d7b25790ac1f023a036122", "source_record_sha256s": {"source_6ae6c4bef52010f96ddb3dbf": "3f51d3e4a3dacc311d2fb7612cd12bbb67bdb9e3b3bd0d4ae351773751fcce83", "source_dbfef5ee180346812d6d9a99": "8787f67fb3a4837d4490d8b5007c6fc91486108cb14e9fa3527ca6ae8e9a4191"}, "raw_state_sha256": "f6d58052bd17d9cb95e877e5e6c686de2640216a452440f6a8dec8478336e585", "evidence_sha256": "bcdbbbe06c50702fcfee2231873932909ab2cb3538da8b84d3dcb81cbd877394", "extraction_state_sha256": "d86681e0a62b4a7a3e3053f4e249d4385cd6912b9893986851c37b769de1fa7a", "work_identity_sha256": "842d370c2707a4081a19af512a48fb7c5ec2b4cffff90456a28428db6629887b", "relation_neighborhood_sha256": "9f4173d82d1418371f11068a7ca9e3679b6742245f8fb2e4717e0006e8e72b07", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_conserved_quantity_small_network_correlations_20260716"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "findings": [
        "evidence_entailment:full"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_revalidated": {
      "findings": [
        "evidence:ev_primary_d321a733ab22"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T18:17:30+08:00",
        "source:source_6ae6c4bef52010f96ddb3dbf work_sha256:none",
        "source:source_dbfef5ee180346812d6d9a99 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_6ae6c4bef52010f96ddb3dbf record_sha256:3f51d3e4a3dacc311d2fb7612cd12bbb67bdb9e3b3bd0d4ae351773751fcce83",
        "source:source_dbfef5ee180346812d6d9a99 record_sha256:8787f67fb3a4837d4490d8b5007c6fc91486108cb14e9fa3527ca6ae8e9a4191"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_6ae6c4bef52010f96ddb3dbf raw_sha256:1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e",
        "source:source_dbfef5ee180346812d6d9a99 raw_sha256:8bd7c3fb4b6c8d6acf6c23a0911cd40c21102c66ebb3e096bc265265d10fb681"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_dbfef5ee180346812d6d9a99"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_conserved_quantity_small_network_correlations_20260716.md"
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
  "completed_at": "2026-07-17T18:35:29+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "bcdbbbe06c50702fcfee2231873932909ab2cb3538da8b84d3dcb81cbd877394",
    "extraction_state_sha256": "d86681e0a62b4a7a3e3053f4e249d4385cd6912b9893986851c37b769de1fa7a",
    "memory_schema_version": 2,
    "object_sha256": "b76bc5548f37547182ded0feb06a9fcea5fde6532644869b0905457e5572e05d",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "f6d58052bd17d9cb95e877e5e6c686de2640216a452440f6a8dec8478336e585",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "9f4173d82d1418371f11068a7ca9e3679b6742245f8fb2e4717e0006e8e72b07",
    "source_record_sha256s": {
      "source_6ae6c4bef52010f96ddb3dbf": "3f51d3e4a3dacc311d2fb7612cd12bbb67bdb9e3b3bd0d4ae351773751fcce83",
      "source_dbfef5ee180346812d6d9a99": "8787f67fb3a4837d4490d8b5007c6fc91486108cb14e9fa3527ca6ae8e9a4191"
    },
    "source_state_sha256": "b6df925574113667c7b98aa7d31a0d93ce42be3dd5d7b25790ac1f023a036122",
    "work_identity_sha256": "842d370c2707a4081a19af512a48fb7c5ec2b4cffff90456a28428db6629887b"
  },
  "consolidation_id": "consolidation_754ffdc495ab2bb7ec9c4242",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:29+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "ev_primary_d321a733ab22"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_754ffdc495ab2bb7ec9c4242",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_conserved_quantity_small_network_correlations_20260716",
  "object_sha256_after": "b76bc5548f37547182ded0feb06a9fcea5fde6532644869b0905457e5572e05d",
  "object_sha256_before": "275ff69d839de24a176ca07d1583d125b056f8df8e46cd0fe6748448748bb0bc",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
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
  "started_at": "2026-07-17T18:35:29+08:00",
  "status": "complete",
  "title": "Consolidation: In small two-layer networks, conserved quantities were observed to correlate with convergence and minima sharpness",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:29+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
