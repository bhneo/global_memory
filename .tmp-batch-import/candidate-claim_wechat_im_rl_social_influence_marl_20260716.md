---
id: "claim_wechat_im_rl_social_influence_marl_20260716"
title: "该文介绍多智能体「社会影响」内在奖励：用反事实行动评估对同伴行为的因果影响，据称在 Cleanup/Harvest 中优于基线"
tags: ["multi-agent-rl", "social-influence", "communication"]
domains: ["reinforcement-learning", "multi-agent-systems"]
confidence: "medium"
applicability: ["MARL 合作困境", "MOA 模块与通信协议学习"]
uncertainty: "因果影响≈互信息的论述为综述归纳；Jaques et al. 2018 细节需回原文。"
evidence: [{"evidence_id": "ev_9147", "evidence_kind": "quote", "source_id": "source_91199da18f239c48bbcdd49f", "content_id": "content_0a6a4a4981b16af3d9e9decc20cb50cdc254ce7a2383bcf0381497839eb903b3", "extraction_id": "extraction_b0ef424e09475b568376445b", "input_sha256": "0a6a4a4981b16af3d9e9decc20cb50cdc254ce7a2383bcf0381497839eb903b3", "span_start": 9147, "span_end": 9342, "original_text": "Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning\n论文地址：https://arxiv.org/pdf/1810.08647.pdf\n这篇文章聚焦的是解决 RL 跨多个领域学习的问题，即多主体强化学习（multi-agent reinforcement learning", "section": "社会影响论文", "stance": "supports", "verification_status": "verified", "reason": "文内对社会影响 MARL 论文的标题级引述。"}, {"evidence_id": "ev_9475", "evidence_kind": "quote", "source_id": "source_91199da18f239c48bbcdd49f", "content_id": "content_0a6a4a4981b16af3d9e9decc20cb50cdc254ce7a2383bcf0381497839eb903b3", "extraction_id": "extraction_b0ef424e09475b568376445b", "input_sha256": "0a6a4a4981b16af3d9e9decc20cb50cdc254ce7a2383bcf0381497839eb903b3", "span_start": 9475, "span_end": 9487, "original_text": "反事实推理法评估因果影响", "section": "反事实因果", "stance": "supports", "verification_status": "verified", "reason": "文内对反事实评估因果影响机制的核心说明。"}]
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

# 社会影响 MARL

奖励对其他智能体行为有因果影响的动作；可鼓励合作与通信。
