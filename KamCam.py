#!/usr/bin/env python3
import subprocess
from tkinter import *
import tkinter as tk
from tkinter import messagebox

# ============ PHONE RESOLUTION (mutable, updated by Detect) ============
# Defaults for Redmi 8. Change if you have a different phone, or use
# the "Detect Phone Size" button at runtime.
phone_size = {"w": 720, "h": 1520}
# ======================================================================


def detect_phone_size():
    """Query the connected phone via adb and update phone_size."""
    try:
        out = subprocess.check_output(
            ["adb", "shell", "wm", "size"],
            stderr=subprocess.STDOUT,
            timeout=5,
        ).decode("utf-8", errors="replace")
    except FileNotFoundError:
        messagebox.showerror("Error", "adb not found. Install android-tools.")
        return
    except subprocess.TimeoutExpired:
        messagebox.showerror("Error", "adb timed out.\nIs the phone connected and USB debugging on?")
        return
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"adb failed:\n{e.output.decode(errors='replace')}")
        return

    override = None
    physical = None
    for line in out.splitlines():
        line = line.strip()
        low = line.lower()
        if low.startswith("override size:"):
            override = line.split(":", 1)[1].strip()
        elif low.startswith("physical size:"):
            physical = line.split(":", 1)[1].strip()

    chosen = override or physical
    if not chosen or "x" not in chosen:
        messagebox.showerror("Error", f"Could not parse size from:\n{out}")
        return

    try:
        w_str, h_str = chosen.split("x", 1)
        w, h = int(w_str), int(h_str)
    except ValueError:
        messagebox.showerror("Error", f"Invalid size format: {chosen}")
        return

    phone_size["w"] = w
    phone_size["h"] = h
    phone_size_label.config(text=f"Using: {w} × {h}")


def build_crop_flag():
    """Return '--crop=W:H:X:Y' or '' if no trim is set."""
    try:
        t = int(trim_top.get() or 0)
        b = int(trim_bottom.get() or 0)
        l = int(trim_left.get() or 0)
        r = int(trim_right.get() or 0)
    except ValueError:
        messagebox.showerror("Error", "Crop values must be integers.")
        return None

    if (t, b, l, r) == (0, 0, 0, 0):
        return ""

    w = phone_size["w"] - l - r
    h = phone_size["h"] - t - b
    if w <= 0 or h <= 0:
        messagebox.showerror("Error", "Crop leaves no image area.")
        return None

    return f"--crop={w}:{h}:{l}:{t}"

def _to_int(var, label):
    raw = var.get().strip()
    if not raw:
        return 0
    try:
        return int(raw)
    except ValueError:
        raise ValueError(f"{label}: '{raw}' is not a number")

def normalize_on_blur(var):
    def handler(event):
        if not var.get().strip():
            var.set("0")
    return handler


def make_numeric(var):
    def validate(new):
        return new == "" or new.isdigit()
    vcmd = (root.register(validate), "%P")
    return vcmd

def start_normal():
    crop = build_crop_flag()
    if crop is None:
        return
    try:
        cmd = ["scrcpy"]
        if hwdec_disabled_var.get():
            cmd.append("--hwdec=disabled")
        if crop:
            cmd.append(crop)
        subprocess.Popen(cmd)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start scrcpy:\n{e}")

def start_webcam():
    crop = build_crop_flag()
    if crop is None:
        return
    try:
        hwdec_flag = "--hwdec=disabled " if hwdec_disabled_var.get() else ""
        crop_flag = f"{crop} " if crop else ""
        cmd = (
            "if ! lsmod | grep -q v4l2loopback; then "
            "  pkexec modprobe v4l2loopback exclusive_caps=1 card_label='KamCam Virtual Webcam'; "
            "fi; "
            f"scrcpy {hwdec_flag}{crop_flag}--max-size=1280 --turn-screen-off "
            f"--v4l2-sink=/dev/video0 --no-playback"
        )
        subprocess.Popen(["bash", "-c", cmd])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start webcam stream:\n{e}")

def toggle_hwdec():
    hwdec_disabled_var.set(not hwdec_disabled_var.get())
    update_toggle_ui()

