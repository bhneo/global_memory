---
id: "consolidation_fcc10a404f177a90bc379516"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 非特权开放世界移动操作评测边界"
created_at: "2026-07-26T12:33:24+08:00"
updated_at: "2026-07-26T12:33:24+08:00"
consolidation_id: "consolidation_fcc10a404f177a90bc379516"
object_id: "concept_16a7c84a59e39784c801e4ff"
object_version_before: 1
object_sha256_before: "c5d806610cadf5ed7f52781b7b444b3656b10410cdfa1c6f4be6542f2526a080"
object_sha256_after: "7997396519604d03cf0439aa7111ffd6a06d890fbebdc36b2d39c7bbd5798d54"
source_ids: ["source_92fed4343c703da77f798f08"]
source_sha256s: ["9659c5560a55cef7d207f0ab0102391b3ec7e054f5052a9e057e74b5fa9002db"]
source_records: [{"source_id": "source_92fed4343c703da77f798f08", "source_record_sha256": "705ec68e64a57583faefb8ff9c9029842ab1cfa64cc72e3bee79451cde879c1e", "raw_content_sha256": "9659c5560a55cef7d207f0ab0102391b3ec7e054f5052a9e057e74b5fa9002db", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:24+08:00"
completed_at: "2026-07-26T12:33:24+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_16a7c84a59e39784c801e4ff.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_92fed4343c703da77f798f08 raw_sha256:9659c5560a55cef7d207f0ab0102391b3ec7e054f5052a9e057e74b5fa9002db"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_92fed4343c703da77f798f08 record_sha256:705ec68e64a57583faefb8ff9c9029842ab1cfa64cc72e3bee79451cde879c1e"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_16a7c84a59e39784c801e4ff"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_92fed4343c703da77f798f08", "related:concept_dual_protocol_hri_agent_execution_boundary"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-22T18:12:26+08:00", "source:source_92fed4343c703da77f798f08 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "7997396519604d03cf0439aa7111ffd6a06d890fbebdc36b2d39c7bbd5798d54", "source_state_sha256": "bcca1b4869139bfcd7d87c5e58c53be922201f8d442831cdf3ee77436e1648eb", "source_record_sha256s": {"source_92fed4343c703da77f798f08": "705ec68e64a57583faefb8ff9c9029842ab1cfa64cc72e3bee79451cde879c1e"}, "raw_state_sha256": "09f5e6e8b299a150c8f7df586fd59c502ef759038622726603cc4807ee1971ab", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "7d8e61f92a0fd887ff66f5d4459de45a569a62b26b87da05ec71a1364f9ee7a3", "relation_fingerprint": {"outgoing_relations_sha256": "e29ea1fe61c3262ce89d7b5f209457175e94e21a3e5b9a2c5226e536e482df96", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "e29ea1fe61c3262ce89d7b5f209457175e94e21a3e5b9a2c5226e536e482df96"}, "relation_neighborhood_sha256": "e29ea1fe61c3262ce89d7b5f209457175e94e21a3e5b9a2c5226e536e482df96", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_16a7c84a59e39784c801e4ff"
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
        "object_updated_at:2026-07-22T18:12:26+08:00",
        "source:source_92fed4343c703da77f798f08 work_sha256:none"
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
        "source:source_92fed4343c703da77f798f08 record_sha256:705ec68e64a57583faefb8ff9c9029842ab1cfa64cc72e3bee79451cde879c1e"
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
        "source:source_92fed4343c703da77f798f08 raw_sha256:9659c5560a55cef7d207f0ab0102391b3ec7e054f5052a9e057e74b5fa9002db"
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
        "related:source_92fed4343c703da77f798f08",
        "related:concept_dual_protocol_hri_agent_execution_boundary"
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
        "validated:vault/memory/concept/concept_16a7c84a59e39784c801e4ff.md"
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
  "completed_at": "2026-07-26T12:33:24+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "7997396519604d03cf0439aa7111ffd6a06d890fbebdc36b2d39c7bbd5798d54",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "09f5e6e8b299a150c8f7df586fd59c502ef759038622726603cc4807ee1971ab",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "e29ea1fe61c3262ce89d7b5f209457175e94e21a3e5b9a2c5226e536e482df96",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "e29ea1fe61c3262ce89d7b5f209457175e94e21a3e5b9a2c5226e536e482df96"
    },
    "relation_neighborhood_sha256": "e29ea1fe61c3262ce89d7b5f209457175e94e21a3e5b9a2c5226e536e482df96",
    "source_record_sha256s": {
      "source_92fed4343c703da77f798f08": "705ec68e64a57583faefb8ff9c9029842ab1cfa64cc72e3bee79451cde879c1e"
    },
    "source_state_sha256": "bcca1b4869139bfcd7d87c5e58c53be922201f8d442831cdf3ee77436e1648eb",
    "work_identity_sha256": "7d8e61f92a0fd887ff66f5d4459de45a569a62b26b87da05ec71a1364f9ee7a3"
  },
  "consolidation_id": "consolidation_fcc10a404f177a90bc379516",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:24+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_fcc10a404f177a90bc379516",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_16a7c84a59e39784c801e4ff",
  "object_sha256_after": "7997396519604d03cf0439aa7111ffd6a06d890fbebdc36b2d39c7bbd5798d54",
  "object_sha256_before": "c5d806610cadf5ed7f52781b7b444b3656b10410cdfa1c6f4be6542f2526a080",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_92fed4343c703da77f798f08"
  ],
  "source_records": [
    {
      "raw_content_sha256": "9659c5560a55cef7d207f0ab0102391b3ec7e054f5052a9e057e74b5fa9002db",
      "source_id": "source_92fed4343c703da77f798f08",
      "source_record_sha256": "705ec68e64a57583faefb8ff9c9029842ab1cfa64cc72e3bee79451cde879c1e",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "9659c5560a55cef7d207f0ab0102391b3ec7e054f5052a9e057e74b5fa9002db"
  ],
  "started_at": "2026-07-26T12:33:24+08:00",
  "status": "complete",
  "title": "Consolidation: 非特权开放世界移动操作评测边界",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:24+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
