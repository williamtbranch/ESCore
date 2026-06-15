[CmdletBinding()]
param(
    [string[]]$StoryDirs,

    [switch]$ScanTopLevelStories,

    [switch]$AllowNoSource,

    [string]$DateStamp = (Get-Date -Format 'yyyy-MM-dd')
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch {}

$ScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
$ScoreTool = Join-Path $ScriptRoot 'score_story.ps1'

$DefaultVenvPython = 'E:\Bill\development\weavelang\.venv\Scripts\python.exe'
$PythonCmd = $null
$PythonPrefixArgs = @()

if ($env:ESCORE_PYTHON -and (Test-Path -LiteralPath $env:ESCORE_PYTHON -PathType Leaf)) {
    $PythonCmd = $env:ESCORE_PYTHON
}
elseif (Test-Path -LiteralPath $DefaultVenvPython -PathType Leaf) {
    $PythonCmd = $DefaultVenvPython
}
else {
    $PythonCmd = 'py'
    $PythonPrefixArgs = @('-3.13')
}

function Resolve-StoryDirPath {
    param([string]$PathValue)

    if ([string]::IsNullOrWhiteSpace($PathValue)) {
        throw 'Story directory path cannot be empty.'
    }

    $full = if ([System.IO.Path]::IsPathRooted($PathValue)) {
        $PathValue
    }
    else {
        Join-Path $ScriptRoot $PathValue
    }

    if (-not (Test-Path -LiteralPath $full -PathType Container)) {
        throw "Story directory not found: $PathValue"
    }

    return (Resolve-Path -LiteralPath $full).Path
}

function Get-WordCount {
    param([string]$Text)

    $matches = [regex]::Matches($Text, "[\p{L}]+(?:['’-][\p{L}]+)*")
    return $matches.Count
}

function Get-CountableText {
    param([string]$Path)

    $text = Get-Content -LiteralPath $Path -Raw -Encoding UTF8
    $lines = $text -split "`r?`n"
    $keptLines = @(foreach ($line in $lines) {
        if ($line -match '^\s*%%META\b') { continue }
        $line
    })

    if ([System.IO.Path]::GetExtension($Path).ToLowerInvariant() -eq '.md') {
        $separatorIndex = [Array]::IndexOf($keptLines, '---')
        if ($separatorIndex -ge 0 -and $separatorIndex + 1 -lt $keptLines.Count) {
            $keptLines = $keptLines[($separatorIndex + 1)..($keptLines.Count - 1)]
        }
    }

    return ($keptLines -join "`n")
}

function Get-WordCountCheck {
    param(
        [string]$SubmissionPath,
        [string]$SourcePath,
        [double]$MinPercent = 75.0,
        [double]$MaxPercent = 120.0
    )

    $submissionWords = Get-WordCount -Text (Get-CountableText -Path $SubmissionPath)
    $sourceWords = Get-WordCount -Text (Get-CountableText -Path $SourcePath)
    if ($sourceWords -le 0) {
        throw "Source has zero countable words after stripping metadata: $SourcePath"
    }

    $percent = [Math]::Round((100.0 * $submissionWords / $sourceWords), 2)
    return [ordered]@{
        submission_words = $submissionWords
        source_words = $sourceWords
        percent_of_source = $percent
        min_percent = $MinPercent
        max_percent = $MaxPercent
        pass = ($percent -ge $MinPercent) -and ($percent -le $MaxPercent)
    }
}

function Get-NoSourceWordCountCheck {
    param(
        [string]$SubmissionPath,
        [double]$MinPercent = 75.0,
        [double]$MaxPercent = 120.0
    )

    $submissionWords = Get-WordCount -Text (Get-CountableText -Path $SubmissionPath)
    return [ordered]@{
        submission_words = $submissionWords
        source_words = 0
        percent_of_source = $null
        min_percent = $MinPercent
        max_percent = $MaxPercent
        pass = $false
        no_source = $true
    }
}

function Get-IllustrationCheck {
    param(
        [string]$SubmissionPath,
        [int]$SubmissionWords,
        [int]$WordsPerIllustration = 250,
        [double]$TolerancePercent = 15.0,
        [bool]$TextGatesPass
    )

    $submissionText = Get-Content -LiteralPath $SubmissionPath -Raw -Encoding UTF8
    $illustrationRegex = [regex]'(?im)^\s*%%META\s+illustration\s*:\s*([^%]+)%%\s*$'
    $matches = $illustrationRegex.Matches($submissionText)
    $markers = @($matches | ForEach-Object { $_.Groups[1].Value.Trim() })
    $actualIllustrations = $markers.Count

    $requiredIllustrations = [int][Math]::Round(([double]$SubmissionWords / [double]$WordsPerIllustration), [System.MidpointRounding]::AwayFromZero)
    if ($requiredIllustrations -lt 1) {
        $requiredIllustrations = 1
    }

    $toleranceByPercent = ([double]$requiredIllustrations) * ($TolerancePercent / 100.0)
    $illustrationTolerance = [double][Math]::Min(1.0, $toleranceByPercent)
    $minAllowedIllustrations = [int][Math]::Ceiling(([double]$requiredIllustrations) - $illustrationTolerance)
    $maxAllowedIllustrations = [int][Math]::Floor(([double]$requiredIllustrations) + $illustrationTolerance)
    if ($minAllowedIllustrations -lt 1) {
        $minAllowedIllustrations = 1
    }
    if ($maxAllowedIllustrations -lt $minAllowedIllustrations) {
        $maxAllowedIllustrations = $minAllowedIllustrations
    }

    $illustrationPass = if ($TextGatesPass) {
        ($actualIllustrations -ge $minAllowedIllustrations) -and ($actualIllustrations -le $maxAllowedIllustrations)
    }
    else {
        $true
    }

    return [ordered]@{
        words_per_illustration = $WordsPerIllustration
        required_count = $requiredIllustrations
        actual_count = $actualIllustrations
        tolerance_percent = $TolerancePercent
        min_allowed = $minAllowedIllustrations
        max_allowed = $maxAllowedIllustrations
        evaluated = $TextGatesPass
        pass = $illustrationPass
        deferred_until_text_pass = (-not $TextGatesPass)
        markers = @($markers)
    }
}

function Get-SourcePath {
    param([string]$StoryDir)

    $sourceTxt = Join-Path $StoryDir 'source.txt'
    if (Test-Path -LiteralPath $sourceTxt -PathType Leaf) {
        return $sourceTxt
    }

    $storyEnglish = Join-Path $StoryDir 'story_en.md'
    if (Test-Path -LiteralPath $storyEnglish -PathType Leaf) {
        return $storyEnglish
    }

    return $null
}

function Get-DomainLemmaPath {
    param([string]$StoryDir)

    if ($StoryDir -notmatch [regex]::Escape("stories\Moby_Dick\chapters\")) {
        return $null
    }

    $domainPath = Join-Path $ScriptRoot 'stories\Moby_Dick\domain_lemmas.txt'
    if (Test-Path -LiteralPath $domainPath -PathType Leaf) {
        return $domainPath
    }

    return $null
}

function Get-DisplayTitle {
    param([string]$StoryDir)

    $dirName = Split-Path -Leaf $StoryDir
    $parentDirName = Split-Path -Leaf (Split-Path -Parent $StoryDir)
    if ($dirName -match '^Chapter_(\d+)_([A-Za-z0-9_]+)$') {
        $chapterNumber = [int]$Matches[1]
        $chapterTitle = ($Matches[2] -replace '_', ' ')
        return ('Moby Dick {0} Chapter {1} "{2}"' -f [char]0x2014, $chapterNumber, $chapterTitle)
    }

    if ($parentDirName -match '^Chapter_(\d+)_([A-Za-z0-9_]+)$') {
        $chapterNumber = [int]$Matches[1]
        $chapterTitle = ($Matches[2] -replace '_', ' ')
        $variantLabel = ($dirName -replace '_', ' ')
        return ('Moby Dick {0} Chapter {1} "{2}" ({3})' -f [char]0x2014, $chapterNumber, $chapterTitle, $variantLabel)
    }

    $headingPath = Join-Path $StoryDir 'story.md'
    if (Test-Path -LiteralPath $headingPath -PathType Leaf) {
        $headingLine = Get-Content -LiteralPath $headingPath -Encoding UTF8 |
            Where-Object { $_ -match '^#\s+' } |
            Select-Object -First 1
        if ($headingLine) {
            return ($headingLine -replace '^#\s+', '').Trim()
        }
    }

    return ($dirName -replace '_', ' ')
}

function Get-TargetStoryDirs {
    $targets = [System.Collections.Generic.List[string]]::new()

    foreach ($storyDir in $StoryDirs) {
        $targets.Add((Resolve-StoryDirPath -PathValue $storyDir))
    }

    if ($ScanTopLevelStories) {
        $storiesRoot = Join-Path $ScriptRoot 'stories'
        Get-ChildItem -LiteralPath $storiesRoot -Directory | ForEach-Object {
            $storyPath = Join-Path $_.FullName 'story.txt'
            if (Test-Path -LiteralPath $storyPath -PathType Leaf) {
                $targets.Add($_.FullName)
            }
        }
    }

    @($targets | Select-Object -Unique)
}

function Write-MetricsFile {
    param([string]$StoryDir)

    $submissionPath = Join-Path $StoryDir 'story.txt'
    if (-not (Test-Path -LiteralPath $submissionPath -PathType Leaf)) {
        throw "story.txt not found in $StoryDir"
    }

    $sourcePath = Get-SourcePath -StoryDir $StoryDir
    if (-not $sourcePath) {
        if (-not $AllowNoSource) {
            Write-Warning "Skipping $StoryDir because no source.txt or story_en.md was found."
            return $false
        }
    }

    $domainPath = Get-DomainLemmaPath -StoryDir $StoryDir
    $scoreParams = @{
        Json = $true
        Coverage = 0.85
        Paths = @($submissionPath)
    }
    if ($domainPath) {
        $scoreParams.DomainLemmas = $domainPath
    }

    $scoreJson = & $ScoreTool @scoreParams
    if ($LASTEXITCODE -ne 0) {
        throw "score_story.ps1 failed for $StoryDir"
    }

    $scoreParsed = $scoreJson | ConvertFrom-Json
    if ($scoreParsed -is [array]) {
        $score = $scoreParsed[0]
    }
    else {
        $score = $scoreParsed
    }

    if ($null -eq $score.i_score) {
        throw "score_story.ps1 did not return i_score data for $StoryDir"
    }

    $wordCountCheck = if ($sourcePath) {
        $wc = Get-WordCountCheck -SubmissionPath $submissionPath -SourcePath $sourcePath
        $wc.no_source = $false
        $wc
    }
    else {
        Get-NoSourceWordCountCheck -SubmissionPath $submissionPath
    }
    $iLevel = [double]$score.i_score.i_level
    $iPass = $iLevel -le 25.5
    $corePass = $iPass -and [bool]$wordCountCheck.pass
    $illustrationCheck = Get-IllustrationCheck -SubmissionPath $submissionPath -SubmissionWords ([int]$wordCountCheck.submission_words) -TextGatesPass $corePass
    $overallPass = $corePass -and [bool]$illustrationCheck.pass

    $title = Get-DisplayTitle -StoryDir $StoryDir
    $status = if ($overallPass) { 'PASS' } else { 'FAIL' }
    $iStatus = if ($iPass) { 'PASS' } else { 'FAIL' }
    $wcStatus = if ($wordCountCheck.pass) { 'PASS' } else { 'FAIL' }
    $illStatus = if ($illustrationCheck.evaluated) {
        if ($illustrationCheck.pass) { 'PASS' } else { 'FAIL' }
    }
    else {
        'SKIP'
    }

    $markerLines = if ($illustrationCheck.markers.Count -gt 0) {
        ($illustrationCheck.markers | ForEach-Object { "    * $_" }) -join "`r`n"
    }
    else {
        '    * none'
    }

    $content = @(
        "$title",
        ('DRC Metrics Log {0} {1}' -f [char]0x2014, $DateStamp),
        '',
        '====================================================================',
        "OVERALL STATUS: $status",
        '====================================================================',
        '',
        '1. TEXT DIFFICULTY GATES',
        '------------------------',
        "i-score (Primary Gate):    $iStatus",
        ('  - iLevel:                {0:N1} (limit <= 25.5)' -f [double]$score.i_score.i_level),
        ('  - iRank:                 {0:N0} (85% boundary word frequency rank)' -f [double]$score.i_score.i_rank),
        ('  - Coverage Level:        {0:N2} (85% of text in core, 15% in +1 tail)' -f [double]$score.i_score.coverage),
        ('  - +1 Tail Details:       {0:N1}% of running text is unpunished vocabulary' -f [double]$score.i_score.plus1_pct),
        ('    * Rare Tokens:         {0}' -f [int]$score.i_score.plus1_tokens),
        ('    * Unique Rare Lemmas:  {0}' -f [int]$score.i_score.plus1_unique),
        '',
        ('User Level (Info-Only):    UL{0} (Gating bypassed per free-flow policy)' -f [int][Math]::Floor([double]$score.ul_exact)),
        ('  - UL (exact decimal):    {0:N1}' -f [double]$score.ul_exact),
        ('  - UL (rounded floor):    UL{0}' -f [int][Math]::Floor([double]$score.ul_exact)),
        ('  - AVD (tail-weighted):   {0:N2}' -f [double]$score.avd),
        ('  - p85 Rank:              {0:N0}' -f [double]$score.p85_rank),
        ('  - p95 Rank:              {0:N0}' -f [double]$score.p95_rank),
        '',
        '2. LENGTH GATE',
        '--------------',
        "Word Count Ratio:          $wcStatus",
        ('  - Spanish Submission:    {0:N0} words (excluding metadata)' -f [int]$wordCountCheck.submission_words),
        $(if ($wordCountCheck.no_source) { '  - English Source:        [none provided]' } else { ('  - English Source:        {0:N0} words' -f [int]$wordCountCheck.source_words) }),
        $(if ($wordCountCheck.no_source) { ('  - Percentage:            n/a (auto-fail; allowed range: {0:N1}% - {1:N1}%)' -f [double]$wordCountCheck.min_percent, [double]$wordCountCheck.max_percent) } else { ('  - Percentage:            {0:N2}% of source (allowed range: {1:N1}% - {2:N1}%)' -f [double]$wordCountCheck.percent_of_source, [double]$wordCountCheck.min_percent, [double]$wordCountCheck.max_percent) }),
        '',
        '3. PACKAGING GATE',
        '-----------------',
        "Illustration Density:      $illStatus",
        ('  - Target Density:        1 illustration per {0} words' -f [int]$illustrationCheck.words_per_illustration),
        ('  - Required Count:        {0} (allowed range: {1} - {2})' -f [int]$illustrationCheck.required_count, [int]$illustrationCheck.min_allowed, [int]$illustrationCheck.max_allowed),
        ('  - Actual Count:          {0} illustration markers' -f [int]$illustrationCheck.actual_count),
        $markerLines
    ) -join "`r`n"

    $outputPath = Join-Path $StoryDir 'metrics.txt'
    Set-Content -LiteralPath $outputPath -Value $content -Encoding UTF8
    Write-Host "Wrote $outputPath"
    return $true
}

$targetDirs = @(Get-TargetStoryDirs)
if (-not $targetDirs -or $targetDirs.Count -eq 0) {
    throw 'No story directories selected.'
}

$written = 0
foreach ($storyDir in $targetDirs) {
    if (Write-MetricsFile -StoryDir $storyDir) {
        $written++
    }
}

Write-Host "Completed. Wrote $written metrics file(s)."