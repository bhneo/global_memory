---
id: "proposal_22a6901bd5eb2d045eed57fc"
type: "proposal"
status: "pending"
title: "模型提议：该文称该数据集专为中国家庭户型设计，覆盖封闭式厨房、生活阳台、玄关等本土特征，区别于欧美开源室内数据"
created_at: "2026-07-16T00:59:30+08:00"
updated_at: "2026-07-16T00:59:30+08:00"
aliases: []
tags: []
domains: []
confidence: "low"
source_ids: ["source_a20c5fb22d91216503d413e1"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_kairos_china_specific_layout_20260716"
target_path: "vault/knowledge/claims/claim_wechat_kairos_china_specific_layout_20260716-该文称该数据集专为中国家庭户型设计-覆盖封闭式厨房-生活阳台-玄关等本土特征-区别于欧美开源室内数据.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_22a6901bd5eb2d045eed57fc.md"
candidate_sha256: "2bb7730eaad40207d8972e4e011ce7c50efcaf9301c6e8892c7e429c857adb0b"
change_reason: "导入 claim_wechat_kairos_china_specific_layout_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_a20c5fb22d91216503d413e1", "input_sha256": "10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "uncertainty": "厂商发布稿；规模/效果宣称需回 kairos-homeworld.github.io 与论文核验。"}
reviewed_at: null
review_reason: null
---

# 模型提议：该文称该数据集专为中国家庭户型设计，覆盖封闭式厨房、生活阳台、玄关等本土特征，区别于欧美开源室内数据

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_a20c5fb22d91216503d413e1`
- Input SHA-256：`10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8`
- 不确定性：厂商发布稿；规模/效果宣称需回 kairos-homeworld.github.io 与论文核验。
- 提议理由：导入 claim_wechat_kairos_china_specific_layout_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_kairos_china_specific_layout_20260716-该文称该数据集专为中国家庭户型设计-覆盖封闭式厨房-生活阳台-玄关等本土特征-区别于欧美开源室内数据.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_kairos_china_specific_layout_20260716"
+title: "该文称该数据集专为中国家庭户型设计，覆盖封闭式厨房、生活阳台、玄关等本土特征，区别于欧美开源室内数据"
+tags: ["china-housing", "dataset-localization", "indoor-scene"]
+domains: ["robotics", "embodied-ai"]
+confidence: "low"
+applicability: ["本土机器人训练数据本地化讨论", "与欧美 indoor scene 数据集对比"]
+uncertainty: "「水土不服」为定性判断；具体覆盖城市/户型分布需回官方数据说明。"
+evidence: [{"evidence_id": "ev_2691", "evidence_kind": "quote", "source_id": "source_a20c5fb22d91216503d413e1", "content_id": "content_10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "extraction_id": "extraction_a5edbc0cf2b49e4a1ec77b62", "input_sha256": "10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "span_start": 2691, "span_end": 2760, "original_text": "欧美居住习惯构建，普遍存在房间布局和装饰欧美化、开放式厨房、缺乏阳台功能区等问题，导致基于这些数据训练的机器人在进入中国家庭时出现水土不服", "section": "与欧美数据差异", "stance": "supports", "verification_status": "verified", "reason": "文内对欧美数据集局限的表述。"}, {"evidence_id": "ev_2850", "evidence_kind": "quote", "source_id": "source_a20c5fb22d91216503d413e1", "content_id": "content_10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "extraction_id": "extraction_a5edbc0cf2b49e4a1ec77b62", "input_sha256": "10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "span_start": 2850, "span_end": 2908, "original_text": "封闭式厨房、独立生活阳台、干湿分离卫生间、玄关鞋柜等本土居住特征，甚至包含老小区非矩形厨房、不规则客厅等常见复杂户型", "section": "本土特征", "stance": "supports", "verification_status": "verified", "reason": "文内对中国家庭布局特征的列举。"}]
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
+# 中国家庭专属
+
+本土户型特征 vs 欧美数据集。
```
