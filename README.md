# KamCam

> Hello! KamCam is a Python project I've been working on.
>
> KamCam creates a virtual camera using **scrcpy** as a mainframe for
> connecting through USB to the PC. I'm still working on it, so please
> **AWAIT PROGRESS!!!**

---

## What it does

Turns your Android phone into a virtual webcam on Linux. It pipes the
phone's screen or camera feed through `scrcpy` into a `v4l2loopback`
device, which any app can then use as a normal camera — OBS, Discord,
Zoom, Firefox, anything that accepts a V4L2 input.

## Features

- Stream phone screen or camera to `/dev/video0` as a standard webcam
- Toggle hardware decoding (NVIDIA VA-API or software)
- Adjustable crop — hide status bars and phone UI from the feed
- Auto-detect phone resolution via `adb`
- Simple Tkinter GUI, no terminal required

## Requirements

- Linux with the `v4l2loopback` kernel module
- `scrcpy` 5.0 or newer
- `adb` (from `android-tools`)
- Python 3.10+ with Tkinter
- An Android phone with USB debugging enabled

Install on Arch / CachyOS:

```bash
sudo pacman -S scrcpy android-tools v4l2loopback-dkms python tk


python KamCam.py

