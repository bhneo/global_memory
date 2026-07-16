# Global Memory Index

## M6 navigation

- 正式 proposal：`vault/proposals/`；当前主要审阅单位是 source/source-collection bundle。
- Primary-source/recovery tasks：`vault/followups/`。
- 用户注意力补充：`vault/annotations/`，与 immutable source fact 分离。
- 可删除运行记录：`system/runs/`；不得保存唯一 candidate。
- 推荐顺序：`gm review queue` → `gm review bundle <id> --summary` → 指定 item 审批/修订/defer/source-only。
- Research/Exploration Context 若要看到待审图，必须显式 `--include-proposals`；输出中的 `truth_layer` 不得丢弃。

本页是人类与 Agent 的渐进式入口，不是全库内容清单。

## 先读

- 项目目标：[[docs/VISION]]
- 不可牺牲原则：[[docs/PRINCIPLES]]
- 系统边界与数据流：[[docs/ARCHITECTURE]]
- 对象与关系：[[docs/DATA_MODEL]]
- 文件 schema：[[SCHEMA]]
- 当前接管点：[[PROJECT_STATE]]
- 路线图：[[docs/ROADMAP]]

## 知识区域

- `vault/raw/`：只追加的 source capture；物理原文统一位于 `objects/sha256/` 全局内容对象库。
- `data/derived/extractions/`：可删除重建的 HTML/text/PDF 正文和页码视图，不是真相层。
- `vault/knowledge/works/`：经 proposal 审阅的 logical document/work identity。
- `vault/knowledge/`：人工确认的 entity、concept、claim、pattern、comparison、synthesis。
- `vault/frontier/`：intuition、question、tension、analogy、hypothesis、anomaly。
- `vault/action/`：project、decision、experiment、failure、opportunity。
- `vault/proposals/`：Agent/规则生成的待审修改和 candidate。
- `vault/archive/`：保留历史，不作为删除替代品。

## 检索协议

1. 先用本页和 `SCHEMA.md` 确认区域与字段。
2. 用 `gm search` 找少量候选，不默认扫描整个 vault。
3. 用 `gm show` 打开候选；用 `gm related` 沿 typed relations 扩展，或用有深度/节点上限的 `gm search --relation-depth`。
4. 重要结论回到 `source_ids` 指向的 source record，再核验 `raw_content_path`。
5. 面向任务使用 `gm context --profile execution|research|exploration`；proposal 默认不进入 Context Pack。
6. 新解释只创建 proposal，除非通过 provisional 门禁或用户明确批准 canonical 修改。
