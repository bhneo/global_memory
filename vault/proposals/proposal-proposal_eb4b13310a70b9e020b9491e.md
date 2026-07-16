---
id: "proposal_eb4b13310a70b9e020b9491e"
type: "proposal"
status: "pending"
title: "模型提议：该文称对上述硬币游戏凯利公式建议每次下注总资金的 37.5%，以平衡增长与避免爆仓"
created_at: "2026-07-16T00:35:53+08:00"
updated_at: "2026-07-16T00:35:53+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_9d39636775b188c87d6a001f"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_kelly_bet_fraction_20260716"
target_path: "vault/knowledge/claims/claim_wechat_kelly_bet_fraction_20260716-该文称对上述硬币游戏凯利公式建议每次下注总资金的-37-5-以平衡增长与避免爆仓.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_eb4b13310a70b9e020b9491e.md"
candidate_sha256: "ab7a508b16d5b03d967039d11aa21be245a8b06d8190197815d1e2b4a7c1f5b3"
change_reason: "导入 claim_wechat_kelly_bet_fraction_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_9d39636775b188c87d6a001f", "input_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "uncertainty": "概率/决策科普；模拟与 37.5% 需独立验算；Thorp 原文未 capture。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称对上述硬币游戏凯利公式建议每次下注总资金的 37.5%，以平衡增长与避免爆仓

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_9d39636775b188c87d6a001f`
- Input SHA-256：`0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33`
- 不确定性：概率/决策科普；模拟与 37.5% 需独立验算；Thorp 原文未 capture。
- 提议理由：导入 claim_wechat_kelly_bet_fraction_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_kelly_bet_fraction_20260716-该文称对上述硬币游戏凯利公式建议每次下注总资金的-37-5-以平衡增长与避免爆仓.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_kelly_bet_fraction_20260716"
+title: "该文称对上述硬币游戏凯利公式建议每次下注总资金的 37.5%，以平衡增长与避免爆仓"
+tags: ["kelly-criterion", "bet-sizing", "risk-management"]
+domains: ["probability", "finance"]
+confidence: "medium"
+applicability: ["+80%/-50% 公平硬币重复博弈", "Kelly 最优下注比例科普"]
+uncertainty: "37.5% 为文内给定值；p/b/a 参数推导步骤在科普中被压缩，需独立验算。"
+evidence: [{"evidence_id": "ev_1835", "evidence_kind": "quote", "source_id": "source_9d39636775b188c87d6a001f", "content_id": "content_0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "extraction_id": "extraction_c6f5aba2b1a589d028d27b57", "input_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "span_start": 1835, "span_end": 2361, "original_text": "Kelly Criterion）是一种用于重复博弈中的最优下注策略，目标是最大化长期收益的同时避免短期亏光出局。它最初由约翰·凯利（John L. Kelly Jr.）于 1956 年在贝尔实验室提出，原意是解决通信系统中“如何在有噪声的信道中分配信号功率”，以实现信息传输效率最大化。\n\n后来这套理论很快就跨界出圈。\n\n美国数学家、投资奇才爱德华·索普（Edward Thorp）发现凯利公式能够优化财富增长路径。他将凯式带进赌场，在《Beat the Dealer》中首次用它系统性打败了21点庄家，之后又带进了华尔街，在《Beat the Market》中继续“收割”。\n\n这一准则本质上等价于最大化对数期望收益（log-utility），从而兼顾了增长与风险之间的动态平衡。它帮你在“活得长久”和“赚得够多”之间，找到一个最优平衡点。\n\n凯利公式：\n\n其中，成功的概率是 p，失败的概率是q = 1-p；成功时的收益倍率（不包含本金）是b，失败时的亏损比例是 a（通常是1，如果亏的是全部下注金额）。\n\n回到开篇提到的抛硬币游戏，你可以选择下注一定比例的本金一直玩下去，但每次押多少最合理？\n\n也就是说，凯利公式建议你每次投入总资金的37.5%", "section": "凯利公式", "stance": "supports", "verification_status": "verified", "reason": "文内对凯利公式来源与下注比例建议。"}, {"evidence_id": "ev_2362", "evidence_kind": "quote", "source_id": "source_9d39636775b188c87d6a001f", "content_id": "content_0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "extraction_id": "extraction_c6f5aba2b1a589d028d27b57", "input_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "span_start": 2362, "span_end": 2436, "original_text": "押得太多，即使有优势，也可能因为几次连输直接爆仓；押得太少，又错过了本该属于你的增长。\n\n凯利公式的意义就在于：找到那个既能长期赚最多，又能活得下去", "section": "下注权衡", "stance": "supports", "verification_status": "verified", "reason": "文内对过大/过小下注的风险说明。"}]
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
+# 凯利 37.5%
+
+硬币游戏最优下注比例（文内叙述）。
```
