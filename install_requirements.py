import os
import platform
import subprocess
import sys

def install_requirements():
    system = platform.system()
    if system == 'Windows':
        requirements_file = 'requirements-windows.txt'
    else:
        requirements_file = 'requirements.txt'
    
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file])
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar pacotes: {e}")

if __name__ == "__main__":
    install_requirements()
