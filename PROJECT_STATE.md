# Current State

## M6 current milestone — completed 2026-07-16

M6 Knowledge Distillation and Graph Formation 已完成工程实现与 33-source 受控重编译。临时 batch 双重真相源已迁移并清理；source lifecycle、quality gate、atomic claim gate、knowledge classification、bundle review、authority/follow-up、epistemic dimensions、typed relations 与 proposal-aware Context Pack 已落地。

真实语料结果：143 个 input model proposals（其中 134 个待审）被保留并 supersede 到唯一 pending corpus bundle；当前活动 bundle 含 66 items：14 concept、27 atomic claim（4 full、23 partial）、6 question、4 tension、5 hypotheses、4 analogies、2 syntheses、2 experiments、1 project、1 opportunity。另保留 4 个已拆分 compound item 为 superseded 历史。11 个 source-only、1 个 invalid source、6 个 open primary-source follow-up；canonical writes = 0。

当前 source processing state：22 awaiting_review、10 completed、1 failed、7 个新 primary captures 处于 inbox/extracted（作为核验材料，不自动编译知识）。未完成边界：66 个活动 items 仍需人工 bundle review；SkillEvolver 与 PhySO 共 4 个 atomic claims 已由 primary PDF 逐字回验为 full evidence，其余 23 个 claims 仍需核验；6 个 follow-up 尚未关闭。PhySO 原 compound 已拆成 RNN/RL 方法和单位约束两个 children，旧 item 保留为 superseded；未改 canonical。

## Current milestone

M5：Real Knowledge Compilation 核心实现完成；工程验收通过，真实跨领域 20–30 份资料验证因当前样本不足而保持未完成。

## What is working

- Python 标准库 CLI 与本地仓库初始化。
- 文本、本地文件和 HTTP(S) URL capture。
- 单篇微信公众号文章 capture：`gm capture-wechat` 或 `gm capture <mp.weixin.qq.com/s/...>`；使用移动端 UA 抓取 HTML，解析标题/作者/公众号/发布时间，并以 `source_kind: wechat` 入库。
- 不可变 raw content、结构化 source Markdown、SHA-256 与 capture audit event。
- 全局 content-addressed raw store：不同 capture kind 的相同 bytes 共用 `objects/sha256/` 物理对象；source provenance 保持独立。
- `gm migrate raw-store` 支持 dry-run、自动 source 备份、journal 续做、幂等重跑与迁移后验证；当前 6 个 source 已合并为 5 个唯一对象，旧路径未删除。
- `gm raw verify` 校验 content_id、对象路径与磁盘 SHA-256。
- `gm extract` 生成绑定 input hash/extractor version 的 derived extraction；支持文本、Markdown、HTML、PDF 页码、中文编码降级、warning/error/stale/rebuild。
- `gm work propose` 以审计 proposal 聚合 logical work；已测试同一 arXiv 的 PDF URL、本地 PDF 和 abstract capture 只形成一个 work，source record 不变。
- Evidence taxonomy 支持 quote、paraphrase、translation、table_value、figure、calculation；quote 必须逐字回验 extraction span。
- CLI `gm compile` 已升级为检索优先 Compile Bundle；deterministic fallback 只生成有显式材料的类型，不强制填充 schema。
- Bundle review 支持完整 diff、source/evidence、潜在冲突、approve all、按 item approve/reject/revise；多目标批准由 bundle recovery journal 幂等续做。
- Context Pack 支持 execution/research/exploration profile、组合、project/domain/type/status/time/source-kind 过滤、有界 relation traversal、evidence 与 truncation report。
- SQLite/FTS 对 title、aliases、tags、domains、body 分字段检索；结果解释 metadata/body/关系命中，proposal 仅在显式请求时出现。
- 旧 `discover` 保留兼容别名，用户界面准确称为 `related-content`，不再把词汇重合描述为真正 serendipity。
- GitHub Actions 配置覆盖 Ubuntu/Windows 与 Python 3.11/3.12/3.13，并执行 pytest、doctor、lint、raw integrity、migration dry-run 和 M5 acceptance smoke。
- `scripts/m5_acceptance_demo.py` 演示跨入口 PDF 去重、两页 extraction、7-item bundle、三 profile Context Pack 与 index/extraction 重建。
- 当前 6 个真实 capture 已全部生成本地 extraction：4 PDF、1 HTML、1 Markdown，均 ready 且无 warning；VIA 和 Play2Perfect 各有一个 pending work enrichment proposal。
- canonical URL 规范化、同来源去重、跨来源内容去重且不丢 source record。
- SQLite FTS5 + 中文子串 fallback；结果包含来源 ID。
- 确定性规则 compile proposal、candidate 哈希、内容级 unified diff。
- 分级发布 gate：合格的结构化 claim 可先进入 `provisional` canonical；`approved`/`confirmed` 仍要求用户显式确认。
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
- `gm related-content`（旧 `discover` 兼容别名）以共享 source、tags、relation target 和关键词生成关联候选，保留可解释信号与输入 hash。
- Relation discovery approve 只记录已审阅，绝不自动修改 canonical relation；采纳关系仍须独立 update proposal。
- `gm context` 按 profile/filter/token budget 只读生成临时 Context Pack，保留文档 hash、来源链、evidence、状态、命中/选择理由与截断报告。
- 第一条真实论文材料 VIA（arXiv:2607.11119v1）已完成官方 URL raw capture、带页码证据与反外推边界的 proposal 审阅，并经用户明确批准写入 canonical claim。
- VIA 验收确认 canonical claim 可被 `VIA`、`waypoint` 等内容查询召回；其 20 页 PDF 已生成带页码边界的本地 extraction。
- VIA 首次导入暴露了范围治理问题：材料入库是为了积累跨领域知识并验证 Global Memory，不要求每条来源都映射为系统自身的设计启发；范围纠正 proposal 已经用户明确批准，canonical 正文现只保留机器人论文知识、实验结果与适用边界，纠偏原因保留在审计 metadata 中。
- 首轮 quickstart 端到端测试 fixture 已按用户要求完整清理：source 移入 `vault/archive/` 并移出活动索引，claim 墓碑与 `examples/quickstart-note.md` 已删除；不可变 raw object 与 compile/approve proposal 历史保留供审计；`find_document` 与 `gm lint` 可解析归档 source。
- Cursor 首批真实材料导入完成两篇论文、八条 model proposal；人工 PDF 复核后已通过 revision 补全自包含正文、收紧 33×/2.4× 结论范围，并为 Play2Perfect 增加官方 arXiv 页面来源。原八条 proposal 保留为 superseded，新八条仍为 pending，尚未写入 canonical；可在新门禁下逐条发布为 provisional。

