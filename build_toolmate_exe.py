import os
import subprocess
import sys

REPO_URL = "https://github.com/eliranwong/toolmate.git"
REPO_DIR = "toolmate"


def run(cmd, cwd=None):
    print(f"Running: {' '.join(cmd)}")
    subprocess.check_call(cmd, cwd=cwd)


def clone_repo():
    if not os.path.exists(REPO_DIR):
        run(["git", "clone", REPO_URL, REPO_DIR])
    else:
        print("Repository already cloned")


def install_requirements():
    req_file = os.path.join(REPO_DIR, "package", "toolmate", "requirements.txt")
    run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    run([sys.executable, "-m", "pip", "install", "-r", req_file])
    run([sys.executable, "-m", "pip", "install", "pyinstaller"])


def build_exe():
    main_py = os.path.join(REPO_DIR, "package", "toolmate", "main.py")
    run(["pyinstaller", "--onefile", "--name", "toolmate", main_py])
    exe_path = os.path.join("dist", "toolmate.exe")
    target = os.path.join(os.getcwd(), "toolmate.exe")
    if os.path.isfile(exe_path):
        os.replace(exe_path, target)
        print(f"Executable created: {target}")
    else:
        print("pyinstaller did not produce expected executable")

def run_agentmake_setup():
    try:
        run([sys.executable, "-m", "agentmake", "-m"])
    except Exception:
        print("Skipping agentmake setup step")


def main():
    clone_repo()
    install_requirements()
    build_exe()
    run_agentmake_setup()


if __name__ == "__main__":
    main()
