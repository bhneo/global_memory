---
id: "consolidation_a0e076f63f0c1220ba187dc6"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: Codex M7 真实读取与 receipt 回写验收"
created_at: "2026-07-17T18:36:01+08:00"
updated_at: "2026-07-17T18:36:01+08:00"
consolidation_id: "consolidation_a0e076f63f0c1220ba187dc6"
object_id: "experiment_b6f1e1956690ac08fd56a5da"
object_version_before: 1
object_sha256_before: "c7fce3be3a850790870071fecebf867b7871190235929bca42acafa82eff004c"
object_sha256_after: "6292fbd646577002efa7ef5f3c2d6b2fab1102e9bdc2eebb3beec3879fbe2e87"
source_ids: ["source_46d0aad5afd18dd21899796f"]
source_sha256s: ["2e13b0cabfba3ebff022f53d7ac3005e994ac0137e0fc131a110a7ecc79f4d8e"]
source_records: [{"source_id": "source_46d0aad5afd18dd21899796f", "source_record_sha256": "0a933462047f72c81f4a5b13962e04f25e48e486905d03f9acdcbdec82ba8cf1", "raw_content_sha256": "2e13b0cabfba3ebff022f53d7ac3005e994ac0137e0fc131a110a7ecc79f4d8e", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-17T18:36:01+08:00"
completed_at: "2026-07-17T18:36:01+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"status": "passed", "findings": ["validated:vault/memory/experiment/experiment_b6f1e1956690ac08fd56a5da.md"], "warnings": []}, "raw_available": {"status": "passed", "findings": ["source:source_46d0aad5afd18dd21899796f raw_sha256:2e13b0cabfba3ebff022f53d7ac3005e994ac0137e0fc131a110a7ecc79f4d8e"], "warnings": []}, "provenance_revalidated": {"status": "passed", "findings": ["source:source_46d0aad5afd18dd21899796f record_sha256:0a933462047f72c81f4a5b13962e04f25e48e486905d03f9acdcbdec82ba8cf1"], "warnings": []}, "evidence_revalidated": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"status": "passed", "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"status": "passed", "findings": ["searched title; 2 candidates inspected", "candidate:experiment_b6f1e1956690ac08fd56a5da", "candidate:experiment_7101e03fb065226e65f388a5"], "warnings": []}, "related_object_search_completed": {"status": "passed", "findings": ["relation index inspected; 1 related objects found", "related:source_46d0aad5afd18dd21899796f"], "warnings": []}, "contradiction_search_completed": {"status": "passed", "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"status": "passed", "findings": ["object_updated_at:2026-07-17T15:24:05+08:00", "source:source_46d0aad5afd18dd21899796f work_sha256:none"], "warnings": []}, "source_independence_checked": {"status": "passed", "findings": ["distinct_source_ids:1", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"status": "passed", "findings": ["drift_reports:0"], "warnings": []}}
consolidation_fingerprint: {"object_sha256": "6292fbd646577002efa7ef5f3c2d6b2fab1102e9bdc2eebb3beec3879fbe2e87", "source_state_sha256": "f30b7c0798fd172e2d3857faca2a8dbe9258b40212c6c37e346b7fad4038d028", "source_record_sha256s": {"source_46d0aad5afd18dd21899796f": "0a933462047f72c81f4a5b13962e04f25e48e486905d03f9acdcbdec82ba8cf1"}, "raw_state_sha256": "2c5ebec5b620b84cc42e95ca4093ec1a004dbe70f899de595144bbb3ba671d92", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "599fff3b90ac590dbc437c120ca90d48732c5c39bceb73024d591c34fe5010bf", "relation_neighborhood_sha256": "bbce8de11bf0eba970a3e3bf37d40c61e335abb424571566222065b3053e6c6b", "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
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
        "candidate:experiment_b6f1e1956690ac08fd56a5da",
        "candidate:experiment_7101e03fb065226e65f388a5"
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
        "object_updated_at:2026-07-17T15:24:05+08:00",
        "source:source_46d0aad5afd18dd21899796f work_sha256:none"
      ],
      "status": "passed",
      "warnings": []
    },
    "provenance_revalidated": {
      "findings": [
        "source:source_46d0aad5afd18dd21899796f record_sha256:0a933462047f72c81f4a5b13962e04f25e48e486905d03f9acdcbdec82ba8cf1"
      ],
      "status": "passed",
      "warnings": []
    },
    "raw_available": {
      "findings": [
        "source:source_46d0aad5afd18dd21899796f raw_sha256:2e13b0cabfba3ebff022f53d7ac3005e994ac0137e0fc131a110a7ecc79f4d8e"
      ],
      "status": "passed",
      "warnings": []
    },
    "related_object_search_completed": {
      "findings": [
        "relation index inspected; 1 related objects found",
        "related:source_46d0aad5afd18dd21899796f"
      ],
      "status": "passed",
      "warnings": []
    },
    "schema_validated": {
      "findings": [
        "validated:vault/memory/experiment/experiment_b6f1e1956690ac08fd56a5da.md"
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
  "completed_at": "2026-07-17T18:36:01+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "6292fbd646577002efa7ef5f3c2d6b2fab1102e9bdc2eebb3beec3879fbe2e87",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "2c5ebec5b620b84cc42e95ca4093ec1a004dbe70f899de595144bbb3ba671d92",
    "receipt_schema_version": 2,
    "relation_neighborhood_sha256": "bbce8de11bf0eba970a3e3bf37d40c61e335abb424571566222065b3053e6c6b",
    "source_record_sha256s": {
      "source_46d0aad5afd18dd21899796f": "0a933462047f72c81f4a5b13962e04f25e48e486905d03f9acdcbdec82ba8cf1"
    },
    "source_state_sha256": "f30b7c0798fd172e2d3857faca2a8dbe9258b40212c6c37e346b7fad4038d028",
    "work_identity_sha256": "599fff3b90ac590dbc437c120ca90d48732c5c39bceb73024d591c34fe5010bf"
  },
  "consolidation_id": "consolidation_a0e076f63f0c1220ba187dc6",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "created_at": "2026-07-17T18:36:01+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_a0e076f63f0c1220ba187dc6",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "experiment_b6f1e1956690ac08fd56a5da",
  "object_sha256_after": "6292fbd646577002efa7ef5f3c2d6b2fab1102e9bdc2eebb3beec3879fbe2e87",
  "object_sha256_before": "c7fce3be3a850790870071fecebf867b7871190235929bca42acafa82eff004c",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "unchanged",
  "source_ids": [
    "source_46d0aad5afd18dd21899796f"
  ],
  "source_records": [
    {
      "raw_content_sha256": "2e13b0cabfba3ebff022f53d7ac3005e994ac0137e0fc131a110a7ecc79f4d8e",
      "source_id": "source_46d0aad5afd18dd21899796f",
      "source_record_sha256": "0a933462047f72c81f4a5b13962e04f25e48e486905d03f9acdcbdec82ba8cf1",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "2e13b0cabfba3ebff022f53d7ac3005e994ac0137e0fc131a110a7ecc79f4d8e"
  ],
  "started_at": "2026-07-17T18:36:01+08:00",
  "status": "complete",
  "title": "Consolidation: Codex M7 真实读取与 receipt 回写验收",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-17T18:36:01+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
