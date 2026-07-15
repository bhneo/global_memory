# ADR 0015：Derived Extraction Layer

- 状态：accepted
- 日期：2026-07-15

## 决策

Raw/source 与正文抽取严格分层。Extraction 位于 `data/derived/extractions/`，绑定 input SHA、extractor 和 version，可删除重建。HTML 使用本地确定性正文抽取；PDF 使用 optional pypdf 并保留页码注释；扫描 PDF 仅警告，不在 M5 引入 OCR。失败写 error extraction，不触碰 raw。

## 结果

Compiler 可以使用可定位正文而无需把 PDF/HTML 派生文本伪装成原始证据。Extractor 升级或输入变化不会静默复用旧结果。
