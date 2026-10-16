#!/usr/bin/env python3
"""
Voice Recorder - registratore da microfono con interfaccia grafica stile player.

- Registra dal microfono e salva SEMPRE in .mp3
- Nome file: <nome>_<AAAA-MM-GG>_<HH-MM-SS>.mp3   (gli spazi nel nome diventano "-")
- File salvati nella cartella "registrazioni" dentro il folder del progetto
- Equalizzatore a 5 bande + volume ingresso + auto-livello per voci lontane/basse
- Lista delle registrazioni con riproduzione, apertura cartella ed eliminazione

Dipendenze:
    py -m pip install sounddevice imageio-ffmpeg numpy
(tkinter è già incluso in Python su Windows; imageio-ffmpeg include ffmpeg)
"""

import json
import os
import queue
import re
import subprocess
import sys
import threading
import tkinter as tk
from datetime import datetime
from pathlib import Path
from tkinter import messagebox, ttk

import imageio_ffmpeg
import numpy as np
import sounddevice as sd


def get_base_dir() -> Path:
    """Cartella base: il folder del progetto (da sorgente) oppure, se il programma
    è un eseguibile, accanto all'.exe su Windows e in ~/Documents/VoiceRecorder su Mac."""
    if getattr(sys, "frozen", False):
        if sys.platform == "darwin":
            return Path.home() / "Documents" / "VoiceRecorder"
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


PROJECT_DIR = get_base_dir()
OUTPUT_DIR = PROJECT_DIR / "registrazioni"
SETTINGS_FILE = PROJECT_DIR / "impostazioni.json"
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0) if sys.platform == "win32" else 0

# ----------------------------------------------------------------- colori ---
BG = "#121212"
PANEL = "#1c1c1e"
PANEL2 = "#2a2a2d"
FG = "#f2f2f2"
MUTED = "#8e8e93"
RED = "#e5383b"
ACCENT = "#1db954"
YELLOW = "#f4c430"

FONT = ("Segoe UI", 10)
FONT_BOLD = ("Segoe UI", 10, "bold")
FONT_TITLE = ("Segoe UI", 16, "bold")
FONT_TIMER = ("Consolas", 44, "bold")

# ------------------------------------------------------------ equalizzatore ---
BANDS = [(100, "100 Hz"), (400, "400 Hz"), (1000, "1 kHz"), (3000, "3 kHz"), (8000, "8 kHz")]
TAPS = 1025  # lunghezza del filtro FIR dell'equalizzatore

PRESETS = {
    "Piatto": dict(gain=0, bands=[0, 0, 0, 0, 0], agc=False),
    "Voce (lezione)": dict(gain=6, bands=[-6, -2, 0, 3, 1], agc=False),
    "Prof lontano": dict(gain=12, bands=[-9, -3, 2, 6, 3], agc=True),
    "Prof molto lontano": dict(gain=18, bands=[-12, -4, 3, 8, 4], agc=True),
}
DEFAULT_PRESET = "Prof lontano"


# ---------------------------------------------------------------- utility ---
def fmt_time(seconds: float) -> str:
    s = int(seconds)
    return f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}"


def sanitize_name(name: str) -> str:
    """Spazi -> '-', rimuove caratteri non validi per i nomi file."""
    name = name.strip()
    name = re.sub(r"\s+", "-", name)
    name = re.sub(r'[\\/:*?"<>|]', "", name)
    name = name.strip("-.")
    return name or "registrazione"


def build_filename(name: str, when: datetime) -> str:
    return f"{sanitize_name(name)}_{when:%Y-%m-%d}_{when:%H-%M-%S}.mp3"


def unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    i = 2
    while True:
        candidate = path.with_name(f"{path.stem}_{i}{path.suffix}")
        if not candidate.exists():
            return candidate
        i += 1


FILE_RE = re.compile(r"^(?P<name>.+)_(?P<d>\d{4}-\d{2}-\d{2})_(?P<t>\d{2}-\d{2}-\d{2})(_\d+)?$")


