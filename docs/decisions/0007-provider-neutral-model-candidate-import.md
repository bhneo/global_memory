# ADR 0007: Provider-neutral model candidate import

- Status: Accepted
- Date: 2026-07-14

## Context

Global Memory 需要能够利用模型提炼资料，但不应把任何特定 SDK、云服务或模型记忆变成真相层依赖。默认上传 raw 会违反本地优先和隐私边界；即使模型输出质量很高，也不能绕过人工审批。另一方面，只保存最终 candidate 会让未来无法判断它基于哪份输入、哪种模型和哪版 prompt 产生。

## Decision

1. 第一版模型边界不调用 provider。用户在自己选择的模型环境中生成 candidate Markdown，再用 `gm model-propose` 显式导入。
2. Candidate 必须使用既有 proposal schema，保留输入 `source_id`，并经过同一套不可变保存、diff、approve/reject/defer/revise、乐观并发和 recovery 流程。
3. 每个 `model_candidate` proposal 保存 provider、model、prompt version、可选 prompt SHA-256、输入 source ID/content SHA-256 与不确定性。
4. Prompt 本文和 raw 本文不复制进 proposal，也不由 CLI 向 provider 发送；外部发送行为属于用户选择的模型环境。
5. 未来实际 provider adapter 只能扩展该导入边界，必须默认显式授权并产出同一审计字段和 proposal schema。

## Consequences

模型可替换、输出可追溯且不会改变本地优先默认值。代价是当前没有“一键调用模型”体验，用户需要先生成 candidate；这能避免在授权、成本、网络和隐私策略尚未确定前把外部行为固化进核心仓库。

## Rejected alternatives

- 在 `gm` 中默认配置云 SDK：会把隐私、密钥、费用和供应商锁定引入真相层工作流。
- 直接把模型输出写入 canonical：违反 Agent 只能提议和人工审批原则。
- 只记录 provider/model 名称：不足以追溯输入证据、prompt 演化和不确定性。
- 将完整 prompt/raw 复制进 proposal：增加敏感材料重复和备份面，且不是可复现的充分条件。
