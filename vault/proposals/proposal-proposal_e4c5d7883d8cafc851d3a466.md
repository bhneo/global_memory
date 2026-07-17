---
id: "proposal_e4c5d7883d8cafc851d3a466"
type: "proposal"
status: "migrated"
title: "修订：模型提议：Play2Perfect 仿真微调策略可零样本迁移到真实世界紧配合插入，0.5 mm 间隙成功率 6/10"
created_at: "2026-07-15T14:28:04+08:00"
updated_at: "2026-07-17T12:00:05+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"]
relations: [{"type": "supersedes", "target_id": "proposal_8f4f674531190e1f2c7c400a", "reason": "人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份"}]
proposal_kind: "knowledge_revision"
processor: "human-candidate-revision-v1"
action: "create"
target_id: "claim_play2perfect_realworld_tight_insertion_20260715"
target_path: "vault/knowledge/claims/claim_play2perfect_realworld_tight_insertion_20260715-play2perfect-仿真微调策略可零样本迁移到真实世界紧配合插入-0-5-mm-间隙成功率-6-10.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_e4c5d7883d8cafc851d3a466.md"
candidate_sha256: "4496101420695eb52879175a9be69b74c16c7cf7ebc149a42b0fe544eb4aeb2d"
change_reason: "人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份"
revision_of: "proposal_8f4f674531190e1f2c7c400a"
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# 修订：模型提议：Play2Perfect 仿真微调策略可零样本迁移到真实世界紧配合插入，0.5 mm 间隙成功率 6/10

## 修订说明

- 被替代 proposal：`proposal_8f4f674531190e1f2c7c400a`
- 修订理由：人工对照 PDF 后补全可读正文、收紧结论范围并修正来源身份
- 建议操作：`create` `vault/knowledge/claims/claim_play2perfect_realworld_tight_insertion_20260715-play2perfect-仿真微调策略可零样本迁移到真实世界紧配合插入-0-5-mm-间隙成功率-6-10.md`
- 原 candidate 保持不可变；本 proposal 使用新的 candidate。

## Base → Revised Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_play2perfect_realworld_tight_insertion_20260715-play2perfect-仿真微调策略可零样本迁移到真实世界紧配合插入-0-5-mm-间隙成功率-6-10.md
@@ -0,0 +1,26 @@
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
+source_ids: ["source_ea5eb55121fccd1ed14a40b0", "source_05d8a9da9e0b53b94872f2a7"]
+relations: [{"type": "derived_from", "target_id": "source_ea5eb55121fccd1ed14a40b0", "reason": "Play2Perfect 官方 arXiv 页面"}, {"type": "derived_from", "target_id": "source_05d8a9da9e0b53b94872f2a7", "reason": "本地保存的 Play2Perfect 原始 PDF 提供页码证据"}]
+superseded_by: null
+valid_during: null
+change_reason: "批量导入原始论文知识；等待人工核验"
+applicability: ["Tight-Insertion 真实部署", "FoundationPose 跟踪、无 real-world finetuning", "10 rollouts/条件", "Sharpa + KUKA iiwa 14"]
+uncertainty: "仅 10 次 rollout/条件；依赖 FoundationPose；摘要 60% 与 Table 1 的 6/10 一致。"
+evidence: [{"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 1 页 Abstract", "excerpt": "achieving 60% success on tight insertions with only 0.5 mm contact clearance", "stance": "supports", "reason": "摘要给出 0.5 mm 成功率。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 8 页 Table 1", "excerpt": "Success Rate 10/10 9/10 6/10", "stance": "supports", "reason": "Table 1 各 clearance 成功次数。"}, {"source_id": "source_05d8a9da9e0b53b94872f2a7", "location": "第 8 页 Section 4.4", "excerpt": "using FoundationPose for object pose tracking and no real-world finetuning", "stance": "context", "reason": "限定 sim-to-real 设定。"}]
+---
+
+# Play2Perfect 的真实世界紧配合插入结果
+
+论文将完全在仿真中微调的 Play2Perfect 部署到真实 Sharpa 手与 KUKA iiwa 14 系统，使用 FoundationPose 跟踪物体，并且没有进行 real-world finetuning。在 Tight-Insertion 的 10 次 rollout/条件中，10 mm、2 mm 和 0.5 mm clearance 分别取得 `10/10`、`9/10` 和 `6/10`。
+
+该结果证明的是论文特定硬件、视觉跟踪和插入任务上的零样本 sim-to-real 表现。每个条件只有 10 次 rollout，失败仍集中在最终接触阶段，因此不能外推为一般真实装配可靠性。
```
