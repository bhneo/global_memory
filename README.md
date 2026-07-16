# Global Memory

## M6：Knowledge Distillation and Graph Formation

当前真实语料已从 143 条逐条 model candidates 受控蒸馏为一个 62-item source-collection bundle：14 concepts、23 claims、6 questions、4 tensions、5 hypotheses、4 analogy proposals、2 syntheses，以及 4 个 action/project candidates。旧 proposals 保留为 superseded；新对象全部仍是 proposal，canonical 写入数为 0。

常用命令：

```text
gm quality <source-id>
gm source status <source-id>
gm review queue
gm review bundle <bundle-id> --summary
gm followups
gm followup normalize-locators             # 默认 dry-run
gm followup normalize-locators --apply     # 备份后迁移并保留 superseded 历史
gm runs list
gm migrate batch-artifacts --dry-run
gm distill corpus --dry-run
gm context Epiplexity --profile exploration --include-proposals
```

编译顺序为 quality gate → extraction/evidence → atomicity → existing-knowledge lookup → typed bundle → review。deleted/login/anti-bot/too-short 等 source 保留 provenance，但不生成知识 proposal。Context Pack 默认只读 canonical/source；显式包含 proposal 时逐项显示 truth layer、authority、verification 与选择理由。

Global Memory 是一个本地优先、用户拥有、模型无关的个人长期认知基础设施。Markdown 与不可变 raw source 是长期真相源；SQLite、全文索引、缓存和未来的向量索引都只是可删除、可重建的派生层。

当前版本完成第一阶段最小纵向闭环：

```text
URL / 文本 / 本地文件
→ 不可变 raw content + source record
→ URL 与内容去重
→ SQLite FTS5 检索
→ 确定性规则 compile proposal + 内容级 diff
→ 人工 approve / reject
→ canonical knowledge
→ 来源回溯与索引重建
```

## 快速开始

要求 Python 3.11+。运行时只使用 Python 标准库；测试使用 pytest。

```powershell
cd C:\Users\bhneo\Desktop\project\超级大脑\global_memory
python -m pip install -e .
gm init
gm capture-text --text "人的原始文字会原样保留" --comment "验证最小闭环"
gm capture https://example.com/article --refresh --comment "显式检查网页是否更新"
gm inbox
gm compile <source-id> # deterministic fallback，生成 Compile Bundle Proposal
gm compile <source-id> --bundle-file cursor-output.json --provider-name cursor-json-v1
gm proposal diff <bundle-proposal-id>
gm proposal approve <bundle-proposal-id> --items claim-1,concept-2
gm proposal reject <bundle-proposal-id> --items question-3 --reason "暂不保留"
gm proposal revise <bundle-proposal-id> --item claim-1 --from-file revised.md --reason "人工修订"
gm proposal split-item <bundle-proposal-id> --item claim-1 --from-files child-1.md,child-2.md --reason "拆成可独立核验的断言"
gm proposal verify-item-quote <bundle-proposal-id> --item claim-1 --source <primary-source-id> --extraction <id> --span-start -1 --quote "原文" --section "p.5" --reason "原始论文核验"
gm proposal mark-compound <bundle-proposal-id> --item claim-1 --reason "原文复核发现两个可独立检验的断言"
gm search "query" --types claim,concept --statuses confirmed,provisional --relation-depth 1
gm context --profile execution,research --project project_id --question "当前问题" --token-budget 20000
gm model-propose <source-id> --candidate model-candidate.md --provider local --model my-model --prompt-version v1 --prompt-file prompt.md --uncertainty "待人工核验" --reason "导入模型结果"
gm proposal show <proposal-id>
gm proposal approve <proposal-id>
gm proposal publish <proposal-id>
gm promote <canonical-id> --reason "已核对原文"
gm raw verify
gm migrate raw-store --dry-run
gm migrate raw-store
gm migrate raw-store --verify
gm extract <source-id>
gm extract <source-id> --rebuild
gm work propose <source-id>... --arxiv-id 2607.11119v1
gm proposal defer <proposal-id> --reason "等待补充证据"
gm proposal revise <proposal-id> --from-file revised-candidate.md --reason "人工修订候选主张"
gm recover
gm propose-update <canonical-id> --from-file candidate.md --reason "新证据改变了适用范围"
gm search "原始文字"
gm context "为下一个 Agent 准备哪些长期记忆" --token-budget 1200
gm lint
gm audit contradictions
gm synthesize <claim-id-1> <claim-id-2>
gm discover <claim-id>
gm backup manifest
gm backup create D:\GlobalMemoryRawBackup
gm backup verify D:\GlobalMemoryRawBackup
gm backup restore D:\GlobalMemoryRawBackup
gm backup restore D:\GlobalMemoryRawBackup --apply
gm doctor
```

