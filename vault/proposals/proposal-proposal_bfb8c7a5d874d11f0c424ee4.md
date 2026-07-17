---
id: "proposal_bfb8c7a5d874d11f0c424ee4"
type: "proposal"
status: "migrated"
title: "Work enrichment：[2605.10500] SkillEvolver: Skill Learning as a Meta-Skill"
created_at: "2026-07-16T18:04:45+08:00"
updated_at: "2026-07-17T11:59:20+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_0214d3d2f8cddf30a1140f8a", "source_ca1f80f2bf2e7d410ab2459e"]
relations: []
proposal_kind: "work_enrichment"
processor: "deterministic-work-identity-v1"
action: "create"
target_id: "work_arxiv_2605_10500"
target_path: "vault/knowledge/works/work_arxiv_2605_10500-2605-10500-skillevolver-skill-learning-as-a-meta-skill.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_bfb8c7a5d874d11f0c424ee4.md"
candidate_sha256: "eb01f02245d6263b8b70d95374036d52b4ac55eb6cf58163d45c05a62bb9b661"
change_reason: "显式 work identity enrichment"
reviewed_at: null
review_reason: null
migration_mode: "working-ingestion-v1"
---

# Work enrichment：[2605.10500] SkillEvolver: Skill Learning as a Meta-Skill

Metadata enrichment 不修改 source capture；审批后只创建或更新 logical work。

## Diff

```diff
--- /dev/null
+++ vault/knowledge/works/work_arxiv_2605_10500-2605-10500-skillevolver-skill-learning-as-a-meta-skill.md
@@ -0,0 +1,35 @@
+---
+id: "work_arxiv_2605_10500"
+type: "work"
+status: "proposal"
+title: "[2605.10500] SkillEvolver: Skill Learning as a Meta-Skill"
+canonical_title: "[2605.10500] SkillEvolver: Skill Learning as a Meta-Skill"
+created_at: "2026-07-16T18:04:45+08:00"
+updated_at: "2026-07-16T18:04:45+08:00"
+aliases: ["arxiv.org"]
+tags: []
+domains: []
+confidence: "medium"
+source_ids: ["source_0214d3d2f8cddf30a1140f8a", "source_ca1f80f2bf2e7d410ab2459e"]
+relations: [{"type": "derived_from", "target_id": "source_0214d3d2f8cddf30a1140f8a", "reason": "该 capture 属于此 logical work"}, {"type": "derived_from", "target_id": "source_ca1f80f2bf2e7d410ab2459e", "reason": "该 capture 属于此 logical work"}]
+work_type: "paper"
+authors: []
+published_at: null
+doi: null
+arxiv_id: "2605.10500"
+repository_url: null
+version: null
+language: "und"
+same_work_as: []
+supersedes_version: null
+---
+
+# [2605.10500] SkillEvolver: Skill Learning as a Meta-Skill
+
+## Logical work identity
+
+- arXiv：`2605.10500`
+- Version：`unknown`
+- Captures：`source_0214d3d2f8cddf30a1140f8a`, `source_ca1f80f2bf2e7d410ab2459e`
+
+此对象聚合现实世界作品身份，不替代任何 source capture 的 provenance。
```
