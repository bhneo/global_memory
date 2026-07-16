---
id: "proposal_0f5335fe19f69a42cfbd608a"
type: "proposal"
status: "superseded"
title: "模型提议：该文称 VLM-as-Encoder + 流匹配专家可提速，但 VLM 生成/CoT 能力受条件瓶颈限制，且动作梯度可导致 VLM 能力退化；PI 以知识绝缘阻断有害梯度"
created_at: "2026-07-16T11:07:21+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_e6608d8f849ad472bbd95143"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_g05_flow_encoder_bottleneck_ki_20260716"
target_path: "vault/knowledge/claims/claim_wechat_g05_flow_encoder_bottleneck_ki_20260716-该文称-vlm-as-encoder-流匹配专家可提速-但-vlm-生成-cot-能力受条件瓶颈限制-且动作梯度可导致-vlm-.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_0f5335fe19f69a42cfbd608a.md"
candidate_sha256: "dd21a531610c30fed356ff30e1db98cca6b8502da581b7544f977d4b8c6f04b4"
change_reason: "导入 claim_wechat_g05_flow_encoder_bottleneck_ki_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_e6608d8f849ad472bbd95143", "input_sha256": "4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "uncertainty": "自媒体解读 Galaxea G0.5；benchmark 数字 confidence 低，需回技术报告核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称 VLM-as-Encoder + 流匹配专家可提速，但 VLM 生成/CoT 能力受条件瓶颈限制，且动作梯度可导致 VLM 能力退化；PI 以知识绝缘阻断有害梯度

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_e6608d8f849ad472bbd95143`
- Input SHA-256：`4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228`
- 不确定性：自媒体解读 Galaxea G0.5；benchmark 数字 confidence 低，需回技术报告核验。
- 提议理由：导入 claim_wechat_g05_flow_encoder_bottleneck_ki_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_g05_flow_encoder_bottleneck_ki_20260716-该文称-vlm-as-encoder-流匹配专家可提速-但-vlm-生成-cot-能力受条件瓶颈限制-且动作梯度可导致-vlm-.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_g05_flow_encoder_bottleneck_ki_20260716"
+title: "该文称 VLM-as-Encoder + 流匹配专家可提速，但 VLM 生成/CoT 能力受条件瓶颈限制，且动作梯度可导致 VLM 能力退化；PI 以知识绝缘阻断有害梯度"
+tags: ["VLM-as-encoder", "catastrophic-forgetting", "knowledge-insulation"]
+domains: ["robotics", "machine-learning"]
+confidence: "medium"
+applicability: ["50Hz 灵巧操作动机", "离散 token 预测 vs 连续回归目标不同构"]
+uncertainty: "抗遗忘/ KI 机制来自对 PI 论文的二手解读；需回 π0.5 原文核验。"
+evidence: [{"evidence_id": "ev_685", "evidence_kind": "quote", "source_id": "source_e6608d8f849ad472bbd95143", "content_id": "content_4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "extraction_id": "extraction_4180d1579b26ecbbd8e5b21b", "input_sha256": "4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "span_start": 685, "span_end": 961, "original_text": "VLM-as-Encoder） 的架构。PI的π0系列工作就是个典型。π0 第一个引入参数独立的流匹配专家，让视觉-语言模型只提供隐藏状态或缓存特征，再由专家去预测连续动作块。\n\nπ0的action chunk和flow matching\n\n这是为了实现50hz的灵巧操作，需要高精度、多峰的连续动作，而离散的自回归在这个频率下又慢又不精确。正是这个延迟瓶颈，把整个领域推向了第二条路。\n\n在这个架构下，VLM 退居二线，只负责提供隐状态或视觉语言上下文；而在它之上，挂载一个单独训练的 Flow Matching 或 Diffusion 动作专家模型", "section": "编码器架构", "stance": "supports", "verification_status": "verified", "reason": "文内对 VLM 退居二线、外挂专家的说明。"}, {"evidence_id": "ev_1272", "evidence_kind": "quote", "source_id": "source_e6608d8f849ad472bbd95143", "content_id": "content_4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "extraction_id": "extraction_4180d1579b26ecbbd8e5b21b", "input_sha256": "4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "span_start": 1272, "span_end": 1386, "original_text": "抗遗忘问题。\n\n原因在于两个目标根本不同构。视觉-语言模型预训练做的是离散的下一个 token 预测，流匹配专家做的是连续动作回归，后者的梯度灌回来，是在把一套通用表示改写成单一本体的运动分布。\n\nPI提出的方法是KI，知识绝缘", "section": "KI 与遗忘", "stance": "supports", "verification_status": "verified", "reason": "文内对梯度回传伤害与 PI KI 对策。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T11:08:00+08:00"
+updated_at: "2026-07-16T11:08:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入 G0.5 vs PI flow matching 解读；等待人工核验"
+source_ids: ["source_e6608d8f849ad472bbd95143"]
+relations: [{"type": "derived_from", "target_id": "source_e6608d8f849ad472bbd95143", "reason": "具身纪元 Marilyn Liu 解读 Galaxea G0.5 技术报告 vs PI flow matching；非官方 primary source"}]
+---
+
+# 流匹配代价
+
+高频控制推动 flow matching；VLA-0 被引证自回归仍可竞争。
```
