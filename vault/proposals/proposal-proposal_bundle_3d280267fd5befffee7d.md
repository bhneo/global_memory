---
id: "proposal_bundle_3d280267fd5befffee7d"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-21T17:42:01+08:00"
updated_at: "2026-07-21T17:42:02+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_b470fe87f9d09df2b7d3b5fd"]
relations: []
proposal_kind: "compile_bundle"
processor: "agent-semantic-daily-gpt56sol-readmission-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_e98976f6b17c4f967f55c0f7"
input_sha256: "f80199510097fd1765513eef97313ef2277609951eb0e1f9a6dd37756ade4c11"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_relation_triggered_process_safety", "target_path": "vault/knowledge/concepts/concept_relation_triggered_process_safety-关系触发的具身过程安全.md", "base_sha256": null, "candidate_sha256": "64f1d6e27809397688bd00a33be5810f286e16e371c88a8bc1c55b6401f8defe", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_3d280267fd5befffee7d-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_relation_triggered_process_safety.md", "working_at": "2026-07-21T17:42:02+08:00"}]
existing_context: [{"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…This is a WeChat launch report, not the Qwen technical reports, model cards, repositories, or [benchmark] artifacts. Dataset…", "match_reason": "full-text:body"}, {"id": "reflection_59bfe9d29f3ebbb4c8a6b162", "type": "reflection", "title": "Secondary architecture commentary: autoregression versus flow matching is an interface question", "path": "vault/reflections/reflection-reflection_59bfe9d29f3ebbb4c8a6b162.md", "status": "active", "source_ids": ["source_e6608d8f849ad472bbd95143"], "snippet": "…of G0.5, not the official technical report. [Benchmark] numbers, training-data descriptions, tokenizer details, and causal claims…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_b470fe87f9d09df2b7d3b5fd"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`agent-semantic-daily-gpt56sol-readmission-v1`
- Extraction：`extraction_e98976f6b17c4f967f55c0f7`
- 编译前召回已有对象：2
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_relation_triggered_process_safety-关系触发的具身过程安全.md
@@ -0,0 +1,20 @@
+---
+id: "concept_relation_triggered_process_safety"
+type: "concept"
+status: "proposal"
+title: "关系触发的具身过程安全"
+created_at: "2026-07-21T17:42:01+08:00"
+updated_at: "2026-07-21T17:42:01+08:00"
+aliases: ["Relation-Triggered Embodied Process Safety", "SafeRelBench", "Spatial-Relation-Aware Process Safety", "空间关系过程安全"]
+tags: []
+domains: ["embodied-ai", "robot-safety", "spatial-reasoning"]
+confidence: "medium"
+source_ids: ["source_b470fe87f9d09df2b7d3b5fd"]
+relations: [{"type": "derived_from", "target_id": "source_b470fe87f9d09df2b7d3b5fd", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_typed_verified_robot_skill_graph", "reason": "两者都要求在动作执行前检查类型化前置条件；该基准提供过程安全评测，而技能图提供执行结构。", "confidence": "medium", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_b470fe87f9d09df2b7d3b5fd"
+reflection_context: {"reflection_ids": ["reflection_ee2dc3e5679d14ca67d9f5df"], "importance": "high", "changed_belief": "完成任务与安全完成任务必须分开计量；即使最终目标正确，错误动作顺序仍可能造成不可见于终态指标的危险。", "surprising": "七个 VLM Agent 在匹配控制中安全成功率最高达 0.91，而加入空间关系风险后降至 0.16–0.40；增加安全提示仍不足以解决动作落地。", "connections": [{"shared_mechanism": "都用类型化前置条件约束动作序列。", "boundary": "基准中的符号关系和模拟器检查不能替代真实传感、动力学和控制级安全。", "difference": "类型化技能图面向执行前验证契约；SafeRelBench 衡量 Agent 是否在风险动作发生前主动满足关系条件。"}], "open_questions": ["关系安全条件如何从模拟器真值迁移到带感知不确定性的真实场景？"]}
+---
+
+# 关系触发的具身过程安全
+
+将安全条件绑定到会触发风险的具体动作，并要求支撑、容纳、邻近等关系前置条件在该动作执行前成立，而不只检查最终任务状态。SafeRelBench 以 507 个可执行家庭操作样本、匹配非空间控制和 SR/SSR/SRec 指标评测这一缺口；其结果说明任务完成率不能代表过程安全，但模拟关系标注仍需真实感知与动力学验证。
```
