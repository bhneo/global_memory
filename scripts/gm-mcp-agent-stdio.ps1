$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
$env:PYTHONPATH = Join-Path $repoRoot "src"
Set-Location -LiteralPath $repoRoot
& python -m global_memory mcp stdio --allow-capture
exit $LASTEXITCODE
