---
title: "Installation & Requirements"
description: "System requirements, installation, updates, and app data directory management."
order: 2
group: "Getting Started"
---

# 📦 Installation & System Requirements

## 💻 System Requirements

| Specification | Minimum | Recommended |
| :--- | :--- | :--- |
| **Operating System** | Windows 10 (64-bit) 1909+ | Windows 11 (22H2+) |
| **Processor (CPU)** | Intel Core i3 / AMD Ryzen 3 | Intel Core i5 / AMD Ryzen 5 or higher |
| **Graphics (GPU)** | Direct3D 11 hardware decoding | DX12 / HEVC / AV1 / VP9 hardware acceleration |
| **Memory (RAM)** | 4 GB | 8 GB or higher |

---

## 🚀 Installation & Updating

1. **Download Installer**
   Visit [GitHub Releases](https://github.com/fynx-dev/kyna-release/releases/latest) to download `Kyna-Player-vX.Y.Z-windows-x64.exe`.
2. **Run Setup Wizard**
   Launch the setup program and follow the on-screen steps to install.
3. **Upgrading**
   Close the player and run the latest installer directly to overwrite. Your custom settings and downloaded AI models will be preserved.

---

## 🗄️ App Data & Logs

Installed builds store user data under `%LOCALAPPDATA%\Kyna\`. A portable build with a `data` folder beside the executable uses that folder instead. Logs are in `logs\`; crash dumps, if you choose to save one, are in `dumps\`.

---

## 🛠️ Troubleshoot Startup Crashes

1. **Record the error.** Note when the crash happened and any message or code. If a required component is missing, reinstall from the [official release](https://github.com/fynx-dev/kyna-release/releases/latest). The installer includes the required MSVC runtime; do not download individual DLLs from third-party sites.
2. **Find the logs.** Open `%LOCALAPPDATA%\Kyna\logs` in File Explorer. Check `kyna-launcher.log` and the newest `kyna-player-*.log`. For portable builds, also check `data\logs` beside the executable.
3. **Save a dump only if you choose to.** If the crash dialog offers a dump option, select it to save a local file and reveal it in File Explorer. Dumps can contain private memory data and are never uploaded automatically. Some early failures cannot produce a dump; never attach one to a public issue.
4. **Check Windows events.** Press **Win+R**, run `eventvwr.msc`, then open **Windows Logs → Application**. Find the error at the crash time and note the **Faulting module name** and **Exception code**.

When [reporting a bug](https://github.com/fynx-dev/kyna-release/issues/new?template=bug.yml), include the player and Windows versions, reproduction steps, crash time, any error code, and relevant logs. Inspect logs before sharing: general logs can still contain private paths or URLs. Share dumps only through a private channel after reviewing their contents.
