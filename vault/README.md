# Vault

`raw/` 保存来源与不可变内容；`knowledge/`、`frontier/`、`action/` 保存经批准 canonical 对象；`proposals/` 保存待审修改；`archive/` 保留退出活跃视图的历史。不要手工覆盖 raw，也不要绕过 proposal gate 修改 confirmed 对象。
