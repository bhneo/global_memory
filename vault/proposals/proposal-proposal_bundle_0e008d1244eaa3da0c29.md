---
id: "proposal_bundle_0e008d1244eaa3da0c29"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-21T17:41:51+08:00"
updated_at: "2026-07-21T17:41:52+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_79475aef7849b08664b51a4e"]
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
extraction_id: "extraction_0910d8df1547c174208b8eba"
input_sha256: "6e3cbcbc0ab4db0c20e693c905c9ff4e7f7afe726b15f8fb6dc3a6d7415e4ca0"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_test_time_fast_weight_robot_memory", "target_path": "vault/knowledge/concepts/concept_test_time_fast_weight_robot_memory-机器人策略的测试时快速权重记忆.md", "base_sha256": null, "candidate_sha256": "0d58a76fa115821d743ca710a4c06dbad4cec0fe79a80619a20b8562ccd913ec", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_0e008d1244eaa3da0c29-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_test_time_fast_weight_robot_memory.md", "working_at": "2026-07-21T17:41:52+08:00"}]
existing_context: [{"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…Qwen-[Robot] separates navigation, manipulation, and world prediction behind language-first interfaces\n\n## Why important\n\nThe article presents a…", "match_reason": "metadata:title"}, {"id": "concept_21a37fbe65868f6e97a68a20", "type": "concept", "title": "机器人坐标系稠密 Pointmap 观察接口", "path": "vault/memory/concept/concept_21a37fbe65868f6e97a68a20.md", "status": "working", "source_ids": ["source_b64b4a539b8c17d0cfe662ba"], "snippet": "# 机器人坐标系稠密 Pointmap 观察接口\n\n把 RGB-D 像素对应的三维点预先转换到机器人动作所用坐标系，并保留图像 H×W 网格供预训练 VLA 视觉通路编码。该接口减少相机视角到动作坐标的学习负担，但依赖深度和相机标定质量。", "match_reason": "metadata:aliases"}, {"id": "concept_real_robot_deployment_iteration_loop", "type": "concept", "title": "真机部署评估迭代闭环", "path": "vault/memory/concept/concept_real_robot_deployment_iteration_loop.md", "status": "working", "source_ids": ["source_3e845794fed758f1dda5248e"], "snippet": "# 真机部署评估迭代闭环\n\n用模型无关的客户端把遥操作采集、动作块调度与平滑、实机执行、里程碑评分、视频及三路动作流日志连成可检查闭环，使每次物理评估同时产生可回放、可归因并可反馈训练的数据。", "match_reason": "metadata:aliases"}, {"id": "reflection_7b23a8a7adc7b353d26fbc30", "type": "reflection", "title": "Robot-centric Pointmap：先消除观察与动作坐标错配，再让 VLA 学控制", "path": "vault/reflections/reflection-reflection_7b23a8a7adc7b353d26fbc30.md", "status": "active", "source_ids": ["source_b64b4a539b8c17d0cfe662ba"], "snippet": "# [Robot]-centric Pointmap：先消除观察与动作坐标错配，再让 VLA 学控制\n\n## Why important\n\n[Robot]-centric pointmap 把每个 RGB-D 像素转换为机器人基座或末端中心坐标，同时保留 H…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_79475aef7849b08664b51a4e"}
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
- Extraction：`extraction_0910d8df1547c174208b8eba`
- 编译前召回已有对象：4
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_test_time_fast_weight_robot_memory-机器人策略的测试时快速权重记忆.md
@@ -0,0 +1,20 @@
+---
+id: "concept_test_time_fast_weight_robot_memory"
+type: "concept"
+status: "proposal"
+title: "机器人策略的测试时快速权重记忆"
+created_at: "2026-07-21T17:41:51+08:00"
+updated_at: "2026-07-21T17:41:51+08:00"
+aliases: ["Test-Time Fast-Weight Memory for Robot Policies", "RoboTTT", "TTT Robot Policy", "测试时训练机器人策略"]
+tags: []
+domains: ["embodied-ai", "test-time-training", "long-horizon-manipulation"]
+confidence: "medium"
+source_ids: ["source_79475aef7849b08664b51a4e"]
+relations: [{"type": "derived_from", "target_id": "source_79475aef7849b08664b51a4e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}, {"type": "related_to", "target_id": "concept_native_action_aligned_vla_memory", "reason": "两者分别以快速权重和显式原生 token 承载长时历史，形成可比较的记忆接口。", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_79475aef7849b08664b51a4e"
+reflection_context: {"reflection_ids": ["reflection_245f74ef295bd04767608b26"], "importance": "high", "changed_belief": "长上下文能力既可通过显式记忆 token 实现，也可通过参数化快速状态实现；两者在可解释性、遗忘和计算成本上有不同风险。", "surprising": "在三项双臂装配任务中作者报告平均完成分 79%，高于单步 GR00T N1.7 的 42% 和 GDN 的 56%；训练使用 16 张 GB200，长上下文收益伴随显著训练成本。", "connections": [{"shared_mechanism": "都保留分钟级历史以改进后续动作。", "boundary": "fast-weight 适应不等于持久跨会话记忆，也不自动保证纠正方向安全。", "difference": "NativeMEM 显式保存动作对齐视觉 token；RoboTTT 通过测试时梯度更新把上下文折叠进快速权重。"}], "open_questions": ["fast weights 遇到错误动作、自生成偏差或任务切换时如何检测并回滚？"]}
+---
+
+# 机器人策略的测试时快速权重记忆
+
+RoboTTT 在预训练 GR00T N1.7 的 DiT 层加入可在序列中更新的 TTT fast-weight 模块，通过长序列 flow-matching 和纠正数据训练，使每轮推理将新上下文写入快速权重并传递到下一轮。它把分钟级历史压入参数化在线状态，但需要额外训练计算，并面临错误历史污染、遗忘、回滚和任务切换边界。
```
