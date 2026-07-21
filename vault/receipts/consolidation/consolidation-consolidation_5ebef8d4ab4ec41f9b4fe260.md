---
id: "consolidation_5ebef8d4ab4ec41f9b4fe260"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 机器人坐标系稠密 Pointmap 观察接口"
created_at: "2026-07-20T13:37:23+08:00"
updated_at: "2026-07-20T13:37:23+08:00"
consolidation_id: "consolidation_5ebef8d4ab4ec41f9b4fe260"
object_id: "concept_21a37fbe65868f6e97a68a20"
object_version_before: 1
object_sha256_before: "c524eccfede3f1e41a5500ee3ef260e472dbb78564c4c5c3f8d3ebb71894da14"
object_sha256_after: "33abaa1412a10b1879a65c7bde56e8452d739b933ed5b75ad4be35bf7b7f32e3"
source_ids: ["source_b64b4a539b8c17d0cfe662ba"]
source_sha256s: ["c3ba696ff1b8a234315f2e706cd4da2c05855a1ec36982ea900319059a95b1d0"]
source_records: [{"source_id": "source_b64b4a539b8c17d0cfe662ba", "source_record_sha256": "0c0b726298a83fe21d5ee1598bfcaaa979e1d900a2f1b5a82b42fb274011b428", "raw_content_sha256": "c3ba696ff1b8a234315f2e706cd4da2c05855a1ec36982ea900319059a95b1d0", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-20T13:37:23+08:00"
completed_at: "2026-07-20T13:37:23+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_21a37fbe65868f6e97a68a20.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_b64b4a539b8c17d0cfe662ba raw_sha256:c3ba696ff1b8a234315f2e706cd4da2c05855a1ec36982ea900319059a95b1d0"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_b64b4a539b8c17d0cfe662ba record_sha256:0c0b726298a83fe21d5ee1598bfcaaa979e1d900a2f1b5a82b42fb274011b428"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_21a37fbe65868f6e97a68a20"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 3 related objects found", "related:source_b64b4a539b8c17d0cfe662ba", "related:concept_90d52ab5e62d9847f9529875", "related:concept_21a37fbe65868f6e97a68a20"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-20T12:33:21+08:00", "source:source_b64b4a539b8c17d0cfe662ba work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "33abaa1412a10b1879a65c7bde56e8452d739b933ed5b75ad4be35bf7b7f32e3", "source_state_sha256": "c672bca5f987278d38e36cec358cdc63b7ddedf301030f4126710d6a7b8d45e8", "source_record_sha256s": {"source_b64b4a539b8c17d0cfe662ba": "0c0b726298a83fe21d5ee1598bfcaaa979e1d900a2f1b5a82b42fb274011b428"}, "raw_state_sha256": "8ece503caa5609fac24061d77b810e9b2b2f855e91055d5f961d953bec83f7ac", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "e30281474d0a21b84b082664e7362094fa910086fa3a8b1dc68ee3b6bdbc2f5d", "relation_fingerprint": {"outgoing_relations_sha256": "f9f5707857e05729826d86d13920f4b001bfb3dc113c76e836646959bf2a6d4c", "incoming_relations_sha256": "dfefd3e06f01a7ab69c70941e9b39cc470cbc281ce5c23339bce643c45e818b1", "full_neighborhood_sha256": "f7aa7a231c5a9dea941f7538b25955bd8b0b5bd8e60e8c2bca8893dbe36ffb03"}, "relation_neighborhood_sha256": "f7aa7a231c5a9dea941f7538b25955bd8b0b5bd8e60e8c2bca8893dbe36ffb03", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_21a37fbe65868f6e97a68a20"
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
        "object_updated_at:2026-07-20T12:33:21+08:00",
        "source:source_b64b4a539b8c17d0cfe662ba work_sha256:none"
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
        "source:source_b64b4a539b8c17d0cfe662ba record_sha256:0c0b726298a83fe21d5ee1598bfcaaa979e1d900a2f1b5a82b42fb274011b428"
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
        "source:source_b64b4a539b8c17d0cfe662ba raw_sha256:c3ba696ff1b8a234315f2e706cd4da2c05855a1ec36982ea900319059a95b1d0"
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
        "related:source_b64b4a539b8c17d0cfe662ba",
        "related:concept_90d52ab5e62d9847f9529875",
        "related:concept_21a37fbe65868f6e97a68a20"
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
        "validated:vault/memory/concept/concept_21a37fbe65868f6e97a68a20.md"
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
  "completed_at": "2026-07-20T13:37:23+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "33abaa1412a10b1879a65c7bde56e8452d739b933ed5b75ad4be35bf7b7f32e3",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "8ece503caa5609fac24061d77b810e9b2b2f855e91055d5f961d953bec83f7ac",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "f7aa7a231c5a9dea941f7538b25955bd8b0b5bd8e60e8c2bca8893dbe36ffb03",
      "incoming_relations_sha256": "dfefd3e06f01a7ab69c70941e9b39cc470cbc281ce5c23339bce643c45e818b1",
      "outgoing_relations_sha256": "f9f5707857e05729826d86d13920f4b001bfb3dc113c76e836646959bf2a6d4c"
    },
    "relation_neighborhood_sha256": "f7aa7a231c5a9dea941f7538b25955bd8b0b5bd8e60e8c2bca8893dbe36ffb03",
    "source_record_sha256s": {
      "source_b64b4a539b8c17d0cfe662ba": "0c0b726298a83fe21d5ee1598bfcaaa979e1d900a2f1b5a82b42fb274011b428"
    },
    "source_state_sha256": "c672bca5f987278d38e36cec358cdc63b7ddedf301030f4126710d6a7b8d45e8",
    "work_identity_sha256": "e30281474d0a21b84b082664e7362094fa910086fa3a8b1dc68ee3b6bdbc2f5d"
  },
  "consolidation_id": "consolidation_5ebef8d4ab4ec41f9b4fe260",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-20T13:37:23+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_5ebef8d4ab4ec41f9b4fe260",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_21a37fbe65868f6e97a68a20",
  "object_sha256_after": "33abaa1412a10b1879a65c7bde56e8452d739b933ed5b75ad4be35bf7b7f32e3",
  "object_sha256_before": "c524eccfede3f1e41a5500ee3ef260e472dbb78564c4c5c3f8d3ebb71894da14",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_b64b4a539b8c17d0cfe662ba"
  ],
  "source_records": [
    {
      "raw_content_sha256": "c3ba696ff1b8a234315f2e706cd4da2c05855a1ec36982ea900319059a95b1d0",
      "source_id": "source_b64b4a539b8c17d0cfe662ba",
      "source_record_sha256": "0c0b726298a83fe21d5ee1598bfcaaa979e1d900a2f1b5a82b42fb274011b428",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "c3ba696ff1b8a234315f2e706cd4da2c05855a1ec36982ea900319059a95b1d0"
  ],
  "started_at": "2026-07-20T13:37:23+08:00",
  "status": "complete",
  "title": "Consolidation: 机器人坐标系稠密 Pointmap 观察接口",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-20T13:37:23+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
