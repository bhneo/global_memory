---
id: "proposal_ef6b02dd675338f29289f9ec"
type: "proposal"
status: "pending"
title: "模型提议：该文称 2021 最佳视错觉大赛第一名「幽灵女王」由 Matt Pritchard 创作，白棋被「隐形斗篷」纸板遮挡却在镜中可见"
created_at: "2026-07-15T21:30:14+08:00"
updated_at: "2026-07-15T21:30:14+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_046487376d500224386ff628"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_ghost_queen_illusion_20260715"
target_path: "vault/knowledge/claims/claim_wechat_ghost_queen_illusion_20260715-该文称-2021-最佳视错觉大赛第一名-幽灵女王-由-matt-pritchard-创作-白棋被-隐形斗篷-纸板遮挡却在镜中可见.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_ef6b02dd675338f29289f9ec.md"
candidate_sha256: "6135323248436ad480cf8f728baf6f324c2af02b7c3ac8799b36fd80d17d59c3"
change_reason: "导入 claim_wechat_ghost_queen_illusion_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_046487376d500224386ff628", "input_sha256": "591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "uncertainty": "科普文章；获奖与实验细节需回 Best Illusion 官方或原论文核验。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称 2021 最佳视错觉大赛第一名「幽灵女王」由 Matt Pritchard 创作，白棋被「隐形斗篷」纸板遮挡却在镜中可见

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_046487376d500224386ff628`
- Input SHA-256：`591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7`
- 不确定性：科普文章；获奖与实验细节需回 Best Illusion 官方或原论文核验。
- 提议理由：导入 claim_wechat_ghost_queen_illusion_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_ghost_queen_illusion_20260715-该文称-2021-最佳视错觉大赛第一名-幽灵女王-由-matt-pritchard-创作-白棋被-隐形斗篷-纸板遮挡却在镜中可见.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_ghost_queen_illusion_20260715"
+title: "该文称 2021 最佳视错觉大赛第一名「幽灵女王」由 Matt Pritchard 创作，白棋被「隐形斗篷」纸板遮挡却在镜中可见"
+tags: ["optical-illusion", "best-illusion-contest", "mirror-illusion"]
+domains: ["psychology", "perception"]
+confidence: "medium"
+applicability: ["2021 年度最佳视错觉大赛第一名作品介绍", "棋盘+镜子场景"]
+uncertainty: "机制描述为科普转述；Matt Pritchard 获奖信息未 capture 官方 contest 页面；图片素材文内称来自网络。"
+evidence: [{"evidence_id": "ev_86", "evidence_kind": "quote", "source_id": "source_046487376d500224386ff628", "content_id": "content_591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "extraction_id": "extraction_8e6bec146e8c61326ddc9aca", "input_sha256": "591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "span_start": 86, "span_end": 129, "original_text": "幽灵女王这是今年获得第一名的视错觉作品，作者是来自英国的Matt Pritchard。", "section": "第一名与作者", "stance": "supports", "verification_status": "verified", "reason": "文内对作品名次与作者的说明。"}, {"evidence_id": "ev_259", "evidence_kind": "quote", "source_id": "source_046487376d500224386ff628", "content_id": "content_591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "extraction_id": "extraction_8e6bec146e8c61326ddc9aca", "input_sha256": "591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "span_start": 259, "span_end": 288, "original_text": "白色棋子原本就在棋盘上，只不过上面遮盖了一层「隐形斗篷」。", "section": "隐形斗篷机制", "stance": "supports", "verification_status": "verified", "reason": "文内对遮挡机制的核心解释。"}, {"evidence_id": "ev_456", "evidence_kind": "quote", "source_id": "source_046487376d500224386ff628", "content_id": "content_591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "extraction_id": "extraction_8e6bec146e8c61326ddc9aca", "input_sha256": "591e25dfb5ae1789e1db3c5056e1b4a939173d007b0c39e7cacc3a63d7fd89b7", "span_start": 456, "span_end": 487, "original_text": "但这并不妨碍镜子映出那颗白棋，也就是镜子里有，但我们眼前没有：", "section": "镜子可见", "stance": "supports", "verification_status": "verified", "reason": "文内对镜中可见、肉眼不可见的对比。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-15T21:25:00+08:00"
+updated_at: "2026-07-15T21:25:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入视错觉科普；等待人工核验"
+source_ids: ["source_046487376d500224386ff628"]
+relations: [{"type": "derived_from", "target_id": "source_046487376d500224386ff628", "reason": "由中科院物理所转载的 2021 最佳视错觉大赛科普文章归纳；非原始实验论文"}]
+---
+
+# 幽灵女王
+
+纸板图案与棋盘重合遮挡；镜中仍映出白棋。
```
