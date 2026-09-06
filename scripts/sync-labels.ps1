[CmdletBinding()]
param(
    [string]$Repository = 'fynx-dev/kyna-release'
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$labels = Get-Content -LiteralPath (Join-Path $PSScriptRoot '..\.github\labels.json') -Raw | ConvertFrom-Json
foreach ($label in $labels) {
    & gh label create $label.name --repo $Repository --color $label.color --description $label.description --force
    if ($LASTEXITCODE -ne 0) {
        throw "Unable to synchronize label $($label.name)."
    }
}
