# ADR 0055 — Research Signals and Borrow-Before-Build

Status: accepted  
Date: 2026-07-18

## Decision

M9.0 先记录真实科研注意力、连接反馈和使用信号，再设计自动科学发现能力。

1. 用户注意力信号是长期科研资产，以 append-only Annotation 保存。
2. Annotation 的用户原文与 Agent Interpretation 分离。
3. Activation 与 Trust、Evidence、Epistemic Status 和 Receipt 正交。
4. Project/Domain 路由优先于全库检索，并输出 Route Trace。
5. Feedback 描述研究价值，不描述对象真实性。
6. 外部产品优先通过只读 Service、CLI、MCP 或 Adapter 接入。
7. 科学发现核心不外包；本地 Raw/Markdown 始终是真相源。
8. 当前阶段只记录信号，不自动学习用户研究偏好，不改变默认排序。

## Consequences

Annotation 可进入 Research/Exploration Context，但必须标记 `truth_layer: user_annotation`；Execution 不把它当事实。Activation 日志和 Research Map/Digest 是本地派生产物。M9.0 不引入 embedding、向量/图数据库、新 Web UI、写 MCP、自动类比、自动假设、自动实验或自动 Canonical。
