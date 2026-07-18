---
id: "consolidation_f639fa16dcaa13ee0ff85009"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: humans are able to overcome t"
created_at: "2026-07-18T16:02:43+08:00"
updated_at: "2026-07-18T16:02:43+08:00"
consolidation_id: "consolidation_f639fa16dcaa13ee0ff85009"
object_id: "claim_92804ba3893e52d0c5696e45"
object_version_before: 1
object_sha256_before: "4c219ed64e934661b858ba2309b48c8d4b07bb9225d865326378f976479b2790"
object_sha256_after: "b03da21c861a3f61a141527aa10a268812acf82475eec6e11ce9faec7213604e"
source_ids: ["source_62389152cf0723e2f3a753c1"]
source_sha256s: ["f12c9547bb3f451ba4585e51e8683948e8b9b703610d5adf6ba99e38f4ff3344"]
source_records: [{"source_id": "source_62389152cf0723e2f3a753c1", "source_record_sha256": "655f55c1bb14f2e2e7e82799dbd12e1cdeebe83d1a1bbbad14ffb49ed5b6f8b6", "raw_content_sha256": "f12c9547bb3f451ba4585e51e8683948e8b9b703610d5adf6ba99e38f4ff3344", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["evidence_0a60001a90a32cfb3283"]
started_at: "2026-07-18T16:02:43+08:00"
completed_at: "2026-07-18T16:02:43+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/claim/claim_92804ba3893e52d0c5696e45.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_62389152cf0723e2f3a753c1 raw_sha256:f12c9547bb3f451ba4585e51e8683948e8b9b703610d5adf6ba99e38f4ff3344"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_62389152cf0723e2f3a753c1 record_sha256:655f55c1bb14f2e2e7e82799dbd12e1cdeebe83d1a1bbbad14ffb49ed5b6f8b6"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["evidence:evidence_0a60001a90a32cfb3283"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "passed", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": "none", "findings": ["evidence_entailment:none"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 2 candidates inspected", "candidate:claim_92804ba3893e52d0c5696e45", "candidate:source_08e53bb30d37610610477e01"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 1 related objects found", "related:source_62389152cf0723e2f3a753c1"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-17T18:35:24+08:00", "source:source_62389152cf0723e2f3a753c1 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "b03da21c861a3f61a141527aa10a268812acf82475eec6e11ce9faec7213604e", "source_state_sha256": "29fc4c8a9304b61f6d591d339b581fdd19eaca6115d1391eecb48302a179e52e", "source_record_sha256s": {"source_62389152cf0723e2f3a753c1": "655f55c1bb14f2e2e7e82799dbd12e1cdeebe83d1a1bbbad14ffb49ed5b6f8b6"}, "raw_state_sha256": "01a4761ae95e21fb037e478874a6e93131c6ccd0fe09690c13f688676b8b62ad", "evidence_sha256": "af5c369619873af6cedd9dc7b163e9567df4e89acf47270ce879b2195c0e8df7", "extraction_state_sha256": "99683b2d53e8b76a07461b81c2d180f5e9572e6ddc2c0338ddadae9f8906436b", "work_identity_sha256": "f38e07a79426c39e52f4c5ccede4859e271314e666849f01d85701212662c996", "relation_fingerprint": {"outgoing_relations_sha256": "54e5ea86f00f345b70e91c46377361e454b20446ec4e21ac61eb679f8fa7827e", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "54e5ea86f00f345b70e91c46377361e454b20446ec4e21ac61eb679f8fa7827e"}, "relation_neighborhood_sha256": "54e5ea86f00f345b70e91c46377361e454b20446ec4e21ac61eb679f8fa7827e", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "searched title; 2 candidates inspected",
        "candidate:claim_92804ba3893e52d0c5696e45",
        "candidate:source_08e53bb30d37610610477e01"
      ],
      "method": "deterministic repository check",
      "semantic_recheck_performed": null,
      "validation_outcome": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "check_name": "evidence_entailment_rechecked",
      "declared_value": "none",
      "execution_status": "completed",
      "findings": [
        "evidence_entailment:none"
      ],
      "method": "declared-metadata-inspection",
      "semantic_recheck_performed": true,
      "validation_outcome": "passed",
      "warnings": []
    },
    "evidence_revalidated": {
      "check_name": "evidence_revalidated",
      "declared_value": null,
      "execution_status": "completed",
      "findings": [
        "evidence:evidence_0a60001a90a32cfb3283"
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
        "object_updated_at:2026-07-17T18:35:24+08:00",
        "source:source_62389152cf0723e2f3a753c1 work_sha256:none"
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
        "source:source_62389152cf0723e2f3a753c1 record_sha256:655f55c1bb14f2e2e7e82799dbd12e1cdeebe83d1a1bbbad14ffb49ed5b6f8b6"
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
        "source:source_62389152cf0723e2f3a753c1 raw_sha256:f12c9547bb3f451ba4585e51e8683948e8b9b703610d5adf6ba99e38f4ff3344"
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
        "related:source_62389152cf0723e2f3a753c1"
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
        "validated:vault/memory/claim/claim_92804ba3893e52d0c5696e45.md"
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
  "completed_at": "2026-07-18T16:02:43+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "af5c369619873af6cedd9dc7b163e9567df4e89acf47270ce879b2195c0e8df7",
    "extraction_state_sha256": "99683b2d53e8b76a07461b81c2d180f5e9572e6ddc2c0338ddadae9f8906436b",
    "memory_schema_version": 2,
    "object_sha256": "b03da21c861a3f61a141527aa10a268812acf82475eec6e11ce9faec7213604e",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "01a4761ae95e21fb037e478874a6e93131c6ccd0fe09690c13f688676b8b62ad",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "54e5ea86f00f345b70e91c46377361e454b20446ec4e21ac61eb679f8fa7827e",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "54e5ea86f00f345b70e91c46377361e454b20446ec4e21ac61eb679f8fa7827e"
    },
    "relation_neighborhood_sha256": "54e5ea86f00f345b70e91c46377361e454b20446ec4e21ac61eb679f8fa7827e",
    "source_record_sha256s": {
      "source_62389152cf0723e2f3a753c1": "655f55c1bb14f2e2e7e82799dbd12e1cdeebe83d1a1bbbad14ffb49ed5b6f8b6"
    },
    "source_state_sha256": "29fc4c8a9304b61f6d591d339b581fdd19eaca6115d1391eecb48302a179e52e",
    "work_identity_sha256": "f38e07a79426c39e52f4c5ccede4859e271314e666849f01d85701212662c996"
  },
  "consolidation_id": "consolidation_f639fa16dcaa13ee0ff85009",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-18T16:02:43+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "evidence_0a60001a90a32cfb3283"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_f639fa16dcaa13ee0ff85009",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_92804ba3893e52d0c5696e45",
  "object_sha256_after": "b03da21c861a3f61a141527aa10a268812acf82475eec6e11ce9faec7213604e",
  "object_sha256_before": "4c219ed64e934661b858ba2309b48c8d4b07bb9225d865326378f976479b2790",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_62389152cf0723e2f3a753c1"
  ],
  "source_records": [
    {
      "raw_content_sha256": "f12c9547bb3f451ba4585e51e8683948e8b9b703610d5adf6ba99e38f4ff3344",
      "source_id": "source_62389152cf0723e2f3a753c1",
      "source_record_sha256": "655f55c1bb14f2e2e7e82799dbd12e1cdeebe83d1a1bbbad14ffb49ed5b6f8b6",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "f12c9547bb3f451ba4585e51e8683948e8b9b703610d5adf6ba99e38f4ff3344"
  ],
  "started_at": "2026-07-18T16:02:43+08:00",
  "status": "complete",
  "title": "Consolidation: humans are able to overcome t",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-18T16:02:43+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
