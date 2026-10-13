#!/usr/bin/env python3
"""
Registra dal microfono e salva in .mp4 (audio AAC) dentro la cartella
"registrazioni" nel folder del progetto.

Dipendenze:
    pip install sounddevice imageio-ffmpeg

(imageio-ffmpeg include già un binario di ffmpeg, non serve installarlo a parte.)

Uso:
    python registra_mic.py                  # registra finché premi INVIO
    python registra_mic.py -d 30            # registra 30 secondi
    python registra_mic.py --list-devices   # mostra i dispositivi audio
    python registra_mic.py --device 2       # usa il dispositivo con indice 2
"""

import argparse
import queue
import subprocess
import sys
import threading
import time
from datetime import datetime
from pathlib import Path

import imageio_ffmpeg
import sounddevice as sd

PROJECT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_DIR / "registrazioni"


def parse_args():
    p = argparse.ArgumentParser(description="Registratore da microfono -> .mp4")
    p.add_argument("-d", "--duration", type=float, default=None,
                   help="durata in secondi (se omesso, ferma con INVIO)")
    p.add_argument("--device", type=int, default=None,
                   help="indice del dispositivo di input (vedi --list-devices)")
    p.add_argument("--rate", type=int, default=44100, help="sample rate (default 44100)")
    p.add_argument("--channels", type=int, default=1, help="canali (default 1 = mono)")
    p.add_argument("--bitrate", default="192k", help="bitrate AAC (default 192k)")
    p.add_argument("--name", default=None,
                   help="nome file senza estensione (default: registrazione_DATA_ORA)")
    p.add_argument("--list-devices", action="store_true",
                   help="elenca i dispositivi audio e esce")
    return p.parse_args()


def main():
    args = parse_args()

    if args.list_devices:
        print(sd.query_devices())
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    name = args.name or f"registrazione_{datetime.now():%Y%m%d_%H%M%S}"
    out_path = OUTPUT_DIR / f"{name}.mp4"

    # ffmpeg riceve PCM 16 bit da stdin e lo codifica in AAC dentro un container mp4
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [
        ffmpeg, "-y", "-loglevel", "error",
        "-f", "s16le", "-ar", str(args.rate), "-ac", str(args.channels),
        "-i", "pipe:0",
        "-c:a", "aac", "-b:a", args.bitrate,
        str(out_path),
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    q: "queue.Queue[bytes]" = queue.Queue()
    stop = threading.Event()

    def callback(indata, frames, time_info, status):
        if status:
            print(status, file=sys.stderr)
        q.put(bytes(indata))

    # Thread che aspetta INVIO per fermare la registrazione
    if args.duration is None:
        threading.Thread(
            target=lambda: (input(), stop.set()), daemon=True
        ).start()
        print("Registrazione in corso... premi INVIO per fermare (o Ctrl+C).")
    else:
        print(f"Registrazione di {args.duration:.0f} secondi...")

    start = time.time()
    try:
        with sd.RawInputStream(
            samplerate=args.rate,
            channels=args.channels,
            dtype="int16",
            device=args.device,
            callback=callback,
        ):
            while not stop.is_set():
                if args.duration is not None and time.time() - start >= args.duration:
                    break
                try:
                    proc.stdin.write(q.get(timeout=0.1))
                except queue.Empty:
                    pass
    except KeyboardInterrupt:
        print("\nInterrotto.")
    except sd.PortAudioError as e:
        print(f"Errore audio: {e}", file=sys.stderr)
        proc.stdin.close()
        proc.wait()
        sys.exit(1)

    # Svuota i dati rimasti in coda e chiude il file
    while not q.empty():
        proc.stdin.write(q.get())
    proc.stdin.close()
    proc.wait()

    print(f"Salvato: {out_path}")


if __name__ == "__main__":
    main()