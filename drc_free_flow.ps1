<#
.SYNOPSIS
    Free-flow Design Rule Check (DRC): i-score + word-count + illustration-density gates.

.DESCRIPTION
        Runs:
      1) score_story.ps1 -Json -Coverage (i-score comprehensible-input gate; UL is
         computed and reported but is INFO-ONLY, not a gate)
      2) word_count_ratio.py --json (85%-120% by default)
            3) Illustration density check on %%META illustration: <key>%% markers

    Returns a combined pass/fail for writing iteration. The text gate is the
    coverage-based i-score (default coverage 0.85, i-level <= 25.5): the rarest
    (1 - coverage) of the text is treated as an unpunished +1 vocabulary tail.

.PARAMETER Submission
    Path to candidate Spanish story text. Must be named story.txt.

.PARAMETER Source
    Path to original/source text for length comparison. Must be named source.txt.

.PARAMETER StoryDir
    Optional story/chapter directory that contains story.txt and source.txt.
    If set, relative Submission/Source paths resolve from this directory.

.PARAMETER UlMin
    Minimum allowed UL after rounding down (default 20). INFO-ONLY: UL is
    reported for the sister app's general-difficulty scale but no longer gates.

.PARAMETER UlMax
    Maximum allowed UL after rounding down (default 23). INFO-ONLY (see UlMin).

.PARAMETER Coverage
    Target known-word coverage for the i-score core (default 0.85). The rarest
    (1 - Coverage) of the text is the unpunished +1 vocabulary tail.

.PARAMETER ILevelMax
    Maximum allowed i-level for the comprehensible core (default 25.5). This is
    the primary text gate.

.PARAMETER MinPercent
    Minimum submission word-count percent vs source (default 85).

.PARAMETER MaxPercent
    Maximum submission word-count percent vs source (default 120).

.PARAMETER WordsPerIllustration
    Target density for illustration markers in submission (default 250 words).

.PARAMETER IllustrationTolerancePercent
    Allowed deviation percent from required illustration count (default 15).
    Effective tolerance is min(1 illustration, percent-based tolerance).

.PARAMETER Json
    Emit combined JSON object.

.PARAMETER NoSource
    Allow scoring when no source text is available. The length gate is marked as
    failed automatically, but i-score, UL, and illustration metrics are still
    computed so Spanish-only samples can be evaluated.

.EXAMPLE
    .\drc_free_flow.ps1 -StoryDir stories\Moby_Dick\chapters\Chapter_001_Loomings
#>
[CmdletBinding()]
param(
    [string]$StoryDir,

    [string]$Submission = 'story.txt',

    [string]$Source = 'source.txt',

    [int]$UlMin = 20,
    [int]$UlMax = 23,

    [double]$Coverage = 0.85,

    [double]$ILevelMax = 25.5,

    [double]$MinPercent = 85,
    [double]$MaxPercent = 120,

    [int]$WordsPerIllustration = 250,

    [double]$IllustrationTolerancePercent = 15,

    [switch]$Json,

    [switch]$NoSource,

    [string]$DomainLemmas,

    [int]$DomainDefaultRank = 320
)

try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch {}

function Resolve-InputPath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$PathValue,

        [Parameter(Mandatory = $true)]
        [string]$BaseDir
    )

    if ([System.IO.Path]::IsPathRooted($PathValue)) {
        return $PathValue
    }

    return (Join-Path $BaseDir $PathValue)
}

function Get-CountableText {
    param([string]$Path)

    $text = Get-Content -LiteralPath $Path -Raw -Encoding UTF8
    $lines = $text -split "`r?`n"
    $keptLines = foreach ($line in $lines) {
        if ($line -match '^\s*%%META\b') { continue }
        $line
    }

    return ($keptLines -join "`n")
}

function Get-WordCount {
    param([string]$Text)

    return ([regex]::Matches($Text, "[\p{L}]+(?:['’-][\p{L}]+)*")).Count
}

$ScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
$ScoreTool = Join-Path $ScriptRoot 'score_story.ps1'
$WordTool = Join-Path $ScriptRoot 'word_count_ratio.py'

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
    # Fallback for machines where the hardcoded WeaveLang venv is unavailable.
    $PythonCmd = 'py'
    $PythonPrefixArgs = @('-3.13')
}

