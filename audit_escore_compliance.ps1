param(
    [string]$TargetPath = "stories",
    [string]$WhitelistPath = "whitelist.txt",
    [string]$PNWhitelistPath = "PN_whitelist.txt",
    [string]$LocalWhitelistPath = "",
    [string[]]$Extensions = @(".md", ".txt"),
    [string[]]$ApprovePN = @(),
    [switch]$NoRecurse
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Load-WhitelistSet {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) {
        throw "File not found: $Path"
    }

    $set = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::Ordinal)
    $lines = Get-Content -LiteralPath $Path -Encoding UTF8
    foreach ($line in $lines) {
        $token = $line.Trim()
        if ($token.Length -eq 0) { continue }
        if ($token.StartsWith("#")) { continue }
        [void]$set.Add($token.ToLowerInvariant())
    }

    return ,$set
}

function Save-WhitelistSet {
    param(
        [string]$Path,
        [System.Collections.Generic.HashSet[string]]$Set
    )

    $sorted = $Set.ToArray() | Sort-Object
    Set-Content -LiteralPath $Path -Value $sorted -Encoding UTF8
}

function Get-TextFiles {
    param(
        [string]$Path,
        [string[]]$AllowedExtensions,
        [bool]$Recurse
    )

    if (-not (Test-Path -LiteralPath $Path)) {
        throw "Target path not found: $Path"
    }

    $item = Get-Item -LiteralPath $Path
    if ($item.PSIsContainer) {
        $files = Get-ChildItem -LiteralPath $Path -File -Recurse:$Recurse
        if ($AllowedExtensions.Count -gt 0) {
            $files = $files | Where-Object { $AllowedExtensions -contains $_.Extension.ToLowerInvariant() }
        }
        return $files
    }

    return @($item)
}

$coreSet = Load-WhitelistSet -Path $WhitelistPath
$pnSet = Load-WhitelistSet -Path $PNWhitelistPath

if ($LocalWhitelistPath -and (Test-Path -LiteralPath $LocalWhitelistPath)) {
    $localSet = Load-WhitelistSet -Path $LocalWhitelistPath
    foreach ($t in $localSet) { [void]$coreSet.Add($t) }
    Write-Host "Loaded local whitelist: $LocalWhitelistPath ($($localSet.Count) tokens merged into core)"
}

if ($ApprovePN.Count -gt 0) {
    $added = 0
    foreach ($name in $ApprovePN) {
        $n = $name.Trim().ToLowerInvariant()
        if ($n.Length -eq 0) { continue }
        if ($pnSet.Add($n)) { $added++ }
    }
    Save-WhitelistSet -Path $PNWhitelistPath -Set $pnSet
    Write-Host "Added $added proper noun token(s) to $PNWhitelistPath"
}

$files = @(Get-TextFiles -Path $TargetPath -AllowedExtensions $Extensions -Recurse:(-not $NoRecurse))
if ($files.Count -eq 0) {
    Write-Host "No files found to audit."
    exit 0
}

$unknownCounts = [System.Collections.Generic.Dictionary[string,int]]::new([System.StringComparer]::Ordinal)
$unknownLocations = [System.Collections.Generic.Dictionary[string,System.Collections.Generic.List[string]]]::new([System.StringComparer]::Ordinal)
$pnCandidateCounts = [System.Collections.Generic.Dictionary[string,int]]::new([System.StringComparer]::Ordinal)

# Token regex: words and standalone numbers.
$tokenRegex = [regex]"\p{L}+|\p{N}+"

$totalTokens = 0

