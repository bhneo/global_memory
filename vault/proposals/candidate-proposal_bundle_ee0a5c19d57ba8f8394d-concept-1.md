---
id: "concept_2baeb2cc7c9fb6cc84e1614f"
type: "concept"
status: "proposal"
title: "Kakeya 近极值几何中的 planiness、graininess 与 stickiness / planiness, graininess, and stickiness in near-extremal Kakeya geometry"
created_at: "2026-07-27T09:43:08+08:00"
updated_at: "2026-07-27T16:45:32+08:00"
aliases: ["sticky Kakeya 满维特例", "full dimension for sticky Kakeya sets"]
tags: []
domains: ["harmonic-analysis", "kakeya", "multiscale-geometry"]
confidence: "high"
source_ids: ["source_a44d98212ed6d44a4998646e", "source_32ee0cb3589fdf1de3cb8542"]
relations: [{"type": "derived_from", "target_id": "source_a44d98212ed6d44a4998646e", "reason": "由 compile bundle 从该来源提出", "confidence": "high", "created_by": "codex-gpt56-m91-real-daily-v1", "status": "working"}]
change_reason: "compile bundle from source_32ee0cb3589fdf1de3cb8542"
change_type: "refine"
reflection_context: {"reflection_ids": ["reflection_1d6487542a928a1a5708e64a"], "importance": "high", "changed_belief": "我会把 sticky 结构视为分析潜在近极值构型的条件化工具，不把该 R3 特例误读成一般 Kakeya 猜想已解决。", "surprising": "", "connections": [{"shared_mechanism": "两者都用跨尺度的管族组织、planiness 与受控聚集来排除过度集中的近极值几何。", "boundary": "本文限于满足 sticky 定义的线族，在 R3 中证明其 Hausdorff 与 Minkowski 维数为 3。", "difference": "既有近极值对象描述可能的 planiness、graininess 与弱 Lipschitz stickiness；本文提供 sticky 特例满维的定理，而不覆盖任意 Kakeya 集。"}], "open_questions": ["能否证明一般近极值 Kakeya 配置必然满足足够的 sticky 结构，或用其他机制处理非-sticky 配置？"]}
proposed_status: "working"
---

# Kakeya 维数下界中的近极值几何结构分析

在 R3 的 Besicovitch/Kakeya 维数问题中，改进 Hausdorff 维数下界的一条证明路线会研究假设的小体积或近阈值管族：典型点附近的管方向近似共面、这些平面随位置受控变化，以及方向到管的对应呈弱 Lipschitz 型粘连。此类结构是分析近极值构型的证明工具，不是对所有 Besicovitch 集都自动成立的独立几何分类。

## 新增来源材料

- `source_32ee0cb3589fdf1de3cb8542`：Wang 与 Zahl 对满足 sticky 定义的 R3 Kakeya 集证明 Hausdorff 与 Minkowski 维数均为 3：sticky 线族以 n−1 的 packing 维度在方向间组织出近似多尺度自相似。该定理只解决附加 stickiness 条件的特例，不能推出一般 R3 Kakeya 猜想。
