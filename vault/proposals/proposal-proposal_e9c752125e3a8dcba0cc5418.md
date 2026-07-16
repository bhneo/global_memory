---
id: "proposal_e9c752125e3a8dcba0cc5418"
type: "proposal"
status: "superseded"
title: "模型提议：该文称每场景平均 15+ 可操作物体，借助 Physx-Omni 赋予密度/铰接/流形等属性并可导入仿真引擎"
created_at: "2026-07-16T00:59:30+08:00"
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
target_id: "claim_wechat_kairos_interactive_objects_20260716"
target_path: "vault/knowledge/claims/claim_wechat_kairos_interactive_objects_20260716-该文称每场景平均-15-可操作物体-借助-physx-omni-赋予密度-铰接-流形等属性并可导入仿真引擎.md"
base_path: null
base_sha256: null
candidate_path: "vault/proposals/candidate-proposal_e9c752125e3a8dcba0cc5418.md"
candidate_sha256: "eb9502decbf76783d9d7d317eb5e95ab160eb973f52e83ca5ce12643bb9603ae"
change_reason: "导入 claim_wechat_kairos_interactive_objects_20260716"
model_run: {"provider": "cursor", "model": "composer-2.5", "prompt_version": "knowledge-import-v2", "prompt_sha256": null, "input_source_id": "source_a20c5fb22d91216503d413e1", "input_sha256": "10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "uncertainty": "厂商发布稿；规模/效果宣称需回 kairos-homeworld.github.io 与论文核验。"}
reviewed_at: null
review_reason: "由当前唯一 M6 corpus bundle 接替；修复旧幂等性运行指针"
superseded_by: "proposal_corpus_m6_6078ce0966734a116581"
---

# 模型提议：该文称每场景平均 15+ 可操作物体，借助 Physx-Omni 赋予密度/铰接/流形等属性并可导入仿真引擎

## 模型运行记录

- Provider：`cursor`
- Model：`composer-2.5`
- Prompt version：`knowledge-import-v2`
- Prompt SHA-256：`not-recorded`
- Input source：`source_a20c5fb22d91216503d413e1`
- Input SHA-256：`10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8`
- 不确定性：厂商发布稿；规模/效果宣称需回 kairos-homeworld.github.io 与论文核验。
- 提议理由：导入 claim_wechat_kairos_interactive_objects_20260716
- 隐私边界：此命令不调用 provider；candidate 由用户在仓库外生成后显式提供。

## Base → Candidate Diff

```diff
--- /dev/null
+++ candidate:vault/knowledge/claims/claim_wechat_kairos_interactive_objects_20260716-该文称每场景平均-15-可操作物体-借助-physx-omni-赋予密度-铰接-流形等属性并可导入仿真引擎.md
@@ -0,0 +1,24 @@
+---
+id: "claim_wechat_kairos_interactive_objects_20260716"
+title: "该文称每场景平均 15+ 可操作物体，借助 Physx-Omni 赋予密度/铰接/流形等属性并可导入仿真引擎"
+tags: ["physx-omni", "interactive-objects", "simulation"]
+domains: ["robotics", "simulation"]
+confidence: "low"
+applicability: ["物体级交互仿真训练", "足迹物体密度 4.16 宣传指标"]
+uncertainty: "Physx-Omni 与 footprint density 4.16 为稿内自述；独立评测未 capture。"
+evidence: [{"evidence_id": "ev_1668", "evidence_kind": "quote", "source_id": "source_a20c5fb22d91216503d413e1", "content_id": "content_10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "extraction_id": "extraction_a5edbc0cf2b49e4a1ec77b62", "input_sha256": "10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "span_start": 1668, "span_end": 1711, "original_text": "15 个可操作物体，足迹物体密度（衡量家具表面上物体的密集程度与功能丰富度）达4.16", "section": "物体密度指标", "stance": "supports", "verification_status": "verified", "reason": "文内对可操作物体数量与足迹密度的说明。"}, {"evidence_id": "ev_2326", "evidence_kind": "quote", "source_id": "source_a20c5fb22d91216503d413e1", "content_id": "content_10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "extraction_id": "extraction_a5edbc0cf2b49e4a1ec77b62", "input_sha256": "10e43892aa54422eea042c9a487dddbfe1225fcc01652c5b0b63b1419a257fd8", "span_start": 2326, "span_end": 2555, "original_text": "Physx-Omni模型，自动生成平均15+个带物理属性（包含密度、铰接、流形等）的可交互对象，且全部支持直接导入仿真引擎进行交互式训练。\n\n图注：全球室内场景资源对比表，其中各符号与术语的含义如下：Rec. 代表基于重建的真实世界数据集；S./H. 分别指代带家具场景数（单个、通常为房间级别的独立区域）与住宅数（包含多个房间的统一完整住宅）；Sim-ready 即仿真就绪度，用于衡量数据集是否提供可直接在仿真 / 渲染引擎中实例化、并支持物体级交互操作", "section": "Physx-Omni", "stance": "supports", "verification_status": "verified", "reason": "文内对物理属性生成与仿真导入的说明。"}]
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
+# 可交互物体
+
+15+ 物体/场景；Physx-Omni 物理属性。
```
