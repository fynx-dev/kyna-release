# Install and update Kyna Player on Windows

## Install

1. Download `Kyna-Player-vX.Y.Z-windows-x64.exe` and the matching `SHA256SUMS` file from [Releases](https://github.com/fynx-dev/kyna-release/releases/latest).
2. Verify the download in PowerShell:

   ```powershell
   Get-FileHash .\Kyna-Player-vX.Y.Z-windows-x64.exe -Algorithm SHA256
   Get-Content .\SHA256SUMS
   ```

   The SHA-256 values must match.
3. Run the installer. You can change the installation directory in the setup wizard.
4. Start Kyna Player from the Start menu or by running `kyna_launcher.exe` in the installation directory.

Keep the player, subtitle service, Whisper worker, and providers in their installed locations. Do not mix files from different Kyna Player versions.

## First use

The installer does not include Whisper models or sample media. Before creating subtitles, import a compatible model in the app or use the app's model-download flow. Models are stored in your user data directory, not the installation directory.

## Update and uninstall

1. Exit Kyna Player.
2. Run the newer installer and keep the same installation directory to update the app.
3. Your imported models and app settings remain in your user data directory.
4. To uninstall Kyna Player, use Windows Installed Apps or the Start menu uninstall entry.

## Troubleshoot startup crashes

1. Note the time and any error message or code. If a required component is missing, reinstall Kyna Player using the official installer. The required MSVC runtime is included; do not download individual DLLs from third-party sites.
2. In File Explorer, open `%LOCALAPPDATA%\Kyna\logs`. Check `kyna-launcher.log` and the newest `kyna-player-*.log` from around the crash. For a portable installation, also check `data\logs` beside the executable.
3. If a crash dialog offers **Save a dump file for error diagnosis**, select it only if you want to create a local dump. Explorer will show the saved file. Dumps may contain private memory data, are never uploaded automatically, and should not be posted in public issues. Some early failures cannot produce a dump.
4. If the cause is unclear, press **Win+R**, enter `eventvwr.msc`, then open **Windows Logs → Application**. Find the error at the crash time and note its **Faulting module name** and **Exception code**.

When [reporting a bug](https://github.com/fynx-dev/kyna-release/issues/new?template=bug.yml), include the Kyna Player and Windows versions, reproduction steps, crash time, error code, and relevant logs. Inspect logs before sharing: general logs may still contain private paths or URLs despite best-effort redaction. Share dumps only through a private channel after reviewing their privacy implications. Never post API keys, access tokens, private media paths, or security vulnerabilities publicly.
