---
id: "proposal_db4a4c001be4e95d19c443da"
type: "proposal"
status: "superseded"
title: "模型提议：Robo-ValueRL 项目页报告真实机器人毫米级芯片插入任务最终成功率 86%"
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
target_id: "claim_robo_valuerl_chip_insertion_20260715"
target_path: "vault/knowledge/claims/claim_robo_valuerl_chip_insertion_20260715-robo-valuerl-项目页报告真实机器人毫米级芯片插入任务最终成功率-86.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_db4a4c001be4e95d19c443da.md"
candidate_sha256: "29a357ad641995b1b23a6cb53c6fb3bb47f8cb68d81a87fd58053f1a5eb60421"
change_reason: "导入 claim_robo_valuerl_chip_insertion_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_7b278ba348f2a8bb94cce1fc", "input_sha256": "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "uncertainty": "项目页数字与协议未完整披露；非 peer-reviewed 正文。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：Robo-ValueRL 项目页报告真实机器人毫米级芯片插入任务最终成功率 86%

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_7b278ba348f2a8bb94cce1fc`
- Input SHA-256：`1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9`
- 不确定性：项目页数字与协议未完整披露；非 peer-reviewed 正文。
- 提议理由：导入 claim_robo_valuerl_chip_insertion_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_robo_valuerl_chip_insertion_20260715-robo-valuerl-项目页报告真实机器人毫米级芯片插入任务最终成功率-86.md
@@ -0,0 +1,24 @@
+---
+id: "claim_robo_valuerl_chip_insertion_20260715"
+title: "Robo-ValueRL 项目页报告真实机器人毫米级芯片插入任务最终成功率 86%"
+tags: ["real-robot", "insertion", "manipulation"]
+domains: ["robotics"]
+confidence: "medium"
+applicability: ["项目页 Chip Insertion 任务描述", "Millimeter-level chip insertion 测试床", "真实机器人 rollout"]
+uncertainty: "86% 来自项目页 headline 数字，未给出 trial 数、置信区间或实验协议；PDF/论文未 capture，不能外推为独立复现结果。"
+evidence: [{"evidence_id": "ev_1320", "evidence_kind": "quote", "source_id": "source_7b278ba348f2a8bb94cce1fc", "content_id": "content_1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "extraction_id": "extraction_a288c4114d2d830f1678fd14", "input_sha256": "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "span_start": 1320, "span_end": 1337, "original_text": "86% final success", "section": "Task Videos / Chip Insertion", "stance": "supports", "verification_status": "verified", "reason": "项目页对该任务最终成功率的直接标注。"}, {"evidence_id": "ev_1190", "evidence_kind": "quote", "source_id": "source_7b278ba348f2a8bb94cce1fc", "content_id": "content_1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "extraction_id": "extraction_a288c4114d2d830f1678fd14", "input_sha256": "1c85061a186c9d21533adeddde7b4d4e21711d64175311fb46b20b1595d281a9", "span_start": 1190, "span_end": 1318, "original_text": "The robot grasps a PCB, adjusts it to a feasible insertion pose, then grasps and inserts a chip into millimeter-scale clearance.", "section": "Chip Insertion 任务描述", "stance": "supports", "verification_status": "verified", "reason": "限定任务为毫米级间隙插入。"}]
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
+# 芯片插入 86%
+
+项目页 reported final success。
```
