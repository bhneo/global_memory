$ErrorActionPreference = "Stop"
# Silent compatibility wrapper: stdout is reserved for JSON-RPC.
& (Join-Path $PSScriptRoot "galois-mcp-stdio.ps1") @args
exit $LASTEXITCODE
