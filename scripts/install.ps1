param(
    [string]$DestinationRoot = "$HOME\.codex\skills"
)

$ErrorActionPreference = "Stop"

$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$skillRoot = Resolve-Path (Join-Path $scriptPath "..")
$skillName = "civil-thesis-body-writing"
$destination = Join-Path $DestinationRoot $skillName

if (-not (Test-Path $DestinationRoot)) {
    New-Item -ItemType Directory -Path $DestinationRoot | Out-Null
}

if (Test-Path $destination) {
    $timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $backup = "$destination.bak-$timestamp"
    Move-Item -LiteralPath $destination -Destination $backup
    Write-Host "Existing skill backed up to: $backup"
}

Copy-Item -LiteralPath $skillRoot -Destination $destination -Recurse

Write-Host "Installed $skillName to: $destination"
Write-Host "Restart Codex to load the skill."
