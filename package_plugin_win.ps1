param(
    [String]$wantedVer,
    [Parameter(Mandatory=$true)]
    [String]$plugin)


if ([string]::IsNullOrEmpty($plugin) -or [string]::IsNullOrWhitespace($plugin)) {
    Write-Error "Pass the file name or package name of the plugin release to install, to this script";
}

Write-Host "Requested peek plugin is $plugin"
# Replace String with underscores
$pluginUnder=$plugin.Trim("/-(\d+(\.)).*/g") -replace '-','_'

# Make Powershell stop if it has errors
$ErrorActionPreference = "Stop"

if (-Not [string]::IsNullOrEmpty($wantedVer)) {
    Write-Host "Requested version is $wantedVer"
}

# Get the current location
$startDir=Get-Location

$baseDir="$startDir\dist_win_$pluginUnder";

# Delete the existing dist dir if it exists
If (Test-Path $baseDir){
    Remove-Item $baseDir -Force -Recurse;
}

# Create our new dist dir
New-Item $baseDir -ItemType directory;

# ------------------------------------------------------------------------------
# Download the peek platform and all it's dependencies
New-Item "$baseDir\py" -ItemType directory;
Copy-Item $plugin "$baseDir\py" -Force;
Set-Location "$baseDir\py";
Write-Host "Downloading and creating windows wheels";
pip wheel --no-cache $plugin;

# Make sure we've downloaded the right version
$peekPkgName = Get-ChildItem ".\" |
                    Where-Object {$_.Name.StartsWith("$pluginUnder-")} |
                    Select-Object -exp Name;
$peekPkgVer = $peekPkgName.Split('-')[1];

if (-Not [string]::IsNullOrEmpty($wantedVer) -and $peekPkgVer -ne $wantedVer) {
    Set-Location "$startDir";
    Write-Error "We've downloaded version $peekPkgVer, but you wanted ver $wantedVer";
} else {
    Write-Host "We've downloaded version $peekPkgVer";
}

# ------------------------------------------------------------------------------
# Set the location back to where we were.
Set-Location $startDir;

# Finally, version the directory
$releaseDir="$($baseDir)_$($peekPkgVer)";
$relaseZip="$($releaseDir).zip"
Move-Item $baseDir $releaseDir -Force;

# Create the zip file
Add-Type -Assembly System.IO.Compression.FileSystem;
$compressionLevel = [System.IO.Compression.CompressionLevel]::Optimal;
[System.IO.Compression.ZipFile]::CreateFromDirectory(
    $releaseDir, $relaseZip, $compressionLevel, $false)

# We're all done.
Write-Host "Successfully created release $peekPkgVer";
Write-Host "Located at $relaseZip";
