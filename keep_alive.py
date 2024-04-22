# Libraries
from flask import Flask, render_template
from threading import Thread

# Variables
app = Flask(__name__)

# Functions
@app.route('/')
def index():
    return "I guess the bot's running"

def run():
    app.run(
        host = '0.0.0.0',
        port = 8080
    )

def keep_alive():
    thread = Thread(target=run)
    thread.start()
