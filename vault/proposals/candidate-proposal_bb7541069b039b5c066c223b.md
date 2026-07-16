---
id: "claim_wechat_offline_rl_advantage_bc_20260716"
title: "该文介绍离线框架：MC 回归估计任务剩余时长作进度代理，二值化优势条件 BC 迭代微调 VLA；意式咖啡成功率 40%→90%+、连续运行 13 小时"
tags: ["offline-rl", "VLA", "advantage-conditioning"]
domains: ["robotics", "reinforcement-learning"]
confidence: "medium"
applicability: ["长时序 espresso/叠衣/纸箱任务", "DAgger 式人工修正"]
uncertainty: "数值来自研讨会转述；离线框架名称文中留空；需回原文/视频核验。"
evidence: [{"evidence_id": "ev_2109", "evidence_kind": "quote", "source_id": "source_8b41a014bee47c4239a2fa81", "content_id": "content_15201becf4f645da31cfd5c6c3c5bc10dec18547711dedd2c5fa9bf99fcdf1b6", "extraction_id": "extraction_27a3915bf1f44e95bc06bbae", "input_sha256": "15201becf4f645da31cfd5c6c3c5bc10dec18547711dedd2c5fa9bf99fcdf1b6", "span_start": 2109, "span_end": 2420, "original_text": "蒙特卡洛（Monte Carlo）回归方式训练，而非时序差分（TD）学习。训练目标为简单的有监督回归任务，该设计易于拓展至大模型与大规模离线数据集。\n\n基于优势值条件约束的策略监督学习：训练策略时引入优势值作为条件，以此区分当前动作是推动任务向前推进、停滞不前，还是造成任务倒退。该方法命名为基于二值化优势值的行为克隆（Advantage-Conditioned BC），仅适用于离线训练。\n\n整套完整离线训练流程如下：\n\n利用大规模预训练数据集完成VLA模型基础预训练；\n\n离线回放机器人策略轨迹，采集人工修正故障场景数据；\n\n基于全部离线数据训练价值函数，输出任务剩余时长作为进度代理指标（progress proxy", "section": "价值函数设计", "stance": "supports", "verification_status": "verified", "reason": "文内对 MC 价值函数与进度代理的说明。"}, {"evidence_id": "ev_4328", "evidence_kind": "quote", "source_id": "source_8b41a014bee47c4239a2fa81", "content_id": "content_15201becf4f645da31cfd5c6c3c5bc10dec18547711dedd2c5fa9bf99fcdf1b6", "extraction_id": "extraction_27a3915bf1f44e95bc06bbae", "input_sha256": "15201becf4f645da31cfd5c6c3c5bc10dec18547711dedd2c5fa9bf99fcdf1b6", "span_start": 4328, "span_end": 4339, "original_text": "40%提升至90%以上", "section": "咖啡成功率", "stance": "supports", "verification_status": "verified", "reason": "文内对核心咖啡任务量化结果。"}]
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

# 离线迭代 RL

优势条件 BC 仅离线；13h 回放与平均 2× 吞吐量提升。
