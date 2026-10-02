# Management Engineering

> **Management Engineering @ Unipd — Bachelor's (L-9) and Master's (LM-31) in Vicenza: combining engineering, economics and management to design and run complex production, logistics and service systems.**

Notes, summaries and exercises from the **English-taught "Management Engineering" track of the Master's Degree (LM-31)** at the University of Padova. The notes are plain Markdown files, designed to be read with [Obsidian](https://obsidian.md).
**No coding skills needed**: this guide walks you through everything, step by step.

---

## 🎓 The program in brief

The **Master's Degree in Management Engineering** (Italian: *Ingegneria Gestionale*) is where engineering meets economics and business: graduates learn to "speak" both with engineers and managers, and to analyze, design and run complex production, logistics and service systems.

Key facts about the English-taught track:

| | Master's Degree — Management Engineering track |
|---|---|
| **Degree class** | LM-31 — Ingegneria Gestionale (Management Engineering) |
| **Duration** | 2 years |
| **Location** | Vicenza campus |
| **Language** | English |
| **Access** | Free access, with curricular requirements |

- **What you learn**: the program is multidisciplinary, built on three pillars — technical engineering, economics & management, and quantitative methods. You learn to model socio-technical systems, manage projects and drive innovation, backed by a robust toolkit of analytical and quantitative techniques.
- **The English track focus**: **digital transformation** — how digital technologies reshape business processes, operations and organizations.
- **How it ends**: an internship plus a thesis, where you show you can work autonomously on a real, often company-based, problem.
- **Careers**: production, logistics, purchasing, marketing, R&D, management control, finance, consulting, banking and insurance — in Italy or abroad. According to Almalaurea data, LM-31 graduates in Padova have one of the highest employment rates (~98.6%). The degree also opens the way to PhD programs.
- The same LM-31 degree also runs an Italian-taught track (focused on business processes and sustainability): **this repository covers the English track**.

