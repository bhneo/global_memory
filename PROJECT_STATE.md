# Current State

## Current milestone

M4：渐进式检索的第一版 Context Pack 已完成。

## What is working

- Python 标准库 CLI 与本地仓库初始化。
- 文本、本地文件和 HTTP(S) URL capture。
- 不可变 raw content、结构化 source Markdown、SHA-256 与 capture audit event。
- canonical URL 规范化、同来源去重、跨来源内容去重且不丢 source record。
- SQLite FTS5 + 中文子串 fallback；结果包含来源 ID。
- 确定性规则 compile proposal、candidate 哈希、内容级 unified diff。
- approve/reject gate；未批准 proposal 不触碰 canonical knowledge。
- typed relation 校验、show、related、status、doctor、索引全量重建。
- Windows 路径、中文文件名和索引文件原子替换测试。
- 显式 `gm capture <url> --refresh`；未变化时去重，变化时追加版本。
- Source family、连续 version、previous-version 链与内容回退历史。
- `source_refresh` proposal、原文 diff 和不触碰 canonical 的独立审批。
- `doctor` 对 source version chain 的一致性检查。
- 显式 `gm propose-update`、不可变 base/candidate snapshot 与内容 diff。
- Approval 前重验 base/candidate/current hash，阻止覆盖并发人工修改。
- 冲突时动态显示 Base→Candidate 和 Base→Current，并支持重新提案。
- Update candidate 的稳定 ID、类型、created_at、状态和 claim provenance 校验。
- Canonical approval 在 target 写入前创建 recovery journal，并阶段化完成 target/proposal/audit/index。
- `gm recover` 可幂等续做 create/update approval；audit operation ID 去重。
- `doctor`/`status` 暴露 pending journal；第三状态和 payload 篡改保持 blocked。
- `proposal defer` 暂缓审阅但保持后续 approve/reject/revise 能力。
- `proposal revise` 创建新 candidate/proposal，旧 proposal 标记 superseded，并保留双向 lineage 与 typed relation。
- Update revision 以 current canonical 重新建立 base，避免继承过期并发令牌。
- `gm lint` 检查 metadata、失效 relation/wikilink、claim provenance、raw hash、proposal candidate/base/target/hash 和 revision lineage。
- Lint 将损坏或失效引用报为 error；孤立 canonical 页面与未引用审阅快照报为 warning，且不修改仓库。
- `gm backup manifest/create/verify/restore` 覆盖整个 `vault/raw/`，使用 SHA-256 manifest、外部增量目录与默认 dry-run 的恢复流程。
- Backup/restore 从不覆盖同路径不同 hash 文件；实际恢复只补齐缺失 raw 文件，完成后重建索引。
- `gm model-propose` 只导入用户明确提供的 candidate，不在仓库内调用 provider；proposal 记录 provider/model/prompt version/hash、输入 source hash 与不确定性。
- Model candidate 与规则 compile 共用不可变 candidate、diff、approval、并发和 recovery gate；lint 校验其 model_run 审计字段。
- Claim 支持结构化 `evidence[]`（来源、位置、摘录、supports/contradicts/context、理由）、`applicability[]`、`confidence` 与 `uncertainty`。
- 规则 compile 只生成 context evidence；model claim 必须提供完整 evidence/applicability/uncertainty，旧 Markdown 仍保持兼容读取。
- `gm audit contradictions` 报告 canonical claim 内部正反 evidence 并存，以及跨 claim 的显式 `contradicts` relation；审计不裁决、不写入。
- `gm synthesize` 从至少两个 canonical claim 生成仅汇总显式材料的 synthesis candidate，保留输入来源和 relation。
- Synthesis approval 前重验所有输入 claim hash；输入变化时拒绝批准，不生成自动/夜间任务。
- `gm discover` 以共享 source、tags、relation target 和关键词生成关联候选，保留可解释信号与输入 hash。
- Relation discovery approve 只记录已审阅，绝不自动修改 canonical relation；采纳关系仍须独立 update proposal。
- `gm context <query> --token-budget <n>` 只读生成临时 Context Pack：确定性选择少量 source/claim/synthesis，逐项保留文档 hash、来源链和选择理由；不写入 Markdown、索引或日志，也不提升事实状态。
- 第一条真实论文材料 VIA（arXiv:2607.11119v1）已完成官方 URL raw capture、带页码证据与反外推边界的 proposal 审阅，并经用户明确批准写入 canonical claim。
- VIA 验收确认 canonical claim 可被 `VIA`、`waypoint` 等内容查询召回，Context Pack 在 600/1200 token budget 下保留 claim、source_ids、文档 hash 与 raw source hash；原始 PDF 正文仍未进入派生全文索引。

