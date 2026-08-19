$ProjectPath = Split-Path -Parent $PSScriptRoot
$PythonPath = Join-Path $ProjectPath '.venv\Scripts\python.exe'
$ConfigPath = Join-Path $ProjectPath 'mkdocs.yml'

$ErrorActionPreference = 'Stop'
& $PythonPath -m mkdocs serve --config-file $ConfigPath
if ($LASTEXITCODE) { throw "MkDocs failed with exit code $LASTEXITCODE." }