不安装 editable package 时，可以在 PowerShell 中使用：

```powershell
.\scripts\gm.ps1 status
```

所有命令都接受全局参数 `--root <仓库目录>`，也可以设置 `GM_ROOT`。

## CLI

- `gm init`：创建必要目录并建立空索引。
- `gm capture <url-or-path> --comment "..."`：捕获 URL 或本地文件。
- `gm capture <url> --refresh`：显式重新抓取；内容变化时追加 source version 和 review proposal。
- `gm capture-text [--text "..."]`：捕获文本；未提供 `--text` 时读取 stdin。
- `gm inbox`：列出尚未 compile 的 source。
- `gm compile <source-id>`：生成低置信度 proposal，不修改 canonical knowledge。
- `gm model-propose <source-id> --candidate <Markdown> ...`：导入用户明确提供的外部模型 candidate；记录 provider/model/prompt version/输入哈希与不确定性，但命令自身不调用 provider。
- `gm proposals [--status pending]`：列出 proposal。
- `gm followups`：列出活动 primary-source/recovery 任务；`gm followup normalize-locators [--apply]` 规范化 locator、合并重复任务并重写 proposal 引用，默认只输出迁移计划。
- `gm proposal show|approve|defer|reject <proposal-id>`：查看 diff、明确审批或暂缓处理。
- `gm proposal revise <id> --from-file <candidate.md> --reason "..."`：用新的不可变 candidate 替代待审 proposal。
- `gm proposal split-item <id> --item <item-id> --from-files <a.md,b.md> --reason "..."`：将 pending compound claim 替换为至少两个 atomic child；原 item 保留为 superseded，子项仍独立等待审阅。
- `gm proposal verify-item-quote <id> ...`：把逐字匹配 primary extraction 的 quote 写成新的不可变 item revision；`--span-start -1` 仅在 quote 唯一出现时自动定位。核验不会自动 approve。
- `gm proposal mark-compound <id> --item <item-id> --reason "..."`：原文复核发现漏检复合主张时，创建不可变 atomicity correction revision 并重新阻止发布；旧 candidate 不覆盖。
- `gm propose-update <id> --from-file <candidate.md> --reason "..."`：创建受并发保护的 canonical update proposal。
- `gm search "<query>"`：搜索 source 与 canonical knowledge，结果携带 `source_ids`。
- `gm show <id>` / `gm related <id>`：读取对象与 typed relations。
- `gm rebuild-index`：从文件重建 SQLite FTS5。
- `gm lint`：只读检查 wikilink/relation、claim 来源、raw 哈希、proposal/candidate/base 完整性；孤立 canonical 页面以 warning 报告。
- `gm audit contradictions`：只读报告同一 claim 内正反 evidence 并存，以及 claim 之间显式 `contradicts` relation；不自动裁决或修改状态。
- `gm synthesize <claim-id> ...`：从至少两个 canonical claim 生成可审阅 synthesis proposal；审批前重验所有输入 claim 哈希。
- `gm discover <claim-id>`：依据共享来源、标签、关系目标和确定性关键词生成可解释的关联候选 proposal；不会自动添加 relation。
- `gm context "<query>" [--token-budget 1200]`：从检索结果中确定性挑选少量 source、claim 与 synthesis，输出临时 Context Pack；每项带路径、文档 hash、来源链、入选理由和保守 token 估算。对直接入选的 source，默认只取每个 family 的最新版本；已归档 canonical 及仅被归档对象引用的 source 默认排除；历史材料仍可通过 `search`/`show` 回溯。命令只读，不写入 Markdown、索引或日志，也不把命中升级为事实。
- `gm backup manifest [--output <path>]`：生成整个 `vault/raw/` 的 SHA-256 manifest；默认写入本地 `data/backups/`。
- `gm backup create <外部目录>`：增量复制 raw source record 与 content/blob；已存在同 hash 文件跳过，不覆盖冲突文件。
- `gm backup verify <外部目录>`：校验备份 manifest、文件大小和 SHA-256。
- `gm backup restore <外部目录> [--apply]`：默认只显示恢复计划；`--apply` 只写入本地缺失文件，冲突时不写入任何文件并重建索引。
- `gm status` / `gm doctor`：查看状态与一致性检查。
- `gm recover`：幂等续做中断的 canonical approval；遇到第三方修改时报告 blocked。

## 安全边界

