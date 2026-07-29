---
id: "concept_2ce226e08d585158c1dfbb18"
type: "concept"
status: "working"
title: "接触反馈应区分短时反应、事件记忆与概率后验"
created_at: "2026-07-24T18:06:12+08:00"
updated_at: "2026-07-27T19:04:24+08:00"
aliases: ["Late Reactive Force Injection", "LIFT", "反应式力注入 VLA 后训练"]
tags: []
domains: ["vla", "force-control", "contact-rich-manipulation"]
confidence: "medium"
source_ids: ["source_4e06d1b1cdcd0d07eff47909", "source_1ee2c3fae53a9d05689cd143"]
relations: [{"type": "derived_from", "target_id": "source_4e06d1b1cdcd0d07eff47909", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_637cf7264723c03955c719e2", "reason": "两者都使用交互中的附加信号缓解视觉歧义；本概念采用显式力记忆和反应分支，既有概念采用遥操作跟踪偏差这一隐式 proxy。", "confidence": "medium", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_c37ccf2640da63192432d5d5", "reason": "LIFT 的近期力窗口服务动作块内反应，FM-VLA 的压缩力历史服务非 Markov 接触事件记忆；两者共享 wrench 信号，但时间范围和功能边界不同。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-v2", "status": "proposal"}, {"type": "related_to", "target_id": "concept_bb69fa188e0417143c3277cf", "reason": "力历史与姿态粒子后验都缓解接触状态的部分可观测性；前者编码已发生的事件，后者表示当前几何不确定性，不能互相替代。", "confidence": "high", "created_by": "codex-gpt-5.6-sol-m91-weekly-v2", "status": "proposal"}]
change_reason: "compile bundle from source_1ee2c3fae53a9d05689cd143"
reflection_context: {"reflection_ids": ["reflection_438aaa4e8fa10fc299c05d87", "reflection_bd1bc1b00ef5304ee9d29e9c"], "importance": "weekly", "changed_belief": "我会要求接触融合方法明确说明后验表示、仿真前向模型和新几何/环境下的适用边界，而不把仿真推断自动等同于无训练泛化。\n我会把力传感视为接触事件进度的专用时序记忆，而不把它当成对视觉记忆或一般 VLA 长时推理的无条件替代。", "surprising": "", "connections": [{"shared_mechanism": "两者都用视觉和接触信息缩小接触操作中的状态不确定性。", "boundary": "本文限于 peg-in-hole、粒子 belief、深度和 force/torque 接触证据以及仿真前向模型。", "difference": "深度单独估计输出单一几何匹配；本文用 simulation-based inference 对多个候选位姿加权。"}, {"shared_mechanism": "两者都以额外时序表征弥补单帧 VLA 的 Markov 假设。", "boundary": "本文限于可获得的 wrench 信号、VAE 压缩、三个记忆依赖任务和论文评测。", "difference": "视觉记忆存储图像帧且可能模糊昂贵；本文将接触/重复事件编码为紧凑 force token。"}], "open_questions": ["接触模型失配和未见材料摩擦下，后验校准如何影响闭环插入成功率？", "传感漂移、不同末端执行器和新接触材料下，force memory 的后验事件语义如何校准？"]}
memory_tier: "working"
epistemic_status: "unknown"
created_by: "codex-gpt56-m91-real-daily-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "codex-gpt56-m91-real-daily-v1"
consolidation_count: 2
last_consolidated_at: "2026-07-27T19:04:24+08:00"
last_verified_at: null
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_22e03e8c0d0697f12bc0"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_22e03e8c0d0697f12bc0-concept-1.md"
origin_candidate_sha256: "b2388e92015056e7b66a969bfa97c7d87752f7109cfbaf4954b5921bad16185c"
memory_schema_version: 2
last_consolidation_id: "consolidation_1d55cc9b273ff37b0682fb37"
change_type: "refine"
proposed_status: "working"
change_history: [{"change_type": "refine", "previous_statement": "# 保留视觉语言先验的块内反应式力注入\n\n对预训练视觉语言动作策略，可在保留慢速视觉语言前缀的同时，以因果近期六维末端力记忆驱动并行反应动作分支，并用零初始化残差使后训练前的输出与基线一致；在线纠正数据用于覆盖当前策略遇到的接触失败状态，但效果受传感延迟、任务接触动力学和在线数据质量限制。", "new_statement": "# 保留视觉语言先验的块内反应式力注入\n\n对预训练视觉语言动作策略，可在保留慢速视觉语言前缀的同时，以因果近期六维末端力记忆驱动并行反应动作分支，并用零初始化残差使后训练前的输出与基线一致；在线纠正数据用于覆盖当前策略遇到的接触失败状态，但效果受传感延迟、任务接触动力学和在线数据质量限制。\n\n## 新增来源材料\n\n- `source_1ee2c3fae53a9d05689cd143`：预训练 VLA 的接触反馈接口应区分短时反应、事件记忆与不确定性估计。LIFT 用近期六维力在动作块内做因果反应；FM-VLA 把更长的 wrench 历史压缩为 force-memory tokens，以保留视觉难以区分的接触事件和重复进度；BayesContact 则用深度与接触似然维护物体姿态粒子后验。三者共同弥补纯视觉在接触状态中的可观测性缺口，但短时残差修正、历史压缩和概率信念不能相互替代，且都受传感延迟、模型失配和任务分布限制。", "changed_fields": [], "reason": "compile bundle from source_1ee2c3fae53a9d05689cd143", "trigger_source": "source_1ee2c3fae53a9d05689cd143", "evidence_added": []}]
---

# 保留视觉语言先验的块内反应式力注入

对预训练视觉语言动作策略，可在保留慢速视觉语言前缀的同时，以因果近期六维末端力记忆驱动并行反应动作分支，并用零初始化残差使后训练前的输出与基线一致；在线纠正数据用于覆盖当前策略遇到的接触失败状态，但效果受传感延迟、任务接触动力学和在线数据质量限制。

## 新增来源材料

- `source_1ee2c3fae53a9d05689cd143`：预训练 VLA 的接触反馈接口应区分短时反应、事件记忆与不确定性估计。LIFT 用近期六维力在动作块内做因果反应；FM-VLA 把更长的 wrench 历史压缩为 force-memory tokens，以保留视觉难以区分的接触事件和重复进度；BayesContact 则用深度与接触似然维护物体姿态粒子后验。三者共同弥补纯视觉在接触状态中的可观测性缺口，但短时残差修正、历史压缩和概率信念不能相互替代，且都受传感延迟、模型失配和任务分布限制。
