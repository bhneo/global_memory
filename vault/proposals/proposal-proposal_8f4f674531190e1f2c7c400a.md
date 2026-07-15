---
id: "proposal_8f4f674531190e1f2c7c400a"
type: "proposal"
status: "superseded"
title: "模型提议：Play2Perfect 仿真微调策略可零样本迁移到真实世界紧配合插入，0.5 mm 间隙成功率 6/10"
created_at: "2026-07-15T12:25:11+08:00"
updated_at: "2026-07-15T14:28:04+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_05d8a9da9e0b53b94872f2a7"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_play2perfect_realworld_tight_insertion_20260715"
target_path: "vault/knowledge/claims/claim_play2perfect_realworld_tight_insertion_20260715-play2perfect-仿真微调策略可零样本迁移到真实世界紧配合插入-0-5-mm-间隙成功率-6-10.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_8f4f674531190e1f2c7c400a.md"
candidate_sha256: "aa234f0004b59504c5ea37cecf2501d8e9f408518cc5bb4c15bb40043c4fcc75"
change_reason: "Play2Perfect 真实插入"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v1", "prompt_sha256": "94d886d52ea555f36802b873910cd6129ad84354f793af05df7d9a68cfe59aee", "input_source_id": "source_05d8a9da9e0b53b94872f2a7", "input_sha256": "a5eb515ece7fd538a7bda60c3ee1df1506ff255f13d9dad1ba2b99dd44139a47", "uncertainty": "须人工对照 raw PDF 批准"}
reviewed_at: "2026-07-15T14:28:04+08:00"
review_reason: "人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份"
superseded_by: "proposal_e4c5d7883d8cafc851d3a466"
---

# 模型提议：Play2Perfect 仿真微调策略可零样本迁移到真实世界紧配合插入，0.5 mm 间隙成功率 6/10

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v1`
- Prompt SHA-256：`94d886d52ea555f36802b873910cd6129ad84354f793af05df7d9a68cfe59aee`
- Input source：`source_05d8a9da9e0b53b94872f2a7`
- Input SHA-256：`a5eb515ece7fd538a7bda60c3ee1df1506ff255f13d9dad1ba2b99dd44139a47`
- 不确定性：须人工对照 raw PDF 批准
- 提议理由：Play2Perfect 真实插入
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_play2perfect_realworld_tight_insertion_20260715-play2perfect-仿真微调策略可零样本迁移到真实世界紧配合插入-0-5-mm-间隙成功率-6-10.md
@@ -0,0 +1,24 @@
+---
+id: "claim_play2perfect_realworld_tight_insertion_20260715"
+type: "claim"
+status: "proposal"
+title: "Play2Perfect 仿真微调策略可零样本迁移到真实世界紧配合插入，0.5 mm 间隙成功率 6/10"
+created_at: "2026-07-15T12:20:00+08:00"
+updated_at: "2026-07-15T12:20:00+08:00"
+aliases: []
+tags: ["sim-to-real", "dexterous-manipulation", "assembly"]
+domains: ["robotics"]
+confidence: "medium"
+source_ids: ["source_05d8a9da9e0b53b94872f2a7"]
+relations: [{"type": "derived_from", "target_id": "source_05d8a9da9e0b53b94872f2a7", "reason": "由 Play2Perfect 原始论文归纳"}]
+superseded_by: null
+valid_during: null
+change_reason: "批量导入原始论文知识；等待人工核验"
+applicability: ["Tight-Insertion 真实部署", "FoundationPose 跟踪、无 real-world finetuning", "10 rollouts/条件", "Sharpa + KUKA iiwa 14"]
+uncertainty: "仅 10 次 rollout/条件；依赖 FoundationPose；摘要 60% 与 Table 1 的 6/10 一致。"
+evidence: [{"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 1 页 Abstract", "excerpt": "achieving 60% success on tight insertions with only 0.5 mm contact clearance", "stance": "supports", "reason": "摘要给出 0.5 mm 成功率。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 8 页 Table 1", "excerpt": "Success Rate 10/10 9/10 6/10", "stance": "supports", "reason": "Table 1 各 clearance 成功次数。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 8 页 Section 4.4", "excerpt": "using FoundationPose for object pose tracking and no real-world finetuning", "stance": "context", "reason": "限定 sim-to-real 设定。"}]
+---
+
+# 真实世界紧插入
+
+10mm:10/10; 2mm:9/10; 0.5mm:6/10。
```