foreach ($file in $files) {
    $lines = @(Get-Content -LiteralPath $file.FullName -Encoding UTF8)

    for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]
        if ($line.TrimStart().StartsWith('%%META')) {
            continue
        }
        $matches = $tokenRegex.Matches($line)

        foreach ($match in $matches) {
            $original = $match.Value
            $token = $original.ToLowerInvariant()
            $totalTokens++

            if ($coreSet.Contains($token) -or $pnSet.Contains($token)) {
                continue
            }

            if ($unknownCounts.ContainsKey($token)) {
                $unknownCounts[$token]++
            }
            else {
                $unknownCounts[$token] = 1
            }

            if (-not $unknownLocations.ContainsKey($token)) {
                $unknownLocations[$token] = [System.Collections.Generic.List[string]]::new()
            }

            if ($unknownLocations[$token].Count -lt 3) {
                $rel = Resolve-Path -LiteralPath $file.FullName -Relative
                $unknownLocations[$token].Add("${rel}:$($i + 1): $line")
            }

            $prefix = $line.Substring(0, $match.Index)
            $isFirstWordOnLine = ($prefix -match '^[^\p{L}\p{N}]*$')
            $looksCapitalized = ($original -cmatch "^\p{Lu}")
            if ($looksCapitalized -and -not ($isFirstWordOnLine -and $coreSet.Contains($token))) {
                if ($pnCandidateCounts.ContainsKey($token)) {
                    $pnCandidateCounts[$token]++
                }
                else {
                    $pnCandidateCounts[$token] = 1
                }
            }
        }
    }
}

$totalUnknown = ($unknownCounts.Values | Measure-Object -Sum).Sum
if (-not $totalUnknown) { $totalUnknown = 0 }

$oocRatio = 0.0
$oneInN = 0
if ($totalTokens -gt 0) {
    $oocRatio = [math]::Round(100.0 * $totalUnknown / $totalTokens, 1)
    if ($totalUnknown -gt 0) {
        $oneInN = [math]::Round($totalTokens / $totalUnknown, 0)
    }
}

Write-Host "\n=== ESCore Audit Summary ==="
Write-Host "Files scanned: $($files.Count)"
Write-Host "Total word tokens: $totalTokens"
Write-Host "Unknown token occurrences: $totalUnknown"
Write-Host "Unique unknown tokens: $($unknownCounts.Count)"
if ($totalUnknown -gt 0) {
    Write-Host "Out-of-core ratio: $oocRatio% (about 1 in $oneInN tokens)"
}
else {
    Write-Host "Out-of-core ratio: 0% (fully within core)"
}
Write-Host "PN whitelist size: $($pnSet.Count)"
Write-Host "Note: flat out-of-core counts Bucket A (inflected core verbs) + B (transparent nouns) + C (new lexemes) together."
Write-Host "      For story-tier, judge Bucket C (genuinely new lexemes), not this flat number. See ESCore.md 22.8."

if ($unknownCounts.Count -eq 0) {
    Write-Host "\nNo unknown tokens found."
    exit 0
}

Write-Host "\n=== Unknown Tokens (frequency) ==="
$unknownSorted = $unknownCounts.GetEnumerator() | Sort-Object -Property @{Expression = 'Value'; Descending = $true}, @{Expression = 'Key'; Descending = $false}
foreach ($entry in $unknownSorted) {
    Write-Host ("{0,5}  {1}" -f $entry.Value, $entry.Key)
}

Write-Host "\n=== Sample Locations (up to 3 per token) ==="
foreach ($entry in $unknownSorted) {
    Write-Host "\n[$($entry.Key)]"
    foreach ($loc in $unknownLocations[$entry.Key]) {
        Write-Host "  $loc"
    }
}

if ($pnCandidateCounts.Count -gt 0) {
    Write-Host "\n=== Proper-Noun Candidates (unknown + capitalized) ==="
    $pnSorted = $pnCandidateCounts.GetEnumerator() | Sort-Object -Property @{Expression = 'Value'; Descending = $true}, @{Expression = 'Key'; Descending = $false}
    foreach ($entry in $pnSorted) {
        Write-Host ("{0,5}  {1}" -f $entry.Value, $entry.Key)
    }

    Write-Host "\nTo approve candidates into PN whitelist:"
    Write-Host "  .\audit_escore_compliance.ps1 -ApprovePN name1,name2,name3"
}
else {
    Write-Host "\nNo capitalized unknown-token candidates found."
}
