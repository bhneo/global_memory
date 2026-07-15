---
id: "claim_wechat_gigaworld_vlm_negative_corr_20260715"
title: "该文转述 GigaWorld-1 结论：用 VLM 给世界模型物理一致性打分会与人工金标准负相关"
tags: ["world-model", "evaluation", "vlm", "gigaworld"]
domains: ["world-models", "robot-learning"]
confidence: "low"
applicability: ["作者对 GigaWorld-1 / 极佳 CVPR World Model Track 的解读", "以 rollout 成功失败与真机对齐为金标准的评估设定"]
uncertainty: "负相关结论经公众号转述 GigaWorld-1；具体 VLM 型号、样本量与相关系数未在文中给出；GigaWorld-1 原文未 capture。"
evidence: [{"evidence_id": "ev_2336", "evidence_kind": "quote", "source_id": "source_2d4f3a7d3525782c8ff503ee", "content_id": "content_2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "extraction_id": "extraction_e3377b150ecb9c199dd5bc48", "input_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "span_start": 2336, "span_end": 2448, "original_text": "王啸峰在访谈中给的答案，是一个「金标准」（golden metric）：世界模型里 rollout 出来的成功和失败，必须和真机 rollout 的成功失败完全对上。这边成功，那边也成功；这边失败，那边就一定失败。就这么硬。", "section": "金标准定义", "stance": "supports", "verification_status": "verified", "reason": "作者转述的 golden metric 定义。"}, {"evidence_id": "ev_2734", "evidence_kind": "quote", "source_id": "source_2d4f3a7d3525782c8ff503ee", "content_id": "content_2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "extraction_id": "extraction_e3377b150ecb9c199dd5bc48", "input_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "span_start": 2734, "span_end": 2811, "original_text": "最典型的就是 VLM。现在很多人图省事，直接拿一个多模态大模型去给世界模型的物理一致性打分。极佳实测的结论是：VLM 打出来的这个分，跟金标准是负相关的。", "section": "VLM 负相关", "stance": "supports", "verification_status": "verified", "reason": "作者转述 GigaWorld-1 对 VLM 打分的结论。"}, {"evidence_id": "evp_36296", "evidence_kind": "paraphrase", "source_id": "source_2d4f3a7d3525782c8ff503ee", "input_sha256": "2eb0a83af431f3e7da3ab65e43a3ea289ca86fac3c0cd82065b933a36047834e", "section": "来源层级", "interpretation": "结论来自对 GigaWorld-1 与访谈的二次解读", "stance": "context", "verification_status": "verified", "reason": "需回原文核验指标与实验设置。"}]
type: "claim"
status: "proposal"
created_at: "2026-07-15T18:12:00+08:00"
updated_at: "2026-07-15T18:12:00+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "批量导入微信文章知识；等待人工核验"
source_ids: ["source_2d4f3a7d3525782c8ff503ee"]
relations: [{"type": "derived_from", "target_id": "source_2d4f3a7d3525782c8ff503ee", "reason": "由微信公众号评论文章归纳；非独立 peer-reviewed 论文正文"}]
---

# GigaWorld-1 / VLM

作者转述：VLM 物理一致性分数与人工金标准负相关。