## What is being implemented

- 无进行中的功能；仓库处于可接管状态。

## Known defects

- URL 抓取只处理静态响应，不执行 JavaScript；网页正文仍可能包含 HTML 噪声。
- 第一版 compile 是确定性开头摘录，只验证治理闭环，不等同于高质量知识抽取。
- 二进制内容只保存和哈希，尚未提取 PDF、Office 或图片正文。
- `search` 目前会同时返回同一 family 的多个版本；Context Pack 已默认过滤直接入选 source 的旧版本，但尚无通用 latest/accepted 搜索视图。
- Blocked recovery journal 尚无自动解决命令，必须人工核验第三状态后决定重新提案或受控清理。

## Unresolved architectural questions

- 大型 raw payload 的加密策略与 Git/LFS 边界。
- 实际模型适配器的授权、费用、网络隔离与 provider-specific 错误策略。
- 中文全文检索长期采用 tokenizer、n-gram 派生索引还是混合策略。

## Recent decisions

- Markdown/raw source 为真相源；SQLite 仅为可重建派生层。
- 第一版零运行时第三方依赖，使用 argparse、urllib 与 SQLite FTS5。
- 相同内容不同来源共享 content object，但保留独立 source record。
- compile 默认只生成低置信度 proposal；canonical 写入必须明确 approve。
- 真实示例已完成 capture → compile → diff → approve → search；`gm doctor` 返回 `ok: true`。
- ADR 0002 确定显式 refresh、append-only source version 和独立 refresh proposal。
- ADR 0003 确定 canonical update 使用乐观并发；冲突拒绝覆盖且不自动合并。
- ADR 0004 确定 canonical approval 使用本地 journal 和幂等 roll-forward。
- Candidate revision 不覆盖旧文件，通过新 proposal 和 supersedes lineage 表达人工修订。
- ADR 0005 确定 deferred 可继续审阅，revision 使用不可变新文件，并对 update 重新建立 current base。
- ADR 0006 确定 raw backup 覆盖 source record 与 payload，增量复制不覆盖冲突，恢复默认 dry-run。
- ADR 0007 确定模型输出通过外部 candidate 导入，不由仓库默认调用 provider，并保留最小可复现审计字段。
- ADR 0008 确定 claim 的证据方向、适用范围、置信度与不确定性分别表达，不以单一状态抹平冲突。
- ADR 0009 确定 contradiction audit 只呈现显式冲突，保持人工决定和 proposal gate。
- ADR 0010 确定 synthesis 只整理显式材料并锁定输入 hash，仍由人工批准。
- ADR 0011 确定 serendipity discovery 必须可解释、输入 hash 锁定，并与 canonical relation 写入分离。

## Next concrete task

设计 PDF 正文的可重建派生提取层：原始 PDF 与 source record 继续作为不可变真相源，提取文本必须带 extractor/version/input hash/page provenance，并可删除重建；随后用 VIA 验证中文短语、source version 与 token budget 下的召回质量。

## Do not do yet

- 不引入 embedding、向量数据库、图数据库、复杂前端或 Obsidian 插件。
- 不导入全部浏览器、微信或历史聊天。
- 不启动多 Agent 调度、夜间任务、全库自动重写或复杂本体工程。
