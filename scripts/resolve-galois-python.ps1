function Resolve-GaloisPython {
    $candidates = [System.Collections.Generic.List[string]]::new()
    foreach ($candidate in @(
        $env:GALOIS_PYTHON,
        $(if ($env:CONDA_PREFIX) { Join-Path $env:CONDA_PREFIX "python.exe" }),
        $env:GM_PYTHON,
        $(if ($env:USERPROFILE) { Join-Path $env:USERPROFILE "miniconda3\python.exe" }),
        $(if ($env:USERPROFILE) { Join-Path $env:USERPROFILE "anaconda3\python.exe" })
    )) {
        if ($candidate) { [void]$candidates.Add($candidate) }
    }

    $pathPython = Get-Command python -ErrorAction SilentlyContinue
    if ($pathPython) { [void]$candidates.Add($pathPython.Source) }

    if ($env:LOCALAPPDATA) {
        $pythonHome = Join-Path $env:LOCALAPPDATA "Programs\Python"
        if (Test-Path -LiteralPath $pythonHome) {
            Get-ChildItem -LiteralPath $pythonHome -Directory -ErrorAction SilentlyContinue |
                Sort-Object Name -Descending |
                ForEach-Object { [void]$candidates.Add((Join-Path $_.FullName "python.exe")) }
        }
    }

    foreach ($candidate in $candidates) {
        if (Test-Path -LiteralPath $candidate -PathType Leaf) {
            return [System.IO.Path]::GetFullPath($candidate)
        }
    }
    throw "No Python runtime found. Set GALOIS_PYTHON to a Python 3.11-3.13 executable."
}