def describe_file(path: Path):
    """Ritorna (nome, data 'gg/mm/aaaa', ora 'hh:mm:ss') per la lista."""
    m = FILE_RE.match(path.stem)
    if m:
        y, mo, d = m["d"].split("-")
        return m["name"], f"{d}/{mo}/{y}", m["t"].replace("-", ":")
    ts = datetime.fromtimestamp(path.stat().st_mtime)
    return path.stem, f"{ts:%d/%m/%Y}", f"{ts:%H:%M:%S}"


def load_settings() -> dict:
    try:
        return json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_settings(data: dict):
    try:
        PROJECT_DIR.mkdir(parents=True, exist_ok=True)
        SETTINGS_FILE.write_text(json.dumps(data), encoding="utf-8")
    except OSError:
        pass


# ---------------------------------------------------------- elaborazione audio ---
class AudioProcessor:
    """Elaborazione in tempo reale (mono): equalizzatore a 5 bande, volume,
    auto-livello (AGC) e limiter morbido per evitare distorsione."""

    AGC_TARGET = 0.08    # livello RMS a cui punta l'auto-livello (circa -22 dBFS)
    AGC_MAX_GAIN = 12.0  # guadagno massimo dell'auto-livello (circa +21 dB)
    AGC_MIN_GAIN = 0.2
    AGC_GATE = 0.002     # sotto questo livello (silenzio/rumore) non alza il volume

    def __init__(self):
        self.rate = 44100
        self.gain_db = 0.0
        self.band_gains = [0.0] * len(BANDS)
        self.agc = False
        self.fir = None
        self.history = np.zeros(TAPS - 1, dtype=np.float32)
        self.agc_gain = 1.0
        self.prev_gain = 1.0

    # --- impostazioni (chiamate dalla GUI, anche durante la registrazione)
    def configure(self, rate: int):
        self.rate = rate
        self.history = np.zeros(TAPS - 1, dtype=np.float32)
        self.agc_gain = self.prev_gain = 1.0
        self._design()

    def set_gain(self, db: float):
        self.gain_db = float(db)

    def set_bands(self, gains):
        self.band_gains = [float(g) for g in gains]
        self._design()

    def set_agc(self, on: bool):
        on = bool(on)
        if on and not self.agc:
            self.agc_gain = 1.0
        self.agc = on

    def _design(self):
        """Progetta un filtro FIR a fase lineare dalle curve dei 5 slider."""
        if all(abs(g) < 0.05 for g in self.band_gains):
            self.fir = None
            return
        n = 2048
        freqs = np.fft.rfftfreq(n, 1.0 / self.rate)
        centers = np.log10([f for f, _ in BANDS])
        db = np.interp(np.log10(np.maximum(freqs, 1.0)), centers, self.band_gains)
        mag = 10.0 ** (db / 20.0)
        imp = np.fft.irfft(mag, n)
        imp = np.roll(imp, TAPS // 2)[:TAPS] * np.hanning(TAPS)
        self.fir = imp.astype(np.float32)

    # --- elaborazione di un blocco
    def process(self, data: bytes):
        """Riceve PCM int16 mono, ritorna (PCM int16 elaborato, picco 0..1)."""
        x = np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32768.0
        if x.size == 0:
            return data, 0.0

        # 1) equalizzatore
        buf = np.concatenate((self.history, x))
        self.history = buf[-(TAPS - 1):]
        fir = self.fir
        if fir is not None:
            x = np.convolve(buf, fir, mode="valid").astype(np.float32)

        # 2) volume ingresso
        g = 10.0 ** (self.gain_db / 20.0)
        if g != 1.0:
            x = x * np.float32(g)

        # 3) auto-livello: alza le voci basse, abbassa i picchi troppo forti
        if self.agc:
            rms = float(np.sqrt(np.mean(x * x))) + 1e-9
            if rms > self.AGC_GATE:
                desired = min(max(self.AGC_TARGET / rms, self.AGC_MIN_GAIN), self.AGC_MAX_GAIN)
                coef = 0.5 if desired < self.agc_gain else 0.05  # attacco veloce, rilascio lento
                self.agc_gain += (desired - self.agc_gain) * coef
        target = self.agc_gain if self.agc else 1.0
        if target != 1.0 or self.prev_gain != 1.0:
            ramp = np.linspace(self.prev_gain, target, x.size, endpoint=False, dtype=np.float32)
            x = x * ramp
        self.prev_gain = target

        # 4) limiter morbido (evita la distorsione sui picchi)
        a = np.abs(x)
        over = a > 0.85
        if over.any():
            x = np.where(over, np.sign(x) * (0.85 + 0.15 * np.tanh((a - 0.85) / 0.15)), x)

        peak = min(float(np.max(np.abs(x))), 1.0)
        out = (np.clip(x, -1.0, 1.0) * 32767.0).astype(np.int16).tobytes()
        return out, peak


# -------------------------------------------------------------- registrazione ---
class Recorder:
    """Cattura dal microfono, elabora l'audio e codifica in mp3 al volo con ffmpeg."""

    def __init__(self):
        self.proc = None
        self.stream = None
        self.writer = None
        self.q = queue.Queue()
        self.dsp = AudioProcessor()
        self.recording = False
        self.paused = False
        self.frames = 0
        self.rate = 44100
        self.level = 0.0
        self.error = None

    def start(self, path: Path, device, rate: int, bitrate: str = "192k"):
        channels = 1
        cmd = [
            FFMPEG, "-y", "-loglevel", "error",
            "-f", "s16le", "-ar", str(rate), "-ac", str(channels), "-i", "pipe:0",
            "-c:a", "libmp3lame", "-b:a", bitrate,
            str(path),
        ]
        self.proc = subprocess.Popen(
            cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=NO_WINDOW
        )
        self.rate = rate
        self.dsp.configure(rate)
        self.frames = 0
        self.level = 0.0
        self.error = None
        self.paused = False
        self.q = queue.Queue()
        self.recording = True
        self.writer = threading.Thread(target=self._write_loop, daemon=True)
        self.writer.start()
        try:
            self.stream = sd.RawInputStream(
                samplerate=rate, channels=channels, dtype="int16",
                blocksize=1024, device=device, callback=self._callback,
            )
            self.stream.start()
        except Exception:
            self.recording = False
            self.q.put(None)
            self.writer.join()
            self._close_proc()
            raise

    def _callback(self, indata, frames, time_info, status):
        if self.paused:
            self.level = 0.0
            return
        raw = bytes(indata)
        try:
            out, peak = self.dsp.process(raw)
        except Exception:  # in caso di problemi registra comunque l'audio originale
            out, peak = raw, 0.0
        self.level = peak
        self.frames += frames
        self.q.put(out)

    def _write_loop(self):
        while True:
            chunk = self.q.get()
            if chunk is None:
                break
            try:
                self.proc.stdin.write(chunk)
            except (BrokenPipeError, OSError):
                self.error = "ffmpeg ha interrotto la scrittura del file."
                break

    def _close_proc(self):
        try:
            self.proc.stdin.close()
        except OSError:
            pass
        err = self.proc.stderr.read().decode(errors="replace").strip()
        self.proc.wait()
        if self.proc.returncode != 0 and not self.error:
            self.error = err or "Errore durante la codifica mp3."

    def stop(self):
        if not self.recording:
            return
        self.recording = False
        self.level = 0.0
        try:
            self.stream.stop()
            self.stream.close()
        except Exception:
            pass
        self.q.put(None)
        self.writer.join()
        self._close_proc()


# --------------------------------------------------------------- riproduzione ---
class Player:
    """Riproduce un mp3 decodificandolo con ffmpeg in streaming."""

    RATE, CH = 44100, 2

    def __init__(self):
        self.thread = None
        self.stop_flag = threading.Event()
        self.playing = False
        self.seconds = 0.0
        self.error = None

    def play(self, path: Path):
        self.stop()
        self.stop_flag.clear()
        self.seconds = 0.0
        self.error = None
        self.playing = True
        self.thread = threading.Thread(target=self._run, args=(path,), daemon=True)
        self.thread.start()

    def _run(self, path: Path):
        proc = None
        try:
            proc = subprocess.Popen(
                [FFMPEG, "-loglevel", "error", "-i", str(path),
                 "-f", "s16le", "-ar", str(self.RATE), "-ac", str(self.CH), "pipe:1"],
                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, creationflags=NO_WINDOW,
            )
            bytes_per_sec = self.RATE * self.CH * 2
            with sd.RawOutputStream(samplerate=self.RATE, channels=self.CH, dtype="int16") as out:
                while not self.stop_flag.is_set():
                    data = proc.stdout.read(bytes_per_sec // 10)
                    if not data:
                        break
                    out.write(data)
                    self.seconds += len(data) / bytes_per_sec
        except Exception as e:
            self.error = str(e)
        finally:
            if proc is not None:
                try:
                    proc.kill()
                    proc.stdout.close()
                    proc.wait()
                except Exception:
                    pass
            self.playing = False

    def stop(self):
        self.stop_flag.set()
        if self.thread is not None and self.thread.is_alive():
            self.thread.join(timeout=2)
        self.playing = False


# ------------------------------------------------------------------------ GUI ---
def make_button(parent, text, command, bg=PANEL2, fg=FG, **kw):
    return tk.Button(
        parent, text=text, command=command, bg=bg, fg=fg,
        activebackground=bg, activeforeground=fg, relief="flat", bd=0,
        padx=14, pady=8, cursor="hand2", font=FONT_BOLD, **kw,
    )


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Voice Recorder")
        self.geometry("1020x790")
        self.minsize(960, 720)
        self.configure(bg=BG)

        self.rec = Recorder()
        self.player = Player()
        self.current_path = None
        self.disp_level = 0.0
        self.was_playing = False
        self.play_name = ""
        self._applying = False

        self._setup_style()
        self._build()
        self._load_devices()
        self._load_eq_settings()
        self.refresh_list()
        self.draw_rec_button()
        self.tick()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    # ---------------------------------------------------------------- stile ---
    def _setup_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview", background=PANEL2, fieldbackground=PANEL2,
                        foreground=FG, rowheight=28, borderwidth=0, font=FONT)
        style.map("Treeview", background=[("selected", ACCENT)],
                  foreground=[("selected", "white")])
        style.configure("Treeview.Heading", background=PANEL, foreground=MUTED,
                        relief="flat", font=FONT_BOLD)
        style.map("Treeview.Heading", background=[("active", PANEL)])
        style.configure("Vertical.TScrollbar", background=PANEL2, troughcolor=PANEL,
                        bordercolor=PANEL, arrowcolor=MUTED)
        style.configure("TCombobox", fieldbackground=PANEL2, background=PANEL2,
                        foreground=FG, arrowcolor=FG, bordercolor=PANEL2,
                        lightcolor=PANEL2, darkcolor=PANEL2)
        style.map("TCombobox",
                  fieldbackground=[("readonly", PANEL2), ("disabled", PANEL)],
                  foreground=[("disabled", MUTED)],
                  selectbackground=[("readonly", PANEL2)],
                  selectforeground=[("readonly", FG)])
        self.option_add("*TCombobox*Listbox.background", PANEL2)
        self.option_add("*TCombobox*Listbox.foreground", FG)
        self.option_add("*TCombobox*Listbox.selectBackground", ACCENT)

    # ------------------------------------------------------------- layout ---
    def _build(self):
        # pannello equalizzatore a destra, recorder a sinistra
        right = tk.Frame(self, bg=PANEL, width=340)
        right.pack_propagate(False)
        right.pack(side="right", fill="y", padx=(0, 20), pady=18)
        self._build_eq(right)

        left = tk.Frame(self, bg=BG)
        left.pack(side="left", fill="both", expand=True)
        self._build_recorder(left)

    def _build_recorder(self, parent):
        pad = {"padx": 20}

        tk.Label(parent, text="🎙  Voice Recorder", bg=BG, fg=FG,
                 font=FONT_TITLE).pack(anchor="w", pady=(18, 8), **pad)

        # --- pannello impostazioni
        settings = tk.Frame(parent, bg=PANEL)
        settings.pack(fill="x", pady=(0, 10), **pad)

        tk.Label(settings, text="Nome registrazione", bg=PANEL, fg=MUTED,
                 font=FONT).pack(anchor="w", padx=14, pady=(12, 2))
        self.name_var = tk.StringVar(value="registrazione")
        self.name_entry = tk.Entry(
            settings, textvariable=self.name_var, bg=PANEL2, fg=FG,
            insertbackground=FG, relief="flat", font=("Segoe UI", 12),
            disabledbackground=PANEL, disabledforeground=MUTED,
            highlightthickness=1, highlightbackground=PANEL2, highlightcolor=ACCENT,
        )
        self.name_entry.pack(fill="x", padx=14, ipady=6)

        self.preview_var = tk.StringVar()
        tk.Label(settings, textvariable=self.preview_var, bg=PANEL, fg=MUTED,
                 font=("Segoe UI", 9), wraplength=460, justify="left",
                 anchor="w").pack(fill="x", padx=14, pady=(4, 8))

        tk.Label(settings, text="Microfono", bg=PANEL, fg=MUTED,
                 font=FONT).pack(anchor="w", padx=14, pady=(0, 2))
        self.dev_combo = ttk.Combobox(settings, state="readonly", font=FONT)
        self.dev_combo.pack(fill="x", padx=14, pady=(0, 14), ipady=3)

        # --- display del player
        display = tk.Frame(parent, bg=PANEL)
        display.pack(fill="x", pady=(0, 10), **pad)

        self.time_var = tk.StringVar(value="00:00:00")
        tk.Label(display, textvariable=self.time_var, bg=PANEL, fg=FG,
                 font=FONT_TIMER).pack(pady=(14, 0))

        self.status_var = tk.StringVar(value="Pronto a registrare")
        tk.Label(display, textvariable=self.status_var, bg=PANEL, fg=MUTED,
                 font=FONT, wraplength=460).pack(pady=(0, 8))

        self.meter = tk.Canvas(display, height=10, bg=PANEL2, highlightthickness=0)
        self.meter.pack(fill="x", padx=24, pady=(0, 14))

        controls = tk.Frame(display, bg=PANEL)
        controls.pack(pady=(0, 18))

        self.rec_canvas = tk.Canvas(controls, width=88, height=88, bg=PANEL,
                                    highlightthickness=0, cursor="hand2")
        self.rec_canvas.grid(row=0, column=0, padx=(0, 18))
        self.rec_canvas.bind("<Button-1>", lambda e: self.toggle_record())

        self.pause_btn = make_button(controls, "⏸  Pausa", self.toggle_pause)
        self.pause_btn.grid(row=0, column=1)
        self.pause_btn.config(state="disabled")

        # --- lista registrazioni
        head = tk.Frame(parent, bg=BG)
        head.pack(fill="x", **pad)
        tk.Label(head, text="Le tue registrazioni", bg=BG, fg=FG,
                 font=FONT_BOLD).pack(side="left")

        list_frame = tk.Frame(parent, bg=PANEL2)
        list_frame.pack(fill="both", expand=True, pady=(6, 8), **pad)

        self.tree = ttk.Treeview(list_frame, columns=("nome", "data", "ora"),
                                 show="headings", selectmode="browse")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("data", text="Data")
        self.tree.heading("ora", text="Ora")
        self.tree.column("nome", width=220, anchor="w")
        self.tree.column("data", width=100, anchor="center")
        self.tree.column("ora", width=90, anchor="center")
        sb = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        self.tree.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        self.tree.bind("<Double-1>", lambda e: self.play_selected())

        self.play_var = tk.StringVar(value="")
        tk.Label(parent, textvariable=self.play_var, bg=BG, fg=ACCENT,
                 font=FONT, anchor="w").pack(fill="x", **pad)

        actions = tk.Frame(parent, bg=BG)
        actions.pack(fill="x", pady=(4, 18), **pad)
        make_button(actions, "▶  Riproduci", self.play_selected,
                    bg=ACCENT, fg="white").pack(side="left", padx=(0, 6))
        make_button(actions, "■  Stop", self.stop_playback).pack(side="left", padx=6)
        make_button(actions, "📂  Cartella", self.open_folder).pack(side="left", padx=6)
        make_button(actions, "🗑  Elimina", self.delete_selected).pack(side="right")

    # ------------------------------------------------------------ equalizzatore ---
    def _build_eq(self, parent):
        tk.Label(parent, text="🎚  Equalizzatore", bg=PANEL, fg=FG,
                 font=("Segoe UI", 13, "bold")).pack(anchor="w", padx=16, pady=(16, 2))
        tk.Label(parent, text="Regola il suono in ingresso. Le modifiche valgono subito, "
                              "anche durante la registrazione.",
                 bg=PANEL, fg=MUTED, font=("Segoe UI", 9), wraplength=300,
                 justify="left").pack(anchor="w", padx=16, pady=(0, 12))

        tk.Label(parent, text="Preset", bg=PANEL, fg=MUTED,
                 font=FONT).pack(anchor="w", padx=16)
        self.preset_combo = ttk.Combobox(parent, state="readonly", font=FONT,
                                         values=list(PRESETS))
        self.preset_combo.pack(fill="x", padx=16, pady=(2, 12), ipady=3)
        self.preset_combo.bind("<<ComboboxSelected>>",
                               lambda e: self.apply_preset(self.preset_combo.get()))

        # volume ingresso
        row = tk.Frame(parent, bg=PANEL)
        row.pack(fill="x", padx=16)
        tk.Label(row, text="Volume ingresso", bg=PANEL, fg=MUTED, font=FONT).pack(side="left")
        self.gain_label = tk.Label(row, text="+0 dB", bg=PANEL, fg=ACCENT, font=FONT_BOLD)
        self.gain_label.pack(side="right")
        self.gain_scale = tk.Scale(
            parent, from_=-10, to=30, orient="horizontal", resolution=1, showvalue=False,
            command=self._on_gain, bg=PANEL, fg=FG, troughcolor=PANEL2,
            activebackground=ACCENT, highlightthickness=0, bd=0, sliderrelief="flat",
            sliderlength=22, width=16,
        )
        self.gain_scale.pack(fill="x", padx=16, pady=(2, 8))
        self.gain_scale.bind("<Double-Button-1>", lambda e: self.gain_scale.set(0))

        self.agc_var = tk.BooleanVar(value=False)
        tk.Checkbutton(
            parent, text="Auto-livello (alza le voci basse)", variable=self.agc_var,
            command=self._on_agc, bg=PANEL, fg=FG, selectcolor=PANEL2,
            activebackground=PANEL, activeforeground=FG, font=FONT,
            highlightthickness=0, bd=0, cursor="hand2",
        ).pack(anchor="w", padx=14, pady=(0, 12))

        # slider a 5 bande
        bands = tk.Frame(parent, bg=PANEL)
        bands.pack(fill="x", padx=10)
        self.band_scales, self.band_labels = [], []
        for i, (_, name) in enumerate(BANDS):
            col = tk.Frame(bands, bg=PANEL)
            col.pack(side="left", expand=True, fill="y")
            lbl = tk.Label(col, text="+0", bg=PANEL, fg=ACCENT, font=FONT_BOLD)
            lbl.pack()
            sc = tk.Scale(
                col, from_=12, to=-12, orient="vertical", resolution=1, showvalue=False,
                length=190, width=16, sliderlength=22, command=lambda v, i=i: self._on_band(i, v),
                bg=PANEL, troughcolor=PANEL2, activebackground=ACCENT,
                highlightthickness=0, bd=0, sliderrelief="flat",
            )
            sc.pack()
            sc.bind("<Double-Button-1>", lambda e, sc=sc: sc.set(0))
            tk.Label(col, text=name, bg=PANEL, fg=MUTED, font=("Segoe UI", 9)).pack(pady=(2, 0))
            self.band_scales.append(sc)
            self.band_labels.append(lbl)

        tk.Label(parent, text="Suggerimento: per prof lontani alza il volume e attiva "
                              "l'auto-livello. Doppio clic su uno slider = zero.",
                 bg=PANEL, fg=MUTED, font=("Segoe UI", 9), wraplength=300,
                 justify="left").pack(anchor="w", padx=16, pady=(12, 8))
        make_button(parent, "↺  Reset", lambda: self.apply_preset("Piatto")).pack(
            anchor="w", padx=16, pady=(0, 14))

    def _on_gain(self, value):
        self.gain_label.config(text=f"{float(value):+.0f} dB")
        if not self._applying:
            self.rec.dsp.set_gain(float(value))
            self.preset_combo.set("Personalizzato")

    def _on_band(self, i, value):
        self.band_labels[i].config(text=f"{float(value):+.0f}")
        if not self._applying:
            self.rec.dsp.set_bands([float(s.get()) for s in self.band_scales])
            self.preset_combo.set("Personalizzato")

    def _on_agc(self):
        self.rec.dsp.set_agc(self.agc_var.get())
        self.preset_combo.set("Personalizzato")

    def _sync_dsp(self):
        self.rec.dsp.set_gain(float(self.gain_scale.get()))
        self.rec.dsp.set_bands([float(s.get()) for s in self.band_scales])
        self.rec.dsp.set_agc(self.agc_var.get())

    def apply_preset(self, name):
        p = PRESETS[name]
        self._applying = True
        self.gain_scale.set(p["gain"])
        for sc, g in zip(self.band_scales, p["bands"]):
            sc.set(g)
        self.agc_var.set(p["agc"])
        self._applying = False
        self._sync_dsp()
        self.preset_combo.set(name)

    def _load_eq_settings(self):
        saved = load_settings()
        try:
            self._applying = True
            self.gain_scale.set(saved["gain"])
            for sc, g in zip(self.band_scales, saved["bands"]):
                sc.set(g)
            self.agc_var.set(bool(saved["agc"]))
            self._applying = False
            self._sync_dsp()
            self.preset_combo.set(saved.get("preset", "Personalizzato"))
        except (KeyError, TypeError, IndexError, tk.TclError):
            self._applying = False
            self.apply_preset(DEFAULT_PRESET)

    def _save_eq_settings(self):
        save_settings({
            "gain": float(self.gain_scale.get()),
            "bands": [float(s.get()) for s in self.band_scales],
            "agc": bool(self.agc_var.get()),
            "preset": self.preset_combo.get(),
        })

    # ------------------------------------------------------------ dispositivi ---
    def _load_devices(self):
        self.devices = [(None, 44100)]  # (indice, sample rate)
        names = ["Microfono predefinito"]
        try:
            devs = sd.query_devices()
            default_in = sd.default.device[0]
            hostapi = None
            if default_in is not None and default_in >= 0:
                hostapi = devs[default_in]["hostapi"]
                self.devices[0] = (None, int(devs[default_in]["default_samplerate"]))
            for i, d in enumerate(devs):
                if d["max_input_channels"] > 0 and (hostapi is None or d["hostapi"] == hostapi):
                    names.append(d["name"])
                    self.devices.append((i, int(d["default_samplerate"])))
        except Exception:
            pass
        self.dev_combo["values"] = names
        self.dev_combo.current(0)

    # ------------------------------------------------------------ registrazione ---
    def toggle_record(self):
        if self.rec.recording:
            self.stop_recording()
        else:
            self.start_recording()

    def start_recording(self):
        self.stop_playback()
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        path = unique_path(OUTPUT_DIR / build_filename(self.name_var.get(), datetime.now()))
        device, rate = self.devices[self.dev_combo.current()]
        self._sync_dsp()
        try:
            self.rec.start(path, device, rate)
        except Exception as e:
            messagebox.showerror("Errore", f"Impossibile avviare la registrazione:\n{e}")
            return
        self._save_eq_settings()
        self.current_path = path
        self.name_entry.config(state="disabled")
        self.dev_combo.config(state="disabled")
        self.pause_btn.config(state="normal", text="⏸  Pausa")
        self.status_var.set(f"● Registrazione in corso\n{path.name}")
        self.draw_rec_button()

    def stop_recording(self):
        self.rec.stop()
        self.name_entry.config(state="normal")
        self.dev_combo.config(state="readonly")
        self.pause_btn.config(state="disabled", text="⏸  Pausa")
        self.draw_rec_button()
        if self.rec.error:
            self.status_var.set("Errore durante il salvataggio")
            messagebox.showerror("Errore", self.rec.error)
        else:
            self.status_var.set(f"Salvato: {self.current_path.name}")
        self.refresh_list(select=self.current_path.name if self.current_path else None)

    def toggle_pause(self):
        if not self.rec.recording:
            return
        self.rec.paused = not self.rec.paused
        if self.rec.paused:
            self.pause_btn.config(text="▶  Riprendi")
            self.status_var.set(f"⏸ In pausa\n{self.current_path.name}")
        else:
            self.pause_btn.config(text="⏸  Pausa")
            self.status_var.set(f"● Registrazione in corso\n{self.current_path.name}")

    def draw_rec_button(self):
        c = self.rec_canvas
        c.delete("all")
        c.create_oval(4, 4, 84, 84, fill=RED, outline="")
        if self.rec.recording:
            c.create_rectangle(30, 30, 58, 58, fill="white", outline="")
        else:
            c.create_oval(30, 30, 58, 58, fill="white", outline="")

    # ------------------------------------------------------------ riproduzione ---
    def selected_path(self):
        sel = self.tree.selection()
        return OUTPUT_DIR / sel[0] if sel else None

    def play_selected(self):
        if self.rec.recording:
            messagebox.showinfo("Registrazione in corso",
                                "Ferma la registrazione prima di riprodurre un file.")
            return
        path = self.selected_path()
        if path is None:
            messagebox.showinfo("Riproduci", "Seleziona una registrazione dalla lista.")
            return
        if not path.exists():
            self.refresh_list()
            return
        self.play_name = path.name
        self.player.play(path)
        self.was_playing = True

    def stop_playback(self):
        self.player.stop()

    # ------------------------------------------------------------------ lista ---
    def refresh_list(self, select=None):
        self.tree.delete(*self.tree.get_children())
        if OUTPUT_DIR.exists():
            files = sorted(OUTPUT_DIR.glob("*.mp3"),
                           key=lambda p: p.stat().st_mtime, reverse=True)
            for p in files:
                nome, data, ora = describe_file(p)
                self.tree.insert("", "end", iid=p.name, values=(nome, data, ora))
        if select and self.tree.exists(select):
            self.tree.selection_set(select)
            self.tree.see(select)

    def delete_selected(self):
        path = self.selected_path()
        if path is None:
            messagebox.showinfo("Elimina", "Seleziona una registrazione dalla lista.")
            return
        if not messagebox.askyesno("Elimina", f"Eliminare definitivamente\n{path.name}?"):
            return
        self.player.stop()
        try:
            path.unlink()
        except OSError as e:
            messagebox.showerror("Errore", f"Impossibile eliminare il file:\n{e}")
        self.refresh_list()

    def open_folder(self):
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        try:
            if sys.platform == "win32":
                os.startfile(OUTPUT_DIR)
            elif sys.platform == "darwin":
                subprocess.run(["open", str(OUTPUT_DIR)])
            else:
                subprocess.run(["xdg-open", str(OUTPUT_DIR)])
        except Exception as e:
            messagebox.showerror("Errore", f"Impossibile aprire la cartella:\n{e}")

    # --------------------------------------------------------------- aggiornamento ---
    def tick(self):
        self.after(100, self.tick)

        # timer e livello (il livello mostrato è quello DOPO equalizzatore/volume)
        if self.rec.recording:
            if self.rec.error:
                self.stop_recording()
                return
            self.time_var.set(fmt_time(self.rec.frames / self.rec.rate))
            level = self.rec.level ** 0.5  # leggera compressione per vederlo meglio
            self.preview_var.set(f"Salvataggio in:  {OUTPUT_DIR.name}/{self.current_path.name}")
        else:
            level = 0.0
            self.preview_var.set(
                "Verrà salvato come:  " + build_filename(self.name_var.get(), datetime.now())
            )

        self.disp_level = max(level, self.disp_level * 0.85)
        self._draw_meter(self.disp_level)

        # stato riproduzione
        if self.player.playing:
            self.play_var.set(f"▶  In riproduzione: {self.play_name}   {fmt_time(self.player.seconds)}")
        elif self.was_playing:
            self.was_playing = False
            self.play_var.set("")
            if self.player.error:
                messagebox.showerror("Errore riproduzione", self.player.error)

    def _draw_meter(self, level):
        w = self.meter.winfo_width()
        h = self.meter.winfo_height()
        self.meter.delete("all")
        level = min(level, 1.0)
        color = ACCENT if level < 0.6 else YELLOW if level < 0.85 else RED
        self.meter.create_rectangle(0, 0, int(w * level), h, fill=color, outline="")

    def on_close(self):
        if self.rec.recording:
            if not messagebox.askyesno("Registrazione in corso",
                                       "Fermare e salvare la registrazione ed uscire?"):
                return
            self.rec.stop()
        self.player.stop()
        self._save_eq_settings()
        self.destroy()


if __name__ == "__main__":
    App().mainloop()