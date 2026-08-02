---
id: "consolidation_6151d12685c168397f74e368"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 冻结 flow 先验的分阶段潜空间奖励转向 / Staged latent-space reward steering over a frozen flow prior"
created_at: "2026-08-02T19:55:01+08:00"
updated_at: "2026-08-02T19:55:01+08:00"
consolidation_id: "consolidation_6151d12685c168397f74e368"
object_id: "concept_6a559a41722de87986c350e7"
object_version_before: 1
object_sha256_before: "9785ca074fbcef45f3a927d161a7cedac15ebaa943c538e4f94299db24614b8f"
object_sha256_after: "d32b741e35f68ba04906df9a9a5d30278fda25fd45e9051f3ec265c5e0ad7c33"
source_ids: ["source_98bb68f21232969a79d77918"]
source_sha256s: ["f36392fd9a8ff9e3287bacd91418cb6eb6f873ac961f8431c4982bd5ffb1c43e"]
source_records: [{"source_id": "source_98bb68f21232969a79d77918", "source_record_sha256": "eea586aed80abe443af2d9616d92cca8f0888ffe551253edee91aa8d4a1713ea", "raw_content_sha256": "f36392fd9a8ff9e3287bacd91418cb6eb6f873ac961f8431c4982bd5ffb1c43e", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-08-02T19:55:00+08:00"
completed_at: "2026-08-02T19:55:01+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_6a559a41722de87986c350e7.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_98bb68f21232969a79d77918 raw_sha256:f36392fd9a8ff9e3287bacd91418cb6eb6f873ac961f8431c4982bd5ffb1c43e"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_98bb68f21232969a79d77918 record_sha256:eea586aed80abe443af2d9616d92cca8f0888ffe551253edee91aa8d4a1713ea"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_6a559a41722de87986c350e7"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 6 related objects found", "related:source_98bb68f21232969a79d77918", "related:concept_f9a9f1d1818632c0380b7942", "related:concept_latent_space_intervention_adaptation", "related:concept_6a559a41722de87986c350e7", "related:concept_6a559a41722de87986c350e7"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-08-02T12:30:39+08:00", "source:source_98bb68f21232969a79d77918 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "d32b741e35f68ba04906df9a9a5d30278fda25fd45e9051f3ec265c5e0ad7c33", "source_state_sha256": "1f728f1917e0e9dc36c0df74f9e1747d57c544d5dbd9d54540400d3ef07b93bc", "source_record_sha256s": {"source_98bb68f21232969a79d77918": "eea586aed80abe443af2d9616d92cca8f0888ffe551253edee91aa8d4a1713ea"}, "raw_state_sha256": "f12e4ef20a327584542fefb63e4b9be16e4667d437e3bcfced1e736a8e5ba57b", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "30586ace133b79df104566aa310ddbb1c58d07a6ddad2250ae41499856adfbdd", "relation_fingerprint": {"outgoing_relations_sha256": "37d636f2ab96582b62ce061d37c56289f22ccfa0bb2f1cd3ead047b56a41c149", "incoming_relations_sha256": "c76e8badd436b600f790d6eb08defb372e7c9026854bb88a7dc537fc792e82dd", "full_neighborhood_sha256": "593a91a00a52f825b3f74730963c04aa4538248571ce9e72d941afc564049a93"}, "relation_neighborhood_sha256": "593a91a00a52f825b3f74730963c04aa4538248571ce9e72d941afc564049a93", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:concept_6a559a41722de87986c350e7"
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
        "object_updated_at:2026-08-02T12:30:39+08:00",
        "source:source_98bb68f21232969a79d77918 work_sha256:none"
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
        "source:source_98bb68f21232969a79d77918 record_sha256:eea586aed80abe443af2d9616d92cca8f0888ffe551253edee91aa8d4a1713ea"
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
        "source:source_98bb68f21232969a79d77918 raw_sha256:f36392fd9a8ff9e3287bacd91418cb6eb6f873ac961f8431c4982bd5ffb1c43e"
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
        "relation index inspected; 6 related objects found",
        "related:source_98bb68f21232969a79d77918",
        "related:concept_f9a9f1d1818632c0380b7942",
        "related:concept_latent_space_intervention_adaptation",
        "related:concept_6a559a41722de87986c350e7",
        "related:concept_6a559a41722de87986c350e7"
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
        "validated:vault/memory/concept/concept_6a559a41722de87986c350e7.md"
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
  "completed_at": "2026-08-02T19:55:01+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "d32b741e35f68ba04906df9a9a5d30278fda25fd45e9051f3ec265c5e0ad7c33",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "f12e4ef20a327584542fefb63e4b9be16e4667d437e3bcfced1e736a8e5ba57b",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "593a91a00a52f825b3f74730963c04aa4538248571ce9e72d941afc564049a93",
      "incoming_relations_sha256": "c76e8badd436b600f790d6eb08defb372e7c9026854bb88a7dc537fc792e82dd",
      "outgoing_relations_sha256": "37d636f2ab96582b62ce061d37c56289f22ccfa0bb2f1cd3ead047b56a41c149"
    },
    "relation_neighborhood_sha256": "593a91a00a52f825b3f74730963c04aa4538248571ce9e72d941afc564049a93",
    "source_record_sha256s": {
      "source_98bb68f21232969a79d77918": "eea586aed80abe443af2d9616d92cca8f0888ffe551253edee91aa8d4a1713ea"
    },
    "source_state_sha256": "1f728f1917e0e9dc36c0df74f9e1747d57c544d5dbd9d54540400d3ef07b93bc",
    "work_identity_sha256": "30586ace133b79df104566aa310ddbb1c58d07a6ddad2250ae41499856adfbdd"
  },
  "consolidation_id": "consolidation_6151d12685c168397f74e368",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-08-02T19:55:01+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_6151d12685c168397f74e368",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_6a559a41722de87986c350e7",
  "object_sha256_after": "d32b741e35f68ba04906df9a9a5d30278fda25fd45e9051f3ec265c5e0ad7c33",
  "object_sha256_before": "9785ca074fbcef45f3a927d161a7cedac15ebaa943c538e4f94299db24614b8f",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_98bb68f21232969a79d77918"
  ],
  "source_records": [
    {
      "raw_content_sha256": "f36392fd9a8ff9e3287bacd91418cb6eb6f873ac961f8431c4982bd5ffb1c43e",
      "source_id": "source_98bb68f21232969a79d77918",
      "source_record_sha256": "eea586aed80abe443af2d9616d92cca8f0888ffe551253edee91aa8d4a1713ea",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "f36392fd9a8ff9e3287bacd91418cb6eb6f873ac961f8431c4982bd5ffb1c43e"
  ],
  "started_at": "2026-08-02T19:55:00+08:00",
  "status": "complete",
  "title": "Consolidation: 冻结 flow 先验的分阶段潜空间奖励转向 / Staged latent-space reward steering over a frozen flow prior",
  "type": "consolidation_receipt",
  "updated_at": "2026-08-02T19:55:01+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
