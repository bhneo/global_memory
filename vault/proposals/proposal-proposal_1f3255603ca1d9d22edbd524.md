---
id: "proposal_1f3255603ca1d9d22edbd524"
type: "proposal"
status: "superseded"
title: "模型提议：该文称 G0.5 在同一自回归序列中原生生成 subtask/BBox/trace/action hint 四类推理，ViT 每 4 层插时空注意力记 5 秒历史，预训练 VQA:机器人数据=1:4"
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
target_id: "claim_wechat_g05_native_cot_memory_mixture_20260716"
target_path: "vault/knowledge/claims/claim_wechat_g05_native_cot_memory_mixture_20260716-该文称-g0-5-在同一自回归序列中原生生成-subtask-bbox-trace-action-hint-四类推理-vit-每.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_1f3255603ca1d9d22edbd524.md"
candidate_sha256: "c3eced54e6483a5e4bfcd3429cbc8109ebee91cc34b7f8cf7fb87f2ac9e36b57"
change_reason: "导入 claim_wechat_g05_native_cot_memory_mixture_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_e6608d8f849ad472bbd95143", "input_sha256": "4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "uncertainty": "自媒体解读 Galaxea G0.5；benchmark 数字 confidence 低，需回技术报告核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称 G0.5 在同一自回归序列中原生生成 subtask/BBox/trace/action hint 四类推理，ViT 每 4 层插时空注意力记 5 秒历史，预训练 VQA:机器人数据=1:4

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_e6608d8f849ad472bbd95143`
- Input SHA-256：`4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228`
- 不确定性：自媒体解读 Galaxea G0.5；benchmark 数字 confidence 低，需回技术报告核验。
- 提议理由：导入 claim_wechat_g05_native_cot_memory_mixture_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_g05_native_cot_memory_mixture_20260716-该文称-g0-5-在同一自回归序列中原生生成-subtask-bbox-trace-action-hint-四类推理-vit-每.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_g05_native_cot_memory_mixture_20260716"
+title: "该文称 G0.5 在同一自回归序列中原生生成 subtask/BBox/trace/action hint 四类推理，ViT 每 4 层插时空注意力记 5 秒历史，预训练 VQA:机器人数据=1:4"
+tags: ["chain-of-thought", "visual-memory", "pretraining-mixture"]
+domains: ["robotics", "machine-learning"]
+confidence: "medium"
+applicability: ["Qwen3.5 2B 基座", "Gemini/SAM3 自动标注流水线"]
+uncertainty: "数据规模与标注 pipeline 为报告转述；1:4 配比效果需独立验证。"
+evidence: [{"evidence_id": "ev_3178", "evidence_kind": "quote", "source_id": "source_e6608d8f849ad472bbd95143", "content_id": "content_4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "extraction_id": "extraction_4180d1579b26ecbbd8e5b21b", "input_sha256": "4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "span_start": 3178, "span_end": 3503, "original_text": "Native Chain-of-Thought) 过去带有“思维链”的 VLA 往往是外挂一个大模型负责“想”，再交给控制模型“做”。\n\n而在 G0.5 中，推理和动作共享同一个自回归解码器与交叉熵损失函数，“边想边做”成为了原生的本能。 在输出动作 Token 之前，G0.5 会在同一个数据流中根据 8 种不同的 prompt 模板，按需依次生成四种维度的推理信息：\n\n子任务 (Subtask)将复杂指令拆解为当前的原子动作（如“捡起毛巾”）。\n\n边界框 (BBox)精准输出目标物体在画面中的 2D 坐标框，实现视觉定位。\n\n二维轨迹 (Trace)预测机械臂末端执行器即将在图像平面上划过的 2D 轨迹。\n\n动作提示 (ActionHint", "section": "原生 CoT", "stance": "supports", "verification_status": "verified", "reason": "文内对四类推理 token 的列举。"}, {"evidence_id": "ev_4243", "evidence_kind": "quote", "source_id": "source_e6608d8f849ad472bbd95143", "content_id": "content_4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "extraction_id": "extraction_4180d1579b26ecbbd8e5b21b", "input_sha256": "4a76f134b708400ebaa540062a88f5117c24495a2b0cea717e0250955d280228", "span_start": 4243, "span_end": 4323, "original_text": "1:4 黄金配比在训练中，VQA 样本与机器人动作样本的混合比例被严格设定为 1:4。这意味着通用的视觉问答、具身思维链和底层的动作代码，全部在同一个交叉熵损失", "section": "数据配比", "stance": "supports", "verification_status": "verified", "reason": "文内对 VQA 与动作样本混合比例。"}]
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
+# 统一序列
+
+1Hz×6 帧视觉记忆；训练随机丢弃 30% 历史帧防过拟合。
```