if (-not (Test-Path -LiteralPath $ScoreTool)) {
    Write-Host "ERROR: score_story.ps1 not found: $ScoreTool" -ForegroundColor Red
    exit 1
}
if (-not (Test-Path -LiteralPath $WordTool)) {
    Write-Host "ERROR: word_count_ratio.py not found: $WordTool" -ForegroundColor Red
    exit 1
}
try {
    $null = & $PythonCmd @PythonPrefixArgs '--version'
}
catch {
    Write-Host "ERROR: Could not invoke Python command: $PythonCmd $($PythonPrefixArgs -join ' ')" -ForegroundColor Red
    Write-Host "Set `$env:ESCORE_PYTHON to a valid Python interpreter path." -ForegroundColor Yellow
    exit 1
}

$BaseDir = if ($StoryDir) {
    if ([System.IO.Path]::IsPathRooted($StoryDir)) { $StoryDir } else { Join-Path $ScriptRoot $StoryDir }
} else {
    $ScriptRoot
}

if (-not (Test-Path -LiteralPath $BaseDir -PathType Container)) {
    Write-Host "ERROR: story directory not found: $BaseDir" -ForegroundColor Red
    exit 1
}

$SubmissionPath = Resolve-InputPath -PathValue $Submission -BaseDir $BaseDir
$SourcePath = if ($NoSource) { $null } else { Resolve-InputPath -PathValue $Source -BaseDir $BaseDir }

$submissionName = [System.IO.Path]::GetFileName($SubmissionPath)
if ($submissionName -ine 'story.txt') {
    Write-Host "ERROR: Submission must be named 'story.txt'. Got: $submissionName" -ForegroundColor Red
    exit 1
}
if (-not $NoSource) {
    $sourceName = [System.IO.Path]::GetFileName($SourcePath)
    if ($sourceName -ine 'source.txt') {
        Write-Host "ERROR: Source must be named 'source.txt'. Got: $sourceName" -ForegroundColor Red
        exit 1
    }
}

if (-not (Test-Path -LiteralPath $SubmissionPath -PathType Leaf)) {
    Write-Host "ERROR: submission file not found: $Submission" -ForegroundColor Red
    exit 1
}
if ((-not $NoSource) -and (-not (Test-Path -LiteralPath $SourcePath -PathType Leaf))) {
    Write-Host "ERROR: source file not found: $Source" -ForegroundColor Red
    exit 1
}

if ($UlMin -gt $UlMax) {
    Write-Host "ERROR: UlMin cannot exceed UlMax." -ForegroundColor Red
    exit 1
}
if ($MinPercent -gt $MaxPercent) {
    Write-Host "ERROR: MinPercent cannot exceed MaxPercent." -ForegroundColor Red
    exit 1
}
if ($Coverage -le 0.0 -or $Coverage -ge 1.0) {
    Write-Host "ERROR: Coverage must be between 0 and 1 (exclusive), e.g. 0.85." -ForegroundColor Red
    exit 1
}
if ($ILevelMax -le 0) {
    Write-Host "ERROR: ILevelMax must be greater than 0." -ForegroundColor Red
    exit 1
}
if ($WordsPerIllustration -le 0) {
    Write-Host "ERROR: WordsPerIllustration must be greater than 0." -ForegroundColor Red
    exit 1
}
if ($IllustrationTolerancePercent -lt 0) {
    Write-Host "ERROR: IllustrationTolerancePercent must be non-negative." -ForegroundColor Red
    exit 1
}

$scoreParams = @{
    Json = $true
    Paths = @($SubmissionPath)
    Coverage = $Coverage
}
if ($DomainLemmas) {
    $scoreParams.DomainLemmas = $DomainLemmas
    $scoreParams.DomainDefaultRank = $DomainDefaultRank
}

$ulJson = & $ScoreTool @scoreParams
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: UL scoring failed." -ForegroundColor Red
    exit $LASTEXITCODE
}

try {
    $ulParsed = $ulJson | ConvertFrom-Json
}
catch {
    Write-Host "ERROR: Could not parse UL scorer JSON output." -ForegroundColor Red
    exit 1
}

if ($ulParsed -is [array]) {
    if ($ulParsed.Count -lt 1) {
        Write-Host "ERROR: UL scorer returned no results." -ForegroundColor Red
        exit 1
    }
    $ul = $ulParsed[0]
}
else {
    $ul = $ulParsed
}

