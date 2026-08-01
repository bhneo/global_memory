[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$ConfigPath,
    [string]$PythonPath
)

$ErrorActionPreference = "Stop"
Write-Warning "This installer name is deprecated. Use '.\scripts\install-galois-claude-desktop.ps1'."
$arguments = @{}
if ($ConfigPath) { $arguments.ConfigPath = $ConfigPath }
if ($PythonPath) { $arguments.PythonPath = $PythonPath }
if ($WhatIfPreference) { $arguments.WhatIf = $true }
& (Join-Path $PSScriptRoot "install-galois-claude-desktop.ps1") @arguments
exit $LASTEXITCODE
