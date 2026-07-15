---
id: "proposal_76cd187803aade3dc6c582dd"
type: "proposal"
status: "superseded"
title: "模型提议：Play2Perfect 表明仅 play 预训练不足以完成 tight-clearance 装配，装配专用 RL 微调仍然必要"
created_at: "2026-07-15T12:25:12+08:00"
updated_at: "2026-07-15T14:27:56+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_05d8a9da9e0b53b94872f2a7"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_play2perfect_finetuning_necessary_20260715"
target_path: "vault/knowledge/claims/claim_play2perfect_finetuning_necessary_20260715-play2perfect-表明仅-play-预训练不足以完成-tight-clearance-装配-装配专用-rl-微调仍然必要.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_76cd187803aade3dc6c582dd.md"
candidate_sha256: "531e07a3401525781d9c0e93faa3e711fb3f345dcad33606737689c565d143d6"
change_reason: "Play2Perfect 微调"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v1", "prompt_sha256": "94d886d52ea555f36802b873910cd6129ad84354f793af05df7d9a68cfe59aee", "input_source_id": "source_05d8a9da9e0b53b94872f2a7", "input_sha256": "a5eb515ece7fd538a7bda60c3ee1df1506ff255f13d9dad1ba2b99dd44139a47", "uncertainty": "须人工对照 raw PDF 批准"}
reviewed_at: "2026-07-15T14:27:56+08:00"
review_reason: "人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份"
superseded_by: "proposal_8de5ab93fa9dcd6696a003c1"
---

# 模型提议：Play2Perfect 表明仅 play 预训练不足以完成 tight-clearance 装配，装配专用 RL 微调仍然必要

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v1`
- Prompt SHA-256：`94d886d52ea555f36802b873910cd6129ad84354f793af05df7d9a68cfe59aee`
- Input source：`source_05d8a9da9e0b53b94872f2a7`
- Input SHA-256：`a5eb515ece7fd538a7bda60c3ee1df1506ff255f13d9dad1ba2b99dd44139a47`
- 不确定性：须人工对照 raw PDF 批准
- 提议理由：Play2Perfect 微调
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_play2perfect_finetuning_necessary_20260715-play2perfect-表明仅-play-预训练不足以完成-tight-clearance-装配-装配专用-rl-微调仍然必要.md
@@ -0,0 +1,24 @@
+---
+id: "claim_play2perfect_finetuning_necessary_20260715"
+type: "claim"
+status: "proposal"
+title: "Play2Perfect 表明仅 play 预训练不足以完成 tight-clearance 装配，装配专用 RL 微调仍然必要"
+created_at: "2026-07-15T12:20:00+08:00"
+updated_at: "2026-07-15T12:20:00+08:00"
+aliases: []
+tags: ["finetuning", "contact-rich", "assembly"]
+domains: ["robotics"]
+confidence: "medium"
+source_ids: ["source_05d8a9da9e0b53b94872f2a7"]
+relations: [{"type": "derived_from", "target_id": "source_05d8a9da9e0b53b94872f2a7", "reason": "由 Play2Perfect 原始论文归纳"}]
+superseded_by: null
+valid_during: null
+change_reason: "批量导入原始论文知识；等待人工核验"
+applicability: ["Tight-Insertion", "Play-only vs Play2Perfect", "5–0.5 mm 微调 clearance 范围"]
+uncertainty: "Play-only 在宽松间隙仍可能成功；claim 针对 tight/contact-rich regime。"
+evidence: [{"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 7-8 页 Section 4.3", "excerpt": "RL finetuning is still needed to turn this prior into a precise, contact-rich assembly policy.", "stance": "supports", "reason": "作者结论。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 8 页 Section 4.3", "excerpt": "At 0.5 mm clearance, Play2Perfect still succeeds 60% of the time, whereas Play-only fails completely.", "stance": "supports", "reason": "真实 tight clearance 对比。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 7 页 Section 4.3", "excerpt": "Play-only solves only the loosest insertion settings", "stance": "context", "reason": "play 先验在粗精度仍有用。"}]
+---
+
+# 微调必要性
+
+Section 4.3 Play-only vs Play2Perfect。
```
