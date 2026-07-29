---
id: "concept_generalist_cross_embodiment_vla"
type: "concept"
status: "working"
title: "跨本体通用 VLA 策略"
created_at: "2026-07-19T03:01:52+08:00"
updated_at: "2026-07-28T16:30:35+08:00"
aliases: ["generalist cross-embodiment VLA", "cross-embodiment policy"]
tags: []
domains: ["embodied-ai", "vla", "cross-embodiment", "humanoid"]
confidence: "medium"
source_ids: ["source_34d6513b0522739d0b25e303", "source_233c4bef3a727389ddf81ae2"]
relations: [{"type": "derived_from", "target_id": "source_34d6513b0522739d0b25e303", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_staged_cross_embodiment_alignment", "reason": "跨本体通用策略需要处理共享表征与本体专属控制之间的对齐。", "confidence": "high", "created_by": "agent-semantic-weekly-gpt56sol-v1", "status": "working"}, {"type": "related_to", "target_id": "concept_predictive_vla_deployment", "reason": "跨本体动作语义解决控制接口错位，预测式部署监督解决时间表示错位；二者共同约束泛化但不能互相替代。", "confidence": "high", "created_by": "codex-strong-model-m91-weekly-v3", "status": "proposal"}, {"type": "related_to", "target_id": "concept_progressive_vla_demonstration_curriculum", "reason": "共享动作坐标决定异质数据能否对齐，课程组织决定已对齐数据以何种复杂度进入学习。", "confidence": "medium", "created_by": "codex-strong-model-m91-weekly-v3", "status": "proposal"}]
change_reason: "compile bundle from source_233c4bef3a727389ddf81ae2"
uncertainty: "通用性取决于训练数据、动作空间和具体部署支持，不能从项目定位推出任意机器人上的零样本泛化。"
memory_tier: "working"
epistemic_status: "unknown"
created_by: "agent-semantic-weekly-gpt56sol-v1"
updated_by: "trustworthy-consolidation-v2"
model_provider: null
model_version: null
compiler_version: "agent-semantic-weekly-gpt56sol-v1"
consolidation_count: 9
last_consolidated_at: "2026-07-28T16:30:35+08:00"
last_verified_at: "2026-07-19T03:27:33+08:00"
trust_score: 0
trust_reasons: []
promotion_history: []
user_authored: false
user_locked: false
origin_proposal_id: "proposal_bundle_b42edda3bcd8367515cd"
origin_item_id: "concept-1"
origin_candidate_path: "vault/proposals/candidate-proposal_bundle_b42edda3bcd8367515cd-concept-1.md"
origin_candidate_sha256: "53554fe46394c350e9f4d04c35326fd3a8a97dec6ff9e54c60121411cfe001df"
memory_schema_version: 2
last_consolidation_id: "consolidation_486d6d1b7117d7f5b0accc82"
evidence: []
change_history: [{"change_type": "metadata_only", "previous_statement": "# 跨本体通用 VLA 策略\n\n以统一的视觉、语言和状态输入接口生成连续机器人动作，并通过跨机器人形态的数据与动作表示支持多任务、多环境迁移。", "new_statement": "# 跨本体通用 VLA 策略\n\n以统一的视觉、语言和状态输入接口生成连续机器人动作，并通过跨机器人形态的数据与动作表示支持多任务、多环境迁移。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_34d6513b0522739d0b25e303", "trigger_source": "source_34d6513b0522739d0b25e303", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# 跨本体通用 VLA 策略\n\n以统一的视觉、语言和状态输入接口生成连续机器人动作，并通过跨机器人形态的数据与动作表示支持多任务、多环境迁移。", "new_statement": "# 跨本体通用 VLA 策略\n\n以统一的视觉、语言和状态输入接口生成连续机器人动作，并通过跨机器人形态的数据与动作表示支持多任务、多环境迁移。", "changed_fields": ["source_ids", "evidence", "last_verified_at"], "reason": "compile bundle from source_34d6513b0522739d0b25e303", "trigger_source": "source_34d6513b0522739d0b25e303", "evidence_added": []}, {"change_type": "metadata_only", "previous_statement": "# 跨本体通用 VLA 策略\n\n以统一的视觉、语言和状态输入接口生成连续机器人动作，并通过跨机器人形态的数据与动作表示支持多任务、多环境迁移。", "new_statement": "# 跨本体通用 VLA 策略\n\n以统一的视觉、语言和状态输入接口生成连续机器人动作，并通过跨机器人形态的数据与动作表示支持多任务、多环境迁移。", "changed_fields": ["aliases"], "reason": "compile bundle from source_34d6513b0522739d0b25e303", "trigger_source": "source_34d6513b0522739d0b25e303", "evidence_added": []}, {"change_type": "refine", "previous_statement": "# 跨本体通用 VLA 策略\n\n以统一的视觉、语言和状态输入接口生成连续机器人动作，并通过跨机器人形态的数据与动作表示支持多任务、多环境迁移。", "new_statement": "# 跨本体通用 VLA 策略\n\n以统一的视觉、语言和状态输入接口生成连续机器人动作，并通过跨机器人形态的数据与动作表示支持多任务、多环境迁移。\n\n## 新增来源材料\n\n- `source_233c4bef3a727389ddf81ae2`：跨本体通用 VLA 不仅需要统一输入骨干，还需要声明可跨本体共享的动作语义及其失效边界。相对末端执行器变化可为人类手部运动与部分机器人操作提供弱共享坐标，但全身接触、灵巧手内部自由度、动力学与硬件能力仍需本体专属接口；未来语义—几何监督只有与动作覆盖和本体多样性共同设计时，才可能支持真实部署泛化。", "changed_fields": [], "reason": "compile bundle from source_233c4bef3a727389ddf81ae2", "trigger_source": "source_233c4bef3a727389ddf81ae2", "evidence_added": []}]
change_type: "refine"
reflection_context: {"reflection_ids": ["reflection_0db16c2a58084d442087245e", "reflection_e7fd4c90ed4ee681fb6fdb80"], "importance": "weekly", "changed_belief": "此前跨本体通用 VLA 主要被描述为数据混合和统一接口问题；该材料进一步表明，动作坐标系本身决定不同本体的数据能否形成一致监督。\n此前面向部署的预测式 VLA 更聚焦未来状态预测；该工作表明预测目标只有与动作覆盖和本体多样性共同设计时，才可能转化为实际控制收益。", "surprising": "官方说明把相对 EEF 表示列为跨本体表现的关键因素，而不是只把改进归因于更大的 VLM 或更多数据。\n未来预测并非直接重建完整动力学，而是用视频语义与深度几何蒸馏形成双查询代理目标，说明实用世界监督可以是任务相关的部分预测。", "connections": [{"shared_mechanism": "通过选择跨本体更稳定的中间监督变量，减少形态差异进入共享表示", "boundary": "相对 EEF 只适用于可映射到末端位姿变化的操作，不覆盖全身接触、灵巧手内部自由度或不可比动作空间", "difference": "GR00T 共享的是相对动作坐标，跨本体世界监督共享的是未来场景变化；前者靠近控制输出，后者靠近环境表征"}, {"shared_mechanism": "都用未来表征为当前动作学习增加前瞻性监督，同时避免要求完整环境生成", "boundary": "代理目标改善表示不等于模型能准确模拟动作后果，也不能单独证明闭环部署可靠", "difference": "LingBot 的双查询蒸馏面向语义和几何未来目标；触觉世界模型面向接触子目标并配有高频反应回路"}], "open_questions": ["相对 EEF、对象中心动作和未来世界表示在不同任务中各自承担多少跨本体迁移收益？", "未来语义、深度几何与接触状态三类预测目标应如何按任务阶段分配权重？"]}
proposed_status: "working"
---

# 跨本体通用 VLA 策略

以统一的视觉、语言和状态输入接口生成连续机器人动作，并通过跨机器人形态的数据与动作表示支持多任务、多环境迁移。

## 新增来源材料

- `source_233c4bef3a727389ddf81ae2`：跨本体通用 VLA 不仅需要统一输入骨干，还需要声明可跨本体共享的动作语义及其失效边界。相对末端执行器变化可为人类手部运动与部分机器人操作提供弱共享坐标，但全身接触、灵巧手内部自由度、动力学与硬件能力仍需本体专属接口；未来语义—几何监督只有与动作覆盖和本体多样性共同设计时，才可能支持真实部署泛化。
