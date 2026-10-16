#!/usr/bin/env python3
"""
Crea l'eseguibile di Voice Recorder con PyInstaller.

  Windows ->  dist/VoiceRecorder.exe          (file singolo)
  macOS   ->  dist/VoiceRecorder.app (+ .zip) (app bundle)

ATTENZIONE: PyInstaller NON fa cross-compilazione. Per avere l'.exe devi lanciare
questo script su Windows, per l'.app devi lanciarlo su un Mac.

Uso:
    py build_exe.py              # Windows
    python3 build_exe.py         # Mac

Opzioni:
    --onedir     su Windows crea una cartella invece di un singolo .exe
                 (parte più velocemente e dà meno falsi positivi dall'antivirus)
    --name NOME  cambia il nome dell'app (default: VoiceRecorder)

Icona (facoltativa): metti "icon.ico" (Windows) o "icon.icns" (Mac) accanto a questo file.
"""

import argparse
import importlib.util
import plistlib
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENTRY = HERE / "main.py"
BUNDLE_ID = "com.matteo.voicerecorder"
MIC_TEXT = "Voice Recorder ha bisogno del microfono per registrare l'audio."

IS_WIN = sys.platform == "win32"
IS_MAC = sys.platform == "darwin"


def has_module(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def pip_install(*packages: str):
    print(f"-> Installo: {', '.join(packages)}")
    subprocess.check_call([sys.executable, "-m", "pip", "install", *packages])


def ensure_dependencies():
    needed = []
    if not has_module("PyInstaller"):
        needed.append("pyinstaller")
    if not has_module("sounddevice"):
        needed.append("sounddevice")
    if not has_module("imageio_ffmpeg"):
        needed.append("imageio-ffmpeg")
    if not has_module("numpy"):
        needed.append("numpy")
    if needed:
        pip_install(*needed)
    try:
        import tkinter  # noqa: F401
    except ImportError:
        sys.exit(
            "tkinter non è disponibile in questo Python.\n"
            "Su Mac con Homebrew: brew install python-tk\n"
            "Oppure usa il Python di python.org, che lo include."
        )


def build(name: str, onedir: bool):
    if not ENTRY.exists():
        sys.exit(f"Non trovo {ENTRY.name} accanto a questo script.")

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--noconfirm", "--clean", "--windowed",
        "--name", name,
        "--distpath", str(HERE / "dist"),
        "--workpath", str(HERE / "build"),
        "--specpath", str(HERE / "build"),
        # ffmpeg incluso in imageio-ffmpeg e libreria PortAudio di sounddevice
        "--collect-all", "imageio_ffmpeg",
        "--collect-all", "sounddevice",
    ]
    if has_module("_sounddevice_data"):
        cmd += ["--collect-all", "_sounddevice_data"]

    if IS_WIN and not onedir:
        cmd.append("--onefile")
    if IS_MAC:
        cmd += ["--osx-bundle-identifier", BUNDLE_ID]

    icon = HERE / ("icon.ico" if IS_WIN else "icon.icns")
    if icon.exists() and (IS_WIN or IS_MAC):
        cmd += ["--icon", str(icon)]

    cmd.append(str(ENTRY))
    print("-> Eseguo PyInstaller...\n")
    subprocess.check_call(cmd, cwd=HERE)


def postprocess_mac(name: str):
    """Aggiunge il permesso microfono all'Info.plist, firma l'app e crea lo zip."""
    app = HERE / "dist" / f"{name}.app"
    plist_path = app / "Contents" / "Info.plist"
    with open(plist_path, "rb") as f:
        info = plistlib.load(f)
    info["NSMicrophoneUsageDescription"] = MIC_TEXT
    info["NSHighResolutionCapable"] = True
    with open(plist_path, "wb") as f:
        plistlib.dump(info, f)

    # Firma "ad-hoc" (necessaria su Apple Silicon e dopo aver modificato il plist)
    print("-> Firmo l'app (ad-hoc)...")
    subprocess.run(["codesign", "--force", "--deep", "--sign", "-", str(app)], check=False)

    zip_path = HERE / "dist" / f"{name}-mac.zip"
    if zip_path.exists():
        zip_path.unlink()
    subprocess.check_call(
        ["ditto", "-c", "-k", "--sequesterRsrc", "--keepParent", str(app), str(zip_path)]
    )
    return app, zip_path


def main():
    ap = argparse.ArgumentParser(description="Crea l'eseguibile di Voice Recorder")
    ap.add_argument("--onedir", action="store_true",
                    help="Windows: crea una cartella invece di un solo .exe")
    ap.add_argument("--name", default="VoiceRecorder", help="nome dell'app")
    args = ap.parse_args()

    if not (IS_WIN or IS_MAC):
        print("Nota: stai usando Linux, verrà creato un eseguibile Linux (non .exe né .app).\n")

    ensure_dependencies()
    build(args.name, args.onedir)

    dist = HERE / "dist"
    print("\n==================== FATTO ====================")
    if IS_MAC:
        app, zip_path = postprocess_mac(args.name)
        print(f"App:  {app}")
        print(f"Zip:  {zip_path}   (da condividere)")
        print("\nSu un altro Mac, al primo avvio: tasto destro sull'app -> Apri.")
    elif IS_WIN:
        target = dist / (args.name if args.onedir else f"{args.name}.exe")
        print(f"Eseguibile: {target}")
    else:
        print(f"Eseguibile: {dist / args.name}")

    # pulizia della cartella temporanea di build
    shutil.rmtree(HERE / "build", ignore_errors=True)


if __name__ == "__main__":
    main()