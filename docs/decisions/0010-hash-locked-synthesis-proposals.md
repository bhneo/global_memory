# ADR 0010: Hash-locked synthesis proposals

- Status: Accepted
- Date: 2026-07-14

## Context

当多个 claim 已具备结构化 evidence 和 contradiction audit 后，用户需要看到可审阅的材料综合。若综合器自动解释、裁决或写入 canonical，会把整理与知识判断混在一起；若 proposal 不记录输入版本，则输入 claim 在审阅期间变化后仍可能批准过期综合。

## Decision

1. `gm synthesize` 至少接受两个 canonical claim，只整理其显式来源、evidence、适用条件、不确定性和 `contradicts` relation。
2. 输出是 `synthesis` candidate/proposal，不是自动写入；它不产生新的事实结论、不选择冲突赢家。
3. Proposal 记录每个输入 claim 的 ID、路径、状态和完整 Markdown SHA-256；candidate 继承去重后的 source IDs，并用 `related_to` relation 连接输入 claim。
4. Approval 前重新校验所有输入路径、ID、类型和 hash。任何变化都会阻止批准，用户必须重新生成综合。
5. Synthesis 继续使用普通 candidate hash、content diff、人工 approve/reject/defer/revise 和 recovery journal。
6. 当前只支持用户显式运行；不引入周期、夜间或自动调度。

## Consequences

系统可以把分散且冲突的材料变成透明的审阅对象，同时保持来源链和并发安全。代价是综合不会替人给出最终结论，且输入变化会增加重新生成的工作；这是为了避免认知演化被静默合并。

## Rejected alternatives

- 直接生成并写入 synthesis：绕过人工审批，且无法审阅 diff。
- 只保存输入 ID：无法发现同一 ID 内容已被更新。
- 自动按 evidence 数量或 confidence 解决矛盾：不具备可靠的语义或适用范围判断。
- 自动定时运行：在资料量、成本和用户关注问题尚未明确时会制造噪声与不可解释的变更。
