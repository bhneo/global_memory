---
id: "proposal_bundle_17177b31b8cc44c17a08"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-20T12:27:36+08:00"
updated_at: "2026-07-20T12:27:37+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_f9128ff3463cfaa7fa41ee7e"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt56-m91-daily-batch-a-20260720"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_9131a419035416778fdfab8d"
input_sha256: "115651988624eed90e76b1b7e3c58cf8d1af4bc2d44a51ea4c59479f66961256"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_f67f822ee20789d74d7b75e3", "target_path": "vault/knowledge/concepts/concept_f67f822ee20789d74d7b75e3-物理失败合成驱动的稠密机器人奖励建模.md", "base_sha256": null, "candidate_sha256": "f071c68b41c6fca1f0111942e6f3929f3420fafdd2827a6ca70f4a6ecbe1dd68", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_17177b31b8cc44c17a08-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_f67f822ee20789d74d7b75e3.md", "working_at": "2026-07-20T12:27:37+08:00"}]
existing_context: [{"id": "claim_play2perfect_sample_efficiency_20260715", "type": "claim", "title": "Play2Perfect 在简化 Fixtured Tight-Insertion 中约 4 小时达到 dense-reward scratch 超过 100 小时才达到的成功率", "path": "vault/memory/claim/claim_play2perfect_sample_efficiency_20260715.md", "status": "working", "source_ids": ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"], "snippet": "# Play2Perfect 在简化插入任务中的训练效率\n\n在额外构造的 `Tight-Insertion (Fixtured)` 简化任务中，物体以易抓取姿态放在 fixture 上。带 10 个 waypoint shaping 的 dense-[reward]…", "match_reason": "metadata:title"}, {"id": "input_a40d415f32bb387e26fabc19", "type": "input", "title": "Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning", "path": "vault/inputs/input-input_a40d415f32bb387e26fabc19.md", "status": "active", "source_ids": ["source_91072aa553af99e6ab97c6cd"], "snippet": "# Simple-to-Complex Structured Demonstrations for Vision-Language-Action [Learning]\n\nInput Episode for `source_91072aa553af99e6ab97c6cd`. The immutable Source…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_f9128ff3463cfaa7fa41ee7e"}
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

- Provider：`codex-gpt56-m91-daily-batch-a-20260720`
- Extraction：`extraction_9131a419035416778fdfab8d`
- 编译前召回已有对象：2
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_f67f822ee20789d74d7b75e3-物理失败合成驱动的稠密机器人奖励建模.md
@@ -0,0 +1,20 @@
+---
+id: "concept_f67f822ee20789d74d7b75e3"
+type: "concept"
+status: "proposal"
+title: "物理失败合成驱动的稠密机器人奖励建模"
+created_at: "2026-07-20T12:27:36+08:00"
+updated_at: "2026-07-20T12:27:36+08:00"
+aliases: ["Failure-synthesis dense reward modeling", "DenseReward", "失败感知稠密奖励"]
+tags: []
+domains: ["embodied-ai", "robot-rl", "reward-modeling", "failure-data"]
+confidence: "high"
+source_ids: ["source_f9128ff3463cfaa7fa41ee7e"]
+relations: [{"type": "derived_from", "target_id": "source_f9128ff3463cfaa7fa41ee7e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-daily-batch-a-20260720", "status": "proposal"}, {"type": "related_to", "target_id": "concept_vla_action_evaluation_distillation", "reason": "二者都把结果知识压缩为轻量评估接口；一个输出逐时刻进度奖励，另一个输出候选动作的长期 Q 值。", "confidence": "medium", "created_by": "codex-gpt56-m91-daily-batch-a-20260720", "status": "proposal"}]
+change_reason: "compile bundle from source_f9128ff3463cfaa7fa41ee7e"
+reflection_context: {"reflection_ids": ["reflection_cb246940931502d077f687f5"], "importance": "high", "changed_belief": "此前容易把稠密奖励建模视为给成功轨迹插值标签；该工作强调，若训练数据没有真实执行中会出现的失败机制，标签再稠密也可能只学到伪进度。", "surprising": "两帧历史优于一帧，而三帧又略差，提示奖励估计既需要时间上下文，也会受到冗余或噪声历史的影响。", "connections": [{"shared_mechanism": "与 VLA 动作评估蒸馏都学习一个轻量评估信号，为原策略的候选动作或后训练提供长期结果信息。", "boundary": "DenseReward 依赖仿真中的阶段标签和定向扰动，论文只证明其所选操作任务上的奖励预测与下游指导效果；合成失败分布仍可能遗漏真机罕见故障。", "difference": "动作评估蒸馏从仿真树搜索回报学习候选动作 Q 值；DenseReward 从视觉历史和语言预测逐时刻进度，并显式训练多类失败轨迹。"}], "open_questions": ["合成失败与真实失败的分布差异应如何检测，并在策略开始利用奖励漏洞前触发人工或真机校准？"]}
+---
+
+# 物理失败合成驱动的稠密机器人奖励建模
+
+通过定向扰动在仿真中生成碰撞、漏抓、掉落与恢复等物理失败轨迹，并用阶段感知逐时刻标签训练视觉语言奖励模型；短时视觉历史用于区分外观相似但进度方向不同的状态。其有效性受合成失败覆盖和奖励校准边界约束。
```