- raw content 与 source record 通过独占创建写入，普通流程不能覆盖。
- 已明确归档并需要清理活动目录的 canonical 可移入 `vault/archive/`，以最小墓碑保留 ID、来源和审计理由；归档目录不进入活动索引。
- compile 只写 `vault/proposals/`；只有明确 approve 才写 canonical knowledge。
- candidate 有 SHA-256 校验，审批前被改动会被拒绝。
- SQLite 位于 `data/indexes/`，不进入 Git，可随时重建。
- 二进制 raw payload 默认不进 Git；必须通过独立备份策略保护。
- URL 捕获当前限制 20 MB，不执行 JavaScript，也不绕过登录或付费墙。

## URL refresh 语义

普通 `gm capture URL` 不会重新访问已经存在的 canonical URL。只有显式 `--refresh` 才发起新请求：内容哈希未变时不创建新版本；内容变化时追加新的 source Markdown 和 raw content，并生成 `source_refresh` proposal，展示旧/新原文 diff。批准 refresh proposal 只确认新来源版本可进入后续知识处理，不会直接修改 canonical knowledge。随后可对新 `source_id` 单独执行 `gm compile`。

## Canonical update 语义

Candidate 必须是 UTF-8 Markdown，保持 target 的 `id`、`type`、`created_at`，使用 `status: proposal`；可用 `proposed_status` 建议 `provisional`、`confirmed`、`contested`、`superseded` 或 `archived`。Claim 必须保留至少一个 `source_id`。

批量导入时，结构化 claim 可通过 `proposal publish` 进入 `provisional`：它会立即进入全文检索和 Context Pack，但明确标注为“已通过自动门禁、尚未人工确认”。缺少来源、证据、适用范围或不确定性，包含反证，属于医疗、法律、金融等高风险领域，或不是 claim 的 proposal，都必须保留在待审区并使用人工 `proposal approve`。用户核对后用 `promote` 将其晋升为 `confirmed`。

所有新 capture 的 bytes 进入与入口无关的 `vault/raw/objects/sha256/`。URL、本地文件和粘贴文本只要 bytes 相同就共享一个物理对象，同时保留各自 source record。`gm raw verify` 校验引用与磁盘哈希；旧布局先运行 migration dry-run，再正式迁移。迁移会自动备份 source record并保留旧 payload，不执行清理。

`gm extract` 从 raw 创建可重建正文：文本/Markdown 保留内容，HTML 去除明显模板噪声，PDF 保留逐页边界。PDF 支持是 optional dependency：`pip install -e .[pdf]`。`gm work propose` 把多个 capture 作为同一现实作品的候选聚合，只有 approve 后才写 logical work，且从不改写 source capture。

`gm compile` 现在先读取 extraction 并检索已有 canonical，再生成 Compile Bundle。Deterministic fallback 只识别显式 `Concept:/Claim:/Question:/Hypothesis:/Tension:/Analogy:` 标记；没有标记时只保留第一段逐字材料，不为了填满 schema 强制生成对象。Bundle 支持整体或按 item approve/reject/revise；一组批准通过多目标 recovery journal 原子续做。

Context Pack 支持 `execution`、`research`、`exploration` profile 及组合，可按 project/domain/type/status/time/source kind 过滤，并沿 typed relations 做深度与节点数受限的扩展。Proposal 默认不进入；只有显式 `--include-proposals` 才返回，并保留 pending/proposal 状态。搜索对 title、aliases、tags、domains 和 body 分字段加权。

外部模型不需要绑定 SDK：让 Cursor 或其他 provider 输出 `{"items": [...]}` JSON，再用 `--bundle-file` 导入。模型输出仍必须通过本地 schema validation，只能形成 proposal，不能直接写或批准 canonical。

工程验收可运行 `python scripts/m5_acceptance_demo.py`。该脚本在忽略的 `data/derived/` 测试 Vault 中演示完整 M5 流程，不读取私人目录，也不修改真实 canonical。

`propose-update` 会不可变保存当时的 base snapshot 和 candidate，并记录两者 SHA-256。审批时 target 必须仍与 base 完全相同；如期间发生人工编辑，审批会失败且不写文件。再次运行 `proposal show` 可看到 Base→Candidate 和 Base→Current，随后应基于当前 canonical 重新创建 proposal。系统当前不自动合并冲突。

## Approval recovery

Canonical approve 在写入任何 target 前，会原子创建 `system/recovery/approve-<proposal-id>.json`。Journal 包含预期 target/proposal 完整文本、前后哈希和 audit operation ID。正常完成后 journal 自动删除；中断后 `gm doctor` 会报告，`gm recover` 按 target → proposal → audit → index 顺序幂等续做。

`defer` 不会修改 candidate 或 canonical，且 deferred proposal 以后仍可 approve、reject 或 revise。`revise` 不覆盖旧 candidate：它创建新的 candidate/proposal，把旧 proposal 标记为 `superseded`，并通过 `revision_of`、`superseded_by` 和 typed `supersedes` relation 保留完整审阅链。Update revision 总是以执行修订时的 current canonical 为新 base。

