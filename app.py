import subprocess
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def open_default_browser():
    subprocess.Popen(['start', 'http://127.0.0.1:5000'], shell=True)
     

if __name__ == '__main__':
    app.run(debug=True)
    open_default_browser()
