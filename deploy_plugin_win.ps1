param([String]$releaseZip)

# Make PowerShell stop if it has errors
$ErrorActionPreference = "Stop"

$7zExe = "C:\Program Files\7-Zip\7z.exe";

if ([string]::IsNullOrEmpty($releaseZip) -or [string]::IsNullOrWhitespace($releaseZip))
{
    Write-Error "Pass the path of the release to install to this script";
}

Write-Host "Requested peek plugin is $plugin"
# Replace String with underscores
$pluginUnder = $plugin.Trim("-0.0.1.tar.gz") -replace '-', '_'
$pluginName = $pluginUnder -replace '-', '_'


# Get the current location
$startDir = Get-Location

$releaseDir = "C:\Users\peek\peek_plugin_dist_win";

# Delete the existing dist dir if it exists
If (Test-Path $releaseDir)
{
    Remove-Item $releaseDir -Force -Recurse;
}

# Create our new release dir
New-Item $releaseDir -ItemType directory;

# Decompress the release
Write-Host "Extracting release to $releaseDir";

if (Test-Path $7zExe)
{
    Write-Host "7z is present, this will be faster";
    Invoke-Expression "&`"$7zExe`" x -y -r `"$releaseZip`" -o`"$releaseDir`"";

}
else
{
    Write-Host "Using standard windows zip handler, this will be slow";
    Add-Type -Assembly System.IO.Compression.FileSystem;
    [System.IO.Compression.ZipFile]::ExtractToDirectory($releaseZip, $releaseDir);
}

# Get the release name from the package
$peekPkgName = Get-ChildItem "$releaseDir\py" |
    Where-Object { $_.Name.StartsWith("$pluginUnder-") } |
    Select-Object -exp Name;
$peekPkgVer = $peekPkgName.Split('-')[1];

# pip install package
pip install --no-index --no-cache "$releaseDir\py\$plugin"

# All done.
Write-Host " ";
Write-Host "$pluginName is now deployed";
Write-Host " ";
