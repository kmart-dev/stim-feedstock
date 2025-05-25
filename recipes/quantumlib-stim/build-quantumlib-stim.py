import platform
import subprocess

if platform.system() == "Windows":
    subprocess.run(["cmd.exe", "/c", "pip install . --no-deps --ignore-installed"])
else:
    subprocess.run(["bash", "-c", "pip install . --no-deps --ignore-installed"])

