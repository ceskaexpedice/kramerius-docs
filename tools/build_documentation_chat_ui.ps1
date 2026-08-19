# cesta k Angular aplikaci - musi byt lokalne k dispozici
$ProjectPath = 'C:\VA\Projects\VA\documentation-chat\documentation-chat-ui'

$ErrorActionPreference = 'Stop'
npm --prefix $ProjectPath run build
if ($LASTEXITCODE) { throw "Build failed with exit code $LASTEXITCODE." }
Copy-Item (Join-Path $ProjectPath 'dist\documentation-chat-ui\browser\main.js') (Join-Path $PSScriptRoot '..\docs\assets\documentation-chat-ui\documentation-chat-ui.js') -Force
