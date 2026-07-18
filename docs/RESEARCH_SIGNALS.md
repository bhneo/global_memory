# Research Signals

Research Annotation 是 append-only、用户拥有的科研注意力记录，位于 `vault/annotations/research/`。修正会创建新文件并使用 `supersedes_annotation_id`，不会覆盖旧记录。

支持三类：

- `capture_intent`：为什么保存、什么令人意外、可能连接、项目、领域和个人关注度。
- `connection_feedback`：对连接的 `obvious|forced|interesting|actionable` 评价。
- `research_note`：自由研究想法及其关联对象。

Annotation 的 `truth_layer` 是 `user_annotation`。用户原文与 `agent_interpretation` 分离；M9.0 不生成后者。Annotation 不改变目标对象、Receipt、Memory Tier、Epistemic Status、Trust Score 或 Canonical。

常用命令：

```powershell
.\scripts\gm.ps1 annotate <target-id> --why-saved "..." --surprised-by "..." --project embodied-agent --salience high
.\scripts\gm.ps1 research note --text "..." --target <object-id> --project scientific-memory
.\scripts\gm.ps1 feedback <object-id> --label interesting --note "..."
.\scripts\gm.ps1 annotations <target-id>
.\scripts\gm.ps1 annotations <target-id> --history
.\scripts\gm.ps1 feedback summary
.\scripts\gm.ps1 research signals
```

Feedback 描述研究价值，不描述命题真实性：`forced` 不删除对象，`actionable` 不晋升 Trusted，`interesting` 不自动生成 Hypothesis。
