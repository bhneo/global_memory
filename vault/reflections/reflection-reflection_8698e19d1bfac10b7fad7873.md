---
id: "reflection_8698e19d1bfac10b7fad7873"
type: "reflection"
status: "active"
title: "同一 Enfold 论文的 arXiv 页面是发现载体，不是第二份独立贡献"
created_at: "2026-08-01T18:22:02+08:00"
updated_at: "2026-08-01T18:22:02+08:00"
aliases: []
tags: ["reflection", "article"]
domains: ["robotics", "world-models", "source-governance"]
confidence: "high"
source_ids: ["source_5c653d6ea053d088d13e6d5c"]
relations: []
target_ids: ["input_0695c83197b78628a87e9c2b", "source_5c653d6ea053d088d13e6d5c"]
input_id: "input_0695c83197b78628a87e9c2b"
created_by: "agent"
reflection_kind: "article"
importance: "medium"
why_important: "该 arXiv 页面提供 Enfold 的作者摘要和作品身份，但与本批完整 PDF 属于同一逻辑工作。把可读摘要与完整论文区分为来源载体而非独立贡献，可避免重复节点和虚增证据独立性。"
what_changed: "同一作品的 HTML 摘要和本地 PDF 应共享语义准入结果；Source 数量不能替代 work-level 独立性。"
surprising: "摘要足以暴露核心主张和延迟数字，却不包含生成状态层选择、梯度隔离、干预实验边界和统计限制，不能承担完整语义审查。"
connections: [{"shared_mechanism": "摘要与完整 PDF 都描述把世界生成器中间计算蒸馏进 current-only representation。", "boundary": "该网页只承担同一作品的发现与元数据角色，不构成第二份独立证据。", "difference": "完整 PDF 提供机制、消融、结果、假设和局限，承担本批 Working 语义准入。"}]
conflicts: []
open_questions: []
possible_mechanisms: []
future_directions: []
truth_layer: "reflection"
user_authored: false
execution_safe: false
---

# 同一 Enfold 论文的 arXiv 页面是发现载体，不是第二份独立贡献

## Why important

该 arXiv 页面提供 Enfold 的作者摘要和作品身份，但与本批完整 PDF 属于同一逻辑工作。把可读摘要与完整论文区分为来源载体而非独立贡献，可避免重复节点和虚增证据独立性。

## What changed

同一作品的 HTML 摘要和本地 PDF 应共享语义准入结果；Source 数量不能替代 work-level 独立性。

## Surprising

摘要足以暴露核心主张和延迟数字，却不包含生成状态层选择、梯度隔离、干预实验边界和统计限制，不能承担完整语义审查。

## Connections

- Shared mechanism: 摘要与完整 PDF 都描述把世界生成器中间计算蒸馏进 current-only representation。
  Boundary: 该网页只承担同一作品的发现与元数据角色，不构成第二份独立证据。
  Difference: 完整 PDF 提供机制、消融、结果、假设和局限，承担本批 Working 语义准入。

## Conflicts

None recorded.

## Open questions

None recorded.

## Possible mechanisms

None recorded.

## Future directions

None recorded.
