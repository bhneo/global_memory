---
id: "proposal_bundle_8444df72003b7db35ca8"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-21T18:08:34+08:00"
updated_at: "2026-07-21T18:08:35+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_5df8ebbcd9bd1afec33d46cc"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-real-daily-v1"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_116bbf92a70281528e7c766c"
input_sha256: "fb589afdf0299c47cf4db2a80d29005bbfbef2cee60c97f8dd36d51ef993b8fb"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_39512575bdcd8ac68d340b03", "target_path": "vault/knowledge/concepts/concept_39512575bdcd8ac68d340b03-状态转换语言驱动的跨本体-vla-两阶段训练.md", "base_sha256": null, "candidate_sha256": "6669b81804048054bc0ebc47209fca7b74e27b69311dd969d33e228453df4df4", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_8444df72003b7db35ca8-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_39512575bdcd8ac68d340b03.md", "working_at": "2026-07-21T18:08:35+08:00"}]
existing_context: [{"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…closed-loop control, action alignment, or predictive fidelity.\n\n## Surprising\n\nThe reported manipulation [scaling] claim is conditional: more data…", "match_reason": "full-text:body"}, {"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-Complex Structured Demonstrations for [Vision-Language-Action] Learning\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "input_5cdcb4ea55f4352398dddd8c", "type": "input", "title": "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement", "path": "vault/inputs/input-input_5cdcb4ea55f4352398dddd8c.md", "status": "active", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# Training-Free Acceleration for Vision-Language-Action [Models] with Action Caching and Refinement\n\nInput Episode for `source_291d6174cf92660287138f47…", "match_reason": "metadata:title"}, {"id": "input_bf6f63ea23391740118ba725", "type": "input", "title": "Frontier Models with Our Harness Achieve ~99% on ARC-AGI-3 Public — Schema", "path": "vault/inputs/input-input_bf6f63ea23391740118ba725.md", "status": "active", "source_ids": ["source_d90b4e9bf278dfc5e68d1bb5"], "snippet": "# Frontier [Models] with Our Harness Achieve ~99% on ARC-AGI-3 Public — Schema\n\nInput Episode for `source_d90b4e9bf278dfc5e68d1bb5…", "match_reason": "metadata:title"}, {"id": "input_a4c337f6b32f32e230317ac9", "type": "input", "title": "GitHub - Tencent-Hunyuan/HY-Embodied: HY-Embodied: Embodied Foundation Models for Real-World Agents · GitHub", "path": "vault/inputs/input-input_a4c337f6b32f32e230317ac9.md", "status": "active", "source_ids": ["source_ffef0c68258ab78320bbe42f"], "snippet": "…Embodied Foundation [Models] for Real-World Agents · GitHub\n\nInput Episode for `source_ffef0c68258ab78320bbe42f`. The immutable Source remains authoritative…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_5df8ebbcd9bd1afec33d46cc"}
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

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_116bbf92a70281528e7c766c`
- 编译前召回已有对象：5
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_39512575bdcd8ac68d340b03-状态转换语言驱动的跨本体-vla-两阶段训练.md
@@ -0,0 +1,20 @@
+---
+id: "concept_39512575bdcd8ac68d340b03"
+type: "concept"
+status: "proposal"
+title: "状态转换语言驱动的跨本体 VLA 两阶段训练"
+created_at: "2026-07-21T18:08:34+08:00"
+updated_at: "2026-07-21T18:08:34+08:00"
+aliases: ["State-Transition Language Driven Cross-Embodiment VLA Training", "Xiaomi-Robotics-1", "状态转换语言跨本体训练"]
+tags: []
+domains: ["embodied-ai", "vla", "robot-learning"]
+confidence: "medium"
+source_ids: ["source_5df8ebbcd9bd1afec33d46cc"]
+relations: [{"type": "derived_from", "target_id": "source_5df8ebbcd9bd1afec33d46cc", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "前者定义训练数据如何跨本体对齐，后者定义对齐后的策略如何被真实执行记录和评估；两者共同需要保留任务与本体边界。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_5df8ebbcd9bd1afec33d46cc"
+reflection_context: {"reflection_ids": ["reflection_3ea617cf483f3d85a6aa4d31"], "importance": "high", "changed_belief": "此前容易把 VLA 扩展理解为只增加遥操作小时数；这里的关键变化是，能扩展的预训练数据需要有与动作结果相连的状态转换语言，且仍需单独处理末端执行器和提示形式的本体差异。", "surprising": "论文报告预训练规模收益会转移到未见环境的后训练真机评估，但这一结果仅适用于其两阶段数据、模型和评测设置，不能替代接触安全或任务特定验证。", "connections": [{"shared_mechanism": "两者都通过结构化数据接口把模型训练连接到可回放的真实机器人评估。", "boundary": "该连接只涉及训练数据语义与评估闭环的衔接，不把一次评测日志变成对跨本体泛化的证据。", "difference": "Xiaomi-Robotics-1处理预训练到后训练的语言和动作本体对齐；真机部署评估闭环强调每次执行的日志、评分和训练反馈。"}], "open_questions": ["固定长度轨迹的状态转换自动标注在长程任务中何时会丢失对接触前提、失败恢复或子目标顺序的必要约束？"]}
+---
+
+# 状态转换语言驱动的跨本体 VLA 两阶段训练
+
+先用大规模轨迹中自动生成的场景状态转换语言训练观察和语言到动作块的映射，再用跨本体机器人数据把该能力对齐到机器人动作空间与祈使任务指令的 VLA 训练配方；其跨本体收益应按目标本体、任务和真机评测分别验证。
```
