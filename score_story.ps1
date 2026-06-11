<#
.SYNOPSIS
    Pre-emptively measure the AVD score and UL (User Level) of ESCore stories,
    fully standalone — without running the WeaveLang application.

.DESCRIPTION
    Thin wrapper around avd_ul_score.py. It reproduces weavelang's
    `measure_user_score` math in-process, reading only static assets
    (the spaCy es_core_news_lg model + the master frequency list) from the
    weavelang folder. The weavelang GUI/daemon is never launched, so there is
    no risk of corrupting its project state.

    Validated parity (matches weavelang exactly):
        La_Llorona     UL27
        John_and_Alice UL21
        Un_Lugar_Bueno UL23
        Nadie_Lo_Vio   UL24

.PARAMETER Paths
    One or more story .txt files to score (absolute or relative). If omitted,
    scans the local stories\ folder for top-level Spanish .txt files
    (skipping *_en.txt English mirrors).

.PARAMETER Json
    Emit JSON instead of a table.

.EXAMPLE
    .\score_story.ps1 stories\La_Llorona\La_Llorona.txt

.EXAMPLE
    .\score_story.ps1                 # scores all top-level story .txt files

.EXAMPLE
    .\score_story.ps1 -Json stories\Un_Lugar_Bueno\Un_Lugar_Bueno.txt
#>
[CmdletBinding()]
param(
    [Parameter(Position = 0, ValueFromRemainingArguments = $true)]
    [string[]]$Paths,

    [switch]$Json
)

try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch {}

$ScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
$Scorer = Join-Path $ScriptRoot 'avd_ul_score.py'

# Python interpreter that has spaCy + es_core_news_lg (the weavelang venv).
# Override with $env:ESCORE_PYTHON if you set up a dedicated ESCore env.
$Python = if ($env:ESCORE_PYTHON) { $env:ESCORE_PYTHON }
          else { 'E:\Bill\development\weavelang\.venv\Scripts\python.exe' }

if (-not (Test-Path -LiteralPath $Python)) {
    Write-Host "ERROR: Python interpreter not found: $Python" -ForegroundColor Red
    Write-Host "Set `$env:ESCORE_PYTHON to a Python that has spacy + es_core_news_lg + snowballstemmer." -ForegroundColor Yellow
    exit 1
}

function Resolve-StoryFiles {
    param([string[]]$Inputs)

    if ($Inputs -and $Inputs.Count -gt 0) {
        $resolved = @()
        foreach ($p in $Inputs) {
            $full = if ([System.IO.Path]::IsPathRooted($p)) { $p } else { Join-Path $ScriptRoot $p }
            if (Test-Path -LiteralPath $full -PathType Leaf) {
                $resolved += (Resolve-Path -LiteralPath $full).Path
            }
            else {
                Write-Warning "Skipping (not found): $p"
            }
        }
        return $resolved
    }

    # Default: top-level Spanish story files under stories\, skip English mirrors.
    $storiesDir = Join-Path $ScriptRoot 'stories'
    if (-not (Test-Path -LiteralPath $storiesDir)) { return @() }
    return Get-ChildItem -Path $storiesDir -Directory | ForEach-Object {
        Get-ChildItem -Path $_.FullName -Filter *.txt -File |
            Where-Object { $_.Name -notmatch '_en\.txt$' }
    } | Select-Object -ExpandProperty FullName
}

$files = Resolve-StoryFiles -Inputs $Paths
if (-not $files -or $files.Count -eq 0) {
    Write-Host "No story files to measure. Pass a path, e.g.:" -ForegroundColor Yellow
    Write-Host "    .\score_story.ps1 stories\La_Llorona\La_Llorona.txt"
    exit 1
}

$argList = @($Scorer)
if ($Json) { $argList += '--json' }
$argList += $files

& $Python @argList
exit $LASTEXITCODE