$submissionWords = Get-WordCount -Text (Get-CountableText -Path $SubmissionPath)

if ($NoSource) {
    $wc = [pscustomobject][ordered]@{
        submission_words = $submissionWords
        source_words = 0
        percent_of_source = $null
        min_percent = [double]$MinPercent
        max_percent = [double]$MaxPercent
        pass = $false
        no_source = $true
    }
}
else {
    $wordJson = & $PythonCmd @PythonPrefixArgs $WordTool --json --min-percent $MinPercent --max-percent $MaxPercent $SubmissionPath $SourcePath
    if ($LASTEXITCODE -ne 0) {
        Write-Host "ERROR: word-count ratio tool failed." -ForegroundColor Red
        exit $LASTEXITCODE
    }

    try {
        $wc = $wordJson | ConvertFrom-Json
    }
    catch {
        Write-Host "ERROR: Could not parse word-count tool JSON output." -ForegroundColor Red
        exit 1
    }

    $wc | Add-Member -NotePropertyName no_source -NotePropertyValue $false -Force
}

$ulExact = [double]$ul.ul_exact
$ulFloor = [int][Math]::Floor($ulExact)
$ulPass = ($ulFloor -ge $UlMin) -and ($ulFloor -le $UlMax)  # info-only, no longer gates

# i-score is the primary text gate; UL above is reported as info-only.
if ($null -eq $ul.i_score) {
    Write-Host "ERROR: scorer did not return an i_score (coverage not applied)." -ForegroundColor Red
    exit 1
}
$iLevel = [double]$ul.i_score.i_level
$iRank = [double]$ul.i_score.i_rank
$plus1Pct = [double]$ul.i_score.plus1_pct
$plus1Tokens = [int]$ul.i_score.plus1_tokens
$plus1Unique = [int]$ul.i_score.plus1_unique
$iPass = ($iLevel -le $ILevelMax)

$corePass = $iPass -and [bool]$wc.pass

$submissionText = Get-Content -LiteralPath $SubmissionPath -Raw -Encoding UTF8
$illustrationRegex = [regex]'(?im)^\s*%%META\s+illustration\s*:\s*[^%]+%%\s*$'
$actualIllustrations = ($illustrationRegex.Matches($submissionText)).Count

$requiredIllustrations = [int][Math]::Round(([double]$wc.submission_words / [double]$WordsPerIllustration), [System.MidpointRounding]::AwayFromZero)
if ($requiredIllustrations -lt 1) {
    $requiredIllustrations = 1
}

$toleranceByPercent = ([double]$requiredIllustrations) * ($IllustrationTolerancePercent / 100.0)
$illustrationTolerance = [double][Math]::Min(1.0, $toleranceByPercent)
$minAllowedIllustrations = [int][Math]::Ceiling(([double]$requiredIllustrations) - $illustrationTolerance)
$maxAllowedIllustrations = [int][Math]::Floor(([double]$requiredIllustrations) + $illustrationTolerance)
if ($minAllowedIllustrations -lt 1) {
    $minAllowedIllustrations = 1
}
if ($maxAllowedIllustrations -lt $minAllowedIllustrations) {
    $maxAllowedIllustrations = $minAllowedIllustrations
}

# Packaging rule: illustration density is enforced only after text-level gates pass.
$illustrationEvaluated = $corePass
$illustrationPass = if ($illustrationEvaluated) {
    ($actualIllustrations -ge $minAllowedIllustrations) -and ($actualIllustrations -le $maxAllowedIllustrations)
} else {
    $true
}

$overallPass = $corePass -and $illustrationPass

