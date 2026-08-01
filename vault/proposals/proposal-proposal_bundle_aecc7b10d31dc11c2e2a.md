---
id: "proposal_bundle_aecc7b10d31dc11c2e2a"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-08-01T18:23:04+08:00"
updated_at: "2026-08-01T18:23:05+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_9ddfb0f3d50b606bd13e17e2"]
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
extraction_id: "extraction_dae950e373fdf450fcbd8f2b"
input_sha256: "cad352444bb5990cac9f8ccd05c5582189745448a987ed41a518e5ca1deebf4c"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_2c69b09323afa79344401cd8", "target_path": "vault/knowledge/concepts/concept_2c69b09323afa79344401cd8-延迟自适应的三段-flow-动作调度-latency-adaptive-three-region-flow-action-sch.md", "base_sha256": null, "candidate_sha256": "c03d53c62117712e7a5c25f95c7513945ef2c2957c5da295ae8eff7a08a596a3", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_aecc7b10d31dc11c2e2a-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_2c69b09323afa79344401cd8.md", "working_at": "2026-08-01T18:23:05+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "input_dd10d4b6286ecf52c06c0361", "type": "input", "title": "TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation", "path": "vault/inputs/input-input_dd10d4b6286ecf52c06c0361.md", "status": "active", "source_ids": ["source_283911da72edc403d1b823fb"], "snippet": "…A Predictive and [Reactive] Tactile Foundation Model for Dexterous Manipulation\n\nInput Episode for `source_283911da72edc403d1b823fb`. The immutable Source…", "match_reason": "metadata:title"}, {"id": "concept_2ce226e08d585158c1dfbb18", "type": "concept", "title": "接触反馈应区分短时反应、事件记忆与概率后验", "path": "vault/memory/concept/concept_2ce226e08d585158c1dfbb18.md", "status": "working", "source_ids": ["source_4e06d1b1cdcd0d07eff47909", "source_1ee2c3fae53a9d05689cd143"], "snippet": "# 保留视觉语言先验的块内反应式力注入\n\n对预训练视觉语言动作策略，可在保留慢速视觉语言前缀的同时，以因果近期六维末端力记忆驱动并行反应动作分支，并用零初始化残差使后训练前的输出与基线一致；在线纠正数据用于覆盖当前策略遇到的接触失败状态，但效果受传感延迟、任务接触动力学和在线数据质量限制。\n\n## 新增来源材料\n\n- `source_1ee2c3fae53a9d05689cd143`：预训练 VLA 的接触反馈接口应区分短时反应、事件记忆与不确定性估计。LIFT 用近期六维力在动作块内做因果反应；FM…", "match_reason": "metadata:aliases"}, {"id": "input_9f6dd11d13abf277fa0e162d", "type": "input", "title": "LIFT: Never Too Late for Force", "path": "vault/inputs/input-input_9f6dd11d13abf277fa0e162d.md", "status": "active", "source_ids": ["source_4e06d1b1cdcd0d07eff47909"], "snippet": "…Never Too Late for Force Accelerating VLA Post-Training with [Reactive] Force Injection Yi Wang 12* , Wendi Chen…", "match_reason": "full-text:body"}, {"id": "concept_a858f8d191d3afdd69418471", "type": "concept", "title": "陈旧性对齐与上下文分区共同约束异步快慢控制接口", "path": "vault/memory/concept/concept_a858f8d191d3afdd69418471.md", "status": "working", "source_ids": ["source_d4762e0cf2330ab6ea00a521", "source_e67cd99ac31c7017d6f7f7c7"], "snippet": "# 陈旧性对齐的异步慢上下文—快控制接口\n\n在需要高频闭环控制的 VLA 系统中，可让冻结的慢速主干低频增量维护逐层上下文缓存，并让轻量动作专家在每个控制 tick 同时读取该缓存、当前传感与自身近期状态；训练时随机截断专家可见的慢速前缀，使其覆盖部署时的缓存陈旧性。该设计要求缓存更新与完整前向近似等价、慢分支不依赖快分支 token、陈旧窗口有界，并不能由更高路线完成率推断道路安全或长时程风险处理已经改善。\n\n## 新增来源材料…", "match_reason": "metadata:domains"}, {"id": "reflection_743b2d2d30d2f822bf2bfb9f", "type": "reflection", "title": "FastSlow-LMDrive：实时性要在训练时显式纳入陈旧上下文接口", "path": "vault/reflections/reflection-reflection_743b2d2d30d2f822bf2bfb9f.md", "status": "active", "source_ids": ["source_d4762e0cf2330ab6ea00a521"], "snippet": "# FastSlow-LMDrive：实时性要在训练时显式纳入陈旧上下文接口\n\n## Why important\n\n该工作把慢速语言与历史聚合、快速当前帧动作预测通过逐层 KV cache 接口解耦，并用随机陈旧性训练匹配异步部署分布；它把实时控制从单纯模型压缩问题改写为时间尺度、缓存一致性与新鲜观测融合的接口问题。\n\n## What changed\n\n此前快慢分层常被概括为慢规划加快控制；这里更具体地表明，只有当慢分支不依赖快分支…", "match_reason": "metadata:domains"}, {"id": "reflection_631ecd2479bd127e62730569", "type": "reflection", "title": "TELEDEXTER: dexterous teleoperation through consecutive hand-object subgoals", "path": "vault/reflections/reflection-reflection_631ecd2479bd127e62730569.md", "status": "active", "source_ids": ["source_570c26541066c02080dd8de5"], "snippet": "…embodiment constraints.\n\n## Surprising\n\nOne co-tracking controller supports [real-time] teleoperation across two dexterous hands and seven tasks…", "match_reason": "full-text:body"}, {"id": "reflection_9b221970c294557b1fcd2370", "type": "reflection", "title": "Secondary project profile: shared workspace as a debuggability boundary for physical agents", "path": "vault/reflections/reflection-reflection_9b221970c294557b1fcd2370.md", "status": "active", "source_ids": ["source_6ada1b3b0033883b83a3bf40"], "snippet": "…do the repository's workspace schema, failure traces, [real-time] deadlines, and safety refusal mechanisms work in code…", "match_reason": "full-text:body"}, {"id": "concept_6a559a41722de87986c350e7", "type": "concept", "title": "冻结 flow 先验的分阶段潜空间奖励转向 / Staged latent-space reward steering over a frozen flow prior", "path": "vault/memory/concept/concept_6a559a41722de87986c350e7.md", "status": "working", "source_ids": ["source_98bb68f21232969a79d77918"], "snippet": "# 冻结 [flow] 先验的分阶段潜空间奖励转向 / Staged latent-space reward steering over a frozen [flow] prior\n\n先用专家轨迹预训练并冻结整身 [flow] policy，再以 action…", "match_reason": "metadata:title"}, {"id": "concept_34269bf138ea36a302aaa11f", "type": "concept", "title": "接触分阶段的 flow-policy 候选选择 / contact-phase candidate selection for flow policies", "path": "vault/memory/concept/concept_34269bf138ea36a302aaa11f.md", "status": "working", "source_ids": ["source_bee998153a82cd2a92db045b"], "snippet": "# 接触分阶段的 flow-policy 候选选择 / contact-phase candidate selection for flow [policies]\n\n对生成多个动作候选的 flow policy，可用接触阶段门控在接触前按 TCP 接近物体、接触后按物体向任务目标的一阶距离下降评分…", "match_reason": "metadata:title"}, {"id": "concept_30d85c442682f6afd96c3022", "type": "concept", "title": "Flow-matching VLA 的流式上下文分区与 KV 缓存 / streaming context partitioning and KV caching for flow-matching VLAs", "path": "vault/memory/concept/concept_30d85c442682f6afd96c3022.md", "status": "working", "source_ids": ["source_e67cd99ac31c7017d6f7f7c7"], "snippet": "# [Flow]-matching VLA 的流式上下文分区与 KV 缓存 / streaming context partitioning and KV caching for [flow]-matching VLAs\n\n在论文所述 [flow]…", "match_reason": "metadata:title"}, {"id": "reflection_93c4dfb77bd88bfdd67b84c8", "type": "reflection", "title": "HCPG-Flow：接触阶段门控替代不可靠的 critic 排序 / contact-phase gating replaces weak critic ranking", "path": "vault/reflections/reflection-reflection_93c4dfb77bd88bfdd67b84c8.md", "status": "active", "source_ids": ["source_bee998153a82cd2a92db045b"], "snippet": "# HCPG-[Flow]：接触阶段门控替代不可靠的 critic 排序 / contact-phase gating replaces weak critic ranking\n\n## Why important\n\nHCPG-[Flow] 对 [flow]…", "match_reason": "metadata:title"}, {"id": "reflection_ff2ab4bfb8e8d08d5e0ab7df", "type": "reflection", "title": "冻结 flow 先验上的奖励转向需要先稳定价值接口，再扩展潜空间自由度", "path": "vault/reflections/reflection-reflection_ff2ab4bfb8e8d08d5e0ab7df.md", "status": "active", "source_ids": ["source_98bb68f21232969a79d77918"], "snippet": "# 冻结 [flow] 先验上的奖励转向需要先稳定价值接口，再扩展潜空间自由度\n\n## Why important\n\nRLMM-[Flow] 把移动操作的奖励后训练限制在冻结 [flow] policy 的初始噪声接口，并把高维整段潜变量优化拆成 action critic 预热与由粗到细的时间残差开放。这使“保留生成先验…", "match_reason": "metadata:title"}, {"id": "reflection_59bfe9d29f3ebbb4c8a6b162", "type": "reflection", "title": "Secondary architecture commentary: autoregression versus flow matching is an interface question", "path": "vault/reflections/reflection-reflection_59bfe9d29f3ebbb4c8a6b162.md", "status": "active", "source_ids": ["source_e6608d8f849ad472bbd95143"], "snippet": "…autoregression versus [flow] matching is an interface question\n\n## Why important\n\nThe article argues that architecture choice affects how…", "match_reason": "metadata:title"}, {"id": "claim_parameter_symmetry_conserved_gradient_flow_20260716", "type": "claim", "title": "Parameter-space symmetry implies conserved quantities in gradient flow", "path": "vault/memory/claim/claim_parameter_symmetry_conserved_gradient_flow_20260716.md", "status": "trusted", "source_ids": ["source_6ae6c4bef52010f96ddb3dbf", "source_dbfef5ee180346812d6d9a99"], "snippet": "Parameter-space symmetry implies conserved quantities in gradient [flow].", "match_reason": "metadata:title"}, {"id": "concept_59f92bcb786f695ddcd47f7f", "type": "concept", "title": "视频原生的光流动作接口", "path": "vault/memory/concept/concept_59f92bcb786f695ddcd47f7f.md", "status": "working", "source_ids": ["source_ef80ef223077ef0855660839"], "snippet": "# 视频原生的光流动作接口\n\n用连续光流视频表示机器人动作，使同一稠密运动接口既可由世界动作模型生成并解码为控制，也可作为未来视频生成条件，还能从无动作标签视频提取预训练监督。该接口覆盖可见跨帧运动，但不天然包含力、遮挡后状态或完整本体动力学。", "match_reason": "metadata:aliases"}, {"id": "concept_d5965e0770273320ea6b28f2", "type": "concept", "title": "主动真机因子评测", "path": "vault/memory/concept/concept_d5965e0770273320ea6b28f2.md", "status": "working", "source_ids": ["source_61152ca8210ad3913764a291"], "snippet": "# 主动真机因子评测\n\n把机器人策略在对象位姿、相机视角和初始状态等结构化任务因子组合上的性能视为未知函数，用带不确定性估计的概率代理模型和信息增益准则依次选择真机试验，以在有限预算下估计性能分布并定位易失败区域。", "match_reason": "metadata:aliases"}, {"id": "concept_test_time_fast_weight_robot_memory", "type": "concept", "title": "机器人策略的测试时快速权重记忆", "path": "vault/memory/concept/concept_test_time_fast_weight_robot_memory.md", "status": "working", "source_ids": ["source_79475aef7849b08664b51a4e"], "snippet": "# 机器人策略的测试时快速权重记忆\n\nRoboTTT 在预训练 GR00T N1.7 的 DiT 层加入可在序列中更新的 TTT fast-weight 模块，通过长序列 flow-matching 和纠正数据训练，使每轮推理将新上下文写入快速权重并传递到下一轮…", "match_reason": "metadata:aliases"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_9ddfb0f3d50b606bd13e17e2"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "22ac896993544c8830591d058011f913172649310f0b17c23e4f96551a5deb79"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt-5.6-sol-strong-daily-v2`
- Extraction：`extraction_dae950e373fdf450fcbd8f2b`
- 编译前召回已有对象：19
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_2c69b09323afa79344401cd8-延迟自适应的三段-flow-动作调度-latency-adaptive-three-region-flow-action-sch.md
@@ -0,0 +1,20 @@
+---
+id: "concept_2c69b09323afa79344401cd8"
+type: "concept"
+status: "proposal"
+title: "延迟自适应的三段 flow 动作调度 / Latency-adaptive three-region flow action schedule"
+created_at: "2026-08-01T18:23:04+08:00"
+updated_at: "2026-08-01T18:23:04+08:00"
+aliases: ["pi-R2 latency-adaptive schedule", "πR² staircase flow schedule", "three-region diffusion-forcing schedule", "三段阶梯动作噪声调度"]
+tags: []
+domains: ["robotics", "vision-language-action", "real-time-control", "flow-policy"]
+confidence: "high"
+source_ids: ["source_9ddfb0f3d50b606bd13e17e2"]
+relations: [{"type": "derived_from", "target_id": "source_9ddfb0f3d50b606bd13e17e2", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_dynamic_execution_horizon", "reason": "两者都针对动作块反应性；动态执行时域决定已生成块执行多少步，三段 flow schedule 把 in-flight 前缀和推理延迟编码进逐位置生成过程。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_a858f8d191d3afdd69418471", "reason": "三段调度依赖异步慢视觉语言与新鲜 proprioception 的快控制接口；该关系补充动作生成连续性，但不改变既有快慢接口的陈旧性边界。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
+change_reason: "compile bundle from source_9ddfb0f3d50b606bd13e17e2"
+reflection_context: {"reflection_ids": ["reflection_65c54683ecbd991d97da21e4"], "importance": "high", "changed_belief": "实时动作块策略并不要求每个控制 tick 都重新运行完整 VLM；局部接触反应可以由新鲜 proprioception 驱动，但必须训练时显式覆盖慢特征陈旧性，并让流调度与实际推理延迟一致。", "surprising": "三段 staircase schedule 在每次调用后滑动 d 个位置并补入 d 个纯噪声位置，稳定延迟时可精确复现自身；因此一次 NFE 既完成新动作释放又保持连续 buffer。", "connections": [{"shared_mechanism": "都保留慢速视觉语言上下文，并让快速动作路径读取更近期的局部传感。", "boundary": "现有异步快慢接口强调缓存陈旧性和上下文分区；πR² 额外把 fresh proprioception、slow-feature age embedding 与 per-position flow schedule 绑定到动作生成。", "difference": "快慢接口可直接复用，三段 latency-adaptive schedule 是新的动作生成与不可逆前缀机制。"}], "open_questions": ["当视觉变化本身是快速故障信号、网络延迟超过训练范围或单 GPU 不能隔离 VLM 与 DiT 时，快慢通道假设会如何失效？"]}
+---
+
+# 延迟自适应的三段 flow 动作调度 / Latency-adaptive three-region flow action schedule
+
+为实测推理延迟 d 构造 per-position noise schedule：前 d 个位置是已经或正在执行的 clean actions，并作为 inpainting 条件排除出训练损失；中间区域的噪声水平由 clean 向 noisy 递增；末尾 d 个位置是每次循环补入的纯噪声。每次 policy call 只做一次按位置 Euler 去噪，使 [d,2d) 变为 clean 并释放 d 个动作，随后 buffer 滑动 d 位并补入新噪声；训练时随机化 d、加入 noise jitter，并混入标准 flow warm-up，使一个模型适应可变延迟并初始化完整 buffer。该机制与仅选择动作块执行长度不同，也不等同于 KV 缓存；它依赖延迟落在训练范围、慢视觉语言通道足够稳定以及算力/通信抖动可被测量。
```
