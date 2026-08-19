# Vzdálené API: .\tools\run_mkdocs.ps1
# Lokální API: .\tools\run_mkdocs.ps1 -LocalChatApi

param([switch]$LocalChatApi)

$ProjectPath = Split-Path -Parent $PSScriptRoot
$PythonPath = Join-Path $ProjectPath '.venv\Scripts\python.exe'
$ConfigPath = Join-Path $ProjectPath $(if ($LocalChatApi) { 'mkdocs.local.yml' } else { 'mkdocs.yml' })

$ErrorActionPreference = 'Stop'
& $PythonPath -m mkdocs serve --config-file $ConfigPath
if ($LASTEXITCODE) { throw "MkDocs failed with exit code $LASTEXITCODE." }
