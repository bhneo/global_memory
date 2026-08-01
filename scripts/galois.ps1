$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$env:PYTHONPATH = Join-Path $repoRoot "src"
$env:GALOIS_ROOT = $repoRoot
$env:GM_ROOT = $repoRoot
. (Join-Path $PSScriptRoot "resolve-galois-python.ps1")

$python = Resolve-GaloisPython

& $python -m global_memory @args
exit $LASTEXITCODE
