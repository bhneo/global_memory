# External Capability Map

Global Memory 保留不可替代的科研认知核心；成熟外围能力优先通过只读服务、CLI、MCP 或 Adapter 借用。外部系统不得成为本地 Raw/Markdown 的真相源。

```yaml
- capability: 普通文档检索与人类 UI
  external_project: Khoj
  possible_integration: 只读搜索或 UI Adapter
  license_boundary: 集成前复核当前许可证和分发条件
  trigger_to_integrate: Obsidian 与 CLI 无法满足真实日常检索时
  why_not_now: M9.0 先验证科研信号与路由
  truth_source_boundary: 只读消费者，不成为真相源

- capability: 记忆评测
  external_project: MemoryBench
  possible_integration: Global Memory Provider
  license_boundary: 不复制完整评测框架
  trigger_to_integrate: M9.1 建立检索与治理基线时
  why_not_now: 当前缺少真实研究使用样本
  truth_source_boundary: 评测结果是报告，不是知识

- capability: 时序知识图
  external_project: Graphiti
  possible_integration: 可重建派生图 Adapter
  license_boundary: 集成前复核依赖和数据模型许可
  trigger_to_integrate: typed relations 无法支持真实时序查询时
  why_not_now: 图数据库尚无必要
  truth_source_boundary: 派生图可删除，Markdown 仍为真相源

- capability: 高频 Agent Episodic Memory
  external_project: Mem0
  possible_integration: 临时 episodic cache
  license_boundary: 不委托 Trusted 或 Canonical 治理
  trigger_to_integrate: 高频会话恢复产生可测瓶颈时
  why_not_now: 当前轻量入口已满足使用
  truth_source_boundary: 不负责 Trusted 或 Canonical

- capability: Agent Context Blocks
  external_project: Letta
  possible_integration: Context Sink
  license_boundary: 不复制其运行时或数据库
  trigger_to_integrate: 多轮上下文注入需要标准化时
  why_not_now: Context Pack 已有稳定接口
  truth_source_boundary: 只消费 Context Pack，不成为数据库

- capability: Connectors
  external_project: Supermemory / Cognee
  possible_integration: Capture Adapter
  license_boundary: 原文仍必须落入本地 immutable Raw
  trigger_to_integrate: 明确连接器带来的导入收益高于维护成本时
  why_not_now: 当前主要资料可由现有 capture 导入
  truth_source_boundary: Connector 只负责传输

- capability: 后台整理模式
  external_project: ClawXMemory / Letta
  possible_integration: 受控 Working writer
  license_boundary: 不授予 Trusted 或 Canonical 写权限
  trigger_to_integrate: Working 整理积压形成可测瓶颈时
  why_not_now: daily/weekly 已能处理当前规模
  truth_source_boundary: 只能提出或写 Working

- capability: Activation / Decay
  external_project: Hippo
  possible_integration: 实验性排序权重
  license_boundary: 算法输出不得进入 Trust 指标
  trigger_to_integrate: 累积足够 Activation 数据并完成离线评测后
  why_not_now: M9.0 只收集信号，不改变排序
  truth_source_boundary: 只影响派生排序，不影响真实性
```

新增大型能力前必须回答：它是否属于科研认知核心；是否已有成熟开源方案；能否通过只读接口接入；是否会让外部数据库成为真相源；引入成本是否低于长期自研成本。
