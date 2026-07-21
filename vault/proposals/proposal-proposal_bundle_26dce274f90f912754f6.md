---
id: "proposal_bundle_26dce274f90f912754f6"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T18:05:48+08:00"
updated_at: "2026-07-20T18:05:49+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_38cba686373b003398483ab2"]
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
extraction_id: "extraction_d13570dcddb3e3847630b7d4"
input_sha256: "e11eb6aacf2a81fe62488337d3e1b0ee926b325ed36b634b5713b2a772e36965"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_09dc6e910b167ba474c89c38", "target_path": "vault/knowledge/concepts/concept_09dc6e910b167ba474c89c38-世界动作模型的激活空间鲁棒性-steering.md", "base_sha256": null, "candidate_sha256": "2a683c19cf677b9bfa8a8ef20b37df31da4e5b020687e820d69c978dceb366d6", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_26dce274f90f912754f6-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_09dc6e910b167ba474c89c38.md", "working_at": "2026-07-20T18:05:49+08:00"}]
existing_context: [{"id": "reflection_4430cc70fe95425f717c1e71", "type": "reflection", "title": "RPent：把冻结 VLA 放进可递归反思的具身 Agent 外壳", "path": "vault/reflections/reflection-reflection_4430cc70fe95425f717c1e71.md", "status": "active", "source_ids": ["source_6b52a51e2b4a3be43c97c386"], "snippet": "…并增加时延与故障面。\n\n## Open questions\n\n- Harness VLA 中 memory-guided [steering] 的具体记忆单元、失败恢复机制和相对无记忆基线收益是什么？\n\n## Possible mechanisms\n\n- 服务化边界把感知、规划和动作原语解耦，使失败轨迹能够被上层记忆重解释并改变后续调用策略。\n\n## Future directions…", "match_reason": "full-text:body"}, {"id": "concept_sensor_conditional_expert_routing", "type": "concept", "title": "传感器条件化专家路由", "path": "vault/memory/concept/concept_sensor_conditional_expert_routing.md", "status": "working", "source_ids": ["source_5d8306b5caf7371feeacbc09"], "snippet": "# 传感器条件化专家路由\n\n根据传感器是否可用选择模态专用稀疏专家，并根据任务意图路由动作侧表示，使 VLA 能利用辅助传感器，同时在传感器缺失时退化而非整体失效。", "match_reason": "metadata:domains"}, {"id": "concept_dual_system_world_action_model", "type": "concept", "title": "双系统 World Action Model", "path": "vault/memory/concept/concept_dual_system_world_action_model.md", "status": "working", "source_ids": ["source_ba057c2c11df2a5eba107870"], "snippet": "# 双系统 [World] Action Model\n\n默认由 [World] Action Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "match_reason": "metadata:title"}, {"id": "concept_ab253cb9064bc1b550d5e973", "type": "concept", "title": "跨本体世界监督通道", "path": "vault/memory/concept/concept_ab253cb9064bc1b550d5e973.md", "status": "working", "source_ids": ["source_61f3045b170e78e4adb2422c"], "snippet": "# 跨本体世界监督通道\n\n在人类与机器人联合训练中，用未来场景表示作为独立于动作标签的监督通道，使共享骨干优先吸收对象、场景和物理变化，同时通过外观抽象、跨本体一致性和 ego-motion 分离降低形态与行为风格泄漏。", "match_reason": "metadata:aliases"}, {"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…The [world] component and dual-system [world]-action models both use predictive representations to connect perception with possible…", "match_reason": "metadata:title"}, {"id": "input_a070092fbe4bbba0a3effe85", "type": "input", "title": "GitHub - RLinf/RPent: RPent: Agentic Infrastructure for the Physical World · GitHub", "path": "vault/inputs/input-input_a070092fbe4bbba0a3effe85.md", "status": "active", "source_ids": ["source_6b52a51e2b4a3be43c97c386"], "snippet": "…Agentic Infrastructure for the Physical [World] · GitHub\n\nInput Episode for `source_6b52a51e2b4a3be43c97c386`. The immutable Source remains authoritative.\n\n# GitHub…", "match_reason": "metadata:title"}, {"id": "input_41c7203faaf98b68b319eebc", "type": "input", "title": "GitHub - InternRobotics/REAL: [ECCV2026] Official open-source repository for REAL——Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation · GitHub", "path": "vault/inputs/input-input_41c7203faaf98b68b319eebc.md", "status": "active", "source_ids": ["source_a5f8ae205338d5f97eea87c7"], "snippet": "…Vision-Driven Embodied Agents for Open-[World] Mobile Manipulation · GitHub\n\nInput Episode for `source_a5f8ae205338d5f97eea87c7`. The immutable Source…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_38cba686373b003398483ab2"}
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
- Extraction：`extraction_d13570dcddb3e3847630b7d4`
- 编译前召回已有对象：7
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_09dc6e910b167ba474c89c38-世界动作模型的激活空间鲁棒性-steering.md
@@ -0,0 +1,20 @@
+---
+id: "concept_09dc6e910b167ba474c89c38"
+type: "concept"
+status: "proposal"
+title: "世界动作模型的激活空间鲁棒性 steering"
+created_at: "2026-07-20T18:05:48+08:00"
+updated_at: "2026-07-20T18:05:48+08:00"
+aliases: ["World-Action Model Activation-Space Robustness Steering", "WA-LQR", "World-Action Linear Quadratic Regulator", "世界动作模型激活引导"]
+tags: []
+domains: ["world-model", "robot-robustness", "mechanistic-interpretability"]
+confidence: "medium"
+source_ids: ["source_38cba686373b003398483ab2"]
+relations: [{"type": "derived_from", "target_id": "source_38cba686373b003398483ab2", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_latent_space_intervention_adaptation", "reason": "两者都在冻结基础策略的潜在表示层实施轻量干预，但一个由人类纠正动作导出输入潜变量，另一个由扰动对比激活和局部控制导出内部 steering。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_38cba686373b003398483ab2"
+reflection_context: {"reflection_ids": ["reflection_f5a4802aeb05942de18022f0"], "importance": "high", "changed_belief": "此前训练后或提示级的鲁棒性改进常被看作统一手段；这里显示能否从激活中得到可迁移干预方向取决于具体架构和扰动。", "surprising": "", "connections": [{"shared_mechanism": "两者都先诊断内部表示中是否存在与目标行为相关的可用结构，再把诊断结果用于干预。", "boundary": "低维可分离只是在所测模型和扰动上的预测信号，不是因果解释或安全保证。", "difference": "表示对齐触觉 grounding 在训练期把未来接触结果监督到中间层；WAM steering 在不微调模型时，于推理期调节已存在的激活方向。"}], "open_questions": ["在新的相机、夹爪和视觉噪声组合上，线性可分性与闭环 steering 效果的相关性是否仍能校准？"]}
+---
+
+# 世界动作模型的激活空间鲁棒性 steering
+
+对世界动作模型在标称与扰动 rollout 的内部激活进行对比，若鲁棒性相关特征在低维子空间中具有可分离结构，可据此构造对比激活方向，并利用局部线性动态在推理时以受惩罚的闭环控制调节激活；该可操控性需要按模型架构和扰动类型分别验证。
```
