---
id: "claim_wechat_im_rl_texplore_vanir_20260716"
title: "该文介绍 texplore-vanir：结合模型预测方差奖励与状态空间新颖性奖励，驱动机器人好奇探索并加速模型学习"
tags: ["curiosity", "model-based-rl", "exploration"]
domains: ["robotics", "reinforcement-learning"]
confidence: "medium"
applicability: ["基于模型 RL 探索", "Nao 机器人按钮任务实验叙述"]
uncertainty: "实验结论（7/13 vs 0/13）来自综述转述 Hester & Stone 2017。"
evidence: [{"evidence_id": "ev_6062", "evidence_kind": "quote", "source_id": "source_91199da18f239c48bbcdd49f", "content_id": "content_0a6a4a4981b16af3d9e9decc20cb50cdc254ce7a2383bcf0381497839eb903b3", "extraction_id": "extraction_b0ef424e09475b568376445b", "input_sha256": "0a6a4a4981b16af3d9e9decc20cb50cdc254ce7a2383bcf0381497839eb903b3", "span_start": 6062, "span_end": 6125, "original_text": "Variance-And-Novelty-Intrinsic-Rewards algorithm，texplore-vanir", "section": "算法命名", "stance": "supports", "verification_status": "verified", "reason": "文内对 texplore-vanir 算法全称与简称。"}, {"evidence_id": "ev_7548", "evidence_kind": "quote", "source_id": "source_91199da18f239c48bbcdd49f", "content_id": "content_0a6a4a4981b16af3d9e9decc20cb50cdc254ce7a2383bcf0381497839eb903b3", "extraction_id": "extraction_b0ef424e09475b568376445b", "input_sha256": "0a6a4a4981b16af3d9e9decc20cb50cdc254ce7a2383bcf0381497839eb903b3", "span_start": 7548, "span_end": 7937, "original_text": "变异报酬，纳入智能体的计划模型中：\n\n其中 v 是一个系数，决定这个奖励应该有多大。这种奖励将驱使智能体达到一种状态反应中，而此时其模型尚未收敛到全局动态的单一假设。因此会出现智能体的所有模型都做出错误预测的情况。对于 texplore-vaniruses 的随机森林模型来说，当它的模型不得不将自己的预测一般化到离它所训练的经验更远的地方时，就更容易出错。引入 2）对应的内在动机，在特征空间中，从一个给定的状态动作和模型训练过的最近的动作之间的 L1 距离。这个距离是针对每个动作分别计算的。对于一个动作 a，X_a 是该动作被采取的所有状态的集合。那么，δ(s，a) 是从给定状态 s 到最近的行动 a 被采取的状态的最小 L1 距离：\n\n其中每个特征被归一化为 0 到 1 的范围。对于布尔特征，假定真和假之间的距离为 1。定义一个奖励函数（Novelty-reward", "section": "双重内在奖励", "stance": "supports", "verification_status": "verified", "reason": "文内对方差奖励与新颖性奖励的定义段落。"}]
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

# texplore-vanir

方差奖励探索模型不确定区域；新颖性奖励远离已访问状态。
