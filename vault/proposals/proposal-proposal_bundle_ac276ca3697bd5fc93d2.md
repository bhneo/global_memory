---
id: "proposal_bundle_ac276ca3697bd5fc93d2"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-28T18:37:16+08:00"
updated_at: "2026-07-28T18:37:22+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_ba71396b5fc37637b125a89f"]
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
extraction_id: "extraction_072c97957f56edc088c9f125"
input_sha256: "172ce81b6a922b1ad05f1c5c102e6aae06509a6a84b2d256ec033b275427d16c"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_fdb5ce439cbb603e19af8653", "target_path": "vault/knowledge/concepts/concept_fdb5ce439cbb603e19af8653-前缀可解码的有序动作令牌-prefix-decodable-ordered-action-tokens.md", "base_sha256": null, "candidate_sha256": "530f94caba42447f7e0b3e3ff81a36969779b3d5474a129e8cdaf699419034a4", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_ac276ca3697bd5fc93d2-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_fdb5ce439cbb603e19af8653.md", "working_at": "2026-07-28T18:37:22+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "concept_ac0f0527a9c7bdba44eb37b8", "type": "concept", "title": "未来语义—几何变化监督的可执行 Latent Action", "path": "vault/memory/concept/concept_ac0f0527a9c7bdba44eb37b8.md", "status": "working", "source_ids": ["source_2d5d59db178b1a20c9213220"], "snippet": "# 未来语义—几何变化监督的可执行 Latent [Action]\n\n从当前帧与稀疏未来帧之间的语义特征变化和深度几何变化学习 latent [action] target，再用机器人动作预测与 latent world-model 监督把该表征绑定到可执行控制；无动作视频可参与未来动力学监督，但不直接提供机器人动作。", "match_reason": "metadata:title"}, {"id": "input_5cdcb4ea55f4352398dddd8c", "type": "input", "title": "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement", "path": "vault/inputs/input-input_5cdcb4ea55f4352398dddd8c.md", "status": "active", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "# Training-Free Acceleration for Vision-Language-[Action] Models with [Action] Caching and Refinement\n\nInput Episode for `source_291d6174cf92660287138f47…", "match_reason": "metadata:title"}, {"id": "concept_dual_system_world_action_model", "type": "concept", "title": "双系统 World Action Model", "path": "vault/memory/concept/concept_dual_system_world_action_model.md", "status": "working", "source_ids": ["source_ba057c2c11df2a5eba107870"], "snippet": "# 双系统 World [Action] Model\n\n默认由 World [Action] Model 直接生成动作块，仅在粗粒度指令需要任务分解时调用视觉语言规划器生成可执行子任务，从而把高频执行与低频语义规划解耦。", "match_reason": "metadata:title"}, {"id": "reflection_3eda5d913d6a736393b8cd9c", "type": "reflection", "title": "WALA：用未来语义与几何变化约束可执行 latent action", "path": "vault/reflections/reflection-reflection_3eda5d913d6a736393b8cd9c.md", "status": "active", "source_ids": ["source_2d5d59db178b1a20c9213220"], "snippet": "# WALA：用未来语义与几何变化约束可执行 latent [action]\n\n## Why important\n\nWALA 不从原始像素重建 latent [action]，而是用稀疏未来帧的 DINOv3 feature delta 与 dense depth delta…", "match_reason": "metadata:title"}, {"id": "reflection_bd1bc1b00ef5304ee9d29e9c", "type": "reflection", "title": "FM-VLA：力历史将接触进度压缩为记忆 token / force history compresses contact progress into memory tokens", "path": "vault/reflections/reflection-reflection_bd1bc1b00ef5304ee9d29e9c.md", "status": "active", "source_ids": ["source_1ee2c3fae53a9d05689cd143"], "snippet": "# FM-VLA：力历史将接触进度压缩为记忆 token / force history compresses contact progress into memory [tokens]\n\n## Why important\n\nFM-VLA 以预训练 VAE…", "match_reason": "metadata:title"}, {"id": "concept_769f84122571858ee48f9c48", "type": "concept", "title": "共享持久对象状态的可验证人形 VLA 闭环", "path": "vault/memory/concept/concept_769f84122571858ee48f9c48.md", "status": "working", "source_ids": ["source_d33321374508784864c44d65"], "snippet": "# 共享持久对象状态的可验证人形 VLA 闭环\n\n对每个活跃子任务维护角色索引的 RGB-D 三维对象记录，将其序列化为动作专家的对象 token，并在执行动作块后刷新同一记录以检查几何成功谓词和触发恢复。该方法依赖对象角色绑定、深度观测与谓词定义，不能把报告的特定 Unitree G1 结果当作一般保证。", "match_reason": "metadata:aliases"}, {"id": "reflection_051f1a0f00d5131171df1440", "type": "reflection", "title": "Pelican-VLA 0.5：注意力泛化先于动作泛化", "path": "vault/reflections/reflection-reflection_051f1a0f00d5131171df1440.md", "status": "active", "source_ids": ["source_3093a2f57587e962f87d6277"], "snippet": "…通用 VLA 概念描述端到端跨本体策略目标，Pelican 的结果把其中的注意力表示能力与最终执行能力拆开评估\n\n## Conflicts\n\n- 可视化注意力可能不是因果解释；操作相关区域聚焦也可能与动作成功无关\n\n## Open questions\n\n- 如何设计干预实验验证 Bottleneck [Tokens] 的注意力是否因果改善跨本体动作泛化？\n\n## Possible mechanisms\n\n- 紧凑瓶颈迫使感知到动作通路压缩并路由任务相关对象与接触区域\n\n## Future…", "match_reason": "full-text:body"}, {"id": "reflection_963ef2c3818ac53b780d8b29", "type": "reflection", "title": "Patch Policy：block-causal 掩码保留时序并接入密集视觉 / block-causal masking admits dense vision without losing temporal causality", "path": "vault/reflections/reflection-reflection_963ef2c3818ac53b780d8b29.md", "status": "active", "source_ids": ["source_e8651a193623cbe2b86becb0"], "snippet": "…大 VLA 借完整 VLM 获得 dense [tokens]；本文以最小策略扩展避开该骨干计算开销。\n\n## Conflicts\n\nNone recorded.\n\n## Open questions\n\n- 遮挡、相机变化和长期多任务上下文下，dense patch 的收益是否仍超过全局表示…", "match_reason": "full-text:body"}, {"id": "concept_97fc87cffe27a2fc9d741e78", "type": "concept", "title": "Block-causal dense patch policy / 区块因果的密集视觉策略", "path": "vault/memory/concept/concept_97fc87cffe27a2fc9d741e78.md", "status": "working", "source_ids": ["source_e8651a193623cbe2b86becb0"], "snippet": "# Block-causal dense patch policy / 区块因果的密集视觉策略\n\n对基于 transformer 的机器人策略，可将预训练 ViT 的密集 patch [tokens] 与状态共同输入，并以 block-causal…", "match_reason": "full-text:body"}, {"id": "concept_2ce226e08d585158c1dfbb18", "type": "concept", "title": "接触反馈应区分短时反应、事件记忆与概率后验", "path": "vault/memory/concept/concept_2ce226e08d585158c1dfbb18.md", "status": "working", "source_ids": ["source_4e06d1b1cdcd0d07eff47909", "source_1ee2c3fae53a9d05689cd143"], "snippet": "…LIFT 用近期六维力在动作块内做因果反应；FM-VLA 把更长的 wrench 历史压缩为 force-memory [tokens]，以保留视觉难以区分的接触事件和重复进度；BayesContact 则用深度与接触似然维护物体姿态粒子后验。三者共同弥补纯视觉在接触状态中的可观测性缺口，但短时残差修正、历史压缩和概率信念不能相互替代，且都受传感延迟、模型失配和任务分布限制。", "match_reason": "full-text:body"}, {"id": "concept_c37ccf2640da63192432d5d5", "type": "concept", "title": "VLA 的力历史记忆用于非 Markov 接触操作 / force-history memory for non-Markov contact-rich VLA manipulation", "path": "vault/memory/concept/concept_c37ccf2640da63192432d5d5.md", "status": "working", "source_ids": ["source_1ee2c3fae53a9d05689cd143"], "snippet": "…Markov 操作中，可将力/力矩历史经预训练 VAE 压缩为 force-memory [tokens]，并连同短状态历史条件化 VLA 的 action expert，以保留接触事件和重复进度。该方法依赖可靠 wrench 传感…", "match_reason": "full-text:body"}, {"id": "concept_17750931a381f8453b27ccba", "type": "concept", "title": "连续曲线动作接口与执行重定时", "path": "vault/memory/concept/concept_17750931a381f8453b27ccba.md", "status": "working", "source_ids": ["source_4b25f596c34869693b9b8151"], "snippet": "# 连续曲线动作接口与执行重定时\n\n策略输出参数化连续动作曲线而非固定采样的离散动作块，使轨迹几何能够被高频采样、按时间缩放并在相邻预测段之间对齐。该接口把动作表示与执行时标解耦，但可用倍速仍受接触动力学、低层控制器和执行器裕度限制。", "match_reason": "metadata:domains"}, {"id": "concept_event_sensitive_task_progress_memory", "type": "concept", "title": "事件敏感的任务进度记忆", "path": "vault/memory/concept/concept_event_sensitive_task_progress_memory.md", "status": "working", "source_ids": ["source_011483b15aae65e849a3772e"], "snippet": "# 事件敏感的任务进度记忆\n\n用连续时间潜在状态跟踪单回合任务进度：在稳定运输或遮挡阶段保留 belief，在接触、释放和子目标切换附近快速改写，并把更新后的 belief 直接调制流匹配动作解码器。", "match_reason": "metadata:domains"}, {"id": "reflection_0078f804e87c7ed12f88876d", "type": "reflection", "title": "B-spline Policy：把动作表示与执行速度从固定采样率中解耦", "path": "vault/reflections/reflection-reflection_0078f804e87c7ed12f88876d.md", "status": "active", "source_ids": ["source_4b25f596c34869693b9b8151"], "snippet": "# B-spline Policy：把动作表示与执行速度从固定采样率中解耦\n\n## Why important\n\nBSP 不再预测等时间间隔的离散动作块，而是预测连续 B-spline 曲线，使同一几何轨迹能被高频采样、时间缩放并在推理重叠时做段间对齐；这把执行速度变成可调接口。\n\n## What changed\n\n此前动作块加速常被理解为少重规划或少执行几步…", "match_reason": "metadata:domains"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_ba71396b5fc37637b125a89f"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 1.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 0, "new_object_count": 1, "updated_object_count": 0, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "66f55092b97414b2e15bf5d56fb96e87e88a847e4db2a4b5ed6ee6d8cf9ec73c"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt-5.6-sol-strong-daily-v2`
- Extraction：`extraction_072c97957f56edc088c9f125`
- 编译前召回已有对象：16
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_fdb5ce439cbb603e19af8653-前缀可解码的有序动作令牌-prefix-decodable-ordered-action-tokens.md
@@ -0,0 +1,20 @@
+---
+id: "concept_fdb5ce439cbb603e19af8653"
+type: "concept"
+status: "proposal"
+title: "前缀可解码的有序动作令牌 / Prefix-decodable ordered action tokens"
+created_at: "2026-07-28T18:37:16+08:00"
+updated_at: "2026-07-28T18:37:16+08:00"
+aliases: ["Ordered Action Tokenization", "OAT", "ordered action tokens", "有序动作令牌"]
+tags: []
+domains: ["robotics", "vision-language-action", "action-tokenization", "adaptive-compute"]
+confidence: "high"
+source_ids: ["source_ba71396b5fc37637b125a89f"]
+relations: [{"type": "derived_from", "target_id": "source_ba71396b5fc37637b125a89f", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_dynamic_execution_horizon", "reason": "两者都提供按预算改变策略粒度的接口；OAT 调节表示精度和生成调用数，动态执行时域调节实际执行的动作前缀，二者可组合但不可混同。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
+change_reason: "compile bundle from source_ba71396b5fc37637b125a89f"
+reflection_context: {"reflection_ids": ["reflection_734dd1ab9b6d593e5af1f262"], "importance": "high", "changed_belief": "动作离散化不再只是词表大小或重建误差问题；token 的顺序、任意前缀的可执行性，以及训练和推理的生成分组是否一致，都会改变策略的精度—延迟前沿。", "surprising": "把单 token OAT 在推理期事后分块并不能复现训练时采用匹配 block-causal mask 的 OATpow2；相同五次前向预算下，匹配训练的结果明显更好。", "connections": [{"shared_mechanism": "都允许根据预算改变一次策略调用所承担的计算或执行粒度。", "boundary": "现有 dynamic execution horizon 改变的是动作块实际执行的前缀长度；OAT 改变的是动作表示的逐级精化和生成调用数。", "difference": "执行时域自适应与表示精度自适应互补，但不是同一个控制量。"}], "open_questions": ["能否让策略按观测不确定性动态选择 OAT 前缀或 block 数，而不是使用固定推理预算？"]}
+---
+
+# 前缀可解码的有序动作令牌 / Prefix-decodable ordered action tokens
+
+动作 tokenizer 同时满足高压缩、任意前缀都可解码为完整可执行动作块，以及由粗到细的有序精化。实现上以 transformer registers 和有限标量量化形成令牌，并用 nested dropout 训练各长度前缀重建整段动作，使早期令牌承载全局粗动作、后续令牌补充残差；OATsing 逐令牌生成，OATpow2 则用与训练匹配的幂次 block-causal 分组减少自回归前向调用。论文在限定操作基准中报告较强的精度—延迟前沿，但不同视觉语言骨干并非一致受益，且更长时域、更多本体与动态预算仍未充分验证。
```
