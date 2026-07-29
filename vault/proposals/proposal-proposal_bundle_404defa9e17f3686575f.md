---
id: "proposal_bundle_404defa9e17f3686575f"
type: "proposal"
status: "migrated"
title: "Compile bundle：arxiv.org"
created_at: "2026-07-27T11:17:30+08:00"
updated_at: "2026-07-27T11:19:13+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_ebf287b4d71ccdc41101466e"]
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
extraction_id: "extraction_2b6f47c1db4a1b1191eb94de"
input_sha256: "424a5539a9edfc183ca236562094673b66ccb87b6fee78160c13e52b5ca23a72"
bundle_items: [{"item_id": "concept-1", "object_type": "concept", "action": "update", "target_id": "concept_d28c0e5c8a5f864e616e2f7a", "target_path": "vault/memory/concept/concept_d28c0e5c8a5f864e616e2f7a.md", "base_sha256": "b270fe0222077e6f7da445b80cb0435c70a4efa57572a8613bc62903a3d72402", "candidate_sha256": "367632d115f170a5016a8533ada8d456bb2e3316ff4d2b7e408200b77ed733df", "decision": "working", "potential_conflicts": [], "atomicity_status": null, "evidence_coverage": null, "review_tier": "high", "candidate_path": "vault/proposals/candidate-proposal_bundle_404defa9e17f3686575f-concept-1.md", "base_path": "vault/proposals/base-proposal_bundle_404defa9e17f3686575f-concept-1.md", "working_path": "vault/memory/concept/concept_d28c0e5c8a5f864e616e2f7a.md", "evolution_action": "refine", "exception_id": null, "working_at": "2026-07-27T11:19:13+08:00"}]
existing_context: [{"id": "concept_cdbe55276db1fb0eb0aa370a", "type": "concept", "title": "硬球平衡涨落的对偶--剪枝长时控制 / duality-pruning long-time control of hard-sphere fluctuations", "path": "vault/memory/concept/concept_cdbe55276db1fb0eb0aa370a.md", "status": "working", "source_ids": ["source_3851b9ffbfbae3ca166308fd"], "snippet": "# 硬球平衡涨落的对偶--剪枝长时控制 / duality-pruning long-[time] control of hard-sphere fluctuations\n\n对处于平衡、低密度极限的硬球气体，可结合对偶方法与剪枝论证，证明涨落协方差在全时间（包括扩散尺度）由线性化 Boltzmann…", "match_reason": "metadata:title"}, {"id": "input_8f16a3ad954bd05b1a2a7752", "type": "input", "title": "[2012.03813] Long-time correlations for a hard-sphere gas at equilibrium", "path": "vault/inputs/input-input_8f16a3ad954bd05b1a2a7752.md", "status": "active", "source_ids": ["source_a5f4d6734479eea71ff9a2a4"], "snippet": "# [2012.03813] Long-[time] correlations for a hard-sphere gas at equilibrium\n\nInput Episode for `source_a5f4d6734479eea71ff9a2a4`. The…", "match_reason": "metadata:title"}, {"id": "claim_agentic_vla_libero_main_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO 上报告平均成功率 97.8%，Long 套件相对 SFT 基线提升 12.3 个百分点", "path": "vault/memory/claim/claim_agentic_vla_libero_main_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# Agentic-VLA 的 LIBERO 主结果\n\n在论文报告的 LIBERO 四套件实验中，Agentic-VLA 的 Spatial、Object、Goal、[Long] 成功率分别为 `97.2…", "match_reason": "metadata:title"}, {"id": "claim_agentic_vla_training_efficiency_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO-Long 上以 700 次迭代达到 90% 成功率，论文报告其相对 EVOLVE-VLA 收敛快 2.4×", "path": "vault/memory/claim/claim_agentic_vla_training_efficiency_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# Agentic-VLA 的训练效率\n\n在 LIBERO-[Long] 达到论文定义的 90% 成功率阈值时，Agentic-VLA 使用 700 次训练迭代和 22.4k rollouts；EVOLVE…", "match_reason": "metadata:title"}, {"id": "claim_agentic_vla_cross_task_20260715", "type": "claim", "title": "Agentic-VLA 在 LIBERO-Long 训练后无 Object 演示的跨任务适应达 31.2% 成功率，Direct SFT 迁移为 0%", "path": "vault/memory/claim/claim_agentic_vla_cross_task_20260715.md", "status": "working", "source_ids": ["source_2c21320690e566fbbf80fd75"], "snippet": "# Agentic-VLA 的跨任务适应结果\n\n论文在 LIBERO-[Long] 训练、LIBERO-Object 评估且不提供 Object task-specific demonstrations 的设置下比较跨任务迁移。Direct Transfer (SFT…", "match_reason": "metadata:title"}, {"id": "concept_test_time_fast_weight_robot_memory", "type": "concept", "title": "机器人策略的测试时快速权重记忆", "path": "vault/memory/concept/concept_test_time_fast_weight_robot_memory.md", "status": "working", "source_ids": ["source_79475aef7849b08664b51a4e"], "snippet": "# 机器人策略的测试时快速权重记忆\n\nRoboTTT 在预训练 GR00T N1.7 的 DiT 层加入可在序列中更新的 TTT fast-weight 模块，通过长序列 flow-matching 和纠正数据训练，使每轮推理将新上下文写入快速权重并传递到下一轮…", "match_reason": "metadata:aliases"}, {"id": "concept_abb38fe58cbeee09ce87a01d", "type": "concept", "title": "跨轨迹任务进度代理校正", "path": "vault/memory/concept/concept_abb38fe58cbeee09ce87a01d.md", "status": "working", "source_ids": ["source_e326446389e083c6ba9c94c2"], "snippet": "# 跨轨迹任务进度代理校正\n\n跨轨迹任务进度代理校正，是利用不同示范中相似物理状态的时间位置来减少单条轨迹的时间扭曲，使进度标签能表示停滞、倒退和非均匀推进，再用于价值或优势条件学习；其有效性取决于相似状态检索是否保持任务与接触语义。", "match_reason": "metadata:aliases"}, {"id": "concept_ebafde4b9db7a2ebd19c6bc6", "type": "concept", "title": "以休眠锚点和意图激活驱动的即时场景图生长", "path": "vault/memory/concept/concept_ebafde4b9db7a2ebd19c6bc6.md", "status": "working", "source_ids": ["source_e8650c5afb7548268f649fb8"], "snippet": "# 以休眠锚点和意图激活驱动的即时场景图生长\n\nJITOMA 不在进入环境时为全部观测建立高成本的稠密三维语义图，而是先从连续观测维护低成本全局休眠锚点；当任务查询出现时，系统解析机器人意图，唤醒相关局部锚点，并只在该子图内执行节点描述、功能推断等高成本操作。该设计旨在减少长期任务切换中的活动图规模、描述延迟和无关语义噪声，其收益受任务热图质量、锚点覆盖和遗漏关键细节风险约束。", "match_reason": "metadata:aliases"}, {"id": "claim_wechat_ergodicity_time_ensemble_equivalence_20260716", "type": "claim", "title": "该文将遍历性描述为个体时间平均与群体平均相等的条件", "path": "vault/memory/claim/claim_wechat_ergodicity_time_ensemble_equivalence_20260716.md", "status": "working", "source_ids": ["source_9d39636775b188c87d6a001f"], "snippet": "该文将遍历性描述为个体时间平均与群体平均相等的条件。", "match_reason": "metadata:tags"}, {"id": "input_dc842109f2de463e2185e842", "type": "input", "title": "[2207.08358] Rigorous justification of the wave kinetic theory", "path": "vault/inputs/input-input_dc842109f2de463e2185e842.md", "status": "active", "source_ids": ["source_542db9d12c226d58c56b30fd"], "snippet": "# [2207.08358] Rigorous justification of the wave kinetic theory\n\nInput Episode for `source_542db9d12c226d58c56b30fd`. The immutable Source remains authoritative.\n\n# [2207.08358] Rigorous justification of the wave kinetic theory\n\n> 原始内容：[va", "match_reason": "metadata:title"}, {"id": "input_0b5fbfe5c9ecee3146dadce4", "type": "input", "title": "[gr-qc/0209088] Gravity from Spacetime Thermodynamics", "path": "vault/inputs/input-input_0b5fbfe5c9ecee3146dadce4.md", "status": "active", "source_ids": ["source_ad785f5be8067788394ec708"], "snippet": "# [gr-qc/0209088] Gravity from Spacetime Thermodynamics\n\nInput Episode for `source_ad785f5be8067788394ec708`. The immutable Source remains authoritative.\n\n# [gr-qc/0209088] Gravity from Spacetime Thermodynamics\n\n> 原始内容：[vault/raw/objects/sh", "match_reason": "full-text:body"}, {"id": "input_0cf0fb98f9d994c03625746f", "type": "input", "title": "GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub", "path": "vault/inputs/input-input_0cf0fb98f9d994c03625746f.md", "status": "active", "source_ids": ["source_34d6513b0522739d0b25e303"], "snippet": "# GitHub - NVIDIA/Isaac-GR00T: NVIDIA Isaac GR00T N1.7 - A Foundation Model for Generalist Robots. · GitHub\n\nInput Episode for `source_34d6513b0522739d0b25e303`. The immutable Source remains authoritative.\n\n# GitHub - NVIDIA/Isaac-GR00T: NV", "match_reason": "metadata:title"}, {"id": "input_30f3dd905ee97551e16138bd", "type": "input", "title": "Chelsea Finn & Perry Dong：真实场景强化学习实现VLA后训练", "path": "vault/inputs/input-input_30f3dd905ee97551e16138bd.md", "status": "active", "source_ids": ["source_8b41a014bee47c4239a2fa81"], "snippet": "# Chelsea Finn & Perry Dong：真实场景强化学习实现VLA后训练\n\nInput Episode for `source_8b41a014bee47c4239a2fa81`. The immutable Source remains authoritative.\n\n# Chelsea Finn & Perry Dong：真实场景强化学习实现VLA后训练\n\n> 原始内容：[vault/raw/objects/sha256/15/20/15201becf4f", "match_reason": "full-text:body"}, {"id": "input_3b2d4a128c5dcd00c6d756b5", "type": "input", "title": "[2210.03878] An improved restriction estimate in $\\mathbb{R}^3$", "path": "vault/inputs/input-input_3b2d4a128c5dcd00c6d756b5.md", "status": "active", "source_ids": ["source_299adfe6dd42f97b6f75b777"], "snippet": "# [2210.03878] An improved restriction estimate in $\\mathbb{R}^3$\n\nInput Episode for `source_299adfe6dd42f97b6f75b777`. The immutable Source remains authoritative.\n\n# [2210.03878] An improved restriction estimate in $\\mathbb{R}^3$\n\n> 原始内容：[", "match_reason": "metadata:title"}, {"id": "input_3b93bb83f5c7407a5a03dcad", "type": "input", "title": "Building scalable AI agents with modular prompt transpilation - Google Developers Blog", "path": "vault/inputs/input-input_3b93bb83f5c7407a5a03dcad.md", "status": "active", "source_ids": ["source_3521fe9ac8d8f054440ec0af"], "snippet": "# Building scalable AI agents with modular prompt transpilation - Google Developers Blog\n\nInput Episode for `source_3521fe9ac8d8f054440ec0af`. The immutable Source remains authoritative.\n\n# Building scalable AI agents with modular prompt tr", "match_reason": "metadata:title"}, {"id": "input_41c7203faaf98b68b319eebc", "type": "input", "title": "GitHub - InternRobotics/REAL: [ECCV2026] Official open-source repository for REAL——Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation · GitHub", "path": "vault/inputs/input-input_41c7203faaf98b68b319eebc.md", "status": "active", "source_ids": ["source_a5f8ae205338d5f97eea87c7"], "snippet": "# GitHub - InternRobotics/REAL: [ECCV2026] Official open-source repository for REAL——Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation · GitHub\n\nInput Episode for `source_a5f8ae2053", "match_reason": "metadata:title"}, {"id": "input_4846565da5dc1656c16a439a", "type": "input", "title": "[1802.04312] A restriction estimate in $\\mathbb{R}^3$ using brooms", "path": "vault/inputs/input-input_4846565da5dc1656c16a439a.md", "status": "active", "source_ids": ["source_f366554c5c3887de7c6ad29b"], "snippet": "# [1802.04312] A restriction estimate in $\\mathbb{R}^3$ using brooms\n\nInput Episode for `source_f366554c5c3887de7c6ad29b`. The immutable Source remains authoritative.\n\n# [1802.04312] A restriction estimate in $\\mathbb{R}^3$ using brooms\n\n> ", "match_reason": "metadata:title"}]
contradiction_candidates: []
unresolved_items: []
provenance_validation: {"ok": true, "items": 1, "source_id": "source_ebf287b4d71ccdc41101466e"}
primary_source_followups: []
duplicate_findings: []
low_value_items_not_proposed: []
bundle_metrics: {"novelty_score": 0.0, "importance_score": "requires_human_judgment", "source_authority": "preprint", "evidence_quality": "good", "knowledge_reuse_count": 1, "new_object_count": 0, "updated_object_count": 1, "duplicate_count": 0, "unresolved_count": 0, "review_cost_estimate": 1, "scoring_basis": "deterministic counts and quality labels; not a calibrated probability"}
reviewed_at: null
review_reason: null
cognitive_artifact_sha256: "3cfbef2ec488e67dfdb7c73bfa9d43a114a3a286b302ff06990b3cc4d7be8e03"
migration_mode: "working-ingestion-v1"
---

