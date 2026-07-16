---
id: "proposal_a8e362c812951f230af55cd3"
type: "proposal"
status: "superseded"
title: "模型提议：该文以 +80%/-50% 公平硬币复利游戏说明：群体平均财富可增长但多数个体长期变穷，属非遍历性陷阱"
created_at: "2026-07-16T00:35:52+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_9d39636775b188c87d6a001f"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_non_ergodic_coin_game_20260716"
target_path: "vault/knowledge/claims/claim_wechat_non_ergodic_coin_game_20260716-该文以-80--50-公平硬币复利游戏说明-群体平均财富可增长但多数个体长期变穷-属非遍历性陷阱.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_a8e362c812951f230af55cd3.md"
candidate_sha256: "42287a43567eb515848727e5f668654805674a17ec728224a110be2da5d0b820"
change_reason: "导入 claim_wechat_non_ergodic_coin_game_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_9d39636775b188c87d6a001f", "input_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "uncertainty": "概率/决策科普；模拟与 37.5% 需独立验算；Thorp 原文未 capture。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文以 +80%/-50% 公平硬币复利游戏说明：群体平均财富可增长但多数个体长期变穷，属非遍历性陷阱

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_9d39636775b188c87d6a001f`
- Input SHA-256：`0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33`
- 不确定性：概率/决策科普；模拟与 37.5% 需独立验算；Thorp 原文未 capture。
- 提议理由：导入 claim_wechat_non_ergodic_coin_game_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_non_ergodic_coin_game_20260716-该文以-80--50-公平硬币复利游戏说明-群体平均财富可增长但多数个体长期变穷-属非遍历性陷阱.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_non_ergodic_coin_game_20260716"
+title: "该文以 +80%/-50% 公平硬币复利游戏说明：群体平均财富可增长但多数个体长期变穷，属非遍历性陷阱"
+tags: ["non-ergodicity", "gambling", "wealth-dynamics"]
+domains: ["probability", "behavioral-economics"]
+confidence: "medium"
+applicability: ["+80%/-50% 重复抛硬币财富过程", "10 万玩家各 100 轮模拟叙述"]
+uncertainty: "72 元阈值等为文内模拟叙述；非原始论文实验，参数需自行复现核验。"
+evidence: [{"evidence_id": "ev_56", "evidence_kind": "quote", "source_id": "source_9d39636775b188c87d6a001f", "content_id": "content_0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "extraction_id": "extraction_c6f5aba2b1a589d028d27b57", "input_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "span_start": 56, "span_end": 172, "original_text": "财富增加 80%。\n\n抛到反面，财富减少 50%。\n\n听上去是个稳赚不赔的游戏！\n\n但现实是……\n\n如果让10万个玩家参加这个游戏，并让他们各自玩100轮，你会发现：他们的平均财富确实在指数增长，但绝大多数人最后的财富竟然不到72元", "section": "硬币游戏设定", "stance": "supports", "verification_status": "verified", "reason": "文内对游戏规则与多数玩家结局的说明。"}, {"evidence_id": "ev_211", "evidence_kind": "quote", "source_id": "source_9d39636775b188c87d6a001f", "content_id": "content_0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "extraction_id": "extraction_c6f5aba2b1a589d028d27b57", "input_sha256": "0fe84716255d0f351c82744980c66aa1eeff10d2d08ed2c770ccbe7d6ece9f33", "span_start": 211, "span_end": 250, "original_text": "非遍历性陷阱。总觉得再来一局就能翻盘，恰恰是因为我们误把群体平均当成了个体命运", "section": "陷阱本质", "stance": "supports", "verification_status": "verified", "reason": "文内对误把群体平均当个体命运的点题。"}]
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
+# 非遍历硬币游戏
+
+群体平均↑ vs 多数个体↓；+80%/-50% 例。
```