$result = [ordered]@{
    submission = $SubmissionPath
    source = $SourcePath
    overall_pass = $overallPass
    ul_check = [ordered]@{
        ul_exact = $ulExact
        ul_floor = $ulFloor
        min_ul = $UlMin
        max_ul = $UlMax
        pass = $ulPass
        avd = [double]$ul.avd
        p85_rank = [double]$ul.p85_rank
        p95_rank = [double]$ul.p95_rank
        tokens = [int]$ul.tokens
        in_freq_list = [int]$ul.in_freq_list
    }
    i_score_check = [ordered]@{
        i_level = $iLevel
        i_rank = $iRank
        coverage = $Coverage
        max_ilevel = $ILevelMax
        plus1_pct = $plus1Pct
        plus1_tokens = $plus1Tokens
        plus1_unique = $plus1Unique
        pass = $iPass
    }
    word_count_check = [ordered]@{
        submission_words = [int]$wc.submission_words
        source_words = [int]$wc.source_words
        percent_of_source = [double]$wc.percent_of_source
        min_percent = [double]$wc.min_percent
        max_percent = [double]$wc.max_percent
        no_source = [bool]$wc.no_source
        pass = [bool]$wc.pass
    }
    illustration_check = [ordered]@{
        words_per_illustration = [int]$WordsPerIllustration
        required_count = [int]$requiredIllustrations
        actual_count = [int]$actualIllustrations
        tolerance_percent = [double]$IllustrationTolerancePercent
        tolerance_count = [double]([Math]::Round($illustrationTolerance, 2))
        min_allowed = [int]$minAllowedIllustrations
        max_allowed = [int]$maxAllowedIllustrations
        evaluated = [bool]$illustrationEvaluated
        pass = [bool]$illustrationPass
        deferred_until_text_pass = [bool](-not $illustrationEvaluated)
    }
}

if ($Json) {
    $result | ConvertTo-Json -Depth 6
}
else {
    $status = if ($result.overall_pass) { 'PASS' } else { 'FAIL' }
    $iStatus = if ($result.i_score_check.pass) { 'PASS' } else { 'FAIL' }
    $wcStatus = if ($result.word_count_check.pass) { 'PASS' } else { 'FAIL' }
    if ($result.illustration_check.evaluated) {
        $illStatus = if ($result.illustration_check.pass) { 'PASS' } else { 'FAIL' }
    }
    else {
        $illStatus = 'SKIP'
    }

    Write-Host "Free-flow DRC"
    Write-Host "-------------"
    Write-Host ("Submission: {0}" -f $result.submission)
    if ($result.word_count_check.no_source) {
        Write-Host "Source:     [none provided]"
    }
    else {
        Write-Host ("Source:     {0}" -f $result.source)
    }
    Write-Host ""
    Write-Host ("i-score:    iLevel={0:N1} (limit <= {1:N1}, cov {2:N2}) [{3}]" -f $result.i_score_check.i_level, $result.i_score_check.max_ilevel, $result.i_score_check.coverage, $iStatus)
    Write-Host ("  +1 tail:  {0:N1}% of text is unpunished (tokens: {1}, unique: {2})" -f $result.i_score_check.plus1_pct, $result.i_score_check.plus1_tokens, $result.i_score_check.plus1_unique)
    Write-Host ("  vocab:    iRank={0:N0}  (UL_exact={1:N1} -> floor UL{2} info-only)" -f $result.i_score_check.i_rank, $result.ul_check.ul_exact, $result.ul_check.ul_floor)
    if ($result.word_count_check.no_source) {
        Write-Host ("Word gate:  {0} words; no source provided -> auto-fail length gate [{1}]" -f $result.word_count_check.submission_words, $wcStatus)
    }
    else {
        Write-Host ("Word gate:  {0}/{1} words = {2:N2}% (range {3:N1}% - {4:N1}%) [{5}]" -f $result.word_count_check.submission_words, $result.word_count_check.source_words, $result.word_count_check.percent_of_source, $result.word_count_check.min_percent, $result.word_count_check.max_percent, $wcStatus)
    }
    if ($result.illustration_check.evaluated) {
        Write-Host ("Illus gate: {0} found; need {1} (allowed {2}-{3}, target 1/{4} words, tol=min(1,{5:N0}%)) [{6}]" -f $result.illustration_check.actual_count, $result.illustration_check.required_count, $result.illustration_check.min_allowed, $result.illustration_check.max_allowed, $result.illustration_check.words_per_illustration, $result.illustration_check.tolerance_percent, $illStatus)
    }
    else {
        Write-Host ("Illus gate: {0} found; need {1} (allowed {2}-{3}, target 1/{4} words, tol=min(1,{5:N0}%)) [{6} - deferred until UL+Word pass]" -f $result.illustration_check.actual_count, $result.illustration_check.required_count, $result.illustration_check.min_allowed, $result.illustration_check.max_allowed, $result.illustration_check.words_per_illustration, $result.illustration_check.tolerance_percent, $illStatus)
    }
    Write-Host ""
    Write-Host ("Overall:    {0}" -f $status)
}

if ($overallPass) { exit 0 } else { exit 2 }
