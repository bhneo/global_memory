---
id: "reflection_9f1bface11ec7ba8723e8def"
type: "reflection"
status: "active"
title: "HY-Embodied 仓库：为论文主张补充可运行工件而非第二份事实"
created_at: "2026-07-21T17:45:20+08:00"
updated_at: "2026-07-21T17:45:20+08:00"
aliases: []
tags: ["reflection", "project"]
domains: ["embodied-ai", "open-source", "vision-language-model"]
confidence: "medium"
source_ids: ["source_ffef0c68258ab78320bbe42f"]
relations: []
target_ids: ["input_a4c337f6b32f32e230317ac9", "source_ffef0c68258ab78320bbe42f"]
input_id: "input_a4c337f6b32f32e230317ac9"
created_by: "agent"
reflection_kind: "project"
importance: "medium"
why_important: "仓库提供模型权重、推理代码、benchmark 表和技术报告，可用于核对可用性与复现入口，但与 arXiv 论文属于同一项目来源。"
what_changed: "配套 GitHub 应作为论文对象的应用和复现 provenance，而不应再制造一个重复模型概念。"
surprising: "仓库同时包含 Hy-Embodied-VLM、HY-VLA 与早期版本，若只按仓库标题消化会把视觉语言推理和动作策略能力混为一谈。"
connections: [{"shared_mechanism": "论文与仓库描述同一模型发布。", "boundary": "代码和权重可用性不独立验证 benchmark 或真机能力。", "difference": "论文给出研究主张；仓库给出版本、权重、推理入口和项目状态。"}]
conflicts: []
open_questions: ["公开权重能否复现项目页列出的 38 项 benchmark 结果？"]
possible_mechanisms: []
future_directions: ["按版本固定 commit、模型权重和评测配置后进行独立复现。"]
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# HY-Embodied 仓库：为论文主张补充可运行工件而非第二份事实

## Why important

仓库提供模型权重、推理代码、benchmark 表和技术报告，可用于核对可用性与复现入口，但与 arXiv 论文属于同一项目来源。

## What changed

配套 GitHub 应作为论文对象的应用和复现 provenance，而不应再制造一个重复模型概念。

## Surprising

仓库同时包含 Hy-Embodied-VLM、HY-VLA 与早期版本，若只按仓库标题消化会把视觉语言推理和动作策略能力混为一谈。

## Connections

- Shared mechanism: 论文与仓库描述同一模型发布。
  Boundary: 代码和权重可用性不独立验证 benchmark 或真机能力。
  Difference: 论文给出研究主张；仓库给出版本、权重、推理入口和项目状态。

## Conflicts

None recorded.

## Open questions

- 公开权重能否复现项目页列出的 38 项 benchmark 结果？

## Possible mechanisms

None recorded.

## Future directions

- 按版本固定 commit、模型权重和评测配置后进行独立复现。
