---
id: "proposal_bundle_4b3f26ed2fd2c96cfe0f"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-08-02T18:21:44+08:00"
updated_at: "2026-08-02T18:21:45+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_9f9972326eb118a8e4bb5623"]
relations: []
proposal_kind: "compile_bundle"
processor: "codex-gpt-5.6-sol-strong-daily-v2"
review_unit: "source_bundle"
compile_disposition: "knowledge_proposed"
source_summary: "arxiv.org"
source_authority: "preprint"
availability_status: "available"
content_quality: "valid"
extraction_quality: "good"
extraction_id: "extraction_ea8246ec6a6dc4c32298a957"
input_sha256: "b4ca82a153732c8fdae606f271f37ecceb2d091c19e221cd1d3c6e21f73311ea"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_61c0ffd089f650a51ec3f00d", "target_path": "vault/knowledge/concepts/concept_61c0ffd089f650a51ec3f00d-上下文匹配的失败动作有界重定向-context-matched-bounded-redirection-of-failure-a.md", "base_sha256": null, "candidate_sha256": "98bde2ccea3a8e882881ca4a9a45dfbec8f7d3a4ab4abf5eb2c9cb8e90e10b39", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_4b3f26ed2fd2c96cfe0f-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_61c0ffd089f650a51ec3f00d.md", "working_at": "2026-08-02T18:21:45+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "concept_e69974f653450465afb2aa3e", "type": "concept", "title": "失败条件化的 VLA 推理时组合转向 / Failure-gated compositional VLA steering", "path": "vault/memory/concept/concept_e69974f653450465afb2aa3e.md", "status": "working", "source_ids": ["source_e504623270d30d733b2cb9e1"], "snippet": "# 失败条件化的 VLA 推理时组合转向 / [Failure]-gated compositional VLA steering\n\n从冻结 VLA 的 action-expert latent 训练轻量离线 RL flow policy…", "match_reason": "metadata:title"}, {"id": "synthesis_c39036fad2cb3b01ea32745c", "type": "synthesis", "title": "Frozen-policy RL interfaces: staged latent training and failure-gated test-time steering", "path": "vault/synthesis/synthesis-synthesis_c39036fad2cb3b01ea32745c.md", "status": "active", "source_ids": ["source_98bb68f21232969a79d77918", "source_e504623270d30d733b2cb9e1"], "snippet": "…staged latent training and [failure]-gated test-time steering\n\n## Emerging patterns\n\n- Post-training around a frozen generative policy…", "match_reason": "metadata:title"}, {"id": "concept_f67f822ee20789d74d7b75e3", "type": "concept", "title": "物理失败合成驱动的稠密机器人奖励建模", "path": "vault/memory/concept/concept_f67f822ee20789d74d7b75e3.md", "status": "working", "source_ids": ["source_f9128ff3463cfaa7fa41ee7e"], "snippet": "# 物理失败合成驱动的稠密机器人奖励建模\n\n通过定向扰动在仿真中生成碰撞、漏抓、掉落与恢复等物理失败轨迹，并用阶段感知逐时刻标签训练视觉语言奖励模型；短时视觉历史用于区分外观相似但进度方向不同的状态。其有效性受合成失败覆盖和奖励校准边界约束。", "match_reason": "metadata:aliases"}, {"id": "synthesis_c7d382870efa4d332c1c447f", "type": "synthesis", "title": "Sparse semantic reasoning above compiled low-latency execution", "path": "vault/synthesis/synthesis-synthesis_c7d382870efa4d332c1c447f.md", "status": "active", "source_ids": ["source_38375a0f6ddc91f3bfde47d3", "source_d0908c8e9c58809dd2665c1e", "source_feaf5bf5a081e27b445c569c"], "snippet": "…measure when semantic novelty or [failure] requires escalation, and keep stable high-rate control outside a generative-language…", "match_reason": "full-text:body"}, {"id": "concept_648a44e346f991eab5956e55", "type": "concept", "title": "不可提升力预算下的语义恢复与快环权限分离", "path": "vault/memory/concept/concept_648a44e346f991eab5956e55.md", "status": "working", "source_ids": ["source_45c4de28acb4ba36642f1594"], "snippet": "# 不可提升力预算下的语义恢复与快环权限分离\n\n接触丰富装配可让慢速语义模块依据对象身份提出每对象力预算，并在失败时依据紧凑力与接触签名从固定恢复菜单中选择动作；实际命令饱和、全局硬上限和力权限必须留在高频控制环，恢复过程不得提高原始预算。该架构仍需测量命令力与接触峰值之间的 overshoot，并以仿真限定、注入故障和代理 baseline 的边界解释结果，不能把硬 clamp 当作真实接触力保证。", "match_reason": "metadata:domains"}, {"id": "reflection_cb246940931502d077f687f5", "type": "reflection", "title": "DenseReward：奖励模型的数据瓶颈是物理失败覆盖与时间信用分配", "path": "vault/reflections/reflection-reflection_cb246940931502d077f687f5.md", "status": "active", "source_ids": ["source_f9128ff3463cfaa7fa41ee7e"], "snippet": "# DenseReward：奖励模型的数据瓶颈是物理失败覆盖与时间信用分配\n\n## Why important\n\nDenseReward 把机器人奖励学习的两个薄弱环节放在同一数据管线中：用定向扰动合成碰撞、漏抓、掉落和恢复等物理失败，再学习带历史帧的逐时刻任务进度奖励。\n\n## What changed\n\n此前容易把稠密奖励建模视为给成功轨迹插值标签；该工作强调，若训练数据没有真实执行中会出现的失败机制，标签再稠密也可能只学到伪进度。\n\n## Surprising\n\n两帧历史优于一帧…", "match_reason": "metadata:domains"}, {"id": "reflection_5eb9ba718b0b143e55d0b020", "type": "reflection", "title": "FORGE-plus：语义恢复可以选动作，但不能拥有力权限", "path": "vault/reflections/reflection-reflection_5eb9ba718b0b143e55d0b020.md", "status": "active", "source_ids": ["source_45c4de28acb4ba36642f1594"], "snippet": "# FORGE-plus：语义恢复可以选动作，但不能拥有力权限\n\n## Why important\n\nFORGE-plus 把对象级力预算、力特征驱动的失败分类、固定恢复菜单与高频控制硬约束分开，显示慢速 LLM 可以参与恢复选择而不成为安全执行器；同时它用接触力 overshoot 暴露了命令上限与物理接触上限之间的差距。\n\n## What…", "match_reason": "metadata:domains"}, {"id": "input_0695c83197b78628a87e9c2b", "type": "input", "title": "[2607.26657] Enfold: Folding World-Generator Computation into Predictive Representations for Efficient Embodied Control", "path": "vault/inputs/input-input_0695c83197b78628a87e9c2b.md", "status": "active", "source_ids": ["source_5c653d6ea053d088d13e6d5c"], "snippet": "…Folding World-Generator Computation [into] Predictive Representations for Efficient Embodied Control\n\nInput Episode for `source_5c653d6ea053d088d13e6d5c`. The immutable…", "match_reason": "metadata:title"}, {"id": "reflection_bd1bc1b00ef5304ee9d29e9c", "type": "reflection", "title": "FM-VLA：力历史将接触进度压缩为记忆 token / force history compresses contact progress into memory tokens", "path": "vault/reflections/reflection-reflection_bd1bc1b00ef5304ee9d29e9c.md", "status": "active", "source_ids": ["source_1ee2c3fae53a9d05689cd143"], "snippet": "# FM-VLA：力历史将接触进度压缩为记忆 token / force history compresses contact progress [into] memory tokens\n\n## Why important\n\nFM-VLA 以预训练 VAE…", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_9f9972326eb118a8e4bb5623"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "b03e5f1947ccaed1e1b3adc09c3ecb192fee63304f21a4aad4f0b8380edd730f"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt-5.6-sol-strong-daily-v2`
- Extraction：`extraction_ea8246ec6a6dc4c32298a957`
- 编译前召回已有对象：11
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_61c0ffd089f650a51ec3f00d-上下文匹配的失败动作有界重定向-context-matched-bounded-redirection-of-failure-a.md
@@ -0,0 +1,20 @@
+---
+id: "concept_61c0ffd089f650a51ec3f00d"
+type: "concept"
+status: "proposal"
+title: "上下文匹配的失败动作有界重定向 / Context-matched bounded redirection of failure actions"
+created_at: "2026-08-02T18:21:44+08:00"
+updated_at: "2026-08-02T18:21:44+08:00"
+aliases: ["RedFlow", "context-aware corrective matching", "adaptive redirection objective", "结构化失败数据复用"]
+tags: []
+domains: ["robotics", "vla", "offline-reinforcement-learning", "flow-policy"]
+confidence: "high"
+source_ids: ["source_9f9972326eb118a8e4bb5623"]
+relations: [{"type": "derived_from", "target_id": "source_9f9972326eb118a8e4bb5623", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_6a559a41722de87986c350e7", "reason": "两者都保留 flow 先验并限制外部反馈的干预范围；RedFlow 在动作速度场中使用上下文匹配的离线成败样本，RLMM-Flow 用 critic 在潜变量中分阶段转向整段轨迹。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
+change_reason: "compile bundle from source_9f9972326eb118a8e4bb5623"
+reflection_context: {"reflection_ids": ["reflection_4602753df83a62d4799d8e91"], "importance": "high", "changed_belief": "我原先更倾向把失败轨迹视为统一的反偏好信号；该工作把它拆成可被同上下文正样本重定向的失败动作，以及只能安全压制的无匹配失败动作。", "surprising": "修正目标不是人工标注的唯一动作，而是同进度、近似本体上下文中的正样本动作重心；这把多解动作空间中的纠正保持为集合内插值。", "connections": [{"shared_mechanism": "RedFlow 与既有 concept_6a559a41722de87986c350e7 都保留 flow 生成先验，并把外部质量或价值反馈限制在比全模型更新更窄的后训练接口。", "boundary": "该连接只适用于基础 flow policy 已覆盖目标行为邻域的条件；两项工作都不能从先验支持域外凭空恢复动作能力。", "difference": "RedFlow 在动作速度场上用离线成败轨迹与 progress-proprioception 上下文匹配纠偏，RLMM-Flow 在潜变量上用 critic 分阶段转向整段轨迹。"}], "open_questions": ["如何检测 progress-proprioception 上的近邻是否已经越出正样本支持域，并在此时自动退化为仅压制而非重定向？"]}
+---
+
+# 上下文匹配的失败动作有界重定向 / Context-matched bounded redirection of failure actions
+
+在 mixed-quality 离线 flow-policy 后训练中，先用任务进度把轨迹切到相近阶段，再用本体状态聚类近似局部决策上下文。对能找到同上下文正样本的失败动作，以正动作的加权重心作为集合内纠正端点并重定向 flow 速度；对没有可靠正支持的失败动作只施加有界抑制；同时保留对高质量动作的吸引。这样可分别表达质量保持、失败抑制和可支持的纠正，但其有效性依赖进度奖励、聚类和正样本覆盖；匹配错误会产生伪纠正，支持域外失败不能由该机制恢复正确动作。
```
