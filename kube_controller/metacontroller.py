from flask import Flask, url_for
app = Flask(__name__)


@app.route('/')
def index(): 
    pass


def run_controller():
    app.run(host='0.0.0.0', port=8080)
