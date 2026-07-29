---
id: "proposal_bundle_5fb495a211a7fa254cbe"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-21T18:09:03+08:00"
updated_at: "2026-07-21T18:09:03+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_46f82af34b1ace2c5c0483af"]
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
extraction_id: "extraction_e73ba5627a6c7eb6d8472171"
input_sha256: "28532a410a13ffdd2810f445234c9ff05c765434b04dfb3cf0e52e2aef57c813"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_8f8ae7b5cac6690d2e341d40", "target_path": "vault/knowledge/concepts/concept_8f8ae7b5cac6690d2e341d40-人形行为基础模型的数量-多样性协同扩展.md", "base_sha256": null, "candidate_sha256": "aa27de85b08659593f82919ab1b7725ddd1443c7ab48dd39f58f347b7ccbd547", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_5fb495a211a7fa254cbe-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_8f8ae7b5cac6690d2e341d40.md", "working_at": "2026-07-21T18:09:03+08:00"}]
existing_context: [{"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…closed-loop control, action alignment, or predictive fidelity.\n\n## Surprising\n\nThe reported manipulation [scaling] claim is conditional: more data…", "match_reason": "full-text:body"}, {"id": "work_arxiv_1811_05931", "type": "work", "title": "[1811.05931] Evolving intrinsic motivations for altruistic behavior", "path": "vault/memory/work/work_arxiv_1811_05931.md", "status": "working", "source_ids": ["source_08e53bb30d37610610477e01", "source_62389152cf0723e2f3a753c1"], "snippet": "# [1811.05931] Evolving intrinsic motivations for altruistic [behavior]\n\n## Logical work identity\n\n- arXiv：`1811.05931`\n- Version：`unknown`\n- Captures：`source…", "match_reason": "metadata:title"}, {"id": "input_dd10d4b6286ecf52c06c0361", "type": "input", "title": "TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation", "path": "vault/inputs/input-input_dd10d4b6286ecf52c06c0361.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "…A Predictive and Reactive Tactile Foundation [Model] for Dexterous Manipulation\n\nInput Episode for `source_283911da72edc403d1b823fb`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "input_a4c337f6b32f32e230317ac9", "type": "input", "title": "GitHub - Tencent-Hunyuan/HY-Embodied: HY-Embodied: Embodied Foundation Models for Real-World Agents · GitHub", "path": "vault/inputs/input-input_a4c337f6b32f32e230317ac9.md", "status": "active", "source_ids": ["source_ffef0c68258ab78320bbe42f"], "snippet": "…Embodied [Foundation] Models for Real-World Agents · GitHub\n\nInput Episode for `source_ffef0c68258ab78320bbe42f`. The immutable Source remains authoritative…", "match_reason": "metadata:title"}, {"id": "input_0cf0fb98f9d994c03625746f", "type": "input", "title": "GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub", "path": "vault/inputs/input-input_0cf0fb98f9d994c03625746f.md", "status": "active", "source_ids": ["source_34d6513b0522739d0b25e303"], "snippet": "…NVIDIA Isaac GR00T N1.7 - A Foundation [Model] for Generalist Robots. · GitHub\n\nInput Episode for `source_34d6513b0522739d0b25e303`. The…", "match_reason": "metadata:title"}, {"id": "concept_27970fb0de0d8995774e31f6", "type": "concept", "title": "多视角具身合成世界模型数据引擎", "path": "vault/memory/concept/concept_27970fb0de0d8995774e31f6.md", "status": "working", "source_ids": ["source_fe986df678d73ef2b6234f0c"], "snippet": "# 多视角具身合成世界模型数据引擎\n\n在保留通用图像与视频生成能力的同时，联合学习多视角具身场景、跨本体结构化编辑和具身视频，使世界基础模型既能预测交互也能生成受机器人与相机约束的策略训练数据。合成数据仍需通过几何、接触和闭环收益验证。", "match_reason": "metadata:aliases"}, {"id": "concept_dual_system_world_action_model", "type": "concept", "title": "双系统 World Action Model", "path": "vault/memory/concept/concept_dual_system_world_action_model.md", "status": "working", "source_ids": ["source_ba057c2c11df2a5eba107870"], "snippet": "# 双系统 World Action [Model]\n\n默认由 World Action [Model] 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_46f82af34b1ace2c5c0483af"}
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
- Extraction：`extraction_e73ba5627a6c7eb6d8472171`
- 编译前召回已有对象：7
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_8f8ae7b5cac6690d2e341d40-人形行为基础模型的数量-多样性协同扩展.md
@@ -0,0 +1,20 @@
+---
+id: "concept_8f8ae7b5cac6690d2e341d40"
+type: "concept"
+status: "proposal"
+title: "人形行为基础模型的数量—多样性协同扩展"
+created_at: "2026-07-21T18:09:03+08:00"
+updated_at: "2026-07-21T18:09:03+08:00"
+aliases: ["Quantity-Diversity Co-Scaling for Humanoid Behavior Foundation Models", "Scaling Behavior Foundation Model", "BFM", "人形行为基础模型扩展"]
+tags: []
+domains: ["humanoid-robotics", "reinforcement-learning", "behavior-foundation-models"]
+confidence: "medium"
+source_ids: ["source_46f82af34b1ace2c5c0483af"]
+relations: [{"type": "derived_from", "target_id": "source_46f82af34b1ace2c5c0483af", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "前者区分训练中产生的数据数量与行为多样性，后者保存部署评估的可回放反馈；二者都需要避免用单一汇总指标掩盖分布覆盖。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_46f82af34b1ace2c5c0483af"
+reflection_context: {"reflection_ids": ["reflection_1b5d5af00fc9d21516615a4b"], "importance": "high", "changed_belief": "此前容易按参考动作数量衡量人形预训练规模；这里应分别追踪并调节在线交互数量、参考动作多样性、全局运动跟踪接口和模型表达能力。", "surprising": "论文将全局坐标系整体轨迹跟踪作为减少行为歧义的统一接口，但这并不意味着局部控制或不同根状态估计下必然获得同样优势。", "connections": [{"shared_mechanism": "两者都以共享的行为表示替代每个任务单独设计奖励或控制逻辑。", "boundary": "连接只适用于行为基础模型的训练与控制接口，不把参考运动跟踪等同于真实任务成功。", "difference": "Scaling BFM讨论人形全身运动的rollout数量和参考分布；跨本体VLA两阶段训练讨论状态转换语言和机器人指令对齐。"}], "open_questions": ["当参考动作覆盖增加但在线rollout预算固定时，如何检测新增多样性是提高泛化还是稀释关键接触和恢复行为？"]}
+---
+
+# 人形行为基础模型的数量—多样性协同扩展
+
+在人形运动跟踪的强化学习预训练中，在线并行环境与rollout时域主要决定有效交互数据数量，经过筛选的参考动作库主要决定行为分布多样性；两者需与全局全身轨迹接口和可扩展模型架构协同评估，而不能以参考动作数量单独替代训练规模。
```
