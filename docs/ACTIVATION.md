# Activation

Activation 只表示某条记忆最近在真实工作中有多活跃。它与 Trust 完全正交：Truth 不等于 Recency，Frequency 不等于 Correctness。

事件写入本地 `system/logs/activation-events.jsonl`，支持 `selected|opened|used|cited|coactivated`。SQLite 中的事件和聚合表可从 JSONL 重建；事件不写知识 Markdown、不使 Receipt 失效，也不改变 Evidence、Tier、Epistemic Status、Contradiction 或 Promotion Policy。

```powershell
.\scripts\gm.ps1 activation record <object-id> --kind used --project embodied-agent --reason "用于架构决策"
.\scripts\gm.ps1 activation show <object-id>
.\scripts\gm.ps1 activation top --project embodied-agent
.\scripts\gm.ps1 context "..." --record-use
```

Context 默认不写 Activation；只读 MCP 永远不写。M9.0 只收集并展示 Activation，不把它加入默认排序公式。
