---
id: "consolidation_7fc88ee7c1c53df74942abc9"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 以休眠锚点和意图激活驱动的即时场景图生长"
created_at: "2026-07-26T12:33:48+08:00"
updated_at: "2026-07-26T12:33:48+08:00"
consolidation_id: "consolidation_7fc88ee7c1c53df74942abc9"
object_id: "concept_ebafde4b9db7a2ebd19c6bc6"
object_version_before: 1
object_sha256_before: "2b6fceb0d272c94e9206d13cc0f4839430b264e243e92bd1086074353675e487"
object_sha256_after: "508550bf5d4084d8920e7c2a07933cd5ad400a1385ba1615b8c55163a36042df"
source_ids: ["source_e8650c5afb7548268f649fb8"]
source_sha256s: ["c81e68f77bed6d4fdbe6f2f939a37e1e5b174d1b86ec25d7c49714f520321f2e"]
source_records: [{"source_id": "source_e8650c5afb7548268f649fb8", "source_record_sha256": "05598c2f5d06115ef98a1957e76a52346a6d77b3520ec81303f3e0ce20a32312", "raw_content_sha256": "c81e68f77bed6d4fdbe6f2f939a37e1e5b174d1b86ec25d7c49714f520321f2e", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:48+08:00"
completed_at: "2026-07-26T12:33:48+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_ebafde4b9db7a2ebd19c6bc6.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_e8650c5afb7548268f649fb8 raw_sha256:c81e68f77bed6d4fdbe6f2f939a37e1e5b174d1b86ec25d7c49714f520321f2e"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_e8650c5afb7548268f649fb8 record_sha256:05598c2f5d06115ef98a1957e76a52346a6d77b3520ec81303f3e0ce20a32312"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_ebafde4b9db7a2ebd19c6bc6"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_e8650c5afb7548268f649fb8", "related:concept_typed_verified_robot_skill_graph"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-25T18:08:59+08:00", "source:source_e8650c5afb7548268f649fb8 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "508550bf5d4084d8920e7c2a07933cd5ad400a1385ba1615b8c55163a36042df", "source_state_sha256": "559d42f641bc2ae1a00c37bd4e03d3d736ddc9d58082a1e9e8ed959eb58b2d14", "source_record_sha256s": {"source_e8650c5afb7548268f649fb8": "05598c2f5d06115ef98a1957e76a52346a6d77b3520ec81303f3e0ce20a32312"}, "raw_state_sha256": "d2a2349c70342183c487e101f257c656c6c4286fe0fd8c51ca5b3c45830de294", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "7e5cef8c0370cb3a582d3f36c92ec2b0eb964811cf2d982dcdfd72e68129cba4", "relation_fingerprint": {"outgoing_relations_sha256": "1dbb470d66d4040ff42b95e278e75a221573de3949b76d6c5cc2000f73722039", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "1dbb470d66d4040ff42b95e278e75a221573de3949b76d6c5cc2000f73722039"}, "relation_neighborhood_sha256": "1dbb470d66d4040ff42b95e278e75a221573de3949b76d6c5cc2000f73722039", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_ebafde4b9db7a2ebd19c6bc6"
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
        "object_updated_at:2026-07-25T18:08:59+08:00",
        "source:source_e8650c5afb7548268f649fb8 work_sha256:none"
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
        "source:source_e8650c5afb7548268f649fb8 record_sha256:05598c2f5d06115ef98a1957e76a52346a6d77b3520ec81303f3e0ce20a32312"
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
        "source:source_e8650c5afb7548268f649fb8 raw_sha256:c81e68f77bed6d4fdbe6f2f939a37e1e5b174d1b86ec25d7c49714f520321f2e"
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
        "related:source_e8650c5afb7548268f649fb8",
        "related:concept_typed_verified_robot_skill_graph"
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
        "validated:vault/memory/concept/concept_ebafde4b9db7a2ebd19c6bc6.md"
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
  "completed_at": "2026-07-26T12:33:48+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "508550bf5d4084d8920e7c2a07933cd5ad400a1385ba1615b8c55163a36042df",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "d2a2349c70342183c487e101f257c656c6c4286fe0fd8c51ca5b3c45830de294",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "1dbb470d66d4040ff42b95e278e75a221573de3949b76d6c5cc2000f73722039",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "1dbb470d66d4040ff42b95e278e75a221573de3949b76d6c5cc2000f73722039"
    },
    "relation_neighborhood_sha256": "1dbb470d66d4040ff42b95e278e75a221573de3949b76d6c5cc2000f73722039",
    "source_record_sha256s": {
      "source_e8650c5afb7548268f649fb8": "05598c2f5d06115ef98a1957e76a52346a6d77b3520ec81303f3e0ce20a32312"
    },
    "source_state_sha256": "559d42f641bc2ae1a00c37bd4e03d3d736ddc9d58082a1e9e8ed959eb58b2d14",
    "work_identity_sha256": "7e5cef8c0370cb3a582d3f36c92ec2b0eb964811cf2d982dcdfd72e68129cba4"
  },
  "consolidation_id": "consolidation_7fc88ee7c1c53df74942abc9",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:48+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_7fc88ee7c1c53df74942abc9",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_ebafde4b9db7a2ebd19c6bc6",
  "object_sha256_after": "508550bf5d4084d8920e7c2a07933cd5ad400a1385ba1615b8c55163a36042df",
  "object_sha256_before": "2b6fceb0d272c94e9206d13cc0f4839430b264e243e92bd1086074353675e487",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_e8650c5afb7548268f649fb8"
  ],
  "source_records": [
    {
      "raw_content_sha256": "c81e68f77bed6d4fdbe6f2f939a37e1e5b174d1b86ec25d7c49714f520321f2e",
      "source_id": "source_e8650c5afb7548268f649fb8",
      "source_record_sha256": "05598c2f5d06115ef98a1957e76a52346a6d77b3520ec81303f3e0ce20a32312",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "c81e68f77bed6d4fdbe6f2f939a37e1e5b174d1b86ec25d7c49714f520321f2e"
  ],
  "started_at": "2026-07-26T12:33:48+08:00",
  "status": "complete",
  "title": "Consolidation: 以休眠锚点和意图激活驱动的即时场景图生长",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:48+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