def update_toggle_ui():
    if hwdec_disabled_var.get():
        btn_toggle.config(
            text="⚡ HW Decoding: DISABLED (CPU Mode)", 
            bg="#f38ba8", 
            activebackground="#f5e0dc"
        )
    else:
        btn_toggle.config(
            text="⚡ HW Decoding: ENABLED (GPU Mode)", 
            bg="#a6e3a1", 
            activebackground="#b4befe"
        )

# App Setup
root = tk.Tk()
root.title("KamCam")
root.geometry("400x500")
root.configure(bg="#1e1e2e")
root.resizable(False, False)

# Title Label
title = tk.Label(root, text="📷 KamCam Controls", font=("Cantarell", 14, "bold"), fg="#cdd6f4", bg="#1e1e2e")
title.pack(pady=10)

# --- Detect phone size ---
detect_frame = tk.Frame(root, bg="#1e1e2e")
detect_frame.pack(fill="x", padx=25, pady=(6, 2))

btn_detect = tk.Button(
    detect_frame,
    text="🔍  Detect Phone Size",
    command=detect_phone_size,
    bg="#94e2d5",
    fg="#11111b",
    font=("Cantarell", 10, "bold"),
    relief="flat",
    activebackground="#b4befe",
    cursor="hand2",
    anchor="w",
)
btn_detect.pack(side="left")

phone_size_label = tk.Label(
    detect_frame,
    text=f"Using: {phone_size['w']} × {phone_size['h']}",
    fg="#a6adc8",
    bg="#1e1e2e",
    font=("Cantarell", 9),
)
phone_size_label.pack(side="left", padx=(10, 0))

# Toggle State (True = --hwdec=disabled)
hwdec_disabled_var = tk.BooleanVar(value=True)

# Toggle Button
btn_toggle = tk.Button(
    root, 
    command=toggle_hwdec, 
    font=("Cantarell", 10, "bold"), 
    fg="#11111b", 
    relief="flat", 
    cursor="hand2",
)
btn_toggle.pack(anchor="w", padx=25, ipadx=40, pady=(30, 12), ipady=4)
update_toggle_ui()

# Phone Size Fields
# --- Crop fields ---
trim_frame = tk.Frame(root, bg="#1e1e2e")
trim_frame.pack(fill="x", padx=25, pady=6)

trim_top    = tk.StringVar(value="0")
trim_bottom = tk.StringVar(value="0")
trim_left   = tk.StringVar(value="0")
trim_right  = tk.StringVar(value="0")

fields = [
    ("Trim Top",    trim_top),
    ("Trim Bottom", trim_bottom),
    ("Trim Left",   trim_left),
    ("Trim Right",  trim_right),
]

for i, (label, var) in enumerate(fields):
    row, col = divmod(i, 2)

    tk.Label(trim_frame, text=label, fg="#cdd6f4", bg="#1e1e2e",
             font=("Cantarell", 10)).grid(
        row=row, column=col * 2, sticky="w", padx=(0, 6), pady=2)

    entry = tk.Entry(trim_frame, textvariable=var, width=6)
    entry.grid(row=row, column=col * 2 + 1, sticky="w", padx=(0, 20), pady=2)
    entry.bind("<FocusOut>", normalize_on_blur(var))

# Button: Normal Window Stream
btn_normal = tk.Button(
    root, 
    text="🖥️  Start Window Stream", 
    command=start_normal, 
    bg="#89b4fa", 
    fg="#11111b", 
    font=("Cantarell", 10, "bold"), 
    relief="flat", 
    activebackground="#b4befe", 
    cursor="hand2"
)
btn_normal.pack(anchor="w", padx=25, ipadx=85, pady=(30, 12), ipady=4)

# Button: Virtual Webcam Stream
btn_webcam = tk.Button(
    root, 
    text="📹  Start Virtual Webcam (/dev/video0)", 
    command=start_webcam, 
    bg="#cba6f7", 
    fg="#11111b", 
    font=("Cantarell", 10, "bold"), 
    relief="flat", 
    activebackground="#f5e0dc", 
    cursor="hand2"
)
btn_webcam.pack(anchor="w", padx=25, ipadx=40, pady=(30, 12), ipady=4)

root.mainloop()