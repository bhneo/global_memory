---
id: "consolidation_79a854dba44907e1488a5e56"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: 非特权开放世界移动操作的工具化评测契约"
created_at: "2026-07-29T14:00:06+08:00"
updated_at: "2026-07-29T14:00:06+08:00"
consolidation_id: "consolidation_79a854dba44907e1488a5e56"
object_id: "concept_186fc27b4c190ed39889bb9e"
object_version_before: 1
object_sha256_before: "f60a81befd1e88d0032df246ddaff05bfb62b9e77ab704505d1dc6a761bb0dfd"
object_sha256_after: "595178fa0c49d6132f8adfd3cd14088841766886347c4bbb5a00407aff807bf3"
source_ids: ["source_a5f8ae205338d5f97eea87c7", "source_92fed4343c703da77f798f08"]
source_sha256s: ["7d6568ddbecefded7b02145354ac6d1af42c024a939f9731ad1637d15f88a6c8", "9659c5560a55cef7d207f0ab0102391b3ec7e054f5052a9e057e74b5fa9002db"]
source_records: [{"source_id": "source_a5f8ae205338d5f97eea87c7", "source_record_sha256": "8b8c3935ae162eeacc8d567eaa799615b988e21d34d4f2805dece994ce5a5eaf", "raw_content_sha256": "7d6568ddbecefded7b02145354ac6d1af42c024a939f9731ad1637d15f88a6c8", "work_id": null, "work_document_sha256": null}, {"source_id": "source_92fed4343c703da77f798f08", "source_record_sha256": "705ec68e64a57583faefb8ff9c9029842ab1cfa64cc72e3bee79451cde879c1e", "raw_content_sha256": "9659c5560a55cef7d207f0ab0102391b3ec7e054f5052a9e057e74b5fa9002db", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-29T14:00:03+08:00"
completed_at: "2026-07-29T14:00:06+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_186fc27b4c190ed39889bb9e.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_a5f8ae205338d5f97eea87c7 raw_sha256:7d6568ddbecefded7b02145354ac6d1af42c024a939f9731ad1637d15f88a6c8", "source:source_92fed4343c703da77f798f08 raw_sha256:9659c5560a55cef7d207f0ab0102391b3ec7e054f5052a9e057e74b5fa9002db"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_a5f8ae205338d5f97eea87c7 record_sha256:8b8c3935ae162eeacc8d567eaa799615b988e21d34d4f2805dece994ce5a5eaf", "source:source_92fed4343c703da77f798f08 record_sha256:705ec68e64a57583faefb8ff9c9029842ab1cfa64cc72e3bee79451cde879c1e"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_186fc27b4c190ed39889bb9e"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_a5f8ae205338d5f97eea87c7", "related:concept_typed_verified_robot_skill_graph"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-29T13:58:27+08:00", "source:source_a5f8ae205338d5f97eea87c7 work_sha256:none", "source:source_92fed4343c703da77f798f08 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "595178fa0c49d6132f8adfd3cd14088841766886347c4bbb5a00407aff807bf3", "source_state_sha256": "d8ea93193872a4447eaefa0247ccf8501812761f32b2fd11373ade3582740bd6", "source_record_sha256s": {"source_a5f8ae205338d5f97eea87c7": "8b8c3935ae162eeacc8d567eaa799615b988e21d34d4f2805dece994ce5a5eaf", "source_92fed4343c703da77f798f08": "705ec68e64a57583faefb8ff9c9029842ab1cfa64cc72e3bee79451cde879c1e"}, "raw_state_sha256": "1a2c116e8e6ad4bbbb745f3b779e734ad337076967e3954e4d2ed093aa1773f5", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "4928c897ad2f235e1bb328b5f5665a388a6bf08f1cc89731658b96e029f3b06c", "relation_fingerprint": {"outgoing_relations_sha256": "9525b1645f485c7581feac592a3a81fe9651df892d965ee4f5f827bae124b686", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "9525b1645f485c7581feac592a3a81fe9651df892d965ee4f5f827bae124b686"}, "relation_neighborhood_sha256": "9525b1645f485c7581feac592a3a81fe9651df892d965ee4f5f827bae124b686", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "metadata_updated"
changes: [{"change_type": "metadata_only", "previous_statement": "# 非特权开放世界移动操作的工具化评测契约\n\n面向开放世界移动操作的评测框架：Agent从原始RGB进行探索，通过导航、感知和操作工具执行动作，并在指令含糊时与模拟用户澄清意图；可复现评测还需绑定任务配置、episode生命周期、兼容场景和物体资产，仓库声明的仿真或真机成功率不应脱离这些前提解释。", "new_statement": "# 非特权开放世界移动操作的工具化评测契约\n\n本文件仅作为受治理的 `metadata_only` 输入，将同一 REAL 工作的论文来源并入稳定 Concept；不改变原有陈述。", "changed_fields": ["aliases", "source_ids"], "reason": "Merge the primary-paper source into the stable REAL concept before archiving the duplicate concept.", "trigger_source": "source_92fed4343c703da77f798f08", "evidence_added": []}]
change_summary: "Merge the primary-paper source into the stable REAL concept before archiving the duplicate concept."
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "Merge the primary-paper source into the stable REAL concept before archiving the duplicate concept.",
  "changes": [
    {
      "change_type": "metadata_only",
      "changed_fields": [
        "aliases",
        "source_ids"
      ],
      "evidence_added": [],
      "new_statement": "# 非特权开放世界移动操作的工具化评测契约\n\n本文件仅作为受治理的 `metadata_only` 输入，将同一 REAL 工作的论文来源并入稳定 Concept；不改变原有陈述。",
      "previous_statement": "# 非特权开放世界移动操作的工具化评测契约\n\n面向开放世界移动操作的评测框架：Agent从原始RGB进行探索，通过导航、感知和操作工具执行动作，并在指令含糊时与模拟用户澄清意图；可复现评测还需绑定任务配置、episode生命周期、兼容场景和物体资产，仓库声明的仿真或真机成功率不应脱离这些前提解释。",
      "reason": "Merge the primary-paper source into the stable REAL concept before archiving the duplicate concept.",
      "trigger_source": "source_92fed4343c703da77f798f08"
    }
  ],
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
        "candidate:concept_186fc27b4c190ed39889bb9e"
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
        "object_updated_at:2026-07-29T13:58:27+08:00",
        "source:source_a5f8ae205338d5f97eea87c7 work_sha256:none",
        "source:source_92fed4343c703da77f798f08 work_sha256:none"
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
        "source:source_a5f8ae205338d5f97eea87c7 record_sha256:8b8c3935ae162eeacc8d567eaa799615b988e21d34d4f2805dece994ce5a5eaf",
        "source:source_92fed4343c703da77f798f08 record_sha256:705ec68e64a57583faefb8ff9c9029842ab1cfa64cc72e3bee79451cde879c1e"
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
        "source:source_a5f8ae205338d5f97eea87c7 raw_sha256:7d6568ddbecefded7b02145354ac6d1af42c024a939f9731ad1637d15f88a6c8",
        "source:source_92fed4343c703da77f798f08 raw_sha256:9659c5560a55cef7d207f0ab0102391b3ec7e054f5052a9e057e74b5fa9002db"
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
        "related:source_a5f8ae205338d5f97eea87c7",
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
        "validated:vault/memory/concept/concept_186fc27b4c190ed39889bb9e.md"
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
        "distinct_source_ids:2",
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
  "completed_at": "2026-07-29T14:00:06+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "595178fa0c49d6132f8adfd3cd14088841766886347c4bbb5a00407aff807bf3",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "1a2c116e8e6ad4bbbb745f3b779e734ad337076967e3954e4d2ed093aa1773f5",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "9525b1645f485c7581feac592a3a81fe9651df892d965ee4f5f827bae124b686",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "9525b1645f485c7581feac592a3a81fe9651df892d965ee4f5f827bae124b686"
    },
    "relation_neighborhood_sha256": "9525b1645f485c7581feac592a3a81fe9651df892d965ee4f5f827bae124b686",
    "source_record_sha256s": {
      "source_92fed4343c703da77f798f08": "705ec68e64a57583faefb8ff9c9029842ab1cfa64cc72e3bee79451cde879c1e",
      "source_a5f8ae205338d5f97eea87c7": "8b8c3935ae162eeacc8d567eaa799615b988e21d34d4f2805dece994ce5a5eaf"
    },
    "source_state_sha256": "d8ea93193872a4447eaefa0247ccf8501812761f32b2fd11373ade3582740bd6",
    "work_identity_sha256": "4928c897ad2f235e1bb328b5f5665a388a6bf08f1cc89731658b96e029f3b06c"
  },
  "consolidation_id": "consolidation_79a854dba44907e1488a5e56",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-29T14:00:06+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_79a854dba44907e1488a5e56",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_186fc27b4c190ed39889bb9e",
  "object_sha256_after": "595178fa0c49d6132f8adfd3cd14088841766886347c4bbb5a00407aff807bf3",
  "object_sha256_before": "f60a81befd1e88d0032df246ddaff05bfb62b9e77ab704505d1dc6a761bb0dfd",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "metadata_updated",
  "source_ids": [
    "source_a5f8ae205338d5f97eea87c7",
    "source_92fed4343c703da77f798f08"
  ],
  "source_records": [
    {
      "raw_content_sha256": "7d6568ddbecefded7b02145354ac6d1af42c024a939f9731ad1637d15f88a6c8",
      "source_id": "source_a5f8ae205338d5f97eea87c7",
      "source_record_sha256": "8b8c3935ae162eeacc8d567eaa799615b988e21d34d4f2805dece994ce5a5eaf",
      "work_document_sha256": null,
      "work_id": null
    },
    {
      "raw_content_sha256": "9659c5560a55cef7d207f0ab0102391b3ec7e054f5052a9e057e74b5fa9002db",
      "source_id": "source_92fed4343c703da77f798f08",
      "source_record_sha256": "705ec68e64a57583faefb8ff9c9029842ab1cfa64cc72e3bee79451cde879c1e",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "7d6568ddbecefded7b02145354ac6d1af42c024a939f9731ad1637d15f88a6c8",
    "9659c5560a55cef7d207f0ab0102391b3ec7e054f5052a9e057e74b5fa9002db"
  ],
  "started_at": "2026-07-29T14:00:03+08:00",
  "status": "complete",
  "title": "Consolidation: 非特权开放世界移动操作的工具化评测契约",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-29T14:00:06+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