## Lint

`gm lint` 不写入文件、不重建索引。它把会破坏审阅或来源链的情况列为 `errors`，例如失效 relation/wikilink、无效 `source_id`、无来源 claim、raw 内容哈希不匹配，以及 proposal 的 candidate/base/target/hash 不一致；命令在存在 errors 时以非零状态退出。没有来源或关系的 canonical 页面、未被 proposal 引用的 candidate/base snapshot 则列为 `warnings`，方便人工判断是否确为孤立材料。

## Raw backup 与恢复

`vault/raw/` 同时包含不可变 raw payload 和 source Markdown；两者必须一起备份才能保留来源版本链。`gm backup create` 只接受仓库外、由用户明确指定的本地目录，备份内会写 `global-memory-raw-manifest.json`。增量运行会跳过已验证的相同文件；若目标目录出现同路径不同 hash，命令报告 conflict，且不会覆盖文件或更新 manifest。

恢复默认 dry-run。执行 `--apply` 前会先校验备份 manifest 与所有备份文件；只恢复本地缺失文件。若任一目标同路径但 hash 不同，恢复整体停止，不覆盖本地内容。恢复成功后自动重建 SQLite 索引。此机制不替代 Git：canonical Markdown、proposal 和文档仍应由 Git 或独立仓库备份保护。

## Provider-neutral model proposal

模型处理器的第一版是“外部 candidate 导入器”，而不是 SDK 或云端调用器。请在你选择的模型环境中生成 UTF-8 candidate Markdown，再通过 `gm model-propose` 显式导入。Candidate 必须使用 `status: proposal`，并在 `source_ids` 中保留输入 source；系统将不可变保存 candidate、生成 diff，并记录 `provider`、`model`、`prompt_version`、可选 `prompt_sha256`、输入 source/content hash 与不确定性。导入后可按 ADR 0013 选择门禁发布为 provisional 或人工批准为 confirmed。

若 candidate 类型为 `claim`，还必须填写 `evidence[]`、`applicability[]` 与 `uncertainty`。每条 evidence 需要来源、位置、摘录、`supports` / `contradicts` / `context` 方向和理由；详见 [SCHEMA.md](SCHEMA.md)。

这条命令默认不会发送 raw、prompt 或任何文件到 provider；它也不会自动批准模型结论。模型输出仍要经过 `show → approve/reject/defer/revise`，并适用现有并发保护和 approval recovery。

## Contradiction audit

`gm audit contradictions` 只扫描 canonical claim。输出保留产生冲突的 evidence（来源、位置、摘录、理由）和显式 relation 的双方路径及理由。正反 evidence 并存是需要审阅的认知信号，不是 schema 错误；audit 始终不写入 Markdown、不改变 confidence/status，也不选择任何一方为真。

## Synthesis proposal

`gm synthesize` 接受至少两个 canonical claim，生成 `synthesis` candidate 与 content diff。候选只汇总已显式记录的来源、evidence、适用条件、不确定性和 `contradicts` relation，并列出待人工判断的问题；它不产生新的事实结论或自动解决冲突。

Proposal 记录每个输入 claim 的路径、状态和 SHA-256。审批前若任一输入发生变化，批准会拒绝并要求重新执行 synthesize；成功批准后 synthesis 仍带 `source_ids` 和与输入 claim 的 `related_to` relation。当前由用户显式运行，不包含自动/夜间调度。

## Explainable relation discovery

`gm discover` 从一个 canonical claim 出发，比较其他 canonical claim 的共享 `source_ids`、tags、已有 relation target 和确定性关键词。每个候选显示触发信号和可解释分数；共享 source 与关系目标权重高于 tags 与关键词。没有任何可解释重叠时不会创建 proposal。

该 proposal 只记录候选及其输入 hash。批准表示已审阅候选，**不会**修改任何 claim 的 relation；若希望采纳某条关联，请通过 `gm propose-update` 创建带 diff 的 canonical 更新。审批前 seed 或任一候选 claim 改变时，发现 proposal 会被拒绝，需重新生成。

恢复采用 roll forward：当前文件必须仍是 journal 记录的写前或写后状态。若用户在中断后又修改了 target/proposal，恢复会返回 blocked 并保留 journal，不会覆盖第三种状态。Recovery journal 含可能敏感的候选正文，仅保存在本地并由 `.gitignore` 排除。

## 进一步阅读

从 [INDEX.md](INDEX.md) 开始。数据格式见 [SCHEMA.md](SCHEMA.md)，系统边界见 [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)，当前接管点见 [PROJECT_STATE.md](PROJECT_STATE.md)。
