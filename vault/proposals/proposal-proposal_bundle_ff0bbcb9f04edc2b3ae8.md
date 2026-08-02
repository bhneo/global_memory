---
id: "proposal_bundle_ff0bbcb9f04edc2b3ae8"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-08-02T18:22:04+08:00"
updated_at: "2026-08-02T18:22:05+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_bdb17eb4583ec8af52f28dfb"]
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
extraction_id: "extraction_e00403773cfb4bfa9beb920b"
input_sha256: "3d91b86d88556a90a53a08d659db15ceab89147ebfcff0f844a5d681316abc24"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "create", "target_id": "concept_8a7645759329c1444d94a4cf", "target_path": "vault/knowledge/concepts/concept_8a7645759329c1444d94a4cf-同状态相对价值驱动的扩散导航后训练-same-state-relative-value-diffusion-navigation.md", "base_sha256": null, "candidate_sha256": "b5c7749937ad2b1c8687490fcbd142ffa0d490ef24430de920c5c696103385fb", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_ff0bbcb9f04edc2b3ae8-concept-1.md", "base_path": null, "working_path": "vault/memory/concept/concept_8a7645759329c1444d94a4cf.md", "working_at": "2026-08-02T18:22:05+08:00"}]
existing_context: [{"id": "reflection_ad213cb7065716a7685a1049", "type": "reflection", "title": "被屏蔽公众号页：不可读状态不是证据 / blocked-page state is not evidence", "path": "vault/reflections/reflection-reflection_ad213cb7065716a7685a1049.md", "status": "active", "source_ids": ["source_06fda6f7c8cb1e94d7772818"], "snippet": "# 被屏蔽公众号页：不可读状态不是证据 / blocked-[page] state is not evidence\n\n## Why important\n\n来源只含平台屏蔽提示，缺少可核验正文。\n\n## What changed\n\n我不会从提示推断文章主题或事实，取得原文前不生成知识对象。\n\n## Surprising\n\nNot…", "match_reason": "metadata:title"}, {"id": "reflection_5765b322ec0b7812d775d928", "type": "reflection", "title": "被屏蔽的公众号页：占位提示不是文章证据 / a blocked-page notice is not article evidence", "path": "vault/reflections/reflection-reflection_5765b322ec0b7812d775d928.md", "status": "active", "source_ids": ["source_fac3080b8382a1c6d606cecd"], "snippet": "# 被屏蔽的公众号页：占位提示不是文章证据 / a blocked-[page] notice is not article evidence\n\n## Why important\n\n来源只提供平台屏蔽提示，缺少原文主题、作者和论证，不能承载任何可核验知识。\n\n## What changed…", "match_reason": "metadata:title"}, {"id": "reflection_ad5dbb9f0754e7fa34195d42", "type": "reflection", "title": "Secondary launch report: Qwen-Robot separates navigation, manipulation, and world prediction behind language-first interfaces", "path": "vault/reflections/reflection-reflection_ad5dbb9f0754e7fa34195d42.md", "status": "active", "source_ids": ["source_11bc6c51fa038191e33bc9a7"], "snippet": "…Qwen-Robot separates [navigation], manipulation, and world prediction behind language-first interfaces\n\n## Why important\n\nThe article presents a…", "match_reason": "metadata:title"}, {"id": "concept_34abf7a170a7e0fc0492fc16", "type": "concept", "title": "指向式视觉导航接口", "path": "vault/memory/concept/concept_34abf7a170a7e0fc0492fc16.md", "status": "working", "source_ids": ["source_886372de22c708b28cd11e4b"], "snippet": "# 指向式视觉导航接口\n\n导航策略优先在当前 RGB 图像中预测目标位置与到达朝向，用视觉坐标减少对相机内参和世界尺度的依赖；当目标不可见时，再回退到机器人局部坐标位移。", "match_reason": "metadata:aliases"}, {"id": "input_a318de5517033fc7e9a86795", "type": "input", "title": "Robostral Navigate: single-camera AI navigation | Mistral AI", "path": "vault/inputs/input-input_a318de5517033fc7e9a86795.md", "status": "active", "source_ids": ["source_886372de22c708b28cd11e4b"], "snippet": "…single-camera AI [navigation] | Mistral AI\n\nInput Episode for `source_886372de22c708b28cd11e4b`. The immutable Source remains authoritative.\n\n# Robostral Navigate…", "match_reason": "metadata:title"}, {"id": "reflection_e9882c5308e95eff42280423", "type": "reflection", "title": "Xbotics 学习指南：导航集合而非稳定研究结论", "path": "vault/reflections/reflection-reflection_e9882c5308e95eff42280423.md", "status": "active", "source_ids": ["source_ff5ce793c0efda7112e73c86"], "snippet": "# Xbotics 学习指南：导航集合而非稳定研究结论\n\n## Why important\n\n该仓库可用于发现综述、仿真、开源硬件、人物与公司资料，但内容持续变化且混合多种证据等级。\n\n## What changed\n\n它应作为检索入口保留，而不是编译为关于具身智能路线的知识节点。\n\n## Surprising\n\n仓库覆盖面广，但抓取正文主要是 GitHub…", "match_reason": "metadata:domains"}, {"id": "reflection_6a9092352b95c1ab440d2274", "type": "reflection", "title": "Robostral Navigate：动作接口选择可以降低传感与本体耦合", "path": "vault/reflections/reflection-reflection_6a9092352b95c1ab440d2274.md", "status": "active", "source_ids": ["source_886372de22c708b28cd11e4b"], "snippet": "# Robostral Navigate：动作接口选择可以降低传感与本体耦合\n\n## Why important\n\n它把单目导航的泛化部分归因于动作表达：优先预测当前图像中的目标点与到达朝向，在目标不在视野时才回退到局部坐标位移，从而减少对相机内参、世界尺度和特定底盘的耦合。\n\n## What changed\n\n此前容易把导航鲁棒性主要归因于更多传感器或更大模型；该材料提示视觉坐标系中的指向接口本身就是一种跨相机与跨本体归纳偏置。\n\n## Surprising\n\n官方页面报告单 RGB、仿真训练的…", "match_reason": "metadata:domains"}, {"id": "input_d79b943efae225d156e447cb", "type": "input", "title": "GitHub - WassimTenachi/PhySO: Physical Symbolic Optimization · GitHub", "path": "vault/inputs/input-input_d79b943efae225d156e447cb.md", "status": "active", "source_ids": ["source_a659477a1a8ac8bd6e3c3477"], "snippet": "…Physical Symbolic Optimization · GitHub Skip to content [Navigation] Menu Toggle [navigation] Sign in Appearance settings Platform AI CODE…", "match_reason": "full-text:body"}, {"id": "concept_2c69b09323afa79344401cd8", "type": "concept", "title": "延迟自适应的三段 flow 动作调度 / Latency-adaptive three-region flow action schedule", "path": "vault/memory/concept/concept_2c69b09323afa79344401cd8.md", "status": "working", "source_ids": ["source_9ddfb0f3d50b606bd13e17e2"], "snippet": "# 延迟自适应的三段 flow 动作调度 / Latency-adaptive three-region flow action schedule\n\n为实测推理延迟 d 构造 per-position noise schedule：前…", "match_reason": "metadata:aliases"}, {"id": "concept_3d739e54fe54c8a5205d2301", "type": "concept", "title": "多坐标系同步动作去噪", "path": "vault/memory/concept/concept_3d739e54fe54c8a5205d2301.md", "status": "working", "source_ids": ["source_4df1017326dd7cc4786f4218"], "snippet": "# 多坐标系同步动作去噪\n\n在一个 canonical [diffusion] state 上，把同一噪声动作转换到多个任务相关坐标系，由 frame-specialized denoisers 分别预测，再变换回统一坐标系融合。它利用不同任务阶段在夹爪、基座或相对轨迹 frame 中更紧凑的动作分布，但依赖候选…", "match_reason": "metadata:domains"}, {"id": "reflection_a4abd223b36c137fb9bd6ae4", "type": "reflection", "title": "Mixture of Frames：动作分布复杂度部分来自坐标系选择", "path": "vault/reflections/reflection-reflection_a4abd223b36c137fb9bd6ae4.md", "status": "active", "source_ids": ["source_4df1017326dd7cc4786f4218"], "snippet": "…并把 frame transform 不确定性传播进扩散去噪与执行风险？\n\n## Possible mechanisms\n\n- 共享 canonical [diffusion] state 保持专家同步，各专家在本地 frame 中建模更紧凑的动作分布，路由器按阶段融合其预测。\n\n## Future directions\n\n- 比较人工…", "match_reason": "metadata:domains"}, {"id": "input_5cdcb4ea55f4352398dddd8c", "type": "input", "title": "Training-Free Acceleration for Vision-Language-Action Models with Action Caching and Refinement", "path": "vault/inputs/input-input_5cdcb4ea55f4352398dddd8c.md", "status": "active", "source_ids": ["source_291d6174cf92660287138f47"], "snippet": "…Acceleration of Flow-based VLA Models 2.3 [Diffusion] Caching on Image Generation 2.4 Warm-Starting for…", "match_reason": "full-text:body"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_bdb17eb4583ec8af52f28dfb"}
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
- Extraction：`extraction_e00403773cfb4bfa9beb920b`
- 编译前召回已有对象：12
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (create concept)

```diff
--- /dev/null
+++ candidate:vault/knowledge/concepts/concept_8a7645759329c1444d94a4cf-同状态相对价值驱动的扩散导航后训练-same-state-relative-value-diffusion-navigation.md
@@ -0,0 +1,20 @@
+---
+id: "concept_8a7645759329c1444d94a4cf"
+type: "concept"
+status: "proposal"
+title: "同状态相对价值驱动的扩散导航后训练 / Same-state relative-value diffusion navigation post-training"
+created_at: "2026-08-02T18:22:04+08:00"
+updated_at: "2026-08-02T18:22:04+08:00"
+aliases: ["X-NavDP", "GQRM", "Group Q-score Reweighted Matching", "self-bootstrapped action perturbation"]
+tags: []
+domains: ["robotics", "navigation", "diffusion-policy", "reinforcement-learning", "cross-embodiment"]
+confidence: "high"
+source_ids: ["source_bdb17eb4583ec8af52f28dfb"]
+relations: [{"type": "derived_from", "target_id": "source_bdb17eb4583ec8af52f28dfb", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_generalist_cross_embodiment_vla", "reason": "两者都共享高层策略以迁移不同本体；X-NavDP 仍通过 embodiment FiLM 和各形态低层控制器显式吸收运动学与动力学差异。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_6a559a41722de87986c350e7", "reason": "两者都在保留预训练生成先验的前提下用价值信号后训练；X-NavDP 在线更新 score，RLMM-Flow 冻结 flow decoder 并转向生成潜变量。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-strong-daily-v2", "status": "proposal"}]
+change_reason: "compile bundle from source_bdb17eb4583ec8af52f28dfb"
+reflection_context: {"reflection_ids": ["reflection_7991ec84469c68e4271878a4"], "importance": "high", "changed_belief": "我原先把候选动作 Q 值重加权理解为全局优势过滤；该方法显示，在不同状态回报尺度差异大时，应先在同状态候选组内归一化，避免简单状态垄断梯度。", "surprising": "无目标候选并非随机噪声，而是沿带目标预测相对当前策略动作做有符号外推，从而扩大探索又保留动作流形。", "connections": [{"shared_mechanism": "X-NavDP 与 concept_generalist_cross_embodiment_vla 都把不同机器人形态的数据或策略经验汇入共享高层决策模型。", "boundary": "该连接限于高层导航策略共享；X-NavDP 仍依赖每种形态的 embodiment 条件与预训练低层控制器，不能据此推断控制接口无关。", "difference": "通用跨本体 VLA 节点描述广义数据与本体适配框架，X-NavDP 具体以 FiLM 条件化、结构化扩散候选和在线 Q 重加权处理导航。"}, {"shared_mechanism": "X-NavDP 与 concept_6a559a41722de87986c350e7 都保留预训练生成策略的行为先验，并用价值信号集中改进较小的生成接口。", "boundary": "该连接要求基础策略已在候选邻域提供可行行为；critic 排序错误或先验无覆盖时，两者都不保证安全改进。", "difference": "X-NavDP 在线更新 diffusion score matching，RLMM-Flow 冻结 flow decoder 并由 latent actor-critic 转向初始噪声。"}], "open_questions": ["如何在保持同状态相对归一化优点的同时，加入跨状态的风险校准，使困难状态的高相对分数不掩盖绝对安全下界？"]}
+---
+
+# 同状态相对价值驱动的扩散导航后训练 / Same-state relative-value diffusion navigation post-training
+
+为在在线 RL 中稳定改进连续扩散导航策略，先从当前策略构造保留动作流形的带目标候选，以及沿带目标预测相对当前动作做有符号外推的无目标候选；再在同一状态的候选组内归一化 Q 分数、强化相对高价值候选，并以重加权 score matching 更新策略。这样困难低回报状态不会因绝对 Q 尺度较低而失去梯度，本体 FiLM 则让共享策略适配不同形态。边界是 critic 必须在组内排序可靠；方法仍依赖每种形态的低层控制器、短期观测记忆和训练场景覆盖，对透明或空心障碍的感知也有限。
```