## What is being implemented

- 无进行中的核心代码；等待通过正常资料导入完成 20–30 份真实跨领域验证。

## Known defects

- URL 抓取只处理静态响应，不执行 JavaScript；网页正文仍可能包含 HTML 噪声。
- Deterministic bundle fallback 只识别显式类型标记或保留第一段逐字材料，不等同于高质量模型语义编译。
- PDF 已支持文本提取但不做 OCR；Office、图片和扫描 PDF 正文仍未提取。
- `search` 目前会同时返回同一 family 的多个版本；Context Pack 已默认过滤直接入选 source 的旧版本，但尚无通用 latest/accepted 搜索视图。
- Blocked recovery journal 尚无自动解决命令，必须人工核验第三状态后决定重新提案或受控清理。
- 当前真实资料集中在具身智能领域且只有约 3 个 work，尚不足以验证跨领域知识复利和三条人工认可的远距离连接。

## Unresolved architectural questions

- 大型 raw payload 的加密策略与 Git/LFS 边界。
- 实际模型适配器的授权、费用、网络隔离与 provider-specific 错误策略。
- 中文全文检索长期采用 tokenizer、n-gram 派生索引还是混合策略。

## Recent decisions

- Markdown/raw source 为真相源；SQLite 仅为可重建派生层。
- 第一版零运行时第三方依赖，使用 argparse、urllib 与 SQLite FTS5。
- 相同内容不同来源共享 content object，但保留独立 source record。
- compile 默认只生成低置信度 proposal；自动发布仅限证据结构完整、无反证、非高风险领域的 claim，并固定写为 provisional；confirmed 必须显式 approve 或 promote。
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

审阅并决定两个 work enrichment proposal；随后随用户正常导入真实资料完成 20–30 份跨领域验证。Cursor 首批八条修订 claim 可按新 extraction/evidence 回溯后发布为 provisional，不应批量自动确认。

## Do not do yet

- 不引入 embedding、向量数据库、图数据库、复杂前端或 Obsidian 插件。
- 不导入全部浏览器、微信或历史聊天。
- 不启动多 Agent 调度、夜间任务、全库自动重写或复杂本体工程。
