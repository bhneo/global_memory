---
id: "claim_robo_valuerl_block_disassembly_20260715"
title: "Robo-ValueRL 项目页报告真实机器人可泛化方块拆解任务最终成功率 84%"
tags: ["real-robot", "generalization", "manipulation"]
domains: ["robotics"]
confidence: "medium"
applicability: ["Block Disassembly 测试床", "随机放置方块与随机 plate 布局"]
uncertainty: "84% 同样仅来自项目页；Generalizable 为项目页用语，未给出对照基线或 seed 数。"
evidence: [{"evidence_id": "ev_1530", "evidence_kind": "quote", "source_id": "source_7b278ba348f2a8bb94cce1fc", "content_id": "content_1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "extraction_id": "extraction_a288c4114d2d830f1678fd14", "input_sha256": "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "span_start": 1530, "span_end": 1547, "original_text": "84% final success", "section": "Task Videos / Block Disassembly", "stance": "supports", "verification_status": "verified", "reason": "项目页对该任务最终成功率的直接标注。"}, {"evidence_id": "ev_1410", "evidence_kind": "quote", "source_id": "source_7b278ba348f2a8bb94cce1fc", "content_id": "content_1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "extraction_id": "extraction_a288c4114d2d830f1678fd14", "input_sha256": "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "span_start": 1410, "span_end": 1528, "original_text": "The robot disassembles randomly placed blocks and sorts them into color-matched plates under randomized plate layouts.", "section": "Block Disassembly 任务描述", "stance": "supports", "verification_status": "verified", "reason": "描述泛化压力来自随机布局。"}]
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

# 方块拆解 84%

项目页 reported final success。
