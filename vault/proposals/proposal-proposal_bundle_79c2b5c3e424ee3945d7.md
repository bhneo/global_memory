---
id: "proposal_bundle_79c2b5c3e424ee3945d7"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T18:05:28+08:00"
updated_at: "2026-07-20T18:05:29+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_61152ca8210ad3913764a291"]
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
extraction_id: "extraction_a932cf0e42094571960bb142"
input_sha256: "ea707ec92534a51e0a8de77e5ba52d9ad71f5360f721289e60779f97353581b3"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_d5965e0770273320ea6b28f2", "target_path": "vault/knowledge/concepts/concept_d5965e0770273320ea6b28f2-主动真机因子评测.md", "base_sha256": null, "candidate_sha256": "5de18c8101052363c252b452ab6dae3bc066f77a33e4e2cfe4674081538789d7", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_79c2b5c3e424ee3945d7-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_d5965e0770273320ea6b28f2.md", "working_at": "2026-07-20T18:05:29+08:00"}]
existing_context: [{"id": "claim_play2perfect_realworld_tight_insertion_20260715", "type": "claim", "title": "Play2Perfect 仿真微调策略可零样本迁移到真实世界紧配合插入，0.5 mm 间隙成功率 6/10", "path": "vault/memory/claim/claim_play2perfect_realworld_tight_insertion_20260715.md", "status": "working", "source_ids": ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"], "snippet": "# Play2Perfect 的真实世界紧配合插入结果\n\n论文将完全在仿真中微调的 Play2Perfect 部署到真实 Sharpa 手与 KUKA iiwa 14 系统，使用 FoundationPose 跟踪物体，并且没有进行 [real-world] finetuning…", "match_reason": "full-text:body"}, {"id": "concept_real_robot_deployment_iteration_loop", "type": "concept", "title": "真机部署评估迭代闭环", "path": "vault/memory/concept/concept_real_robot_deployment_iteration_loop.md", "status": "working", "source_ids": ["source_3e845794fed758f1dda5248e"], "snippet": "# 真机部署评估迭代闭环\n\n用模型无关的客户端把遥操作采集、动作块调度与平滑、实机执行、里程碑评分、视频及三路动作流日志连成可检查闭环，使每次物理评估同时产生可回放、可归因并可反馈训练的数据。", "match_reason": "metadata:aliases"}, {"id": "concept_vla_action_evaluation_distillation", "type": "concept", "title": "VLA 动作评估蒸馏", "path": "vault/memory/concept/concept_vla_action_evaluation_distillation.md", "status": "working", "source_ids": ["source_ff90ad99bd47043e812cce9e"], "snippet": "# VLA 动作评估蒸馏\n\n保持预训练 VLA 动作生成器冻结，通过仿真树搜索收集候选轨迹及回报，再把长期后果知识蒸馏为轻量 Q 值评估器，在部署时从多个动作候选中选择预期结果更好的一个。", "match_reason": "metadata:aliases"}, {"id": "claim_wechat_embodied_eval_bottleneck_20260715", "type": "claim", "title": "该文称具身 VLA 迭代速度常被真机评估流程而非训练本身卡住", "path": "vault/memory/claim/claim_wechat_embodied_eval_bottleneck_20260715.md", "status": "working", "source_ids": ["source_2d4f3a7d3525782c8ff503ee"], "snippet": "# 评估瓶颈\n\n真机评测排队与人工摆场使迭代受评估而非训练限制。", "match_reason": "metadata:tags"}, {"id": "concept_validation_gated_skill_optimization", "type": "concept", "title": "验证门控的技能文本优化", "path": "vault/memory/concept/concept_validation_gated_skill_optimization.md", "status": "working", "source_ids": ["source_54c9a7922f348a245d17efaf"], "snippet": "# 验证门控的技能文本优化\n\n把 Agent 技能文档视作可训练的外部状态：根据执行轨迹提出有界增删改，并仅在独立验证集指标严格改善时接受新版本，同时保留拒绝编辑作为后续负反馈。", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_61152ca8210ad3913764a291"}
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
- Extraction：`extraction_a932cf0e42094571960bb142`
- 编译前召回已有对象：5
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_d5965e0770273320ea6b28f2-主动真机因子评测.md
@@ -0,0 +1,20 @@
+---
+id: "concept_d5965e0770273320ea6b28f2"
+type: "concept"
+status: "proposal"
+title: "主动真机因子评测"
+created_at: "2026-07-20T18:05:28+08:00"
+updated_at: "2026-07-20T18:05:28+08:00"
+aliases: ["Active Real-World Factor-Based Evaluation", "Active Testing for Generalist Robot Policies", "主动真机因素评测"]
+tags: []
+domains: ["embodied-ai", "robot-evaluation", "active-learning"]
+confidence: "medium"
+source_ids: ["source_61152ca8210ad3913764a291"]
+relations: [{"type": "derived_from", "target_id": "source_61152ca8210ad3913764a291", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "两者都面向真机部署评估，但前者选择信息量最大的条件，后者保证每次执行可回放和可归因。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_61152ca8210ad3913764a291"
+reflection_context: {"reflection_ids": ["reflection_a7089c995e52da14c2ce2609"], "importance": "high", "changed_belief": "此前真机评测闭环强调可回放和归因；这里补充了试验选择本身也应由不确定性驱动，不能把少量便利条件下的成功率视为部署就绪度。", "surprising": "在三个任务和三类因子的实机研究中，作者报告主动选择通常比随机测试少用 20–40% 的试验；该结果只支持其评测设计空间和代理模型设置，不构成对所有机器人任务的保证。", "connections": [{"shared_mechanism": "两者都把真机 rollout 组织为可用于下一轮决策的结构化反馈。", "boundary": "连接只涉及评测闭环与试验预算分配，不把记录完整性等同于统计有效性。", "difference": "真机部署评估迭代闭环侧重日志、回放和训练反馈；该论文侧重由概率代理模型选择下一组因子配置。"}], "open_questions": ["面对相关的相机、物体和初始状态因素时，代理模型的不确定性校准如何在不同机器人和任务之间验证？"]}
+---
+
+# 主动真机因子评测
+
+把机器人策略在对象位姿、相机视角和初始状态等结构化任务因子组合上的性能视为未知函数，用带不确定性估计的概率代理模型和信息增益准则依次选择真机试验，以在有限预算下估计性能分布并定位易失败区域。
```
