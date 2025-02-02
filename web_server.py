# web_server.py
from flask import Flask
from threading import Thread
from config import Config

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def keep_alive():
    Thread(target=lambda: app.run(
        host='0.0.0.0',
        port=Config.PORT,
        debug=False,
        use_reloader=False
    )).start()
