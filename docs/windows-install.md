# Windows 安装与升级

## 安装

1. 在 [Releases](../../releases) 下载 `Kyna-vX.Y.Z-windows-x64.zip` 和同一 release 的 `SHA256SUMS`。
2. 在 PowerShell 中校验下载文件：

   ```powershell
   Get-FileHash .\Kyna-vX.Y.Z-windows-x64.zip -Algorithm SHA256
   Get-Content .\SHA256SUMS
   ```

   两个 SHA-256 值必须一致。
3. 将 ZIP 解压到用户有写权限的目录，例如 `%LOCALAPPDATA%\Programs\Kyna`。不要直接在 ZIP 内运行。
4. 运行 `kyna_player.exe`。播放器、字幕 sidecar 和 Whisper worker 必须保留在同一个解压目录及其 `whisper\` 子目录中。

## 首次使用

安装包不包含 Whisper 模型或示例媒体。首次生成字幕前，请在应用内导入兼容的模型，或通过应用提供的下载流程取得模型。模型保存在用户数据目录，不会写入安装目录。

## 升级

1. 退出 Kyna。
2. 解压新版本到一个新目录，或替换旧安装目录中的全部文件。
3. 保留用户数据目录；已导入模型和应用设置不随 ZIP 删除。
4. 不要把不同版本的 `kyna_player.exe`、`kyna_subtitle.exe`、DLL 或 `whisper\whisper-cli.exe` 混用。

## 报错与反馈

提交 issue 时请附上 Kyna 版本、Windows 版本、复现步骤和已隐藏个人信息的日志。不要公开 API key、访问 token、私有媒体路径或安全漏洞。
