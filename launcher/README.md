# Desktop launcher

Windows PowerShell 启动器：一个桌面图标，打开 Hub 菜单。

## 安装快捷方式

在仓库根目录运行：

```powershell
powershell -ExecutionPolicy Bypass -File launcher/install-shortcut.ps1
```

会在桌面创建 `Hub.lnk`，指向 `launcher/HubLauncher.ps1`。

## 直接运行

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File launcher/HubLauncher.ps1
```

检查脚本/路径/Python：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File launcher/HubLauncher.ps1 -Check
```

## 菜单

- 打开 GitHub 仓库
- 打开本地 README
- 3 分钟自述计时器
- 随机抽 5 道面试题
- 面试七维打分
- 打开 3 分钟稿
- 打开本地仓库文件夹
- 退出

## 依赖

- Windows PowerShell 5.1+（系统自带）。
- Python 3.11+ 在 PATH 中；三个工具只用标准库。

## 说明

- 快捷方式只在本机，不提交到仓库；换电脑/移动仓库后重新跑安装脚本。
- 交互式工具会打开一个新的 PowerShell 窗口；关掉窗口即结束。
- 如果 PowerShell 执行策略阻止脚本，使用上面的 `-ExecutionPolicy Bypass` 参数（只对本次运行生效）。
