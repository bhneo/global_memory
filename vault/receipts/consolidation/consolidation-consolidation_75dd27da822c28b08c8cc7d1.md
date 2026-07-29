---
id: "consolidation_75dd27da822c28b08c8cc7d1"
type: "consolidation_receipt"
receipt_schema_version: 2
status: "complete"
execution_status: "complete"
validation_outcome: "passed"
title: "Consolidation: R3 restriction 与 Kakeya 几何改进 / R3 restriction and Kakeya-geometric improvements"
created_at: "2026-07-27T16:02:00+08:00"
updated_at: "2026-07-27T16:02:00+08:00"
consolidation_id: "consolidation_75dd27da822c28b08c8cc7d1"
object_id: "concept_0ea689b9ff94e453dd23b64b"
object_version_before: 1
object_sha256_before: "eff3f2e9c1ac4a6d67c318333666e87887ae0e97e7a176d9ac22920c7e9b27ff"
object_sha256_after: "9898e67ea59e5dd8aa953c21e8028fe76a41ad313ecb0145e84a4c6639fffb8d"
source_ids: ["source_299adfe6dd42f97b6f75b777", "source_b6d55666cda69c2a1c407986"]
source_sha256s: ["af745d5dd5f06081d696714a7ab93155e2cd81a73986163c39472ca83549ca04", "4f49125d72501b7b0eebcd4f7136c070d0cd4d1b259817c86738e831e98b60cd"]
source_records: [{"source_id": "source_299adfe6dd42f97b6f75b777", "source_record_sha256": "49c8f2ac1072f62499ee58cb87a67a0956fc5f88871491e4291aef6e9c35a2c5", "raw_content_sha256": "af745d5dd5f06081d696714a7ab93155e2cd81a73986163c39472ca83549ca04", "work_id": null, "work_document_sha256": null}, {"source_id": "source_b6d55666cda69c2a1c407986", "source_record_sha256": "cfa6b94ada59148f26930ff496f9eabe0edaf9833fbec50ab6696d2fc62cf53b", "raw_content_sha256": "4f49125d72501b7b0eebcd4f7136c070d0cd4d1b259817c86738e831e98b60cd", "work_id": null, "work_document_sha256": null}]
evidence_ids: []
started_at: "2026-07-27T16:01:59+08:00"
completed_at: "2026-07-27T16:02:00+08:00"
consolidator: "deterministic"
consolidator_version: "trustworthy-consolidation-v2"
model_provider: "none"
model_version: "none"
checks: {"schema_validated": true, "raw_available": true, "provenance_revalidated": true, "evidence_revalidated": true, "evidence_entailment_rechecked": true, "duplicate_search_completed": true, "related_object_search_completed": true, "contradiction_search_completed": true, "freshness_checked": true, "source_independence_checked": true, "drift_checked": true}
check_details: {"schema_validated": {"check_name": "schema_validated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["validated:vault/memory/concept/concept_0ea689b9ff94e453dd23b64b.md"], "warnings": []}, "raw_available": {"check_name": "raw_available", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_299adfe6dd42f97b6f75b777 raw_sha256:af745d5dd5f06081d696714a7ab93155e2cd81a73986163c39472ca83549ca04", "source:source_b6d55666cda69c2a1c407986 raw_sha256:4f49125d72501b7b0eebcd4f7136c070d0cd4d1b259817c86738e831e98b60cd"], "warnings": []}, "provenance_revalidated": {"check_name": "provenance_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["source:source_299adfe6dd42f97b6f75b777 record_sha256:49c8f2ac1072f62499ee58cb87a67a0956fc5f88871491e4291aef6e9c35a2c5", "source:source_b6d55666cda69c2a1c407986 record_sha256:cfa6b94ada59148f26930ff496f9eabe0edaf9833fbec50ab6696d2fc62cf53b"], "warnings": []}, "evidence_revalidated": {"check_name": "evidence_revalidated", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "evidence_entailment_rechecked": {"check_name": "evidence_entailment_rechecked", "execution_status": "completed", "validation_outcome": "not_applicable", "method": "declared-metadata-inspection", "semantic_recheck_performed": true, "declared_value": null, "findings": ["not applicable for non-claim object"], "warnings": []}, "duplicate_search_completed": {"check_name": "duplicate_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["searched title; 1 candidates inspected", "candidate:concept_0ea689b9ff94e453dd23b64b"], "warnings": []}, "related_object_search_completed": {"check_name": "related_object_search_completed", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["relation index inspected; 2 related objects found", "related:source_299adfe6dd42f97b6f75b777", "related:concept_c0e590dd716efa867bc34cbd"], "warnings": []}, "contradiction_search_completed": {"check_name": "contradiction_search_completed", "execution_status": "completed", "validation_outcome": "clear", "method": "relation-index-query", "semantic_recheck_performed": null, "declared_value": null, "findings": ["contradiction relations inspected; 0 found"], "warnings": []}, "freshness_checked": {"check_name": "freshness_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["object_updated_at:2026-07-27T16:01:40+08:00", "source:source_299adfe6dd42f97b6f75b777 work_sha256:none", "source:source_b6d55666cda69c2a1c407986 work_sha256:none"], "warnings": []}, "source_independence_checked": {"check_name": "source_independence_checked", "execution_status": "completed", "validation_outcome": "not_established", "method": "logical-work-identity-count", "semantic_recheck_performed": null, "declared_value": null, "findings": ["distinct_source_ids:2", "distinct_work_ids:0"], "warnings": []}, "drift_checked": {"check_name": "drift_checked", "execution_status": "completed", "validation_outcome": "passed", "method": "deterministic repository check", "semantic_recheck_performed": null, "declared_value": null, "findings": ["drift_reports:0"], "warnings": []}}
contradiction_search: {"execution_status": "completed", "outgoing": [], "incoming": [], "unresolved_count": 0, "validation_outcome": "clear"}
consolidation_fingerprint: {"object_sha256": "9898e67ea59e5dd8aa953c21e8028fe76a41ad313ecb0145e84a4c6639fffb8d", "source_state_sha256": "27bba9d600090917c218401e0a0a3f5ce875cd8daf5d7eb31140dfbe17b70f03", "source_record_sha256s": {"source_299adfe6dd42f97b6f75b777": "49c8f2ac1072f62499ee58cb87a67a0956fc5f88871491e4291aef6e9c35a2c5", "source_b6d55666cda69c2a1c407986": "cfa6b94ada59148f26930ff496f9eabe0edaf9833fbec50ab6696d2fc62cf53b"}, "raw_state_sha256": "94e26c7ba1489331e09241415db151d596fff635c4e1e83b746613a5356ddc59", "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "work_identity_sha256": "2ee5ed2508472aabf6c733cd674e15232821f9b7d1b53663f2f8dc7e89c31915", "relation_fingerprint": {"outgoing_relations_sha256": "b52ccc5a87fcefd8ce422867c01daae5479ea29f28b927a3cefc8b38a3a5fc1f", "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945", "full_neighborhood_sha256": "b52ccc5a87fcefd8ce422867c01daae5479ea29f28b927a3cefc8b38a3a5fc1f"}, "relation_neighborhood_sha256": "b52ccc5a87fcefd8ce422867c01daae5479ea29f28b927a3cefc8b38a3a5fc1f", "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b", "receipt_schema_version": 2, "memory_schema_version": 2, "consolidator_version": "trustworthy-consolidation-v2", "drift_policy_version": "semantic-drift-v2", "promotion_policy_version": "trusted-promotion-v3-receipt-v2"}
drift_policy_version: "semantic-drift-v2"
result: "refined"
changes: [{"change_type": "refine", "previous_statement": "# 三维 restriction 的 Kakeya--decoupling 指数改进 / Kakeya--decoupling improvement for restriction in R3\n\nWang 与 Wu 的摘要将 R3 中 Lp→Lp restriction 估计的适用范围改进为 p>3+3/14，并归因于 Kakeya 型 incidence estimates 与 refined decoupling 的结合。该条目只记录论文摘要中的定量结果和方法标签，不代表完整线性 restriction 理论已解决。", "new_statement": "# 三维 restriction 的 Kakeya--decoupling 指数改进 / Kakeya--decoupling improvement for restriction in R3\n\nWang 与 Wu 的摘要将 R3 中 Lp→Lp restriction 估计的适用范围改进为 p>3+3/14，并归因于 Kakeya 型 incidence estimates 与 refined decoupling 的结合。该条目只记录论文摘要中的定量结果和方法标签，不代表完整线性 restriction 理论已解决。\n\n## 新增来源材料\n\n- `source_b6d55666cda69c2a1c407986`：对 R3 中紧致、光滑且第二基本形式严格正的曲面，Guth 以 polynomial partitioning 控制 extension 波包，证明 L2(S) 到 Lp(R3) 的 restriction estimate 在 p>3.25 时成立；这是特定曲率与范数下的线性改进，不等同于预期 p>3 的完整 Stein restriction conjecture。", "changed_fields": [], "reason": "compile bundle from source_b6d55666cda69c2a1c407986", "trigger_source": "source_b6d55666cda69c2a1c407986", "evidence_added": []}]
change_summary: "compile bundle from source_b6d55666cda69c2a1c407986"
warnings: []
exceptions_created: []
promotion_recommendation: "evaluate"
---

# Consolidation Receipt

```json
{
  "change_summary": "compile bundle from source_b6d55666cda69c2a1c407986",
  "changes": [
    {
      "change_type": "refine",
      "changed_fields": [],
      "evidence_added": [],
      "new_statement": "# 三维 restriction 的 Kakeya--decoupling 指数改进 / Kakeya--decoupling improvement for restriction in R3\n\nWang 与 Wu 的摘要将 R3 中 Lp→Lp restriction 估计的适用范围改进为 p>3+3/14，并归因于 Kakeya 型 incidence estimates 与 refined decoupling 的结合。该条目只记录论文摘要中的定量结果和方法标签，不代表完整线性 restriction 理论已解决。\n\n## 新增来源材料\n\n- `source_b6d55666cda69c2a1c407986`：对 R3 中紧致、光滑且第二基本形式严格正的曲面，Guth 以 polynomial partitioning 控制 extension 波包，证明 L2(S) 到 Lp(R3) 的 restriction estimate 在 p>3.25 时成立；这是特定曲率与范数下的线性改进，不等同于预期 p>3 的完整 Stein restriction conjecture。",
      "previous_statement": "# 三维 restriction 的 Kakeya--decoupling 指数改进 / Kakeya--decoupling improvement for restriction in R3\n\nWang 与 Wu 的摘要将 R3 中 Lp→Lp restriction 估计的适用范围改进为 p>3+3/14，并归因于 Kakeya 型 incidence estimates 与 refined decoupling 的结合。该条目只记录论文摘要中的定量结果和方法标签，不代表完整线性 restriction 理论已解决。",
      "reason": "compile bundle from source_b6d55666cda69c2a1c407986",
      "trigger_source": "source_b6d55666cda69c2a1c407986"
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
        "candidate:concept_0ea689b9ff94e453dd23b64b"
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
        "object_updated_at:2026-07-27T16:01:40+08:00",
        "source:source_299adfe6dd42f97b6f75b777 work_sha256:none",
        "source:source_b6d55666cda69c2a1c407986 work_sha256:none"
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
        "source:source_299adfe6dd42f97b6f75b777 record_sha256:49c8f2ac1072f62499ee58cb87a67a0956fc5f88871491e4291aef6e9c35a2c5",
        "source:source_b6d55666cda69c2a1c407986 record_sha256:cfa6b94ada59148f26930ff496f9eabe0edaf9833fbec50ab6696d2fc62cf53b"
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
        "source:source_299adfe6dd42f97b6f75b777 raw_sha256:af745d5dd5f06081d696714a7ab93155e2cd81a73986163c39472ca83549ca04",
        "source:source_b6d55666cda69c2a1c407986 raw_sha256:4f49125d72501b7b0eebcd4f7136c070d0cd4d1b259817c86738e831e98b60cd"
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
        "related:source_299adfe6dd42f97b6f75b777",
        "related:concept_c0e590dd716efa867bc34cbd"
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
        "validated:vault/memory/concept/concept_0ea689b9ff94e453dd23b64b.md"
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
  "completed_at": "2026-07-27T16:02:00+08:00",
  "consolidation_fingerprint": {
    "consolidator_version": "trustworthy-consolidation-v2",
    "contradictions_sha256": "17d35d182c9ceebd5c99aabdd4299838ea08f22782f21b0b588dbecee2c2574b",
    "drift_policy_version": "semantic-drift-v2",
    "evidence_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "extraction_state_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "memory_schema_version": 2,
    "object_sha256": "9898e67ea59e5dd8aa953c21e8028fe76a41ad313ecb0145e84a4c6639fffb8d",
    "promotion_policy_version": "trusted-promotion-v3-receipt-v2",
    "raw_state_sha256": "94e26c7ba1489331e09241415db151d596fff635c4e1e83b746613a5356ddc59",
    "receipt_schema_version": 2,
    "relation_fingerprint": {
      "full_neighborhood_sha256": "b52ccc5a87fcefd8ce422867c01daae5479ea29f28b927a3cefc8b38a3a5fc1f",
      "incoming_relations_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
      "outgoing_relations_sha256": "b52ccc5a87fcefd8ce422867c01daae5479ea29f28b927a3cefc8b38a3a5fc1f"
    },
    "relation_neighborhood_sha256": "b52ccc5a87fcefd8ce422867c01daae5479ea29f28b927a3cefc8b38a3a5fc1f",
    "source_record_sha256s": {
      "source_299adfe6dd42f97b6f75b777": "49c8f2ac1072f62499ee58cb87a67a0956fc5f88871491e4291aef6e9c35a2c5",
      "source_b6d55666cda69c2a1c407986": "cfa6b94ada59148f26930ff496f9eabe0edaf9833fbec50ab6696d2fc62cf53b"
    },
    "source_state_sha256": "27bba9d600090917c218401e0a0a3f5ce875cd8daf5d7eb31140dfbe17b70f03",
    "work_identity_sha256": "2ee5ed2508472aabf6c733cd674e15232821f9b7d1b53663f2f8dc7e89c31915"
  },
  "consolidation_id": "consolidation_75dd27da822c28b08c8cc7d1",
  "consolidator": "deterministic",
  "consolidator_version": "trustworthy-consolidation-v2",
  "contradiction_search": {
    "execution_status": "completed",
    "incoming": [],
    "outgoing": [],
    "unresolved_count": 0,
    "validation_outcome": "clear"
  },
  "created_at": "2026-07-27T16:02:00+08:00",
  "drift_policy_version": "semantic-drift-v2",
  "evidence_ids": [],
  "exceptions_created": [],
  "execution_status": "complete",
  "id": "consolidation_75dd27da822c28b08c8cc7d1",
  "model_provider": "none",
  "model_version": "none",
  "object_id": "concept_0ea689b9ff94e453dd23b64b",
  "object_sha256_after": "9898e67ea59e5dd8aa953c21e8028fe76a41ad313ecb0145e84a4c6639fffb8d",
  "object_sha256_before": "eff3f2e9c1ac4a6d67c318333666e87887ae0e97e7a176d9ac22920c7e9b27ff",
  "object_version_before": 1,
  "promotion_recommendation": "evaluate",
  "receipt_schema_version": 2,
  "result": "refined",
  "source_ids": [
    "source_299adfe6dd42f97b6f75b777",
    "source_b6d55666cda69c2a1c407986"
  ],
  "source_records": [
    {
      "raw_content_sha256": "af745d5dd5f06081d696714a7ab93155e2cd81a73986163c39472ca83549ca04",
      "source_id": "source_299adfe6dd42f97b6f75b777",
      "source_record_sha256": "49c8f2ac1072f62499ee58cb87a67a0956fc5f88871491e4291aef6e9c35a2c5",
      "work_document_sha256": null,
      "work_id": null
    },
    {
      "raw_content_sha256": "4f49125d72501b7b0eebcd4f7136c070d0cd4d1b259817c86738e831e98b60cd",
      "source_id": "source_b6d55666cda69c2a1c407986",
      "source_record_sha256": "cfa6b94ada59148f26930ff496f9eabe0edaf9833fbec50ab6696d2fc62cf53b",
      "work_document_sha256": null,
      "work_id": null
    }
  ],
  "source_sha256s": [
    "af745d5dd5f06081d696714a7ab93155e2cd81a73986163c39472ca83549ca04",
    "4f49125d72501b7b0eebcd4f7136c070d0cd4d1b259817c86738e831e98b60cd"
  ],
  "started_at": "2026-07-27T16:01:59+08:00",
  "status": "complete",
  "title": "Consolidation: R3 restriction 与 Kakeya 几何改进 / R3 restriction and Kakeya-geometric improvements",
  "type": "consolidation_receipt",
  "updated_at": "2026-07-27T16:02:00+08:00",
  "validation_outcome": "passed",
  "warnings": []
}
```
