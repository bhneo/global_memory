[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$ConfigPath,
    [string]$PythonPath
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$sourceRoot = Join-Path $root "src"
. (Join-Path $PSScriptRoot "resolve-galois-python.ps1")

if (-not $PythonPath) {
    $PythonPath = Resolve-GaloisPython
}
if (-not (Test-Path -LiteralPath $PythonPath -PathType Leaf)) {
    throw "Galois Python runtime not found: $PythonPath"
}
if (-not (Test-Path -LiteralPath $sourceRoot -PathType Container)) {
    throw "Galois source root not found: $sourceRoot"
}

if (-not $ConfigPath) {
    $candidates = @(
        (Join-Path $env:APPDATA "Claude\claude_desktop_config.json"),
        (Join-Path $env:LOCALAPPDATA "Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude_desktop_config.json")
    )
    $ConfigPath = $candidates | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1
    if (-not $ConfigPath) {
        $ConfigPath = $candidates[0]
    }
}

$configFile = [System.IO.Path]::GetFullPath($ConfigPath)
$configDirectory = Split-Path -Parent $configFile

if (Test-Path -LiteralPath $configFile) {
    $raw = [System.IO.File]::ReadAllText($configFile, [System.Text.Encoding]::UTF8)
    $config = if ([string]::IsNullOrWhiteSpace($raw)) { [pscustomobject]@{} } else { $raw | ConvertFrom-Json }
} else {
    $config = [pscustomobject]@{}
}

$server = [pscustomobject]@{
    command = [System.IO.Path]::GetFullPath($PythonPath)
    args = @("-m", "global_memory", "mcp", "stdio")
    env = [pscustomobject]@{
        PYTHONPATH = $sourceRoot
        GALOIS_ROOT = $root
    }
}
$servers = [ordered]@{}
if ($null -ne $config.mcpServers) {
    foreach ($property in $config.mcpServers.psobject.Properties) {
        if ($property.Name -ne "global-memory") {
            $servers[$property.Name] = $property.Value
        }
    }
}
$servers["galois"] = $server
if ($null -eq $config.psobject.Properties["mcpServers"]) {
    $config | Add-Member -NotePropertyName mcpServers -NotePropertyValue ([pscustomobject]$servers)
} else {
    $config.mcpServers = [pscustomobject]$servers
}

$json = $config | ConvertTo-Json -Depth 64
if ($PSCmdlet.ShouldProcess($configFile, "merge read-only Galois MCP server")) {
    if (-not (Test-Path -LiteralPath $configDirectory)) {
        New-Item -ItemType Directory -Path $configDirectory -Force | Out-Null
    }
    if (Test-Path -LiteralPath $configFile) {
        $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
        $backup = "$configFile.galois-$stamp.bak"
        Copy-Item -LiteralPath $configFile -Destination $backup
    } else {
        $backup = $null
    }
    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($configFile, $json + [Environment]::NewLine, $utf8NoBom)
    [pscustomobject]@{
        ok = $true
        host = "claude-desktop"
        server = "galois"
        config_path = $configFile
        backup_path = $backup
        command = [System.IO.Path]::GetFullPath($PythonPath)
        mode = "read-only"
        restart_required = $true
    } | ConvertTo-Json -Depth 4
}
