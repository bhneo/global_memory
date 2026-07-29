[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$ConfigPath = (Join-Path $env:LOCALAPPDATA "Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\Claude\claude_desktop_config.json")
)

$ErrorActionPreference = "Stop"
$launcher = "C:\Users\bhneo\Desktop\project\global-memory-runtime\scripts\gm-mcp-stdio.ps1"
if (-not (Test-Path -LiteralPath $launcher)) {
    throw "Global Memory launcher not found: $launcher"
}

$configFile = [System.IO.Path]::GetFullPath($ConfigPath)
$configDirectory = Split-Path -Parent $configFile
if (-not (Test-Path -LiteralPath $configDirectory)) {
    throw "Claude Desktop config directory not found: $configDirectory"
}

if (Test-Path -LiteralPath $configFile) {
    $raw = [System.IO.File]::ReadAllText($configFile, [System.Text.Encoding]::UTF8)
    $config = if ([string]::IsNullOrWhiteSpace($raw)) { [pscustomobject]@{} } else { $raw | ConvertFrom-Json }
} else {
    $config = [pscustomobject]@{}
}

$server = [pscustomobject]@{
    command = "powershell.exe"
    args = @(
        "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $launcher
    )
}
$servers = [ordered]@{}
if ($null -ne $config.mcpServers) {
    foreach ($property in $config.mcpServers.psobject.Properties) {
        $servers[$property.Name] = $property.Value
    }
}
$servers["global-memory"] = $server
if ($null -eq $config.psobject.Properties["mcpServers"]) {
    $config | Add-Member -NotePropertyName mcpServers -NotePropertyValue ([pscustomobject]$servers)
} else {
    $config.mcpServers = [pscustomobject]$servers
}

$json = $config | ConvertTo-Json -Depth 64
if ($PSCmdlet.ShouldProcess($configFile, "merge read-only Global Memory MCP server")) {
    if (Test-Path -LiteralPath $configFile) {
        $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
        $backup = "$configFile.global-memory-$stamp.bak"
        Copy-Item -LiteralPath $configFile -Destination $backup
    } else {
        $backup = $null
    }
    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($configFile, $json + [Environment]::NewLine, $utf8NoBom)
    [pscustomobject]@{
        ok = $true
        host = "claude-desktop"
        config_path = $configFile
        backup_path = $backup
        launcher = $launcher
        mode = "read-only"
        restart_required = $true
    } | ConvertTo-Json -Depth 4
}
