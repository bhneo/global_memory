---
id: "proposal_e7802e7d25ad8b5646d392f1"
type: "proposal"
status: "pending"
title: "模型提议：该文称 Kairos-HomeWorld 采用四阶段分层生成（全局结构—局部细节—闭环校验—交互增强）实现全屋可交互 3D 场景"
created_at: "2026-07-16T00:59:29+08:00"
updated_at: "2026-07-16T00:59:29+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_a20c5fb22d91216503d413e1"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_kairos_four_stage_generation_20260716"
target_path: "vault/knowledge/claims/claim_wechat_kairos_four_stage_generation_20260716-该文称-kairos-homeworld-采用四阶段分层生成-全局结构-局部细节-闭环校验-交互增强-实现全屋可交互-3d-场景.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_e7802e7d25ad8b5646d392f1.md"
candidate_sha256: "13051f22dfcdb9b887c7349e10f2b55d9bb4260ae40d5c4ad9c5b9bc2494381e"
change_reason: "导入 claim_wechat_kairos_four_stage_generation_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_a20c5fb22d91216503d413e1", "input_sha256": "10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "uncertainty": "厂商发布稿；规模/效果宣称需回 kairos-homeworld.github.io 与论文核验。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称 Kairos-HomeWorld 采用四阶段分层生成（全局结构—局部细节—闭环校验—交互增强）实现全屋可交互 3D 场景

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_a20c5fb22d91216503d413e1`
- Input SHA-256：`10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8`
- 不确定性：厂商发布稿；规模/效果宣称需回 kairos-homeworld.github.io 与论文核验。
- 提议理由：导入 claim_wechat_kairos_four_stage_generation_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_kairos_four_stage_generation_20260716-该文称-kairos-homeworld-采用四阶段分层生成-全局结构-局部细节-闭环校验-交互增强-实现全屋可交互-3d-场景.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_kairos_four_stage_generation_20260716"
+title: "该文称 Kairos-HomeWorld 采用四阶段分层生成（全局结构—局部细节—闭环校验—交互增强）实现全屋可交互 3D 场景"
+tags: ["kairos-homeworld", "scene-generation", "world-model"]
+domains: ["robotics", "computer-vision"]
+confidence: "low"
+applicability: ["文本到全屋 3D 生成 pipeline 科普", "K-D 树平面图表示讨论"]
+uncertainty: "技术细节来自宣传稿；碰撞率等量化指标未给独立 benchmark。"
+evidence: [{"evidence_id": "ev_1179", "evidence_kind": "quote", "source_id": "source_a20c5fb22d91216503d413e1", "content_id": "content_10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "extraction_id": "extraction_a5edbc0cf2b49e4a1ec77b62", "input_sha256": "10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "span_start": 1179, "span_end": 1208, "original_text": "四阶段分层生成架构（全局结构—局部细节—闭环校验—交互增强", "section": "四阶段架构", "stance": "supports", "verification_status": "verified", "reason": "文内对四阶段 pipeline 的命名。"}, {"evidence_id": "ev_1341", "evidence_kind": "quote", "source_id": "source_a20c5fb22d91216503d413e1", "content_id": "content_10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "extraction_id": "extraction_a5edbc0cf2b49e4a1ec77b62", "input_sha256": "10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "span_start": 1341, "span_end": 1484, "original_text": "K-D树的平面图结构化表示方法，将真实住宅平面图转化为大语言模型可高效学习的分层文本结构，避免房间重叠、拓扑断裂等传统户型生成方法的缺陷。第二阶段采用\"俯视图全局初始化+第一人称细节漫游\"的分层策略，以一阶段生成的3D建筑外壳锚定整个生成过程，解决了2D-3D提升方法普遍存在的几何漂移", "section": "平面图表示", "stance": "supports", "verification_status": "verified", "reason": "文内对 K-D 树平面图表示与 2D-3D 提升的说明。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-16T00:59:00+08:00"
+updated_at: "2026-07-16T00:59:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入 Kairos-HomeWorld 宣传稿；等待人工核验"
+source_ids: ["source_a20c5fb22d91216503d413e1"]
+relations: [{"type": "derived_from", "target_id": "source_a20c5fb22d91216503d413e1", "reason": "由 ACERobotics 对大晓机器人 Kairos-HomeWorld 发布稿的转载归纳；项目主页未 capture"}]
+---
+
+# 四阶段生成
+
+结构→细节→校验→可交互物体。
```
