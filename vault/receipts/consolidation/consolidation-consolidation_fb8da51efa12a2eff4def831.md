---
id: "consolidation_fb8da51efa12a2eff4def831"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: Epiplexity"
created_at: "2026-07-17T18:35:53+08:00"
updated_at: "2026-07-17T18:35:53+08:00"
consolidation_id: "consolidation_fb8da51efa12a2eff4def831"
object_id: "concept_epiplexity"
object_version_before: 1
object_sha256_before: "6e30832bdebb4b9a0dc4ea7aeefe7e22b3c47b4a5d55cdf13b6065977ec770eb"
object_sha256_after: "19abda25c775f528d573fbb235bc773f1ae1ed6c94b8690789450d6e23671d3c"
source_ids: ["source_494ab02c17c5f495f1ed29d0"]
source_sha256s: ["40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d"]
source_records: [{"source_id": "source_494ab02c17c5f495f1ed29d0", "source_record_sha256": "c83384117be8883eece5b9a9da6bcaa1a577c8bb2f8555efa162bc42cf1cf8cb", "raw_content_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-17T18:35:53+08:00"
completed_at: "2026-07-17T18:35:53+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/concept/concept_epiplexity.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_494ab02c17c5f495f1ed29d0 raw_sha256:40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_494ab02c17c5f495f1ed29d0 record_sha256:c83384117be8883eece5b9a9da6bcaa1a577c8bb2f8555efa162bc42cf1cf8cb"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 11 candidates inspected", "candidate:source_deb313c98b03fc4d0b33794a", "candidate:source_494ab02c17c5f495f1ed29d0", "candidate:work_arxiv_2601_03220", "candidate:claim_wechat_epiplexity_definition_20260715", "candidate:analogy_epiplexity_memory"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 4 related objects found", "related:concept_epiplexity", "related:source_494ab02c17c5f495f1ed29d0", "related:concept_epiplexity", "related:concept_epiplexity"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:23:59+08:00", "source:source_494ab02c17c5f495f1ed29d0 work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "19abda25c775f528d573fbb235bc773f1ae1ed6c94b8690789450d6e23671d3c", "source_state_sha256": "455a2309638f5cc2db6b6d70a83a598e0b531a3935fb1de9189cf5dc88aa492d", "source_record_sha256s": {"source_494ab02c17c5f495f1ed29d0": "c83384117be8883eece5b9a9da6bcaa1a577c8bb2f8555efa162bc42cf1cf8cb"}, "raw_state_sha256": "08662ed62cb67f37ccadd5110eefadc9cd30dfc3905e32c21712b0025421a13a", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "2499abf5a62f0fa49b0c285a74b107542496fd3cce6d7b528a73c563102a4412", "relation_neighborhood_sha256": "648e52eacea58e7cb5d6a98c15de11bff140094a3ea1ff3b47faa4ccfce64dd2", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "searched title; 11 candidates inspected",
        "candidate:source_deb313c98b03fc4d0b33794a",
        "candidate:source_494ab02c17c5f495f1ed29d0",
        "candidate:work_arxiv_2601_03220",
        "candidate:claim_wechat_epiplexity_definition_20260715",
        "candidate:analogy_epiplexity_memory"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_entailment_rechecked": {
      "findings": [
        "not applicable for non-claim object"
      ],
      "status": "passed",
      "warnings": []
    },
    "evidence_revalidated": {
      "findings": [
        "not applicable for non-claim object"
      ],
      "status": "passed",
      "warnings": []
    },
    "freshness_checked": {
      "findings": [
        "object_updated_at:2026-07-17T15:23:59+08:00",
        "source:source_494ab02c17c5f495f1ed29d0 work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_494ab02c17c5f495f1ed29d0 record_sha256:c83384117be8883eece5b9a9da6bcaa1a577c8bb2f8555efa162bc42cf1cf8cb"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_494ab02c17c5f495f1ed29d0 raw_sha256:40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 4 related objects found",
        "related:concept_epiplexity",
        "related:source_494ab02c17c5f495f1ed29d0",
        "related:concept_epiplexity",
        "related:concept_epiplexity"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/concept/concept_epiplexity.md"
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
  "completed_at": "2026-07-17T18:35:53+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "19abda25c775f528d573fbb235bc773f1ae1ed6c94b8690789450d6e23671d3c",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "08662ed62cb67f37ccadd5110eefadc9cd30dfc3905e32c21712b0025421a13a",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "648e52eacea58e7cb5d6a98c15de11bff140094a3ea1ff3b47faa4ccfce64dd2",
    "source_record_sha256s": {
      "source_494ab02c17c5f495f1ed29d0": "c83384117be8883eece5b9a9da6bcaa1a577c8bb2f8555efa162bc42cf1cf8cb"
    },
    "source_state_sha256": "455a2309638f5cc2db6b6d70a83a598e0b531a3935fb1de9189cf5dc88aa492d",
    "work_identity_sha256": "2499abf5a62f0fa49b0c285a74b107542496fd3cce6d7b528a73c563102a4412"
  },
  "consolidation_id": "consolidation_fb8da51efa12a2eff4def831",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:35:53+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_fb8da51efa12a2eff4def831",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_epiplexity",
  "object_sha256_after": "19abda25c775f528d573fbb235bc773f1ae1ed6c94b8690789450d6e23671d3c",
  "object_sha256_before": "6e30832bdebb4b9a0dc4ea7aeefe7e22b3c47b4a5d55cdf13b6065977ec770eb",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_494ab02c17c5f495f1ed29d0"
  ],
  "source_records": [
    {
      "raw_content_sha256": "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d",
      "source_id": "source_494ab02c17c5f495f1ed29d0",
      "source_record_sha256": "c83384117be8883eece5b9a9da6bcaa1a577c8bb2f8555efa162bc42cf1cf8cb",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "40dcd2356d0295f225991b186dd407fc56fdc0c0a81555ee276cdb2b2f3f472d"
  ],
  "started_at": "2026-07-17T18:35:53+08:00",
  "status": "complete",
  "title": "Consolidation: Epiplexity",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:35:53+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
