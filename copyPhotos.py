import subprocess
from pathlib import Path

# Full path to adb.exe (adjust if your folder is different)
adb_path = r"C:\platform-tools\adb.exe"

# Path on the phone (Camera folder)
source_folder = "/storage/emulated/0/DCIM/Camera/"

# Path on your external drive (adjust drive letter and folder name)
destination_folder = Path(r"E:\PythonTransferredPhotos")

# Make sure destination folder exists
destination_folder.mkdir(parents=True, exist_ok=True)

# List files in the phone's Camera folder
result = subprocess.run([adb_path, "shell", "ls", source_folder],
                        capture_output=True, text=True)

files = result.stdout.splitlines()

# Copy each file from phone to external drive
for f in files:
    phone_path = source_folder + f
    local_path = destination_folder / f
    print(f"Copying {f}...")
    subprocess.run([adb_path, "pull", phone_path, str(local_path)])

print("✅ Copy complete! All files have been transferred.")
