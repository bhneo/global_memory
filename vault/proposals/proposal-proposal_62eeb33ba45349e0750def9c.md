---
id: "proposal_62eeb33ba45349e0750def9c"
type: "proposal"
status: "superseded"
title: "模型提议：该文称 Kairos-HomeWorld 开源含 30 万中国真实平面图、5000 个全屋仿真场景与 5 万可交互物体资产"
created_at: "2026-07-16T00:59:29+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_a20c5fb22d91216503d413e1"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_kairos_dataset_scale_20260716"
target_path: "vault/knowledge/claims/claim_wechat_kairos_dataset_scale_20260716-该文称-kairos-homeworld-开源含-30-万中国真实平面图-5000-个全屋仿真场景与-5-万可交互物体资产.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_62eeb33ba45349e0750def9c.md"
candidate_sha256: "e44205de5d59446267803d1555c411742133cef5bb01c19bc45fd54e4e851cb1"
change_reason: "导入 claim_wechat_kairos_dataset_scale_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_a20c5fb22d91216503d413e1", "input_sha256": "10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "uncertainty": "厂商发布稿；规模/效果宣称需回 kairos-homeworld.github.io 与论文核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称 Kairos-HomeWorld 开源含 30 万中国真实平面图、5000 个全屋仿真场景与 5 万可交互物体资产

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_a20c5fb22d91216503d413e1`
- Input SHA-256：`10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8`
- 不确定性：厂商发布稿；规模/效果宣称需回 kairos-homeworld.github.io 与论文核验。
- 提议理由：导入 claim_wechat_kairos_dataset_scale_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_kairos_dataset_scale_20260716-该文称-kairos-homeworld-开源含-30-万中国真实平面图-5000-个全屋仿真场景与-5-万可交互物体资产.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_kairos_dataset_scale_20260716"
+title: "该文称 Kairos-HomeWorld 开源含 30 万中国真实平面图、5000 个全屋仿真场景与 5 万可交互物体资产"
+tags: ["kairos-homeworld", "dataset", "simulation"]
+domains: ["robotics", "embodied-ai"]
+confidence: "low"
+applicability: ["中国家庭全屋 3D 数据集规模对比 RPLAN/ResPlan 语境", "2026-06 发布稿"]
+uncertainty: "为厂商/公众号宣传稿；「全球最大」等表述需回项目主页与论文核验。"
+evidence: [{"evidence_id": "ev_374", "evidence_kind": "quote", "source_id": "source_a20c5fb22d91216503d413e1", "content_id": "content_10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "extraction_id": "extraction_a5edbc0cf2b49e4a1ec77b62", "input_sha256": "10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "span_start": 374, "span_end": 426, "original_text": "30万套真实平面图、5000个完整仿真场景，每个场景平均超15个可操作物体，且全部可直接拖入仿真引擎训练", "section": "数据集规模（开篇）", "stance": "supports", "verification_status": "verified", "reason": "文内开篇对数据集规模的说明。"}, {"evidence_id": "ev_1996", "evidence_kind": "quote", "source_id": "source_a20c5fb22d91216503d413e1", "content_id": "content_10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "extraction_id": "extraction_a5edbc0cf2b49e4a1ec77b62", "input_sha256": "10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "span_start": 1996, "span_end": 2045, "original_text": "30万张经过结构化标注的真实住宅平面图、5千个具有完整室内布局与家具布置的全屋仿真场景，以及5万个", "section": "数据集规模（详述）", "stance": "supports", "verification_status": "verified", "reason": "文内对平面图、场景与物体资产数量的详述。"}]
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
+# Kairos 数据规模
+
+30万户型/5千场景/5万物体；宣传性数字待核验。
```
