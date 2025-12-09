**Prerequisites**

- allow USB Debugging on your mobile device
  
  Check for your device how to allow USB Debugging.
  Usually option can be found in Settings || Additional Settings -> Developer Settings || Developer Options.
  
- download ADB (Android Debug Bridge) on your computer
  
  https://developer.android.com/tools/releases/platform-tools - download zip dedicated for your system and unpack

**How to use**

1. Adjust variables:
   - adb_path - path to adb.exe
   - source_folder - path to directory containg photos on your mobile, note that your moblie will likely not be recognised as external disc
   - destination_folder - path to directory where you want photos to be copied
2. Run copyPhotos.py 
  
