---
id: "claim_robo_valuerl_pipeline_20260715"
title: "Robo-ValueRL 项目页称该方法把价值估计、质量条件策略学习与残差在线适应串联为 offline-to-online 流水线"
tags: ["offline-to-online-rl", "value-function", "robotics"]
domains: ["robot-learning", "robotics"]
confidence: "medium"
applicability: ["GeWu-Lab 官方项目页自述的方法概述", "真实机器人 offline-to-online RL 设定"]
uncertainty: "来源是项目 landing page 而非 arXiv/PDF 正文；页面写 Citation will be updated after the arXiv release；演示视频多为 placeholder，不能当作已发表实验细节。"
evidence: [{"evidence_id": "ev_1691", "evidence_kind": "quote", "source_id": "source_7b278ba348f2a8bb94cce1fc", "content_id": "content_1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "extraction_id": "extraction_a288c4114d2d830f1678fd14", "input_sha256": "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "span_start": 1691, "span_end": 1831, "original_text": "The framework links value estimation, quality-conditioned policy learning, and residual online adaptation in one offline-to-online pipeline.", "section": "Methodology", "stance": "supports", "verification_status": "verified", "reason": "项目页对三模块流水线结构的直接陈述。"}, {"evidence_id": "ev_569", "evidence_kind": "quote", "source_id": "source_7b278ba348f2a8bb94cce1fc", "content_id": "content_1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "extraction_id": "extraction_a288c4114d2d830f1678fd14", "input_sha256": "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "span_start": 569, "span_end": 677, "original_text": "Robo-ValueRL studies how value-function reliability shapes offline-to-online robotic reinforcement learning.", "section": "Intro", "stance": "supports", "verification_status": "verified", "reason": "项目页对研究问题的表述。"}, {"evidence_id": "evp_32291", "evidence_kind": "paraphrase", "source_id": "source_7b278ba348f2a8bb94cce1fc", "input_sha256": "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "section": "Citation", "interpretation": "项目页尚未给出正式 arXiv 引用", "stance": "context", "verification_status": "verified", "reason": "提醒来源层级低于原始论文。"}]
type: "claim"
status: "proposal"
created_at: "2026-07-15T17:30:00+08:00"
updated_at: "2026-07-15T17:30:00+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "批量导入项目页知识；等待人工核验"
source_ids: ["source_7b278ba348f2a8bb94cce1fc"]
relations: [{"type": "derived_from", "target_id": "source_7b278ba348f2a8bb94cce1fc", "reason": "由 Robo-ValueRL 官方项目页归纳；非独立 peer-reviewed 论文正文"}]
---

# Robo-ValueRL 方法流水线

三模块：history-conditioned value → quality-conditioned policy → online residual adaptation。
