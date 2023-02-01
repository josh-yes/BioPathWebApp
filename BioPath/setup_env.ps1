$cwd = Get-Location
$cwd = Split-Path -Path $cwd -Parent
$env:BIOPATH_ROOT_PATH = $cwd