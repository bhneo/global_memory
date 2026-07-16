---
id: "claim_wechat_brain_cerebellum_layered_collection_20260716"
title: "该文主张「大脑+小脑」分层：场内真机遥操训练小脑执行，场外 Ego 众包训练大脑决策"
tags: ["brain-cerebellum", "vla", "vlm"]
domains: ["robotics", "embodied-ai"]
confidence: "low"
applicability: ["场内/场外双范式架构讨论", "长程任务 vs 精细操作数据分工"]
uncertainty: "为数据堂提出的框架性主张；与具体模型架构映射为类比性表述。"
evidence: [{"evidence_id": "ev_2274", "evidence_kind": "quote", "source_id": "source_cda5a1b9e036598aff53e5be", "content_id": "content_4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "extraction_id": "extraction_c1cb6fe720013eb77dfa08c9", "input_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "span_start": 2274, "span_end": 2284, "original_text": "端侧小脑」的分层架构", "section": "分层架构", "stance": "supports", "verification_status": "verified", "reason": "文内对大脑/小脑分层类比。"}, {"evidence_id": "ev_2337", "evidence_kind": "quote", "source_id": "source_cda5a1b9e036598aff53e5be", "content_id": "content_4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "extraction_id": "extraction_c1cb6fe720013eb77dfa08c9", "input_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "span_start": 2337, "span_end": 2518, "original_text": "场内采集聚焦短程技能、实时执行与毫米级精度（如抓取、精密装配等）。\n\n这类动作对延迟极度敏感，因此必须部署在端侧，通过VLA模型实现实时响应。\n\n对应的核心数据需求，是电机信号、力矩、力反馈、高频控制指令等能反映「执行细节」的信息。\n\n而最佳采集方式正是真机遥操，只有通过真实机器人的交互才能获取最精准的力触觉反馈，为特定机器人打造稳定、确定、可复现的「肌肉记忆", "section": "场内小脑", "stance": "supports", "verification_status": "verified", "reason": "文内对场内遥操服务小脑训练的说明。"}, {"evidence_id": "ev_2620", "evidence_kind": "quote", "source_id": "source_cda5a1b9e036598aff53e5be", "content_id": "content_4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "extraction_id": "extraction_c1cb6fe720013eb77dfa08c9", "input_sha256": "4fb3166e9d3eca8b3c582dfeb6313482c29134b47423321cdc6c76c407611aa5", "span_start": 2620, "span_end": 2778, "original_text": "场外采集聚焦长程任务与动态决策（如整理房间、设备巡检等）。\n\n这类动作不需要毫秒级延迟，更需要多样化的场景覆盖，因此适合部署在云端，支撑VLM大模型持续迭代。\n\n对应的核心数据需求，是周边环境、决策逻辑、实际人类操作，最佳方式是使用众包方式的Ego采集，无需真机即可快速覆盖海量真实场景，让大脑理解 「做什么、为什么", "section": "场外大脑", "stance": "supports", "verification_status": "verified", "reason": "文内对场外 Ego 服务大脑决策的说明。"}]
type: "claim"
status: "proposal"
created_at: "2026-07-16T01:11:00+08:00"
updated_at: "2026-07-16T01:11:00+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "批量导入具身数据采集软文；等待人工核验"
source_ids: ["source_cda5a1b9e036598aff53e5be"]
relations: [{"type": "derived_from", "target_id": "source_cda5a1b9e036598aff53e5be", "reason": "由新智元对数据堂具身数据采集框架的软文归纳；特斯拉/OpenAI 路线为二手引述"}]
---

# 大脑+小脑分层

场内遥操→执行；场外 Ego→决策。
