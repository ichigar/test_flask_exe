import subprocess
import sys
import os


def run_flask_app():
    subprocess.Popen([sys.executable, 'app.py'], cwd=os.path.abspath(os.path.dirname(__file__)))


def open_default_browser():
    subprocess.Popen(['start', 'http://127.0.0.1:5000'], shell=True)
    

if __name__ == '__main__':
    run_flask_app()
    open_default_browser()
