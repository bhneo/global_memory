---
id: "proposal_e55d83772be9918e1a101832"
type: "proposal"
status: "superseded"
title: "模型提议：该文称托卡马克为磁约束聚变主选装置，苏联 1950 年代发明，运行温度约 1.5–3 亿摄氏度"
created_at: "2026-07-15T20:52:19+08:00"
updated_at: "2026-07-16T16:46:32+08:00"
aliases: []
tags: []
domains: []
confidence: "medium"
source_ids: ["source_9bd3bdfb9a5b1a728c3adf25"]
relations: []
proposal_kind: "model_candidate"
processor: "external-model-candidate-v1"
action: "create"
target_id: "claim_wechat_tokamak_fusion_device_20260715"
target_path: "vault/knowledge/claims/claim_wechat_tokamak_fusion_device_20260715-该文称托卡马克为磁约束聚变主选装置-苏联-1950-年代发明-运行温度约-1-5-3-亿摄氏度.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_e55d83772be9918e1a101832.md"
candidate_sha256: "c5488a05b29e751893811e57eddbebda439325921215ad1bba1998dc3202fb4f"
change_reason: "导入 claim_wechat_tokamak_fusion_device_20260715"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_9bd3bdfb9a5b1a728c3adf25", "input_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "uncertainty": "科普文章；装置数量与 ITER 状态有时效性；聚变温度等为数量级表述。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称托卡马克为磁约束聚变主选装置，苏联 1950 年代发明，运行温度约 1.5–3 亿摄氏度

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_9bd3bdfb9a5b1a728c3adf25`
- Input SHA-256：`acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669`
- 不确定性：科普文章；装置数量与 ITER 状态有时效性；聚变温度等为数量级表述。
- 提议理由：导入 claim_wechat_tokamak_fusion_device_20260715
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_tokamak_fusion_device_20260715-该文称托卡马克为磁约束聚变主选装置-苏联-1950-年代发明-运行温度约-1-5-3-亿摄氏度.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_tokamak_fusion_device_20260715"
+title: "该文称托卡马克为磁约束聚变主选装置，苏联 1950 年代发明，运行温度约 1.5–3 亿摄氏度"
+tags: ["tokamak", "fusion", "iter"]
+domains: ["physics", "energy"]
+confidence: "medium"
+applicability: ["文内对托卡马克历史与工作原理的概述", "ITER 等实验堆语境"]
+uncertainty: "「最有希望」「目前尚未用于能源生产」为 2022 年科普时点判断；ITER 进展需独立更新。"
+evidence: [{"evidence_id": "ev_2401", "evidence_kind": "quote", "source_id": "source_9bd3bdfb9a5b1a728c3adf25", "content_id": "content_acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "extraction_id": "extraction_275083c46743bccdd54985ba", "input_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "span_start": 2401, "span_end": 2518, "original_text": "该设备最初由苏联的研究人员于上世纪50年代发明，它的主体部分是一个圆环形真空室，如下图所示。\n\n它利用套在金属环形管上的线圈产生一个纵向磁场  ，利用等离子体中的感应电流激发角向磁场  ，二者合成总的磁场  ，它也是一种螺旋形状磁场。", "section": "托卡马克起源", "stance": "supports", "verification_status": "verified", "reason": "文内对托卡马克发明与磁场合成的描述。"}, {"evidence_id": "ev_2558", "evidence_kind": "quote", "source_id": "source_9bd3bdfb9a5b1a728c3adf25", "content_id": "content_acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "extraction_id": "extraction_275083c46743bccdd54985ba", "input_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "span_start": 2558, "span_end": 2631, "original_text": "利用辅助加热系统将温度提高到聚变所需的水平（1.5-3亿摄氏度）。在这些条件下，高能量粒子能够克服碰撞时的自然电磁排斥，使其聚合并释放出大量能量。", "section": "运行温度", "stance": "supports", "verification_status": "verified", "reason": "文内给出的托卡马克等离子体温度范围。"}, {"evidence_id": "ev_2632", "evidence_kind": "quote", "source_id": "source_9bd3bdfb9a5b1a728c3adf25", "content_id": "content_acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "extraction_id": "extraction_275083c46743bccdd54985ba", "input_sha256": "acdb10c5d1a22a783c661c333c5a59a2e896d8cd917f92fec72a922a03cfe669", "span_start": 2632, "span_end": 2710, "original_text": "由于启动和维持聚变反应的能量门槛太高，托克马克目前还没有用于能源生产。法国正在建造的ITER托克马克——目前世界上最厉害的托克马克，有望能逐步实现这一目标。", "section": "能源应用状态", "stance": "supports", "verification_status": "verified", "reason": "文内对托卡马克尚未商用与 ITER 期望的表述。"}]
+type: "claim"
+status: "proposal"
+created_at: "2026-07-15T20:30:00+08:00"
+updated_at: "2026-07-15T20:30:00+08:00"
+aliases: []
+superseded_by: null
+valid_during: null
+change_reason: "批量导入等离子体磁约束科普；等待人工核验"
+source_ids: ["source_9bd3bdfb9a5b1a728c3adf25"]
+relations: [{"type": "derived_from", "target_id": "source_9bd3bdfb9a5b1a728c3adf25", "reason": "由中科院物理所转载的等离子体/磁约束科普文章归纳；非原始实验论文"}]
+---
+
+# 托卡马克
+
+1950 年代苏联发明；1.5–3 亿°C；ITER 候选。
```
