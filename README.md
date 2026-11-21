# KamCam 1.0.0

## Turn an Android phone into a Windows camera

KamCam sends live video and microphone audio from an Android phone to a Windows PC. Use the desktop controls to preview the feed, switch between up to three connected phones, select the front or rear camera, adjust resolution and zoom, and route video to one of three separately named Windows cameras:

- **KamCam 1**
- **KamCam 2**
- **KamCam 3**

The Android app supports **Android 5.0 (API 21) and later**. The native virtual cameras require **Windows 11**.

## Install KamCam

1. Download **KamCamSetup-v1.0.0.exe** and **app-release.apk** from [GitHub Releases](https://github.com/xardbazz/KamCam/releases/latest).
2. Run the Windows installer and accept the administrator prompt. Keep **KamCam virtual cameras** selected to register KamCam 1, 2, and 3.
3. Install the APK on your phone, open KamCam, and allow camera, microphone, and local network access.
4. Connect the phone and PC to the same Wi-Fi network. On the phone, tap **Pair with PC**. Its IPv4 address and one-time setup code appear in the app.
5. Enter the address and code in Windows KamCam, then click **Connect Wi-Fi**.
6. In Windows KamCam, select the phone under **Connected phones**, then click **Start camera**.
7. Choose a KamCam numbered camera in the Windows controls. In Zoom, Teams, OBS, or another video app, select the matching **KamCam 1**, **KamCam 2**, or **KamCam 3** camera. Restart the video app if it was open during installation.

The first successful pairing saves trust on that Windows account. Later, select the phone under **Saved phone** and use **Connect saved**. Use **Forget** to remove saved trust.

## Connect over USB

USB is useful when Wi-Fi is unavailable. Install Android SDK Platform-Tools (ADB) using Android Studio's **SDK Manager → SDK Tools → Android SDK Platform-Tools**. On the phone, enable Developer options and **USB debugging**, connect the cable, and accept the USB authorization prompt. Open KamCam and tap **Pair with PC**. In the Windows app, click **Refresh**, select the phone under **USB phone**, enter its setup code the first time, and click **Connect USB**.

USB debugging is required for USB transport and screen sharing. Wi-Fi connection does not require USB debugging.

## Use several phones

One Windows KamCam window supports up to three connected phones. Each connected phone has its own camera slot. Select a phone under **Connected phones** to switch which phone the preview and controls affect. Select the corresponding numbered KamCam device in the video app to use its feed.

## Audio and screen sharing

- Phone microphone audio can be sent to a selected Windows playback device through **Phone mic to output / virtual cable**. Use **Refresh audio** to rescan playback devices.
- This version routes audio to playback outputs; it does not create a Windows microphone input device.
- **Start screen share** uses the optional scrcpy tool. Install [scrcpy for Windows](https://github.com/Genymobile/scrcpy/releases), put its files in a folder named scrcpy beside the KamCam app files, and connect an authorized USB-debugging phone. Phone camera streaming works without scrcpy.

## Requirements and limitations

- Windows 11 is required for KamCam's native virtual cameras. The preview can be used without selecting a virtual camera.
- Wi-Fi connection works on a shared local network. Guest Wi-Fi or router client isolation may block the phone and PC from seeing each other.
- USB connection requires Android SDK Platform-Tools. Get them through Android Studio's SDK Manager.
- Leave the phone app open and the phone awake while streaming.
- KamCam is intended for USB or a trusted local network. Do not forward its connection port directly to the public internet. For connections between separate networks, use a private VPN with access limited to your devices.
- Phone-to-PC video, audio, and control records use the v3 AES-GCM protocol. Use compatible KamCam versions on both devices.

## Troubleshooting

**Wi-Fi connection fails:** Check that both devices are on the same non-guest Wi-Fi network, tap **Pair with PC** again, and use the current IPv4 address shown on the phone. If Windows Firewall prompts, allow KamCam on private networks. Do not expose it to public networks.

**USB phone is missing:** Install Platform-Tools, unlock the phone, enable USB debugging, accept the authorization prompt, and click **Refresh**. Try another cable or USB port if the phone only charges.

**Pairing code is rejected:** Keep the phone app open on the pairing screen and enter the current code. If you reset pairing on the phone, use **Forget** in Windows and pair again.

**KamCam camera is missing:** Confirm Windows 11 and that **KamCam virtual cameras** was selected in setup. Run the installer again as administrator. Close and reopen video apps so they refresh their camera list.

**Camera is busy or fails to start:** Close other camera apps, select the correct KamCam numbered device, then reconnect the phone. If Windows still holds the camera, restart Windows and retry.

**No audio:** Allow microphone permission on Android, start the camera/session, enable **Mic** in Windows KamCam, and select a Windows playback device. To feed a meeting app's mic input, a separate virtual audio cable may be needed; KamCam does not install one.

**Screen sharing fails:** Check that scrcpy is in the expected folder, USB debugging is enabled, and the phone has authorized this PC.

## Uninstall

Use **Settings → Apps → Installed apps → KamCam → Uninstall**. Close video apps first so Windows can release the virtual camera. If the camera stays locked, restart Windows and run the uninstaller again.

## Downloads

- [Latest KamCam release](https://github.com/xardbazz/KamCam/releases/latest)
- [Android Platform-Tools](https://developer.android.com/tools/releases/platform-tools)
- [scrcpy releases](https://github.com/Genymobile/scrcpy/releases)
