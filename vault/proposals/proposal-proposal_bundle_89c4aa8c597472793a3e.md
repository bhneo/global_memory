---
id: "proposal_bundle_89c4aa8c597472793a3e"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-08-02T18:56:47+08:00"
updated_at: "2026-08-02T18:56:48+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_1fa826244c5f3d4ea7f41541"]
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
extraction_id: "extraction_a0ee8dd73d5cc68190d8e52e"
input_sha256: "e4daba797f90e042fbbbe7448b9660b242e74fce84f0940aabf7b283ea2cef7f"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_edcbaa2945d5c05f88c5290b", "target_path": "vault/knowledge/concepts/concept_edcbaa2945d5c05f88c5290b-阶段歧义驱动的扩散控制频率切换-phase-ambiguity-driven-diffusion-control-frequen.md", "base_sha256": null, "candidate_sha256": "c397af42d07551a335c656a0dd198534ab0b9bea92799297b2a0ac156031f58f", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_89c4aa8c597472793a3e-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_edcbaa2945d5c05f88c5290b.md", "working_at": "2026-08-02T18:56:48+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "input_dd10d4b6286ecf52c06c0361", "type": "input", "title": "TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation", "path": "vault/inputs/input-input_dd10d4b6286ecf52c06c0361.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "…A Predictive and [Reactive] Tactile Foundation Model for Dexterous Manipulation\n\nInput Episode for `source_283911da72edc403d1b823fb`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "concept_2ce226e08d585158c1dfbb18", "type": "concept", "title": "接触反馈应区分短时反应、事件记忆与概率后验", "path": "vault/memory/concept/concept_2ce226e08d585158c1dfbb18.md", "status": "working", "source_ids": ["source_4e06d1b1cdcd0d07eff47909", "source_1ee2c3fae53a9d05689cd143"], "snippet": "# 保留视觉语言先验的块内反应式力注入\n\n对预训练视觉语言动作策略，可在保留慢速视觉语言前缀的同时，以因果近期六维末端力记忆驱动并行反应动作分支，并用零初始化残差使后训练前的输出与基线一致；在线纠正数据用于覆盖当前策略遇到的接触失败状态，但效果受传感延迟、任务接触动力学和在线数据质量限制。\n\n## 新增来源材料\n\n- `source_1ee2c3fae53a9d05689cd143`：预训练 VLA 的接触反馈接口应区分短时反应、事件记忆与不确定性估计。LIFT 用近期六维力在动作块内做因果反应；FM…", "match_reason": "metadata:aliases"}, {"id": "input_9f6dd11d13abf277fa0e162d", "type": "input", "title": "LIFT: Never Too Late for Force", "path": "vault/inputs/input-input_9f6dd11d13abf277fa0e162d.md", "status": "active", "source_ids": ["source_4e06d1b1cdcd0d07eff47909"], "snippet": "…Never Too Late for Force Accelerating VLA Post-Training with [Reactive] Force Injection Yi Wang 12* , Wendi Chen…", "match_reason": "full-text:body"}, {"id": "concept_8a7645759329c1444d94a4cf", "type": "concept", "title": "同状态相对价值驱动的扩散导航后训练 / Same-state relative-value diffusion navigation post-training", "path": "vault/memory/concept/concept_8a7645759329c1444d94a4cf.md", "status": "working", "source_ids": ["source_bdb17eb4583ec8af52f28dfb"], "snippet": "# 同状态相对价值驱动的扩散导航后训练 / Same-state relative-value [diffusion] navigation post-training\n\n为在在线 RL 中稳定改进连续扩散导航策略，先从当前策略构造保留动作流形的带目标候选，以及沿带目标预测相对当前动作做有符号外推的无目标候选；再在同一状态的候选组内归一化 Q 分数、强化相对高价值候选…", "match_reason": "metadata:title"}, {"id": "concept_2c69b09323afa79344401cd8", "type": "concept", "title": "延迟自适应的三段 flow 动作调度 / Latency-adaptive three-region flow action schedule", "path": "vault/memory/concept/concept_2c69b09323afa79344401cd8.md", "status": "working", "source_ids": ["source_9ddfb0f3d50b606bd13e17e2"], "snippet": "# 延迟自适应的三段 flow 动作调度 / Latency-adaptive three-region flow action schedule\n\n为实测推理延迟 d 构造 per-position noise schedule：前…", "match_reason": "metadata:aliases"}, {"id": "concept_3d739e54fe54c8a5205d2301", "type": "concept", "title": "多坐标系同步动作去噪", "path": "vault/memory/concept/concept_3d739e54fe54c8a5205d2301.md", "status": "working", "source_ids": ["source_4df1017326dd7cc4786f4218"], "snippet": "# 多坐标系同步动作去噪\n\n在一个 canonical [diffusion] state 上，把同一噪声动作转换到多个任务相关坐标系，由 frame-specialized denoisers 分别预测，再变换回统一坐标系融合。它利用不同任务阶段在夹爪、基座或相对轨迹 frame 中更紧凑的动作分布，但依赖候选…", "match_reason": "metadata:domains"}, {"id": "reflection_a4abd223b36c137fb9bd6ae4", "type": "reflection", "title": "Mixture of Frames：动作分布复杂度部分来自坐标系选择", "path": "vault/reflections/reflection-reflection_a4abd223b36c137fb9bd6ae4.md", "status": "active", "source_ids": ["source_4df1017326dd7cc4786f4218"], "snippet": "…并把 frame transform 不确定性传播进扩散去噪与执行风险？\n\n## Possible mechanisms\n\n- 共享 canonical [diffusion] state 保持专家同步，各专家在本地 frame 中建模更紧凑的动作分布，路由器按阶段融合其预测。\n\n## Future directions\n\n- 比较人工…", "match_reason": "metadata:domains"}, {"id": "reflection_7991ec84469c68e4271878a4", "type": "reflection", "title": "X-NavDP：用同状态相对价值稳定扩散导航后训练", "path": "vault/reflections/reflection-reflection_7991ec84469c68e4271878a4.md", "status": "active", "source_ids": ["source_bdb17eb4583ec8af52f28dfb"], "snippet": "…X-NavDP 在线更新 [diffusion] score matching，RLMM-Flow 冻结 flow decoder 并由 latent actor-critic 转向初始噪声。\n\n## Conflicts\n\n- 组内相对…", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_1fa826244c5f3d4ea7f41541"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "657c678864cc62b59756149a9ec6bfc0bba843ef086c9aebe7435a73f19fcf3f"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt-5.6-sol-strong-daily-v2`
- Extraction：`extraction_a0ee8dd73d5cc68190d8e52e`
- 编译前召回已有对象：10
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_edcbaa2945d5c05f88c5290b-阶段歧义驱动的扩散控制频率切换-phase-ambiguity-driven-diffusion-control-frequen.md
@@ -0,0 +1,20 @@
+---
+id: "concept_edcbaa2945d5c05f88c5290b"
+type: "concept"
+status: "proposal"
+title: "阶段歧义驱动的扩散控制频率切换 / Phase-ambiguity-driven diffusion control-frequency switching"
+created_at: "2026-08-02T18:56:47+08:00"
+updated_at: "2026-08-02T18:56:47+08:00"
+aliases: ["FA-RDP", "frequency-adaptive residual diffusion policy", "ambiguity-conditioned frequency switching", "歧义条件的多频扩散控制"]
+tags: []
+domains: ["robotics", "diffusion-policy", "force-control", "multi-rate-control"]
+confidence: "high"
+source_ids: ["source_1fa826244c5f3d4ea7f41541"]
+relations: [{"type": "derived_from", "target_id": "source_1fa826244c5f3d4ea7f41541", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_dynamic_execution_horizon", "reason": "两者都按阶段调节开环承诺；动态执行时域改变已生成动作块的执行前缀，FA-RDP 联动控制频率、预测长度和生成器。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_multitimescale_tactile_world_model", "reason": "两者都分离慢速语义与快速接触反馈；FA-RDP 以视觉歧义门切换视觉—力扩散采样频率，而既有节点以触觉子目标和残差层组织闭环。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_34269bf138ea36a302aaa11f", "reason": "两者都显式利用接触阶段改变生成式策略执行；既有节点在候选间做几何进度选择，FA-RDP 在低频多步与高频单步生成间切换。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
+change_reason: "compile bundle from source_1fa826244c5f3d4ea7f41541"
+reflection_context: {"reflection_ids": ["reflection_1ca77990ff946c0288b7704c"], "importance": "high", "changed_belief": "我原先把高频控制主要理解为更频繁地重规划；该工作表明，频率切换还必须同步改变预测序列长度和采样器，否则高频多步扩散的计算预算会失控。", "surprising": "频率门由低频视觉 token 学习，而高频阶段每步刷新力输入并复用缓存的慢速上下文；快速反馈并不要求重算全部视觉语义。", "connections": [{"shared_mechanism": "FA-RDP 与 concept_dynamic_execution_horizon 都按任务阶段改变开环承诺长度，以平衡吞吐和反馈反应。", "boundary": "连接限于执行调度；两者都不保证基础策略支持域外的恢复或力安全。", "difference": "动态执行时域改变一个已生成动作块执行多少步，FA-RDP 同时切换 10/30 Hz、16/48 步预测和多步/单步生成器。"}, {"shared_mechanism": "FA-RDP 与 concept_multitimescale_tactile_world_model 都把慢速语义上下文和快速接触反馈分层。", "boundary": "FA-RDP 使用视觉与六维力，不能直接外推到触觉图像、长时任务分解或跨硬件触觉语义。", "difference": "既有概念以触觉子目标和残差控制组织多时间尺度，FA-RDP 以阶段歧义门切换扩散采样频率。"}], "open_questions": ["当视觉歧义在接触后重新出现，或力信号在接触前已经关键时，二阶段门应如何校准和回退？"]}
+---
+
+# 阶段歧义驱动的扩散控制频率切换 / Phase-ambiguity-driven diffusion control-frequency switching
+
+对接触操作中的扩散策略，可让任务歧义而非固定时钟决定控制模式：共享视觉—力 Transformer 以频率自适应位置编码把 10 Hz 的 16 步序列与 30 Hz 的 48 步序列对齐到同一 1.6 秒物理时域。接触前保留低频多步扩散的多模态规划；视觉门判断歧义消退后，切换到高频单步蒸馏并每步刷新力输入，同时缓存慢速视觉上下文以控制计算量。该结构不同于只改变动作块执行前缀，也不同于只在固定策略上叠加高频力补偿；其边界是门依赖视觉阶段线索并假设歧义通常随接触下降，证据目前限于单任务、单机器人和三项视觉—力任务。
```
