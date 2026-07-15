---
id: "proposal_2c7561e3342ca73fe93ee396"
type: "proposal"
status: "superseded"
title: "模型提议：Agentic-VLA 在 LIBERO one-shot 设定下平均成功率 70.5%，相对 OpenVLA-OFT SFT 基线提升 26.9 个百分点"
created_at: "2026-07-15T12:25:12+08:00"
updated_at: "2026-07-15T14:27:48+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_2c21320690e566fbbf80fd75"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_agentic_vla_one_shot_20260715"
target_path: "vault/knowledge/claims/claim_agentic_vla_one_shot_20260715-agentic-vla-在-libero-one-shot-设定下平均成功率-70-5-相对-openvla-oft-sft-基.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_2c7561e3342ca73fe93ee396.md"
candidate_sha256: "d87e76b75a5053323679fc870034c3bef1cd981caccf50677d4ed475521c2da8"
change_reason: "Agentic-VLA one-shot"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v1", "prompt_sha256": "94d886d52ea555f36802b873910cd6129ad84354f793af05df7d9a68cfe59aee", "input_source_id": "source_2c21320690e566fbbf80fd75", "input_sha256": "8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43", "uncertainty": "须人工对照 raw PDF 批准"}
reviewed_at: "2026-07-15T14:27:48+08:00"
review_reason: "人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份"
superseded_by: "proposal_ed15e3a6bc9d3a320d6ce246"
---

# 模型提议：Agentic-VLA 在 LIBERO one-shot 设定下平均成功率 70.5%，相对 OpenVLA-OFT SFT 基线提升 26.9 个百分点

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v1`
- Prompt SHA-256：`94d886d52ea555f36802b873910cd6129ad84354f793af05df7d9a68cfe59aee`
- Input source：`source_2c21320690e566fbbf80fd75`
- Input SHA-256：`8fcca0145e106194abe0e47171ecbd01ffd84ebb4c8904cb4f37ac6ba0629e43`
- 不确定性：须人工对照 raw PDF 批准
- 提议理由：Agentic-VLA one-shot
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_agentic_vla_one_shot_20260715-agentic-vla-在-libero-one-shot-设定下平均成功率-70-5-相对-openvla-oft-sft-基.md
@@ -0,0 +1,24 @@
+---
+id: "claim_agentic_vla_one_shot_20260715"
+type: "claim"
+status: "proposal"
+title: "Agentic-VLA 在 LIBERO one-shot 设定下平均成功率 70.5%，相对 OpenVLA-OFT SFT 基线提升 26.9 个百分点"
+created_at: "2026-07-15T12:20:00+08:00"
+updated_at: "2026-07-15T12:20:00+08:00"
+aliases: []
+tags: ["vla", "one-shot", "libero"]
+domains: ["robot-learning"]
+confidence: "medium"
+source_ids: ["source_2c21320690e566fbbf80fd75"]
+relations: [{"type": "derived_from", "target_id": "source_2c21320690e566fbbf80fd75", "reason": "由 Agentic-VLA 原始论文归纳"}]
+superseded_by: null
+valid_during: null
+change_reason: "批量导入原始论文知识；等待人工核验"
+applicability: ["每任务 1 demo SFT 预训练", "LIBERO 四套件"]
+uncertainty: "摘要 +28.5% 与 Table 2 +26.9% 不一致，批准时以 Table 2 为准。"
+evidence: [{"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 7-8 页 Table 2", "excerpt": "Agentic-VLA 70.5 ... OpenVLA-OFT 43.6 ... Δ vs. SFT +26.9", "stance": "supports", "reason": "Table 2 one-shot 对比。"}, {"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 8 页 Section 4.3", "excerpt": "only a single demonstration per task is available for SFT pre-training", "stance": "context", "reason": "one-shot 协议。"}, {"source_id": "source_2c21320690e566fbbf80fd75", "location": "第 1 页 Abstract", "excerpt": "+28.5% in 1-shot learning", "stance": "context", "reason": "与 Table 2 数字差异，待核对。"}]
+---
+
+# one-shot
+
+Table 2。
```
