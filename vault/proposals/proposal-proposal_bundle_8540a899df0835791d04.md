---
id: "proposal_bundle_8540a899df0835791d04"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-08-02T12:14:39+08:00"
updated_at: "2026-08-02T12:14:40+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_e504623270d30d733b2cb9e1"]
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
extraction_id: "extraction_f8bebe93e1f4817cd687b1f3"
input_sha256: "3621e7493d7c24d61e0a4fdc6b9b2549929584b75196b7b2c8286e39dd17f44c"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_e69974f653450465afb2aa3e", "target_path": "vault/knowledge/concepts/concept_e69974f653450465afb2aa3e-失败条件化的-vla-推理时组合转向-failure-gated-compositional-vla-steering.md", "base_sha256": null, "candidate_sha256": "e39ba6aa49ac53e648faa03628ac98e0dc592bd54b969b935d09b3045a3331b1", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_8540a899df0835791d04-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_e69974f653450465afb2aa3e.md", "working_at": "2026-08-02T12:14:40+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "concept_2c69b09323afa79344401cd8", "type": "concept", "title": "延迟自适应的三段 flow 动作调度 / Latency-adaptive three-region flow action schedule", "path": "vault/memory/concept/concept_2c69b09323afa79344401cd8.md", "status": "working", "source_ids": ["source_9ddfb0f3d50b606bd13e17e2"], "snippet": "# 延迟自适应的三段 flow 动作调度 / Latency-[adaptive] three-region flow action schedule\n\n为实测推理延迟 d 构造 per-position noise schedule：前…", "match_reason": "metadata:title"}, {"id": "concept_adaptive_interleaved_multimodal_planning", "type": "concept", "title": "自适应交错多模态规划", "path": "vault/memory/concept/concept_adaptive_interleaved_multimodal_planning.md", "status": "working", "source_ids": ["source_4ac7cf9f4fce43551683a04b"], "snippet": "# 自适应交错多模态规划\n\n长程机器人规划按步骤选择推理表征：用语言处理任务分解与动作顺序，用想象的未来视觉状态检查容量、碰撞和自由空间，只在几何精度需要时生成视觉思维。", "match_reason": "metadata:aliases"}, {"id": "concept_0c7884679bf6d4e1287ce225", "type": "concept", "title": "控制策略的自适应潜空间推理", "path": "vault/memory/concept/concept_0c7884679bf6d4e1287ce225.md", "status": "working", "source_ids": ["source_be9781ec8ca637c5dfd8fabb"], "snippet": "# 控制策略的自适应潜空间推理\n\n控制策略在输出动作前，通过带停止标记的自回归潜变量序列迭代组织控制相关信息，使内部计算长度能随观测与任务复杂度变化，而不是固定使用同样深度或依赖语言推理。", "match_reason": "metadata:aliases"}, {"id": "concept_fdb5ce439cbb603e19af8653", "type": "concept", "title": "前缀可解码的有序动作令牌 / Prefix-decodable ordered action tokens", "path": "vault/memory/concept/concept_fdb5ce439cbb603e19af8653.md", "status": "working", "source_ids": ["source_ba71396b5fc37637b125a89f"], "snippet": "# 前缀可解码的有序动作令牌 / Prefix-decodable ordered action tokens\n\n动作 tokenizer 同时满足高压缩、任意前缀都可解码为完整可执行动作块，以及由粗到细的有序精化。实现上以 transformer registers 和有限标量量化形成令牌，并用 nested dropout…", "match_reason": "metadata:domains"}, {"id": "reflection_734dd1ab9b6d593e5af1f262", "type": "reflection", "title": "动作令牌的顺序应对应可执行精度，而不只是压缩码位置", "path": "vault/reflections/reflection-reflection_734dd1ab9b6d593e5af1f262.md", "status": "active", "source_ids": ["source_ba71396b5fc37637b125a89f"], "snippet": "# 动作令牌的顺序应对应可执行精度，而不只是压缩码位置\n\n## Why important\n\nOrdered Action Tokenization 把压缩、全前缀可解码和由粗到细的有序结构同时作为策略接口要求。它使自回归策略可按预算提前停止，同时仍输出完整可执行的动作块，并让训练时的分块因果结构与推理时的块级生成匹配。\n\n## What changed\n\n动作离散化不再只是词表大小或重建误差问题；token 的顺序、任意前缀的可执行性…", "match_reason": "metadata:domains"}, {"id": "reflection_65c54683ecbd991d97da21e4", "type": "reflection", "title": "实时 VLA 的关键不是让所有模态同速，而是显式管理新鲜度和不可逆动作前缀", "path": "vault/reflections/reflection-reflection_65c54683ecbd991d97da21e4.md", "status": "active", "source_ids": ["source_9ddfb0f3d50b606bd13e17e2"], "snippet": "…快慢接口可直接复用，三段 latency-[adaptive] schedule 是新的动作生成与不可逆前缀机制。\n\n## Conflicts\n\nNone recorded.\n\n## Open questions\n\n- 当视觉变化本身是快速故障信号、网络延迟超过训练范围或单 GPU 不能隔离 VLM 与 DiT…", "match_reason": "full-text:body"}, {"id": "concept_ac0f0527a9c7bdba44eb37b8", "type": "concept", "title": "未来语义—几何变化监督的可执行 Latent Action", "path": "vault/memory/concept/concept_ac0f0527a9c7bdba44eb37b8.md", "status": "working", "source_ids": ["source_2d5d59db178b1a20c9213220"], "snippet": "# 未来语义—几何变化监督的可执行 [Latent] Action\n\n从当前帧与稀疏未来帧之间的语义特征变化和深度几何变化学习 [latent] action target，再用机器人动作预测与 [latent] world-model 监督把该表征绑定到可执行控制；无动作视频可参与未来动力学监督，但不直接提供机器人动作。", "match_reason": "metadata:title"}, {"id": "concept_6a559a41722de87986c350e7", "type": "concept", "title": "冻结 flow 先验的分阶段潜空间奖励转向 / Staged latent-space reward steering over a frozen flow prior", "path": "vault/memory/concept/concept_6a559a41722de87986c350e7.md", "status": "working", "source_ids": ["source_98bb68f21232969a79d77918"], "snippet": "# 冻结 flow 先验的分阶段潜空间奖励转向 / Staged [latent]-space reward steering over a frozen flow prior\n\n先用专家轨迹预训练并冻结整身 flow policy，再以 action…", "match_reason": "metadata:title"}, {"id": "reflection_3eda5d913d6a736393b8cd9c", "type": "reflection", "title": "WALA：用未来语义与几何变化约束可执行 latent action", "path": "vault/reflections/reflection-reflection_3eda5d913d6a736393b8cd9c.md", "status": "active", "source_ids": ["source_2d5d59db178b1a20c9213220"], "snippet": "# WALA：用未来语义与几何变化约束可执行 [latent] action\n\n## Why important\n\nWALA 不从原始像素重建 [latent] action，而是用稀疏未来帧的 DINOv3 feature delta 与 dense depth delta…", "match_reason": "metadata:title"}, {"id": "reflection_12ec24dd673a937d90f5bc21", "type": "reflection", "title": "Latent Memory Palace：控制中的自适应潜空间推理", "path": "vault/reflections/reflection-reflection_12ec24dd673a937d90f5bc21.md", "status": "active", "source_ids": ["source_be9781ec8ca637c5dfd8fabb"], "snippet": "# [Latent] Memory Palace：控制中的自适应潜空间推理\n\n## Why important\n\n它把控制策略的测试时推理从语言链或固定深度网络，改写为可变长度的潜变量推断过程，使“思考多久”成为控制表示的一部分，而不只是外部规划器的调度选择。\n\n## What changed\n\n此前知识库主要把自适应计算理解为动作块执行多久后重规划；该材料增加了一个正交维度：策略可以在输出动作之前，自适应分配内部潜空间推理步数…", "match_reason": "metadata:title"}, {"id": "reflection_c3b3e3b0cbbc4d820aa25ce5", "type": "reflection", "title": "CLAP：人类视频需先对齐到机器人可执行 token，而不是直接重建视觉变化", "path": "vault/reflections/reflection-reflection_c3b3e3b0cbbc4d820aa25ce5.md", "status": "active", "source_ids": ["source_f4bd7390e1b485ab773f1446"], "snippet": "# CLAP：人类视频需先对齐到机器人可执行 token，而不是直接重建视觉变化\n\n## Why important\n\nCLAP 先从机器人轨迹学习量化、可执行动作词表，再用对比学习把人类视觉转移对齐到该词表，试图避免 [latent] action 被背景变化和外观噪声主导。\n\n## What changed\n\n人类视频规模本身不足以保证机器人迁移；若…", "match_reason": "metadata:domains"}, {"id": "concept_fc70bfc09ac7d9473592f09c", "type": "concept", "title": "全身冗余的部分运动学嵌入", "path": "vault/memory/concept/concept_fc70bfc09ac7d9473592f09c.md", "status": "working", "source_ids": ["source_951559714c0383331b1b30ac"], "snippet": "# 全身冗余的部分运动学嵌入\n\n学习给定末端目标下的可行 partial reference 分布，把全身运动学冗余压缩为高层可导航 [latent]，再由低层 imitation controller 保证动力学可行执行。它利用浮动基座和躯干自由度扩大工作空间，但支持集受运动学数据覆盖约束。", "match_reason": "metadata:aliases"}, {"id": "concept_1920583cd9c7063491d45a40", "type": "concept", "title": "表示对齐的未来触觉 grounding", "path": "vault/memory/concept/concept_1920583cd9c7063491d45a40.md", "status": "working", "source_ids": ["source_38651a884fe5c5c73a6e190d"], "snippet": "# 表示对齐的未来触觉 grounding\n\n在触觉增强 VLA 中，先以冻结 probe 比较各内部表示对未来触觉状态的可预测性，再将紧凑未来触觉 [latent] 的预测损失施加到最能表达动作条件接触动力学的中间 action-expert 接口；该训练期约束不同于直接预测噪声较大的原始触觉，也不同于在多个接口无差别叠加损失。", "match_reason": "metadata:aliases"}, {"id": "concept_latent_space_intervention_adaptation", "type": "concept", "title": "生成策略的潜空间干预适应", "path": "vault/memory/concept/concept_latent_space_intervention_adaptation.md", "status": "working", "source_ids": ["source_9a6e63428ed93e1a99ea4c4d"], "snippet": "# 生成策略的潜空间干预适应\n\n把人的纠正动作反演为冻结生成策略中可产生该动作的噪声变量，再用这些潜变量监督轻量噪声策略，从输入潜空间调整部署行为而不改基础模型权重。", "match_reason": "metadata:aliases"}, {"id": "reflection_070e73598e48429fb5eafe01", "type": "reflection", "title": "PAKE：先学习运动学冗余分布，再让 RL 选择部分参考", "path": "vault/reflections/reflection-reflection_070e73598e48429fb5eafe01.md", "status": "active", "source_ids": ["source_951559714c0383331b1b30ac"], "snippet": "…PAKE 从大规模运动学数据学习条件分布以覆盖多解；REGRIND 从单个人类示范构造交互保持 reference 并围绕它做 residual RL。\n\n## Conflicts\n\n- 运动学 [latent] 缩小搜索空间，却可能排除依赖动力学、接触或动量的可行解。\n\n## Open questions\n\n- 怎样检测目标任务所需解落在 KNF…", "match_reason": "full-text:body"}, {"id": "concept_88f87ddc5dcf77113c5154c4", "type": "concept", "title": "面向组合式 OOD 操作的子任务监督与状态条件视觉遮蔽", "path": "vault/memory/concept/concept_88f87ddc5dcf77113c5154c4.md", "status": "working", "source_ids": ["source_0c017bf657a648ca70e9ae25"], "snippet": "# 面向组合式 OOD 操作的子任务监督与状态条件视觉遮蔽\n\nAC-VLA 针对视觉语言动作模型在未见子任务组合中的轨迹过拟合和腕部视角感知捷径，将复杂指令和对应本体感觉轨迹对齐为稠密子任务监督，并与完整演示混合训练；同时在闭爪阶段按状态抑制腕部视角，以迫使模型更多利用全局空间语义。该方法在论文所述 π0.5 与 LIBERO 设置中报告组合 OOD 改善…", "match_reason": "metadata:aliases"}, {"id": "reflection_4b0d86fae587571975ca7c09", "type": "reflection", "title": "AC-VLA：组合泛化要同时约束轨迹记忆与视觉捷径", "path": "vault/reflections/reflection-reflection_4b0d86fae587571975ca7c09.md", "status": "active", "source_ids": ["source_0c017bf657a648ca70e9ae25"], "snippet": "# AC-VLA：组合泛化要同时约束轨迹记忆与视觉捷径\n\n## Why important\n\nAC-VLA 将未见任务重组时的失败拆为整体轨迹过拟合与腕部视角感知捷径，并分别以子任务监督和状态条件非对称遮蔽应对；它把组合泛化从抽象能力标签转为可区分的数据与感知接口问题。\n\n## What changed\n\n此前容易将组合 OOD 失败归为缺少更多演示；本文提示，即使熟悉子技能都出现过，训练目标若保留完整轨迹关联和局部纹理捷径…", "match_reason": "metadata:domains"}, {"id": "reflection_59bfe9d29f3ebbb4c8a6b162", "type": "reflection", "title": "Secondary architecture commentary: autoregression versus flow matching is an interface question", "path": "vault/reflections/reflection-reflection_59bfe9d29f3ebbb4c8a6b162.md", "status": "active", "source_ids": ["source_e6608d8f849ad472bbd95143"], "snippet": "…Like latent-action work, the article asks whether semantic and motor variables occupy an interface that supports [compositional]…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_e504623270d30d733b2cb9e1"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "07cd53fc7af1bf3f109a79f88f031e0076fefcf0f787b35d3378ba788670e82f"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt-5.6-sol-strong-daily-v2`
- Extraction：`extraction_f8bebe93e1f4817cd687b1f3`
- 编译前召回已有对象：20
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_e69974f653450465afb2aa3e-失败条件化的-vla-推理时组合转向-failure-gated-compositional-vla-steering.md
@@ -0,0 +1,20 @@
+---
+id: "concept_e69974f653450465afb2aa3e"
+type: "concept"
+status: "proposal"
+title: "失败条件化的 VLA 推理时组合转向 / Failure-gated compositional VLA steering"
+created_at: "2026-08-02T12:14:39+08:00"
+updated_at: "2026-08-02T12:14:39+08:00"
+aliases: ["RL2-VLA", "adaptive RL latent compositional steering", "failure-gated test-time VLA scaling", "失败门控 VLA 转向"]
+tags: []
+domains: ["robotics", "vision-language-action", "reinforcement-learning", "test-time-steering"]
+confidence: "high"
+source_ids: ["source_e504623270d30d733b2cb9e1"]
+relations: [{"type": "derived_from", "target_id": "source_e504623270d30d733b2cb9e1", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_6a559a41722de87986c350e7", "reason": "两者都冻结 flow 先验并用离线 RL 改变动作分布；RL2-VLA 在推理期组合速度场并由失败门控，RLMM-Flow 在潜变量训练接口中分阶段优化整段动作。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_vla_action_evaluation_distillation", "reason": "两者都依赖候选动作评价来保留冻结 VLA 的通用先验；RL2-VLA 额外改变失败态候选分布，动作评估蒸馏主要负责从既有候选中选择。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_2db7edf95d63ca80702f042e", "reason": "两者都用失败信号决定是否干预；RL2-VLA 在动作派发前扩展并选择候选，CheckVLA 在派发后按动作后果偏差修复可部署后缀。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
+change_reason: "compile bundle from source_e504623270d30d733b2cb9e1"
+reflection_context: {"reflection_ids": ["reflection_f2923d7702925e8f48787602"], "importance": "high", "changed_belief": "此前容易把 test-time scaling 理解为统一增加候选数量；该论文区分成功态与失败态的相反缩放行为，表明多样性干预需要由失败风险门控，否则会损害已经准确的动作。", "surprising": "论文报告组合转向在失败元组上改善动作误差缩放，却在成功元组上属于最差方法之一；适应性不是附加优化，而是避免转向伤害基础策略的核心边界。", "connections": [{"shared_mechanism": "都冻结基础 flow/VLA 先验，并在小于主干的接口上引入奖励或纠正信号。", "boundary": "RL2-VLA 在推理期组合 VLA 与离线 RL 速度场并依赖失败检测和候选验证；RLMM-Flow 在训练期优化初始潜变量，CheckVLA 在动作派发后检测后果偏差并修复后缀。", "difference": "三者分别改变候选分布、生成潜变量和已提交动作后缀，监督来源与干预时机不可互换。"}], "open_questions": ["失败检测器在新本体、新相机与没有在线失败 rollout 的场景中如何校准，才能避免把门控收益建立在额外任务级数据上？"]}
+---
+
+# 失败条件化的 VLA 推理时组合转向 / Failure-gated compositional VLA steering
+
+从冻结 VLA 的 action-expert latent 训练轻量离线 RL flow policy，并在推理时对 VLA 与 RL 的速度场做加权组合以生成偏离示范主模态的候选；失败检测器仅在基础策略预计失效时启用组合转向，成功状态退回基础 VLA，最后由外部 verifier 选择动作。该接口把多样性放在失败态而非全时段：论文的 scaling analysis 显示组合转向可改善失败元组，却会扰动已准确的成功元组。它不同于优化初始噪声的 RLMM-Flow，也不同于派发后检测并修复后缀的 CheckVLA。适用性仍受离线数据支持域、失败检测校准、候选 verifier 质量与额外任务级 rollout 需求约束；论文的 SIMPLER、PolaRiS 和 PiperX 结果不能直接推出无校准跨本体泛化。
```
