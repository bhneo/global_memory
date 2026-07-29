---
id: "consolidation_3e66c2ba533cfac1f9cb7696"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: Flow-matching VLA 的流式上下文分区与 KV 缓存 / streaming context partitioning and KV caching for flow-matching VLAs"
created_at: "2026-07-27T19:06:33+08:00"
updated_at: "2026-07-27T19:06:33+08:00"
consolidation_id: "consolidation_3e66c2ba533cfac1f9cb7696"
object_id: "concept_30d85c442682f6afd96c3022"
object_version_before: 1
object_sha256_before: "f114efffccfd333303603854f39af3cd8a28f6059f36614f84dd9652b429b50e"
object_sha256_after: "15f972b420e4f5e51ee83bab80a86494f9a1e25c0c6f0bd246cabbe3caf0c711"
source_ids: ["source_e67cd99ac31c7017d6f7f7c7"]
source_sha256s: ["e6bf3f8db991625e97cf1ba92dae7bc67c58a0f71f0f6b19e045b754ae9e9eed"]
source_records: [{"source_id": "source_e67cd99ac31c7017d6f7f7c7", "source_record_sha256": "b39cccc4c3c583b07b3ff137341d6e86fd28e8da29878723a54e9a9a5820a7d7", "raw_content_sha256": "e6bf3f8db991625e97cf1ba92dae7bc67c58a0f71f0f6b19e045b754ae9e9eed", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-27T19:06:32+08:00"
completed_at: "2026-07-27T19:06:33+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_30d85c442682f6afd96c3022.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_e67cd99ac31c7017d6f7f7c7 raw_sha256:e6bf3f8db991625e97cf1ba92dae7bc67c58a0f71f0f6b19e045b754ae9e9eed"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_e67cd99ac31c7017d6f7f7c7 record_sha256:b39cccc4c3c583b07b3ff137341d6e86fd28e8da29878723a54e9a9a5820a7d7"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_30d85c442682f6afd96c3022"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_e67cd99ac31c7017d6f7f7c7", "related:concept_30d85c442682f6afd96c3022"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-27T17:19:57+08:00", "source:source_e67cd99ac31c7017d6f7f7c7 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "15f972b420e4f5e51ee83bab80a86494f9a1e25c0c6f0bd246cabbe3caf0c711", "source_state_sha256": "8759cd3999abf308b6a3c4c9dcad13770acdc8bd8dfe9edcfc8aad38861ba71e", "source_record_sha256s": {"source_e67cd99ac31c7017d6f7f7c7": "b39cccc4c3c583b07b3ff137341d6e86fd28e8da29878723a54e9a9a5820a7d7"}, "raw_state_sha256": "713e41fcf1501a2eff504ce62ca243beb7ac9670d0da1b6b9f991d3ea0dc6dbf", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "f7926564341349ff8ee1e26656609af99344908fba5b8eb0688044e3ed7d9252", "relation_fingerprint": {"outgoing_relations_sha256": "d727a4e7ae019319db178bdbf727fc021a34bb3202130c08ccfa28c692228b47", "incoming_relations_sha256": "a471fb99da6d0ccb10d4eb5a45c6f81e12f565ba90edef28cf341110c73c6792", "full_neighborhood_sha256": "ffbc056719c20917282da9b3da3d8d80f7805bcec75e625522548b86fddbd8f3"}, "relation_neighborhood_sha256": "ffbc056719c20917282da9b3da3d8d80f7805bcec75e625522548b86fddbd8f3", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_30d85c442682f6afd96c3022"
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
        "object_updated_at:2026-07-27T17:19:57+08:00",
        "source:source_e67cd99ac31c7017d6f7f7c7 work_sha256:none"
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
        "source:source_e67cd99ac31c7017d6f7f7c7 record_sha256:b39cccc4c3c583b07b3ff137341d6e86fd28e8da29878723a54e9a9a5820a7d7"
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
        "source:source_e67cd99ac31c7017d6f7f7c7 raw_sha256:e6bf3f8db991625e97cf1ba92dae7bc67c58a0f71f0f6b19e045b754ae9e9eed"
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
        "related:source_e67cd99ac31c7017d6f7f7c7",
        "related:concept_30d85c442682f6afd96c3022"
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
        "validated:vault/memory/concept/concept_30d85c442682f6afd96c3022.md"
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
  "completed_at": "2026-07-27T19:06:33+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "15f972b420e4f5e51ee83bab80a86494f9a1e25c0c6f0bd246cabbe3caf0c711",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "713e41fcf1501a2eff504ce62ca243beb7ac9670d0da1b6b9f991d3ea0dc6dbf",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "ffbc056719c20917282da9b3da3d8d80f7805bcec75e625522548b86fddbd8f3",
      "incoming_relations_sha256": "a471fb99da6d0ccb10d4eb5a45c6f81e12f565ba90edef28cf341110c73c6792",
      "outgoing_relations_sha256": "d727a4e7ae019319db178bdbf727fc021a34bb3202130c08ccfa28c692228b47"
    },
    "relation_neighborhood_sha256": "ffbc056719c20917282da9b3da3d8d80f7805bcec75e625522548b86fddbd8f3",
    "source_record_sha256s": {
      "source_e67cd99ac31c7017d6f7f7c7": "b39cccc4c3c583b07b3ff137341d6e86fd28e8da29878723a54e9a9a5820a7d7"
    },
    "source_state_sha256": "8759cd3999abf308b6a3c4c9dcad13770acdc8bd8dfe9edcfc8aad38861ba71e",
    "work_identity_sha256": "f7926564341349ff8ee1e26656609af99344908fba5b8eb0688044e3ed7d9252"
  },
  "consolidation_id": "consolidation_3e66c2ba533cfac1f9cb7696",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-27T19:06:33+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_3e66c2ba533cfac1f9cb7696",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_30d85c442682f6afd96c3022",
  "object_sha256_after": "15f972b420e4f5e51ee83bab80a86494f9a1e25c0c6f0bd246cabbe3caf0c711",
  "object_sha256_before": "f114efffccfd333303603854f39af3cd8a28f6059f36614f84dd9652b429b50e",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_e67cd99ac31c7017d6f7f7c7"
  ],
  "source_records": [
    {
      "raw_content_sha256": "e6bf3f8db991625e97cf1ba92dae7bc67c58a0f71f0f6b19e045b754ae9e9eed",
      "source_id": "source_e67cd99ac31c7017d6f7f7c7",
      "source_record_sha256": "b39cccc4c3c583b07b3ff137341d6e86fd28e8da29878723a54e9a9a5820a7d7",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "e6bf3f8db991625e97cf1ba92dae7bc67c58a0f71f0f6b19e045b754ae9e9eed"
  ],
  "started_at": "2026-07-27T19:06:32+08:00",
  "status": "complete",
  "title": "Consolidation: Flow-matching VLA 的流式上下文分区与 KV 缓存 / streaming context partitioning and KV caching for flow-matching VLAs",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-27T19:06:33+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
