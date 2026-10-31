param([switch]$Check)

$ErrorActionPreference = "Stop"
$script:root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

$script:python = $null
$pythonCommand = Get-Command python -ErrorAction SilentlyContinue
if ($null -ne $pythonCommand) {
    $script:python = $pythonCommand.Source
} else {
    $pyCommand = Get-Command py -ErrorAction SilentlyContinue
    if ($null -ne $pyCommand) {
        $script:python = $pyCommand.Source
    }
}

if ($Check) {
    Write-Output "HubLauncher check"
    Write-Output "root: $script:root"
    if ($null -eq $script:python) {
        Write-Output "python: NOT FOUND"
    } else {
        Write-Output "python: $script:python"
    }
    exit 0
}

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
[System.Windows.Forms.Application]::EnableVisualStyles()

function Open-HubFile {
    param([string]$Path)
    if (Test-Path -LiteralPath $Path) {
        Start-Process -FilePath "notepad.exe" -ArgumentList "`"$Path`"" | Out-Null
    } else {
        [System.Windows.Forms.MessageBox]::Show("找不到：$Path", "Hub") | Out-Null
    }
}

function Start-HubTool {
    param([string]$Arguments)
    if ($null -eq $script:python) {
        [System.Windows.Forms.MessageBox]::Show("找不到 python，请先安装 Python 并加入 PATH。", "Hub") | Out-Null
        return
    }
    $command = "Set-Location -LiteralPath '$script:root'; & '$script:python' $Arguments"
    Start-Process -FilePath "powershell.exe" -ArgumentList @(
        "-NoProfile", "-NoLogo", "-ExecutionPolicy", "Bypass", "-NoExit", "-Command", $command
    ) | Out-Null
}

function Invoke-HubAction {
    param([string]$Tag)
    switch ($Tag) {
        "github" {
            Start-Process "https://github.com/Appler-D/embedded-transfer-hub" | Out-Null
        }
        "readme" {
            Open-HubFile (Join-Path $script:root "README.md")
        }
        "timer" {
            Start-HubTool "tools/interview_timer.py"
        }
        "questions" {
            Start-HubTool "tools/mock_questions.py --count 5"
        }
        "score" {
            Start-HubTool "tools/score_interview.py"
        }
        "script" {
            Open-HubFile (Join-Path $script:root "docs/13-zafu-3min-script.md")
        }
        "folder" {
            Start-Process explorer.exe -ArgumentList $script:root | Out-Null
        }
        "exit" {
            $script:form.Close()
        }
    }
}

$script:form = New-Object System.Windows.Forms.Form
$script:form.Text = "Embedded Transfer Hub"
$script:form.Size = New-Object System.Drawing.Size(460, 470)
$script:form.StartPosition = "CenterScreen"
$script:form.FormBorderStyle = "FixedSingle"
$script:form.MaximizeBox = $false

$title = New-Object System.Windows.Forms.Label
$title.Text = "转专业 / 嵌入式学习 Hub"
$title.Font = New-Object System.Drawing.Font("Microsoft YaHei UI", 14, [System.Drawing.FontStyle]::Bold)
$title.Location = New-Object System.Drawing.Point(24, 18)
$title.Size = New-Object System.Drawing.Size(400, 34)
$script:form.Controls.Add($title)

$subtitle = New-Object System.Windows.Forms.Label
$subtitle.Text = "抽题 → 计时 → 打分 → 复盘"
$subtitle.Location = New-Object System.Drawing.Point(26, 54)
$subtitle.Size = New-Object System.Drawing.Size(400, 22)
$script:form.Controls.Add($subtitle)

$actions = @(
    @{ Tag = "github";    Text = "打开 GitHub 仓库" },
    @{ Tag = "readme";    Text = "打开本地 README" },
    @{ Tag = "timer";     Text = "3 分钟自述计时器" },
    @{ Tag = "questions"; Text = "随机抽 5 道面试题" },
    @{ Tag = "score";     Text = "面试七维打分" },
    @{ Tag = "script";    Text = "打开 3 分钟稿" },
    @{ Tag = "folder";    Text = "打开本地仓库文件夹" },
    @{ Tag = "exit";      Text = "退出" }
)

$y = 88
foreach ($action in $actions) {
    $button = New-Object System.Windows.Forms.Button
    $button.Text = $action.Text
    $button.Tag = $action.Tag
    $button.Location = New-Object System.Drawing.Point(24, $y)
    $button.Size = New-Object System.Drawing.Size(400, 34)
    $button.Add_Click({ Invoke-HubAction -Tag $this.Tag })
    $script:form.Controls.Add($button)
    $y += 42
}

$footer = New-Object System.Windows.Forms.Label
$footer.Text = "需要 Python 3.11+；计时/抽题/打分工具只用标准库"
$footer.Location = New-Object System.Drawing.Point(24, $y + 4)
$footer.Size = New-Object System.Drawing.Size(400, 40)
$footer.ForeColor = [System.Drawing.Color]::DimGray
$script:form.Controls.Add($footer)

[void]$script:form.ShowDialog()