Sources: [Unipd — LM-31 program page](https://www.ingegneria.unipd.it/offerta-didattica/corsi-di-laurea-magistrale?tipo=LM&ordinamento=2025&key=IN3084) · [Official course catalogue](https://didattica.unipd.it/off/2025/LM/IN/IN3084)

---

## 📁 What's in this repository

```
📁 management-engineering-unipd/
├── 00 - Index.md            ← always start here: it's the "map" of all the notes
├── 01 - ....md              ← one note per chapter/topic
├── 02 - ....md
├── ...
├── allegati/                ← images and figures referenced in the notes
└── README.md                ← this file
```

- Files ending in **`.md`** are simple text documents (Markdown): they read fine here on GitHub too, but with Obsidian they become interactive — math formulas, highlights, and clickable links between topics (`[[like this]]`).
- The **`00 - Index`** note links to every chapter: it's the recommended starting point.

## 🔍 Two ways to read the notes

| Method | For whom | Internet needed? | Easy updates? |
|---|---|---|---|
| **A — Download ZIP** (recommended) | Anyone, zero extra tools | Only to download | Re-download the ZIP |
| **B — Clone with Git** | Anyone with (or willing to learn) Git | Only to download | Yes, one command |

Either way, you'll want **Obsidian** to read the notes with formulas, images and links. Here's how to install it.

---

## 🛠️ Install Obsidian (one time only)

Obsidian is **free** (for personal and commercial use) and does **not** require creating an account: just install it and open it.

### On Windows

1. Open your browser and go to **[obsidian.md/download](https://obsidian.md/download)**.
2. In the **Windows** section, click the download button: an `.exe` file will download (usually to your *Downloads* folder).
3. **Double-click** the downloaded file (`Obsidian-x.x.x.exe`).
4. Click **Install** and wait a few seconds: Obsidian will open by itself when done.
5. The first time, pick your language and feel free to close the welcome window — the next steps show you how to open the notes.

> No account or password will be requested: if you ever see a "Sign in" button, you can safely ignore it.

### On macOS

1. Go to **[obsidian.md/download](https://obsidian.md/download)**.
2. In the **macOS** section, click **Universal** to download the `.dmg` file.
3. **Double-click** the downloaded `.dmg`: a small window opens with the Obsidian icon and the `Applications` folder.
4. **Drag** the Obsidian icon into `Applications`.
5. Close the little window and open Obsidian from the **Launchpad** (or the Applications folder). If macOS asks "do you want to open an app downloaded from the internet?", click **Open**.

### On Linux (optional)

- **Easiest**: run `flatpak install flathub md.obsidian.Obsidian` in a terminal, then launch it from your app menu.
- Alternative: download the **AppImage** from the same page, then run `chmod u+x Obsidian-*.AppImage` and `./Obsidian-*.AppImage`.

---

## 🅰️ Method A — Open the notes without Git (recommended for beginners)

With this method you simply download the notes as a ZIP archive and unzip it on your computer. No extra software required.

1. On this repository's GitHub page, click the green **`<> Code`** button (top right, above the file list).
2. In the menu that opens, click **Download ZIP**.
3. Your browser will download a file like `management-engineering-unipd-main.zip` (usually to your *Downloads* folder).
4. **Extract the archive**:
   - **Windows**: right-click the ZIP file → **Extract All…** → click **Extract** (the suggested destination is fine). You'll get a folder with the same name as the ZIP.
   - **macOS**: just double-click the ZIP file: it extracts itself into a folder with the same name.
5. Open **Obsidian** and click **Open folder as vault**.
   - If you don't see the startup window: menu `File` → `Open vault…` → **Open folder as vault** tab.
6. Select the **folder you just extracted** (the one containing `00 - Index.md` — not the ZIP file!) and confirm.
7. If Obsidian asks *"Do you trust the author of this vault?"*, click **Trust author and enable plugins**: it's a standard prompt that just enables the settings included in the folder.
8. Open the **`00 - Index`** note — happy studying ✨

> 💡 **Keep in mind**: notes downloaded this way are a *snapshot*: they won't update on their own. When new notes come out, repeat steps 1–4 and replace the folder (or switch to Method B).

## 🅱️ Method B — Clone the repository with Git

"Cloning" means downloading a *smart* copy of the notes that you can update with a single command whenever new notes are published.

### B.1 — Install Git (one time only)

- **Windows**: download the installer from **[git-scm.com/download/win](https://git-scm.com/download/win)**, open the downloaded `.exe` and keep clicking **Next** without changing anything — the default options are fine. You can untick "Launch Git Bash" at the end if you want.
- **macOS**: Git is already included. If the terminal asks to install "Command Line Developer Tools", confirm and wait.

### B.2 — Clone the repository

1. On this repository's GitHub page, click the green **`<> Code`** button and copy the HTTPS address (it looks like `https://github.com/your-username/management-engineering-unipd.git`).
2. Open a terminal:
   - **Windows**: press the ⊞ Start key, type **Git Bash** and open that app (a black window where you type).
   - **macOS**: press `Cmd + Space`, type **Terminal** and press Enter.
3. Type (or paste with `Ctrl+V` / `Cmd+V`) the following command, replacing the address with the one you copied in step 1:

   ```bash
   git clone <https://github.com/your-username/management-engineering-unipd.git>
   ```

4. Press **Enter**: a `management-engineering-unipd` folder will be created where you opened the terminal.
   - On Windows, Git Bash opens in your user folder (`C:\Users\YourName`); if you prefer another location, first type e.g. `cd Documents` and then run the clone again.

### B.3 — Open it in Obsidian

1. Open **Obsidian** → **Open folder as vault**.
2. Select the `management-engineering-unipd` folder created by the clone.
3. If asked, click **Trust author and enable plugins**.
4. Open **`00 - Index`** and study! 📖

### B.4 — Update the notes

When new notes come out, open Git Bash (or the Terminal) **inside** the repository folder and type:

```bash
git pull
```

If you're not inside the folder yet: `cd management-engineering-unipd` before `git pull`. Obsidian will refresh the notes automatically.

---

## ❓ Troubleshooting

| Problem | Solution |
|---|---|
| "The `.md` files open in Notepad and look weird" | Don't open the files one by one: install Obsidian and open the **whole folder** as a vault (steps 5–7 of Method A). |
| "I can't see images or formulas" | Did you extract the **complete** ZIP, including the `allegati/` folder? If you only copied some files, the images are missing: extract the whole folder again. |
| "Obsidian asks me to trust the author" | That's normal: click *Trust author and enable plugins*. |
| "Where do I find a topic?" | Press `Ctrl+O` (`Cmd+O` on Mac) to search a note by name, or `Ctrl+Shift+F` to search a word across all notes. |
| "How do I update the notes?" | Method A: re-download the ZIP. Method B: `git pull`. |
| "Can I read them on my phone?" | Yes: Obsidian is free on iOS/Android too (App Store / Play Store), but getting the same files on your phone requires a sync system (e.g. an iCloud/Drive folder) — not covered here. |
| "I improved the notes — can I share them?" | Sure: open a GitHub *Issue* or contact the author. Local changes stay on your computer until you upload them yourself. |

---

## 📜 License

<!-- Pick a license and replace this line, e.g. CC BY-NC-SA 4.0 -->
These notes are provided "as is" for personal study use. Before redistributing them, ask the author or add an explicit license (for university notes, [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) is a common choice).

*Notes written by a student of the program: they may contain mistakes — please report them, contributions are welcome!* ♪
