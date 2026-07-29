---
id: "consolidation_0820dbe4cf261833acc821de"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 以语言选择三维抓取种子的多本体抓取分解"
created_at: "2026-07-26T12:33:36+08:00"
updated_at: "2026-07-26T12:33:36+08:00"
consolidation_id: "consolidation_0820dbe4cf261833acc821de"
object_id: "concept_67c66e870e29ca11e24eaa5f"
object_version_before: 1
object_sha256_before: "9989cd2612d862454913d40a29aa0fbc1d858ba7b9ff91e8ab070c538fb68deb"
object_sha256_after: "32579de60400696218072006cbfdca3c0b5c87507488009744fcff222e04f7df"
source_ids: ["source_7efe67e4901341dddfe120ff"]
source_sha256s: ["bd0cf9a3372abd1bee59061933e83a301531aefb9bcd5c60ed99ca3108b40b90"]
source_records: [{"source_id": "source_7efe67e4901341dddfe120ff", "source_record_sha256": "3a06c93a9068a65b8e0ae2b1850effe1b6af4e830263ea8624726024e3488dc8", "raw_content_sha256": "bd0cf9a3372abd1bee59061933e83a301531aefb9bcd5c60ed99ca3108b40b90", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-26T12:33:35+08:00"
completed_at: "2026-07-26T12:33:36+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_67c66e870e29ca11e24eaa5f.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_7efe67e4901341dddfe120ff raw_sha256:bd0cf9a3372abd1bee59061933e83a301531aefb9bcd5c60ed99ca3108b40b90"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_7efe67e4901341dddfe120ff record_sha256:3a06c93a9068a65b8e0ae2b1850effe1b6af4e830263ea8624726024e3488dc8"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_67c66e870e29ca11e24eaa5f"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_7efe67e4901341dddfe120ff", "related:concept_generalist_cross_embodiment_vla"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-24T18:05:50+08:00", "source:source_7efe67e4901341dddfe120ff work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "32579de60400696218072006cbfdca3c0b5c87507488009744fcff222e04f7df", "source_state_sha256": "bfbc30f25e0b3c90025896506f0492492bff378acf33241219115b1b25f884fc", "source_record_sha256s": {"source_7efe67e4901341dddfe120ff": "3a06c93a9068a65b8e0ae2b1850effe1b6af4e830263ea8624726024e3488dc8"}, "raw_state_sha256": "339545c71060932e852932f535be054e209fbd4ecb6eeba9a084b689e99456c6", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "47d7c19e3424b40c293b1eeb4a41e49353cc895df93a8428e2398f5c838cfbe8", "relation_fingerprint": {"outgoing_relations_sha256": "3fc7a336625fbd3281591c1d36cdff2b08dc7b28960eded8943cd4ca90ad32ab", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "3fc7a336625fbd3281591c1d36cdff2b08dc7b28960eded8943cd4ca90ad32ab"}, "relation_neighborhood_sha256": "3fc7a336625fbd3281591c1d36cdff2b08dc7b28960eded8943cd4ca90ad32ab", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_67c66e870e29ca11e24eaa5f"
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
        "object_updated_at:2026-07-24T18:05:50+08:00",
        "source:source_7efe67e4901341dddfe120ff work_sha256:none"
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
        "source:source_7efe67e4901341dddfe120ff record_sha256:3a06c93a9068a65b8e0ae2b1850effe1b6af4e830263ea8624726024e3488dc8"
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
        "source:source_7efe67e4901341dddfe120ff raw_sha256:bd0cf9a3372abd1bee59061933e83a301531aefb9bcd5c60ed99ca3108b40b90"
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
        "related:source_7efe67e4901341dddfe120ff",
        "related:concept_generalist_cross_embodiment_vla"
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
        "validated:vault/memory/concept/concept_67c66e870e29ca11e24eaa5f.md"
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
  "completed_at": "2026-07-26T12:33:36+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "32579de60400696218072006cbfdca3c0b5c87507488009744fcff222e04f7df",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "339545c71060932e852932f535be054e209fbd4ecb6eeba9a084b689e99456c6",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "3fc7a336625fbd3281591c1d36cdff2b08dc7b28960eded8943cd4ca90ad32ab",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "3fc7a336625fbd3281591c1d36cdff2b08dc7b28960eded8943cd4ca90ad32ab"
    },
    "relation_neighborhood_sha256": "3fc7a336625fbd3281591c1d36cdff2b08dc7b28960eded8943cd4ca90ad32ab",
    "source_record_sha256s": {
      "source_7efe67e4901341dddfe120ff": "3a06c93a9068a65b8e0ae2b1850effe1b6af4e830263ea8624726024e3488dc8"
    },
    "source_state_sha256": "bfbc30f25e0b3c90025896506f0492492bff378acf33241219115b1b25f884fc",
    "work_identity_sha256": "47d7c19e3424b40c293b1eeb4a41e49353cc895df93a8428e2398f5c838cfbe8"
  },
  "consolidation_id": "consolidation_0820dbe4cf261833acc821de",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-26T12:33:36+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_0820dbe4cf261833acc821de",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_67c66e870e29ca11e24eaa5f",
  "object_sha256_after": "32579de60400696218072006cbfdca3c0b5c87507488009744fcff222e04f7df",
  "object_sha256_before": "9989cd2612d862454913d40a29aa0fbc1d858ba7b9ff91e8ab070c538fb68deb",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_7efe67e4901341dddfe120ff"
  ],
  "source_records": [
    {
      "raw_content_sha256": "bd0cf9a3372abd1bee59061933e83a301531aefb9bcd5c60ed99ca3108b40b90",
      "source_id": "source_7efe67e4901341dddfe120ff",
      "source_record_sha256": "3a06c93a9068a65b8e0ae2b1850effe1b6af4e830263ea8624726024e3488dc8",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "bd0cf9a3372abd1bee59061933e83a301531aefb9bcd5c60ed99ca3108b40b90"
  ],
  "started_at": "2026-07-26T12:33:35+08:00",
  "status": "complete",
  "title": "Consolidation: 以语言选择三维抓取种子的多本体抓取分解",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-26T12:33:36+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
