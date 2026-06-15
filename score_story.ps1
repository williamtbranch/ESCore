<#
.SYNOPSIS
    Pre-emptively measure the AVD score and UL (User Level) of ESCore stories,
    fully standalone — without running the WeaveLang application.

.DESCRIPTION
    Thin wrapper around avd_ul_score.py. It computes ESCore's OWN AVD/UL
    difficulty metric in-process, reading only static assets (the spaCy
    es_core_news_lg model + the master frequency list) from the weavelang
    folder. The weavelang GUI/daemon is never launched, so there is no risk of
    corrupting its project state.

    This is NOT a 1:1 replica of weavelang's score: a verb-form rescue step
    corrects spaCy mis-lemmatizations (enclitic imperatives like "diselo" and
    guillemet-mistagged verbs like "«Vuelve") that weavelang's raw pipeline
    leaves as spuriously rare. Relative difficulty ordering still carries over.
    Reference UL values (corrected scorer):
        La_Llorona     UL26
        John_and_Alice UL20
        Un_Lugar_Bueno UL22
        Nadie_Lo_Vio   UL23

.PARAMETER Paths
    One or more story .txt files to score (absolute or relative). If omitted,
    scans the local stories\ folder for top-level Spanish .txt files
    (skipping *_en.txt English mirrors).

.PARAMETER Json
    Emit JSON instead of a table.

.PARAMETER DomainLemmas
    Optional plain-text domain lemma policy file (one lemma per line; optional
    '=rank'). Lemmas in this file are scored with a gentler effective rank via
    avd_ul_score.py (min(raw_rank, policy_rank)).

.PARAMETER DomainDefaultRank
    Default policy rank used by DomainLemmas lines that do not provide a rank.

.EXAMPLE
    .\score_story.ps1 stories\La_Llorona\La_Llorona.txt

.EXAMPLE
    .\score_story.ps1                 # scores all top-level story .txt files

.EXAMPLE
    .\score_story.ps1 -Json stories\Un_Lugar_Bueno\Un_Lugar_Bueno.txt

.EXAMPLE
    .\score_story.ps1 stories\Moby_Dick\chapters\Chapter_001_Loomings\story.txt -DomainLemmas stories\Moby_Dick\domain_lemmas.txt
#>
[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [string[]]$Paths,

    [switch]$Json,

    [int]$ShowRare = 0,

    [string]$DomainLemmas,

    [int]$DomainDefaultRank = 320,

    [double]$Coverage = 0.0
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
        return @($resolved)
    }

    # Default: top-level Spanish story files under stories\, skip English mirrors.
    $storiesDir = Join-Path $ScriptRoot 'stories'
    if (-not (Test-Path -LiteralPath $storiesDir)) { return @() }
    return @(Get-ChildItem -Path $storiesDir -Directory | ForEach-Object {
        Get-ChildItem -Path $_.FullName -Filter *.txt -File |
            Where-Object { $_.Name -notmatch '_en\.txt$' }
    } | Select-Object -ExpandProperty FullName)
}

$files = @(Resolve-StoryFiles -Inputs $Paths)
if (-not $files -or $files.Count -eq 0) {
    Write-Host "No story files to measure. Pass a path, e.g.:" -ForegroundColor Yellow
    Write-Host "    .\score_story.ps1 stories\La_Llorona\La_Llorona.txt"
    exit 1
}

$argList = @($Scorer)
if ($Json) { $argList += '--json' }
if ($ShowRare -gt 0) { $argList += @('--show-rare', $ShowRare) }
if ($Coverage -gt 0.0) { $argList += @('--coverage', $Coverage) }
if ($DomainLemmas) {
    $policyPath = if ([System.IO.Path]::IsPathRooted($DomainLemmas)) {
        $DomainLemmas
    }
    else {
        Join-Path $ScriptRoot $DomainLemmas
    }
    $argList += @('--domain-lemmas', $policyPath, '--domain-default-rank', $DomainDefaultRank)
}
$argList += $files

& $Python @argList
exit $LASTEXITCODE
