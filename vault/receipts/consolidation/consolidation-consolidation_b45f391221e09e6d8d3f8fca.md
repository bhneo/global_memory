---
id: "consolidation_b45f391221e09e6d8d3f8fca"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 陈旧性对齐与上下文分区共同约束异步快慢控制接口"
created_at: "2026-08-02T12:30:47+08:00"
updated_at: "2026-08-02T12:30:47+08:00"
consolidation_id: "consolidation_b45f391221e09e6d8d3f8fca"
object_id: "concept_a858f8d191d3afdd69418471"
object_version_before: 1
object_sha256_before: "ce16441921488725434ce8b7e55db7b9d8d6768821b63217582b325b22195f70"
object_sha256_after: "a1154b5cd1993d88fdf6f1c6e583014fba1f40774a89984f3131245357cfc6fa"
source_ids: ["source_d4762e0cf2330ab6ea00a521", "source_e67cd99ac31c7017d6f7f7c7"]
source_sha256s: ["f8d363f6a631f9a6f28ebfffeb5f9d1cd19b9f8bec643ecf54bcd8744deb0b35", "e6bf3f8db991625e97cf1ba92dae7bc67c58a0f71f0f6b19e045b754ae9e9eed"]
source_records: [{"source_id": "source_d4762e0cf2330ab6ea00a521", "source_record_sha256": "b286871c8d1940a63a2092ab31eee35237324336a980824860aefd75aa69ce4a", "raw_content_sha256": "f8d363f6a631f9a6f28ebfffeb5f9d1cd19b9f8bec643ecf54bcd8744deb0b35", "work_id": null, "work_document_sha256": null}, {"source_id": "source_e67cd99ac31c7017d6f7f7c7", "source_record_sha256": "b39cccc4c3c583b07b3ff137341d6e86fd28e8da29878723a54e9a9a5820a7d7", "raw_content_sha256": "e6bf3f8db991625e97cf1ba92dae7bc67c58a0f71f0f6b19e045b754ae9e9eed", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-08-02T12:30:47+08:00"
completed_at: "2026-08-02T12:30:47+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_a858f8d191d3afdd69418471.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_d4762e0cf2330ab6ea00a521 raw_sha256:f8d363f6a631f9a6f28ebfffeb5f9d1cd19b9f8bec643ecf54bcd8744deb0b35", "source:source_e67cd99ac31c7017d6f7f7c7 raw_sha256:e6bf3f8db991625e97cf1ba92dae7bc67c58a0f71f0f6b19e045b754ae9e9eed"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_d4762e0cf2330ab6ea00a521 record_sha256:b286871c8d1940a63a2092ab31eee35237324336a980824860aefd75aa69ce4a", "source:source_e67cd99ac31c7017d6f7f7c7 record_sha256:b39cccc4c3c583b07b3ff137341d6e86fd28e8da29878723a54e9a9a5820a7d7"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_a858f8d191d3afdd69418471"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 5 related objects found", "related:source_d4762e0cf2330ab6ea00a521", "related:concept_2ce226e08d585158c1dfbb18", "related:concept_30d85c442682f6afd96c3022", "related:concept_asymmetric_frozen_vla_harness", "related:concept_a858f8d191d3afdd69418471"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-27T19:03:10+08:00", "source:source_d4762e0cf2330ab6ea00a521 work_sha256:none", "source:source_e67cd99ac31c7017d6f7f7c7 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "a1154b5cd1993d88fdf6f1c6e583014fba1f40774a89984f3131245357cfc6fa", "source_state_sha256": "3a01da5498fc7bddb81c75b368b089f0e869446397f0b20ea59fc6b8eff3d270", "source_record_sha256s": {"source_d4762e0cf2330ab6ea00a521": "b286871c8d1940a63a2092ab31eee35237324336a980824860aefd75aa69ce4a", "source_e67cd99ac31c7017d6f7f7c7": "b39cccc4c3c583b07b3ff137341d6e86fd28e8da29878723a54e9a9a5820a7d7"}, "raw_state_sha256": "73e105c70c01977b75997f9cbfeb4fffb16a868b506e39d12d53286f805284d2", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "fee78f5c9e2577e2967d037484029ad839ea8d8886a770e00f2f75c13e9181e8", "relation_fingerprint": {"outgoing_relations_sha256": "c37957f135ff4d322310a5f9df5f00301a69f965afaf132a6241b06aa438e2b2", "incoming_relations_sha256": "1b08ba681a84bbfe8314ae10ecac4a97819a5079a0b4958878b4a572080ac419", "full_neighborhood_sha256": "f62ecd2cd68ce78eca3ccffe39946b4fa165b37e25172b14fc49f7d57f93c91a"}, "relation_neighborhood_sha256": "f62ecd2cd68ce78eca3ccffe39946b4fa165b37e25172b14fc49f7d57f93c91a", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_a858f8d191d3afdd69418471"
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
        "object_updated_at:2026-07-27T19:03:10+08:00",
        "source:source_d4762e0cf2330ab6ea00a521 work_sha256:none",
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
        "source:source_d4762e0cf2330ab6ea00a521 record_sha256:b286871c8d1940a63a2092ab31eee35237324336a980824860aefd75aa69ce4a",
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
        "source:source_d4762e0cf2330ab6ea00a521 raw_sha256:f8d363f6a631f9a6f28ebfffeb5f9d1cd19b9f8bec643ecf54bcd8744deb0b35",
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
        "relation index inspected; 5 related objects found",
        "related:source_d4762e0cf2330ab6ea00a521",
        "related:concept_2ce226e08d585158c1dfbb18",
        "related:concept_30d85c442682f6afd96c3022",
        "related:concept_asymmetric_frozen_vla_harness",
        "related:concept_a858f8d191d3afdd69418471"
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
        "validated:vault/memory/concept/concept_a858f8d191d3afdd69418471.md"
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
  "completed_at": "2026-08-02T12:30:47+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "a1154b5cd1993d88fdf6f1c6e583014fba1f40774a89984f3131245357cfc6fa",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "73e105c70c01977b75997f9cbfeb4fffb16a868b506e39d12d53286f805284d2",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "f62ecd2cd68ce78eca3ccffe39946b4fa165b37e25172b14fc49f7d57f93c91a",
      "incoming_relations_sha256": "1b08ba681a84bbfe8314ae10ecac4a97819a5079a0b4958878b4a572080ac419",
      "outgoing_relations_sha256": "c37957f135ff4d322310a5f9df5f00301a69f965afaf132a6241b06aa438e2b2"
    },
    "relation_neighborhood_sha256": "f62ecd2cd68ce78eca3ccffe39946b4fa165b37e25172b14fc49f7d57f93c91a",
    "source_record_sha256s": {
      "source_d4762e0cf2330ab6ea00a521": "b286871c8d1940a63a2092ab31eee35237324336a980824860aefd75aa69ce4a",
      "source_e67cd99ac31c7017d6f7f7c7": "b39cccc4c3c583b07b3ff137341d6e86fd28e8da29878723a54e9a9a5820a7d7"
    },
    "source_state_sha256": "3a01da5498fc7bddb81c75b368b089f0e869446397f0b20ea59fc6b8eff3d270",
    "work_identity_sha256": "fee78f5c9e2577e2967d037484029ad839ea8d8886a770e00f2f75c13e9181e8"
  },
  "consolidation_id": "consolidation_b45f391221e09e6d8d3f8fca",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-08-02T12:30:47+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_b45f391221e09e6d8d3f8fca",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_a858f8d191d3afdd69418471",
  "object_sha256_after": "a1154b5cd1993d88fdf6f1c6e583014fba1f40774a89984f3131245357cfc6fa",
  "object_sha256_before": "ce16441921488725434ce8b7e55db7b9d8d6768821b63217582b325b22195f70",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_d4762e0cf2330ab6ea00a521",
    "source_e67cd99ac31c7017d6f7f7c7"
  ],
  "source_records": [
    {
      "raw_content_sha256": "f8d363f6a631f9a6f28ebfffeb5f9d1cd19b9f8bec643ecf54bcd8744deb0b35",
      "source_id": "source_d4762e0cf2330ab6ea00a521",
      "source_record_sha256": "b286871c8d1940a63a2092ab31eee35237324336a980824860aefd75aa69ce4a",
      "work_document_sha256": null,
      "work_id": null
    },
    {
      "raw_content_sha256": "e6bf3f8db991625e97cf1ba92dae7bc67c58a0f71f0f6b19e045b754ae9e9eed",
      "source_id": "source_e67cd99ac31c7017d6f7f7c7",
      "source_record_sha256": "b39cccc4c3c583b07b3ff137341d6e86fd28e8da29878723a54e9a9a5820a7d7",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "f8d363f6a631f9a6f28ebfffeb5f9d1cd19b9f8bec643ecf54bcd8744deb0b35",
    "e6bf3f8db991625e97cf1ba92dae7bc67c58a0f71f0f6b19e045b754ae9e9eed"
  ],
  "started_at": "2026-08-02T12:30:47+08:00",
  "status": "complete",
  "title": "Consolidation: 陈旧性对齐与上下文分区共同约束异步快慢控制接口",
  "type": "consolidation_receipt",
  "updated_at": "2026-08-02T12:30:47+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
