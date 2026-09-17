# Install and update Kyna on Windows

## Install

1. Download `Kyna-vX.Y.Z-windows-x64.exe` and the matching `SHA256SUMS` file from [Releases](../../releases).
2. Verify the download in PowerShell:

   ```powershell
   Get-FileHash .\Kyna-vX.Y.Z-windows-x64.exe -Algorithm SHA256
   Get-Content .\SHA256SUMS
   ```

   The SHA-256 values must match.
3. Run the installer. You can change the installation directory in the setup wizard.
4. Start Kyna from the Start menu or by running `kyna_player.exe` in the installation directory.

Keep the player, subtitle service, Whisper worker, and providers in their installed locations. Do not mix files from different Kyna versions.

## First use

The installer does not include Whisper models or sample media. Before creating subtitles, import a compatible model in the app or use the app's model-download flow. Models are stored in your user data directory, not the installation directory.

## Update and uninstall

1. Exit Kyna.
2. Run the newer installer and keep the same installation directory to update the app.
3. Your imported models and app settings remain in your user data directory.
4. To uninstall Kyna, use Windows Installed Apps or the Start menu uninstall entry.

## Getting help

When reporting an issue, include your Kyna version, Windows version, reproduction steps, and redacted logs. Never post API keys, access tokens, private media paths, or security vulnerabilities publicly.
