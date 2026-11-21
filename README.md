# KamCam 1.0.0

## Use your Android phone as a Windows camera

KamCam streams live video and microphone audio from an Android phone to the Windows controls. Preview the feed, change the front or rear camera, adjust resolution and zoom, and send video to three separate Windows cameras: **KamCam 1**, **KamCam 2**, and **KamCam 3**. One Windows instance can connect and switch between up to three phones.

The Android app supports **Android 5.0 (API 21) and later**. The native virtual cameras require **Windows 11**.

## Choose how to use KamCam on Windows

Download the APK and Windows ZIP from the [latest GitHub release](https://github.com/xardbazz/KamCam/releases/latest). The ZIP is the portable option. The setup program is the local installation option.

### Local installation (recommended)

1. Download and open **KamCamSetup-v1.0.0.exe**.
2. Accept the administrator prompt.
3. Leave **KamCam virtual cameras** selected to register the three Windows cameras. Uncheck it if you only want the desktop controls and preview.
4. Finish setup. Launch KamCam from the Start menu or desktop shortcut. Uninstall later from **Settings → Apps → Installed apps → KamCam**.

The installer copies KamCam under Program Files, creates shortcuts, and can register the camera devices. Administrator access is required.

### Portable ZIP

1. Download **KamCam-v1.0.0-Windows.zip** and extract it to a folder you can write to, such as Documents or a USB drive.
2. Open the extracted folder, then run **KamCam\\KamCam.exe**. No local app installation is needed.
3. The preview and desktop controls work from the extracted folder. To add the Windows virtual cameras, open an Administrator PowerShell in the extracted **Camera** folder and run **Set-ExecutionPolicy -Scope Process Bypass**, then **.\\Install-KamCamCamera.ps1**.
4. To remove the cameras, run **.\\Install-KamCamCamera.ps1 -Uninstall** from the same Administrator PowerShell. You can then remove the extracted folder.

## Install and pair the phone

1. Install **app-release.apk** on the phone. If Android asks, allow installation from the app used to open the APK.
2. Open KamCam and allow camera, microphone, and local network access when asked. Keep the app open while connecting.
3. Connect the phone and PC to the same local Wi-Fi. The phone's IPv4 address appears in the KamCam app.
4. Tap **Pair with PC** on the phone to show its setup code.
5. Enter the phone's IPv4 address and code in the Windows app, then click **Connect Wi-Fi**.
6. The first successful connection trusts the phone on this Windows account. Later, select it under **Saved phone** and click **Connect saved**. Use **Forget** to remove saved trust.

### Connect by USB

Install Android SDK Platform-Tools (ADB) using Android Studio's **SDK Manager → SDK Tools → Android SDK Platform-Tools**. On the phone, enable Developer options and **USB debugging**, connect the cable, unlock the phone, and accept its USB authorization prompt. Open KamCam on the phone and tap **Pair with PC**. In Windows KamCam, click **Refresh**, select the phone under **USB phone**, enter the code the first time, and click **Connect USB**.

USB debugging is needed for USB transport and optional screen sharing. It is not required for Wi-Fi.

## Start video and switch phones

1. Select a connected phone under **Connected phones**. This selects which phone the preview and controls use.
2. Click **Start camera**. Choose front or rear camera, resolution, zoom, and the available camera controls. Keep the phone awake with KamCam open.
3. In the Windows app, select **KamCam 1**, **KamCam 2**, or **KamCam 3** as the camera output.
4. In Zoom, Teams, OBS, or another video app, select that same numbered KamCam camera. If the video app was already open during installation, close and reopen it so it refreshes its camera list.

Each connected phone has a camera slot. Select the active phone in KamCam and the matching numbered camera in your video app.

## Audio and screen sharing

- Phone microphone audio can be sent to a chosen Windows playback device using **Phone mic to output / virtual cable**. Use **Refresh audio** to rescan.
- This version routes phone audio to playback outputs; it does not create a Windows microphone input device.
- **Start screen share** uses optional scrcpy. Install [scrcpy for Windows](https://github.com/Genymobile/scrcpy/releases) and place its files in a folder named **scrcpy** inside the app's **KamCam** folder (next to KamCam.exe). USB debugging and phone authorization are required. Camera streaming does not require scrcpy.

## Requirements and connection security

- Windows 11 is required for native virtual cameras. Preview is available without selecting a virtual camera.
- Wi-Fi requires both devices on a shared local network. Guest Wi-Fi and router client isolation may block connections.
- USB requires Android SDK Platform-Tools.
- Phone-to-PC video, audio, and control use the v3 AES-GCM protocol. Use compatible KamCam versions on both devices.
- KamCam is intended for USB or a trusted local network. Do not forward its connection port to the public internet. For different networks, use a private VPN and restrict access to your devices.

## Troubleshooting

**Wi-Fi connection fails:** Ensure both devices use the same non-guest Wi-Fi, reopen the phone app, tap **Pair with PC**, and use the current phone IPv4 address. If Windows Firewall asks, allow KamCam on private networks. Check for client isolation or third-party firewall blocks.

**USB phone is missing:** Install Platform-Tools, unlock the phone, enable USB debugging, accept the authorization prompt, then click **Refresh**. Try another cable or port if the phone only charges.

**Pairing code is rejected:** Enter the current code shown on the phone. If you reset pairing on the phone, click **Forget** in Windows and pair again.

**KamCam camera is missing:** Confirm Windows 11 and that virtual cameras were selected in setup. For the portable option, run the camera script from an Administrator PowerShell. Close and reopen video apps to refresh their device list.

**Camera is busy or will not start:** Close other camera apps, select the matching KamCam number, and reconnect the phone. If Windows still holds the device, restart Windows and retry.

**No audio:** Allow microphone permission on Android, start the camera/session, enable **Mic** in Windows KamCam, and select a Windows playback device. A separate virtual audio cable may be needed to route sound into a meeting app's mic input.

**Screen share does not start:** Check scrcpy is in the expected subfolder, USB debugging is enabled, and the phone has authorized this PC.

## Uninstall

Use **Settings → Apps → Installed apps → KamCam → Uninstall**. Close video apps first so Windows can release the virtual camera. If the camera stays locked, restart Windows and run the uninstaller again.

## Downloads

- [KamCam releases](https://github.com/xardbazz/KamCam/releases/latest)
- [Android SDK Platform-Tools](https://developer.android.com/tools/releases/platform-tools)
- [scrcpy releases](https://github.com/Genymobile/scrcpy/releases)
