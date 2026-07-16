---
id: "claim_wechat_param_symmetry_definition_20260716"
title: "该文称参数空间对称性是保持损失函数不变的参数变换，并在参数空间中形成等价轨道"
tags: ["parameter-symmetry", "loss-landscape", "group-theory"]
domains: ["deep-learning", "optimization"]
confidence: "medium"
applicability: ["置换对称等函数等价参数配置讨论", "2506.13018 综述科普语境"]
uncertainty: "为机器之心科普转述；形式化群论表述需回 arXiv:2506.13018 核验。"
evidence: [{"evidence_id": "ev_210", "evidence_kind": "quote", "source_id": "source_6ae6c4bef52010f96ddb3dbf", "content_id": "content_1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "extraction_id": "extraction_4806a53e6b1eaf92d41816d5", "input_sha256": "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "span_start": 210, "span_end": 626, "original_text": "parameter space symmetry）。这篇长达三十页的论文揭示了对称性如何塑造损失地形、影响优化与训练动力学，并为理解深度学习提供了一个统一的几何视角。\n\n论文链接：https://arxiv.org/abs/2506.13018\n\n作者主页：https://b-zhao.github.io/\n\n什么是参数空间对称性？\n\n在一个神经网络中，不同的参数组合可能产生完全相同的输出。最直观的例子是神经元置换：交换隐藏层中两个神经元及其对应的输入 / 输出权重，网络实现的函数不变。\n\n图1 置换对称：交换隐藏层两个单元及其关联权重，函数保持不变\n\n这类保持函数不变的参数变换，被称为参数空间对称性 (parameter space symmetry)。\n\n数学上，它是一组使损失函数 L (θ) 保持不变的变换 g，即 L (g ⋅ θ) = L (θ)。这些变换构成一个群 (group)，并在参数空间中定义了等价轨道", "section": "对称性定义", "stance": "supports", "verification_status": "verified", "reason": "文内对参数空间对称性与轨道的说明。"}, {"evidence_id": "ev_576", "evidence_kind": "quote", "source_id": "source_6ae6c4bef52010f96ddb3dbf", "content_id": "content_1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "extraction_id": "extraction_4806a53e6b1eaf92d41816d5", "input_sha256": "1f67ffbd82de0a35e47bc93a507a2c05176ac8bb8262a07cefad2db996b0684e", "span_start": 576, "span_end": 593, "original_text": "L (g ⋅ θ) = L (θ)", "section": "损失不变性", "stance": "supports", "verification_status": "verified", "reason": "文内对对称变换保持损失的形式化表述。"}]
type: "claim"
status: "proposal"
created_at: "2026-07-16T00:06:00+08:00"
updated_at: "2026-07-16T00:06:00+08:00"
aliases: []
superseded_by: null
valid_during: null
change_reason: "批量导入参数空间对称性科普；等待人工核验"
source_ids: ["source_6ae6c4bef52010f96ddb3dbf"]
relations: [{"type": "derived_from", "target_id": "source_6ae6c4bef52010f96ddb3dbf", "reason": "由机器之心对 arXiv:2506.13018 参数空间对称性综述的科普转述归纳；原论文未 capture"}]
---

# 参数空间对称性

保持 L(g·θ)=L(θ)；等价轨道表示同一函数。
