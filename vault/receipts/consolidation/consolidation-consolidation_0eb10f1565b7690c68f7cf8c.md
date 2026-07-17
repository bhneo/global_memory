---
id: "consolidation_0eb10f1565b7690c68f7cf8c"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence Marc Finzi∗1 Shikai Qiu∗2 Yiding Jiang∗1 Pavel Izmailov2 J. Zico Kol"
created_at: "2026-07-17T18:35:26+08:00"
updated_at: "2026-07-17T18:35:26+08:00"
consolidation_id: "consolidation_0eb10f1565b7690c68f7cf8c"
object_id: "claim_ad8c28d32a7d55ab2806574d"
object_version_before: 1
object_sha256_before: "5330f6a4538a89a8f19cc48554d81900943ca5165202f9698945c9533c0dd757"
object_sha256_after: "c461eace7bff25cc1dc3e2300844bb28f4b0e03e1a31db354c832c43b85df468"
source_ids: ["source_1c0f944bf6b14cf9d1fff939"]
source_sha256s: ["8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c"]
source_records: [{"source_id": "source_1c0f944bf6b14cf9d1fff939", "source_record_sha256": "0a2d70b38b3383e6aa78f3bbbba3f3602921cbf2890fbd2c497bd2921ef4ef6f", "raw_content_sha256": "8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c", "work_id": null, "work_document_sha256": null}]
evidence_ids: ["evidence_21e8c945846dd77a8e9c"]
started_at: "2026-07-17T18:35:25+08:00"
completed_at: "2026-07-17T18:35:26+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/claim/claim_ad8c28d32a7d55ab2806574d.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_1c0f944bf6b14cf9d1fff939 raw_sha256:8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_1c0f944bf6b14cf9d1fff939 record_sha256:0a2d70b38b3383e6aa78f3bbbba3f3602921cbf2890fbd2c497bd2921ef4ef6f"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["evidence:evidence_21e8c945846dd77a8e9c"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["evidence_entailment:none"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 1 candidates inspected", "candidate:claim_ad8c28d32a7d55ab2806574d"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_1c0f944bf6b14cf9d1fff939"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:37+08:00", "source:source_1c0f944bf6b14cf9d1fff939 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "c461eace7bff25cc1dc3e2300844bb28f4b0e03e1a31db354c832c43b85df468", "source_state_sha256": "029f2a98a346756be0dd5086d5a7dc1ed76d1d9dfbb671f33397e858138e68f6", "source_record_sha256s": {"source_1c0f944bf6b14cf9d1fff939": "0a2d70b38b3383e6aa78f3bbbba3f3602921cbf2890fbd2c497bd2921ef4ef6f"}, "raw_state_sha256": "531bbaee0a083ad75b7b2a9cbc29fee1e0e0f8d001271d9beb9220c77f9afabb", "evidence_sha256": "7656816ce6e3f702b2d3adda8761eacf0cc7d2e50ed5522024ae9097d3a732e3", "extraction_state_sha256": "d95a96d63be6bbcaef6e54e2ab8888ea84ede06dd3e0826e939941f43b47f80c", "work_identity_sha256": "b37b78741bd022bdac18339c6a4713b30940e01e7193cb7aa2f5be62ae728ab2", "relation_neighborhood_sha256": "154b29d16526c21d1a7bb1f4455537e5f1556e422134249c3262fddbe5813137", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "searched title; 1 candidates inspected",
        "candidate:claim_ad8c28d32a7d55ab2806574d"
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
        "evidence:evidence_21e8c945846dd77a8e9c"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:37+08:00",
        "source:source_1c0f944bf6b14cf9d1fff939 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_1c0f944bf6b14cf9d1fff939 record_sha256:0a2d70b38b3383e6aa78f3bbbba3f3602921cbf2890fbd2c497bd2921ef4ef6f"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_1c0f944bf6b14cf9d1fff939 raw_sha256:8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_1c0f944bf6b14cf9d1fff939"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/claim/claim_ad8c28d32a7d55ab2806574d.md"
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
  "completed_at": "2026-07-17T18:35:26+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "7656816ce6e3f702b2d3adda8761eacf0cc7d2e50ed5522024ae9097d3a732e3",
    "extraction_state_sha256": "d95a96d63be6bbcaef6e54e2ab8888ea84ede06dd3e0826e939941f43b47f80c",
    "memory_schema_version": 2,
    "object_sha256": "c461eace7bff25cc1dc3e2300844bb28f4b0e03e1a31db354c832c43b85df468",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "531bbaee0a083ad75b7b2a9cbc29fee1e0e0f8d001271d9beb9220c77f9afabb",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "154b29d16526c21d1a7bb1f4455537e5f1556e422134249c3262fddbe5813137",
    "source_record_sha256s": {
      "source_1c0f944bf6b14cf9d1fff939": "0a2d70b38b3383e6aa78f3bbbba3f3602921cbf2890fbd2c497bd2921ef4ef6f"
    },
    "source_state_sha256": "029f2a98a346756be0dd5086d5a7dc1ed76d1d9dfbb671f33397e858138e68f6",
    "work_identity_sha256": "b37b78741bd022bdac18339c6a4713b30940e01e7193cb7aa2f5be62ae728ab2"
  },
  "consolidation_id": "consolidation_0eb10f1565b7690c68f7cf8c",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:26+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [
    "evidence_21e8c945846dd77a8e9c"
  ],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_0eb10f1565b7690c68f7cf8c",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "claim_ad8c28d32a7d55ab2806574d",
  "object_sha256_after": "c461eace7bff25cc1dc3e2300844bb28f4b0e03e1a31db354c832c43b85df468",
  "object_sha256_before": "5330f6a4538a89a8f19cc48554d81900943ca5165202f9698945c9533c0dd757",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_1c0f944bf6b14cf9d1fff939"
  ],
  "source_records": [
    {
      "raw_content_sha256": "8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c",
      "source_id": "source_1c0f944bf6b14cf9d1fff939",
      "source_record_sha256": "0a2d70b38b3383e6aa78f3bbbba3f3602921cbf2890fbd2c497bd2921ef4ef6f",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "8c67d250b0507f341bf3bd91961c28ebde33290c8548f4af48d0e5683699488c"
  ],
  "started_at": "2026-07-17T18:35:25+08:00",
  "status": "complete",
  "title": "Consolidation: From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence Marc Finzi∗1 Shikai Qiu∗2 Yiding Jiang∗1 Pavel Izmailov2 J. Zico Kol",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:26+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
