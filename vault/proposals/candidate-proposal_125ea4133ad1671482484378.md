---
id: "claim_wechat_expo_ft_reliability_motivation_20260716"
title: "该文称仅靠模仿学习难以达到机器人长期自主所需的高可靠性，需让系统针对目标场景自主迭代优化策略"
tags: ["robotics", "imitation-learning", "reliability"]
domains: ["robotics", "reinforcement-learning"]
confidence: "medium"
applicability: ["Finn/PI 研讨会动机", "99.9%+ 可靠性目标表述"]
uncertainty: "为研讨会转述与观点性论述；可靠性阈值未给出严格实验定义。"
evidence: [{"evidence_id": "ev_769", "evidence_kind": "quote", "source_id": "source_8b41a014bee47c4239a2fa81", "content_id": "content_15201becf4f645da31cfd5c6c3c5bc10dec18547711dedd2c5fa9bf99fcdf1b6", "extraction_id": "extraction_27a3915bf1f44e95bc06bbae", "input_sha256": "15201becf4f645da31cfd5c6c3c5bc10dec18547711dedd2c5fa9bf99fcdf1b6", "span_start": 769, "span_end": 795, "original_text": "仅依靠模仿学习几乎无法直接训练出高可靠性的机器人策略", "section": "IL 不足", "stance": "supports", "verification_status": "verified", "reason": "文内对模仿学习局限的核心判断。"}, {"evidence_id": "ev_1021", "evidence_kind": "quote", "source_id": "source_8b41a014bee47c4239a2fa81", "content_id": "content_15201becf4f645da31cfd5c6c3c5bc10dec18547711dedd2c5fa9bf99fcdf1b6", "extraction_id": "extraction_27a3915bf1f44e95bc06bbae", "input_sha256": "15201becf4f645da31cfd5c6c3c5bc10dec18547711dedd2c5fa9bf99fcdf1b6", "span_start": 1021, "span_end": 1088, "original_text": "99.9%+（多个9s） 的可靠性标准、让机器人能够稳定落地到对可靠性要求严苛的真实场景，就必须让人工智能系统针对目标场景自主优化策略", "section": "可靠性目标", "stance": "supports", "verification_status": "verified", "reason": "文内对落地可靠性标准与自主迭代的表述。"}]
type: "claim"
status: "proposal"
created_at: "2026-07-16T11:05:00+08:00"
updated_at: "2026-07-16T11:05:00+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "批量导入 EXPO-FT / 离线 VLA RL 研讨会；等待人工核验"
source_ids: ["source_8b41a014bee47c4239a2fa81"]
relations: [{"type": "derived_from", "target_id": "source_8b41a014bee47c4239a2fa81", "reason": "human five 转载 Chelsea Finn & Perry Dong 研讨会：离线迭代 RL 与 EXPO-FT 在线 VLA 微调；原论文未 capture"}]
---

# 可靠性动机

人工迭代数据集遇瓶颈；模型自主迭代可定位数据缺口。
