---
id: "claim_wechat_rt2_vlm_prior_not_robot_scaling_20260716"
title: "该文以 RT-2 为例称关键在联网规模 VLM 先验加有限机器人示范，而非继续堆机器人数据"
tags: ["rt-2", "vla", "pretraining"]
domains: ["robotics", "machine-learning"]
confidence: "medium"
applicability: ["RT-2 / Open X-Embodiment 案例讨论", "robotics scaling 变量辨析"]
uncertainty: "为作者对 DeepMind 博客的解读；与原始论文细节需回原文核验。"
evidence: [{"evidence_id": "ev_897", "evidence_kind": "quote", "source_id": "source_0a113baae7ce4d1ab78da1a3", "content_id": "content_5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "extraction_id": "extraction_c6ecc197e026c4f58b633b83", "input_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "span_start": 897, "span_end": 1008, "original_text": "RT-2 是一个很好的例子。它的动作数据只来自 13 台机器人、17 个月、一间 office kitchen，听起来并不算多。真正让它上了一个台阶的，恰恰是接入了互联网规模的视觉语言预训练，跟机器人动作数据的增量关系不大", "section": "RT-2 案例", "stance": "supports", "verification_status": "verified", "reason": "文内对 RT-2 数据量与能力来源的分析。"}, {"evidence_id": "ev_1039", "evidence_kind": "quote", "source_id": "source_0a113baae7ce4d1ab78da1a3", "content_id": "content_5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "extraction_id": "extraction_c6ecc197e026c4f58b633b83", "input_sha256": "5a002d5dff7b4a4ff65cc54dc1c4aee2bf4b78acc3af4defde572c2d1ee8fe0c", "span_start": 1039, "span_end": 1071, "original_text": "web 预训练的视觉语言模型，再结合 RT-1 的机器人示范数据", "section": "VLM 先验", "stance": "supports", "verification_status": "verified", "reason": "文内对 RT-2 训练组成的归纳。"}]
type: "claim"
status: "proposal"
created_at: "2026-07-16T01:19:00+08:00"
updated_at: "2026-07-16T01:19:00+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "批量导入具身数据问题分析文；等待人工核验"
source_ids: ["source_0a113baae7ce4d1ab78da1a3"]
relations: [{"type": "derived_from", "target_id": "source_0a113baae7ce4d1ab78da1a3", "reason": "由杜伦文/青稞具身智能专栏归纳；引述 RT-2、Re-Mix、Covariant 等为二手分析"}]
---

# RT-2 启示

互联网 VLM 先验 + 有限动作数据；非纯 robot data scaling。
