---
id: "proposal_bundle_638d31071d5f46673df0"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-21T17:41:40+08:00"
updated_at: "2026-07-21T17:41:41+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_5e14510061220db7f2344913"]
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
extraction_id: "extraction_abe9d0b397429a158beb8674"
input_sha256: "f51e46837fe735938289d8bf326aef2cccd4ab59f152b5e39002b622c7ec76b1"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_language_corrective_memory_data_flywheel", "target_path": "vault/knowledge/concepts/concept_language_corrective_memory_data_flywheel-语言纠错记忆驱动的机器人数据飞轮.md", "base_sha256": null, "candidate_sha256": "5bef2ee70451068e9c0561c6d30b55199272c0706925a6738d125913a8d500a1", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_638d31071d5f46673df0-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_language_corrective_memory_data_flywheel.md", "working_at": "2026-07-21T17:41:41+08:00"}]
existing_context: [{"id": "concept_21a37fbe65868f6e97a68a20", "type": "concept", "title": "机器人坐标系稠密 Pointmap 观察接口", "path": "vault/memory/concept/concept_21a37fbe65868f6e97a68a20.md", "status": "working", "source_ids": ["source_b64b4a539b8c17d0cfe662ba"], "snippet": "# 机器人坐标系稠密 Pointmap 观察接口\n\n把 RGB-D 像素对应的三维点预先转换到机器人动作所用坐标系，并保留图像 H×W 网格供预训练 VLA 视觉通路编码。该接口减少相机视角到动作坐标的学习负担，但依赖深度和相机标定质量。", "match_reason": "metadata:aliases"}, {"id": "concept_real_robot_deployment_iteration_loop", "type": "concept", "title": "真机部署评估迭代闭环", "path": "vault/memory/concept/concept_real_robot_deployment_iteration_loop.md", "status": "working", "source_ids": ["source_3e845794fed758f1dda5248e"], "snippet": "# 真机部署评估迭代闭环\n\n用模型无关的客户端把遥操作采集、动作块调度与平滑、实机执行、里程碑评分、视频及三路动作流日志连成可检查闭环，使每次物理评估同时产生可回放、可归因并可反馈训练的数据。", "match_reason": "metadata:aliases"}, {"id": "reflection_7b23a8a7adc7b353d26fbc30", "type": "reflection", "title": "Robot-centric Pointmap：先消除观察与动作坐标错配，再让 VLA 学控制", "path": "vault/reflections/reflection-reflection_7b23a8a7adc7b353d26fbc30.md", "status": "active", "source_ids": ["source_b64b4a539b8c17d0cfe662ba"], "snippet": "# [Robot]-centric Pointmap：先消除观察与动作坐标错配，再让 VLA 学控制\n\n## Why important\n\n[Robot]-centric pointmap 把每个 RGB-D 像素转换为机器人基座或末端中心坐标，同时保留 H…", "match_reason": "metadata:title"}, {"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…Qwen-[Robot] separates navigation, manipulation, and world prediction behind language-first interfaces\n\n## Why important\n\nThe article presents a…", "match_reason": "metadata:title"}, {"id": "concept_validation_gated_skill_optimization", "type": "concept", "title": "验证门控的技能文本优化", "path": "vault/memory/concept/concept_validation_gated_skill_optimization.md", "status": "working", "source_ids": ["source_54c9a7922f348a245d17efaf"], "snippet": "# 验证门控的技能文本优化\n\n把 Agent 技能文档视作可训练的外部状态：根据执行轨迹提出有界增删改，并仅在独立验证集指标严格改善时接受新版本，同时保留拒绝编辑作为后续负反馈。", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_5e14510061220db7f2344913"}
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
- Extraction：`extraction_abe9d0b397429a158beb8674`
- 编译前召回已有对象：5
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_language_corrective_memory_data_flywheel-语言纠错记忆驱动的机器人数据飞轮.md
@@ -0,0 +1,20 @@
+---
+id: "concept_language_corrective_memory_data_flywheel"
+type: "concept"
+status: "proposal"
+title: "语言纠错记忆驱动的机器人数据飞轮"
+created_at: "2026-07-21T17:41:40+08:00"
+updated_at: "2026-07-21T17:41:40+08:00"
+aliases: ["Language-Corrective Memory Data Flywheel", "Zero2Skill", "Corrective Memory", "语言纠错数据飞轮"]
+tags: []
+domains: ["embodied-ai", "robot-data", "agent-memory"]
+confidence: "medium"
+source_ids: ["source_5e14510061220db7f2344913"]
+relations: [{"type": "derived_from", "target_id": "source_5e14510061220db7f2344913", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}, {"type": "applied_in", "target_id": "concept_real_robot_deployment_iteration_loop", "reason": "它把部署闭环中的失败归因转化为持久语言修正、自动重试和训练数据认证。", "confidence": "high", "created_by": "agent-semantic-daily-gpt56sol-readmission-v1", "status": "proposal"}]
+change_reason: "compile bundle from source_5e14510061220db7f2344913"
+reflection_context: {"reflection_ids": ["reflection_6628e0dee92b8a90b106317d"], "importance": "high", "changed_belief": "人类在环的主要价值不一定是持续遥操作，而可以是把重复失败压缩为可复用语言约束；但验证器误判会直接污染数据集。", "surprising": "作者在所测桌面任务中报告无需遥操作即可达到 100% episode collection success，并使下游策略达到与全遥操作数据相当的 80%；范围受工具、相机和任务设置限制。", "connections": [{"shared_mechanism": "两者都把执行结果反馈到下一轮数据或策略选择。", "boundary": "语言纠错和视觉验证仍不是力学安全证明，也不保证跨任务迁移。", "difference": "真机部署迭代闭环强调可回放和归因；Zero2Skill 进一步把人类纠错持久化并驱动自主重试与数据认证。"}], "open_questions": ["如何校准视觉验证器的假阳性，使采集成功不被错误标签夸大？"]}
+---
+
+# 语言纠错记忆驱动的机器人数据飞轮
+
+Zero2Skill 让自主 Agent 采集演示，在失败复现时接收简短人类语言修正，将其持久化为 Corrective Memory，并用视觉验证和轨迹认证决定重试与入库；随后用合格数据微调策略并部署。该闭环可降低持续遥操作负担，但其数据质量取决于工具执行、视觉验证器和任务分布，采集成功率不能替代下游策略评测。
```
