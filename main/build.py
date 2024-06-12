import os
import shutil
import subprocess
import sys
import shutil

def build_exe():
    # Pfad zum main.py-Skript
    script_path = "main.py"

    # Find the pyinstaller executable from the current environment
    pyinstaller_path = shutil.which("pyinstaller")
    if pyinstaller_path is None:
        print("PyInstaller is not installed or not found in the PATH.")
        sys.exit(1)

    # Ausführbare Datei erstellen
    print("building...")
    subprocess.run([
        pyinstaller_path,
        script_path,
        "--collect-all", "backend",
        "--paths", ".",  # Add the current directory to the search path
    ])
    print("build finished")

    # # Zielverzeichnis für die ausführbare Datei
    # target_dir = "."

    # # Pfad zur erzeugten ausführbaren Datei
    # exe_path = os.path.join("dist", os.listdir("dist")[0])
    # print("build generated in " + exe_path)

    # # Kopiere die ausführbare Datei in das Zielverzeichnis
    # shutil.move(exe_path, target_dir)
    # print("build moved to " + target_dir)

if __name__ == "__main__":
    build_exe()
