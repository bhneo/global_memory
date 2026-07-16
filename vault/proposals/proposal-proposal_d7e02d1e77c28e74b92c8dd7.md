---
id: "proposal_d7e02d1e77c28e74b92c8dd7"
type: "proposal"
status: "superseded"
title: "模型提议：Robo-ValueRL 项目页报告真实机器人可泛化方块拆解任务最终成功率 84%"
created_at: "2026-07-15T17:34:06+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_7b278ba348f2a8bb94cce1fc"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_robo_valuerl_block_disassembly_20260715"
target_path: "vault/knowledge/claims/claim_robo_valuerl_block_disassembly_20260715-robo-valuerl-项目页报告真实机器人可泛化方块拆解任务最终成功率-84.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_d7e02d1e77c28e74b92c8dd7.md"
candidate_sha256: "98ce0b009df6d3e554224426a1f9f3efd4119fada50e87f05e406683a5ec3dc3"
change_reason: "导入 claim_robo_valuerl_block_disassembly_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_7b278ba348f2a8bb94cce1fc", "input_sha256": "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "uncertainty": "项目页数字与协议未完整披露；非 peer-reviewed 正文。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：Robo-ValueRL 项目页报告真实机器人可泛化方块拆解任务最终成功率 84%

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_7b278ba348f2a8bb94cce1fc`
- Input SHA-256：`1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9`
- 不确定性：项目页数字与协议未完整披露；非 peer-reviewed 正文。
- 提议理由：导入 claim_robo_valuerl_block_disassembly_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_robo_valuerl_block_disassembly_20260715-robo-valuerl-项目页报告真实机器人可泛化方块拆解任务最终成功率-84.md
@@ -0,0 +1,24 @@
+---
+id: "claim_robo_valuerl_block_disassembly_20260715"
+title: "Robo-ValueRL 项目页报告真实机器人可泛化方块拆解任务最终成功率 84%"
+tags: ["real-robot", "generalization", "manipulation"]
+domains: ["robotics"]
+confidence: "medium"
+applicability: ["Block Disassembly 测试床", "随机放置方块与随机 plate 布局"]
+uncertainty: "84% 同样仅来自项目页；Generalizable 为项目页用语，未给出对照基线或 seed 数。"
+evidence: [{"evidence_id": "ev_1530", "evidence_kind": "quote", "source_id": "source_7b278ba348f2a8bb94cce1fc", "content_id": "content_1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "extraction_id": "extraction_a288c4114d2d830f1678fd14", "input_sha256": "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "span_start": 1530, "span_end": 1547, "original_text": "84% final success", "section": "Task Videos / Block Disassembly", "stance": "supports", "verification_status": "verified", "reason": "项目页对该任务最终成功率的直接标注。"}, {"evidence_id": "ev_1410", "evidence_kind": "quote", "source_id": "source_7b278ba348f2a8bb94cce1fc", "content_id": "content_1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "extraction_id": "extraction_a288c4114d2d830f1678fd14", "input_sha256": "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "span_start": 1410, "span_end": 1528, "original_text": "The robot disassembles randomly placed blocks and sorts them into color-matched plates under randomized plate layouts.", "section": "Block Disassembly 任务描述", "stance": "supports", "verification_status": "verified", "reason": "描述泛化压力来自随机布局。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-15T17:30:00+08:00"
+updated_at: "2026-07-15T17:30:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入项目页知识；等待人工核验"
+source_ids: ["source_7b278ba348f2a8bb94cce1fc"]
+relations: [{"type": "derived_from", "target_id": "source_7b278ba348f2a8bb94cce1fc", "reason": "由 Robo-ValueRL 官方项目页归纳；非独立 peer-reviewed 论文正文"}]
+---
+
+# 方块拆解 84%
+
+项目页 reported final success。
```
