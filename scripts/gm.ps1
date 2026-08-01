$ErrorActionPreference = "Stop"
Write-Warning "The 'gm' launcher is deprecated. Use '.\scripts\galois.ps1' or 'galois'."
& (Join-Path $PSScriptRoot "galois.ps1") @args
exit $LASTEXITCODE
