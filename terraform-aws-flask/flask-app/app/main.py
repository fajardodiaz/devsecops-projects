from flask import Flask
import socket


app = Flask(__name__)


@app.route("/")
def home():
    return {"message":"Hello World"}


@app.route("/host")
def host():
    host = socket.gethostname()
    # message = f"Hello from {host}"
    return {"message": f"Hello from {host}"}
