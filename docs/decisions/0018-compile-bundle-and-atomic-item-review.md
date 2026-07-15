# ADR 0018：Compile Bundle 与原子 Item Review

- 状态：accepted
- 日期：2026-07-15

## 决策

`gm compile` 以一个包含多个独立 item 的 bundle proposal 为输出。编译前先检索已有 knowledge；每项明确 create/update、target、base、candidate、hash、潜在冲突和 decision。Provider 只返回结构，不写文件或批准。默认 fallback 只识别显式类型标记或保留一段逐字材料。

Review 支持全部或选择 item 批准、拒绝与不可变 revision。一次批准选择的所有目标在写入前全部校验，并由多目标 recovery journal roll-forward 完成 target、proposal、audit 和 index；中断不回滚用户后续工作，第三状态 blocked。

## 结果

一篇资料可以提出多个彼此独立但共同审阅的知识变化，也能更新已有 concept，而不是永远创建孤立摘要。文件系统无法提供真正多文件 ACID，因此原子语义定义为“全部预检 + journal 化确定性续做”。
