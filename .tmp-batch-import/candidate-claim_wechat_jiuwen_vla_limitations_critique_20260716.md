---
id: "claim_wechat_jiuwen_vla_limitations_critique_20260716"
title: "该文批评当前 VLA「2.0」阶段：缺组合泛化、长程任务分解与异常回退、端到端黑盒难定位故障、成功率与稳定性不足"
tags: ["VLA", "compositional-generalization", "long-horizon"]
domains: ["robotics", "machine-learning"]
confidence: "low"
applicability: ["Sim2Real 2.0 问题清单", "开抽屉+抓取零样本组合举例"]
uncertainty: "为 openJiuwen 产品叙事中的竞品/现状批评；未给出独立实验对照。"
evidence: [{"evidence_id": "ev_982", "evidence_kind": "quote", "source_id": "source_6ada1b3b0033883b83a3bf40", "content_id": "content_d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567", "extraction_id": "extraction_4d37e41c1600afe16e196923", "input_sha256": "d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567", "span_start": 982, "span_end": 1011, "original_text": "组合泛化能力——无法将已学的“开抽屉”与“抓取”零样本组合", "section": "组合泛化不足", "stance": "supports", "verification_status": "verified", "reason": "文内对 VLA 无法组合已学技能的批评。"}, {"evidence_id": "ev_1018", "evidence_kind": "quote", "source_id": "source_6ada1b3b0033883b83a3bf40", "content_id": "content_d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567", "extraction_id": "extraction_4d37e41c1600afe16e196923", "input_sha256": "d7c637ec507a962632eee3ea0ecf37746317b5f051cfd986b1d6a3ed14d18567", "span_start": 1018, "span_end": 1146, "original_text": "长程复合任务能力不足：当前模型擅长短程原子操作（如“抓取红色方块”），但面对长程复合任务（如“从料架上取Tray盘→绕过设备→放入机台→按压确认→返回原位”），单一VLA模型缺乏任务分解、子任务编排、异常回退的能力。它只能在训练分布内“模仿”，无法在运行时", "section": "规划能力不足", "stance": "supports", "verification_status": "verified", "reason": "文内对长程任务需重训、缺运行时规划的说明。"}]
type: "claim"
status: "proposal"
created_at: "2026-07-16T11:10:00+08:00"
updated_at: "2026-07-16T11:10:00+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "批量导入 Jiuwen Symbiosis 宣传文；等待人工核验"
source_ids: ["source_6ada1b3b0033883b83a3bf40"]
relations: [{"type": "derived_from", "target_id": "source_6ada1b3b0033883b83a3bf40", "reason": "量子位授权转载 openJiuwen Jiuwen Symbiosis 开源宣传；属 vendor/社区软文"}]
---

# VLA 2.0 批评

视觉→语言→物理→动作压入单一 Transformer 致故障难归因。
