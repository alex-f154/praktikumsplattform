import sys
import os
import shutil
import subprocess

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'main')))

def build_exe():
    # Pfad zum main.py-Skript
    script_path = "main.py"

    # Ausführbare Datei erstellen
    subprocess.run(["pyinstaller", "--onefile", script_path])

    # Zielverzeichnis für die ausführbare Datei
    target_dir = "."

    # Pfad zur erzeugten ausführbaren Datei
    exe_path = os.path.join("dist", os.listdir("dist")[0])

    # Kopiere die ausführbare Datei in das Zielverzeichnis
    shutil.move(exe_path, target_dir)

if __name__ == "__main__":
    build_exe()