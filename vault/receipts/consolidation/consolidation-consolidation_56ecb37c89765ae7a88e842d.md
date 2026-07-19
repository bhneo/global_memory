---
id: "consolidation_56ecb37c89765ae7a88e842d"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 该研究的 pass@k 诊断显示冻结 VLA 输出中存在大量可行候选"
created_at: "2026-07-19T03:05:44+08:00"
updated_at: "2026-07-19T03:05:44+08:00"
consolidation_id: "consolidation_56ecb37c89765ae7a88e842d"
object_id: "claim_ed202cdc4c79d46f2ac31913"
object_version_before: 1
object_sha256_before: "4895b5d8a5012364f4b62283ad9702ac4e3549a7418fd92b82386fe390d3ad27"
object_sha256_after: "983e3cdb9bb64bc886fd6ed93d4dbc2f8f9e0b478ba36e476589d811b3e46689"
source_ids: ["source_ff90ad99bd47043e812cce9e"]
source_sha256s: ["fc1f2b9d77c84df800f82c811028d99bc188ae8992dc1769ebcc8dcbd98f266c"]
source_records: [{"source_id": "source_ff90ad99bd47043e812cce9e", "source_record_sha256": "78f72094fe8a9e31b0e62c638742a9c7f7dcc6f42a385d5213b9b694100df179", "raw_content_sha256": "fc1f2b9d77c84df800f82c811028d99bc188ae8992dc1769ebcc8dcbd98f266c", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["evidence_a0ed7c22bb0d15f4c2cb"]
started_at: "2026-07-19T03:05:44+08:00"
completed_at: "2026-07-19T03:05:44+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/claim/claim_ed202cdc4c79d46f2ac31913.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_ff90ad99bd47043e812cce9e raw_sha256:fc1f2b9d77c84df800f82c811028d99bc188ae8992dc1769ebcc8dcbd98f266c"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_ff90ad99bd47043e812cce9e record_sha256:78f72094fe8a9e31b0e62c638742a9c7f7dcc6f42a385d5213b9b694100df179"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["evidence:evidence_a0ed7c22bb0d15f4c2cb"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "needs_review", "method": "declared-metadata-inspection", "semantic_recheck_performed": false, "declared_value": "full", "findings": ["evidence_entailment:full"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:claim_ed202cdc4c79d46f2ac31913"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_ff90ad99bd47043e812cce9e", "related:concept_vla_action_evaluation_distillation"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-19T03:03:51+08:00", "source:source_ff90ad99bd47043e812cce9e work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "983e3cdb9bb64bc886fd6ed93d4dbc2f8f9e0b478ba36e476589d811b3e46689", "source_state_sha256": "577f07324e84cf6b4c0cd9d1623475b72c1f846afa5897babd4ef79d97924c34", "source_record_sha256s": {"source_ff90ad99bd47043e812cce9e": "78f72094fe8a9e31b0e62c638742a9c7f7dcc6f42a385d5213b9b694100df179"}, "raw_state_sha256": "f5832511036616a15899099e35f2ca5cca9e2f08388abe32f3d8b7b922f2d258", "evidence_sha256": "699ff2895ed5d29e21f6d311a5cd1de2289365d358ff7c96556834bb249ceded", "extraction_state_sha256": "25b64850a7daca60e554ee6c6dafc4c7b327ca1a63dd829dd09becc80d9bbc2a", "work_identity_sha256": "1829624627831aa5e3498b23a90b8c72aaa43e21000bf59a039270de80766c80", "relation_fingerprint": {"outgoing_relations_sha256": "6dba04a736d5e216e6cefaf62d852758156f5cb135f52a4364f9050cdb2b1479", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "6dba04a736d5e216e6cefaf62d852758156f5cb135f52a4364f9050cdb2b1479"}, "relation_neighborhood_sha256": "6dba04a736d5e216e6cefaf62d852758156f5cb135f52a4364f9050cdb2b1479", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:claim_ed202cdc4c79d46f2ac31913"
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
        "evidence:evidence_a0ed7c22bb0d15f4c2cb"
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
        "object_updated_at:2026-07-19T03:03:51+08:00",
        "source:source_ff90ad99bd47043e812cce9e work_sha256:none"
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
        "source:source_ff90ad99bd47043e812cce9e record_sha256:78f72094fe8a9e31b0e62c638742a9c7f7dcc6f42a385d5213b9b694100df179"
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
        "source:source_ff90ad99bd47043e812cce9e raw_sha256:fc1f2b9d77c84df800f82c811028d99bc188ae8992dc1769ebcc8dcbd98f266c"
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
        "related:source_ff90ad99bd47043e812cce9e",
        "related:concept_vla_action_evaluation_distillation"
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
        "validated:vault/memory/claim/claim_ed202cdc4c79d46f2ac31913.md"
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
  "completed_at": "2026-07-19T03:05:44+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "699ff2895ed5d29e21f6d311a5cd1de2289365d358ff7c96556834bb249ceded",
    "extraction_state_sha256": "25b64850a7daca60e554ee6c6dafc4c7b327ca1a63dd829dd09becc80d9bbc2a",
    "memory_schema_version": 2,
    "object_sha256": "983e3cdb9bb64bc886fd6ed93d4dbc2f8f9e0b478ba36e476589d811b3e46689",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "f5832511036616a15899099e35f2ca5cca9e2f08388abe32f3d8b7b922f2d258",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "6dba04a736d5e216e6cefaf62d852758156f5cb135f52a4364f9050cdb2b1479",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "6dba04a736d5e216e6cefaf62d852758156f5cb135f52a4364f9050cdb2b1479"
    },
    "relation_neighborhood_sha256": "6dba04a736d5e216e6cefaf62d852758156f5cb135f52a4364f9050cdb2b1479",
    "source_record_sha256s": {
      "source_ff90ad99bd47043e812cce9e": "78f72094fe8a9e31b0e62c638742a9c7f7dcc6f42a385d5213b9b694100df179"
    },
    "source_state_sha256": "577f07324e84cf6b4c0cd9d1623475b72c1f846afa5897babd4ef79d97924c34",
    "work_identity_sha256": "1829624627831aa5e3498b23a90b8c72aaa43e21000bf59a039270de80766c80"
  },
  "consolidation_id": "consolidation_56ecb37c89765ae7a88e842d",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-19T03:05:44+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "evidence_a0ed7c22bb0d15f4c2cb"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_56ecb37c89765ae7a88e842d",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_ed202cdc4c79d46f2ac31913",
  "object_sha256_after": "983e3cdb9bb64bc886fd6ed93d4dbc2f8f9e0b478ba36e476589d811b3e46689",
  "object_sha256_before": "4895b5d8a5012364f4b62283ad9702ac4e3549a7418fd92b82386fe390d3ad27",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_ff90ad99bd47043e812cce9e"
  ],
  "source_records": [
    {
      "raw_content_sha256": "fc1f2b9d77c84df800f82c811028d99bc188ae8992dc1769ebcc8dcbd98f266c",
      "source_id": "source_ff90ad99bd47043e812cce9e",
      "source_record_sha256": "78f72094fe8a9e31b0e62c638742a9c7f7dcc6f42a385d5213b9b694100df179",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "fc1f2b9d77c84df800f82c811028d99bc188ae8992dc1769ebcc8dcbd98f266c"
  ],
  "started_at": "2026-07-19T03:05:44+08:00",
  "status": "complete",
  "title": "Consolidation: 该研究的 pass@k 诊断显示冻结 VLA 输出中存在大量可行候选",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-19T03:05:44+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