# Compile bundle：arxiv.org

## 编译边界

- Provider：`codex-gpt56-m91-real-daily-v1`
- Extraction：`extraction_2b6f47c1db4a1b1191eb94de`
- 编译前召回已有对象：17
- deterministic fallback 只识别显式类型块或保留第一段逐字材料；显式块完整保留到下一个类型标记，不补齐无意义对象。

## Items and diffs

### concept-1 (update concept)

```diff
--- base:vault/memory/concept/concept_d28c0e5c8a5f864e616e2f7a.md
+++ candidate:vault/memory/concept/concept_d28c0e5c8a5f864e616e2f7a.md
@@ -1,41 +1,26 @@
 ---
 id: "concept_d28c0e5c8a5f864e616e2f7a"
 type: "concept"
-status: "working"
+status: "proposal"
 title: "三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS"
 created_at: "2026-07-27T10:47:14+08:00"
-updated_at: "2026-07-27T10:47:15+08:00"
-aliases: ["wave kinetic equation", "cubic NLS kinetic limit", "波动动理学方程", "三次 NLS 动理学极限"]
+updated_at: "2026-07-27T11:17:30+08:00"
+aliases: ["rigorous long-time wave-kinetic limit for cubic NLS", "long-time justification of wave turbulence theory", "三次 NLS 长时波动动理学严格极限", "长时波湍流理论严格证明"]
 tags: []
 domains: ["wave-turbulence", "kinetic-theory", "nonlinear-schrodinger-equation"]
 confidence: "high"
-source_ids: ["source_9ec7a0dfcdc6c43339383f13"]
+source_ids: ["source_9ec7a0dfcdc6c43339383f13", "source_ebf287b4d71ccdc41101466e"]
 relations: [{"type": "derived_from", "target_id": "source_9ec7a0dfcdc6c43339383f13", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
-change_reason: "compile bundle from source_9ec7a0dfcdc6c43339383f13"
-reflection_context: {"reflection_ids": ["reflection_039e793833ff803621c37f30"], "importance": "high", "changed_belief": "我会把波动动理学方程看作与盒尺度、耦合强度和观察时间共同定义的有效描述，而不是任意弱非线性波的普适长时方程。", "surprising": "", "connections": [{"shared_mechanism": "它与 Boltzmann--Grad 涨落层级都通过协同极限将确定性微观或介观演化连接到统计动理学方程。", "boundary": "该结果针对三次 NLS、d≥3、α∼L⁻¹ 和动理学时间的固定倍数。", "difference": "硬球结果依赖粒子低密度与碰撞半径标度；波动结果依赖大盒极限和弱非线性共振结构。"}], "open_questions": []}
-memory_tier: "working"
-epistemic_status: "unknown"
-created_by: "codex-gpt56-m91-real-daily-v1"
-updated_by: "working-ingestion-v1"
-model_provider: null
-model_version: null
-compiler_version: "codex-gpt56-m91-real-daily-v1"
-consolidation_count: 0
-last_consolidated_at: null
-last_verified_at: null
-trust_score: 0
-trust_reasons: []
-promotion_history: []
-user_authored: false
-user_locked: false
-origin_proposal_id: "proposal_bundle_b43108e78a2a6116b029"
-origin_item_id: "concept-1"
-origin_candidate_path: "vault/proposals/candidate-proposal_bundle_b43108e78a2a6116b029-concept-1.md"
-origin_candidate_sha256: "5187efb5f75f79ce8d7758660bf81ea980a482d5f945fe2f2ad3830bb94bd9ac"
-origin_cognitive_artifact_sha256: "4451ba8095f3fddeba82a9383e77828628ba8be1be6dd8738784909274a4c30c"
-memory_schema_version: 2
+change_reason: "compile bundle from source_ebf287b4d71ccdc41101466e"
+change_type: "refine"
+reflection_context: {"reflection_ids": ["reflection_46d4dcf890fae70ce354f2d4"], "importance": "high", "changed_belief": "我会把三次 NLS 的波动动理学极限理解为可覆盖 WKE 全部存活区间的条件性长时结论，而不是“只要弱非线性就能无限延长”的普适近似。", "surprising": "证明的关键不是把 Duhamel 展开机械追溯到初始时刻：对每个时间层的二点相关应以当前 WKE 谱近似并保留高阶累积量的历史结构，才能消除表面同阶的伪主项。", "connections": [{"shared_mechanism": "它与既有三次 NLS 波动动理学概念都通过大盒与弱非线性协同极限，把随机 NLS 的统计量连接到 WKE。", "boundary": "定理针对 d≥3、随机 Schwartz 初值、α=L^-γ（γ∈(0,1)，端点另有几何条件）且 τ*<τmax；WKE 可有限时爆破，近似不声称跨越该点。", "difference": "既有条目概括早期的固定动理学窗口；本文用分层累积量、正向时间结构与二点相关闭合，将窗口推进至 WKE 的整个存活区间。"}], "open_questions": ["若 WKE 全局有界，τ* 随 L 增长的最优速率是什么；在 WKE 爆破后应以何种弱解或可观测量修改近似？"]}
+proposed_status: "working"
 ---
 
 # 三次 NLS 的波动动理学严格极限 / rigorous wave-kinetic limit for cubic NLS
 
 对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性强度 α→0 且 α 与 L 满足论文指定的 α∼L⁻¹ 标度时，其统计长时行为可在动理学时间 Tkin∼α⁻² 的固定倍数内由波动动理学方程近似描述。该结论依赖具体方程、标度和时间窗口，不是所有非线性波系统的无条件定律。
+
+## 新增来源材料
+
+- `source_ebf287b4d71ccdc41101466e`：对 d≥3 的大盒三次非线性 Schrödinger 方程，在 L→∞、弱非线性 α=L^-γ（γ∈(0,1)；γ=1 需通用矩形环面条件）与随机 Schwartz 初值的协同极限下，随机 NLS 的二点统计可在任意固定 τ*<τmax 的 [0,τ*Tkin] 区间逼近齐次 WKE；τmax 是 WKE 的最大存在时间。该结论覆盖 WKE 的存活区间而非跨越可能的有限时爆破，也不能外推到任意 NLS 初值、维度或无限时间。
```
