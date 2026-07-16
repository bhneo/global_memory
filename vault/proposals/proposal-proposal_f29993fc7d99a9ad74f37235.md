---
id: "proposal_f29993fc7d99a9ad74f37235"
type: "proposal"
status: "pending"
title: "模型提议：该文称乘法型过程中几何平均（长期增长率）低于算术平均，个体长期表现系统性低于群体平均"
created_at: "2026-07-16T00:35:52+08:00"
updated_at: "2026-07-16T00:35:52+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_9d39636775b188c87d6a001f"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_multiplicative_jensen_gap_20260716"
target_path: "vault/knowledge/claims/claim_wechat_multiplicative_jensen_gap_20260716-该文称乘法型过程中几何平均-长期增长率-低于算术平均-个体长期表现系统性低于群体平均.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_f29993fc7d99a9ad74f37235.md"
candidate_sha256: "822911c8fc99154edb1296e3def61d4efc0f33a069a0647c410f5ad05b1d358d"
change_reason: "导入 claim_wechat_multiplicative_jensen_gap_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_9d39636775b188c87d6a001f", "input_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "uncertainty": "概率/决策科普；模拟与 37.5% 需独立验算；Thorp 原文未 capture。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称乘法型过程中几何平均（长期增长率）低于算术平均，个体长期表现系统性低于群体平均

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_9d39636775b188c87d6a001f`
- Input SHA-256：`0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33`
- 不确定性：概率/决策科普；模拟与 37.5% 需独立验算；Thorp 原文未 capture。
- 提议理由：导入 claim_wechat_multiplicative_jensen_gap_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_multiplicative_jensen_gap_20260716-该文称乘法型过程中几何平均-长期增长率-低于算术平均-个体长期表现系统性低于群体平均.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_multiplicative_jensen_gap_20260716"
+title: "该文称乘法型过程中几何平均（长期增长率）低于算术平均，个体长期表现系统性低于群体平均"
+tags: ["jensen-inequality", "geometric-mean", "multiplicative-process"]
+domains: ["probability", "finance"]
+confidence: "medium"
+applicability: ["复利/乘法财富过程", "波动越大差距越大叙述"]
+uncertainty: "公式在提取文本中被省略为文字描述；严格条件与证明未给出。"
+evidence: [{"evidence_id": "ev_1589", "evidence_kind": "quote", "source_id": "source_9d39636775b188c87d6a001f", "content_id": "content_0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "extraction_id": "extraction_c6f5aba2b1a589d028d27b57", "input_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "span_start": 1589, "span_end": 1644, "original_text": "Jensen不等式，有：\n\n因此，乘法系统的长期增长率（即几何平均）始终小于算术平均。波动越大，这个差距越明显", "section": "Jensen 不等式", "stance": "supports", "verification_status": "verified", "reason": "文内对几何平均小于算术平均的解释。"}, {"evidence_id": "ev_1377", "evidence_kind": "quote", "source_id": "source_9d39636775b188c87d6a001f", "content_id": "content_0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "extraction_id": "extraction_c6f5aba2b1a589d028d27b57", "input_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "span_start": 1377, "span_end": 1731, "original_text": "乘法型、且具有路径依赖的特征——比如投资的复利、健康的衰退、声誉的损毁。这类系统的典型特征是：上行有限，下行无底。\n\n一次破产，可能毁掉一生；\n\n一场次错误决策，可能彻底改变命运；\n\n一次失信可能彻底摧毁信任；\n\n而能赚到的财富、涨的绩效、建立的优势却总是有限。\n\n这正是为什么在数学上，乘法型过程的长期增长率并不等于“平均收益”，而是更接近于：\n\n相比之下，群体平均通常用的是算术平均，\n\n而由于对数函数是严格凹函数，基于Jensen不等式，有：\n\n因此，乘法系统的长期增长率（即几何平均）始终小于算术平均。波动越大，这个差距越明显。算术平均是告诉你‘如果永远幸运会怎样’，而几何平均告诉你‘在真实世界里走过风雨之后你剩下多少。\n\n这意味着个体的长期表现总是远低于“群体平均收益”，不是运气不好而是结构使然", "section": "乘法系统", "stance": "supports", "verification_status": "verified", "reason": "文内对上行有限、下行无底的乘法特征。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T00:36:00+08:00"
+updated_at: "2026-07-16T00:36:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入非遍历性/凯利公式科普；等待人工核验"
+source_ids: ["source_9d39636775b188c87d6a001f"]
+relations: [{"type": "derived_from", "target_id": "source_9d39636775b188c87d6a001f", "reason": "由 DataCafe/雪鹅经中科院物理所转载的非遍历性与凯利公式科普归纳；Thorp 等原书未 capture"}]
+---
+
+# 几何 vs 算术平均
+
+乘法过程：个体长期低于群体算术平均。
```
