---
id: "consolidation_7e20534ba2b68bcc67fd66b2"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: Evolving Intrinsic Motivations for Altruistic Behavior Jane X. Wang, Edward Hughes, Chrisantha Fernando, Wojciech M. Czarnecki, Edgar A. Duéñez-Guzmán, & Joel Z"
created_at: "2026-07-17T18:35:33+08:00"
updated_at: "2026-07-17T18:35:33+08:00"
consolidation_id: "consolidation_7e20534ba2b68bcc67fd66b2"
object_id: "claim_ea6b984ae4bdd1dfdf5288a1"
object_version_before: 1
object_sha256_before: "94cbdaf41a5a74f3e65529d4fc9ade13640fd6db14ce117db0fdeec81c5b6fac"
object_sha256_after: "ac5cdf1893be94bf9c615270002d92b5959e6d6edbd58cbf7843d730bd4ea036"
source_ids: ["source_62389152cf0723e2f3a753c1"]
source_sha256s: ["f12c9547bb3f451ba4585e51e8683948e8b9b703610d5adf6ba99e38f4ff3344"]
source_records: [{"source_id": "source_62389152cf0723e2f3a753c1", "source_record_sha256": "655f55c1bb14f2e2e7e82799dbd12e1cdeebe83d1a1bbbad14ffb49ed5b6f8b6", "raw_content_sha256": "f12c9547bb3f451ba4585e51e8683948e8b9b703610d5adf6ba99e38f4ff3344", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["evidence_416a5dfb545cb300c3b1"]
started_at: "2026-07-17T18:35:33+08:00"
completed_at: "2026-07-17T18:35:33+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_ea6b984ae4bdd1dfdf5288a1.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_62389152cf0723e2f3a753c1 raw_sha256:f12c9547bb3f451ba4585e51e8683948e8b9b703610d5adf6ba99e38f4ff3344"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_62389152cf0723e2f3a753c1 record_sha256:655f55c1bb14f2e2e7e82799dbd12e1cdeebe83d1a1bbbad14ffb49ed5b6f8b6"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:evidence_416a5dfb545cb300c3b1"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:none"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 2 candidates inspected", "candidate:claim_ea6b984ae4bdd1dfdf5288a1", "candidate:source_08e53bb30d37610610477e01"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_62389152cf0723e2f3a753c1"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:43+08:00", "source:source_62389152cf0723e2f3a753c1 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "ac5cdf1893be94bf9c615270002d92b5959e6d6edbd58cbf7843d730bd4ea036", "source_state_sha256": "29fc4c8a9304b61f6d591d339b581fdd19eaca6115d1391eecb48302a179e52e", "source_record_sha256s": {"source_62389152cf0723e2f3a753c1": "655f55c1bb14f2e2e7e82799dbd12e1cdeebe83d1a1bbbad14ffb49ed5b6f8b6"}, "raw_state_sha256": "01a4761ae95e21fb037e478874a6e93131c6ccd0fe09690c13f688676b8b62ad", "evidence_sha256": "b298272d40382eafde43b98e9bf4239c435289e5ffd84339864225a44f73e783", "extraction_state_sha256": "c39163e650125627262abad0e80c039436e67c2b7469f6269e75cc916c76c313", "work_identity_sha256": "f38e07a79426c39e52f4c5ccede4859e271314e666849f01d85701212662c996", "relation_neighborhood_sha256": "f2ed81348a2171aa29f3fea6104e9967d4f0730698795f709bba110dfa1b2a5a", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "searched title; 2 candidates inspected",
        "candidate:claim_ea6b984ae4bdd1dfdf5288a1",
        "candidate:source_08e53bb30d37610610477e01"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "findings": [
        "evidence_entailment:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_revalidated": {
      "findings": [
        "evidence:evidence_416a5dfb545cb300c3b1"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:43+08:00",
        "source:source_62389152cf0723e2f3a753c1 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_62389152cf0723e2f3a753c1 record_sha256:655f55c1bb14f2e2e7e82799dbd12e1cdeebe83d1a1bbbad14ffb49ed5b6f8b6"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_62389152cf0723e2f3a753c1 raw_sha256:f12c9547bb3f451ba4585e51e8683948e8b9b703610d5adf6ba99e38f4ff3344"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_62389152cf0723e2f3a753c1"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_ea6b984ae4bdd1dfdf5288a1.md"
      ],
      "status": "passed",
      "warnings": []
    },
    "source_independence_checked": {
      "findings": [
        "distinct_source_ids:1",
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
  "completed_at": "2026-07-17T18:35:33+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "b298272d40382eafde43b98e9bf4239c435289e5ffd84339864225a44f73e783",
    "extraction_state_sha256": "c39163e650125627262abad0e80c039436e67c2b7469f6269e75cc916c76c313",
    "memory_schema_version": 2,
    "object_sha256": "ac5cdf1893be94bf9c615270002d92b5959e6d6edbd58cbf7843d730bd4ea036",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "01a4761ae95e21fb037e478874a6e93131c6ccd0fe09690c13f688676b8b62ad",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "f2ed81348a2171aa29f3fea6104e9967d4f0730698795f709bba110dfa1b2a5a",
    "source_record_sha256s": {
      "source_62389152cf0723e2f3a753c1": "655f55c1bb14f2e2e7e82799dbd12e1cdeebe83d1a1bbbad14ffb49ed5b6f8b6"
    },
    "source_state_sha256": "29fc4c8a9304b61f6d591d339b581fdd19eaca6115d1391eecb48302a179e52e",
    "work_identity_sha256": "f38e07a79426c39e52f4c5ccede4859e271314e666849f01d85701212662c996"
  },
  "consolidation_id": "consolidation_7e20534ba2b68bcc67fd66b2",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:33+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "evidence_416a5dfb545cb300c3b1"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_7e20534ba2b68bcc67fd66b2",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_ea6b984ae4bdd1dfdf5288a1",
  "object_sha256_after": "ac5cdf1893be94bf9c615270002d92b5959e6d6edbd58cbf7843d730bd4ea036",
  "object_sha256_before": "94cbdaf41a5a74f3e65529d4fc9ade13640fd6db14ce117db0fdeec81c5b6fac",
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
  "started_at": "2026-07-17T18:35:33+08:00",
  "status": "complete",
  "title": "Consolidation: Evolving Intrinsic Motivations for Altruistic Behavior Jane X. Wang, Edward Hughes, Chrisantha Fernando, Wojciech M. Czarnecki, Edgar A. Duéñez-Guzmán, & Joel Z",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:33+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
