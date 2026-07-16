---
id: "claim_wechat_im_rl_hdqn_hierarchy_20260716"
title: "该文介绍 Kulkarni 的 h-DQN：元控制器最大化外在奖励选目标，控制器以内在奖励学习达成子目标的原子动作"
tags: ["h-DQN", "hierarchical-rl", "goal-driven"]
domains: ["reinforcement-learning", "deep-learning"]
confidence: "medium"
applicability: ["稀疏奖励环境", "分层时间尺度 Q 学习"]
uncertainty: "架构描述来自综述；超参与实验细节需回 NIPS 2016 原文。"
evidence: [{"evidence_id": "ev_4283", "evidence_kind": "quote", "source_id": "source_91199da18f239c48bbcdd49f", "content_id": "content_0a6a4a4981b16af3d9e9decc20cb50cdc254ce7a2383bcf0381497839eb903b3", "extraction_id": "extraction_b0ef424e09475b568376445b", "input_sha256": "0a6a4a4981b16af3d9e9decc20cb50cdc254ce7a2383bcf0381497839eb903b3", "span_start": 4283, "span_end": 4305, "original_text": "hierarchical-DQN，h-DQN", "section": "h-DQN 引入", "stance": "supports", "verification_status": "verified", "reason": "文内对 h-DQN 框架名称与提出者。"}, {"evidence_id": "ev_4820", "evidence_kind": "quote", "source_id": "source_91199da18f239c48bbcdd49f", "content_id": "content_0a6a4a4981b16af3d9e9decc20cb50cdc254ce7a2383bcf0381497839eb903b3", "extraction_id": "extraction_b0ef424e09475b568376445b", "input_sha256": "0a6a4a4981b16af3d9e9decc20cb50cdc254ce7a2383bcf0381497839eb903b3", "span_start": 4820, "span_end": 4951, "original_text": "元控制器）接受状态并选择新的目标；（b）下层模块（控制器）同时使用状态和所选目标来选择操作，直到达到目标或事件终止为止。\n之后，定义元控制器选择另一个目标，并重复步骤（a-b）。在不同的时间尺度上使用随机梯度下降训练模型，以优化预期的未来内在（控制器）和外在奖励", "section": "分层奖励分工", "stance": "supports", "verification_status": "verified", "reason": "文内对元控制器与控制器奖励分工的说明。"}]
type: "claim"
status: "proposal"
created_at: "2026-07-16T10:42:00+08:00"
updated_at: "2026-07-16T10:42:00+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "批量导入内在动机×RL 综述；等待人工核验"
source_ids: ["source_91199da18f239c48bbcdd49f"]
relations: [{"type": "derived_from", "target_id": "source_91199da18f239c48bbcdd49f", "reason": "Synced 机器之心 2020 综述：内在动机在 RL 中的应用；引述 Baldassarre/Barto/h-DQN/texplore-vanir/MARL 等文献"}]
---

# h-DQN

顶层选目标（外在）；底层学动作（内在）；稀疏反馈下先学子技能。
