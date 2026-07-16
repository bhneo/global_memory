---
id: "proposal_04101797862b2571c0fbdc45"
type: "proposal"
status: "superseded"
title: "模型提议：该文称 EXPO 对扩散/流匹配 VLA 采用双策略：预训练流策略仅用监督损失，轻量高斯修正策略优化 Q，避免长降噪链价值梯度反传"
created_at: "2026-07-16T11:04:29+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_8b41a014bee47c4239a2fa81"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_expo_dual_policy_20260716"
target_path: "vault/knowledge/claims/claim_wechat_expo_dual_policy_20260716-该文称-expo-对扩散-流匹配-vla-采用双策略-预训练流策略仅用监督损失-轻量高斯修正策略优化-q-避免长降噪链价值梯度反.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_04101797862b2571c0fbdc45.md"
candidate_sha256: "9a6ef206e763f0bd5f89c6dbbd510482dcc5f8339968b2f068081cd8adccf33b"
change_reason: "导入 claim_wechat_expo_dual_policy_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_8b41a014bee47c4239a2fa81", "input_sha256": "15201becf4f645da31cfd5c6c3c5bc10dec18547711dedd2c5fa9bf99fcdf1b6", "uncertainty": "Finn/Dong 研讨会转述；实验数字与算法细节需回 EXPO/EXPO-FT 原文核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称 EXPO 对扩散/流匹配 VLA 采用双策略：预训练流策略仅用监督损失，轻量高斯修正策略优化 Q，避免长降噪链价值梯度反传

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_8b41a014bee47c4239a2fa81`
- Input SHA-256：`15201becf4f645da31cfd5c6c3c5bc10dec18547711dedd2c5fa9bf99fcdf1b6`
- 不确定性：Finn/Dong 研讨会转述；实验数字与算法细节需回 EXPO/EXPO-FT 原文核验。
- 提议理由：导入 claim_wechat_expo_dual_policy_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_expo_dual_policy_20260716-该文称-expo-对扩散-流匹配-vla-采用双策略-预训练流策略仅用监督损失-轻量高斯修正策略优化-q-避免长降噪链价值梯度反.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_expo_dual_policy_20260716"
+title: "该文称 EXPO 对扩散/流匹配 VLA 采用双策略：预训练流策略仅用监督损失，轻量高斯修正策略优化 Q，避免长降噪链价值梯度反传"
+tags: ["EXPO", "diffusion-policy", "off-policy-rl"]
+domains: ["reinforcement-learning", "robotics"]
+confidence: "medium"
+applicability: ["扩散策略在线 RL 不稳定问题", "OTF 候选池 Q 选优"]
+uncertainty: "公式与消融结论为综述级；12 项基准细节需回 EXPO 论文。"
+evidence: [{"evidence_id": "ev_5494", "evidence_kind": "quote", "source_id": "source_8b41a014bee47c4239a2fa81", "content_id": "content_15201becf4f645da31cfd5c6c3c5bc10dec18547711dedd2c5fa9bf99fcdf1b6", "extraction_id": "extraction_27a3915bf1f44e95bc06bbae", "input_sha256": "15201becf4f645da31cfd5c6c3c5bc10dec18547711dedd2c5fa9bf99fcdf1b6", "span_start": 5494, "span_end": 5587, "original_text": "双策略解耦优化，隔离VLA主干梯度\n\n不直接对底层扩散流匹配VLA做Q值最大化梯度更新，构建双参数化策略：\n\n基础流策略：即预训练VLA ，仅使用原始监督损失更新，全程不参与TD价值梯度", "section": "双策略设计", "stance": "supports", "verification_status": "verified", "reason": "文内对 VLA 主干隔离 Q 梯度的核心思路。"}, {"evidence_id": "ev_5675", "evidence_kind": "quote", "source_id": "source_8b41a014bee47c4239a2fa81", "content_id": "content_15201becf4f645da31cfd5c6c3c5bc10dec18547711dedd2c5fa9bf99fcdf1b6", "extraction_id": "extraction_27a3915bf1f44e95bc06bbae", "input_sha256": "15201becf4f645da31cfd5c6c3c5bc10dec18547711dedd2c5fa9bf99fcdf1b6", "span_start": 5675, "span_end": 5923, "original_text": "实时采样（OTF）候选池选优，贝尔曼回溯同步复用\n\n从基础VLA采样N组原始候选动作；\n\n对每组原始动作，通过修正策略生成独立修正动作，组合得到「原始动作+修正动作」候选池；\n\n全局选取候选池中Q值最大的动作作为当前执行动作；\n\n贝尔曼价值回溯计算下一状态目标值时，同步复用这套实时采样选优机制，保证目标动作始终是当前最优候选。\n\nQ网络采用TD学习训练，损失公式：\n\n该机制两大优势：\n\n实时调用最新Q网络筛选动作，自适应能力强；\n\n候选池永久保留原始VLA输出动作，抵御离线RL常见的策略坍缩", "section": "OTF 选优", "stance": "supports", "verification_status": "verified", "reason": "文内对候选池选优与防坍缩的说明。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T11:05:00+08:00"
+updated_at: "2026-07-16T11:05:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入 EXPO-FT / 离线 VLA RL 研讨会；等待人工核验"
+source_ids: ["source_8b41a014bee47c4239a2fa81"]
+relations: [{"type": "derived_from", "target_id": "source_8b41a014bee47c4239a2fa81", "reason": "human five 转载 Chelsea Finn & Perry Dong 研讨会：离线迭代 RL 与 EXPO-FT 在线 VLA 微调；原论文未 capture"}]
+---
+
+# EXPO 双策略
+
+基础 VLA + 修正量；贝尔曼回溯复用选优机制。
```
